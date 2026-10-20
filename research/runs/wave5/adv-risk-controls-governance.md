# Advisory / risk-controls / governance: deep dive

Run date: 2026-10-20. Wave 5. Archetype `advisory`, module `risk-controls`, angle `governance` (what constrains and measures the work).

Conventions: refs follow `PUBLISHER-SHORT-YYYY` and reuse the landscape's refs where the document is the same (`COSO-GENAI-2026`, `FRC-GENAI-2026`, `KPMG-AIFINANCE-2026`, `CPAPA-AGENTSCLOSE-2026`, `GT-EAS-2026`, `GT-CBIZ-2026`, `PCAOB-GENAI-2024`, `CB-FIELDGUIDE-2026`, `APRIO-FIELDGUIDE-2026`, `STANFORD-JAR-2026`, `IIA-AIKC-2026`, `AICPA-AUDITAID-2026`). `access: full` means the page or PDF was opened and read in this run. Quotations are under 25 words. All figures are as reported by the named source; provenance is marked on each outcome.

---

## 1. Summary

**What the evidence shows.** For risk and controls advisory, the governance picture is dense on *rules and frameworks* and thin on *measured results*. Of 20 candidate use cases, none reaches grade A: no firm or client has published a tracked quality metric (error rate, override rate, parallel-run result) for AI used in internal audit (IA), SOX or enterprise risk work. The best independent measurements come from adjacent work (bookkeeping, legal research, consulting tasks, finance-analyst questions) and cap those entries at B.

**Six findings.**

1. **A control framework for client AI now exists, and the profession is using it.** COSO published *Achieving Effective Internal Control Over Generative AI* on 2026-02-23. It adapts the 2013 five components and 17 principles, adds eight capability types, a six-step roadmap and starter metrics (COSO-GENAI-2026, pp. 4, 18-19). KPMG's SOX paper (2026-09-24) points to it as the anchor for AI governance inside ICFR (KPMG-SOX2030-2026).
2. **Regulators and professional bodies say the same thing: the human stays accountable, and the firm needs documented controls over its own AI.** FRC (2026-03-30), PCAOB staff (2024-07), AICPA (practice aid 2026-10-13; ethics article 2026-08-05), ABA Formal Opinion 512 (2024-07-29), Texas Opinion 705 (2025-02) and the SRA warning notice (2026-08-18) converge on competence, confidentiality, supervision and verification. None sets a numeric quality threshold.
3. **Client-side demand is real but readiness is low.** KPMG's survey of 1,013 senior finance leaders reports active AI use in finance rose from 30% to 75%, yet only 29% track where AI adoption fails (KPMG-AIFINANCE-2026). Only 17.7% of 2,000+ webinar respondents report a formal AI program or broad adoption in internal audit (CPAPA-IAPOLL-2026; self-selected, not representative).
4. **Attest and non-attest lines constrain what a firm can sell.** SEC Rule 2-01(c)(4) bars internal audit outsourcing and certain systems-design services for SEC audit clients unless the results will not be subject to audit procedures (SEC-REGSX2-01-2026). The AICPA says developing or hosting an AI system for an attest client can raise independence concerns (JOFA-ETHICS-2026). AI assurance (AIUC-1, SOC 2) is attest work and goes to the assurance archetype.
5. **Quality evidence is mostly cautionary.** The independent measures found are: legal AI research tools hallucinated 17% to 33% of the time (STANFORD-LEGALAI-2024); consultants using GPT-4 were 19% less likely to produce correct solutions on a task outside the AI frontier (HBS-JAGGED-2023); the best model scored 64.37% on a 537-question finance-analyst benchmark (VALS-FAB-2026); and accountants who followed AI suggestions on uncertain transactions risked adding errors (STANFORD-JAR-2026; MITSLOAN-CHOIXIE-2025). No parallel-run or inspection result for AI in IA or SOX work was found.
6. **Where firms report results, they are vendor-published.** The one figure from a named IA team is Reddit's: 175 controls, more than 40% of SOX scope, 60% less testing time per control in three months, published in the vendor's press release (OPTRO-CRX-2026). KPMG expects the first wave of AI-related material weaknesses in 2027 (KPMG-SOX2030-2026), which makes controls advisory a forward-looking demand story.

**Coverage.** 49 sources opened across professional bodies, regulators, standard-setters, firms, vendors, academic work, surveys and press (counts in section 5). Several primary sources were blocked (ABA, SRA, PCAOB project page, Wolters Kluwer) and reached through mirrors or secondary reports; each case is marked.

---

## 2. Use cases

