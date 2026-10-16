# Module deep dive: assurance / controls-testing / discourse

- **Archetype:** assurance
- **Module:** controls-testing. Testing the design and operating effectiveness of internal controls in external ICFR audits (SOX 404, ISA 330, AS 2201/AS 2301), in internal audit and SOX compliance programs, and in SOC 1/SOC 2 examinations. Covers walkthroughs, ITGC and application controls, sampling, evidence and tick-marking, deficiency evaluation, and documentation.
- **Angle:** discourse. What practitioners have said in the last 12–18 months at conferences, on podcasts and webinars, in practitioner articles and in community discussion.
- **Prepared:** 2026-10-16
- **Method note:** About 70 pages and PDFs were opened and read directly with curl, including primary documents the landscape scan could only see in snippets: the KPMG *Future of SOX 2030* PDF, the EY SOC conference highlights PDF, the Microsoft internal audit PDFs, the WCARS Seville programme PDF, and the CPA Practice Advisor, JofA, CFO Dive and Accounting Today articles. Another 20 or so items were seen only in search results; they are marked "(search only)" where cited. The PCAOB, Gartner research, Reddit, Going Concern, Protiviti's blog, FEI and Crowe refused automated access (see §5). Figures attributed to vendors are vendor claims, even when the vendor names a customer.

---

## 1. Summary

1. **The conversation moved from GenAI assistants to "autonomous testing" in about 12 months, and internal audit and SOX teams are ahead of external audit.** The main venues were IIA GAM in March 2026 (headline theme "the rise of agentic AI"), Optro CRX in October 2026, Workiva Amplify in September 2026 and the Speaking of Risk and Audit podcast. Practitioners now describe agents that read unstructured evidence, run attribute tests, tick-mark the source and draft workpapers. Named in-house cases are emerging. Optro reports that Reddit automated 175 controls (over 40% of its SOX scope) in three months and cut testing time per control by about 60% on average (S04). Microsoft reports 850 hours a year saved by its ITGC change-management testing agent (S14). External audit voices are more cautious. In October 2026, a year into its programme, PwC's assurance transformation leader said the time savings were "not that drastic yet" (S21).
2. **Full-population and continuous testing is the stated destination.** The sharpest debates are about what that means for evidence and for reliance. KPMG's *Future of SOX 2030* (September 2026) predicts a move to continuous testing of 100% of transactions. It also says the value of the auditor relying on management's testing may shrink, or may grow, depending on whose AI meets the evidential bar (S01). Practitioners warn that testing every transaction surfaces more exceptions and can widen the expectation gap if marketed as certainty (S33). MindBridge's comment letter to the PCAOB says inspection uncertainty leads firms to run AI procedures alongside the old manual ones ("over-auditing") (S34).
3. **The worries cluster around four themes:**
   - **Automation bias and rubber-stamp review:** ICAEW says the FRC guidance gives this only one paragraph (S41), and KPMG says a human approval step that rubber-stamps every AI recommendation provides no real control value (S01).
   - **Agents acting wrongly:** In Optro's survey, 34% of organisations said they had acted on an inaccurate agent output (S05).
   - **Commoditised SOC 2 reports:** The AICPA Peer Review Board issued an alert, and the Delve allegations followed (S25–S31).
   - **Standards not yet written for AI:** The PCAOB is "still figuring it out" (S37), and the IAASB has chosen to stay technology-neutral (S52).

   A new idea also appears: testing controls that are themselves performed by AI. KPMG expects the first wave of AI-related material weaknesses in 2027 (S01).

---

## 2. Use cases

