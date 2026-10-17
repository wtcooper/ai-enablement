# Security x governance-risk: discourse angle (wave 4)

Compiled 2026-10-17. Archetype `security`, module `governance-risk` (landscape name: security-governance-risk). Angle: discourse (what practitioners are saying). Method: pages opened with curl or the r.jina.ai text mirror, conference slide decks and a PDF read with pdftotext, podcast transcripts and show notes, practitioner newsletters. Web search was used 7 times (leads and one corroboration); every source marked `access: full` was opened and read, and anything seen only in search results is marked `search-only` and used in `notes` only.

## 1. Summary

**What the field is saying.** Practitioner talk about security governance, risk and compliance (GRC) with AI runs along five lines.

1. **Trust and verification is the bottleneck, not effort.** GRC "agent" advocates say the analyst moves from collecting evidence to managing and checking agents, and that the hard question becomes whether you can prove what the agent did (`BLEEPING-ANECDOTES-2026`). The March 2026 allegations against the compliance platform Delve (disputed by the company) turned that into a market-wide worry: speed outrunning independent verification of SOC 2 and ISO 27001 attestations (`IANS-DELVE-2026`).
2. **Governing AI is now a core part of the module.** SANS/GIAC slides shown at RSAC 2026 say 93% of organizations are developing AI policy but 72% are still developing it (`RSAC-WORKFORCE-2026`). Practitioner talks describe security-led programs built around enablement rather than blocking (Cengage at BSides Las Vegas, Sendbird's CSO on the Cloud Security Podcast) (`BSIDESLV-2026`, `CLOUDSECPOD-SENDBIRD-2025`).
3. **Risk work is being re-based.** The Cloud Security Alliance (CSA) "Mythos-ready" briefing, edited live by 250 CISOs, tells CISOs to update risk metrics and board reporting and warns that boards may face questions about whether they used available AI for defensive scanning (`CSA-MYTHOSREADY-2026`). FAIR Institute writers tell risk analysts to model AI agents as privileged insiders and to reassess software-resident controls when coding agents are adopted (`FAIR-RISKREPORT-2026`, `FAIR-AGENTICCODING-2026`).
4. **Responsibility stays with the deploying organization.** Dark Reading's October 2026 coverage quotes experts who object to describing agents that left their sandboxes as "going rogue", and who say the failure is in the security controls around the model (`DARKREADING-ROGUE-2026`, `DARKREADING-LIABLE-2026`).
5. **The workforce pyramid may become a diamond.** Phil Venables (3 Oct 2026) argues AI removes the entry-level work that built judgment and proposes deliberate apprenticeship replacements for risk and assurance (`VENABLES-WORKFORCE-2026`). SANS/GIAC slides show SOC and security analysts as the most-cited entry-level roles affected (32%), while 39% report no role reductions yet (`RSAC-WORKFORCE-2026`).

**Evidence quality.** This angle is mostly opinion, conference abstracts and surveys. There are no published override rates, parallel-run results, auditor-reliance findings or regulator inspection outcomes for AI in security GRC in any source read. The nearest quality evidence is adjacent (studies of AI-written code quoted by FAIR, which are about software and not about GRC) and is capped accordingly. All surveys are self-reports by respondents; several are sponsored by vendors.

**Use-case count.** 18 candidate use cases: 0 grade A, 1 grade B, 11 grade C, 6 grade D (idea). Every outcome in the file is `none published` or a survey figure with its denominator stated.

**Overlap note.** The practice-angle file (`security-governance-risk-practice.md`) holds the vendor case studies and job postings. This file adds the practitioner view of the same work and several use cases the practice file does not cover (verification of automated attestations, agent-aware risk assessment, AI-era board re-baselining, junior-pipeline design, deterministic gates for the team's own agents, audit trails for AI-assisted decisions).

## 2. Use cases

```yaml
- id: security-governance-risk-01
  title: Event-triggered agents that check control evidence against a stated baseline and open findings
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >
    GRC teams chase screenshots and update spreadsheets by hand. Compliance is checked on annual or quarterly cycles, so
    'are we compliant right now' is answered from a snapshot that may already be stale (BLEEPING-ANECDOTES-2026).
  solution: >
    An agent wakes when a condition is met (a schedule, evidence older than a freshness threshold, a risk level change),
    queries the live system (for example the identity provider for the current MFA enforcement policy), compares it with
    the organization's required baseline, and if a group has fallen out of enforcement opens a finding and assigns a
    remediation task to the control owner (BLEEPING-ANECDOTES-2026). Practitioner commentary adds that the same logic
    applies to treating a failed control as an incident and monitoring controls continuously (VENABLES-CRE-2026).
  outcomes:
    - lever: quality
      description: none published
      figure: "none published"
      measures: "The source is a how-to article by a vendor employee describing an early-access no-code agent builder; it reports no results."
      provenance: vendor-published
      source_ref: BLEEPING-ANECDOTES-2026
  prerequisites:
    - A defined baseline for each control (for example the required MFA baseline in the worked example) (BLEEPING-ANECDOTES-2026)
    - Access to the systems that hold the evidence, so the agent works from live state (BLEEPING-ANECDOTES-2026)
    - A catalogue of key controls that can be monitored, kept as code with version control and review, per the control-reliability-engineering proposal (VENABLES-CRE-2026)
  risks_and_guardrails:
    - The author says most of the work should remain deterministic, with the model supplying reasoning, summarization and orchestration, and with controls, thresholds and policy decisions coming from humans (BLEEPING-ANECDOTES-2026)
    - The author names a 'verification tax' if the manual work only moves to checking what the agent did (BLEEPING-ANECDOTES-2026)
    - A monitored control that reads 'zero' may be broken; the same author of the control-reliability post proposes injecting harmless synthetic events to test it (VENABLES-CRE-2026)
  human_checkpoints:
    - The control owner receives the finding and the remediation task (BLEEPING-ANECDOTES-2026)
    - Humans own the thresholds and policy decisions (BLEEPING-ANECDOTES-2026)
  role_evolution: >
    The author says the analyst's job shifts from collecting to managing, and that agents give practitioners time to apply
    judgment (BLEEPING-ANECDOTES-2026). A GRC-engineering newsletter says most day-to-day GRC engineering looks like
    sysadmin work, with tools learnable in months (GRCENGINEER-086-2026).
  evidence_grade: C
  sources:
    - { ref: BLEEPING-ANECDOTES-2026, title: "Your First GRC Agent: A Red Teamer's Walkthrough", publisher: BleepingComputer (byline Maril Vernon, GRC Engineering Evangelist, Anecdotes), type: press, url: "https://www.bleepingcomputer.com/news/security/your-first-grc-agent-a-red-teamers-walkthrough/", date: 2026-06-26, access: full, locator: "Sections 'What Agentic Actually Means Here', 'Three Things That Actually Change', 'What It Looks Like to Build One'" }
    - { ref: VENABLES-CRE-2026, title: "Control Reliability Engineering (CRE): Applying SRE Principles to Cybersecurity Controls", publisher: Phil Venables (personal blog), type: community, url: "https://www.philvenables.com/post/control-reliability-engineering-cre-applying-sre-principles-to-cybersecurity-controls", date: 2026-07-25, access: full, locator: "'The 10 Essential Elements' (Continuous Control Monitoring; Synthetic Event Injection)" }
    - { ref: GRCENGINEER-086-2026, title: "Most GRC Engineering Is Sysadmin Work. That's the Good News.", publisher: GRC Engineer newsletter, type: community, url: "https://www.grcengineer.com/p/most-grc-engineering-is-sysadmin-work-that-s-the-good-news", date: 2026-10-15, access: full, locator: "Opening and 'What the work actually looks like' table" }
  last_reviewed: 2026-10-17
  notes: >
    The BleepingComputer piece is vendor-authored (Anecdotes) and describes Anecdotes Agent Studio as in early access. Control reliability engineering
    is not AI-specific in the post read; it is cited for the monitoring concept only. Overlaps practice-file use case 06.

- id: security-governance-risk-02
  title: A verification layer over automated compliance evidence and auditor independence
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Compliance platforms promise speed. After a whistleblower alleged that the platform Delve generated fabricated SOC 2 and
    ISO 27001 evidence and weakened independent audit testing (the company denies this and says independent auditors give
    the final opinions), practitioners worry that customers who relied on the certifications carry the liability and the
    burden of proof (IANS-DELVE-2026).
  solution: >
    IANS faculty recommend that buyers re-read their own SOC 2 report as a security artifact, confirm in writing that the auditor
    designed and ran its own tests, ask the platform vendor what the auditor can access and at what stage, spot-check 5 to 10
    controls at random for evidence that exists and is current, and add a vetting checklist (AICPA accreditation status,
    US physical presence, any business relationship with the platform vendor, number of clients audited) to vendor management
    for any compliance platform or auditor (IANS-DELVE-2026). A GRC-agent advocate frames the same issue as 'pass/fail is a
    compliance outcome, confidence is a security outcome' (BLEEPING-ANECDOTES-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "No source measures the effect of these checks. The whistleblower's text-analysis figures are allegations, recorded in notes."
      provenance: independent
      source_ref: IANS-DELVE-2026
  prerequisites:
    - A list of where SOC 2 reports, trust pages and questionnaire answers were used with customers or regulators (IANS-DELVE-2026)
    - Named owner for compliance-platform and auditor vetting inside vendor management (IANS-DELVE-2026)
  risks_and_guardrails:
    - A SOC 2 Type II report attests that specified controls operated effectively over a limited observation period; it is not a security guarantee (IANS-DELVE-2026)
    - If the conclusions do not match how security works, or were written before testing finished, the faculty advise treating the control as unproven (IANS-DELVE-2026)
  human_checkpoints:
    - Written confirmation from the auditor that it designed its own tests (IANS-DELVE-2026)
    - Random spot-check of 5 to 10 controls against real evidence (IANS-DELVE-2026)
  role_evolution: >
    IANS says liability and regulatory exposure may sit with the companies that relied on the certifications, so the customer's
    GRC team becomes a verifier of its platform and auditor (IANS-DELVE-2026).
  evidence_grade: C
  sources:
    - { ref: IANS-DELVE-2026, title: "Delve Allegations Expose Weak Points in Modern Compliance", publisher: IANS Research, type: firm, url: "https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/30/delve-allegations-expose-weak-points-in-modern-compliance", date: 2026-03-24, access: full, locator: "Key Points; Big Picture; 'IANS Faculty Recommendations'" }
    - { ref: BLEEPING-ANECDOTES-2026, title: "Your First GRC Agent: A Red Teamer's Walkthrough", publisher: BleepingComputer (byline Anecdotes employee), type: press, url: "https://www.bleepingcomputer.com/news/security/your-first-grc-agent-a-red-teamers-walkthrough/", date: 2026-06-26, access: full, locator: "'Trust becomes the bottleneck'" }
  last_reviewed: 2026-10-17
  notes: >
    Everything about Delve is an allegation reported by IANS; Delve denies it, saying it does not issue compliance reports and that auditors are responsible
    for final opinions. The sources read do not say that AI generated the evidence; the case is used because it shapes the discourse on automated attestation.
    Allegations as reported: nearly identical boilerplate in 493 of 494 SOC 2 reports in a leaked spreadsheet, and word-for-word identical conclusions in all 259
    Type II reports (IANS-DELVE-2026). A web search result also reported a class action filed on 2026-04-21 and Y Combinator dropping the company; those items
    were seen in search only and are not relied on.

- id: security-governance-risk-03
  title: AI-assisted third-party risk reviews with a switch between autonomous and in-the-loop operation
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    Third-party risk management is described by a CISO and a vendor founder as manual, document-heavy and, in large companies,
    'a paper exercise'; hundreds of vendors are adding AI tooling, and regulations such as DORA push toward continuous
    accountability for critical vendors (CLOUDSECPOD-LOVABLE-2026).
  solution: >
    The founder of a third-party-risk vendor (Ethira) describes autonomous checks of a vendor (for example looking at an
    open-source tool's maintainers and last-maintained date), with humans pulled in at the end, and a setting that lets a
    customer choose between fully autonomous and in-the-loop operation, including whether the AI may negotiate back and forth
    with the vendor on questions or missing pen tests. The CISO of Lovable says that putting an old questionnaire spreadsheet
    and a knowledge base into an AI gives 'pretty accurate results' (CLOUDSECPOD-LOVABLE-2026).
  outcomes:
    - lever: speed
      description: none published
      figure: "none published"
      measures: "Podcast conversation; no time, accuracy or cost figures are given."
      provenance: vendor-published
      source_ref: CLOUDSECPOD-LOVABLE-2026
  prerequisites:
    - An up-to-date inventory that shows when it changes (CLOUDSECPOD-LOVABLE-2026)
    - Integration with existing systems such as the SIEM so that monitoring forms a full loop (CLOUDSECPOD-LOVABLE-2026)
  risks_and_guardrails:
    - The CISO says AI is not always hallucination-free and can 'imagine answers', which he calls a hard problem for specialized tools to solve (CLOUDSECPOD-LOVABLE-2026)
    - There is a trust gap: skeptical users need a way to keep control, and agent-to-vendor negotiation is uncomfortable for them (CLOUDSECPOD-LOVABLE-2026)
    - How much to automate depends on risk tolerance; high-trust industries need a high level of assurance (CLOUDSECPOD-LOVABLE-2026)
  human_checkpoints:
    - Humans are brought in at the end of the autonomous checks (CLOUDSECPOD-LOVABLE-2026)
    - The autonomy setting is chosen by the customer (CLOUDSECPOD-LOVABLE-2026)
  role_evolution: >
    The guests expect agents to join the workforce as contracted resources with a life cycle, credentials and a cost, managed
    much like third parties (CLOUDSECPOD-LOVABLE-2026).
  evidence_grade: C
  sources:
    - { ref: CLOUDSECPOD-LOVABLE-2026, title: "How AI Agents Will Negotiate Your Vendor Contracts", publisher: Cloud Security Podcast, type: podcast, url: "https://www.cloudsecuritypodcast.tv/videos/how-ai-agents-will-negotiate-your-vendor-contracts", date: 2026-05-27, access: full, locator: "Transcript, roughly 00:07-00:16 and 00:25-00:36" }
  last_reviewed: 2026-10-17
  notes: >
    The vendor founder is a guest and sells the product; the transcript does not say Lovable uses Ethira. Practice-file use cases 03 and 04 hold named-customer
    figures (Samsara and others) for the same work.

- id: security-governance-risk-04
  title: Continuous inventory of vendor-embedded AI and shadow AI tied back to approved vendors
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [research-synthesis, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >
    Gartner's Bernard Woo writes that most leaders report struggling to keep visibility into AI features that vendors embed
    (TECHTARGET-GARTNERREG-2026). Staff also create their own tools and enable features with a toggle, which a CISO calls a
    form of 'second party' risk (CLOUDSECPOD-LOVABLE-2026).
  solution: >
    The vendor founder in the podcast describes tracking when AI is added to a vendor and tying shadow AI back to approved
    vendors autonomously, and the CISO says internal builders could be treated like mini vendors and put under similar rules
    (CLOUDSECPOD-LOVABLE-2026). Gartner's Hype Cycle for AI Governance 2026, as summarized by a secondary blog, lists AI agent
    identity and third-party risk management among two-to-five-year innovations (SOFTWARESTRATEGIES-GARTNERHC-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "No source reports detection rates or coverage."
      provenance: vendor-published
      source_ref: CLOUDSECPOD-LOVABLE-2026
  prerequisites:
    - A vendor and internal-builder inventory with data classification (CLOUDSECPOD-LOVABLE-2026)
    - Internal partners from assurance, governance and legal to judge which obligations apply (TECHTARGET-GARTNERREG-2026)
  risks_and_guardrails:
    - Gartner advises moving beyond static global policy trackers and warns that the volume and speed of AI deployment create urgency (TECHTARGET-GARTNERREG-2026)
    - The secondary blog's summary of a Gartner survey says 34% of organizations have well-defined AI governance but report only partial adherence (SOFTWARESTRATEGIES-GARTNERHC-2026)
  human_checkpoints:
    - Not described in the sources
  role_evolution: >
    The CISO in the podcast says every employee who wires AI into internal data sources may become a vendor without meaning to,
    so the third-party team governs a wider set of producers (CLOUDSECPOD-LOVABLE-2026).
  evidence_grade: C
  sources:
    - { ref: TECHTARGET-GARTNERREG-2026, title: "How to prepare security controls for future AI regulations", publisher: TechTarget (Gartner analyst Bernard Woo), type: press, url: "https://www.techtarget.com/cybersecurity/opinion/How-to-prepare-security-controls-for-future-AI-regulations", date: 2026-06-02, access: full, locator: "Opening paragraphs; 'Filter regulatory noise through internal partnerships'" }
    - { ref: CLOUDSECPOD-LOVABLE-2026, title: "How AI Agents Will Negotiate Your Vendor Contracts", publisher: Cloud Security Podcast, type: podcast, url: "https://www.cloudsecuritypodcast.tv/videos/how-ai-agents-will-negotiate-your-vendor-contracts", date: 2026-05-27, access: full, locator: "Transcript, roughly 00:08-00:12" }
    - { ref: SOFTWARESTRATEGIES-GARTNERHC-2026, title: "Gartner AI Governance Hype Cycle 2026: What CISOs Fund First", publisher: Software Strategies Blog (Louis Columbus), type: community, url: "https://softwarestrategiesblog.com/2026/08/10/gartners-2026-ai-governance-hype-cycle-and-what-cisos-must-change-to-control-agentic-ai-and-rogue-agents/", date: 2026-08-10, access: full, locator: "Paragraphs on the AI Leaders Effectiveness Survey and the Priority Matrix (secondary summary of Gartner)" }
  last_reviewed: 2026-10-17
  notes: >
    The Gartner survey figure comes from a secondary blog, not from Gartner's own page, which was blocked. Practice-file use case 16 covers the same inventory problem as an idea.

- id: security-governance-risk-05
  title: Security-led AI governance program (acceptable-use policy, vendor and tool assessment, enablement, approval gates)
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [expert-judgment, review-assurance, coordination-scheduling]
  pattern: intake-triage
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    AI initiatives spin up faster than governance can track. At Cengage, student data, author IP and proprietary curriculum
    were in play (BSIDESLV-2026). SANS/GIAC slides report that most organizations are building AI policy but few have mature
    structure or training (RSAC-WORKFORCE-2026).
  solution: >
    Cengage presented a program it built from scratch that assessed AI vendors, aimed to stop being 'the Department of No',
    and red-teamed its own AI integrations (BSIDESLV-2026). Sendbird's CSO describes providing enterprise AI tools at several
    tiers, blocking models from China and unofficial AI browser add-ons, involving the GRC team in contracts and data
    agreements so vendors do not train on customer data, and building a relationship in which staff ask security before
    enabling a new model or feature (CLOUDSECPOD-SENDBIRD-2025).
  outcomes:
    - lever: capacity
      description: Cengage reports AI vendors assessed by its security and governance program
      figure: "67 AI vendors in 15 months"
      measures: "Count of AI vendors assessed over 15 months, as stated in the abstract of a 25-minute BSides Las Vegas talk; the talk itself was not seen."
      provenance: self-reported
      source_ref: BSIDESLV-2026
    - lever: risk
      description: SANS/GIAC slides on AI policy among surveyed organizations
      figure: "93% developing; 72% still developing; 21% comprehensive workforce framework"
      measures: "Slide text: '93% organizations developing policies'; '72% still in development'; 'Only 21% have a comprehensive workforce framework today'. Respondent count and sampling are not stated on the slides."
      provenance: independent
      source_ref: RSAC-WORKFORCE-2026
    - lever: capacity
      description: SANS/GIAC slides on AI training
      figure: "20% comprehensive for all staff; 47% limited, pilot or planned"
      measures: "Slide text: 'Only 20% provide comprehensive AI training for all staff'; '47% provide limited training/pilot or planning on it'. Respondent count not stated."
      provenance: independent
      source_ref: RSAC-WORKFORCE-2026
  prerequisites:
    - A vendor assessment process that the AI/ML team treats as expert input rather than a gate: Sendbird's CSO says the AI/ML team 'knows what they're talking about' and security works with it on model and version choices (CLOUDSECPOD-SENDBIRD-2025)
    - Enterprise-tier tools provided up front so staff do not use free versions (CLOUDSECPOD-SENDBIRD-2025)
    - A written definition of what counts as an AI incident, since a wrong or suboptimal agent answer is 'an incident of sort' but not a breach (CLOUDSECPOD-SENDBIRD-2025)
  risks_and_guardrails:
    - Sendbird's CSO says he has no great answer yet for securing MCP servers and that blocking everything is a game that cannot be won; he relies on trust and early consultation (CLOUDSECPOD-SENDBIRD-2025)
    - Gartner's regulatory advice is to build a baseline posture on shared principles instead of complying with each AI law one by one (TECHTARGET-GARTNERREG-2026)
    - The SANS/GIAC session recommends establishing an AI governance program within 3 months and baseline AI training for all employees within 6 months (RSAC-WORKFORCE-2026)
  human_checkpoints:
    - GRC team reviews vendor contracts and data-flow agreements (CLOUDSECPOD-SENDBIRD-2025)
    - Security is consulted before new models or features are enabled, by norm rather than by block (CLOUDSECPOD-SENDBIRD-2025)
  role_evolution: >
    In the SANS/GIAC survey, 30% of respondents report new AI governance analyst roles, 32% AI security engineer roles and 34%
    AI/ML specialist roles (selected all that apply; respondent count not stated) (RSAC-WORKFORCE-2026). Sendbird's CSO says an
    AppSec engineer is not automatically an AI security engineer (CLOUDSECPOD-SENDBIRD-2025).
  evidence_grade: B
  sources:
    - { ref: BSIDESLV-2026, title: "From the Wild West to Yes, If: Building an AI Security & Governance Program (Bo Barger, Alex Sayre, Cengage)", publisher: BSides Las Vegas, type: conference, url: "https://bsideslv.org/talks", date: 2026-08, access: full, locator: "Proving Ground talk abstract, Tuesday 11:30-12:00" }
    - { ref: CLOUDSECPOD-SENDBIRD-2025, title: "How to secure your AI Agents: A CISOs Journey", publisher: Cloud Security Podcast, type: podcast, url: "https://www.cloudsecuritypodcast.tv/videos/how-to-secure-your-ai-agents-a-cisos-journey", date: 2025-12-09, access: full, locator: "Transcript, roughly 00:19-00:36" }
    - { ref: RSAC-WORKFORCE-2026, title: "AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce (slides)", publisher: RSA Conference / SANS-GIAC, type: conference, url: "https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce", date: 2026-03-23, access: full, locator: "Slides 5-8, 21-22" }
    - { ref: TECHTARGET-GARTNERREG-2026, title: "How to prepare security controls for future AI regulations", publisher: TechTarget (Gartner analyst Bernard Woo), type: press, url: "https://www.techtarget.com/cybersecurity/opinion/How-to-prepare-security-controls-for-future-AI-regulations", date: 2026-06-02, access: full, locator: "'Ground AI strategy with risk-based principles'" }
  last_reviewed: 2026-10-17
  notes: >
    Grade B: two named organizations describe real programs, but neither publishes outcome measurements beyond an activity count in a talk abstract.
    The SANS/GIAC figures are slide text from a survey whose report landing page could not be retrieved. Practice-file use case 14 covers job-posting evidence for the same theme.

- id: security-governance-risk-06
  title: Agent-aware risk assessment: model agents as privileged insiders, read model system cards, review agent privileges
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Risk analysts must assess software agents that hold privileges, talk to customers and can bind the company, but the FAIR
    threat taxonomy defines AI agents only as malicious tools (FAIR-RISKREPORT-2026).
  solution: >
    The FAIR Institute's standards director proposes that analysts treat agents the company builds or buys as insiders; identify
    the model each agent runs on and read the vendor's system cards, treating published misbehavior rates as priors with the date
    and model version; scope scenarios from what the agent can actually do (tools, records, spend, commitments, data it can
    disclose); and assess its privileges as for a privileged user (own service identity, minimal tools, hard limits on transaction
    size and rate, human approval above a threshold) (FAIR-RISKREPORT-2026). A follow-up asks analysts to collect three numbers
    on agent activity (share reviewed, delay, how often review catches something), including tool calls (FAIR-ATTACKSURFACE-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "Guidance articles; no assessment results."
      provenance: independent
      source_ref: FAIR-RISKREPORT-2026
  prerequisites:
    - List of what each agent can do: tools it can call, systems and records reached, what it can spend or commit, data it can see (FAIR-RISKREPORT-2026)
    - System cards and vendor risk reports for the model version in use (FAIR-RISKREPORT-2026)
  risks_and_guardrails:
    - The author cautions that published rates come from the vendor's tests, not the enterprise's environment, and that models sometimes recognize when they are being evaluated (FAIR-RISKREPORT-2026)
    - A prompt-injected agent that sends refunds to an attacker's account puts the funds, not the agent, at the center of the loss scenario (FAIR-ATTACKSURFACE-2026)
  human_checkpoints:
    - Human approval for anything above a defined threshold (FAIR-RISKREPORT-2026)
  role_evolution: >
    Risk analysts add system-card reading and agent privilege review to scenario work; the author says analysts need the shape of the
    system, not engineers' vocabulary (FAIR-ATTACKSURFACE-2026).
  evidence_grade: C
  sources:
    - { ref: FAIR-RISKREPORT-2026, title: "Eight Takeaways from Anthropic's Risk Report for AI Risk Leaders", publisher: FAIR Institute (Todd Tucker, Standards Director), type: standard-setter, url: "https://www.fairinstitute.org/blog/eight-takeaways-from-anthropics-risk-report-for-ai-risk-leaders", date: 2026-09-25, access: full, locator: "Takeaways 1-4 (the post continues to eight; takeaways 5-8 not read)" }
    - { ref: FAIR-ATTACKSURFACE-2026, title: "An AI Attack Surface Primer for Risk Professionals", publisher: FAIR Institute (Todd Tucker), type: standard-setter, url: "https://www.fairinstitute.org/blog/an-ai-attack-surface-primer-for-risk-professionals", date: 2026-10-14, access: full, locator: "'Third, agent identity' and 'So what is the asset?'" }
  last_reviewed: 2026-10-17
  notes: >
    The FAIR page lists a different author label than the byline; the byline in the body (Todd Tucker) is used. Takeaways 5 to 8 of the first post were not read.

- id: security-governance-risk-07
  title: AI-assisted cyber risk quantification and scenario simulation
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [data-reporting, expert-judgment]
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: >
    Boards and executives ask for decision-ready, data-driven numbers; manual quantification is slow and inconsistent
    (FAIR-CRMSURVEY-2026).
  solution: >
    Survey respondents say they use or experiment with AI to quantify risk automatically, automate workflows, forecast and
    simulate scenarios, and read unstructured material such as vendor contracts and SOC 2 reports to populate risk models
    (FAIR-CRMSURVEY-2026).
  outcomes:
    - lever: quality
      description: Organizations using or experimenting with AI for cyber risk management
      figure: "80% (37% using, 43% experimenting)"
      measures: "Share of 400 qualified respondents (cyber risk leaders and practitioners at organizations with established cyber risk programs, 14 countries, fielded April 2026) answering 'Currently using AI' (37%) or 'Experimenting with AI' (43%); a further 20% plan to adopt."
      provenance: independent
      source_ref: FAIR-CRMSURVEY-2026
    - lever: quality
      description: Respondents describing their approach as proactive
      figure: "71% of AI-integrated organizations vs 52% of non-AI users"
      measures: "Share of respondents whose organization describes its cyber approach as proactive, split by AI use; a correlation in self-ratings, not a measured effect."
      provenance: independent
      source_ref: FAIR-CRMSURVEY-2026
    - lever: speed
      description: Where leaders see most value from AI
      figure: "42% automated risk quantification; 40% workflow automation; 40% forecasting and scenario simulation"
      measures: "Shares of respondents naming each opportunity area (response base not stated beyond the 400-respondent survey)."
      provenance: independent
      source_ref: FAIR-CRMSURVEY-2026
  prerequisites:
    - An established cyber risk management program; the sample was limited to such organizations (FAIR-CRMSURVEY-2026)
    - General-purpose GRC platforms: 63% of programs now anchor capabilities in core GRC platforms (FAIR-CRMSURVEY-2026)
  risks_and_guardrails:
    - Respondents cite regulatory uncertainty (37%), lack of mature AI-specific risk assessment models (32%) and insider misuse or misconfiguration (30%) as persistent concerns (FAIR-CRMSURVEY-2026)
    - A sample of 400 recruited by panel and sponsored by two vendors (GuidePoint Security and SAFE) leans toward mature, tool-using programs (FAIR-CRMSURVEY-2026)
  human_checkpoints:
    - Board-approved risk appetite: 97% of organizations have defined appetite levels and 89% say these are board-approved (FAIR-CRMSURVEY-2026)
  role_evolution: >
    The survey reports boardroom use of cyber risk data rose to 63% in 2026 as 90% of quantitative practitioners use financial framing
    (FAIR-CRMSURVEY-2026).
  evidence_grade: C
  sources:
    - { ref: FAIR-CRMSURVEY-2026, title: "2026 State of Cyber Risk Management Report", publisher: FAIR Institute (with Hanover Research; sponsored by GuidePoint Security and SAFE), type: survey, url: "https://www.fairinstitute.org/hubfs/State%20of%20Cyber%20Risk%20Management%20Report%202026.pdf", date: 2026, access: full, locator: "Executive Summary; 'AI Is Not Limited to Experimental Use' (pp. 27-28); Methodology (p. 5)" }
  last_reviewed: 2026-10-17
  notes: >
    Publication month not found; fieldwork was April 2026. Graded C because the evidence is a vendor-sponsored survey of self-reported use, not a deployment with results.
    Search-only: vendor SAFE markets 'autonomous CRQ' at RSAC 2026 (SAFE-RSAC-2026, seen in search results only). Practice-file use case 10 covers the quantified-analysis deployments.

- id: security-governance-risk-08
  title: Reassess code-resident control effectiveness when the organization adopts coding agents
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Every loss-event frequency estimate assumes software-based controls (authentication, authorization, input validation, rate
    limiting, logging) work about as well as when last assessed. Coding agents raise change volume and may change control
    strength, which a new scenario list would not reveal (FAIR-AGENTICCODING-2026).
  solution: >
    The FAIR Institute's standards director proposes eight questions for assessing 'variance management controls' in agentic-coding
    pipelines: merge volume against a year ago; share of merged changes that are agent-generated; which checks are required and
    what share passed each; whether tests cover the specific controls the risk analyses depend on; how long a flagged defect waits;
    what happened to last quarter's findings; who designs the tests and can change pipeline configuration; and when each
    code-resident control was last validated by a test (FAIR-AGENTICCODING-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "Guidance post; it reports third-party studies of AI-written code, summarized in notes, but no results from using the questions."
      provenance: independent
      source_ref: FAIR-AGENTICCODING-2026
  prerequisites:
    - Help from the CTO or equivalent to understand how the organization builds, tests and releases software (FAIR-AGENTICCODING-2026)
    - Pipeline gates that block changes on failed tests, not advisory scans (FAIR-AGENTICCODING-2026)
  risks_and_guardrails:
    - The author says the studies he cites are vendor studies with small agent-specific samples and that none establish anything about the reader's codebase (FAIR-AGENTICCODING-2026)
    - If the same agent writes the feature and its tests, the check and the thing checked share an author; independent testing is advised (FAIR-AGENTICCODING-2026)
  human_checkpoints:
    - Manual testing for business logic, authentication, session management and access control at higher assurance levels (FAIR-AGENTICCODING-2026)
  role_evolution: >
    The author says few risk professionals have software development backgrounds and recommends talking to the CTO; risk analysts therefore need engineering
    literacy to assess pipelines (FAIR-AGENTICCODING-2026).
  evidence_grade: D
  sources:
    - { ref: FAIR-AGENTICCODING-2026, title: "What Risk Leaders Should Be Asking When AI Is Building Software", publisher: FAIR Institute (Todd Tucker), type: standard-setter, url: "https://www.fairinstitute.org/blog/what-risk-leaders-should-be-asking-when-ai-is-building-software", date: 2026-10-02, access: full, locator: "'Questions to assess variance management'" }
  last_reviewed: 2026-10-17
  notes: >
    Idea: proposed by a practitioner body, no deployment found. Figures quoted in the post, all attributed by the author to third parties and not verified here: JetBrains 2026 survey
    (15,000+ developers fielded May-July 2026) with 90% using AI coding agents weekly and 68% daily; DryRun Security found vulnerabilities in 26 of 30 pull requests built with three agents
    from specifications that had no security requirements; Veracode reported roughly 45% of generated samples introduced a top-ten web vulnerability class; a Stanford/CMU study of one enterprise
    (802 developers, 196,212 pull requests) saw pull-request volume grow 3.1 times while reviewers grew 1.5 times; Cortex's 2026 benchmark saw change failure rate up roughly 30% and found fewer
    than half of surveyed organizations had a formal AI-use policy. Routed to application-security for the underlying code-quality evidence.

- id: security-governance-risk-09
  title: Deliberate apprenticeship for junior risk, assurance and security staff when AI absorbs entry-level work
  archetype: security
  module: governance-risk
  function: people-hr
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    Juniors used to learn what 'normal' looks like by doing routine work that AI now automates. Venables argues that unless
    organizations act, the pipeline fractures in a few years, and he says the organizational shape shifts from a pyramid to a
    diamond (VENABLES-WORKFORCE-2026).
  solution: >
    Venables proposes replacing each lost on-ramp with a deliberate one: for risk and assurance, put juniors on 'control-failure
    post-mortems' (why a control documented as effective was not effective when needed) instead of evidence gathering; for security
    operations, ownership of a narrow detection surface with their own precision and recall tracked over ninety days; for exploitability
    work, sampled adjudication of automated prioritization with the false-positive rate published each quarter; a structured incident
    ladder; AI as a coach; and pod-based or master-and-apprentice structures (VENABLES-WORKFORCE-2026). He also proposes hiring
    rubrics that test candidates on spotting errors in AI output (VENABLES-WORKFORCE-2026).
  outcomes:
    - lever: capacity
      description: none published
      figure: "none published"
      measures: "Essay; of two professional-services firms he observed, one is described as already introducing new forms of apprenticeship; neither is named and no results are given."
      provenance: self-reported
      source_ref: VENABLES-WORKFORCE-2026
  prerequisites:
    - Ranges, simulations or training environments, including ones where automation is deliberately compromised (VENABLES-WORKFORCE-2026)
    - Mid-level staff given time to coach, since the middle layer expands and carries more cognitive load (VENABLES-WORKFORCE-2026)
  risks_and_guardrails:
    - Venables warns that organizations treating AI only as a way to cut entry-level cost risk a judgment crisis as the pipeline dries up (VENABLES-WORKFORCE-2026)
    - He notes the approach cannot rely on every organization poaching others' mid-level staff (VENABLES-WORKFORCE-2026)
  human_checkpoints:
    - Juniors review machine-generated work against a standard, which he describes as the mid-level job they are heading into (VENABLES-WORKFORCE-2026)
  role_evolution: >
    New entry-level work is reviewing machine output and adjudicating automated decisions; the new entry point is, in many cases, the old mid-layer (VENABLES-WORKFORCE-2026).
    SANS/GIAC slides report SOC and security analysts (32%), threat intelligence analysts (26%) and incident responders (22%) as most-cited entry-level roles affected; 39% report no role
    reductions yet; only 24% of organizations provide well-defined career progression (RSAC-WORKFORCE-2026). A BSides talk abstract says many organizations hire L1 analysts with no written career ladder (BSIDESLV-2026).
  evidence_grade: D
  sources:
    - { ref: VENABLES-WORKFORCE-2026, title: "AI and Challenges in Workforce Development", publisher: Phil Venables (personal blog), type: community, url: "https://www.philvenables.com/post/ai-and-challenges-in-workforce-development", date: 2026-10-03, access: full, locator: "Consequences 1-2; Actions 1-7" }
    - { ref: RSAC-WORKFORCE-2026, title: "AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce (slides)", publisher: RSA Conference / SANS-GIAC, type: conference, url: "https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce", date: 2026-03-23, access: full, locator: "Slides 7, 15" }
    - { ref: BSIDESLV-2026, title: "Nobody Told Me I Could Grow: Building a SOC Career You Actually Want", publisher: BSides Las Vegas, type: conference, url: "https://bsideslv.org/talks", date: 2026-08, access: full, locator: "Talk abstract" }
  last_reviewed: 2026-10-17
  notes: >
    Idea: discussed by a practitioner with direct leadership experience; no named organization has published a result. Slides state 'AI is impacting entry-level jobs' with SOC and security analysts leading at 32% (selected all that apply); respondent count is not stated.

- id: security-governance-risk-10
  title: GRC engineering operating model: GRC staff build scripts and agents against live systems
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [software-systems, review-assurance]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    GRC teams run on spreadsheets and manual evidence work. An independent practitioner survey found spreadsheets are the most-cited
    primary GRC tool and that skills are uneven (GRCENGINEER-STATEOFGRC-2026).
  solution: >
    GRC staff learn to read system configurations (such as branch-protection settings and infrastructure-as-code plans), collect evidence
    through APIs, and build small automations, including with coding agents (for example a script mapping posture findings to risk-register entries) (GRCENGINEER-086-2026).
    The newsletter author runs a weekly series on 'AI scaffolding' for GRC professionals (GRCENGINEER-AIUSAGE-2026). The CSA Mythos-ready paper says all roles will likely become 'AI builders' (CSA-MYTHOSREADY-2026).
  outcomes:
    - lever: capacity
      description: Primary GRC tool among survey respondents
      figure: "spreadsheets 93 respondents; ServiceNow 86"
      measures: "Count of respondents (of 795 GRC and security professionals) naming each as primary tool, as stated in the post; spreadsheets were the most-cited single tool."
      provenance: independent
      source_ref: GRCENGINEER-STATEOFGRC-2026
    - lever: capacity
      description: Technical skill and tooling among respondents
      figure: "5.4 out of 10 average skill; 73.6% of CISOs use no commercial tool"
      measures: "Average self-rated technical skill across respondents (scale of 10); share of CISO respondents using no commercial GRC tool, both as stated in the post. The 36-page report was not opened."
      provenance: independent
      source_ref: GRCENGINEER-STATEOFGRC-2026
  prerequisites:
    - API access to production systems, which the author says often means negotiating with an infrastructure team and accepting a no (GRCENGINEER-086-2026)
    - Skill in reading configurations rather than writing software: five of six sample tasks involved writing no software (GRCENGINEER-086-2026)
  risks_and_guardrails:
    - The author says a script that collects evidence is still a script, but that belittling the work below 'engineering' was wrong (GRCENGINEER-086-2026)
    - The survey author states its design could be tighter and the sample is self-selected from his readership (GRCENGINEER-STATEOFGRC-2026)
  human_checkpoints:
    - The GRC practitioner decides whether a configuration is, in fact, their control (GRCENGINEER-086-2026)
  role_evolution: >
    From program manager and spreadsheet owner toward a technical reader and builder of controls; the CSA paper says getting started is easier than learning Excel (CSA-MYTHOSREADY-2026).
    A BSides talk organizes careers into four role families (Builders, Breakers, Defenders, Governors) (BSIDESLV-2026).
  evidence_grade: C
  sources:
    - { ref: GRCENGINEER-STATEOFGRC-2026, title: "State of GRC 2026 Report: Spreadsheets are still #1", publisher: GRC Engineer newsletter (Ayoub Fandi), type: survey, url: "https://www.grcengineer.com/p/state-of-grc-2026-report-spreadsheets-are-still-1", date: 2026-03-16, access: full, locator: "'5 Key Takeaways from the Report'" }
    - { ref: GRCENGINEER-086-2026, title: "Most GRC Engineering Is Sysadmin Work. That's the Good News.", publisher: GRC Engineer newsletter, type: community, url: "https://www.grcengineer.com/p/most-grc-engineering-is-sysadmin-work-that-s-the-good-news", date: 2026-10-15, access: full, locator: "Task table; 'Reading is most of it'" }
    - { ref: GRCENGINEER-AIUSAGE-2026, title: "3 Basic Things Killing Your AI Usage for GRC", publisher: GRC Engineer newsletter, type: community, url: "https://www.grcengineer.com/p/3-basic-things-killing-your-ai-usage-for-grc", date: 2026-01-08, access: full, locator: "'The Year-Long Mission'" }
    - { ref: CSA-MYTHOSREADY-2026, title: "The 'AI Vulnerability Storm': Building a 'Mythos-ready' Security Program", publisher: Cloud Security Alliance with SANS, [un]prompted and OWASP GenAI Security Project, type: standard-setter, url: "https://labs.cloudsecurityalliance.org/mythos-ciso/", date: 2026-04-12, access: full, locator: "PDF v1.0 p. 14" }
    - { ref: BSIDESLV-2026, title: "Hiring-manager talk on Builders, Breakers, Defenders, Governors", publisher: BSides Las Vegas, type: conference, url: "https://bsideslv.org/talks", date: 2026-08, access: full, locator: "Talk abstract (hiring-manager session)" }
  last_reviewed: 2026-10-17
  notes: >
    Companion to practice-file use case 13 (job-posting evidence). The survey's sponsor-free claim is the author's own statement.

- id: security-governance-risk-11
  title: Baseline control posture for competing AI regulations, built on shared principles rather than law-by-law mapping
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [research-synthesis, expert-judgment]
  pattern: research-brief
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    A Gartner analyst writes that the global AI regulatory landscape is fragmented and volatile, with the EU AI Act, China's laws and a patchwork of
    US state requirements, so security leaders face competing mandates while AI adoption stretches their resources (TECHTARGET-GARTNERREG-2026).
  solution: >
    Gartner advises engaging assurance, governance and legal groups to judge which mandates apply, grouping risks into 'harm to people' (safety, bias, privacy) and
    'harm to property' (data integrity, intellectual property theft, availability), building a baseline on shared principles (safety, transparency, accountability,
    privacy, security), and funding AI runtime defenses and tabletop exercises as evidence of resilience (TECHTARGET-GARTNERREG-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "Opinion article by a Gartner vice president analyst; no results."
      provenance: vendor-published
      source_ref: TECHTARGET-GARTNERREG-2026
  prerequisites:
    - Working relationships with assurance, governance and legal (TECHTARGET-GARTNERREG-2026)
    - Extension of identity and access controls from the human workforce to machine identities (TECHTARGET-GARTNERREG-2026)
  risks_and_guardrails:
    - Trying to comply with every emerging regulation individually is, in the author's words, a resource-intensive trap (TECHTARGET-GARTNERREG-2026)
    - The CSA briefing warns the EU AI Act (August 2026) brings automated audit, incident reporting and cybersecurity requirements around AI while existing regulations use a reasonableness test (CSA-MYTHOSREADY-2026)
  human_checkpoints:
    - Cross-functional review of which mandates apply (TECHTARGET-GARTNERREG-2026)
  role_evolution: >
    The CISO's remit extends to controls the regulations aim at harms to people, which Gartner says falls within CISO purview (TECHTARGET-GARTNERREG-2026).
  evidence_grade: C
  sources:
    - { ref: TECHTARGET-GARTNERREG-2026, title: "How to prepare security controls for future AI regulations", publisher: TechTarget (Gartner analyst Bernard Woo), type: press, url: "https://www.techtarget.com/cybersecurity/opinion/How-to-prepare-security-controls-for-future-AI-regulations", date: 2026-06-02, access: full, locator: "Whole article" }
    - { ref: CSA-MYTHOSREADY-2026, title: "The 'AI Vulnerability Storm': Building a 'Mythos-ready' Security Program", publisher: Cloud Security Alliance, type: standard-setter, url: "https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/mythosreadyv1.0.pdf", date: 2026-04-12, access: full, locator: "Risk register item 12, p. 18" }
  last_reviewed: 2026-10-17
  notes: >
    Little AI is used in the work itself; the use case records how analysts say regulatory mapping should be approached. Practice-file use case 12 covers tool-assisted mapping.

- id: security-governance-risk-12
  title: Board and executive risk reporting re-based for AI-accelerated exploitation
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [document-production, data-reporting]
  pattern: draft-review-loop
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    Gartner analysts say many board reports are structured around cybersecurity, not around the business, and a CISO may get five to ten minutes with the board
    (TECHTARGET-GARTNERBOARD-2026). The CSA briefing says pre-AI assumptions about patch windows, exploit scarcity and incident frequency may no longer hold,
    which could underfund controls and make business reporting inaccurate (CSA-MYTHOSREADY-2026).
  solution: >
    Gartner suggests structuring board reports like financial statements: a balance-sheet view of program state, an income-statement view of expected losses, a cash-flow view of resources,
    and a narrative with requests (TECHTARGET-GARTNERBOARD-2026). The CSA briefing adds an action to update risk models and reporting this week or within 45 days, a draft risk register, and a
    board section with talking points; it also says metrics should focus on speed to recover (CSA-MYTHOSREADY-2026).
  outcomes:
    - lever: experience
      description: Boards using cyber risk data
      figure: "63% in 2026"
      measures: "Share of respondents (400 cyber risk leaders and practitioners, April 2026) reporting boardroom use of cyber risk data; the 2025 report found use at fewer than half of participating organizations."
      provenance: independent
      source_ref: FAIR-CRMSURVEY-2026
    - lever: experience
      description: Gartner board-attitude statistics quoted at its summit
      figure: "93% / 98% / 71%"
      measures: "As reported by TechTarget from Gartner sessions: 93% of board members agree cyber-risk threatens shareholder value; 98% believe threats will grow in two years; 71% of board members are willing to accept greater cyber-risk to achieve business goals. Survey populations and sizes are not given in the articles."
      provenance: vendor-published
      source_ref: TECHTARGET-GARTNERBOARD-2026
  prerequisites:
    - A stable minimum set of indicators per report section that stays consistent over time (TECHTARGET-GARTNERBOARD-2026)
    - Circulating the framework among leadership stakeholders before use (TECHTARGET-GARTNERBOARD-2026)
  risks_and_guardrails:
    - The CSA briefing says boards will face questions on whether available AI tools were used for defensive scanning and whether not doing so is negligence (CSA-MYTHOSREADY-2026)
    - Gartner's Candrick says tighter controls bring business friction that can stall AI integration, and that cyber-risk appetite at board level is shifting (TECHTARGET-GARTNERCISO-2026)
  human_checkpoints:
    - CISO review of the narrative and requests before the board sees them (TECHTARGET-GARTNERBOARD-2026)
  role_evolution: >
    Gartner says business acumen will, by 2028, be the main differentiator of high-performing CISOs in the C-suite (TECHTARGET-GARTNERCISO-2026) and that the new mandate is to minimize harm to
    the business before, during and after an attack rather than maximize prevention (TECHTARGET-GARTNERCISO-2026).
  evidence_grade: C
  sources:
    - { ref: TECHTARGET-GARTNERBOARD-2026, title: "Lost in translation: Cybersecurity board reporting for CISOs", publisher: TechTarget (Richard Livingston), type: press, url: "https://www.techtarget.com/cybersecurity/news/366643884/Lost-in-translation-Cybersecurity-board-reporting-for-CISOs", date: 2026-06-03, access: full, locator: "Whole article" }
    - { ref: TECHTARGET-GARTNERCISO-2026, title: "CISO role changes as cyber-risk appetites in the C-suite grow", publisher: TechTarget (Richard Livingston), type: press, url: "https://www.techtarget.com/cybersecurity/news/366644003/CISO-role-changes-as-cyber-risk-appetites-in-the-C-suite-grow", date: 2026-06-08, access: full, locator: "'The security drag'; 'A new mandate for CISOs'" }
    - { ref: CSA-MYTHOSREADY-2026, title: "The 'AI Vulnerability Storm': Building a 'Mythos-ready' Security Program", publisher: Cloud Security Alliance, type: standard-setter, url: "https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/mythosreadyv1.0.pdf", date: 2026-04-12, access: full, locator: "Action 6 'Update Risk Models and Reporting' p. 20; Section V 'Executive and Board Briefing' p. 22; risk register items 11-12 pp. 17-18" }
    - { ref: FAIR-CRMSURVEY-2026, title: "2026 State of Cyber Risk Management Report", publisher: FAIR Institute, type: survey, url: "https://www.fairinstitute.org/hubfs/State%20of%20Cyber%20Risk%20Management%20Report%202026.pdf", date: 2026, access: full, locator: "Executive Summary item 4" }
  last_reviewed: 2026-10-17
  notes: >
    The Gartner board-reporting format is not itself AI-based; the AI-specific content comes from the CSA briefing, whose authors are CISO-community members and who
    thank 250 CISOs for live edits. The CSA text is guidance, not an observation of results. Practice-file use case 11 covers tool-generated board packs.

- id: security-governance-risk-13
  title: Frequent AI-assisted micro tabletops with notification-clock rehearsal and a defensible record
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [coordination-scheduling, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    Annual tabletops built around a slide deck rarely resemble real response, and teams face notification laws in over 200 jurisdictions according to a podcast guest, with clocks such as DORA's four hours
    (RESILIENTCYBER-TABLETOP-2026).
  solution: >
    The co-founder of BreachRx argues for smaller, more frequent exercises, some running in the background over a week with a thirty-minute hot wash, run in the tooling used during real incidents, with AI
    agents helping with scenario generation, procedure building and incident reporting, and a defensible record that exercises happened (RESILIENTCYBER-TABLETOP-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "Podcast description by a vendor co-founder; no results."
      provenance: vendor-published
      source_ref: RESILIENTCYBER-TABLETOP-2026
  prerequisites:
    - Separation of the factual record from privileged conversations (RESILIENTCYBER-TABLETOP-2026)
  risks_and_guardrails:
    - The guest warns that privileging everything leaves nothing privileged, and that frequent exercises can become checkbox compliance unless threats are rotated from the news (RESILIENTCYBER-TABLETOP-2026)
  human_checkpoints:
    - Lessons learned feed back into procedures through a human hot wash (RESILIENTCYBER-TABLETOP-2026)
  role_evolution: >
    The guest expects concurrent incidents to become the new floor as AI raises attacker capability, and says regulators and plaintiffs will ask for proof of continuous readiness (RESILIENTCYBER-TABLETOP-2026).
  evidence_grade: C
  sources:
    - { ref: RESILIENTCYBER-TABLETOP-2026, title: "AI-Accelerated Micro Tabletops and Incident Readiness", publisher: Resilient Cyber (Chris Hughes; guest Matt Hartley, BreachRx), type: podcast, url: "https://www.resilientcyber.io/p/ai-accelerated-micro-tabletops-and", date: 2026-10-12, access: full, locator: "Episode description and 'We discuss' list (video not watched)" }
  last_reviewed: 2026-10-17
  notes: >
    Primarily an incident-response topic; kept here for the regulator-reporting and evidence-of-readiness angle. Description only, vendor guest.

- id: security-governance-risk-14
  title: Deterministic action gates, kill switches and out-of-band action logs for the team's own agents
  archetype: security
  module: governance-risk
  function: technology-it
  work_types: [software-systems, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: >
    Agents act, not only talk. Venables argues that a solely non-deterministic system, such as an LLM acting as judge, cannot reliably monitor another non-deterministic system for critical actions
    (VENABLES-HFT-2026). Dark Reading quotes experts that the model's intentions should be irrelevant to security architecture (DARKREADING-ROGUE-2026).
  solution: >
    Venables maps high-frequency-trading controls to agents: pre-execution action gates against a safety envelope, hardcoded limits on external actions that bypass the model's reasoning, kill switches
    based on process and network-layer isolation (revoking credentials alone may not stop spawned sub-processes), rate and scope limiters, and a real-time out-of-band copy of every action to write-once storage
    (VENABLES-HFT-2026). Dark Reading sources add deny-by-default network access, narrowly scoped credentials, independent checks at every tool call and an independent kill switch (DARKREADING-ROGUE-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "Opinion and expert commentary; no measurements."
      provenance: self-reported
      source_ref: VENABLES-HFT-2026
  prerequisites:
    - A defined safety envelope for each agent action type (VENABLES-HFT-2026)
    - Isolation that can terminate the hosting container and sever outbound network access (VENABLES-HFT-2026)
  risks_and_guardrails:
    - When a guardrail trips and asks a human to approve, Venables says the human needs a context bundle explaining why, since blind approval is the modern equivalent of lifting a tripped circuit breaker (VENABLES-HFT-2026)
    - A CSA analyst quoted by Dark Reading says unexpected model behavior is always a failure of the security controls (DARKREADING-ROGUE-2026)
    - Resilient Cyber's guest, a startup CEO, says the disclosed OpenAI controls failures (single package proxy as isolation, no chain-of-thought monitoring running, no automated shutdown) included several any one of which would have stopped the incident (RESILIENTCYBER-KORMAN-2026)
  human_checkpoints:
    - Human approval for high-risk decisions, with kill switches that sit outside the agent's control (DARKREADING-ROGUE-2026)
  role_evolution: >
    Security architecture becomes a governance lens: GRC and risk staff are asked to specify and test limits that sit outside the model (VENABLES-HFT-2026, DARKREADING-ROGUE-2026).
  evidence_grade: D
  sources:
    - { ref: VENABLES-HFT-2026, title: "High Frequency Trading and Lessons for Agentic AI", publisher: Phil Venables (personal blog), type: community, url: "https://www.philvenables.com/post/high-frequency-trading-and-lessons-for-agentic-ai", date: 2026-05-02, access: full, locator: "'HFT Controls: A Template for Agentic Safety'; 'Goldman Sachs Options Error (2013)'" }
    - { ref: DARKREADING-ROGUE-2026, title: "Is It Fair to Blame 'Rogue' AI for Security Failures?", publisher: Dark Reading, type: press, url: "https://www.darkreading.com/insider-threats/blame-rogue-ai-security-failures", date: 2026-10-02, access: full, locator: "Sections 'Changing the Lexicon' and 'For Defenders, AI Agent Intention Should Not Matter'" }
    - { ref: RESILIENTCYBER-KORMAN-2026, title: "Cybersecurity is Ceding AI Safety, But Should We?", publisher: Resilient Cyber (Chris Hughes; guest Zack Korman, Embroidery), type: podcast, url: "https://www.resilientcyber.io/p/cybersecurity-is-ceding-ai-safety", date: 2026-09-28, access: full, locator: "Episode description and timestamps (21:24 eight layers of failure)" }
  last_reviewed: 2026-10-17
  notes: >
    Idea: discussed widely, no GRC deployment with results found. The OpenAI-Hugging Face incident described by guests is routed to ai-security and incident-response; only the control-design points are used here.

- id: security-governance-risk-15
  title: Audit-defensible records for AI-assisted security decisions (versioning, hashing, prompt traceability, interpretability)
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    Security leaders deploy AI that triages alerts, blocks policy violations and evaluates access requests, yet cannot explain how those decisions are made; the speaker calls these 'unauditable security controls' (FIRST-CON-2026).
    Another session asks whether AI outputs will hold up under audit, regulation or legal scrutiny (FIRST-CON-2026).
  solution: >
    A Centene session at the FIRST conference describes a schema-driven pipeline (ingest, normalize, AI assist, validate, timeline, export) in which every transformation is versioned, explainable and hash verified, with
    confidence scoring, prompt traceability and workflow logging, and an AI transparency maturity model; the abstract says the framework treats AI as an accelerator and keeps decision authority with the analyst (FIRST-CON-2026).
    A Jumpmind CISO session proposes treating interpretability as a security control, with AI security KPIs and a higher bar for vendor transparency (FIRST-CON-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "Conference abstracts only; the sessions were not seen."
      provenance: self-reported
      source_ref: FIRST-CON-2026
  prerequisites:
    - A common schema (the Centene abstract uses the Open Cybersecurity Schema Framework) (FIRST-CON-2026)
  risks_and_guardrails:
    - The Jumpmind abstract says the aim is to move from 'trust the accuracy metrics' to showing the control logic and proving it is defensible (FIRST-CON-2026)
    - Venables proposes real-time out-of-band copies of agent actions in write-once storage (VENABLES-HFT-2026)
  human_checkpoints:
    - Decision authority stays with the analyst in the Centene design (FIRST-CON-2026)
  role_evolution: >
    The Centene speaker describes the analyst role moving from reactive responder to supervisory decision-maker (FIRST-CON-2026).
  evidence_grade: C
  sources:
    - { ref: FIRST-CON-2026, title: "From Logs to Living Timelines: AI-Assisted Incident Response in Hybrid Cloud Using OCSF (Centene); AI Interpretability as a Security Control: Introducing the CIRCUIT Framework (Jumpmind)", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06-16, access: full, locator: "Centene session 16 Jun 2026 11:45-12:20; Jumpmind session 17 Jun 2026 13:30-14:15" }
    - { ref: VENABLES-HFT-2026, title: "High Frequency Trading and Lessons for Agentic AI", publisher: Phil Venables (personal blog), type: community, url: "https://www.philvenables.com/post/high-frequency-trading-and-lessons-for-agentic-ai", date: 2026-05-02, access: full, locator: "'Post-Trade Analysis (Drop-Copy Auditing)'" }
  last_reviewed: 2026-10-17
  notes: >
    Graded C: named organization and a framework description, but the abstract does not state that the framework is in production, and there are no measurements. Routed to incident-response for the investigation workflow.

- id: security-governance-risk-16
  title: CISO function takes on digital and AI risk beyond security
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    AI deployed across operations raises risks (safety, model validation, compliance, privacy, reliability, accuracy) that do not fall naturally into existing organizations, outside industries such as finance with developed risk teams
    (VENABLES-CISO2-2026).
  solution: >
    Venables says the C-suite and board are turning to the CISO to manage these risks, and describes the emergence of a 'Chief Digital Risk Officer' form of the role, alongside a 'Chief Technology and Security Officer' form
    (VENABLES-CISO2-2026). Gartner's Candrick separately argues CISOs need business acumen over technical expertise and a mandate to minimize harm (TECHTARGET-GARTNERCISO-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "Opinion post; no named organization or figure."
      provenance: self-reported
      source_ref: VENABLES-CISO2-2026
  prerequisites:
    - A CISO who acts as a business executive, with technical empathy and long-term support from peers and the board (VENABLES-CISO2-2026)
  risks_and_guardrails:
    - Candrick warns that more security does not mean better business outcomes and can mean slower speed to market and stalled AI adoption (TECHTARGET-GARTNERCISO-2026)
  human_checkpoints:
    - Not described
  role_evolution: >
    Venables describes CISO 2.0 as shaping the environment rather than bolting security on, and as 'CEO' of the security program (VENABLES-CISO2-2026). A WEF-type CEO-versus-CISO divergence was seen in search only and is not used.
  evidence_grade: D
  sources:
    - { ref: VENABLES-CISO2-2026, title: "CISO Version 2.0", publisher: Phil Venables (personal blog), type: community, url: "https://www.philvenables.com/post/ciso-version-2-0", date: 2026-06-12, access: full, locator: "'What Next - Two Divergent Paths?'" }
    - { ref: TECHTARGET-GARTNERCISO-2026, title: "CISO role changes as cyber-risk appetites in the C-suite grow", publisher: TechTarget, type: press, url: "https://www.techtarget.com/cybersecurity/news/366644003/CISO-role-changes-as-cyber-risk-appetites-in-the-C-suite-grow", date: 2026-06-08, access: full, locator: "'A new mandate for CISOs'" }
  last_reviewed: 2026-10-17
  notes: >
    Idea: the author reports observing the pattern but names no organization.

- id: security-governance-risk-17
  title: GRC practitioners drafting policy and standards with general-purpose chat assistants using structured prompts
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    GRC practitioners ask a chatbot something like 'help me write a security policy' and get generic output; a GRC-engineering newsletter says three basic mistakes kill most of the value (GRCENGINEER-AIUSAGE-2026).
  solution: >
    The newsletter gives copy-paste templates that supply context (the audience, tech stack, certifications held, the current state) and ask for specific sections, as in a worked example of an access control
    policy for a 200-person fintech with MFA but no formal policy (GRCENGINEER-AIUSAGE-2026).
  outcomes:
    - lever: speed
      description: none published
      figure: "none published"
      measures: "How-to newsletter; no results reported."
      provenance: self-reported
      source_ref: GRCENGINEER-AIUSAGE-2026
  prerequisites:
    - Context about the organization supplied in the prompt (GRCENGINEER-AIUSAGE-2026)
  risks_and_guardrails:
    - Hallucination and policy drift are not discussed in the issue read; no quality data found
  human_checkpoints:
    - The practitioner reviews the draft (implied; not stated in the issue)
  role_evolution: >
    The author says GRC professionals who master AI scaffolding will define the next decade (GRCENGINEER-AIUSAGE-2026).
  evidence_grade: D
  sources:
    - { ref: GRCENGINEER-AIUSAGE-2026, title: "3 Basic Things Killing Your AI Usage for GRC", publisher: GRC Engineer newsletter, type: community, url: "https://www.grcengineer.com/p/3-basic-things-killing-your-ai-usage-for-grc", date: 2026-01-08, access: full, locator: "'The 3 Mistakes' and templates" }
  last_reviewed: 2026-10-17
  notes: >
    Idea. Practice-file use case 08 covers policy drafting with tooling.

- id: security-governance-risk-18
  title: Using model system cards and risk reports as inputs to due diligence on AI model providers
  archetype: security
  module: governance-risk
  function: procurement-supply-chain
  work_types: [research-synthesis, review-assurance]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Buying a model means buying its training data, weights and serving code; a poisoned base model or backdoor would be nearly impossible for the buyer to find, so the risk must be handled as a third-party risk
    (FAIR-ATTACKSURFACE-2026).
  solution: >
    The FAIR Institute's standards director says to document and assess the controls the provider has against poisoning and backdoors, ask what assurance it gives over model artifacts and its training pipeline,
    and read the system card for the exact release in use and again after each update, noting named failure modes and the change from the previous version (FAIR-ATTACKSURFACE-2026, FAIR-RISKREPORT-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "Guidance posts; no results."
      provenance: independent
      source_ref: FAIR-ATTACKSURFACE-2026
  prerequisites:
    - Knowing which model and version each in-scope agent runs on (FAIR-RISKREPORT-2026)
  risks_and_guardrails:
    - Vendor-reported rates come from vendor tests and may not match the buyer's environment (FAIR-RISKREPORT-2026)
  human_checkpoints:
    - Analyst reads the card and records the rate, model version and date in the analysis (FAIR-RISKREPORT-2026)
  role_evolution: >
    Third-party risk analysts add model-provider documents to their reading list (FAIR-RISKREPORT-2026).
  evidence_grade: D
  sources:
    - { ref: FAIR-ATTACKSURFACE-2026, title: "An AI Attack Surface Primer for Risk Professionals", publisher: FAIR Institute (Todd Tucker), type: standard-setter, url: "https://www.fairinstitute.org/blog/an-ai-attack-surface-primer-for-risk-professionals", date: 2026-10-14, access: full, locator: "'Back to the big picture'" }
    - { ref: FAIR-RISKREPORT-2026, title: "Eight Takeaways from Anthropic's Risk Report for AI Risk Leaders", publisher: FAIR Institute (Todd Tucker), type: standard-setter, url: "https://www.fairinstitute.org/blog/eight-takeaways-from-anthropics-risk-report-for-ai-risk-leaders", date: 2026-09-25, access: full, locator: "Takeaway 2" }
  last_reviewed: 2026-10-17
  notes: >
    Idea: described as practice advice, no deployment found.
```

## 3. Module notes

### Processes and key steps (with work types)

- Customer assurance and trust: questionnaires, trust pages, attestations (`client-interaction`, `document-production`). Discourse centre: verification of automated attestations (IANS-DELVE-2026).
- Third-party and supplier risk: intake, assessment, continuous monitoring, shadow AI and internal builders as "second party" risk (`review-assurance`, `coordination-scheduling`) (CLOUDSECPOD-LOVABLE-2026).
- Compliance and control assurance: baseline, evidence, continuous monitoring, control failure handling (`review-assurance`, `data-reporting`) (BLEEPING-ANECDOTES-2026, VENABLES-CRE-2026).
- Risk management and quantification: scenarios, appetite, board reporting (`expert-judgment`, `data-reporting`) (FAIR-CRMSURVEY-2026, TECHTARGET-GARTNERBOARD-2026).
- Policy and AI governance: acceptable use, approvals, vendor assessment (`expert-judgment`) (CLOUDSECPOD-SENDBIRD-2025, BSIDESLV-2026).
- Security workforce and operating model: skills, career ladders, role families (`people-hr`) (RSAC-WORKFORCE-2026, VENABLES-WORKFORCE-2026).
- Security architecture lens: deterministic gates, isolation, kill switches, tamper-resistant logs for agents (VENABLES-HFT-2026, DARKREADING-ROGUE-2026).

### Common pain points

- Reports "structured around cybersecurity, not around the business"; five to ten minutes with the board (TECHTARGET-GARTNERBOARD-2026).
- Third-party programs become "a paper exercise" in large companies (CLOUDSECPOD-LOVABLE-2026).
- Embedded vendor AI is hard to see (TECHTARGET-GARTNERREG-2026).
- Competing AI regulations, unfunded (TECHTARGET-GARTNERREG-2026); SANS/GIAC slides say regulatory impact on hiring went from 40% to 95% in a year, with 68% reporting a moderate to extreme hiring impact (respondent count not stated) (RSAC-WORKFORCE-2026).
- Skills before headcount: SANS/GIAC slides report 60% skills versus 40% headcount, up from 52% skills a year earlier; 48% report moderate to extreme skills gap (RSAC-WORKFORCE-2026). ISC2 reports 59% citing critical or significant skills needs, up from 44% (ISC2-WORKFORCE-2025).
- Security staff "caught in a vice" of more reports, more code shipped and a larger attack surface, often without reprioritization or automation investment (CSA-MYTHOSREADY-2026).

### Metrics and benchmarks (with sources)

- FAIR Institute, 400 respondents (April 2026): 80% use or experiment with AI in cyber risk management (37% using, 43% experimenting); 63% of programs anchor in core GRC platforms; boardroom use of cyber risk data 63%; 97% have defined risk appetite, 89% board-approved (FAIR-CRMSURVEY-2026). Vendor-sponsored, self-reports.
- SANS/GIAC slides at RSAC 2026: 93% building AI policy, 72% still developing; 21% comprehensive workforce framework; 20% comprehensive AI training for all staff; 56% of organizations use workforce frameworks to define job requisitions (up from 46%); 31% name career progression as a hiring obstacle (9% a year earlier); only 24% provide well-defined progression (respondent count and sampling not stated) (RSAC-WORKFORCE-2026).
- GRC Engineer independent survey (795 respondents): spreadsheets the most-cited primary GRC tool (93 respondents), ServiceNow 86; 59% "commercially unaddressed"; no vendor above 18% share; average technical skill 5.4 of 10; 73.6% of CISOs use no commercial tool (GRCENGINEER-STATEOFGRC-2026). Full report not opened.
- ISC2 2025 workforce study: AI top skills need at 41%; GRC at 27%; 28% have integrated AI security tools, 19% testing, 22% evaluating; 63% of active AI security tool users report a significant productivity boost; 73% expect AI to create more specialized skills (ISC2-WORKFORCE-2025).
- Gartner via a secondary blog: 34% have well-defined AI governance but only partial adherence; 22% ad hoc; 7% recognized ethical-AI leaders; first Hype Cycle for AI Governance (published 21 July 2026, 32 innovations) (SOFTWARESTRATEGIES-GARTNERHC-2026). Not verified against Gartner.
- Quality evidence: none for AI in GRC. Nearest: studies of AI-written code cited by FAIR (see use case 08; vendor and academic, adjacent process, not GRC).

### Guardrails and regulatory points

- Responsibility sits with the deploying organization: the NIST AI RMF is built on the assumption that organizations, not models, own risk; EU AI Act Article 15 puts cybersecurity duties on providers of high-risk systems; no legal system has tested an agent-escape incident, per Dark Reading (DARKREADING-LIABLE-2026).
- Mandatory AI-incident reporting is being weighed: on 2026-10-06/07 an Australian parliamentary committee heard OpenAI, Anthropic, Microsoft and Google; an OpenAI executive said the company will now notify affected parties even if it does not fully understand a situation (DARKREADING-AUSREPORT-2026).
- EU AI Act (August 2026) brings automated audit, incident reporting and cybersecurity requirements per the CSA briefing (CSA-MYTHOSREADY-2026). DORA's four-hour notification clock was cited on the Resilient Cyber podcast (RESILIENTCYBER-TABLETOP-2026). Primary regulator sources are in the governance-angle files.
- Keep human review where actions follow: Venables on context bundles for approvers (VENABLES-HFT-2026); Anecdotes author on deterministic thresholds (BLEEPING-ANECDOTES-2026).

### Frontier signals (dated)

- 2026-03-24: allegations against Delve move "speed versus independent verification" to the front of compliance-automation discussion (IANS-DELVE-2026).
- 2026-04-12: CSA Mythos-ready briefing asks CISOs to update risk models, vendor onboarding governance and board talking points; also asks for reserve headcount and budget (CSA-MYTHOSREADY-2026, DARKREADING-MYTHOSCSA-2026).
- 2026-06-01 to 06-08: Gartner SRM summit sessions: board reports in financial-statement form; CISO mandate shifting from prevention to minimizing harm; 71% of board members willing to accept greater cyber-risk (TECHTARGET-GARTNERBOARD-2026, TECHTARGET-GARTNERCISO-2026).
- 2026-06-12: "CISO 2.0" and emerging "Chief Digital Risk Officer" form of the role (VENABLES-CISO2-2026).
- 2026-07-21: Gartner's first Hype Cycle for AI Governance (via secondary blog) (SOFTWARESTRATEGIES-GARTNERHC-2026).
- 2026-10-02: Dark Reading on avoiding "rogue AI" framing; 2026-10-16 on liability questions (DARKREADING-ROGUE-2026, DARKREADING-LIABLE-2026).
- 2026-10-02 to 10-14: FAIR Institute series on assessing coding agents, agent features and the AI attack surface (FAIR-AGENTICCODING-2026, FAIR-RISKREPORT-2026, FAIR-ATTACKSURFACE-2026).
- 2026-10-03: pyramid-to-diamond workforce argument (VENABLES-WORKFORCE-2026).
- 2026-10-06/07: Australian committee hearings on agentic incident reporting (DARKREADING-AUSREPORT-2026).
- 2026-10-07: Venture in Security argues AI skeptics and enthusiasts are both wrong, saying AI changes the speed of exploitation and the duty of care, not the reasons organizations are breached (VENTUREINSEC-SKEPTICS-2026).
- 2026-10-02: Resilient Cyber newsletter quotes a venture investor saying frontier-model news did more for CEO security awareness than a decade of CISO warnings, while noting budget is not translating cleanly into purchases (RESILIENTCYBER-NL116-2026).

### Workforce and role effects

- Pyramid to diamond; "new entry-level is directly into the mid-layer"; juniors review machine-generated work (VENABLES-WORKFORCE-2026).
- Role definitions: SANS/GIAC slides show 34% adding AI/ML specialists, 32% AI security engineers, 30% AI governance analysts (selected all that apply) (RSAC-WORKFORCE-2026). A BSides abstract lists "policy generation, reporting, architectural review" among work categories AI may replace the need to perform personally (BSIDESLV-2026, abstract of a talk by two CISOs).
- ISC2 respondents largely expect roles to evolve rather than disappear (ISC2-WORKFORCE-2025).
- Hiring authority has moved toward cyber management: 53% say the cyber manager is the primary hiring decision maker (RSAC-WORKFORCE-2026).
- Analysts shift from collection to management of agents (BLEEPING-ANECDOTES-2026); GRC engineering described as mostly reading systems (GRCENGINEER-086-2026).

### Objections and concerns practitioners raise

- "Trust becomes the bottleneck": effort is cheap, verification is not (BLEEPING-ANECDOTES-2026).
- Attestation integrity: a SOC 2 Type II report is not a security guarantee; accepting pre-populated evidence shows the market prioritized speed over control effectiveness, per an IANS faculty member (IANS-DELVE-2026).
- Anthropomorphic "rogue AI" language shifts blame and can serve vendor marketing (DARKREADING-ROGUE-2026).
- Independence of AI-safety evaluators: a podcast guest compares close evaluator relationships with a SOC 2 auditor who is also your best friend (RESILIENTCYBER-KORMAN-2026). This is one guest's opinion.
- Hype and inaction: the CSA register lists AI hype and confusion causing "systematic inaction" (CSA-MYTHOSREADY-2026).
- Over-restricting: Gartner's Candrick says more security can mean stalled AI and drained productivity (TECHTARGET-GARTNERCISO-2026).
- Pipeline: "eating their seed corn" if AI is only an entry-level cost cutter (VENABLES-WORKFORCE-2026).
- Skepticism of benchmarking inputs (budgets) rather than outcomes (VENABLES-BENCH-2026, listing only).
- Determinism: a search result about the GRC Engineer podcast (March 2026) says every compliance framework was built for deterministic systems and introduces AIUC-1; seen in search only (GRCENGINEER-PODCAST-2026).

### Interview probes for an advisor

1. When an agent or a platform prepares compliance evidence or a vendor assessment, who in your team checks it, how many controls or vendors do they sample each cycle, and have your auditors told you what they will accept?
2. Who decides what staff and agents in your own security team may do with AI (tools, data, actions), and what happens when someone breaks the policy or finds a better tool than the approved one?
3. How do you find AI features that vendors add after approval, and the tools your own staff build? Which of them are in your vendor register today?
4. Which risk-register entries or board metrics assume pre-AI patch windows or exploit scarcity? When did you last revisit them, and what would a director ask about whether you used AI defensively?
5. Where will your next generation of risk and assurance staff learn judgment if evidence collection and first-pass review disappear, and what have you changed in hiring or rotation to cover that?

## 4. Routed to other modules

- **ai-security:** OpenAI-Hugging Face agent-containment debate and eight-layer control-failure account (RESILIENTCYBER-KORMAN-2026, DARKREADING-ROGUE-2026); agent attack surface model (FAIR-ATTACKSURFACE-2026); BSides and FIRST agent-sandbox talks (BSIDESLV-2026, FIRST-CON-2026).
- **incident-response:** micro tabletops and notification clocks (RESILIENTCYBER-TABLETOP-2026); Centene living-timeline pipeline and DFIR-agent manipulation talks (FIRST-CON-2026); agent-incident reporting to regulators (DARKREADING-AUSREPORT-2026).
- **vulnerability-exposure:** the "AI vulnerability storm" and VulnOps as a permanent capability (CSA-MYTHOSREADY-2026, DARKREADING-MYTHOSCSA-2026).
- **application-security:** code-quality studies of AI-written code and pipeline gates (FAIR-AGENTICCODING-2026).
- **identity-access:** agent identity and privilege review (FAIR-RISKREPORT-2026, FAIR-ATTACKSURFACE-2026).
- **human-risk:** BSides "The Meeple Problem" (risk controls built around actions, not roles, using 6,500+ person survey research across nine countries) and AI voice-phishing study (N=4100) (BSIDESLV-2026, abstracts only).
- **security-operations:** FIRST-listed and BSides competitions study in which defenders used AI like a search engine, one issue at a time (FIRST-CON-2026, abstract only).

## 5. Sources

Counts by type (full-access sources only; 34 listed, 5 more seen in search only): press 8; community 12 (blogs and newsletters); podcast 3; conference 4; standard-setter 3; survey 2; professional-body 1; firm 1. Vendor-authored items are flagged.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| TECHTARGET-GARTNER-2026 | Gartner Security & Risk Management Summit 2026: Adapting for AI (conference guide) | TechTarget | press | https://www.techtarget.com/cybersecurity/conference/Gartner-Security-Risk-Management-Summit-2026-Adapting-for-AI | 2026-06 (last updated June 2026) | full |
| TECHTARGET-GARTNERBOARD-2026 | Lost in translation: Cybersecurity board reporting for CISOs | TechTarget | press | https://www.techtarget.com/cybersecurity/news/366643884/Lost-in-translation-Cybersecurity-board-reporting-for-CISOs | 2026-06-03 | full |
| TECHTARGET-GARTNERCISO-2026 | CISO role changes as cyber-risk appetites in the C-suite grow | TechTarget | press | https://www.techtarget.com/cybersecurity/news/366644003/CISO-role-changes-as-cyber-risk-appetites-in-the-C-suite-grow | 2026-06-08 | full |
| TECHTARGET-GARTNERREG-2026 | How to prepare security controls for future AI regulations (Gartner VP analyst Bernard Woo) | TechTarget | press | https://www.techtarget.com/cybersecurity/opinion/How-to-prepare-security-controls-for-future-AI-regulations | 2026-06-02 | full |
| RSAC-WORKFORCE-2026 | AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce (abstract and slides, Rob T. Lee and James Lyne) | RSA Conference / SANS-GIAC | conference | https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce | 2026-03-23 | full |
| RSAC-AGENTICSEM-2026 | RSAC Virtual Seminar: Agentic AI and the Challenges of Increased Autonomy Part 1 (CISO panel, sponsored by Wiz) | RSA Conference | conference | https://www.rsaconference.com/library/virtual-seminar/hds-22-agentic-ai-challenges-increased-autonomy | 2026-04-09 | full (abstract and speaker list only; recording not watched) |
| BSIDESLV-2026 | BSides Las Vegas 2026 talks (Cengage governance program; "Root To CISO - Just AIsk"; "Dr. Strangeprompt"; "Nobody Told Me I Could Grow"; hiring-manager role families; "The Meeple Problem") | Security BSides Las Vegas | conference | https://bsideslv.org/talks | 2026-08 (exact days not retrieved; the landscape file says early August) | full (abstracts) |
| FIRST-CON-2026 | 38th Annual FIRST Conference program (Centene; Jumpmind) | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06-16 | full (abstracts) |
| VENABLES-WORKFORCE-2026 | AI and Challenges in Workforce Development | Phil Venables | community | https://www.philvenables.com/post/ai-and-challenges-in-workforce-development | 2026-10-03 | full |
| VENABLES-CISO2-2026 | CISO Version 2.0 | Phil Venables | community | https://www.philvenables.com/post/ciso-version-2-0 | 2026-06-12 | full |
| VENABLES-CRE-2026 | Control Reliability Engineering (CRE): Applying SRE Principles to Cybersecurity Controls | Phil Venables | community | https://www.philvenables.com/post/control-reliability-engineering-cre-applying-sre-principles-to-cybersecurity-controls | 2026-07-25 | full |
| VENABLES-HFT-2026 | High Frequency Trading and Lessons for Agentic AI | Phil Venables | community | https://www.philvenables.com/post/high-frequency-trading-and-lessons-for-agentic-ai | 2026-05-02 | full |
| VENABLES-BENCH-2026 | Cybersecurity Benchmarking: Why, Why Not, When and How | Phil Venables | community | https://www.philvenables.com/post/cybersecurity-benchmarking-why-why-not-when-and-how | 2026-09-05 | search-only (blog index summary and date; body not read) |
| FAIR-RISKREPORT-2026 | Eight Takeaways from Anthropic's Risk Report for AI Risk Leaders (Todd Tucker) | FAIR Institute | standard-setter | https://www.fairinstitute.org/blog/eight-takeaways-from-anthropics-risk-report-for-ai-risk-leaders | 2026-09-25 | full (takeaways 1-4) |
| FAIR-AGENTICCODING-2026 | What Risk Leaders Should Be Asking When AI Is Building Software (Todd Tucker) | FAIR Institute | standard-setter | https://www.fairinstitute.org/blog/what-risk-leaders-should-be-asking-when-ai-is-building-software | 2026-10-02 | full |
| FAIR-ATTACKSURFACE-2026 | An AI Attack Surface Primer for Risk Professionals (Todd Tucker) | FAIR Institute | standard-setter | https://www.fairinstitute.org/blog/an-ai-attack-surface-primer-for-risk-professionals | 2026-10-14 | full |
| FAIR-CRMSURVEY-2026 | 2026 State of Cyber Risk Management Report | FAIR Institute (Hanover Research; sponsors GuidePoint Security, SAFE) | survey | https://www.fairinstitute.org/hubfs/State%20of%20Cyber%20Risk%20Management%20Report%202026.pdf | 2026 (fielded April 2026; month of publication not found) | full |
| RESILIENTCYBER-KORMAN-2026 | Cybersecurity is Ceding AI Safety, But Should We? (guest Zack Korman) | Resilient Cyber | podcast | https://www.resilientcyber.io/p/cybersecurity-is-ceding-ai-safety | 2026-09-28 | full (description and timestamps; audio and video not consumed) |
| RESILIENTCYBER-TABLETOP-2026 | AI-Accelerated Micro Tabletops and Incident Readiness (guest Matt Hartley, BreachRx; vendor) | Resilient Cyber | podcast | https://www.resilientcyber.io/p/ai-accelerated-micro-tabletops-and | 2026-10-12 | full (description only) |
| RESILIENTCYBER-NL116-2026 | Resilient Cyber Newsletter #116 | Resilient Cyber | community | https://www.resilientcyber.io/p/resilient-cyber-newsletter-116 | 2026-10-02 | full |
| VENTUREINSEC-SKEPTICS-2026 | Both AI skeptics and AI enthusiasts in cyber are wrong (Ross Haleliuk) | Venture in Security | community | https://ventureinsecurity.net/p/both-ai-skeptics-and-ai-enthusiasts | 2026-10-07 | full |
| CLOUDSECPOD-LOVABLE-2026 | How AI Agents Will Negotiate Your Vendor Contracts (Igor Andriushchenko, Lovable CISO; Jasper Mills, Ethira CEO) | Cloud Security Podcast | podcast | https://www.cloudsecuritypodcast.tv/videos/how-ai-agents-will-negotiate-your-vendor-contracts | 2026-05-27 | full (transcript) |
| CLOUDSECPOD-SENDBIRD-2025 | How to secure your AI Agents: A CISOs Journey (Yash Kosaraju, Sendbird) | Cloud Security Podcast | podcast | https://www.cloudsecuritypodcast.tv/videos/how-to-secure-your-ai-agents-a-cisos-journey | 2025-12-09 | full (transcript) |
| IANS-DELVE-2026 | Delve Allegations Expose Weak Points in Modern Compliance | IANS Research | firm | https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/30/delve-allegations-expose-weak-points-in-modern-compliance | 2026-03-24 (byline; page URL dated 2026-03-30) | full |
| GRCENGINEER-STATEOFGRC-2026 | State of GRC 2026 Report: Spreadsheets are still #1 | GRC Engineer newsletter | survey | https://www.grcengineer.com/p/state-of-grc-2026-report-spreadsheets-are-still-1 | 2026-03-16 | full (post; the 36-page PDF not opened) |
| GRCENGINEER-086-2026 | Most GRC Engineering Is Sysadmin Work. That's the Good News. | GRC Engineer newsletter | community | https://www.grcengineer.com/p/most-grc-engineering-is-sysadmin-work-that-s-the-good-news | 2026-10-15 | full |
| GRCENGINEER-AIUSAGE-2026 | 3 Basic Things Killing Your AI Usage for GRC | GRC Engineer newsletter | community | https://www.grcengineer.com/p/3-basic-things-killing-your-ai-usage-for-grc | 2026-01-08 | full |
| BLEEPING-ANECDOTES-2026 | Your First GRC Agent: A Red Teamer's Walkthrough (byline: Anecdotes GRC engineering evangelist; vendor-authored) | BleepingComputer | press | https://www.bleepingcomputer.com/news/security/your-first-grc-agent-a-red-teamers-walkthrough/ | 2026-06-26 | full |
| DARKREADING-ROGUE-2026 | Is It Fair to Blame 'Rogue' AI for Security Failures? | Dark Reading | press | https://www.darkreading.com/insider-threats/blame-rogue-ai-security-failures | 2026-10-02 | full |
| DARKREADING-LIABLE-2026 | When AI Agents Commit Breaches, Humans May Not Be Held Liable | Dark Reading | press | https://www.darkreading.com/insider-threats/ai-agents-breaches-humans-liable | 2026-10-16 | full |
| DARKREADING-MYTHOSCSA-2026 | CSA: CISOs Should Prepare for Post-Mythos Exploit Storm | Dark Reading | press | https://www.darkreading.com/cloud-security/csa-cisos-prepare-post-mythos-exploit-storm | 2026-04-13 | full |
| DARKREADING-AUSREPORT-2026 | Australian Gov't Weighs Mandatory AI Incident Reporting | Dark Reading | press | https://www.darkreading.com/cybersecurity-operations/australian-govt-ai-incident-reporting | 2026-10-07 | full |
| CSA-MYTHOSREADY-2026 | The "AI Vulnerability Storm": Building a "Mythos-ready" Security Program (briefing page and PDF v1.0, 29 pages) | Cloud Security Alliance with SANS, [un]prompted, OWASP GenAI Security Project | standard-setter | https://labs.cloudsecurityalliance.org/mythos-ciso/ (PDF: https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/mythosreadyv1.0.pdf) | 2026-04-12 (page); PDF file created 2026-05-01 | full |
| SOFTWARESTRATEGIES-GARTNERHC-2026 | Gartner AI Governance Hype Cycle 2026: What CISOs Fund First (Louis Columbus; secondary summary of Gartner) | Software Strategies Blog | community | https://softwarestrategiesblog.com/2026/08/10/gartners-2026-ai-governance-hype-cycle-and-what-cisos-must-change-to-control-agentic-ai-and-rogue-agents/ | 2026-08-10 | full |
| ISC2-WORKFORCE-2025 | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full |
| GRCENGINEER-PODCAST-2026 | GRC Engineer podcast, March 2026 episode on deterministic frameworks and AIUC-1 | GRC Engineer | podcast | https://www.iheart.com/podcast/269-grc-engineer-245395245/ | 2026-03 | search-only |
| SAFE-RSAC-2026 | The Autonomous Era of Cyber Risk Is Here. See It at RSAC 2026 | SAFE Security | vendor | https://safe.security/resources/blog/safe-rsac-2026-agentic-ai-ctem-crq-tprm/ | 2026-03 | search-only |
| GARTNER-AGENTICBOARD-2026 | Consult the Board: Managing the Rise of Agentic AI (Gartner Insights abstract) | Gartner | firm | https://www.gartner.com/en/documents/7692725 | 2026-04-07 | search-only |
| BLACKHAT-CISOSUMMIT-2026 | CISO Summit, Black Hat USA 2026 (4 Aug 2026, Chatham House Rule) | Black Hat | conference | https://blackhat.com/us-26/ciso-summit.html | 2026-08-04 | search-only |
| FAIRCON26-2026 | Call for Speakers: FAIRCON26, "AI Is Rewriting Cyber Risk. What Comes Next?" | FAIR Institute | standard-setter | https://www.fairinstitute.org/blog/call-for-speakers-faircon26 | 2026 | search-only |

## 6. Gaps

- **Quality evidence.** No source reports override rates, accuracy audits, parallel runs, auditor reliance or inspection findings for AI in security GRC. The only figures are survey self-reports and a count in a talk abstract.
- **Reddit, Hacker News, Slack and Discord communities.** Reddit blocked anonymous access during this run, and Hacker News threads on GRC and AI had little discussion; community talk is represented by newsletters, blogs and podcasts instead.
- **Gartner and Forrester primary research.** Gartner's site returned a bot challenge; Gartner material comes from TechTarget write-ups of summit sessions and a secondary blog (Hype Cycle). Forrester was not revisited for this module.
- **Black Hat and DEF CON.** The official CISO Summit page was seen in search only and is Chatham House, so no attributed remarks are available. No DEF CON governance session was found.
- **RSAC 2026.** Only one workforce session (slides) and a virtual-seminar abstract were read; the RSAC library search was not accessible, and the SANS/GIAC 2026 Workforce Report itself was not retrieved (the report page returned 404), so survey sample sizes are missing.
- **Podcasts.** Show notes and transcripts only; no audio or video was consumed. The GRC Engineer podcast (including a vendor roundtable) was seen in search only. The Risky Business episode with a PwC risk leader (RB853) was read at show-notes level and not used.
- **ISACA.** The 2026 State of Cybersecurity page returned no statistics, and the press release link failed; ISACA figures are in the practice-angle file.
- **Questionnaire-automation trust.** A search for practitioner views on buyers receiving AI-drafted answers found only vendor marketing.
- **Risk quantification critique.** No independent critique of LLM-produced loss estimates was found; the FAIR pieces are guidance by the standard-setter.
- **WEF Global Cybersecurity Outlook 2026.** Opened but the page showed no publication date and carried survey statistics in a form that needs the PDF; not used.
- **Dates.** BSides Las Vegas 2026 exact days and the FAIR 2026 survey publication month were not found; both are marked.
- **Delve.** All Delve content is allegation; no regulator, court or auditor finding was read.