```yaml
- id: advisory-risk-controls-01
  title: COSO-aligned design and gap assessment of a client's generative-AI internal controls
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Clients, including private middle-market companies, are deploying AI in finance faster than they are documenting how it is
    controlled. In KPMG's survey, active AI use in finance rose from 30% to 75% while fewer than half of organisations were
    fully assurance-ready (KPMG-AIFINANCE-2026). COSO notes that GenAI can be confidently wrong, shifts with vendor updates, and
    can start as unsanctioned "shadow AI" (COSO-GENAI-2026, p. 5).
  solution: >-
    The advisor uses COSO's GenAI publication as the assessment frame: classify each client AI use by one of eight capability
    types, assess risk against the five COSO components, map preventive, detective and corrective controls, and set starter
    metrics (COSO-GENAI-2026, pp. 7, 18-19). COSO notes that GenAI can itself help govern GenAI, for example cross-checking
    outputs across independent models (COSO-GENAI-2026, p. 8). The deliverable is a control matrix and remediation plan, not
    assurance. Pattern is `other`: structured framework application by an advisor, with AI as a drafting aid only.
  outcomes:
    - lever: risk
      description: Share of surveyed finance leaders whose organisations are fully assurance-ready for AI-enabled finance processes (demand indicator, not a result of this service)
      figure: "42%"
      measures: >-
        Release text: "Fewer than half of organizations (42 percent) are fully assurance-ready"; n=1,013 C-suite and senior finance
        leaders at organisations with annual revenue of at least US$250M (US$500M in the US), online survey March 2026; Technology
        and Financial Services are 58% of the sample. The same release uses 42% for a different measure (scaling confidence of
        assurance-ready organisations, against 14%).
      provenance: vendor-published
      source_ref: KPMG-AIFINANCE-2026
    - lever: growth
      description: Grant Thornton Advisors' CEO said AI is already driving demand for AI governance work and predicted that demand will grow
      figure: none published
      measures: Executive statement in an interview; no engagement count or revenue figure given
      provenance: self-reported
      source_ref: GT-CBIZ-2026
  prerequisites:
    - A client inventory of AI uses with named owners (COSO-GENAI-2026, p. 19)
    - A client acceptable-use policy and a cross-functional governance forum (COSO-GENAI-2026, pp. 9-10, 18)
  risks_and_guardrails:
    - COSO adapts the 2013 framework rather than creating a new one, and is guidance, not a rule (COSO-GENAIPR-2026, p. 1)
    - Where the firm also audits the client, designing or hosting an AI system for that client can raise independence concerns under the AICPA Code (JOFA-ETHICS-2026)
    - For SEC audit clients, Rule 2-01(c)(4)(ii) restricts designing or implementing a system that generates information significant to the financial statements unless the results will not be subject to audit procedures (SEC-REGSX2-01-2026)
    - Advice must not be framed as assurance over the client's AI; that is attest work (see Routed section)
  human_checkpoints:
    - Partner review of the risk assessment and control matrix before release
    - Client control owner confirms each control is operated, not only designed
  role_evolution: >-
    COSO names external auditors and internal audit among its readers and assigns each GenAI tool a named owner with
    authority and accountability (COSO-GENAI-2026, pp. 4, 10). Advisors take on control design for AI as a distinct skill beside
    classic ICFR work; KPMG says AI governance should be integrated into existing ICFR infrastructure rather than run as a
    separate workstream (KPMG-SOX2030-2026, POV 1).
  evidence_grade: C
  sources:
    - { ref: "COSO-GENAI-2026", title: "Achieving Effective Internal Control Over Generative AI (GenAI)", publisher: "COSO", type: "standard-setter", url: "https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf", date: "2026-02-23", access: "full", locator: "Executive summary p. 4; Scope p. 5; Figure 3 p. 7; foundational characteristics p. 8; roadmap pp. 18-19" }
    - { ref: "COSO-GENAIPR-2026", title: "COSO Releases Practical Roadmap for Managing Generative AI Risks and Controls (press release)", publisher: "COSO", type: "standard-setter", url: "https://www.coso.org/_files/ugd/719ba0_e08afa6e8d7940cd9ae18d0c25b2cb55.pdf", date: "2026-02-23", access: "full", locator: "p. 1, paragraphs 1-6" }
    - { ref: "KPMG-AIFINANCE-2026", title: "AI adoption in finance doubles, but assurance readiness determines who wins, KPMG finds", publisher: "KPMG International", type: "firm", url: "https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html", date: "2026-05-11", access: "full", locator: "Key findings; 'Assurance readiness powers AI performance'; 'About' box" }
    - { ref: "GT-CBIZ-2026", title: "Grant Thornton CEO Says CBIZ Merger Is Key to Unlocking AI Value", publisher: "Bloomberg Law", type: "press", url: "https://news.bloomberglaw.com/financial-accounting/grant-thornton-ceo-says-cbiz-merger-is-key-to-unlocking-ai-value", date: "2026-09-02", access: "full", locator: "Paragraphs on AI governance demand (read via r.jina.ai mirror)" }
    - { ref: "JOFA-ETHICS-2026", title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division staff)", type: "professional-body", url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: "full", locator: "Paragraph on AI-related nonattest services for attest clients" }
    - { ref: "SEC-REGSX2-01-2026", title: "17 CFR 210.2-01 Qualifications of accountants, paragraph (c)(4) non-audit services", publisher: "SEC (text via Cornell LII)", type: "regulator", url: "https://www.law.cornell.edu/cfr/text/17/210.2-01", date: "2026-10-20", access: "full", locator: "(c)(4)(ii) and (c)(4)(v); date is the access date of the current CFR text" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: Grant Thornton Advisors is the non-attest entity of an alternative practice structure (GT-EAS-2026, About box);
    New Mountain Capital ownership is from the landscape (GT-GTAP-2026), not re-opened here. COSO's press release lists the eighth
    capability type as regulatory intelligence while the document names it knowledge retrieval and summarization. Two of the five
    COSO authors work at EY and Meta (COSO-GENAI-2026, p. 1). No firm was found publishing a delivered COSO-GenAI engagement.

- id: advisory-risk-controls-02
  title: Agent inventory, named owners and replayable evidence for a client's finance agents (idea)
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Close and reconciliation agents are reaching production (BlackLine, FloQast, Microsoft and Workday products named), and an
    academic commentator says finance teams are deploying faster than they are documenting (CPAPA-AGENTSCLOSE-2026). KPMG's survey
    found only 29% of organisations track where AI adoption fails (KPMG-AIFINANCE-2026).
  solution: >-
    Before an agent touches a production close, the advisor helps the client put five controls in writing: an agent inventory with
    a named control owner; evidence a reviewer can replay (inputs, steps, exceptions, basis for each match); human sign-off gates
    scaled to risk; read-through of third-party assurance; and monitoring with an exit threshold (CPAPA-AGENTSCLOSE-2026). This
    matches COSO roadmap steps 2 and 6 (inventory; monitor and adapt) (COSO-GENAI-2026, pp. 18-19).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: No firm or client result found; the source is a practitioner checklist
      provenance: self-reported
      source_ref: CPAPA-AGENTSCLOSE-2026
  prerequisites:
    - Client willingness to run a validation period on its own data; the article calls vendor match-rate and time-saving claims marketing figures until the client's data reproduces them (CPAPA-AGENTSCLOSE-2026)
  risks_and_guardrails:
    - Sign-off gates must be written into the close checklist with names, or review becomes assumed rather than performed (CPAPA-AGENTSCLOSE-2026)
    - The article cites Deloitte Australia's 2025 refund as a warning that unreviewed AI output is a professional liability (CPAPA-AGENTSCLOSE-2026; see use case 17)
  human_checkpoints:
    - Controller signs the one-page control memo
    - Named human owns each agent's output; a person is authorised to pull the agent
  role_evolution: >-
    The article says CAS and controllership firms can hand clients this checklist and that auditors will ask the same questions
    (CPAPA-AGENTSCLOSE-2026). Control ownership shifts to named finance staff per agent (COSO-GENAI-2026, p. 10).
  evidence_grade: D
  sources:
    - { ref: "CPAPA-AGENTSCLOSE-2026", title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: "CPA Practice Advisor (author: Anthony L. Fulmore Sr., Texas A&M University Central Texas)", type: "press", url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: "2026-08-13", access: "full", locator: "Five numbered controls; paragraph 4 on SOC" }
    - { ref: "KPMG-AIFINANCE-2026", title: "AI adoption in finance doubles, but assurance readiness determines who wins, KPMG finds", publisher: "KPMG International", type: "firm", url: "https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html", date: "2026-05-11", access: "full", locator: "'Assurance readiness powers AI performance', second paragraph" }
    - { ref: "COSO-GENAI-2026", title: "Achieving Effective Internal Control Over Generative AI (GenAI)", publisher: "COSO", type: "standard-setter", url: "https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf", date: "2026-02-23", access: "full", locator: "Roadmap steps 2 and 6, pp. 18-19; Control Environment p. 10" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea: the checklist is a commentator's, not a firm's. Firm type: not applicable (no firm named). The article's statement that
    the AICPA had not yet published SOC guidance on AI predates AICPA TQA section 9561 (reported 2026-09-21; see use case 11).
    The 42% 'fully assurance ready' figure that the article quotes appears in the KPMG release's body text.

- id: advisory-risk-controls-03
  title: Internal-audit review of a client's AI governance using the IIA AI Auditing Framework and board questionnaires
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Boards and audit committees ask whether the company's AI is governed, and internal audit functions are early in their own AI
    use: 17.7% of 2,000+ webinar respondents reported a formal AI program or broad adoption (CPAPA-IAPOLL-2026), and 76% of
    respondents to a 2024 Internal Audit Foundation survey rated themselves novice or beginner in GenAI (IIAF-RIDDLE-2024).
  solution: >-
    Outsourced or co-sourced IA teams use The IIA's AI Auditing Framework (issued 2024-09-13) and its practitioner checklist to
    assess AI strategy, governance maturity and AI-related risks (IIA-AIFW-2024). In June 2026 the IIA issued templates including
    an audit-committee questionnaire on IA's AI coverage and a board AI-governance questionnaire (IIA-IPPF-2026). Protiviti's
    'AI in Motion' document suite, listed on the IIA site from 2026-09-18, covers reading AI outputs skeptically, GenAI internal
    controls and vibe-coding risks; contents are members-only and were not read (IIA-IPPF-2026).
  outcomes:
    - lever: risk
      description: Webinar poll on the most important next step for IA functions
      figure: "35.1%"
      measures: >-
        Respondents who prioritised establishing AI governance and acceptable-use guidance as their most important next step, among
        2,078 to 2,327 attendees answering each question at the 2026-10-06 Wolters Kluwer TeamMate webinar; the publisher says
        results are not a representative survey
      provenance: vendor-published
      source_ref: CPAPA-IAPOLL-2026
  prerequisites:
    - IA charter and skills that cover AI risk (the IIA ships a free AI certificate and a prompts guide; IIA-AIKC-2026)
    - Client management willing to supply an AI inventory
  risks_and_guardrails:
    - The framework emphasises reasonable assurance given AI's complexity and evolving nature (IIA-AIFW-2024)
    - Internal audit outsourcing for an SEC audit client is restricted unless the results will not be subject to audit procedures (SEC-REGSX2-01-2026, (c)(4)(v)); the AICPA's rules for non-SEC audit clients were not read
  human_checkpoints:
    - IA lead approves scope and rating of findings
    - Audit committee receives the results
  role_evolution: >-
    KPMG describes AI as becoming the subject of the audit as well as a tool, and expects ICFR programs to extend their perimeter
    to AI systems (KPMG-SOX2030-2026, POV 1).
  evidence_grade: C
  sources:
    - { ref: "IIA-AIFW-2024", title: "AI Auditing Framework", publisher: "The IIA", type: "professional-body", url: "https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/", date: "2024-09-13", access: "full", locator: "Page summary; practitioner's guide; reasonable-assurance paragraph. Issue date from the IPPF listing" }
    - { ref: "IIA-IPPF-2026", title: "IPPF documents listing, topic Artificial Intelligence", publisher: "The IIA", type: "professional-body", url: "https://www.theiia.org/en/standards/documents/", date: "2026-09-18", access: "full", locator: "AI-topic entries: templates issued 2026-06-16; prompts guide 2026-08-18; Protiviti suite 2026-09-18 (date is the latest listed item)" }
    - { ref: "IIA-AIKC-2026", title: "IIA AI Knowledge Center: New Tools for Internal Auditors", publisher: "IIA Belgium", type: "professional-body", url: "https://www.iiabelgium.org/news-publications/iia-ai-knowledge-center-new-tools-for-internal-auditors", date: "2026-08", access: "full", locator: "Sections 'New AI Framework Support Tools' and 'AI Prompting for Internal Auditors'; month taken from the page's reference to the August 2026 prompts guide" }
    - { ref: "CPAPA-IAPOLL-2026", title: "Internal Auditors Eye Broader AI Use", publisher: "CPA Practice Advisor (reporting Wolters Kluwer TeamMate poll)", type: "survey", url: "https://www.cpapracticeadvisor.com/?p=191508", date: "2026-10-12", access: "full", locator: "Paragraphs 2-3 and 'About the polling' note" }
    - { ref: "IIAF-RIDDLE-2024", title: "Solving the riddle: Harnessing Generative AI for internal audit activities", publisher: "Internal Audit Foundation and Wolters Kluwer TeamMate", type: "survey", url: "https://www.theiia.org/en/content/research/foundation/2024/solving-the-riddle-harnessing-generative-ai-for-internal-audit-activities/", date: "2024", access: "full", locator: "Key findings, third bullet; year from the URL path, month not shown" }
    - { ref: "KPMG-SOX2030-2026", title: "The Future of SOX: A point of view for 2030 and beyond", publisher: "KPMG LLP", type: "firm", url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: "2026-09-24", access: "full", locator: "POV 1: The governance of AI" }
    - { ref: "SEC-REGSX2-01-2026", title: "17 CFR 210.2-01 Qualifications of accountants, paragraph (c)(4) non-audit services", publisher: "SEC (text via Cornell LII)", type: "regulator", url: "https://www.law.cornell.edu/cfr/text/17/210.2-01", date: "2026-10-20", access: "full", locator: "(c)(4)(v); date is the access date" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: Protiviti is a consulting firm (not an accounting firm); its documents are listed by the IIA but their content is
    members-only. The IIA lists the framework as issued 2024-09-13; other sources date it 2023 (landscape). The IIA templates and
    the Protiviti suite show product availability, not engagements delivered.

- id: advisory-risk-controls-04
  title: Agentic SOX control testing with full-population coverage and human review of exceptions
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    SOX testing is heavy and getting heavier. KPMG's 2025 SOX Survey excerpts report that the cost of maintaining SOX controls rose
    45% between its 2023 and 2025 surveys, average testing hours per control rose from 12 (FY2022) to 16 (FY2024), and 52% of IA
    departments spent more than 40% of their hours on SOX in FY2024 (KPMG-SOX2030-2026, Introduction).
  solution: >-
    An agentic testing engine runs control tests across a population, with auditors handling exceptions and judgment. Optro
    reports that its engine now extends beyond SOX to operational audit testing and that evidence collection will follow
    (OPTRO-CRX-2026). KPMG's April 2026 poll found AI in SOX, controls and IA functions is mostly at pilot stage (KPMG-FUTURESOX-2026, p. 5).
  outcomes:
    - lever: speed
      description: Reddit's internal audit team automated controls in its first three months on the vendor's Autonomous Testing
      figure: "175 controls; more than 40% of SOX scope"
      measures: Number of controls automated, and their share of the team's SOX scope, in the first three months, as stated in the vendor's launch release
      provenance: vendor-published
      source_ref: OPTRO-CRX-2026
    - lever: speed
      description: Average reduction in testing time per control for the same team
      figure: "60%"
      measures: Average reduction in testing time per control, per the vendor's release (baseline and method not stated)
      provenance: vendor-published
      source_ref: OPTRO-CRX-2026
    - lever: capacity
      description: Reddit has since expanded agentic testing to more than 75% of its SOX controls and to other recurring testing programs
      figure: "over 75% of SOX controls"
      measures: Share of Reddit's SOX controls under agentic testing, per the vendor's release; date of measurement not stated
      provenance: vendor-published
      source_ref: OPTRO-CRX-2026
  prerequisites:
    - Controls documented and evidence reachable by the tool; KPMG says continuous testing cannot happen without continuous evidence collection (KPMG-SOX2030-2026, POV 3)
    - A validation period against the team's past conclusions (see use case 06)
  risks_and_guardrails:
    - Full-population coverage surfaces more exceptions, so follow-up capacity must rise (CPAPA-FULLPOP-2026)
    - Marketing of full testing must not imply certainty; an audit gives reasonable, not absolute, assurance (CPAPA-FULLPOP-2026)
    - Vendor-reported results; no independent measurement of test accuracy or false-exception rate found
  human_checkpoints:
    - Auditor reviews every exception and every conclusion that feeds a deficiency evaluation
  role_evolution: >-
    Optro says auditors get time back for judgment-based work (OPTRO-CRX-2026). KPMG's SOX leader says the concept of auditor
    reliance on management testing will go away and the role becomes more of a controls adviser (KPMG-FUTURESOX-2026, p. 7).
  evidence_grade: B
  sources:
    - { ref: "OPTRO-CRX-2026", title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: "Optro (via CPA Practice Advisor)", type: "vendor", url: "https://www.cpapracticeadvisor.com/2026/10/14/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance/191695/", date: "2026-10-14", access: "full", locator: "'Autonomous Testing' paragraph" }
    - { ref: "KPMG-SOX2030-2026", title: "The Future of SOX: A point of view for 2030 and beyond", publisher: "KPMG LLP", type: "firm", url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: "2026-09-24", access: "full", locator: "Introduction, '2025 SOX Survey excerpts' (p. 4); POV 3" }
    - { ref: "KPMG-FUTURESOX-2026", title: "Revolutionizing internal controls: Insights from an April 2026 KPMG Future of SOX webcast", publisher: "KPMG LLP", type: "firm", url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/revolutionizing-internal-controls.pdf", date: "2026-05-20", access: "full", locator: "pp. 2-3, 5, 7 (date is the PDF creation date; the webcast was in April 2026)" }
    - { ref: "CPAPA-FULLPOP-2026", title: "Testing Every Transaction Changes the Audit - Here's What Firms Should Know Before They Sell It", publisher: "CPA Practice Advisor (author: Tunde Adewole, Ledgerline)", type: "press", url: "https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/", date: "2026-10-15", access: "full", locator: "Paragraphs on exceptions and the expectation gap" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: vendor (Optro). Reddit, Klaviyo and FJ Management are in-house IA teams, not outsourced providers; no co-sourced or
    outsourced-provider figure was found. The Ledgerline article comes from an employee-benefit-plan audit firm (attest side) and is
    used here only for the expectation-gap point. Independence: for an SEC audit client, a firm cannot take IA outsourcing that
    relates to internal accounting controls unless the results will not be subject to audit procedures (SEC-REGSX2-01-2026).

- id: advisory-risk-controls-05
  title: Mid-market firm delivers IA, SOC and risk advisory on an agentic platform with vendor-certified governance
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, document-production, coordination-scheduling]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: >-
    Firms want one methodology and one evidence trail across audit, internal audit and SOC work, and want to show regulators and
    clients that agent output is traceable and overseen by people.
  solution: >-
    Cherry Bekaert (a top-20 firm) announced on 2026-06-03 that it selected Fieldguide as strategic AI partner, building on an
    existing deployment in its Risk and Cybersecurity practice, and that it will centralise planning, testing, review and
    reporting for Financial Audit, Internal Audit and SOC on the platform (CB-FIELDGUIDE-2026). Aprio (described as the 20th
    largest US advisory and accounting firm) says it standardised SOC, ISO, HITRUST and PCI engagements on Fieldguide in December
    2025 across Risk Advisory Services and is now co-developing role-specific agents, with human oversight at every stage
    (APRIO-FIELDGUIDE-2026).
  outcomes:
    - lever: quality
      description: none published; both releases describe intended benefits (traceability, consistent methodology, more time with clients)
      figure: none published
      measures: No tracked metric reported by either firm
      provenance: self-reported
      source_ref: CB-FIELDGUIDE-2026
  prerequisites:
    - Firm methodology configured into the platform; Aprio says its professionals are configuring Fieldguide to their own engagement methodology (APRIO-FIELDGUIDE-2026)
    - Vendor governance evidence; Cherry Bekaert's release says Fieldguide claims AIUC-1 certification and ISO 42001 (vendor claim, not verified here; CB-FIELDGUIDE-2026)
  risks_and_guardrails:
    - Aprio states every workflow is built to comply with AICPA, PCAOB and GAAS standards (firm statement; APRIO-FIELDGUIDE-2026)
    - The FRC guidance asks firms to certify an AI tool per use case, test it, monitor it and recertify after material changes (FRC-GENAIGUIDE-2026, pp. 32-33)
  human_checkpoints:
    - Human oversight at each stage of the lifecycle (CB-FIELDGUIDE-2026; APRIO-FIELDGUIDE-2026)
  role_evolution: >-
    Aprio says staff spend more time on interpretation and advice as AI handles preparation, data validation and documentation
    (APRIO-FIELDGUIDE-2026). Fieldguide's CEO links the shift to a shrinking CPA pipeline (vendor claim; CB-FIELDGUIDE-2026).
  evidence_grade: B
  sources:
    - { ref: "CB-FIELDGUIDE-2026", title: "Cherry Bekaert Expands AI Audit With Fieldguide", publisher: "Cherry Bekaert", type: "firm", url: "https://www.cbh.com/newsroom/cherry-bekaert-expands-ai-audit-with-fieldguide/", date: "2026-06-03", access: "full", locator: "Paragraphs 1-4" }
    - { ref: "APRIO-FIELDGUIDE-2026", title: "Aprio and Fieldguide Co-Build the Future of Audit with Agentic AI", publisher: "CPA Practice Advisor", type: "press", url: "https://www.cpapracticeadvisor.com/?p=188025", date: "2026-08-05", access: "full", locator: "Paragraphs 1-3 and final timeline paragraph" }
    - { ref: "FRC-GENAIGUIDE-2026", title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "UK Financial Reporting Council", type: "regulator", url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03", access: "full", locator: "pp. 32-33 (certification, recertification, monitoring, limited deployment)" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: both are top-100 mid-market firms. The platform is also used for financial audit and SOC examinations, which are
    attest work (assurance archetype); the advisory slice is internal audit and non-attest risk advisory. For the same client,
    internal audit outsourcing is restricted if the firm audits an SEC registrant (SEC-REGSX2-01-2026). The FRC guidance is
    aimed at audit firms' central technical teams (FRC-GENAIGUIDE-2026, p. 4) and is used here as a model, not a binding rule for US advisory.

- id: advisory-risk-controls-06
  title: Pre-use certification and parallel run of AI testing tools against completed engagements (idea)
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    No public parallel-run or error-rate result exists for AI in internal audit or SOX testing, so firms and clients cannot yet
    compare an AI tool's conclusions with their own.
  solution: >-
    Run the tool in shadow mode on engagements already completed and compare its results with the team's conclusions, then ramp
    gradually (CPAPA-FULLPOP-2026). The FRC guidance describes the same controls from a regulator's side: test default, edge and
    diverse cases; recertify after material changes; and, for limited deployment, perform alternative procedures in full in
    parallel (FRC-GENAIGUIDE-2026, pp. 32-33). COSO's roadmap adds revalidating after vendor updates (COSO-GENAI-2026, p. 19).
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: No parallel-run results found in any source
      provenance: self-reported
      source_ref: CPAPA-FULLPOP-2026
  prerequisites:
    - A set of completed engagements with documented conclusions to use as the comparison baseline (CPAPA-FULLPOP-2026)
  risks_and_guardrails:
    - FRC says tolerance for deficiencies in output is a matter of professional judgement and that tests will often be qualitative (FRC-GENAIGUIDE-2026, p. 32)
    - COSO case example: a vendor OCR update degraded accuracy and the team rolled back within 24 hours; the case is illustrative, with no organisation named (COSO-GENAI-2026, p. 20)
  human_checkpoints:
    - A named reviewer compares tool output with prior conclusions before any live cutover
  role_evolution: >-
    FRC states the human auditor remains accountable regardless of the tool (FRC-GENAI-2026). Firms need staff who can design tests
    for AI output, a skill the AICPA practice aid says requires a blend of audit, AI and data expertise (CPAPA-AUDITAID-2026).
  evidence_grade: D
  sources:
    - { ref: "CPAPA-FULLPOP-2026", title: "Testing Every Transaction Changes the Audit - Here's What Firms Should Know Before They Sell It", publisher: "CPA Practice Advisor (author: Tunde Adewole, Ledgerline)", type: "press", url: "https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/", date: "2026-10-15", access: "full", locator: "Paragraphs beginning 'The worst way to adopt automation'" }
    - { ref: "FRC-GENAIGUIDE-2026", title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "UK Financial Reporting Council", type: "regulator", url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03", access: "full", locator: "pp. 32-33" }
    - { ref: "FRC-GENAI-2026", title: "Innovative new guidance supports audit firm adoption of emerging AI technologies", publisher: "UK Financial Reporting Council", type: "regulator", url: "https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/", date: "2026-03-30", access: "full", locator: "Paragraph 4 (accountability unchanged)" }
    - { ref: "COSO-GENAI-2026", title: "Achieving Effective Internal Control Over Generative AI (GenAI)", publisher: "COSO", type: "standard-setter", url: "https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf", date: "2026-02-23", access: "full", locator: "Step 6 p. 19; Case 1 p. 20" }
    - { ref: "CPAPA-AUDITAID-2026", title: "AICPA Practice Aid Provides Guidance to Auditors on AI Use in Financial Statement Audits", publisher: "CPA Practice Advisor", type: "press", url: "https://www.cpapracticeadvisor.com/?p=191588", date: "2026-10-13", access: "full", locator: "Bullet on audit team capabilities" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea: practitioners and the FRC discuss this control; no firm reports doing it with results. Firm type: not applicable. The FRC
    describes parallel procedures as something teams often perform for limited deployment; no firm is named. The FRC guidance is
    not a response to identified quality deficiencies (FRC-GENAI-2026).

- id: advisory-risk-controls-07
  title: AI-assisted risk assessment scoring and audit planning for internal audit
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [research-synthesis, expert-judgment]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Risk assessment and planning are where internal audit teams say AI could add most value, but few functions have a formal AI
    program (CPAPA-IAPOLL-2026).
  solution: >-
    AI drafts starting risk scores with supporting evidence from the team's own data, and the auditor adjusts and approves. Optro
    describes an agentic risk-assessment scoring product that recommends starting scores with evidence (OPTRO-CRX-2026). KPMG's
    poll found one third of SOX, controls and IA functions use AI mainly for research, planning, scoping and risk assessment (KPMG-FUTURESOX-2026, p. 2).
  outcomes:
    - lever: speed
      description: IA professionals who see most AI value in planning and risk assessment
      figure: "38.2%"
      measures: >-
        Respondents selecting planning and risk assessment as where AI could create the most value, among 2,078 to 2,327 attendees
        per question at the 2026-10-06 Wolters Kluwer TeamMate webinar; not a representative survey
      provenance: vendor-published
      source_ref: CPAPA-IAPOLL-2026
    - lever: capacity
      description: Leaders who primarily use AI in SOX, internal controls and IA functions for research, planning, scoping and risk assessment
      figure: "33%"
      measures: >-
        Share of leaders primarily using AI for research, planning, scoping and risk assessment, from inputs by about 3,900 audit and
        risk leaders in KPMG's April 2026 Future of SOX webcast (self-selected audience)
      provenance: vendor-published
      source_ref: KPMG-FUTURESOX-2026
  prerequisites:
    - Structured risk data in a GRC system the agent can read (OPTRO-CRX-2026)
  risks_and_guardrails:
    - Same-source scores can anchor the reviewer; the AICPA's ethics article lists anchoring bias as a risk of AI output (JOFA-ETHICS-2026)
    - Overreliance and loss of professional judgment was the top agentic-AI concern for 27.5% of poll respondents (CPAPA-IAPOLL-2026)
  human_checkpoints:
    - Auditor confirms or overrides each starting score before the plan is issued
  role_evolution: >-
    Wolters Kluwer's product lead says AI can contribute but can never inherit the auditor's accountability (CPAPA-IAPOLL-2026).
  evidence_grade: C
  sources:
    - { ref: "CPAPA-IAPOLL-2026", title: "Internal Auditors Eye Broader AI Use", publisher: "CPA Practice Advisor (reporting Wolters Kluwer TeamMate poll)", type: "survey", url: "https://www.cpapracticeadvisor.com/?p=191508", date: "2026-10-12", access: "full", locator: "Paragraphs 1, 6-8 and 'About the polling'" }
    - { ref: "KPMG-FUTURESOX-2026", title: "Revolutionizing internal controls: Insights from an April 2026 KPMG Future of SOX webcast", publisher: "KPMG LLP", type: "firm", url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/revolutionizing-internal-controls.pdf", date: "2026-05-20", access: "full", locator: "p. 2" }
    - { ref: "OPTRO-CRX-2026", title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: "Optro (via CPA Practice Advisor)", type: "vendor", url: "https://www.cpapracticeadvisor.com/2026/10/14/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance/191695/", date: "2026-10-14", access: "full", locator: "'Agentic Risk Assessment Scoring' paragraph" }
    - { ref: "JOFA-ETHICS-2026", title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division staff)", type: "professional-body", url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: "full", locator: "Paragraph on anchoring bias" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: vendor (Optro) and Big Four (KPMG) survey content. The 43.8% 'individual experimentation' figure for this poll appeared
    only in a search summary of the Wolters Kluwer release (page blocked), so it is not used in outcomes. Poll audiences are
    self-selected webinar attendees. Landscape lists BDO's Risk Assessment Coach (BDO-AI-2025); it was not re-opened here.

- id: advisory-risk-controls-08
  title: AI-assisted workpaper analysis and calibrated review inside an internal audit team
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Review of audit workpapers is a bottleneck, and reviewers need evidence of how each conclusion was reached.
  solution: >-
    The head of internal audit at FJ Management says the team uses the platform to analyze workpapers automatically, run
    calibrated reviews and log evidence in live workflows, keeping what he calls an auditable human-in-the-loop standard (OPTRO-CRX-2026).
  outcomes:
    - lever: capacity
      description: The FJ Management IA head says the tool has changed what the team can get through; no figure given
      figure: none published
      measures: Qualitative statement in a vendor release
      provenance: vendor-published
      source_ref: OPTRO-CRX-2026
  prerequisites:
    - Workpapers held in a structured, permissioned workflow (OPTRO-CRX-2026)
  risks_and_guardrails:
    - PCAOB staff report that firms expect supervisors to apply the same diligence to work done with GenAI as to other work (PCAOB-GENAI-2024, pp. 4-5)
    - Vendor claims that agents are logged, cited and audit-ready were not independently tested (OPTRO-CRX-2026)
  human_checkpoints:
    - Human reviewer signs off every reviewed workpaper
  role_evolution: >-
    PCAOB staff heard from firms that engagement team members using GenAI remain responsible for the results and documentation (PCAOB-GENAI-2024, p. 5).
  evidence_grade: B
  sources:
    - { ref: "OPTRO-CRX-2026", title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: "Optro (via CPA Practice Advisor)", type: "vendor", url: "https://www.cpapracticeadvisor.com/2026/10/14/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance/191695/", date: "2026-10-14", access: "full", locator: "Quote from Matt Sewell, FJ Management" }
    - { ref: "PCAOB-GENAI-2024", title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting", publisher: "PCAOB staff", type: "regulator", url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: "2024-07", access: "full", locator: "pp. 4-5, 'Supervision and Review of GenAI'" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: in-house IA team using a vendor platform. The PCAOB spotlight is older than the preferred window (2024-07) and
    reflects outreach mainly to larger audit firms; the staff document is not a rule. No 2025-2026 PCAOB successor was found.

- id: advisory-risk-controls-09
  title: Year-round control testing with automated evidence collection replacing point-in-time SOX cycles
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: >-
    Point-in-time testing finds issues late. KPMG says periodic assessments, manual evidence collection and sample-based testing
    are reaching their limit (KPMG-SOX2030-2026, Introduction).
  solution: >-
    Klaviyo's VP of Internal Audit and Compliance says that with the vendor's autonomous testing the team no longer bundles
    testing into a single point in time and now tests throughout the year, which surfaces issues earlier (OPTRO-CRX-2026). KPMG argues continuous testing needs
    continuous evidence collection and that automating evidence may offer a more immediate return than automating tests (KPMG-SOX2030-2026, POV 3).
  outcomes:
    - lever: quality
      description: Klaviyo says it catches issues earlier and works with control owners to fix them sooner; no figure given
      figure: none published
      measures: Qualitative statement in a vendor release
      provenance: vendor-published
      source_ref: OPTRO-CRX-2026
  prerequisites:
    - Control evidence embedded in process workflows or standard repositories that tools can read (KPMG-SOX2030-2026, POV 3)
  risks_and_guardrails:
    - KPMG notes the independence line: the first line owns monitoring and IA tests the monitoring itself (KPMG-SOX2030-2026, POV 5)
    - KPMG's SOX leader says external auditors are moving to ingesting large data sets and away from sampling, so management must be ready for that level of scrutiny (KPMG-FUTURESOX-2026, p. 7)
  human_checkpoints:
    - Control owners work exceptions; IA reviews the reliability of the monitoring
  role_evolution: >-
    KPMG expects the ICFR function to move from a point-in-time opinion on prior-year control effectiveness to a living view of
    control health (KPMG-SOX2030-2026, POV 3).
  evidence_grade: B
  sources:
    - { ref: "OPTRO-CRX-2026", title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: "Optro (via CPA Practice Advisor)", type: "vendor", url: "https://www.cpapracticeadvisor.com/2026/10/14/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance/191695/", date: "2026-10-14", access: "full", locator: "Quote from Carmen Lam, Klaviyo" }
    - { ref: "KPMG-SOX2030-2026", title: "The Future of SOX: A point of view for 2030 and beyond", publisher: "KPMG LLP", type: "firm", url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: "2026-09-24", access: "full", locator: "Introduction; POV 3 'Automating evidence collection'; POV 5" }
    - { ref: "KPMG-FUTURESOX-2026", title: "Revolutionizing internal controls: Insights from an April 2026 KPMG Future of SOX webcast", publisher: "KPMG LLP", type: "firm", url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/revolutionizing-internal-controls.pdf", date: "2026-05-20", access: "full", locator: "p. 7, Sue King quote" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: in-house IA team (Klaviyo) on a vendor platform; Big Four commentary (KPMG). Independence: when a firm that audits an
    SEC client also tests that client's controls as IA outsourcing, Rule 2-01(c)(4)(v) applies (SEC-REGSX2-01-2026).

- id: advisory-risk-controls-10
  title: AI-system readiness advisory ahead of AIUC-1 certification, SOC 2 and ISO 42001 (non-attest side)
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Enterprise buyers ask AI vendors and AI-using clients for independent proof that agents behave as intended. The AICPA release
    says AI misfires in critical operations have raised safety and security concerns (JOFA-AIUC-2026).
  solution: >-
    Firms advise clients on gaps against a certifiable standard before examination. Grant Thornton launched an Enterprise Assurance
    Services practice on 2026-09-23 that includes provisional accreditation to support AIUC-1 certification of agentic AI controls
    (GT-EAS-2026). On 2026-10-19 the AICPA and the Artificial Intelligence Underwriting Company announced a joint offering that
    pairs a SOC 2 report with AIUC-1 certification in one CPA-led engagement; multiple CPA firms are already delivering it, and a
    full launch is expected in early 2027 (JOFA-AIUC-2026).
  outcomes:
    - lever: growth
      description: none published; announcements describe a new service line, not results
      figure: none published
      measures: No engagement counts or revenue reported by Grant Thornton or the AICPA
      provenance: self-reported
      source_ref: GT-EAS-2026
  prerequisites:
    - Client AI agents in scope with documented controls; AIUC-1 requires quarterly technical retesting and annual renewal (JOFA-AIUC-2026)
  risks_and_guardrails:
    - The examination itself is attest work and belongs to the assurance archetype; readiness advice to a client the same firm will examine raises independence questions that were not confirmed in this run
    - A Cloud Security Alliance note (AI-assisted, not reviewed by CSA) says two AI companies can hold clean SOC 2 reports with different tested control sets because no AI baseline exists (CSA-SOC2AI-2026, Key Takeaways)
  human_checkpoints:
    - Licensed CPA leads the examination (JOFA-AIUC-2026)
  role_evolution: >-
    Grant Thornton's new practice groups SOC, benefit plan, sustainability and AI assurance staff in one dedicated organisation
    rather than splitting them across service lines (GT-EAS-2026).
  evidence_grade: C
  sources:
    - { ref: "GT-EAS-2026", title: "Grant Thornton launches first-of-its-kind Enterprise Assurance Services practice", publisher: "Grant Thornton LLP", type: "firm", url: "https://www.grantthornton.com/insights/press-releases/2026/september/gt-launches-first-of-its-kind-enterprise-assurance-services", date: "2026-09-23", access: "full", locator: "Paragraphs 1-3; offerings list; About box" }
    - { ref: "JOFA-AIUC-2026", title: "AICPA partners on new offering that assures AI systems and agents", publisher: "Journal of Accountancy (AICPA & CIMA)", type: "professional-body", url: "https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/", date: "2026-10-19", access: "full", locator: "Paragraphs 1-2, 6-7" }
    - { ref: "CSA-SOC2AI-2026", title: "The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted", publisher: "Cloud Security Alliance (CSAI Foundation)", type: "community", url: "https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/08/CSA_research_note_soc2_ai_controls_gap_20260830-csa-styled.pdf", date: "2026-08-30", access: "full", locator: "Key Takeaways; Security Analysis" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: Grant Thornton LLP is the licensed attest firm of an alternative practice structure (GT-EAS-2026, About box); the
    non-attest entity is Grant Thornton Advisors. The CSA note says it was AI-assisted and did not go through official CSA review,
    and its claim that the AICPA had not acted predates AICPA TQA 9561 (use case 11). Primary home of this service is the assurance archetype.

- id: advisory-risk-controls-11
  title: AI-aware reading of a client's third-party assurance reports for its AI vendors
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Most agentic close tools are subservice organisations in SOC terms, and existing SOC 1 and SOC 2 reports may say little about
    model behaviour, retraining or prompt controls (CPAPA-AGENTSCLOSE-2026, control 4).
  solution: >-
    The advisor reads each vendor's SOC report for what it covers about AI components, maps gaps to contract terms,
    complementary user entity controls and the client's own validation testing, and documents that mapping (CPAPA-AGENTSCLOSE-2026,
    control 4). The AICPA released technical Q&A section 9561 on the effect of a service organisation's use of AI on SOC 1
    (AT-C 320) and SOC 2 (AT-C 205) examinations (DART-TQA9561-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: No result found
      provenance: self-reported
      source_ref: CPAPA-AGENTSCLOSE-2026
  prerequisites:
    - Client has its vendors' current SOC reports and contract terms (CPAPA-AGENTSCLOSE-2026)
  risks_and_guardrails:
    - A security-focused SOC 2 auditor population is improvising AI evidence requests such as model lineage and per-inference logging; no common baseline exists (CSA-SOC2AI-2026, Background; AI-assisted note)
    - Nothing in the TQA text was read; the Deloitte summary gives only its scope (DART-TQA9561-2026)
  human_checkpoints:
    - Advisor and client owner sign off the gap mapping
  role_evolution: >-
    Third-party risk reviewers need AI literacy beyond traditional SOC reading; the AICPA practice aid says engagement teams may
    need a blend of audit, AI, data and specialist skills (CPAPA-AUDITAID-2026).
  evidence_grade: D
  sources:
    - { ref: "CPAPA-AGENTSCLOSE-2026", title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: "CPA Practice Advisor (author: Anthony L. Fulmore Sr.)", type: "press", url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: "2026-08-13", access: "full", locator: "Control 4" }
    - { ref: "DART-TQA9561-2026", title: "AICPA Releases TQAs on a Service Organization's Use of AI", publisher: "Deloitte Accounting Research Tool (DART)", type: "firm", url: "https://dart.deloitte.com/USDART/home/news/all-news/2026/sep/aicpa-releases-tqas-service-organization-use-ai", date: "2026-09-21", access: "full", locator: "Opening paragraph" }
    - { ref: "CSA-SOC2AI-2026", title: "The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted", publisher: "Cloud Security Alliance (CSAI Foundation)", type: "community", url: "https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/08/CSA_research_note_soc2_ai_controls_gap_20260830-csa-styled.pdf", date: "2026-08-30", access: "full", locator: "Background, pp. 2-3" }
    - { ref: "CPAPA-AUDITAID-2026", title: "AICPA Practice Aid Provides Guidance to Auditors on AI Use in Financial Statement Audits", publisher: "CPA Practice Advisor", type: "press", url: "https://www.cpapracticeadvisor.com/?p=191588", date: "2026-10-13", access: "full", locator: "Bullet on audit team capabilities" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea: advised as a checklist step, not shown as a delivered service. Firm type: not applicable. The SOC examinations themselves
    are assurance work. The DART post is dated 2026-09-21; one search summary gave 2026-09-11 for the TQA release (search-only), so
    the release date is not confirmed beyond 'by 2026-09-21'.

- id: advisory-risk-controls-12
  title: Shadow-AI discovery and AI use-case inventory for a client
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [research-synthesis, data-reporting]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Staff use AI tools the organisation has not approved. A LexisNexis report says 54% of consultants admit to using AI tools
    without approval (LEXISNEXIS-CONSULTING-2026). In ISACA's European poll, 33% of organisations do not require staff to disclose when
    AI contributed to a work product, and 42% have a formal, comprehensive AI policy (ISACA-AIPULSE-2026).
  solution: >-
    The advisor surveys and scans for unsanctioned use, then builds an inventory classifying each use by capability type with an
    owner and criticality (COSO-GENAI-2026, p. 19). Optro previews an 'AI Discovery' feature to surface shadow AI enterprise-wide,
    ahead of 2027 availability (OPTRO-CRX-2026). ACCA suggests asking who is actually using AI in the business, since the answer may
    not match the list of authorised products (ACCA-ENGLETTERS-2026).
  outcomes:
    - lever: risk
      description: Share of consultants who admit using AI tools without approval
      figure: "54%"
      measures: >-
        Consultants who 'admit to using AI tools without approval' per the Management Consulting Industry Report 2026 as described on
        the vendor's landing page; sample, fieldwork date and wording not shown on the page
      provenance: vendor-published
      source_ref: LEXISNEXIS-CONSULTING-2026
  prerequisites:
    - Client mandate to scan network and SaaS use; clear acceptable-use policy (COSO-GENAI-2026, p. 9)
  risks_and_guardrails:
    - Too much control drives workarounds; a Warren Averett risk partner says to govern what people are allowed to use rather than what they cannot do (JOFA-CYBERCHECK-2026)
  human_checkpoints:
    - Governance committee classifies and approves each discovered use
  role_evolution: >-
    COSO assigns each AI use a named owner and a RACI for prompts, retrieval data and rules (COSO-GENAI-2026, p. 10).
  evidence_grade: C
  sources:
    - { ref: "LEXISNEXIS-CONSULTING-2026", title: "AI Is Accelerating Consulting and Introducing Risk (landing page for the Management Consulting Industry Report 2026)", publisher: "LexisNexis", type: "vendor", url: "https://professional.lexisnexis.com/en-us/ps-fowmini2026", date: "2026", access: "full", locator: "Second and third paragraphs; page carries no publication date, so only the year is given" }
    - { ref: "ISACA-AIPULSE-2026", title: "A Third of European Organisations Don't Know if They've Been Hit by an AI-Powered Cyberattack, New ISACA Research Finds", publisher: "ISACA", type: "survey", url: "https://www.isaca.org/about-us/newsroom/press-releases/2026/a-third-of-european-organisations-dont-know-if-they-have-been-hit-by-an-ai-powered-cyberattack", date: "2026-06-17", access: "full", locator: "Final paragraph (date from the ISACA press-release listing)" }
    - { ref: "COSO-GENAI-2026", title: "Achieving Effective Internal Control Over Generative AI (GenAI)", publisher: "COSO", type: "standard-setter", url: "https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf", date: "2026-02-23", access: "full", locator: "Step 2 p. 19; Control Environment pp. 9-10" }
    - { ref: "OPTRO-CRX-2026", title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: "Optro (via CPA Practice Advisor)", type: "vendor", url: "https://www.cpapracticeadvisor.com/2026/10/14/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance/191695/", date: "2026-10-14", access: "full", locator: "'Agentic AI Governance' paragraph" }
    - { ref: "ACCA-ENGLETTERS-2026", title: "Engagement letters, AI and PCRT", publisher: "ACCA", type: "professional-body", url: "https://www.accaglobal.com/gb/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/september/Engagement-letters-AI-and-PCRT.html", date: "2026-09", access: "full", locator: "Final paragraph (month from the URL path)" }
    - { ref: "JOFA-CYBERCHECK-2026", title: "New checklist helps CPAs manage AI cyber risks", publisher: "Journal of Accountancy (AICPA & CIMA)", type: "professional-body", url: "https://www.journalofaccountancy.com/news/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/", date: "2026-10-01", access: "full", locator: "Paragraph quoting Paul Perry" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: vendors (LexisNexis, Optro) and a Warren Averett partner (top-100 mid-market). The ISACA poll is a European
    sample; the LexisNexis figure covers consultants, not accounting firms.

- id: advisory-risk-controls-13
  title: Governance of end-user AI-built automations and agents in client finance teams (idea)
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [software-systems, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Employees can now use AI to generate code and build their own automations, dashboards and apps. A Cherry Bekaert risk
    advisory partner says this extends the developer pool to people who may not understand what happens behind the scenes
    (JOFA-CYBERCHECK-2026). COSO lists low barrier to entry as a foundational characteristic that controls must address (COSO-GENAI-2026, p. 8).
  solution: >-
    Advisors set up a review and validation process for AI-generated software, agents and automations, with ownership and change
    management before they enter the workflow, plus least-privilege access, sandboxes and human approval for higher-risk actions
    (JOFA-CYBERCHECK-2026). Protiviti's IIA-listed document on vibe-coding risks for internal audit was issued 2026-09-18 (title only;
    members-only; IIA-IPPF-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: No result found
      provenance: self-reported
      source_ref: JOFA-CYBERCHECK-2026
  prerequisites:
    - Data-classification policy and an approved-tools list (JOFA-CYBERCHECK-2026)
  risks_and_guardrails:
    - Agents with access to enterprise data, credentials or APIs open new attack paths (JOFA-CYBERCHECK-2026)
  human_checkpoints:
    - Review and change-management gate before any user-built agent touches production data
  role_evolution: >-
    Finance staff become developers of automations and therefore owners of controls over them (COSO-GENAI-2026, p. 8).
  evidence_grade: D
  sources:
    - { ref: "JOFA-CYBERCHECK-2026", title: "New checklist helps CPAs manage AI cyber risks", publisher: "Journal of Accountancy (AICPA & CIMA)", type: "professional-body", url: "https://www.journalofaccountancy.com/news/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/", date: "2026-10-01", access: "full", locator: "Paragraphs on vibe coding and agent guardrails" }
    - { ref: "COSO-GENAI-2026", title: "Achieving Effective Internal Control Over Generative AI (GenAI)", publisher: "COSO", type: "standard-setter", url: "https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf", date: "2026-02-23", access: "full", locator: "Foundational characteristic 4, p. 8" }
    - { ref: "IIA-IPPF-2026", title: "IPPF documents listing, topic Artificial Intelligence", publisher: "The IIA", type: "professional-body", url: "https://www.theiia.org/en/standards/documents/", date: "2026-09-18", access: "full", locator: "Entry 'Vibe Coding Risks & What Internal Audit Needs to Know'" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea: discussed by practitioners; no engagement result found. Firm type: Cherry Bekaert (top-20 mid-market firm) partner
    quoted as a commentator, not describing a client engagement.

- id: advisory-risk-controls-14
  title: AI incident-response playbooks and exercises for client finance and IT teams (idea)
  archetype: advisory
  module: risk-controls
  function: technology-it
  work_types: [coordination-scheduling, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    ISACA's 2026 State of Cybersecurity survey (more than 1,800 cybersecurity professionals, sponsored by Wolters Kluwer TeamMate)
    found 64% of enterprises have not run any AI-related incident response exercise, only 8% run them regularly, and 48% either do
    not know whether AI incident playbooks exist or say they do not (ISACA-STATECYBER-2026).
  solution: >-
    Advisors build AI incident playbooks (data exposure through AI systems, AI-enabled phishing and fraud, employee misuse of
    GenAI) and run tabletop exercises, drawing on the incident types ISACA's respondents named (ISACA-STATECYBER-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: The survey measures the gap, not the result of any exercise service
      provenance: independent
      source_ref: ISACA-STATECYBER-2026
  prerequisites:
    - Inventory of AI systems and owners (COSO-GENAI-2026, p. 19)
  risks_and_guardrails:
    - ISACA's survey is of cybersecurity professionals; it does not isolate private middle-market companies (ISACA-STATECYBER-2026)
  human_checkpoints:
    - Incident commander and legal approve playbooks
  role_evolution: >-
    ISACA reports 51% of respondents are now involved in developing, onboarding or implementing AI solutions (up from 40% in 2025)
    and 56% helped write an AI-use policy (ISACA-STATECYBER-2026).
  evidence_grade: D
  sources:
    - { ref: "ISACA-STATECYBER-2026", title: "Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises, ISACA Research Finds", publisher: "ISACA", type: "survey", url: "https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises", date: "2026-09-22", access: "full", locator: "Paragraphs 1-4 (date from the ISACA press-release listing)" }
    - { ref: "COSO-GENAI-2026", title: "Achieving Effective Internal Control Over Generative AI (GenAI)", publisher: "COSO", type: "standard-setter", url: "https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf", date: "2026-02-23", access: "full", locator: "Step 2, p. 19" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea: the landscape found almost no AI-specific evidence for cyber and IT risk advisory; this entry rests on a survey of the gap,
    not on a delivered service. Firm type: not applicable.

- id: advisory-risk-controls-15
  title: AI disclosure and consent clauses in engagement letters, and handling client restrictions on AI
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [document-production, client-interaction]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Clients may restrict or object to AI use, and engagement terms often lag how work is delivered. ACCA says a blanket ban may be
    impossible to meet because firms use AI behind the scenes for AML, administration and research (ACCA-ENGLETTERS-2026).
  solution: >-
    Add AI disclosure and consent wording to engagement letters. A Woodard webinar deck gives a sample clause: AI used under
    supervision of licensed professionals, outputs reviewed, no confidential client data shared with public or third-party AI
    systems without explicit written consent, and a check of IRC section 7216 for tax return data (WOODARD-ENGLETTERS-2025, sample
    clause 3). ACCA reports that the January 2026 UK PCRT update suggests disclosing AI use in the engagement letter and, where AI
    is fundamental to the work, telling the client first (ACCA-ENGLETTERS-2026). ABA Opinion 512 says lawyers must evaluate the
    risk of putting client information into AI tools and may need informed consent (ABA-FO512-2024, section II.B).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: No source reports a client acceptance or objection rate
      provenance: self-reported
      source_ref: ACCA-ENGLETTERS-2026
  prerequisites:
    - Firm AI policy and approved-tools list (JOFA-AIPOLICY-2026)
    - Legal review of the clause (JOFA-AIPOLICY-2026; WOODARD-ENGLETTERS-2025)
  risks_and_guardrails:
    - A client restriction may raise costs or mean the firm cannot act (ACCA-ENGLETTERS-2026)
    - The ABA opinion says disclosure may be unnecessary depending on the facts, so a blanket clause is not a rule-based requirement (LAWNEXT-ABA512-2024)
    - The AICPA's confidential-client-information rule (ET 1.700.001) asks members to consider consent before putting client data into AI systems (JOFA-ETHICS-2026)
  human_checkpoints:
    - Partner and counsel approve the clause; client signs
  role_evolution: >-
    Engagement partners now negotiate AI terms alongside scope and fees (ACCA-ENGLETTERS-2026).
  evidence_grade: D
  sources:
    - { ref: "WOODARD-ENGLETTERS-2025", title: "Future Ready Engagement Letters (webinar deck)", publisher: "Woodard", type: "firm", url: "https://www.woodard.com/hubfs/Future_Ready_Engagement_Letters_Oct2025.pdf", date: "2025-10", access: "full", locator: "Slides 'AICPA Guidance: AI Use & Transparency' and 'Sample clauses' item 3 (month from the file name)" }
    - { ref: "ACCA-ENGLETTERS-2026", title: "Engagement letters, AI and PCRT", publisher: "ACCA", type: "professional-body", url: "https://www.accaglobal.com/gb/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/september/Engagement-letters-AI-and-PCRT.html", date: "2026-09", access: "full", locator: "Paragraphs 2-4 and 'The first question is simple' section" }
    - { ref: "ABA-FO512-2024", title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: "ABA Standing Committee on Ethics and Professional Responsibility", type: "professional-body", url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: "2024-07-29", access: "full", locator: "Section II.B Confidentiality, pp. 6-8; II.C Communication, p. 9. Copy hosted by LawNext; the ABA URL returned 403" }
    - { ref: "LAWNEXT-ABA512-2024", title: "In First Ethics Ruling on Gen AI, ABA Says Lawyers Must Have Reasonable Understanding of the Technology, But Need Not Become Experts", publisher: "LawSites (Robert Ambrogi)", type: "press", url: "https://www.lawnext.com/2024/07/in-first-ethics-ruling-on-gen-ai-aba-says-lawyers-must-have-reasonable-understanding-of-the-technology-but-need-not-become-experts.html", date: "2024-07-30", access: "full", locator: "'Communication' paragraph" }
    - { ref: "JOFA-AIPOLICY-2026", title: "Drafting an AI policy that actually works", publisher: "Journal of Accountancy (author: Nicole L. Graham, Aon)", type: "professional-body", url: "https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works.html", date: "2026-07-01", access: "full", locator: "Paragraph on engagement-letter disclosure language" }
    - { ref: "JOFA-ETHICS-2026", title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division staff)", type: "professional-body", url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: "full", locator: "Paragraph on the Confidential Client Information Rule" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: not applicable (professional-body and consultancy templates). ACCA is a UK body; PCRT is UK tax guidance and ACCA says
    its logic applies more widely, which is ACCA's view. ABA Opinion 512 binds lawyers, not accountants; it is cited as the closest
    analogue. The Woodard deck is a copyrighted webinar slide set; the clause is a sample, not evidence of adoption.

- id: advisory-risk-controls-16
  title: Documenting AI use, verification and review in the engagement file (idea)
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    AI output can sound confident while wrong, and a client will come after the firm, not the tool, if unchecked output is relied
    on (JOFA-AIPOLICY-2026). PCAOB staff heard that supervisors are expected to apply the same diligence to work done with GenAI
    as to other work (PCAOB-GENAI-2024, p. 5).
  solution: >-
    Staff record in the client file the prompts used, how outputs were verified and who reviewed them, integrated into the firm's
    quality control system rather than handled informally (JOFA-AIPOLICY-2026). ABA Opinion 512 expects supervisory lawyers to
    establish clear policies, train and monitor compliance (LAWNEXT-ABA512-2024; ABA-FO512-2024, section II.E).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: No source reports compliance or defect rates for such documentation
      provenance: self-reported
      source_ref: JOFA-AIPOLICY-2026
  prerequisites:
    - Firm AI policy with approved tools and an AI lead or committee (JOFA-AIPOLICY-2026)
  risks_and_guardrails:
    - AI-generated research, explanations and citations should be verified against primary authoritative sources before use (JOFA-AIPOLICY-2026)
    - The AICPA ethics article says the signing professional and firm remain responsible for the work product (JOFA-ETHICS-2026)
  human_checkpoints:
    - Reviewer signs off the AI-use record in the file
  role_evolution: >-
    The signing CPA remains responsible for accuracy (JOFA-AIPOLICY-2026); PCAOB staff report firms see GenAI as augmenting, not
    replacing, humans (PCAOB-GENAI-2024, p. 4).
  evidence_grade: D
  sources:
    - { ref: "JOFA-AIPOLICY-2026", title: "Drafting an AI policy that actually works", publisher: "Journal of Accountancy (author: Nicole L. Graham, Aon)", type: "professional-body", url: "https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works.html", date: "2026-07-01", access: "full", locator: "Paragraphs beginning 'Generative AI can be confidently wrong' and 'If it isn't documented, it didn't happen'" }
    - { ref: "PCAOB-GENAI-2024", title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting", publisher: "PCAOB staff", type: "regulator", url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: "2024-07", access: "full", locator: "pp. 4-5" }
    - { ref: "ABA-FO512-2024", title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: "ABA Standing Committee on Ethics and Professional Responsibility", type: "professional-body", url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: "2024-07-29", access: "full", locator: "Section II.E Supervisory Responsibilities, pp. 10-11" }
    - { ref: "LAWNEXT-ABA512-2024", title: "In First Ethics Ruling on Gen AI, ABA Says Lawyers Must Have Reasonable Understanding of the Technology, But Need Not Become Experts", publisher: "LawSites (Robert Ambrogi)", type: "press", url: "https://www.lawnext.com/2024/07/in-first-ethics-ruling-on-gen-ai-aba-says-lawyers-must-have-reasonable-understanding-of-the-technology-but-need-not-become-experts.html", date: "2024-07-30", access: "full", locator: "'Supervisory responsibilities' paragraph" }
    - { ref: "JOFA-ETHICS-2026", title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division staff)", type: "professional-body", url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: "full", locator: "Paragraphs on competence and 'human in the loop'" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea: policy guidance, no evidence of a firm measuring this control. The Aon author is a risk consultant, not a firm
    practitioner. The PCAOB spotlight reflects mainly larger audit firms and is older than the preferred window.

- id: advisory-risk-controls-17
  title: Citation and fact-verification gate on AI-assisted advisory and review reports
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Deloitte Australia's 'independent assurance review' for the Department of Employment and Workplace Relations contained
    nonexistent references and citations, and was re-uploaded with a note that a generative AI tool chain had been used (CITYAM-DELOITTE-2025;
    STORYBOARD18-DELOITTE-2025). The SRA reported 42 reports of potential AI misuse between July 2025 and July 2026 (LEGALCHEEK-SRA-2026).
  solution: >-
    Every AI-assisted deliverable passes a verification gate: each citation, quotation and figure is checked against the primary
    source and the check is recorded, before release. ABA Opinion 512 says lawyers must review all outputs and correct errors
    before submitting materials (LAWNEXT-ABA512-2024). ACCA advises asking the tool for its source, checking it independently and
    evidencing the check on file (ACCA-ENGLETTERS-2026).
  outcomes:
    - lever: risk
      description: Deloitte Australia agreed to repay the final instalment of its contract for the review after the errors were found; the firm said the corrections did not affect the findings
      figure: "final instalment of an approximately AU$440,000 contract (Storyboard18 gives AU$439,000)"
      measures: Amount is the contract value; the size of the final instalment is not stated in the sources
      provenance: independent
      source_ref: CITYAM-DELOITTE-2025
    - lever: quality
      description: Three legal AI research tools hallucinated between 17% and 33% of the time in a preregistered evaluation
      figure: "17% to 33%"
      measures: >-
        Rate at which each of Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI hallucinated on the authors' legal
        research queries; legal domain, not accounting or advisory; v1 posted 2024-05-30
      provenance: independent
      source_ref: STANFORD-LEGALAI-2024
  prerequisites:
    - Access to primary sources and a reviewer with subject expertise
  risks_and_guardrails:
    - The SRA says firms must have effective governance, systems and controls for AI risks, and that entering confidential client information into open AI tools can waive privilege (LEGALCHEEK-SRA-2026; SRA notice itself was not opened)
    - Evidence from adjacent legal domain only; no accounting-firm hallucination rate found
  human_checkpoints:
    - Named reviewer verifies each reference before the report is issued
  role_evolution: >-
    SRA's strategy director said individuals remain responsible for work and advice whether or not AI is used (LEGALCHEEK-SRA-2026).
  evidence_grade: B
  sources:
    - { ref: "CITYAM-DELOITTE-2025", title: "Deloitte refunds Australian government after AI 'made up citations' in report", publisher: "City AM", type: "press", url: "https://www.cityam.com/?p=2367690", date: "2025-10-06", access: "full", locator: "Paragraphs 1-6" }
    - { ref: "STORYBOARD18-DELOITTE-2025", title: "Deloitte to repay Australian govt over flawed $440,000 report aided by AI", publisher: "Storyboard18", type: "press", url: "https://storyboard18.com/digital/deloitte-to-repay-australian-govt-over-flawed-440000-report-aided-by-ai-82083.htm", date: "2025-10-07", access: "full", locator: "Paragraphs 2-5" }
    - { ref: "STANFORD-LEGALAI-2024", title: "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools", publisher: "Stanford University and Yale University researchers (arXiv 2405.20362)", type: "academic", url: "https://arxiv.org/pdf/2405.20362", date: "2024-05-30", access: "full", locator: "Abstract" }
    - { ref: "LEGALCHEEK-SRA-2026", title: "SRA warns over AI misuse following rise in blunders", publisher: "Legal Cheek", type: "press", url: "https://www.legalcheek.com/2026/08/sra-warns-over-ai-misuse-following-rise-in-blunders/", date: "2026-08-18", access: "full", locator: "Paragraphs 1-3 and 6-7" }
    - { ref: "LAWNEXT-ABA512-2024", title: "In First Ethics Ruling on Gen AI, ABA Says Lawyers Must Have Reasonable Understanding of the Technology, But Need Not Become Experts", publisher: "LawSites (Robert Ambrogi)", type: "press", url: "https://www.lawnext.com/2024/07/in-first-ethics-ruling-on-gen-ai-aba-says-lawyers-must-have-reasonable-understanding-of-the-technology-but-need-not-become-experts.html", date: "2024-07-30", access: "full", locator: "Paragraph beginning 'Recognizing that issues have arisen'" }
    - { ref: "ACCA-ENGLETTERS-2026", title: "Engagement letters, AI and PCRT", publisher: "ACCA", type: "professional-body", url: "https://www.accaglobal.com/gb/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/september/Engagement-letters-AI-and-PCRT.html", date: "2026-09", access: "full", locator: "Paragraph on hallucinations" }
  last_reviewed: 2026-10-20
  notes: >-
    Firm type: Big Four (Deloitte Australia); the report was a government assurance review, not an accounting-firm advisory
    engagement in the middle market. Grade B: a named deployment with an outcome, but the control (the gate) was not measured. The
    HBS and Stanford numbers are adjacent. Search results (not opened: TechSpot, blocked) reported that 127 of 141 original
    references survive in the revised report; that figure is not used. Independence note: the SRA and ABA items bind lawyers, not
    accountants.

- id: advisory-risk-controls-18
  title: Confidence-threshold routing of AI classifications and extractions to human review
  archetype: advisory
  module: risk-controls
  function: finance-accounting
  work_types: [transaction-processing, review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Accountants working with AI suggestions face a risk of error when they follow AI recommendations on uncertain items. In a
    framed field experiment, AI assistance improved classification accuracy on average, but reliance on non-consensus AI
    recommendations can increase the risk of error (STANFORD-JAR-2026).
  solution: >-
    Set confidence thresholds so low-confidence items go to a person. In the Choi and Xie field data, accountants selectively
    intervene when AI confidence scores are low (STANFORD-JAR-2026). COSO's roadmap gives the same design for invoice extraction:
    confidence thresholds and human review for new templates, plus monthly accuracy sampling (COSO-GENAI-2026, p. 19).
  outcomes:
    - lever: capacity
      description: Time shifted from routine data entry to business communication and quality assurance in the field data
      figure: "approximately 8.5% of accountant time"
      measures: >-
        Reallocation of approximately 8.5% of accountant time from routine data entry toward higher-value tasks, per the MIT Sloan
        summary of the working-paper version; field data from an AI-enabled platform serving 79 SMEs (over 200,000 transaction-level
        records) and a survey of 277 accountants; bookkeeping context, adjacent to risk-controls work
      provenance: independent
      source_ref: MITSLOAN-CHOIXIE-2025
    - lever: quality
      description: Survey respondents worried about errors and accuracy in AI-generated reporting
      figure: "62%"
      measures: Share of the 277 surveyed accountants who were worried about errors and accuracy in AI-generated reporting, per the MIT Sloan summary
      provenance: independent
      source_ref: MITSLOAN-CHOIXIE-2025
  prerequisites:
    - The AI system exposes a usable confidence score; reviewers trained to read it (MITSLOAN-CHOIXIE-2025)
  risks_and_guardrails:
    - Accountants tended to follow AI's divergent categories for uncertain transactions, which can introduce errors (MITSLOAN-CHOIXIE-2025)
    - Threshold design and accuracy sampling need re-validation after vendor updates (COSO-GENAI-2026, p. 19)
  human_checkpoints:
    - Low-confidence items and new templates go to a named reviewer; monthly accuracy sample reviewed by a controller
  role_evolution: >-
    The authors report effort moving from data entry to communication and quality assurance, and more experienced accountants gain more
    from the AI (STANFORD-JAR-2026; MITSLOAN-CHOIXIE-2025).
  evidence_grade: B
  sources:
    - { ref: "STANFORD-JAR-2026", title: "Human + AI in Accounting: Early Evidence from the Field (Journal of Accounting Research 64(3), pp. 1333-1373)", publisher: "Stanford GSB (Choi and Xie)", type: "academic", url: "https://www.gsb.stanford.edu/index%2ephp/node/629989", date: "2026-06", access: "full", locator: "Abstract" }
    - { ref: "MITSLOAN-CHOIXIE-2025", title: "How generative AI can make accountants more productive", publisher: "MIT Sloan Ideas Made to Matter", type: "academic", url: "https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-can-make-accountants-more-productive", date: "2025-08-05", access: "full", locator: "Paragraphs 2-6" }
    - { ref: "COSO-GENAI-2026", title: "Achieving Effective Internal Control Over Generative AI (GenAI)", publisher: "COSO", type: "standard-setter", url: "https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf", date: "2026-02-23", access: "full", locator: "Step 4 example, p. 19; Case 1, p. 20" }
  last_reviewed: 2026-10-20
  notes: >-
    Grade capped at B: the measurements come from bookkeeping and small-business accounting on one vendor's platform, not from risk
    and controls advisory work. Firm type: not applicable (academic study; platform vendor not named in the sources read). The MIT
    Sloan summary describes an earlier version of the paper; figures may differ from the journal version, which was read only as an abstract.

- id: advisory-risk-controls-19
  title: Synthetic-data and agent stress-testing of controls during ERP implementations and acquisitions (idea)
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: >-
    The window between go-live and a stable, tested control environment is a high-risk period for financial reporting in system
    implementations and acquisitions (KPMG-SOX2030-2026, POV 4).
  solution: >-
    Introduce AI-generated synthetic transaction populations into the new environment, and deploy AI agents that simulate users,
    transactions and edge or adversarial events to see how access controls, approvals and rules respond before real data is at
    stake (KPMG-SOX2030-2026, POV 4).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: Firm point of view; no deployment or result reported
      provenance: vendor-published
      source_ref: KPMG-SOX2030-2026
  prerequisites:
    - Representative transaction data from which synthetic populations can be modelled (KPMG-SOX2030-2026, POV 4)
  risks_and_guardrails:
    - For SEC audit clients, designing or implementing financial information systems is restricted unless results will not be subject to audit procedures (SEC-REGSX2-01-2026, (c)(4)(ii))
  human_checkpoints:
    - Control owners review failure modes and remediation before go-live
  role_evolution: >-
    KPMG expects the ICFR function to shift from reporting control effectiveness toward guiding the first line (KPMG-SOX2030-2026, POV 5).
  evidence_grade: D
  sources:
    - { ref: "KPMG-SOX2030-2026", title: "The Future of SOX: A point of view for 2030 and beyond", publisher: "KPMG LLP", type: "firm", url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: "2026-09-24", access: "full", locator: "POV 4: AI as a guide through transformation" }
    - { ref: "SEC-REGSX2-01-2026", title: "17 CFR 210.2-01 Qualifications of accountants, paragraph (c)(4) non-audit services", publisher: "SEC (text via Cornell LII)", type: "regulator", url: "https://www.law.cornell.edu/cfr/text/17/210.2-01", date: "2026-10-20", access: "full", locator: "(c)(4)(ii); date is the access date" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea: a Big Four point of view using the word 'could'; no deployment found. Firm type: Big Four (KPMG US).

- id: advisory-risk-controls-20
  title: Disclosure-control review of a client's AI capability claims (idea)
  archetype: advisory
  module: risk-controls
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Clients that market or report AI capabilities face enforcement when claims are false. In March 2024 the SEC settled charges against
    two investment advisers for false and misleading statements about their use of AI, with $400,000 in total civil penalties (SEC-AIWASH-2024).
  solution: >-
    Review marketing, investor and filing statements about AI against how the client's systems actually work, and design controls so
    representations are supported (SEC-AIWASH-2024). The SEC's enforcement director said public issuers making AI adoption claims
    must remain vigilant about misstatements that may be material (SEC-AIWASH-2024).
  outcomes:
    - lever: risk
      description: Two investment advisers paid civil penalties in settled SEC charges over AI claims
      figure: "$400,000 total"
      measures: Combined civil penalties paid by Delphia (USA) Inc. and Global Predictions Inc. in settled charges announced 2024-03-18
      provenance: independent
      source_ref: SEC-AIWASH-2024
  prerequisites:
    - Access to the client's AI technical documentation and marketing materials
  risks_and_guardrails:
    - SEC action reported here concerns investment advisers; applicability to private middle-market clients was not researched
    - Attest clients: a review of the client's disclosures can touch the audit; independence analysis needed (not researched)
  human_checkpoints:
    - Engagement partner and client counsel review conclusions
  role_evolution: >-
    Risk advisors add technical AI claim verification to disclosure-controls work (SEC-AIWASH-2024).
  evidence_grade: D
  sources:
    - { ref: "SEC-AIWASH-2024", title: "SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of Artificial Intelligence", publisher: "SEC", type: "regulator", url: "https://www.sec.gov/newsroom/press-releases/2024-36", date: "2024-03-18", access: "full", locator: "Paragraphs 1-3" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea: the SEC release is an enforcement announcement, not a description of an advisory service. Search summaries (secondary
    law-firm blogs, not opened) report further AI-claims actions in August and September 2026; those are search-only and not used.
    Boundary: the forensic-disputes module may take AI-washing investigations.
```