```yaml
- id: assurance-controls-testing-01
  title: Agentic attribute testing of SOX controls against unstructured evidence
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  lens: delegate
  ladder: delegate
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >
    Testers open PDFs, screenshots, tickets and spreadsheets for each sample, check each control
    attribute by hand and document the result. KPMG's 2025 SOX survey found that average testing
    hours per control rose from 12 (FY2022) to 16 (FY2024).
  solution: >
    An agent reads the evidence for each sample, checks every defined attribute (for example
    approval, date, threshold), records pass, fail or open items with citations, and sends
    exceptions to a human reviewer. Practitioners say standard ITGCs (user access, password
    controls) and three-way matches are automated first, because their evidence and rules are bounded.
  outcomes:
    - {lever: capacity, description: "Reddit internal audit automated 175 controls (>40% of SOX scope) in its first three months, later expanded to >75% of SOX controls", figure: "175 controls; >40% then >75% of SOX scope", source_ref: S04}
    - {lever: speed, description: "Average testing time per control reduced at Reddit (vendor-published)", figure: "-60% per control", source_ref: S04}
    - {lever: speed, description: "Vendor claim that a SOX test falls from about 16 hours to under 15 minutes; up to 85% of SOX controls automatable, especially ITGCs", figure: "16h -> <15 min (claim)", source_ref: S09}
  prerequisites:
    - Control library with explicit attributes, evidence requirements and exception rules (practitioners say vague criteria such as 'approval is required' break agents)
    - Evidence accessible in a consistent location; a reviewer workflow
    - Central record of previously accepted deviations, so the agent can check new exceptions against it
  risks_and_guardrails:
    - "Plateau when agents are pointed at judgment-heavy controls, such as management review controls (Optro, S07)"
    - "Every result reviewed before it enters the workpaper (Riveron model, S18)"
    - "KPMG warns that control owners could hide instructions in evidence aimed at testing agents (prompt injection) (S01)"
  human_checkpoints:
    - Reviewer signs off each test conclusion
    - Humans own deviation evaluation, root cause and deficiency classification
  role_evolution: "Testers become reviewers and 'managers of AI agents' who handle exceptions, ad hoc testing and control-owner remediation (S09, S11)."
  evidence_grade: A
  sources:
    - {ref: S04, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14}
    - {ref: S07, title: "Agentic AI in Internal Audit: What to Automate First", publisher: Optro, type: vendor, url: "https://optro.ai/blog/agentic-ai-internal-audit-controls", date: 2026-08-11}
    - {ref: S09, title: "From 16 Hours to 15 Minutes: Agentic AI Rewrites SOX Testing", publisher: "Speaking of Risk and Audit (Richard Chambers)", type: podcast, url: "https://srapodcast.podbean.com/e/from-16-hours-to-15-minutes-agentic-ai-rewrites-sox-testing/", date: 2026-05-28}
  last_reviewed: 2026-10-16
  notes: "Grade A because a named organisation and a measured figure are published, but the figure is vendor-reported (in Optro's launch release) and covers time and volume, not quality. A Reddit job posting for an 'AI-first internal audit' role confirms the direction (S64)."

- id: assurance-controls-testing-02
  title: Two-agent ITGC change-management testing (attribute extraction plus tick-marking)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: document-to-decision
  lens: automate
  ladder: automate
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Auditors review change tickets across several ticketing systems with inconsistent formats to check testing, approvals and timing before deployment, then tick-and-tie each attribute by hand."
  solution: >
    One agent ingests ticket data, extracts the required attributes (tester, approver, dates) into a
    standard table and pre-fills pass/fail logic. A second agent annotates the source evidence with
    visual tick-marks showing where each attribute was validated. Built on Copilot Studio and M365.
  outcomes:
    - {lever: capacity, description: "Annual time saved (self-reported by Microsoft)", figure: "850 hours/year", source_ref: S14}
    - {lever: cost, description: "Annual cost saved", figure: "$185K/year", source_ref: S14}
    - {lever: speed, description: "Time to launch", figure: "1-3 months", source_ref: S14}
  prerequisites: [Ticket data access across systems, Defined attribute and pass/fail rules, Low-code agent platform]
  risks_and_guardrails: ["Pre-filled pass/fail logic must be reviewed; pass/fail logic is rule-based rather than generative"]
  human_checkpoints: [Auditor reviews exceptions and signs off the workpaper]
  role_evolution: "Auditors move from opening and annotating each sample to reviewing SOX exceptions."
  evidence_grade: A
  sources:
    - {ref: S14, title: "SOX Change Management Testing Agent (Frontier Finance innovation story)", publisher: Microsoft, type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/SOX-Change-Management-Testing-Agent.pdf", date: FY2026}
    - {ref: S15, title: "AI solution overviews: Internal Audit", publisher: Microsoft, type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf", date: FY2026}
  last_reviewed: 2026-10-16
  notes: "The landscape's '850 vs 50 hours' conflict is a text-extraction artefact. In the Internal Audit PDF a glyph is missing before '50' (other numbers in that PDF lose digits the same way), so both documents most likely say 850. Self-reported, with no quality measure."

- id: assurance-controls-testing-03
  title: Agent-driven evidence (PBC) collection and control-owner follow-up
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [coordination-scheduling, data-reporting]
  pattern: other
  lens: automate
  ladder: automate
  runtime_class: background-agent
  maturity: announced
  problem: "Testers spend weeks requesting, chasing and re-requesting evidence from control owners spread across 20+ systems; screenshots are captured by hand each quarter."
  solution: >
    Agents pull evidence through direct integrations or computer-use navigation of legacy systems,
    capture the screenshots auditors require, and message control owners in Slack or Teams with
    pre-filled context. They also flag gaps before submission. KPMG argues automated evidence
    collection may pay back sooner than automated testing.
  outcomes:
    - {lever: speed, description: "Less evidence follow-up before testing starts (vendor description, no figure)", figure: "n/a", source_ref: S04}
  prerequisites: ["Evidence embedded in workflows or stored in standard repositories (KPMG POV 3)", System access for agents]
  risks_and_guardrails: ["SOC peer reviewers warn against dashboard extraction replacing inquiry and testing (S26)", "Access and segregation of duties for agents holding system credentials"]
  human_checkpoints: [Control owner confirms submissions, Tester judges sufficiency]
  role_evolution: "Less evidence chasing by staff; more time on design and exceptions."
  evidence_grade: C
  sources:
    - {ref: S01, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24}
    - {ref: S60, title: "Arden: AI-native internal audit firm", publisher: Y Combinator, type: vendor, url: "https://ycombinator.com/companies/arden", date: 2026}
    - {ref: S04, title: "Optro Launches Domain-Trained Agents...", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14}
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': an evidence-request agent that negotiates with control owners. Optro says automated evidence collection is 'upcoming'. Midship's 2025 launch post also named it as the next roadmap item (S61)."

- id: assurance-controls-testing-04
  title: AI-prepared walkthroughs and test-of-design documentation
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Walkthroughs are re-performed every year to confirm nothing changed. Following one transaction end to end in a global company is laborious, and the same system architecture is redrawn for each walkthrough."
  solution: >
    The tool ingests prior-year walkthroughs and current documentation, generates a tailored work
    plan, highlights what is missing or changed, and drafts process and control documentation for
    review. KPMG's agentic SOX framework adds meeting scheduling and call transcription.
  outcomes:
    - {lever: speed, description: "PwC reports quicker work and more informative quality, but only modest busy-season time savings so far", figure: "not quantified", source_ref: S21}
  prerequisites: [Prior-year walkthrough files, Current process documentation, Firm methodology templates]
  risks_and_guardrails: ["Change detection must not replace inquiry and observation", "Test of design gains emphasis as AI-enabled processes spread (KPMG 404(a) paper, S03)"]
  human_checkpoints: [Auditor performs or attends walkthrough, Reviewer approves design conclusion]
  role_evolution: "Less transcription and diagramming; more time on design challenge."
  evidence_grade: B
  sources:
    - {ref: S20, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28}
    - {ref: S21, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07}
    - {ref: S02, title: "Seize the future: The agentic shift in SOX compliance", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/us/en/articles/2025/seize-the-future-the-agentic-shift-in-sox-compliance.html", date: 2025-08-06}
    - {ref: S06, title: "Autonomous Controls Testing Will Redefine Internal Audit", publisher: Optro, type: vendor, url: "https://optro.ai/blog/autonomous-controls-testing-internal-audit", date: 2026-06-15}
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-05
  title: External-audit tests of controls using agentic sample-to-evidence matching
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  lens: automate
  ladder: automate
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Engagement teams match each selected item to supporting documents in many formats; PwC staff quip that the client 'may hand you a napkin'."
  solution: >
    An agent-led module extracts, matches and validates evidence against documents, with an evidence
    trail for each match. It is already used in substantive testing (cash, AR, AP). PwC says its
    automated controls-testing solutions will work in a similar way. Thomson Reuters offers a
    comparable product for smaller firms.
  outcomes:
    - {lever: speed, description: "Thomson Reuters early-adopter claim of faster preparation and workpaper review (vendor)", figure: "up to 70%", source_ref: S62}
  prerequisites: [Firm-certified tool under the quality management system, Ingestion of heterogeneous evidence]
  risks_and_guardrails: ["PCAOB AS 1105 amendments (effective FY2026) require evaluating the reliability of information processed by technology tools", "Documentation must show the population covered, items flagged and follow-up (S36)"]
  human_checkpoints: [Engagement team reviews matches and exceptions]
  role_evolution: "Junior tick-and-tie work shrinks; reviewers check exceptions."
  evidence_grade: C
  sources:
    - {ref: S20, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28}
    - {ref: S62, title: "Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html", date: 2025-11-05}
  last_reviewed: 2026-10-16
  notes: "PwC's controls-testing variant was described as expected (Oct 2025). No later public confirmation was found. Grade C for the controls use."

- id: assurance-controls-testing-06
  title: Full-population testing of transaction-level controls in place of sampling
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  lens: reinvent
  ladder: automate
  runtime_class: background-agent
  maturity: piloting
  problem: "Sample-based conclusions carry an inherent limitation, since most transactions are never examined. KPMG says management's 25-item sample adds little when the auditor can test 100%."
  solution: >
    AI agents, paired with deterministic code for the calculations, test every transaction in a
    population (for example every 401(k) deposit against payroll, or every match calculation). Human
    hours shift to investigating exceptions.
  outcomes:
    - {lever: capacity, description: "Microsoft Internal Audit says agents run full-population testing on high-risk data sets and internal quality review effort fell", figure: "QA review effort about -50%; report issuance 3 -> 2 weeks", source_ref: S15}
    - {lever: speed, description: "Practitioner estimate that 20 hours of junior manual testing runs in minutes", figure: "20h -> minutes (claim)", source_ref: S33}
  prerequisites: [Complete and reliable populations, "Deterministic calculation layer alongside LLM reading (S33, S41)", Capacity to work more exceptions]
  risks_and_guardrails:
    - "More exceptions means more follow-up and materiality judgment (S33)"
    - "Do not market 'we test everything' as certainty; reasonable assurance still applies (S33)"
    - "PCAOB standards do not say what a clean full-population run means for sufficiency or how to set investigation thresholds (S34)"
  human_checkpoints: ["Investigation thresholds set before seeing output (MindBridge proposal, S34)", Exception disposition]
  role_evolution: "From mechanical testing to judgment on exceptions; 'a person accountable for every conclusion' (S33)."
  evidence_grade: B
  sources:
    - {ref: S01, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: 2026-09-24}
    - {ref: S15, title: "AI solution overviews: Internal Audit", publisher: Microsoft, type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf", date: FY2026}
    - {ref: S33, title: "Testing Every Transaction Changes the Audit – Here's What Firms Should Know Before They Sell It", publisher: CPA Practice Advisor (Tunde Adewole, Ledgerline), type: press, url: "https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/", date: 2026-10-15}
    - {ref: S34, title: "MindBridge's Response to the PCAOB's Strategic Priorities on AI Audit", publisher: MindBridge, type: vendor, url: "https://www.mindbridge.ai/blog/pcaob-ai-audit-strategic-priorities/", date: 2026-07-06}
  last_reviewed: 2026-10-16
  notes: "Microsoft's figures cover its whole internal audit operating model, not controls testing alone."

- id: assurance-controls-testing-07
  title: Continuous, year-round control testing and monitoring instead of point-in-time cycles
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  lens: reinvent
  ladder: delegate
  runtime_class: background-agent
  maturity: in-production
  problem: "Testing bunched at a single point in time finds failures late. Exceptions surface at year-end or during the external audit."
  solution: >
    Agents test controls continually through the year, and continuous monitoring tools flag exceptions
    in near real time. Practitioners frame a three-lines split: the first line runs continuous
    monitoring, and internal audit tests the reliability of that monitoring.
  outcomes:
    - {lever: risk, description: "Klaviyo's internal audit VP says testing throughout the year catches issues earlier and speeds remediation (no figure)", figure: "n/a", source_ref: S04}
  prerequisites: [Automated evidence feeds, "Risk-to-control-to-data-source mappings (GT, S19)", Alert routing to named owners]
  risks_and_guardrails: ["Independence: internal audit should test the monitoring, not run the first-line operations (S01)", "Human-approved criteria for when AI can auto-clear versus route to review (S19)"]
  human_checkpoints: [Exception triage, Periodic validation of monitoring logic]
  role_evolution: "Internal audit moves from re-performance to assuring monitoring and advising on control design."
  evidence_grade: B
  sources:
    - {ref: S04, title: "Optro Launches Domain-Trained Agents...", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14}
    - {ref: S19, title: "The power of AI in efficient SOX compliance", publisher: Grant Thornton, type: firm, url: "https://grantthornton.com/insights/articles/advisory/2026/the-power-of-ai-in-efficient-sox-compliance", date: 2026-07-21}
    - {ref: S01, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24}
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-08
  title: Risk-scored sample selection agent
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: other
  lens: automate
  ladder: augment
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Sample selection relied on static lists, geographic assumptions and judgment-heavy reviews, so coverage choices were hard to explain or adapt."
  solution: "An agent scores items on revenue, discounts, country risk and control indicators to produce a defensible risk-based selection."
  outcomes:
    - {lever: speed, description: "Weeks of manual analysis cut to a single day (Microsoft Internal Audit)", figure: "weeks -> 1 day", source_ref: S15}
  prerequisites: [Risk indicators in structured data, M365 Copilot]
  risks_and_guardrails: ["Selection logic must be documented and explainable to reviewers or inspectors"]
  human_checkpoints: [Audit lead approves the selection basis]
  role_evolution: "Planners review and adjust scored selections instead of building them."
  evidence_grade: A
  sources:
    - {ref: S15, title: "AI solution overviews: Internal Audit", publisher: Microsoft, type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf", date: FY2026}
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': risk-scored selection. Microsoft's annual-hours figure for this agent did not extract cleanly from the PDF (a digit is missing), so it is not reported here. Applied to partner and compliance audits rather than SOX sampling alone."

- id: assurance-controls-testing-09
  title: Audit-ready workpaper drafting with traceable, annotated citations
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  lens: automate
  ladder: augment
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Every test result has to be named, timestamped and cross-referenced into Excel and Word in the format the external auditor expects."
  solution: "Agents generate annotated workpapers that link each conclusion back to the source evidence, in the auditor's expected format (often through an Excel add-in), with an approval workflow."
  outcomes:
    - {lever: capacity, description: "Petual-reported efficiency gain on existing SOX workflows (vendor)", figure: "68-80%", source_ref: S57}
    - {lever: speed, description: "Midship users report time saved preparing a first-draft workpaper (vendor)", figure: "60%", source_ref: S07}
    - {lever: cost, description: "Customer quoted by the investor as cutting budget 'to a quarter' (anonymous, investor-reported)", figure: "~75% budget cut (claim)", source_ref: S56}
  prerequisites: [Workpaper templates agreed with the external auditor, Approval workflow]
  risks_and_guardrails: ["A generic 'AI tool was used' note does not meet documentation standards (CalCPA, S35)", "Reviewers need to see where their own judgment entered the workpaper (S36)"]
  human_checkpoints: [Preparer and reviewer sign-off]
  role_evolution: "Staff edit and review drafts instead of assembling them."
  evidence_grade: C
  sources:
    - {ref: S57, title: "Petual raises $20m for AI-powered SOX compliance", publisher: FinTech Global, type: press, url: "https://fintech.global/2026/04/24/petual-raises-20m-for-ai-powered-sox-compliance/", date: 2026-04-24}
    - {ref: S56, title: "Investing in Petual", publisher: Andreessen Horowitz, type: vendor, url: "https://a16z.com/announcement/investing-in-petual/", date: 2026-04-23}
    - {ref: S16, title: "Andera and RSM US Partner to Create AI-Enabled Control Testing Platform for Internal Audit", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/", date: 2026-08-26}
  last_reviewed: 2026-10-16
  notes: "Navan's head of audit, risk and compliance is quoted as a Petual user (S57). Grade C because all figures are vendor or investor claims."

- id: assurance-controls-testing-10
  title: AI-delivered co-sourced and outsourced SOX testing (service-model change)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, client-interaction]
  pattern: end-to-end-case-agent
  lens: reinvent
  ladder: delegate
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Companies outsource overflow SOX testing at high hourly rates. KPMG's survey found that 58% of companies using outsourced providers spend over 20% of their SOX budget on them."
  solution: >
    Advisory firms embed testing agents into co-source and outsource delivery. RSM's platform built
    with Andera reviews any evidence type, runs directed test steps and produces annotated
    documentation. Riveron places different agents at specific workflow steps, with a professional
    reviewing every result. AI-native start-ups present themselves as internal audit firms.
  outcomes:
    - {lever: growth, description: "RSM is extending the platform to middle-market internal audit; Andera says it is trusted by multiple Fortune 500 companies across SOX, KYC, PCI, AML and cyber testing", figure: "n/a", source_ref: S16}
  prerequisites: [Firm methodology encoded in agents, Client evidence access]
  risks_and_guardrails: ["Riveron: general-purpose LLMs used alone do not meet an audit-grade standard (S18)", "Measure shorter cycles and reviewable workpapers, not hours saved (S18)"]
  human_checkpoints: [Firm professional reviews every test result before the workpaper]
  role_evolution: "Co-source staffing shifts from testers to reviewers; pricing pressure on hourly models (Verdantix, S63)."
  evidence_grade: B
  sources:
    - {ref: S16, title: "Andera and RSM US Partner...", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/", date: 2026-08-26}
    - {ref: S18, title: "AI in Internal Audit and SOX: Applying Methods that Work", publisher: Riveron, type: firm, url: "https://riveron.com/ai-in-internal-audit-and-sox-applying-methods-that-work/", date: 2026-06-16}
    - {ref: S60, title: "Arden: AI-native internal audit firm", publisher: Y Combinator, type: vendor, url: "https://ycombinator.com/companies/arden", date: 2026}
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-11
  title: AI support across the SOC examination lifecycle (evidence, Section 3, deviation responses)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "SOC preparation involves heavy documentation: control descriptions mapped to the Trust Services Criteria, evidence snapshots, management responses to deviations, and security questionnaires."
  solution: "AI drafts control descriptions and the Section 3 system description, collects evidence continuously, drafts management responses to deviations, and tracks project status."
  outcomes:
    - {lever: capacity, description: "Share of EY SOC conference attendees using AI for each task (live poll)", figure: "evidence 63%; Section 3 45%; deviation responses 41%; project mgmt 29%", source_ref: S24}
  prerequisites: [AI inventory, Data governance]
  risks_and_guardrails: ["EY: AI may invent details and fill blanks; agents may rewrite themselves", "AICPA TQA 9561: AI in scope only where it affects in-scope services and controls; avoid scope inflation (S29)"]
  human_checkpoints: [Service auditor evaluates evidence and deviations, Management approves responses]
  role_evolution: "Service auditors and management spend less time on drafting."
  evidence_grade: C
  sources:
    - {ref: S24, title: "How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC conference)", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09}
    - {ref: S29, title: "AI in SOC Examinations: What the AICPA's New TQA Section 9561 Means", publisher: Schneider Downs, type: firm, url: "https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/", date: 2026-09-30}
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-12
  title: Compliance-automation platforms feeding SOC 2 examiners with continuously pulled evidence
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  lens: automate
  ladder: automate
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Clients submit dozens of screenshots and spreadsheets per SOC engagement; SOC 2 is a gating requirement for enterprise sales."
  solution: "Tools connect to the client's systems and pull evidence into a real-time dashboard that the CPA examiner tests against."
  outcomes:
    - {lever: speed, description: "SOC leaders agree the tools make the process quicker and more efficient (no figure)", figure: "n/a", source_ref: S25}
  prerequisites: [Independent examiner who designs their own procedures, Tailored risk assessment per client]
  risks_and_guardrails:
    - "AICPA Peer Review Board alert (May 2026): identical reports, risk assessments, sample sizes or procedures across clients can be judged nonconforming (S26)"
    - "AICPA ethics guidance: watch terms that shift control, judgment or evidence access to the tool provider (S27)"
    - "Delve allegations (unproven, denied): near-identical text in 493 of 494 reports and conclusions drafted before evidence arrived (S30, S31)"
  human_checkpoints: [Licensed CPA designs and executes tests and signs the opinion]
  role_evolution: "High-volume SOC practices face peer-review scrutiny. Linton (AICPA SOC 2 Working Group) warns that full financial audits may be targeted next."
  evidence_grade: C
  sources:
    - {ref: S25, title: "Promises of 'fast and easy' threaten SOC credibility", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/", date: 2026-02-01}
    - {ref: S26, title: "AICPA guides peer reviewers to address SOC 2 risks", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/", date: 2026-05-14}
    - {ref: S30, title: "Delve Allegations Expose Weak Points in Compliance", publisher: IANS Research, type: press, url: "https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/30/delve-allegations-expose-weak-points-in-modern-compliance", date: 2026-03-30}
  last_reviewed: 2026-10-16
  notes: "Included because it is the most contested change in SOC controls testing. The use case is real; the debate is about where automation replaces the examiner's own testing."

- id: assurance-controls-testing-13
  title: Testing controls that AI performs (AI-enabled controls in ICFR and SOC scope)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, software-systems, expert-judgment]
  pattern: other
  lens: reinvent
  ladder: augment
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Companies put GenAI and agents into close, approvals and access workflows. SOX programmes are still testing around the AI rather than relying on it, and there is no agreed method for testing a black-box control."
  solution: >
    Testing extends to model governance and AI-specific evidence: lineage, per-inference logs (model
    version, prompt hash, tool calls), drift monitoring, change tickets for model deployment, and
    subprocessor risk. COSO's GenAI guidance supplies control-testing templates for eight capability
    types.
  outcomes:
    - {lever: risk, description: "KPMG expects the first wave of AI-related material weaknesses in 2027", figure: "2027 (forecast)", source_ref: S01}
  prerequisites: [AI inventory mapped to the system boundary, Logging that produces evidence for agent actions]
  risks_and_guardrails:
    - "SOC 2 practitioner overlays are inconsistent, so two clean reports may test different AI controls (CSA, S28)"
    - "Agents acting without a human request create an accountability gap for access and change criteria (S28)"
    - "The AICPA practice aid (Oct 2026) promises further guidance on evaluating evidence when a company uses AI (S54)"
  human_checkpoints: [Auditor judges reliance on AI-performed controls]
  role_evolution: "Testers need fluency in model risk. KPMG says the skills are not core to the CPA curriculum."
  evidence_grade: C
  sources:
    - {ref: S01, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24}
    - {ref: S28, title: "The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted", publisher: Cloud Security Alliance, type: professional-body, url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/", date: 2026-08-30}
    - {ref: S55, title: "COSO creates audit-ready guidance for governing generative AI", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/", date: 2026-02-26}
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': assurance over AI-performed controls. Uniqus suggests companies with agentic AI in the close may want to keep a voluntary 404(b) attestation if the SEC filer proposal is adopted (S51)."

- id: assurance-controls-testing-14
  title: "Idea: agent and synthetic-data stress-testing of controls before an ERP go-live or acquisition"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: other
  lens: reinvent
  ladder: augment
  runtime_class: background-agent
  maturity: emerging
  problem: "The window between go-live and a stable, well-tested control environment is among the highest-risk periods for ICFR."
  solution: "Agents simulate users, transactions and edge cases, and synthetic transaction populations run through the new environment so failure modes are seen before real data."
  outcomes: []
  prerequisites: [Synthetic data that mirrors real populations, Test environment]
  risks_and_guardrails: ["Synthetic results are not audit evidence of operating effectiveness"]
  human_checkpoints: [Control designers review findings]
  role_evolution: "Moves controls testing upstream into implementation."
  evidence_grade: D
  sources:
    - {ref: S01, title: "The Future of SOX: A point of view for 2030 and beyond (POV 4)", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24}
  last_reviewed: 2026-10-16
  notes: "Idea. Discussed by KPMG; no deployment found."

- id: assurance-controls-testing-15
  title: "Idea: testing self-healing, embedded preventive controls through configuration and logic review"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [software-systems, review-assurance]
  pattern: other
  lens: reinvent
  ladder: augment
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Control sets lean on detective and manual controls. KPMG expects AI-driven controls that detect and fix anomalies in real time, which a sample of manual reviews cannot test."
  solution: "Test design shifts to system configuration, data logic and the conditions under which automation fails or is bypassed; external auditors put more weight on test of design."
  outcomes: []
  prerequisites: [IT audit skills, Configuration and change logs]
  risks_and_guardrails: ["Model drift can make an effective control ineffective with no visible change (S01)"]
  human_checkpoints: [Design evaluation by an IT auditor]
  role_evolution: "In KPMG's words, the auditor must be as comfortable in a configuration log as in a ledger."
  evidence_grade: D
  sources:
    - {ref: S01, title: "The Future of SOX (POV 2)", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24}
    - {ref: S03, title: "The 404(a) opportunity", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/404-opportunity.pdf", date: 2026-08}
  last_reviewed: 2026-10-16
  notes: "Idea."

- id: assurance-controls-testing-16
  title: "Idea: AI-assisted deviation evaluation and deficiency classification, with a deviation memory"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [expert-judgment]
  pattern: grounded-knowledge-assistant
  lens: improve
  ladder: assist
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Deciding whether a failure is a minor gap, a significant deficiency or a material weakness depends on enterprise context that is often unwritten, and past rationales are scattered."
  solution: "Teams record why past exceptions were accepted in one repository. An agent checks new exceptions against it and drafts a classification once a human supplies the context."
  outcomes: []
  prerequisites: [Central log of deviations and rationales]
  risks_and_guardrails: ["A general model sent the question cold gives a confident answer with no grounding (S07)"]
  human_checkpoints: [Auditor makes the classification]
  role_evolution: "Judgment stays human; preparation of the analysis is assisted."
  evidence_grade: D
  sources:
    - {ref: S07, title: "Agentic AI in Internal Audit: What to Automate First", publisher: Optro, type: vendor, url: "https://optro.ai/blog/agentic-ai-internal-audit-controls", date: 2026-08-11}
  last_reviewed: 2026-10-16
  notes: "Idea. Discussed by Optro and Confluent's CAE in a webinar; no deployment found."

- id: assurance-controls-testing-17
  title: Multi-agent "swarm" orchestration for internal audit analytics and testing
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: other
  lens: delegate
  ladder: delegate
  runtime_class: background-agent
  maturity: piloting
  problem: "Analytics and testing routines are built one by one, and moving AI from one system to another adds overhead (described as a 'bridge tax')."
  solution: "Prompt libraries plus orchestrated agents run analytics and tests together. Practitioners advise keeping the knowledge base separate from the AI engine."
  outcomes: []
  prerequisites: [Prompt library, Agent permission model]
  risks_and_guardrails: ["Agent permissions and the 'lethal trifecta' security risk (S12)", Balance automation with human oversight]
  human_checkpoints: [Auditor oversight of agent outputs]
  role_evolution: "Shifts auditors toward judgment, ethics and strategic oversight (S10)."
  evidence_grade: B
  sources:
    - {ref: S10, title: "How AI Agents are transforming internal audit (Richard Penfill, PayPal)", publisher: "Speaking of Risk and Audit (Richard Chambers)", type: podcast, url: "https://srapodcast.podbean.com/e/swarm-auditing-how-ai-agents-are-transforming-internal-audit", date: 2026-02-11}
    - {ref: S12, title: "Ep 296: Why Every Auditor Needs to Learn How AI Agents Work w/ Richard Penfil (AssureSwarm)", publisher: The Audit Podcast, type: podcast, url: "https://podcasts.apple.com/mx/podcast/the-audit-podcast/id1502796518", date: 2026-09-15}
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': multi-agent orchestration. Grade B because PayPal internal audit's use is described by its data-science lead (episode summary only; no figures). By September 2026 he had founded AssureSwarm."

- id: assurance-controls-testing-18
  title: "Idea: external auditor reliance redefined by AI-enabled management testing"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: other
  lens: reinvent
  ladder: augment
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "Reliance on management's or internal audit's testing has been the main efficiency lever for SOX. It may lose value if auditors can test 100% themselves."
  solution: "Either auditors use their own AI to test at scale and rely less, or management's AI testing meets the evidential bar and auditors rely more. Vendors already format workpapers for external-auditor reliance."
  outcomes: []
  prerequisites: [Shared evidence standards, Auditor acceptance of management's tool outputs]
  risks_and_guardrails: ["No regulator view yet on reliance on agent-produced testing", "With 404(b) possibly narrowing (SEC proposal, May 2026), reliance economics change (S51)"]
  human_checkpoints: [Engagement partner decides on reliance]
  role_evolution: "SOX teams invest in tooling to keep reliance; KPMG calls it a race to meet the evidential bar."
  evidence_grade: D
  sources:
    - {ref: S01, title: "The Future of SOX (POV 5)", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24}
    - {ref: S06, title: "Autonomous Controls Testing Will Redefine Internal Audit", publisher: Optro, type: vendor, url: "https://optro.ai/blog/autonomous-controls-testing-internal-audit", date: 2026-06-15}
  last_reviewed: 2026-10-16
  notes: "Idea and debate."

- id: assurance-controls-testing-19
  title: Firm-wide audit agents executing preliminary procedures and drafting preliminary conclusions for review
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  lens: delegate
  ladder: delegate
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Audit platforms hold many separate tools; teams orchestrate tasks across phases by hand."
  solution: >
    Network-wide agent frameworks inside the audit platform extract data, analyse evidence, draft
    documentation and develop preliminary conclusions for professionals to review. EY says agents are
    in all phases and targets end-to-end support by 2028.
  outcomes:
    - {lever: capacity, description: "Deployment scale (EY: 130,000 assurance staff; Deloitte: about 85,000)", figure: "130k / 85k practitioners", source_ref: S22}
    - {lever: speed, description: "PwC (separate programme) reports only modest busy-season time savings after year one", figure: "not quantified", source_ref: S21}
  prerequisites: [Central platform, Firm methodology encoded, Training programme]
  risks_and_guardrails: ["FRC: deficient output, misinterpretation and non-compliance risks; the human auditor is always accountable (S40)"]
  human_checkpoints: [Professionals review preliminary conclusions]
  role_evolution: "Deloitte's 'tutor mode' gives micro-training in context while staff supervise and validate agents."
  evidence_grade: B
  sources:
    - {ref: S22, title: "EY Rolls Out Agentic AI in Assurance Across Its Global Network", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/", date: 2026-04-07}
    - {ref: S23, title: "Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia", publisher: Deloitte, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: 2026-06-24}
  last_reviewed: 2026-10-16
  notes: "Not specific to controls testing. Neither firm says which control-testing steps the agents perform."

- id: assurance-controls-testing-20
  title: Predictive, risk-scored targeting of control testing
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: monitor-diagnose-act
  lens: improve
  ladder: augment
  runtime_class: background-agent
  maturity: announced
  problem: "Testing effort is spread by rotation and habit rather than by where control breakdowns are likely."
  solution: "Models trained on historical deficiencies and process data predict where controls are likely to fail; agents recommend starting risk scores with evidence for planning."
  outcomes: []
  prerequisites: [Historical deficiency data, GRC platform data]
  risks_and_guardrails: ["Scores need explainable evidence for scoping decisions"]
  human_checkpoints: [Audit leader approves scoping]
  role_evolution: "Planning becomes review of model-suggested priorities."
  evidence_grade: C
  sources:
    - {ref: S03, title: "The 404(a) opportunity", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/404-opportunity.pdf", date: 2026-08}
    - {ref: S04, title: "Optro Launches Domain-Trained Agents (Agentic Risk Assessment Scoring)", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14}
  last_reviewed: 2026-10-16
```

**Count by grade:** A = 3 (01, 02, 08) · B = 6 (04, 06, 07, 10, 17, 19) · C = 7 (03, 05, 09, 11, 12, 13, 20) · D = 4, all ideas (14, 15, 16, 18). Total 20.

---

## 3. Module notes

### Processes and key steps (work types)

- **Scoping and control rationalisation:** `expert-judgment`, `research-synthesis`. KPMG recommends a "controls clean-up" before layering on AI, because in its words AI magnifies a poorly designed environment (S01).
- **Walkthroughs and test of design:** `document-production`, `research-synthesis`. Test of design matters more as AI-enabled and automated controls spread (S03).
- **Evidence (PBC) request and collection:** `coordination-scheduling`, `data-reporting`.
- **Sample selection, or full-population runs:** `data-reporting`.
- **Attribute testing, tick-marking and reperformance:** `review-assurance`. ITGC testing (access, change) is usually the first to be automated (S07, S09).
- **Deviation evaluation and deficiency classification:** `expert-judgment`.
- **Workpaper documentation and review:** `document-production`, `review-assurance`.
- **Reporting:** deficiency reports, management responses, and SOC Section 3/4 content. `document-production`, `client-interaction`.
- **Reliance decisions:** the external auditor relying on management's or internal audit's work, and user auditors relying on SOC reports. `expert-judgment`.