---

## 3. Module notes

### 3.1 Processes and key steps, with work types

- **Internal-audit outsourcing and co-sourcing.** Risk assessment and planning (research-synthesis, expert-judgment); fieldwork and control testing (review-assurance, data-reporting); workpaper review (review-assurance); reporting (document-production); follow-up with control owners (coordination-scheduling). KPMG's 2025 SOX Survey excerpts say 52% of IA departments spent over 40% of hours on SOX in FY2024 (KPMG-SOX2030-2026, Introduction).
- **SOX readiness.** Scoping and risk assessment (expert-judgment); walkthroughs and narratives (document-production); control testing and evidence collection (review-assurance, data-reporting); deficiency evaluation (expert-judgment); remediation tracking (coordination-scheduling). KPMG lists AI uses as testing, evidence collection, walkthrough documentation and SOC-report review (search summary of KPMG's 2025 agentic paper; the 2026 paper was read in full, KPMG-SOX2030-2026).
- **Enterprise risk.** Risk identification and scoring (research-synthesis); risk reporting to boards (data-reporting). Little AI-specific public material was found beyond Optro's scoring agents (OPTRO-CRX-2026).
- **Advising clients on governing their own AI (the module's growth area).** AI governance structure, use-case inventory, risk assessment by COSO component, control design, implementation, monitoring (COSO-GENAI-2026, pp. 18-19); board and audit-committee oversight tools (IIA-IPPF-2026).

### 3.2 Common pain points

- Use outruns control. 75% active AI use in finance but only 29% tracking where AI fails (KPMG-AIFINANCE-2026).
- Piloting without scale. In KPMG's April 2026 poll, 55% of first-line finance functions and 51% of SOX/IA functions were at "some pilots/just starting" (KPMG-FUTURESOX-2026, pp. 3, 5). Time and resource constraints were the most-cited obstacle (about 26% for first line; KPMG-FUTURESOX-2026, p. 7).
- Shadow AI and low policy coverage: 54% of consultants admit unapproved use (LEXISNEXIS-CONSULTING-2026); 42% of European organisations have a formal comprehensive AI policy (ISACA-AIPULSE-2026).
- SOX cost and effort: cost of maintaining SOX controls up 45% between the 2023 and 2025 KPMG surveys; testing hours per control from 12 to 16 (KPMG-SOX2030-2026, p. 4).
- No common AI baseline in SOC reporting: the AICPA issued TQA 9561 (DART-TQA9561-2026), yet a Cloud Security Alliance note (AI-assisted, 2026-08-30) says auditors improvise evidence requests (CSA-SOC2AI-2026).

### 3.3 Metrics and benchmarks (with provenance)

| Metric | Value | What it measures | Provenance | Ref |
|---|---|---|---|---|
| Active AI use in finance | 30% (2024) to 75% (2026) | Senior finance leaders, n=1,013, revenue at least US$250M | vendor-published | KPMG-AIFINANCE-2026 |
| Fully assurance-ready | 42% | Organisations "fully assurance-ready for AI-enabled finance processes" | vendor-published | KPMG-AIFINANCE-2026 |
| Track where AI adoption fails | 29% | Organisations that track it | vendor-published | KPMG-AIFINANCE-2026 |
| Error reduction, assurance-ready vs not | 33% vs 6% | Organisations reporting improvement in error reduction | vendor-published | KPMG-AIFINANCE-2026 |
| IA formal AI program or broad adoption | 17.7% | Webinar respondents (not representative) | vendor-published | CPAPA-IAPOLL-2026 |
| IA novice or beginner in GenAI | 76% | Respondents to the 2024 IAF and Wolters Kluwer survey | survey, vendor-sponsored | IIAF-RIDDLE-2024 |
| SOX testing hours per control | 12 (FY2022) to 16 (FY2024) | KPMG 2025 SOX Survey | vendor-published | KPMG-SOX2030-2026 |
| Reddit SOX automation | 175 controls, over 40% of scope, 60% less time per control | One IA team, vendor release | vendor-published | OPTRO-CRX-2026 |
| Regular AI incident response exercises | 8% | Organisations, ISACA survey of 1,800+ | independent | ISACA-STATECYBER-2026 |
| Legal AI tool hallucination | 17% to 33% | Three legal research tools, preregistered test | independent | STANFORD-LEGALAI-2024 |
| Outside-the-frontier task correctness | 19% less likely to be correct | 758 BCG consultants using GPT-4, one task outside the AI frontier | independent | HBS-JAGGED-2023 |
| Inside-the-frontier gains | 12.2% more tasks, 25.1% faster | Same experiment, 18 tasks | independent | HBS-JAGGED-2023 |
| Finance-analyst benchmark | 64.37% top accuracy | 537 questions on SEC-filing research, LLM-judged, live leaderboard read 2026-10-20 | independent | VALS-FAB-2026 |
| Customer-support productivity | 14% (34% for novices) | 5,179 agents, issues resolved per hour; not professional services | independent | NBER-GENAIWORK-2023 |

**Quality evidence, stated plainly.** No source reports an error rate, override rate or inspection outcome for AI used in internal audit, SOX testing or enterprise risk advisory. The FRC says its guidance is not a response to identified quality deficiencies (FRC-GENAI-2026). The PCAOB spotlight reports observations, not inspection results (PCAOB-GENAI-2024). The independent measures above are all from adjacent work and cap the related entries at B.

### 3.4 Guardrails and regulatory points

- **Competence, confidentiality, communication, supervision, fees.** ABA Formal Opinion 512 (2024-07-29): lawyers need a reasonable understanding of the tool, must verify output, must protect client information, and must charge reasonable fees; it says a flat fee may be unreasonable if AI makes the work much quicker (ABA-FO512-2024, II.A-F, pp. 12-13). Texas Opinion 705 (2025-02) applies the Texas rules similarly (TXBAR-OP705-2025). The SRA warning notice (2026-08-18, read via Legal Cheek) says firms need effective governance, systems and controls for AI risk (LEGALCHEEK-SRA-2026). These bind lawyers; no Florida, NY or California opinion text was read; the Florida page returned no content.
- **Accountancy bodies.** The AICPA Code's general standards and confidential client information rules apply to AI (JOFA-ETHICS-2026). The AICPA Ethics Staff Insights article "AI Through an Ethics Lens" is cited but its text is in the Online Ethics Library and was not read. ACCA reports the January 2026 PCRT update suggests AI disclosure in engagement letters (ACCA-ENGLETTERS-2026). Management Consultancies Association guidance: none found.
- **Audit-side models.** AICPA practice aid (2026-10-13; two parts: client's AI in financial reporting, and the firm's AI in the audit; more guidance to be added) (AICPA-AUDITAID-2026). FRC guidance (2026-03-30): three risks to audit quality (deficient output, misuse, non-compliant methodology) and mitigations of design, certification, staff education and governance, and human in the loop (FRC-GENAIGUIDE-2026, pp. 4-6). PCAOB staff spotlight (2024-07; larger firms mainly) (PCAOB-GENAI-2024).
- **Control frameworks.** COSO GenAI (2026-02-23); IIA AI Auditing Framework (2024-09-13); NIST AI RMF Generative AI Profile (NIST AI 600-1, released 2024-07-26 per the NIST page) (NIST-AIRMF-2024).
- **Independence.** SEC Rule 2-01(c)(4) lists internal audit outsourcing, financial information systems design and implementation, bookkeeping and valuation among prohibited non-audit services for SEC audit clients, each unless results will not be subject to audit procedures (SEC-REGSX2-01-2026). The AICPA says developing or hosting an AI system for an attest client can raise independence concerns (JOFA-ETHICS-2026). The AICPA's rules for non-issuer audit clients were not read. Private middle-market clients are often non-SEC, so the AICPA rules, not Rule 2-01, usually apply.
- **EU AI Act.** A provisional agreement on the Digital Omnibus would move Annex III high-risk obligations to 2027-12-02 and Annex I to 2028-08-02; formal adoption was expected before 2026-08-02, and publication in the Official Journal was not confirmed in this run (GIBSONDUNN-EUOMNIBUS-2026). Article 50 transparency obligations largely stay on the original schedule (same source).
- **Client AI terms.** Engagement letters are the main contract lever found: Woodard's sample clause and ACCA's checklist (WOODARD-ENGLETTERS-2025; ACCA-ENGLETTERS-2026). No source on client-imposed AI restrictions in outside-counsel-style guidelines or MSAs was found.

### 3.5 Frontier signals (dated, sourced)

- **2026-02-23.** COSO issues GenAI internal-control guidance with a six-step roadmap and starter metrics (COSO-GENAI-2026; COSO-GENAIPR-2026).
- **2026-03-30.** FRC publishes the first regulator guidance on generative and agentic AI in audit; a certification-and-recertification model per use case (FRC-GENAI-2026; FRC-GENAIGUIDE-2026, pp. 32-33).
- **2026-05-11.** KPMG survey: assurance readiness separates better results from hidden risk (KPMG-AIFINANCE-2026).
- **2026-05-27.** EU provisional deal to delay high-risk AI obligations; adoption not confirmed here (GIBSONDUNN-EUOMNIBUS-2026).
- **2026-06-16.** IIA issues board and audit-committee AI questionnaires (IIA-IPPF-2026).
- **2026-08-18.** SRA warning notice on AI misuse (LEGALCHEEK-SRA-2026).
- **By 2026-09-21.** AICPA TQA section 9561 on service organisations' AI in SOC 1 and SOC 2 (DART-TQA9561-2026).
- **2026-09-23 and 2026-10-19.** Grant Thornton launches AIUC-1 services; AICPA and AIUC announce a joint SOC 2 plus AIUC-1 offering, with a full launch expected in early 2027 (GT-EAS-2026; JOFA-AIUC-2026).
- **2026-09-24.** KPMG says it expects the first wave of AI-related material weaknesses to appear in 2027, and that external auditors testing whole populations will reduce the value of management's sample testing in lower-risk areas (KPMG-SOX2030-2026, POV 1 and POV 5).
- **2026-10-13.** AICPA practice aid on AI for financial statement auditors; more guidance on risk of material misstatement and audit evidence to follow (AICPA-AUDITAID-2026; CPAPA-AUDITAID-2026).
- **2026-10-14.** Optro previews AI Discovery for shadow AI, ahead of 2027 availability (OPTRO-CRX-2026).

### 3.6 Workforce and role effects

- Auditor reliance on management testing may "go away", with the SOX role shifting toward controls advice (KPMG-FUTURESOX-2026, p. 7).
- Named owners per AI tool and RACI for prompts and data (COSO-GENAI-2026, p. 10).
- Skills: KPMG's survey says organisations mostly upskill existing finance and IA staff (38%) rather than hire (28%) (KPMG-AIFINANCE-2026). ISACA reports 45% see LLM security operations as a skill gap (ISACA-STATECYBER-2026).
- FRC lists erosion of human knowledge over time as an organisational risk it did not address in its guidance (FRC-GENAIGUIDE-2026, p. 6).
- Fieldguide's CEO says the CPA pipeline is at a 17-year low (vendor claim; CB-FIELDGUIDE-2026).
- Experienced accountants gain more from AI and intervene more at low confidence (STANFORD-JAR-2026; MITSLOAN-CHOIXIE-2025).

### 3.7 Objections and concerns practitioners raise

- Overreliance and loss of professional judgment (27.5% top agentic-AI concern among poll respondents; CPAPA-IAPOLL-2026).
- Hallucination and fabricated citations (ABA-FO512-2024, II.D; CITYAM-DELOITTE-2025).
- Data privacy, confidentiality and security as obstacles to scaling in finance (KPMG-FUTURESOX-2026, p. 7).
- Expectation gap: "we test everything" read as "nothing can be wrong" (CPAPA-FULLPOP-2026).
- Vendor claims are marketing until the client's own data reproduces them (CPAPA-AGENTSCLOSE-2026).
- Look-alike SOC reports from templated platforms; the Cloud Security Alliance note cites an AICPA Peer Review Board alert of May 2026 (secondhand, AI-assisted source; CSA-SOC2AI-2026).
- Over-control drives workarounds (JOFA-CYBERCHECK-2026).

### 3.8 Interview probes

1. "Which of your clients' AI uses can you list today, and who owns each one?" Probes inventory, shadow AI and ownership (COSO roadmap step 2).
2. "When your team ran an AI test next to the manual one, what differed?" Probes parallel-run evidence, which no source publishes.
3. "What do you write in the engagement letter and the file about AI, and has any client objected?" Probes disclosure, consent and documentation.
4. "Which of your services would your firm's independence rules stop you selling to an audit client?" Probes IA outsourcing, systems design and AI readiness work for attest clients.
5. "What happens when the vendor updates the model?" Probes recertification, rollback and monitoring (FRC pp. 32-33; COSO p. 19).

---

## 4. Routed to other modules

| Item | Target | Why |
|---|---|---|
| AIUC-1 and SOC 2 examinations, SOC 1/2 AI TQA 9561, AICPA practice aid for auditors, FRC audit guidance, PCAOB spotlight (JOFA-AIUC-2026, DART-TQA9561-2026, AICPA-AUDITAID-2026, FRC-GENAIGUIDE-2026, PCAOB-GENAI-2024) | assurance archetype | Attest work and audit methodology; only readiness advice sits here |
| Full-population audit testing at an employee-benefit-plan audit firm (CPAPA-FULLPOP-2026) | assurance archetype | Attest side; used here only for the expectation-gap point |
| Alternative practice structure, PE ownership, IA outsourcing as a fee line, GT-CBIZ deal (GT-CBIZ-2026) | professional-services | Firm operations and ownership |
| Fee reasonableness when AI shortens work (ABA-FO512-2024, II.F) | professional-services (pricing) | Pricing of the firm's own work |
| Close and reconciliation agents delivered as CAS; bookkeeping field evidence (STANFORD-JAR-2026, CPAPA-AGENTSCLOSE-2026) | client-accounting-services | Firm-run bookkeeping and close; this module keeps only the control framing |
| AI-fuelled fraud and deepfake preparedness (ISACA-AIPULSE-2026; landscape ACFE-TECHBENCH-2026); AI-washing investigations (SEC-AIWASH-2024) | forensic-disputes | Investigation and disputes work |
| IRS OPR and UK PCRT tax-practice AI guidance (ACCA-ENGLETTERS-2026) | tax archetype | Tax technical practice |
| IVSC AI disclosure in valuation reports (landscape IVSC-IVSED-2026) | valuation | Valuation standards |
| AI assistance in firm quality control and peer review (CSA-SOC2AI-2026 note on peer review) | professional-services | Firm quality management |

---

## 5. Sources

All entries opened (`access: full`) unless marked search-only. Provenance of figures is in the use-case YAML.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| ABA-FO512-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools | ABA Standing Committee on Ethics and Professional Responsibility (copy hosted by LawNext; ABA URL returned 403) | professional-body | https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf | 2024-07-29 |
| LAWNEXT-ABA512-2024 | In First Ethics Ruling on Gen AI, ABA Says Lawyers Must Have Reasonable Understanding... | LawSites | press | https://www.lawnext.com/2024/07/in-first-ethics-ruling-on-gen-ai-aba-says-lawyers-must-have-reasonable-understanding-of-the-technology-but-need-not-become-experts.html | 2024-07-30 |
| TXBAR-OP705-2025 | Opinion 705 (generative AI in law practice) | Professional Ethics Committee, State Bar of Texas (Texas Center for Legal Ethics) | professional-body | https://www.legalethicstexas.com/resources/opinions/opinion-705/ | 2025-02 |
| LEGALCHEEK-SRA-2026 | SRA warns over AI misuse following rise in blunders | Legal Cheek | press | https://www.legalcheek.com/2026/08/sra-warns-over-ai-misuse-following-rise-in-blunders/ | 2026-08-18 |
| AICPA-AUDITAID-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| CPAPA-AUDITAID-2026 | AICPA Practice Aid Provides Guidance to Auditors on AI Use in Financial Statement Audits | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=191588 | 2026-10-13 |
| JOFA-AIUC-2026 | AICPA partners on new offering that assures AI systems and agents | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/ | 2026-10-19 |
| JOFA-ETHICS-2026 | Accounting ethics in the age of AI | Journal of Accountancy (AICPA Professional Ethics Division) | professional-body | https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/ | 2026-08-05 |
| JOFA-AIPOLICY-2026 | Drafting an AI policy that actually works | Journal of Accountancy (Aon author) | professional-body | https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works.html | 2026-07-01 |
| JOFA-CYBERCHECK-2026 | New checklist helps CPAs manage AI cyber risks | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/ | 2026-10-01 |
| ACCA-ENGLETTERS-2026 | Engagement letters, AI and PCRT | ACCA | professional-body | https://www.accaglobal.com/gb/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/september/Engagement-letters-AI-and-PCRT.html | 2026-09 |
| IIA-AIFW-2024 | AI Auditing Framework | The IIA | professional-body | https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/ | 2024-09-13 |
| IIA-IPPF-2026 | IPPF documents listing, topic Artificial Intelligence | The IIA | professional-body | https://www.theiia.org/en/standards/documents/ | 2026-09-18 |
| IIA-AIKC-2026 | IIA AI Knowledge Center: New Tools for Internal Auditors | IIA Belgium | professional-body | https://www.iiabelgium.org/news-publications/iia-ai-knowledge-center-new-tools-for-internal-auditors | 2026-08 |
| COSO-GENAI-2026 | Achieving Effective Internal Control Over Generative AI (GenAI) | COSO | standard-setter | https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf | 2026-02-23 |
| COSO-GENAIPR-2026 | COSO Releases Practical Roadmap for Managing Generative AI Risks and Controls | COSO | standard-setter | https://www.coso.org/_files/ugd/719ba0_e08afa6e8d7940cd9ae18d0c25b2cb55.pdf | 2026-02-23 |
| FRC-GENAI-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies | UK FRC | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 |
| FRC-GENAIGUIDE-2026 | Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples | UK FRC | regulator | https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03 |
| PCAOB-GENAI-2024 | Spotlight: Staff Update on Outreach Activities Related to GenAI | PCAOB staff | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 |
| SEC-REGSX2-01-2026 | 17 CFR 210.2-01, paragraph (c)(4) | SEC (via Cornell LII) | regulator | https://www.law.cornell.edu/cfr/text/17/210.2-01 | 2026-10-20 (access date of current text) |
| SEC-AIWASH-2024 | SEC Charges Two Investment Advisers... Use of Artificial Intelligence | SEC | regulator | https://www.sec.gov/newsroom/press-releases/2024-36 | 2024-03-18 |
| NIST-AIRMF-2024 | AI Risk Management Framework page (NIST AI 600-1 GenAI Profile, 2024-07-26) | NIST | regulator | https://www.nist.gov/itl/ai-risk-management-framework | 2024-07-26 |
| GIBSONDUNN-EUOMNIBUS-2026 | EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines | Gibson Dunn | firm | https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines/ | 2026-05-27 |
| KPMG-AIFINANCE-2026 | AI adoption in finance doubles, but assurance readiness determines who wins | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html | 2026-05-11 |
| KPMG-SOX2030-2026 | The Future of SOX: A point of view for 2030 and beyond | KPMG LLP | firm | https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html | 2026-09-24 |
| KPMG-FUTURESOX-2026 | Revolutionizing internal controls (April 2026 Future of SOX webcast) | KPMG LLP | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/revolutionizing-internal-controls.pdf | 2026-05-20 |
| GT-EAS-2026 | Grant Thornton launches first-of-its-kind Enterprise Assurance Services practice | Grant Thornton LLP | firm | https://www.grantthornton.com/insights/press-releases/2026/september/gt-launches-first-of-its-kind-enterprise-assurance-services | 2026-09-23 |
| GT-CBIZ-2026 | Grant Thornton CEO Says CBIZ Merger Is Key to Unlocking AI Value | Bloomberg Law | press | https://news.bloomberglaw.com/financial-accounting/grant-thornton-ceo-says-cbiz-merger-is-key-to-unlocking-ai-value | 2026-09-02 |
| CB-FIELDGUIDE-2026 | Cherry Bekaert Expands AI Audit With Fieldguide | Cherry Bekaert | firm | https://www.cbh.com/newsroom/cherry-bekaert-expands-ai-audit-with-fieldguide/ | 2026-06-03 |
| APRIO-FIELDGUIDE-2026 | Aprio and Fieldguide Co-Build the Future of Audit with Agentic AI | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=188025 | 2026-08-05 |
| DART-TQA9561-2026 | AICPA Releases TQAs on a Service Organization's Use of AI | Deloitte DART | firm | https://dart.deloitte.com/USDART/home/news/all-news/2026/sep/aicpa-releases-tqas-service-organization-use-ai | 2026-09-21 |
| WOODARD-ENGLETTERS-2025 | Future Ready Engagement Letters (webinar deck) | Woodard | firm | https://www.woodard.com/hubfs/Future_Ready_Engagement_Letters_Oct2025.pdf | 2025-10 |
| CPAPA-AGENTSCLOSE-2026 | Before You Let the Agents Run the Close: Five Controls to Put in Writing First | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/ | 2026-08-13 |
| CPAPA-FULLPOP-2026 | Testing Every Transaction Changes the Audit... | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/ | 2026-10-15 |
| CITYAM-DELOITTE-2025 | Deloitte refunds Australian government after AI 'made up citations' in report | City AM | press | https://www.cityam.com/?p=2367690 | 2025-10-06 |
| STORYBOARD18-DELOITTE-2025 | Deloitte to repay Australian govt over flawed $440,000 report aided by AI | Storyboard18 | press | https://storyboard18.com/digital/deloitte-to-repay-australian-govt-over-flawed-440000-report-aided-by-ai-82083.htm | 2025-10-07 |
| CPAPA-IAPOLL-2026 | Internal Auditors Eye Broader AI Use | CPA Practice Advisor (Wolters Kluwer TeamMate poll) | survey | https://www.cpapracticeadvisor.com/?p=191508 | 2026-10-12 |
| IIAF-RIDDLE-2024 | Solving the riddle: Harnessing Generative AI for internal audit activities | Internal Audit Foundation and Wolters Kluwer TeamMate | survey | https://www.theiia.org/en/content/research/foundation/2024/solving-the-riddle-harnessing-generative-ai-for-internal-audit-activities/ | 2024 |
| ISACA-STATECYBER-2026 | Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises | ISACA | survey | https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises | 2026-09-22 |
| ISACA-AIPULSE-2026 | A Third of European Organisations Don't Know if They've Been Hit by an AI-Powered Cyberattack | ISACA | survey | https://www.isaca.org/about-us/newsroom/press-releases/2026/a-third-of-european-organisations-dont-know-if-they-have-been-hit-by-an-ai-powered-cyberattack | 2026-06-17 |
| OPTRO-CRX-2026 | Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance | Optro via CPA Practice Advisor | vendor | https://www.cpapracticeadvisor.com/2026/10/14/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance/191695/ | 2026-10-14 |
| LEXISNEXIS-CONSULTING-2026 | AI Is Accelerating Consulting and Introducing Risk (Management Consulting Industry Report 2026 landing page) | LexisNexis | vendor | https://professional.lexisnexis.com/en-us/ps-fowmini2026 | 2026 |
| VALS-FAB-2026 | Finance Agent Benchmark v1.1 leaderboard and methodology | Vals AI | vendor | https://www.vals.ai/benchmarks/finance_agent | 2026-10-20 (live page, access date) |
| CSA-SOC2AI-2026 | The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted | Cloud Security Alliance | community | https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/08/CSA_research_note_soc2_ai_controls_gap_20260830-csa-styled.pdf | 2026-08-30 |
| STANFORD-JAR-2026 | Human + AI in Accounting: Early Evidence from the Field | Stanford GSB (J. of Accounting Research 64(3)) | academic | https://www.gsb.stanford.edu/index%2ephp/node/629989 | 2026-06 |
| MITSLOAN-CHOIXIE-2025 | How generative AI can make accountants more productive | MIT Sloan | academic | https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-can-make-accountants-more-productive | 2025-08-05 |
| HBS-JAGGED-2023 | Navigating the Jagged Technological Frontier (HBS Working Paper 24-013) | Harvard Business School with BCG | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 (read through r.jina.ai mirror) | 2023-09 |
| NBER-GENAIWORK-2023 | Generative AI at Work (NBER Working Paper 31161) | NBER | academic | https://www.nber.org/papers/w31161 | 2023-04 |
| STANFORD-LEGALAI-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools | Stanford and Yale researchers (arXiv) | academic | https://arxiv.org/pdf/2405.20362 | 2024-05-30 |

**Search-only or blocked (leads, not used in A or B outcomes):**

| Ref | Item | Why not opened |
|---|---|---|
| SRA-NOTICE-2026 | SRA warning notice on AI (sra.org.uk) | Site returned a security check; read only through Legal Cheek |
| WK-IAPOLL-2026 | Wolters Kluwer release on the 2026-10-06 TeamMate poll | Page returned 403; read through CPAPA-IAPOLL-2026 |
| AICPA-TQA9561-2026 | AICPA TQA section 9561 text | Behind AICPA login; Schneider Downs summary blocked (403) |
| SIDLEY-EUOMNIBUS-2026 | Sidley, 2026-06-22 note on the EU AI omnibus | Blocked (403); results seen only in search |
| PCAOB-PROJECTS-2026 | PCAOB standard-setting and research projects page | Blocked; a search summary mentions a data and technology research project and a 2026 comment request, unconfirmed |
| SEC-AIWASH-2026 | Law-firm blog summaries of SEC AI-claims actions, August-September 2026 | Secondary blogs only; not opened |
| PROTIVITI-TOPTECH | Protiviti technology-risk survey (23% of IT audit functions using AI/ML per a search summary) | Year not confirmed; not opened |

**Source counts by type (opened, 49 distinct):** professional-body 12, regulator 7, standard-setter 2, firm 9, press 8, survey 4, vendor 3, academic 6, community 1, conference 0, podcast 0, job-posting 0. Nine of the eleven type values in the vocabulary that apply here are represented.

---

## 6. Gaps

- **No quality measurements for AI in IA, SOX or ERM advisory.** No error rate, override rate, false-exception rate, parallel-run result or inspection finding was found. The Reddit figure is a vendor-published time saving; no source reports test accuracy.
- **No outsourced-provider case.** All named IA and SOX results are in-house teams (Reddit, Klaviyo, FJ Management). Cherry Bekaert and Aprio describe platforms but publish no outcomes.
- **Blocked primary sources.** ABA (read via a LawNext-hosted copy), SRA notice, PCAOB project pages, Wolters Kluwer release, AICPA TQA 9561 text and AICPA's "AI Through an Ethics Lens" article. No Florida, New York or California bar opinion text was read; the Florida page returned no content.
- **MCA (Management Consultancies Association).** No AI guidance, code or client-disclosure rule found; only member-survey coverage in search.
- **Client AI terms.** Only engagement-letter templates and ACCA guidance were found; no evidence on clients writing AI restrictions into contracts or procurement terms for accounting or advisory firms.
- **Independence for non-SEC clients.** The AICPA's nonattest-services rules for non-issuer audit clients were not read; Rule 2-01 applies to SEC registrants only. Whether AIUC-1 readiness advice conflicts with a later examination by the same firm was not resolved.
- **NBER and academic work specific to risk advisory.** No NBER or SSRN paper on AI in internal audit or SOX advisory was found. The measured academic work is adjacent: bookkeeping (STANFORD-JAR-2026), customer support (NBER-GENAIWORK-2023), consulting tasks (HBS-JAGGED-2023), legal research (STANFORD-LEGALAI-2024). HBS-JAGGED-2023 is a September 2023 working paper, kept as foundation.
- **Conflicts noted.** (a) KPMG's release uses 42% for two different measures; the landscape's concern about conflation is confirmed in the release text. (b) CPA Practice Advisor said on 2026-08-13 that the AICPA had not published AI guidance for SOC; DART reported TQA 9561 on 2026-09-21; the Cloud Security Alliance note of 2026-08-30 predates it. (c) COSO's press release names the eighth capability type "regulatory intelligence"; the document names it "knowledge retrieval and summarization". (d) EU omnibus adoption is unconfirmed. (e) The IIA framework date is 2024-09-13 per the IIA listing; other sources say 2023.
- **Survey limits.** Wolters Kluwer and KPMG webcast polls are self-selected audiences; the KPMG finance survey has a revenue floor of US$250M and a sample that is 58% technology and financial services, so it does not describe the private middle market.
- **Not researched.** Colorado AI Act status, IESBA's technology guidance text, SEC and state regulator statements on ICFR over AI, and Big Four internal-audit AI whitepapers beyond KPMG.