### Common pain points

- **Rising SOX cost and effort.** KPMG's 2025 SOX survey found the cost of maintaining SOX controls rose 45% between its 2023 and 2025 surveys. Testing hours per control rose from 12 to 16 between FY2022 and FY2024, with ITGCs taking the most time. 52% of internal audit departments spent more than 40% of their hours on SOX (S01).
- **Evidence in many formats.** Practitioners describe PDFs, screenshots, emails, system logs, and in PwC's words a client who "may hand you a napkin" (S20). Missing support may reflect how a control was performed rather than a failure (S18).
- **Repeating the same work every year.** PwC's AI assurance leader noted that walkthroughs are repeated even when processes barely change (S20). Midship's founder described redrawing the same architecture for every walkthrough (S06).
- **Budgets.** In the IIA 2026 North American Pulse, as cited by Optro, only 23% of internal audit teams had budget increases and 19% had cuts (S07, S08).
- **Weak links to judgment work.** Riveron says test results are often not reviewable and that criteria, sampling logic and exception rules are under-specified (S18).

### Metrics and benchmarks

| Metric | Figure | Source |
|---|---|---|
| Internal audit using GenAI for audit testing | 30% (vs 60% for drafting issues/reports) | Gartner poll of 743, Aug 2026 (S49) |
| Reddit: controls automated in 3 months | 175 (>40% of SOX); testing time per control −60%; later >75% of SOX | Optro, Oct 2026 (S04) |
| Microsoft ITGC change-management agent | 850 h/yr; $185K/yr; built in 1–3 months | Microsoft FY26 (S14) |
| Microsoft internal audit (overall) | Report issuance 3→2 weeks; QA review effort about −50% | Microsoft FY26 (S15) |
| Midship (vendor claims) | 16 h → <15 min per test; up to 85% of SOX controls automatable; 70% time saved in year 1; 60% on first-draft workpapers | S09, S11, S07 |
| Petual (vendor claim) | 68–80% efficiency on SOX workflows | S57 |
| Thomson Reuters early adopters (vendor claim) | Up to 70% faster preparation and workpaper review | S62 |
| AI in SOC work (EY conference poll) | Evidence 63%; Section 3 45%; deviation responses 41%; project management 29% | S24 |
| Organisations that acted on a wrong agent output | 34%; 46% say staff spend more time checking AI; 9% have redesigned workflows for agents | Optro survey of 417 GRC and audit leaders, Oct 2026 (S05) |
| Auditor time spent on data collection and formatting | About 40% (as cited at GAM) | Baker Tilly, Apr 2026 (S44) |

No independent or academic measurement of the accuracy or quality of AI controls testing was found. All time savings are self-reported or vendor-reported.

### Guardrails and regulatory points

- **External audit:**
  - The PCAOB's AS 1105 and AS 2301 technology-assisted analysis amendments apply to calendar-2026 audits. They do not address AI specifically (S35).
  - QC 1000 takes effect on 15 December 2026, and the PCAOB is consulting on revisions to it (S37). Under QC 1000, approving AI tools is a quality-control matter (S36).
- **UK:** The FRC's guidance on generative and agentic AI (30 March 2026) sets out three risk types: deficient output, misinterpretation or misuse, and non-compliance with methodology. The human auditor is always accountable, and the guidance is "not a response to identified quality deficiencies" (S40, S39).
- **US private-company audits and SOC:**
  - The AICPA practice aid (13 October 2026) says the auditor remains responsible for the audit and the opinion. More guidance is promised on evidence when a company uses AI (S54).
  - TQA 9561 sets no new SOC criteria. AI comes into scope only where it touches in-scope services, and third-party AI providers are handled under the subservice-organisation model (S29).
  - The Peer Review Board's SOC 2 alert took effect 1 June 2026. Reviewers may select about five engagements from different partners and look for identical procedures (S26).
- **International:** The IAASB ISA 330/500/520 exposure drafts are principles-based and technology-neutral, and clarify the role of tests of controls. Comments are due 15 December 2026 (S52, S53).
- **Management side:** COSO's GenAI guidance (February 2026) defines eight capability types and provides control-testing templates (S55).
- **Documentation:** Practitioners say a generic note that an AI tool was used is not enough. The file must show the population covered, the items flagged, the follow-up, and where the reviewer's judgment entered (S35, S36).
- **Design guardrails practitioners name:**
  - Pair LLMs with deterministic or rules-based code (S33, S41).
  - Back-test agents on completed engagements, then ramp up gradually (S33).
  - Set human-approved criteria for when AI may auto-clear an item and when it must route to review, and enforce segregation of duties across AI-assisted workflows (S19).
  - Treat AI output as a first draft with a named reviewer (S44).
  - Agents should recognise when a task has moved outside their bounds and route it to a person (S07).

### Frontier signals (dated)

| Date | Signal | Source |
|---|---|---|
| 2025-09-15 | Midship launches on YC as an "end-to-end SOX automation platform", naming continuous monitoring as the next step | S61 |
| 2025-10-28 | PwC promises a tool for every audit step in 2026, with controls-testing automation planned to work like Evidence Match | S20 |
| 2025-12 | At the SEC/PCAOB conference, PCAOB staff say firms' adoption of AI will be an inspection focus; SEC OCA says existing standards "were not written" for AI | S38 |
| 2026-02-01 → 2026-05-14 | AICPA SOC 2 Working Group warns about "fast and easy" SOC; the Peer Review Board issues an alert; the Delve allegations follow (March–May) | S25, S26, S30 |
| 2026-03-09/11 | IIA GAM: "the rise of agentic AI" is the headline theme, with a pre-conference AI workshop; Baker Tilly calls 2026 "the year of execution" | S43, S44 |
| 2026-03-30 | FRC issues the first regulator guidance on generative and agentic AI in audit | S40 |
| 2026-05-06 | Optro acquires Midship and folds autonomous testing into Controls Management | S08 |
| 2026-05-19 | SEC filer-status proposal would remove 404(b) attestation for about 80.8% of reporting companies if adopted | S51 |
| 2026-05-21/22 | WCARS Seville sessions: "From Generative AI to agentic audit"; "Auditor judgment as a behavioral control mechanism in AI-driven audits"; an "agentic CA/CM" keynote | S46 |
| 2026-07-02 | PCAOB board member Botic, at an NACD event, says the regulator is still working out whether AI needs new standards or documentation rules | S37 |
| 2026-07-06 | MindBridge asks the PCAOB for guidance on investigation thresholds and on what a clean full-population result means for sufficiency | S34 |
| 2026-08-10 | Gartner poll: only 30% of audit teams use GenAI for testing; AI is "not generally resulting in transformation" | S49 |
| 2026-08-26 | RSM US and Andera launch an AI control-testing platform for internal audit | S16 |
| 2026-09-15 | Workiva launches automated testing for internal audit and GRC using evidence, attribute and testing agents | S17 |
| 2026-09-24 | KPMG *Future of SOX 2030*: continuous full-population assurance; first AI-related material weaknesses expected in 2027 | S01 |
| 2026-10-07 | PwC says the AI time savings are "not that drastic yet" after year one | S21 |
| 2026-10-08 → 2026-10-14 | Optro: 34% have acted on wrong agent output; days later, Autonomous Testing is extended beyond SOX to operational audit | S05, S04 |
| 2026-10-15 | Practitioner warns firms not to sell full-population testing as certainty | S33 |
| 2026-11-06/07 (scheduled) | 75th WCARS, "Taming the Autonomous Frontier: AI Governance and Continuous Auditing" | S45 |

### Workforce and role effects

- **Testers become reviewers and agent supervisors.**
  - Midship's founder talks about auditors managing AI agents and doing ad hoc testing (S09).
  - Riveron and Ledgerline describe hours moving to exceptions, control assessment and remediation (S18, S33).
  - Newell Brands' CAE says adoption depends on trust and on staff feeling supported (S17).
- **New hiring profiles.**
  - PwC is hiring engineers into assurance and wants dual-track CPA plus data or computer science graduates (S20).
  - KPMG says the skills needed to audit AI are not core to the CPA curriculum and points to audit data scientists and dual credentials (S01).
  - Reddit advertised a first-of-its-kind role to build an "AI-first" internal audit function, starting with agentic SOX testing (S64).
- **Pyramid pressure.** *The Accounting Podcast* describes lean senior teams overseeing automated systems, and a "verification tax" that slows headcount reduction (S70). The AAA 2026 workshop held a panel on how junior auditors use GenAI across fieldwork, including internal control analysis (S48).
- **Training.** Deloitte offers in-workflow "tutor mode" (S23). EY runs a global upskilling programme (S22). Baker Tilly reports a persistent competency gap (S44).

### Objections and concerns practitioners raise

- **Automation bias and empty human-in-the-loop review.** KPMG says a rubber-stamp approval step provides no real control value (S01). ICAEW says the FRC guidance covers automation bias in a single paragraph (S41). WCARS research addresses humanised AI and auditor reliance (S46).
- **Probabilistic outputs.** RSM UK's audit data analytics director says no tool can be guaranteed to give the right output every time, so rules-based tools should sit alongside GenAI (S41).
- **Agents acting wrongly or beyond their remit.** 34% have acted on wrong agent outputs (S05). EY says agents may rewrite themselves to work around anomalies (S24). There is an accountability gap for autonomous actions under SOC criteria (S28).
- **Prompt injection through evidence.** Control owners could plant instructions to mislead testing agents (S01).
- **Inspection uncertainty and over-auditing.** Firms run AI and manual procedures in parallel because they cannot be sure AI-only work will survive inspection (S34). CalCPA reports, unverified, that a PCAOB board member warned that exhaustive model-documentation demands could make AI costlier to defend than manual sampling (S35).
- **Expectation gap.** "We test everything" is not "nothing can be wrong" (S33).
- **Commoditisation and independence in SOC.** Templated reports, vendors steering clients to firms, and terms that shift control of evidence to tool providers (S25, S27).
- **Value not yet visible.** PwC calls the savings modest so far (S21). Gartner says AI use is mostly productivity, not transformation (S49). Optro reports 46% spend more time reviewing AI output (S05).
- **Smaller firms.** Smaller firms lack technology specialists and lean on vendors. ICAEW says the FRC guidance is thin on vendor management (S41).
- **Fee pressure.** The KPMG and Grant Thornton UK fee dispute raises the question of whether AI means cheaper assurance or repriced continuous assurance (S63).

### Interview probes

1. Which control types have you moved to agent testing? Which did you try and pull back from, and why (evidence format, judgment content, exception rate)?
2. When an agent marks a sample "pass", what exactly does the reviewer look at? How do you guard against rubber-stamping, and have you measured reviewer override or disagreement rates?
3. Has your external auditor relied on agent-produced testing or workpapers? What did they ask for (tool validation, logs, reperformance), and did reliance go up or down?
4. Did full-population or continuous testing change your exception volumes and your deficiency evaluation process? How do you set investigation thresholds, and document a clean result?
5. Which of your in-scope controls are now performed or influenced by AI, and how do you test them (logs, model change management, drift monitoring)? Are you testing around the AI or relying on it?

---

## 4. Sources

Read in full means the page or PDF was opened and its text read. "Search only" items are marked.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| S01 | The Future of SOX: A point of view for 2030 and beyond (PDF and article page) | KPMG LLP | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf ; https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html | 2026-09-24 |
| S02 | Seize the future: The agentic shift in SOX compliance | KPMG LLP | firm | https://kpmg.com/us/en/articles/2025/seize-the-future-the-agentic-shift-in-sox-compliance.html | 2025-08-06 |
| S03 | The 404(a) opportunity | KPMG LLP | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/404-opportunity.pdf | 2026-08 |
| S04 | Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance (CRX 2026) | Optro | vendor | https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance | 2026-10-14 |
| S05 | One in Three Organizations Say They Have Acted on Wrong Decisions Made by AI Agents | Optro | survey | https://optro.ai/blog/one-in-three-organizations-say-they-have-acted-on-wrong-decisions-made-by-ai-agents-optro-research-finds | 2026-10-08 |
| S06 | Autonomous Controls Testing Will Redefine Internal Audit (Kieran Taylor) | Optro | vendor | https://optro.ai/blog/autonomous-controls-testing-internal-audit | 2026-06-15 |
| S07 | Agentic AI in Internal Audit: What to Automate First | Optro | vendor | https://optro.ai/blog/agentic-ai-internal-audit-controls | 2026-08-11 |
| S08 | Optro Leads the Global Audit Transformation with the Acquisition of AI-Native Midship | Optro | vendor | https://optro.ai/blog/optro-leads-the-global-audit-transformation-with-the-acquisition-of-ai-native-midship | 2026-05-06 |
| S09 | From 16 Hours to 15 Minutes: Agentic AI Rewrites SOX Testing | Speaking of Risk and Audit (R. Chambers) | podcast | https://srapodcast.podbean.com/e/from-16-hours-to-15-minutes-agentic-ai-rewrites-sox-testing/ | 2026-05-28 |
| S10 | How AI Agents are transforming internal audit (R. Penfill, PayPal) | Speaking of Risk and Audit (R. Chambers) | podcast | https://srapodcast.podbean.com/e/swarm-auditing-how-ai-agents-are-transforming-internal-audit | 2026-02-11 |
| S11 | Inside the Optro acquisition of Midship (AI Governance Watch) | Optro TV | podcast | https://optro.ai/optro-tv/ai-governance-watch-podcast/inside-the-optro-acquisition-of-midship | 2026 (n.d.) |
| S12 | Ep 296: Why Every Auditor Needs to Learn How AI Agents Work w/ Richard Penfil (AssureSwarm) | The Audit Podcast (T. Russell) | podcast | https://podcasts.apple.com/mx/podcast/the-audit-podcast/id1502796518 | 2026-09-15 |
| S13 | Ep 293: The Future of Internal Audit: AI, Trust, and Human Judgment w/ Rania Bijlani | The Audit Podcast | podcast | https://podcasts.apple.com/mx/podcast/the-audit-podcast/id1502796518 | 2026-08-26 |
| S14 | SOX Change Management Testing Agent | Microsoft (Frontier Finance) | firm | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/SOX-Change-Management-Testing-Agent.pdf | FY2026 |
| S15 | AI solution overviews: Internal Audit | Microsoft (Frontier Finance) | firm | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf | FY2026 |
| S16 | Andera and RSM US Partner to Create AI-Enabled Control Testing Platform for Internal Audit | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/ | 2026-08-26 |
| S17 | Workiva Advances Regulatory Work with AI Innovation (Amplify 2026) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/09/15/workiva-advances-regulatory-work-with-ai-innovation/190227/ | 2026-09-15 |
| S18 | AI in Internal Audit and SOX: Applying Methods that Work (D. Niehaus) | Riveron | firm | https://riveron.com/ai-in-internal-audit-and-sox-applying-methods-that-work/ | 2026-06-16 |
| S19 | The power of AI in efficient SOX compliance | Grant Thornton | firm | https://grantthornton.com/insights/articles/advisory/2026/the-power-of-ai-in-efficient-sox-compliance | 2026-07-21 |
| S20 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 |
| S21 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 |
| S22 | EY Rolls Out Agentic AI in Assurance Across Its Global Network | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/ | 2026-04-07 |
| S23 | Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia | Deloitte | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 2026-06-24 |
| S24 | How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC conference highlights) | EY | conference | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf | 2026-09 |
| S25 | Promises of 'fast and easy' threaten SOC credibility | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/ | 2026-02-01 |
| S26 | AICPA guides peer reviewers to address SOC 2 risks | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/ | 2026-05-14 |
| S27 | The risks of quick-turn SOC engagements and what CPAs should know (A. Pawlicki) | JofA podcast (AICPA) | podcast | https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick‑turn-soc-engagements-and-what-cpas-should-know/ | 2026-04-30 |
| S28 | The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted | Cloud Security Alliance | professional-body | https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/ | 2026-08-30 |
| S29 | AI in SOC Examinations: What the AICPA's New TQA Section 9561 Means | Schneider Downs | firm | https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/ | 2026-09-30 |
| S30 | Delve Allegations Expose Weak Points in Compliance | IANS Research | press | https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/30/delve-allegations-expose-weak-points-in-modern-compliance | 2026-03-30 |
| S31 | SOC 2 Is Broken. The Delve Scandal Is Showing Us How. (C. Chio) | Corporate Compliance Insights | press | https://www.corporatecomplianceinsights.com/soc-2-broken-delve-scandal-shows/ | 2026-05-21 |
| S32 | Show HN: Ex-Deloitte auditor open-sourced the whole SOC 2 method (thread) | Hacker News | community | https://news.ycombinator.com/item?id=49171140 | 2026-08-04 |
| S33 | Testing Every Transaction Changes the Audit – Here's What Firms Should Know Before They Sell It (T. Adewole, Ledgerline) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/ | 2026-10-15 |
| S34 | MindBridge's Response to the PCAOB's Strategic Priorities on AI Audit | MindBridge | vendor | https://www.mindbridge.ai/blog/pcaob-ai-audit-strategic-priorities/ | 2026-07-06 |
| S35 | AI Standard Setting, Regulation in Audit: Part 1 (S. Gadzhieva) | CalCPA | professional-body | https://www.calcpa.org/whats-happening/articles/ai-standard-setting-regulation-in-audit-part-1 | 2026-08 (approx.) |
| S36 | PCAOB AI oversight: where the Board stands on AI in audit | Fieldguide | vendor | https://www.fieldguide.io/resource-articles/pcaob-ai-audit-standards | 2026 (n.d.) |
| S37 | What Directors Should be Asking About the Audit and the Auditors Now (PCAOB board member G. Botic at NACD) | Foley & Lardner | firm | https://www.foley.com/insights/publications/2026/07/what-directors-should-be-asking-about-the-audit-and-the-auditors-now/ | 2026-07-02 |
| S38 | AICPA & CIMA Conference on Current SEC and PCAOB Developments 2025: key takeaways | Deloitte DART | conference | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways | 2025-12 |
| S39 | Auditors warned they remain accountable despite use of AI | Board Agenda | press | https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/ | 2026-03-31 |
| S40 | Innovative new guidance supports audit firm adoption of emerging AI technologies | FRC | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 |
| S41 | How helpful is FRC's guidance on generative and agentic AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai | 2026-05 |
| S42 | How should audit firms use AI? (FRC, Grant Thornton, Deloitte guests) | ICAEW Beyond Finance podcast | podcast | https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai | 2025-11-11 |
| S43 | IIA Great Audit Minds Conference to be held March 9–11 in Las Vegas | The IIA | conference | https://www.theiia.org/en/content/communications/press-releases/2026/the-institute-of-internal-auditors-great-audit-minds-conference-to-be-held-march-9-11-in-las-vegas/ | 2026-02-03 |
| S44 | Strategy in motion: Internal audit's 2026 execution mandate (GAM 2026 takeaways) | Baker Tilly | firm | https://www.bakertilly.com/insights/internal-audit-2026-execution-mandate | 2026-04-10 |
| S45 | 75th World Continuous Auditing & Reporting Symposium | Rutgers CAR Lab | conference | https://raw.rutgers.edu/75wcars.html | 2026 (event Nov 6–7) |
| S46 | 70th WCARS programme, Seville | Rutgers / Universidad Pablo de Olavide | conference | https://raw.rutgers.edu/70wcars/70%20WCARS%20Programa_4as.pdf | 2026-05-21 |
| S47 | 69th World Continuous Auditing & Reporting Symposium | Rutgers CAR Lab | conference | https://raw.rutgers.edu/69wcars.html | 2025-11-07 |
| S48 | 2026 Auditing Section Midyear Meeting: Excellence in Auditing Education workshop | American Accounting Association | conference | https://aaahq.org/Meetings/2026/Auditing-Section-Midyear-Meeting/Workshop | 2026-01 |
| S49 | Gartner Survey Finds Audit Teams' AI Use is Common, But Most Teams are Lacking Strategic Adoption | Gartner | survey | https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-08-10-gartner-survey-finds-audit-teams-ai-use-is-common-but-most | 2026-08-10 |
| S50 | Deloitte Sees Internal Audit Moving Closer to the Center of Enterprise Risk in 2026 | GRC Report | press | https://www.grcreport.com/post/deloitte-sees-internal-audit-moving-closer-to-the-center-of-enterprise-risk-in-2026 | 2026-05-29 |
| S51 | What the SEC's Filer Status Overhaul Means for ICFR Governance | Uniqus | firm | https://uniqus.com/what-the-secs-filer-status-overhaul-means-for-icfr-governance/ | 2026-06-04 |
| S52 | IAASB proposes to revise audit standards for new risks and tech | Accounting Today | press | https://www.accountingtoday.com/news/iaasb-proposes-to-revise-audit-standards-for-new-risks-and-tech | 2026-08-05 |
| S53 | Proposed Revisions for Audit Evidence & Risk Response: ISA 330, ISA 500 & ISA 520 | IAASB | standard-setter | https://www.iaasb.org/publications/proposed-revisions-audit-evidence-risk-response-isa-330-isa-500-isa-520 | 2026-08 |
| S54 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| S55 | COSO creates audit-ready guidance for governing generative AI | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ | 2026-02-26 |
| S56 | Investing in Petual | Andreessen Horowitz | vendor | https://a16z.com/announcement/investing-in-petual/ | 2026-04-23 |
| S57 | Petual raises $20m for AI-powered SOX compliance | FinTech Global | press | https://fintech.global/2026/04/24/petual-raises-20m-for-ai-powered-sox-compliance/ | 2026-04-24 |
| S58 | Andera raises $37m to automate internal audit | FinTech Global | press | https://fintech.global/2026/06/22/andera-raises-37m-to-automate-internal-audit/ | 2026-06-22 |
| S59 | Fieldguide raises $75M on $700M valuation to scale agentic AI | SiliconANGLE | press | https://siliconangle.com/2026/02/02/fieldguide-raises-75m-700m-valuation-scale-agentic-ai-audit-advisory-firms/ | 2026-02-02 |
| S60 | Arden: AI-native internal audit firm | Y Combinator | vendor | https://ycombinator.com/companies/arden | 2026 |
| S61 | Midship – AI for SOX Testing (YC launch post) | Y Combinator | vendor | https://www.ycombinator.com/launches/OOf-midship-ai-for-sox-testing | 2025-09-15 |
| S62 | Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html | 2025-11-05 |
| S63 | What Goes Around Comes Around: KPMG's AI-Driven Fee Argument | Verdantix | press | https://www.verdantix.com/venture/blog/what-goes-around-comes-around--kpmg-s-ai-driven-fee-argument-raises-uncomfortable-questions-about-audit-pricing-models | 2026 (n.d.; about Feb) |
| S64 | Senior, Business Risk & AI Automation (Reddit; expired listing) | Reddit via Working Nomads | job-posting | https://www.workingnomads.com/jobs/senior-business-risk-ai-automation-reddit | 2026 (n.d.) |
| S65 | Supervised AI Agents as Internal Audit Team Members (webcast) | Washington Society of CPAs | professional-body | https://www.wscpa.org/cpe/245647imp:supervised-ai-agents-as-internal-audit-team-members-webcast | 2026-11-07 (scheduled) |
| S66 | AAFCPAs Takes the Stage at AICPA ENGAGE 2026 (AI and analytics in audit session with Caseware) | AAFCPAs | conference | https://aafcpa.com/2026/05/20/aafcpas-takes-the-stage-at-aicpa-engage-2026/ | 2026-05-20 |
| S67 | IIA GAM 2025 Recap: The AI-Powered Future of Internal Audit is Here | MindBridge | vendor | https://www.mindbridge.ai/blog/iia-gam-2025-recap-the-ai-powered-future-of-internal-audit-is-here/ | 2025-03-17 |
| S68 | ISACA's 2026 North America Conference to Highlight Governance and Trust in Emerging Technologies | ISACA | conference | https://www.isaca.org/about-us/newsroom/press-releases/2026/isacas-2026-north-america-conference-to-highlight-governance-and-trust-in-emerging-technologies | 2026 |
| S69 | AI Isn't a Threat to Auditors—It's the Key to Elevating the Profession (S. D. Sampa, ISACA) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/12/02/ai-isnt-a-threat-to-auditors-its-the-key-to-elevating-the-profession/174120/ | 2025-12-02 |
| S70 | The Accounting Podcast (episode summaries: "verification tax", lean senior teams) | Podwise / The Accounting Podcast | podcast | https://podwise.ai/podcasts/18626 | 2026 (n.d.) |
| S71 | Testing Gen AI platforms: can they do audit work? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work | 2025-09 |
| S72 | AI Implementation Guide: SOX Testing; Gartner case study on Xerox's AI for SOX execution (search only) | Gartner | survey | https://www.gartner.com/en/documents/7766321 | 2026-04-28 / 2026-05 |
| S73 | SEC filer status proposal coverage (search only: Weaver, Goodwin, Faegre Drinker, Cleary) | various | press | https://www.goodwinlaw.com/en/insights/publications/2026/10/alerts-practices-pcap-secs-filer-status-proposal-key-themes-emerging | 2026-05 to 2026-10 |

**Source count by type (73 refs):** press 17 · firm 12 · vendor 11 · conference 9 · professional-body 9 · podcast 8 · survey 3 · community 1 · job-posting 1 · regulator 1 · standard-setter 1. The total includes two items seen in search only (S72, S73). About 70 distinct pages and PDFs were opened and read; about 20 further items were seen only in search results.

---

## 5. Gaps

- **Could not reach (automated access refused):**
  - pcaobus.org returned a Cloudflare challenge (403), so PCAOB speeches, Release 2026-005 and the inspection reports were not read. The CalCPA claim that recent PCAOB inspection reports cite AI-assisted journal-entry anomaly detection, and that a board member warned against "turn over every rock" documentation demands, could not be verified (S35).
  - gartner.com research documents returned 403. The *AI Implementation Guide: SOX Testing* and the Xerox case study were seen only as search abstracts.
  - Also refused: Reddit (403, so r/InternalAudit and r/Accounting were not read), Going Concern (403), Protiviti's blog (429), the FEI CCR comment letter to the PCAOB (403), Crowe (403), the Ideagen IIA 2025 recap (404), and the JofA February 2026 cover story "How AI is transforming the audit" (the NJCPA mirror returned 404).
  - WebFetch failed with DNS errors for every host. All pages were read with curl.
- **Conference content:** No session recordings or slide decks were found for CRX 2026, GAM 2026, ENGAGE 2026, ISACA NA 2026, IIA International 2026 or DCPA 2025. Discourse from these events is known only through press releases, vendor recaps and firm takeaways. The SEC/PCAOB conference in December 2026 has not yet happened.
- **Community discussion is thin.** Only Hacker News threads could be reached, and they were mostly about SOC 2. LinkedIn was not used. No practitioner forum debate about the reliability of AI controls testing was reachable.
- **No independent outcome evidence.** Every time-saving figure is self-reported or vendor-reported. No study measured the accuracy of agentic attribute testing, false-pass rates, or reviewer override rates. No regulator inspection finding specific to AI in tests of controls was found.
- **External auditors' tests of controls.** No Big Four firm has publicly described agents performing ICFR tests of operating effectiveness with measured results. PwC's controls-testing automation was still "expected" as of October 2025, with no later confirmation.
- **Unresolved claims:**
  - The Delve allegations are unproven and denied (S30, S31).
  - Baker Tilly's statement that the EU AI Act "explicitly" classifies audit AI as high risk (S44) conflicts with the landscape note that this is contested, so it was not used as fact.
  - IIA 2026 Pulse AI-usage figures were available only from secondary blogs.
  - The landscape's Microsoft "850 vs 50 hours" conflict appears to be a PDF glyph-extraction artefact, not two different figures (see use case 02).
