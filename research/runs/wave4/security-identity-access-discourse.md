# Security / identity-access / discourse: how practitioners talk about AI in identity and access

Archetype: security. Module: identity-access (IAM, privileged access, authentication, identity governance, identity threat detection and response, identity-related fraud; identities for AI agents are routed to ai-security). Angle: discourse. Researched 2026-10-17. Window: roughly 2025-04 to 2026-10, with older items used only as foundations.

## 1. Summary

- **The conversation is dominated by agent identity, which is out of scope here.** Identiverse 2026, KuppingerCole EIC 2026, Oktane 2026 and the Gartner IAM Summit agenda (December 2026) are all framed around AI agents. Forrester's Identiverse recap says non-human identity and AI security was the predominant theme across the 200-plus expo booths (FORRESTER-IDENTIVERSE-2026). I routed that material to ai-security and kept the human-identity and defender-use material here.
- **For human IAM, the loudest AI story is the attacker's.** Practitioners describe AI-enabled impersonation (cloned voices, deepfake video and documents, injection attacks against selfie checks) landing on the weakest control: the service desk and the account-recovery path. The recurring prescription is to stop asking staff to judge whether a caller is real and to enforce a verification step instead (INFOSEC-SERVICEDESK-2026, PETRI-SERVICEDESK-2026, NAMETAG-IMPERSONATION-2026).
- **A counter-narrative is credible and measured.** Okta Threat Intelligence argues that AI is an accelerant and not a new attack class, and says its analysis of about 6,000 real-world social-engineering events shows that enforcing phishing-resistant factors, including in factor-enrollment policies, would have stopped nearly all account takeovers in that sample. This is a "would have" estimate by a vendor, not a deployed result (OKTA-TI-INVARIANTS-2026). Forrester made a similar point about RSAC: agentic AI was "pasted into" old messages such as "you need good identity governance" (FORRESTER-RSAC-2026).
- **Defender-side AI in human IAM is mostly vendor announcements with no published outcomes.** AI-guided access reviews (SailPoint, Opal), a Conditional Access optimization agent and risky-user summaries (Microsoft Entra), AI access-request approval (Opal) and AI-contextual just-in-time privilege (Palo Alto Networks/CyberArk Idira) are all described. None has a published override rate, false-approval rate or parallel-run result. The two named-deployment entries (Okta's own IT assistant and Push Security's agentic detection pipeline) report throughput or adoption, not decision quality.
- **Measured evidence that does exist is about the gap between detection and response.** SANS's 2026 ITDR survey reports 68% of organizations detect identity attacks within 24 hours but 55% contain them in that window, and 55% had an identity-related breach in the past 12 months despite 85% reporting ITDR tools (SANS-ITDR-2026). That is the strongest independent-style number for the module.
- **Main worries:** deepfake detectors that decay against new generators (HN-REALITYDEFENDER-2025, ARXIV-2609.09489); help-desk and recovery abuse that sidesteps strong authentication (OKTA-TI-MFADOWNGRADE-2026, VECTRA-SPIDER-2026); auto-approval turning certification into an unaccountable model decision; automation lockouts and false positives (NETWRIX-ITDR-2026, FORRESTER-BIOCATCH-2026); and the "five-year problem" for early-career talent (FORRESTER-RSAC-2026).

## 2. Use cases

Grades: no entry reaches grade A. Two are grade B (named deployment, no quality measurement, adjacent process), twelve are C (vendor or analyst claim) and two are D (ideas that researchers discuss).

```yaml
- id: security-identity-access-01
  title: AI-guided approve/revoke recommendations in access certification campaigns
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Managers and application owners are handed long lists of entitlements to certify with little context. SailPoint says many end up approving everything for fear of removing needed access, which leaves over-provisioning in place. Opal describes the same pattern: routine and dangerous grants get the same glance."
  solution: "SailPoint describes Access Recommendations: peer-group analysis using identity attributes such as location, role and department suggests approve or revoke during a campaign, excludes birthright access from the list and auto-approves low-risk items. Opal announced AI-guided access reviews on 2026-06-15: its access agent surfaces low-risk grants with the signals it used (resource sensitivity, requester risk, temporal context) so a reviewer can clear them in one click, and risky grants go to a person. Opal also describes natural-language campaign scoping and an adjustable autonomy setting."
  outcomes:
    - lever: quality
      description: "none published. Neither source gives an override rate, a false-approval rate or a before/after comparison."
      figure: "none published"
      measures: "n/a"
      provenance: vendor-published
      source_ref: OPAL-REVIEWS-2026
  prerequisites:
    - "Accurate manager and HR mappings plus entitlement context; NHIMG's summary of an Omada post says reviews degrade without them (NHIMG-OMADA-2026, key questions)."
    - "A written policy the model can be tuned to; Opal says customers articulate their own policy and set a confidence threshold a recommendation must clear before it acts (OPAL-REVIEWS-2026, section 'Tune the AI to your policy')."
  risks_and_guardrails:
    - "SailPoint says the feature auto-approves low-risk access so managers can focus on high-risk items; it publishes no error or override rate for those auto-approvals (SAILPOINT-RECS-2022, section 'AI-driven Access Recommendations')."
    - "Opal logs every recommendation and approval with its reasoning for audit (OPAL-REVIEWS-2026, section 'Review faster, with AI that shows its work')."
    - "NHIMG's summary argues AI recommendations change how reviewers are supported but human sign-off keeps accountability (NHIMG-SAILPOINT-2026, key questions)."
  human_checkpoints:
    - "Opal says risky calls always reach a person and that autonomy is a dial, from a human approving every grant to wider scope (OPAL-REVIEWS-2026, section 'A dial, not a switch')."
  role_evolution: "Reviewer effort is meant to shift to the high-risk grants; Opal frames the constraint as reviewer attention and not effort (OPAL-REVIEWS-2026, opening paragraph)."
  evidence_grade: C
  sources:
    - { ref: SAILPOINT-RECS-2022, title: "AI-driven Access Recommendations: Less Certification. More Revocation.", publisher: SailPoint, type: vendor, url: "https://www.sailpoint.com/blog/ai-driven-access-recommendations-less-certification-more-revocation", date: 2022-06-30, access: full, locator: "section 'AI-driven Access Recommendations'" }
    - { ref: OPAL-REVIEWS-2026, title: "AI-Guided access reviews, now in Opal", publisher: Opal Security, type: vendor, url: "https://www.opal.dev/blog/ai-guided-access-reviews", date: 2026-06-15, access: full, locator: "sections 'Review faster', 'A dial, not a switch', 'Tune the AI to your policy'" }
    - { ref: NHIMG-SAILPOINT-2026, title: "AI-driven access recommendations expose the limits of certification (NHIMG summary of the SailPoint post)", publisher: Non-Human Identity Management Group, type: community, url: "https://nhimg.org/articles/ai-driven-access-recommendations-expose-the-limits-of-certification/", date: 2026-06-24, access: full, locator: "'At a glance' and 'Key questions'" }
  last_reviewed: 2026-10-17
  notes: "Date conflict: NHIMG labels the SailPoint post 'December 10, 2025', but the SailPoint page's own JSON-LD gives datePublished 2022-06-30, so this is a long-standing feature, not a 2025-26 launch. Opal's post names Mercari as governing more than 5,000 Okta entitlements through automated reviews on Opal; the post does not say Mercari uses the AI-guided features, so I did not treat it as a deployment of this use case. Search-only vendor figures (an Avatier claim of a 70% fatigue reduction and a Ponemon figure of 63% rubber-stamping, both seen only in search results) are not used."

- id: security-identity-access-02
  title: AI role discovery and policy suggestions for access governance (idea stage)
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [expert-judgment, data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Role engineering is hand-curated, and stable access sits as long entitlement lists that reviewers cannot interpret. NHIMG's summary of an Omada post says legacy governance assumes people can read dense access data at scale."
  solution: "Omada (via NHIMG) says AI adds context to certification, approvals, audit reporting and role discovery, with stable access grouped into lean roles and reviews focused on permissions that do not match peer patterns. Opal's 2026-08-06 post lists role mining (propose roles and cohorts from the access people actually hold and use) and policy suggestions (promote access every cohort member gets to auto-approval, flag outliers) under 'Where Paladin is going'."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "n/a"
      provenance: vendor-published
      source_ref: OPAL-PALADIN-2026
  prerequisites:
    - "Usage data on granted access, since Opal's role mining learns from what people hold and use (OPAL-PALADIN-2026, section 'Where Paladin is going')."
  risks_and_guardrails:
    - "Not stated by the sources beyond Opal's general statement that Paladin's authority is graduated and logged (OPAL-PALADIN-2026, section 'Automate the routine, escalate the rest')."
  human_checkpoints:
    - "Not specified for role mining or policy suggestions in the sources read."
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
    - { ref: OPAL-PALADIN-2026, title: "Paladin: AI that applies your policy to every request", publisher: Opal Security, type: vendor, url: "https://www.opal.dev/blog/paladin-policy-ai", date: 2026-08-06, access: full, locator: "section 'Where Paladin is going'" }
    - { ref: NHIMG-OMADA-2026, title: "AI augments IGA by fixing review fatigue and weak audit context (NHIMG summary of an Omada post)", publisher: Non-Human Identity Management Group, type: community, url: "https://nhimg.org/articles/ai-augments-iga-by-fixing-review-fatigue-and-weak-audit-context/", date: 2026-06-24, access: full, locator: "'Context' and 'Key questions'" }
  last_reviewed: 2026-10-17
  notes: "NHIMG says its summary is based on an Omada post dated 2025-08-15; I could not open the Omada original (403), so the Omada claims are second-hand."

- id: security-identity-access-03
  title: Conditional Access gap analysis and policy suggestions by an AI agent
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [software-systems, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: "Administrators must keep Conditional Access policies covering every new user, application and agent identity, avoid overlapping policies, and spot policies with too many exceptions (gaps) or none (lockout risk)."
  solution: "Microsoft documents a Security Copilot agent that scans the tenant every 24 hours for new users, applications and agent identities, checks policy gaps, proposes consolidation of similar policies and creates new policies only in report-only mode. Suggestions cover MFA, device controls, legacy-authentication and device-code blocking, and risk-based policies; a deep MFA gap analysis counts users outside any MFA-requiring policy. An administrator reviews and applies each suggestion; phased rollout plans and ServiceNow ticket creation are optional."
  outcomes:
    - lever: quality
      description: "none published. The documentation lists capabilities and limits but no results."
      figure: "none published"
      measures: "n/a"
      provenance: vendor-published
      source_ref: MS-CAAGENT-2026
  prerequisites:
    - "Entra ID P1 (P2 for risk-based suggestions), provisioned security compute units (documented average under one unit per run, with the provisioned unit billed monthly), Security Administrator to activate the first time, and Intune licenses for device-based suggestions (MS-CAAGENT-2026, section 'Prerequisites')."
  risks_and_guardrails:
    - "Documented limits: a run cannot be stopped once started; each run reviews up to 300 users and 150 applications and evaluates 40 similar policy pairs; scanning covers a 24-hour period; suggestions cannot be customized or overridden (MS-CAAGENT-2026, section 'Limitations')."
    - "The agent makes no change to existing policies unless an administrator approves, and new policies are created in report-only mode (MS-CAAGENT-2026, 'Important' note)."
  human_checkpoints:
    - "Administrator reviews the policy and its impact and applies the suggestion; Security Reader and Global Reader can view but not act (MS-CAAGENT-2026, section 'Prerequisites' and 'Getting started')."
  role_evolution: "Conditional Access administrators can be given Security Copilot access to use the agent; no workforce effect is described (MS-CAAGENT-2026, section 'Prerequisites')."
  evidence_grade: C
  sources:
    - { ref: MS-CAAGENT-2026, title: "Microsoft Entra Conditional Access Optimization Agent", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization", date: 2026-06-23, access: full, locator: "sections 'How it works', 'Limitations', 'Prerequisites'; date is the page's ms.date" }
  last_reviewed: 2026-10-17
  notes: "Practitioner reviews exist but I could only see them in search results (PRACTICAL365-ENTRAAGENTS-2025, 2025-10-07, whose page returned a server error; a Substack write-up and a changelog). One commenter reportedly cross-checks the agent against the free Maester tool; this is search-only and not used as evidence. The documentation marks ServiceNow integration and activity-based runs as preview."

- id: security-identity-access-04
  title: Natural-language risk summaries for identity incidents and risky users
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [research-synthesis]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: "Analysts and administrators investigating a flagged identity must assemble context on why a user's risk level rose and what to do."
  solution: "Copilot in Microsoft Entra, inside Entra ID Protection, summarizes in natural language why a user was flagged, lists next steps and links to documentation. The documentation also mentions a separate Identity Risk Management Agent whose summary appears alongside it when enabled."
  outcomes:
    - lever: speed
      description: "Microsoft says the feature helps reduce time to resolution; no figure is published."
      figure: "none published"
      measures: "n/a"
      provenance: vendor-published
      source_ref: MS-ENTRA-RISKYUSER-2025
  prerequisites:
    - "Entra ID P2 and a tenant with Security Copilot enabled; Security Reader at minimum (MS-ENTRA-RISKYUSER-2025, sections 'Prerequisites' and 'Investigate risky users')."
  risks_and_guardrails:
    - "The summary is advice; remediation (for example creating sign-in risk policies) is performed by the responder (MS-ENTRA-RISKYUSER-2025, 'What to do' list)."
  human_checkpoints:
    - "The responder decides and applies any remediation."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: MS-ENTRA-RISKYUSER-2025, title: "Respond to identity threats using risky user summarization", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/entra/security-copilot/entra-risky-user-summarization", date: 2025-09-23, access: full, locator: "opening paragraphs; date is the page's ms.date" }
  last_reviewed: 2026-10-17

- id: security-identity-access-05
  title: Closed-loop identity threat response that acts on high-confidence detections without a ticket
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [transaction-processing]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Identity attacks are detected quickly but response waits in a human queue. SANS's survey finds a gap between detecting identity attacks and containing them. Palo Alto Networks describes a ticket hand-off between the SOC and the identity team as a structural flaw."
  solution: "Netwrix describes ITDR automation as running pre-defined responses (disable the account, block the protocol operation, force re-authentication, trigger SOAR playbooks) the moment high-confidence thresholds are met, rolled out in stages with audit-mode testing and two thresholds per rule (act automatically vs route to a human). Palo Alto Networks proposes 'IdentitySecOps', joining identity posture, detection, response and learning in one loop with shared context."
  outcomes:
    - lever: speed
      description: "Gap between detecting and containing identity attacks (the problem baseline, not a result of a fix)."
      figure: "68% detect within 24 hours; 55% contain within the same window"
      measures: "Share of surveyed organizations that detect identity attacks within 24 hours, and share that contain them in that window (SANS 2026 ITDR survey; respondent count not stated on the page)"
      provenance: independent
      source_ref: SANS-ITDR-2026
  prerequisites:
    - "An identity attack-surface inventory and clean posture baseline before enabling automation, because untuned rules produce false positives and programs then stay detection-only (NETWRIX-ITDR-2026, best practice 1 and core component 3, 'Identity posture management as an automation prerequisite')."
    - "Structured alerts (attack type, accounts, timeline, confidence score) that SOAR playbooks can use (NETWRIX-ITDR-2026, best practice 5)."
  risks_and_guardrails:
    - "Start with well-defined, near-zero-false-positive patterns (Kerberoasting, DCSync, pass-the-hash, golden ticket) and expand to behavioral rules later; enabling response on untuned behavioral rules leads to alert fatigue (NETWRIX-ITDR-2026, best practice 2)."
    - "Test blocking in audit mode so legitimate admin workflows are not blocked (NETWRIX-ITDR-2026, best practice 4)."
  human_checkpoints:
    - "Netwrix defines a second, lower threshold that routes to a human review queue (NETWRIX-ITDR-2026, best practice 3)."
  role_evolution: "Palo Alto Networks says identity and security operations should share context, response and accountability (PANW-IDSECOPS-2026, section 'IdSecOps Connects Detection and Response')."
  evidence_grade: C
  sources:
    - { ref: SANS-ITDR-2026, title: "SANS 2026 State of Identity Threat Detection and Response: Key Findings", publisher: SANS Institute, type: survey, url: "https://www.sans.org/research/identity-threat-detection-response-report", date: 2026-03, access: full, locator: "'Key Findings' and 'FAQs'" }
    - { ref: NETWRIX-ITDR-2026, title: "ITDR automation best practices for security teams", publisher: Netwrix, type: vendor, url: "https://www.netwrix.com/en/resources/blog/itdr-automation-best-practices/", date: 2026-06-05, access: full, locator: "seven best practices" }
    - { ref: PANW-IDSECOPS-2026, title: "IdentitySecOps for AI-Speed Defense", publisher: Palo Alto Networks (Idira blog), type: vendor, url: "https://www.paloaltonetworks.com/blog/identity-security/identitysecops-closed-loop-model-ai-speed-defense/", date: 2026-08-05, access: full, locator: "sections 'AI Attacks Can Outrun Human-Speed Defense', 'Four Questions That Define IdSecOps'" }
  last_reviewed: 2026-10-17
  notes: "The Netwrix post describes rule-based automation and does not say it uses AI; the AI link comes from Palo Alto Networks' framing and the survey's 73% figure for agentic automations (see Routed). Grade C because the SANS figures measure the problem, not an outcome of automating response. The SANS page is internally inconsistent: its headline says 85% of organizations with identity tools still suffered a breach, while its key findings and FAQ say 85% deployed ITDR tools and 55% had an identity-related breach; I used the key findings. SANS states sponsors had no role in design or analysis. Search-only: Blackpoint Cyber (MSSP-BLACKPOINT-2026, via MSSP Alert, blocked) is reported to have an AI SOC agent for identity threat response, with a vendor claim of containment in under two minutes on average; not used as evidence."

- id: security-identity-access-06
  title: Behavioral biometrics to detect account takeover, mule accounts and scams before payment
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types: [transaction-processing, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Payment-transaction monitoring does not address pre-payment risks such as identity theft, account takeover, scams and first-party fraud (Forrester's reading of the Visa deal)."
  solution: "Forrester describes BioCatch as using website JavaScript and mobile SDKs to analyze typing cadence, touchscreen gestures, mouse movements, hesitation and device handling to detect identity theft at registration, account takeover, mule accounts and scams before a payment occurs. Visa announced its intent to acquire BioCatch for USD 2.4 billion (reported 2026-08-05)."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "n/a"
      provenance: independent
      source_ref: FORRESTER-BIOCATCH-2026
  prerequisites:
    - "Integration with customer identity and access management, authentication and deepfake-detection platforms; Forrester names the cost and complexity of that integration as a main deployment challenge (FORRESTER-BIOCATCH-2026, paragraph beginning 'The main challenges')."
  risks_and_guardrails:
    - "Forrester lists ways to evade behavioral biometrics (AI-driven robotic behaviors, bots, robotic process automation) and false positives when users' motor patterns change, for example from an injury; false positives can insult honest customers and cause attrition (FORRESTER-BIOCATCH-2026, paragraph beginning 'Behavioral biometrics provides')."
    - "Behavioral data may count as personally identifiable information in some jurisdictions (FORRESTER-BIOCATCH-2026)."
  human_checkpoints:
    - "Not described; the product provides risk signals."
  role_evolution: "Forrester says the standalone behavioral-biometrics market is effectively ending as it is absorbed into financial-crime, CIAM and commerce fraud management markets (FORRESTER-BIOCATCH-2026, closing section)."
  evidence_grade: C
  sources:
    - { ref: FORRESTER-BIOCATCH-2026, title: "Visa To Acquire Behavioral Biometrics Specialist BioCatch For $2.4 Billion", publisher: Forrester, type: firm, url: "https://www.forrester.com/blogs/visa-to-acquire-behavioral-biometrics-specialist-biocatch-for-2-4-billion/", date: 2026-08-05, access: full, locator: "whole post" }
  last_reviewed: 2026-10-17
  notes: "This is an analyst post on an acquisition announcement. It names no customer deployment and no result. The source does not call the technology AI; behavioral biometrics are machine-learning based, but that is my characterization, not the source's."

- id: security-identity-access-07
  title: Deepfake- and injection-resistant identity verification for onboarding, step-up and account recovery
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types: [transaction-processing, review-assurance]
  pattern: document-to-decision
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Single-moment selfie and document checks can be defeated by deepfaked media and by injection attacks that feed manipulated images or video straight into the verification pipeline. FinCEN reported rising suspicious-activity reports describing suspected deepfake media since 2023 (fraudulent identity documents used to circumvent verification)."
  solution: "Vendors and analysts recommend layered checks: presentation-attack detection, injection-attack detection, image inspection, device and session context, and workforce-grade identity verification (government ID plus selfie, blocking injection and deepfakes) wrapped around enrollment, recovery and step-up. NIST SP 800-63-4 (final July 2025) adds controls for injection attacks and forged media."
  outcomes:
    - lever: risk
      description: "Threat measurement, not a defender result: share of biometric fraud attempts that were deepfakes."
      figure: "deepfakes were 'one in five biometric fraud attempts'; deepfaked selfies up 58% in 2025; injection attacks up 40% year over year"
      measures: "Entrust 2026 Identity Fraud Report, as quoted by Crowdfund Insider: share of biometric fraud attempts involving deepfakes; change in deepfaked selfies during 2025; change in injection attacks year over year. Denominators and customer base not stated in the article."
      provenance: vendor-published
      source_ref: CFI-ENTRUST-2025
  prerequisites:
    - "Integration with directories and enterprise identity infrastructure and fast deployment, which Nametag lists as requirements for workforce-grade verification (NAMETAG-IMPERSONATION-2026, p.14)."
  risks_and_guardrails:
    - "Detector robustness is contested: a Hacker News thread on a deepfake-detection launch raised unseen generators and the arms-race dynamic (HN-REALITYDEFENDER-2025, comments), and an arXiv preprint reports that 21 of 29 statistical features reversed their discriminative direction between training and in-the-wild deployment for its audio detector (ARXIV-2609.09489, abstract)."
    - "Nametag says video calls should not be trusted for verifying employees or candidates, and advises in-person verification when someone cannot complete identity verification (NAMETAG-IMPERSONATION-2026, p.13)."
    - "Oz Forensics, as summarized by NHIMG, says a single liveness check is not a durable trust boundary and that the problem moves to session integrity and signal provenance (NHIMG-OZ-2026, 'Context')."
  human_checkpoints:
    - "Failed or suspicious verifications are escalated for human review (NAMETAG-IMPERSONATION-2026, p.13)."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: CFI-ENTRUST-2025, title: "Deepfakes, Social Engineering, Injection Attacks On The Rise, Report Reveals (on Entrust's 2026 Identity Fraud Report)", publisher: Crowdfund Insider, type: press, url: "https://www.crowdfundinsider.com/?p=255847", date: 2025-11-25, access: full, locator: "first three paragraphs" }
    - { ref: NAMETAG-IMPERSONATION-2026, title: "Rebuilding Trust in the Age of AI: The 2026 Workforce Impersonation Report", publisher: Nametag, type: vendor, url: "https://www.go.nametag.co/hubfs/The%202026%20Workforce%20Impersonation%20Report.pdf", date: 2026, access: full, locator: "pp.13-14 'The Limits of Video Verification' and 'Workforce Identity Verification'" }
    - { ref: FINCEN-DEEPFAKE-2024, title: "FinCEN Alert FIN-2024-Alert004: Fraud Schemes Involving Deepfake Media Targeting Financial Institutions", publisher: FinCEN (US Treasury), type: regulator, url: "https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf", date: 2024-11-13, access: full, locator: "p.1 and 'Detecting and Mitigating Deepfake Identity Documents'" }
    - { ref: NIST-80063-2025, title: "NIST SP 800-63 Digital Identity Guidelines, Revision 4", publisher: NIST, type: standard-setter, url: "https://pages.nist.gov/800-63-4/", date: 2025-07, access: full, locator: "'Background' list of changes" }
    - { ref: NHIMG-OZ-2026, title: "Industrialized fraud is breaking legacy identity verification controls (NHIMG summary of an Oz Forensics post)", publisher: Non-Human Identity Management Group, type: community, url: "https://nhimg.org/articles/industrialized-fraud-is-breaking-legacy-identity-verification-controls/", date: 2026-07-11, access: full, locator: "'TL;DR' and 'Context'" }
    - { ref: HN-REALITYDEFENDER-2025, title: "Launch HN: Reality Defender (YC W22) - API for Deepfake and GenAI Detection", publisher: Hacker News, type: community, url: "https://news.ycombinator.com/item?id=44941580", date: 2025-08-18, access: full, locator: "top-level threads on reliability and the arms race" }
    - { ref: ARXIV-2609.09489, title: "Audio Deepfake Detection Using Temporal Coherence Analysis", publisher: arXiv (preprint), type: academic, url: "https://arxiv.org/abs/2609.09489", date: 2026-09-08, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: "Nametag's report date: the title says 2026 and the text cites events through September 2025 and makes 2026 predictions; I could not find the month. Nametag, Entrust and Oz Forensics sell identity verification, so their threat figures are vendor-published. The Reality Defender founder's claim in the thread of deployments to 'several Tier 1 banks' is unnamed and unverified. Search-only: a Gartner 2024-02-01 press release predicting that by 2026, 30% of enterprises will not consider identity verification and authentication solutions reliable in isolation because of deepfakes (GARTNER-DEEPFAKE-2024, seen in search results; Gartner's site blocked access), and Entrust's press release itself (blocked)."

- id: security-identity-access-08
  title: Service-desk and account-recovery verification enforced by workflow instead of agent judgment
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [transaction-processing, client-interaction]
  pattern: service-agent-escalation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Attackers call the help desk posing as employees and ask for password and MFA resets. An FBI complaint, as analyzed by Vectra, describes one May 2025 intrusion where calls from two Google Voice numbers led to three compromised accounts within roughly two to three hours with no exploit or malware. Practitioners say cloned voices make it harder still for staff to judge a caller."
  solution: "Specops authors (writing on Petri and Infosecurity Magazine) argue that no password, MFA or recovery action should proceed until the user passes an enforced identity-verification workflow using an approved authenticator, that knowledge-based proof (employee ID, security questions) should stop, and that the agent should not have to decide whether a caller sounds genuine. They also recommend red-team testing of service-desk procedures. Okta Threat Intelligence adds that factor-enrollment policies should themselves demand phishing-resistant proof, with a managed device, a trusted network or a third-party identity-verification service."
  outcomes:
    - lever: risk
      description: "Counterfactual estimate by Okta on account-takeover attempts, not a deployed result."
      figure: "88% of account-takeover attempts could have been stopped by mandatory phishing-resistant enrollment; 99.75% with phishing resistance in app sign-in policies; 0.25% still compromised"
      measures: "Share of about 6,000 analyzed real-world social-engineering events (from an internal dataset of over 10,000 campaigns) in which the account-takeover session would have been prevented had the policy been in place; account takeover defined as any compromised identity-provider session; excludes compromised devices, malware or remote-management downloads and malicious-app authorizations"
      provenance: vendor-published
      source_ref: OKTA-TI-INVARIANTS-2026
  prerequisites:
    - "Phishing-resistant authenticators already enrolled; the residual risk Okta describes is 'account bootstrapping', verifying a user before they can enroll a strong factor (OKTA-TI-INVARIANTS-2026, section on residual risk)."
    - "A documented escalation path for failed verification (PETRI-SERVICEDESK-2026, closing paragraph)."
  risks_and_guardrails:
    - "Attackers push users to downgrade from a phishing-resistant method to a phishable one; Okta saw a phishing kit from August 2026 telling users a hardware key 'may need to be re-registered' to push them to a one-time code (OKTA-TI-MFADOWNGRADE-2026, 'When the downgrade pretext is baked into the phishing kit')."
    - "Specops says its product exports verification events to a SIEM so there is an audit trail showing verification happened before a sensitive action (INFOSEC-SERVICEDESK-2026, section 'Remove the Judgement Call from Identity Verification')."
    - "Petri's author cites a Google Mandiant red-team exercise in which researchers trained a model on a security team member's voice and spoofed calls to gain initial access; it was not run against a service desk (PETRI-SERVICEDESK-2026, point 4)."
  human_checkpoints:
    - "Failed verification goes into a documented escalation workflow and is not handled as an exception under pressure (PETRI-SERVICEDESK-2026, closing paragraph)."
  role_evolution: "Specops argues service-desk staff should not be the final identity control; their job is to follow a process that stays secure even when the caller is persuasive (PETRI-SERVICEDESK-2026, point 5; INFOSEC-SERVICEDESK-2026, 'Why Agent Training Reaches a Limit')."
  evidence_grade: C
  sources:
    - { ref: INFOSEC-SERVICEDESK-2026, title: "Your Service Desk Agents Can't Out-Talk an AI", publisher: Infosecurity Magazine (author from Specops Software, an Outpost24 company), type: vendor, url: "https://www.infosecurity-magazine.com/blogs/your-service-desk-agents-cant/", date: 2026-10-06, access: full, locator: "sections 'Why Agent Training Reaches a Limit', 'The Service Desk is Where Strong Authentication Can Weaken'" }
    - { ref: PETRI-SERVICEDESK-2026, title: "5 Ways to Secure Your Service Desk Against AI-Enabled Attacks", publisher: Petri (author from Specops), type: vendor, url: "https://petri.com/5-ways-to-secure-your-service-desk-against-ai-attacks/", date: 2026-09-01, access: full, locator: "opening and 'Stop using knowledge as proof of identity'" }
    - { ref: OKTA-TI-INVARIANTS-2026, title: "New speed, same tricks: Defend against AI threats with security fundamentals", publisher: Okta Threat Intelligence, type: vendor, url: "https://www.okta.com/newsroom/articles/new-speed-same-tricks-defend-against-ai-threats-with-security-fundamentals/", date: 2026-10-07, access: full, locator: "'We put phishing resistance to the test' and 'How the security invariants performed'" }
    - { ref: OKTA-TI-MFADOWNGRADE-2026, title: "When enrollment isn't enough: How attackers trick users into MFA downgrades", publisher: Okta Threat Intelligence, type: vendor, url: "https://www.okta.com/blog/threat-intelligence/when_enrollment_isnt_enough/", date: 2026-10-05, access: full, locator: "'Executive summary' and 'Threat analysis'" }
    - { ref: VECTRA-SPIDER-2026, title: "The FBI wrote down the Scattered Spider playbook, and it starts with a phone call", publisher: Vectra AI, type: vendor, url: "https://www.vectra.ai/blog/the-fbi-wrote-down-the-scattered-spider-playbook-and-it-starts-with-a-phone-call", date: 2026-07-06, access: full, locator: "section 'The attack, in the order it happened'" }
    - { ref: NAMETAG-IMPERSONATION-2026, title: "Rebuilding Trust in the Age of AI: The 2026 Workforce Impersonation Report", publisher: Nametag, type: vendor, url: "https://www.go.nametag.co/hubfs/The%202026%20Workforce%20Impersonation%20Report.pdf", date: 2026, access: full, locator: "p.6 'Helpdesk Social Engineering'" }
    - { ref: GARTNER-IAMSUMMIT-2026, title: "Gartner Identity & Access Management Summit 2026 agenda and FAQ", publisher: Gartner, type: conference, url: "https://www.gartner.com/en/conferences/na/identity-access-management-us/agenda", date: 2026-10-17, access: full, locator: "FAQ list on access management ('Secure service desk authentication and recovery processes'); page retrieved 2026-10-17, event starts 2026-12-07" }
  last_reviewed: 2026-10-17
  notes: "This entry is about defending identity assurance against AI-enabled impersonation, not about an AI tool replacing staff. The Vectra account describes an unproven allegation in a federal complaint (it says so) and the FBI complaint did not involve cloned voices as far as the post states. Okta's 88% and 99.75% figures are 'could have' estimates and the post gates part of its content behind a form. Both Specops-authored articles promote its own Secure Service Desk product. Search-only: a Deepwatch note that voice-phishing SSO resets surged, and an FS-ISAC Scattered Spider guidance PDF dated 2023-11."

- id: security-identity-access-09
  title: Context-aware just-in-time and zero-standing-privilege access across all identities
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [software-systems, transaction-processing]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Standing privilege, permissions that sit dormant and access reviewed on a schedule leave a compromised identity with whatever it holds. Palo Alto Networks argues privilege now reaches far beyond administrators and that attackers can use identity paths faster than reviews cycle."
  solution: "Palo Alto Networks describes three levels: vaulted persistent access, just-in-time access, and zero standing privileges where its platform 'analyzes live context and risk' and grants short-lived, task-scoped access that expires when the task ends. It says traditional PAM, JIT and ZSP can run in parallel so teams can move gradually."
  outcomes:
    - lever: risk
      description: "none published for the control; the post cites survey context only."
      figure: "83% of organizations reported two or more identity-related breaches last year (as stated in the post)"
      measures: "Share of surveyed organizations reporting two or more identity-related breaches in the prior year, as stated by Palo Alto Networks without citing the survey in the passage read; this measures the problem"
      provenance: vendor-published
      source_ref: PANW-DYNPRIV-2026
  prerequisites:
    - "Discovery of identities, entitlements and access paths first (the post is part 3 of a series after discovery) (PANW-DYNPRIV-2026, opening paragraphs)."
  risks_and_guardrails:
    - "Palo Alto Networks says moving to Level 3 cannot happen overnight and does not replace all controls at once; vaulting stays for root, built-in and break-glass accounts (PANW-DYNPRIV-2026, 'Modernize Control Without Abandoning Vaulting')."
  human_checkpoints:
    - "For autonomous agents the post says control cannot depend on a person reviewing every action; for human requests the approval step is not described in the passages read."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: PANW-DYNPRIV-2026, title: "Dynamic Privilege Control Beyond Login", publisher: Palo Alto Networks (Idira blog), type: vendor, url: "https://www.paloaltonetworks.com/blog/identity-security/dynamic-privilege-control-moment-of-action/", date: 2026-09-23, access: full, locator: "sections 'Static Controls Leave Privilege Exposed', 'Modernize Control Without Abandoning Vaulting'" }
    - { ref: PANW-MODERNPAM-2026, title: "Modern Privileged Access Management (PAM)", publisher: Palo Alto Networks (Idira blog), type: vendor, url: "https://www.paloaltonetworks.com/blog/identity-security/modern-privileged-access-management/", date: 2026-08-17, access: full, locator: "sections 'What Is Modern PAM?' and 'Privilege Is Defined by the Action, Not the Account'" }
  last_reviewed: 2026-10-17
  notes: "Marketing content from the vendor that completed the CyberArk acquisition (Forrester reports the USD 25 billion deal in FORRESTER-RSAC-2026). The AI element (live risk analysis) is the vendor's description of its own product. A 2026-07 1Password launch (auto-approve lower-risk requests, route higher-risk to reviewers) was seen only in search results and is described there as rule-based routing; not used."

- id: security-identity-access-10
  title: Natural-language authoring and troubleshooting of joiner-mover-leaver workflows
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [software-systems]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: "Identity administrators spend time configuring custom lifecycle workflows for joiners, movers and leavers and diagnosing workflow processing results."
  solution: "Microsoft documents Security Copilot in Entra ID Governance for creating step-by-step guidance for a new lifecycle workflow from a prompt, exploring configurations, analyzing the active workflow list, troubleshooting processing results and comparing versions of a workflow."
  outcomes:
    - lever: capacity
      description: "Microsoft says it saves administrators time and effort; no figure is published."
      figure: "none published"
      measures: "n/a"
      provenance: vendor-published
      source_ref: MS-ENTRA-LIFECYCLE-2025
  prerequisites:
    - "Entra ID Governance license, Security Copilot enabled and the Lifecycle Workflow Administrator role (MS-ENTRA-LIFECYCLE-2025, 'Prerequisites')."
  risks_and_guardrails:
    - "If an action is blocked by insufficient permissions the tool shows a recommended role; activation depends on an eligible role assignment (MS-ENTRA-LIFECYCLE-2025, note after 'Launch Security Copilot')."
  human_checkpoints:
    - "The administrator creates and enables the workflow; the assistant gives guidance."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: MS-ENTRA-LIFECYCLE-2025, title: "Manage employee lifecycle using Microsoft Security Copilot", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/entra/security-copilot/entra-lifecycle-workflows", date: 2025-09-23, access: full, locator: "opening paragraph and use-case list; date is the page's ms.date" }
  last_reviewed: 2026-10-17

- id: security-identity-access-11
  title: Employee-facing orchestrating agent for IT and people support, including access questions
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [client-interaction, transaction-processing]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Employees do not know which of roughly 1,500 applications to ask for what, and building a separate agent per workflow would produce tens of thousands of agents (Okta's description)."
  solution: "Okta built an orchestrating agent, Dex, on its own Okta One platform for IT, people, travel and expense support. For a new hire, Dex is meant to answer benefits questions, route access requests and handle device and VPN questions through one front door."
  outcomes:
    - lever: experience
      description: "Early adoption figures, not decision quality."
      figure: "25% employee adoption in two weeks; over 23,500 interactions to date"
      measures: "Share of Okta employees using Dex within two weeks of launch (denominator is Okta's workforce, not stated); count of interactions Dex has fielded to the post date"
      provenance: self-reported
      source_ref: OKTA-DEX-2026
  prerequisites:
    - "An orchestration layer and identity-governed access for the agents; Okta says it deployed its own products first ('customer zero')."
  risks_and_guardrails:
    - "The author warns that rushing AI without a foundation leads to fragmented systems, security risks and spiraling costs (OKTA-DEX-2026, opening)."
  human_checkpoints:
    - "Not described in the passage read."
  role_evolution: "IT risks becoming 'the Department of No' if it blocks AI; the author describes a customer-zero posture (OKTA-DEX-2026, opening)."
  evidence_grade: B
  sources:
    - { ref: OKTA-DEX-2026, title: "Lessons learned from securing our digital workforce", publisher: Okta, type: vendor, url: "https://www.okta.com/newsroom/articles/lessons-from-securing-our-digital-workforce/", date: 2026-09-17, access: full, locator: "'Lesson 1: Avoid death by a thousand agents'" }
  last_reviewed: 2026-10-17
  notes: "Grade B and not A: a named deployment with adoption counts but no quality, error or security measure. The process (IT and people support) is adjacent to IAM controls, which also caps the grade at B; it overlaps with a technology/IT service-desk module. Only the first lesson was read in detail."

- id: security-identity-access-12
  title: AI attack-chain simulation to test identity detection and response speed
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: delegate
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: "Detection and response were built on assumptions about human attackers: sequential steps, limited headcount, memory, fatigue and recognizable tools. Silverfort says AI agents break most of them."
  solution: "Silverfort built a model- and tool-agnostic AI attack simulator, run in a contained lab, with five to 10 agents working different phases in parallel and sharing findings in a common memory. It uses the results to describe what defenders should expect."
  outcomes:
    - lever: speed
      description: "Lab measurements of attacker speed and cost, useful for testing defenses; the vendor says treat them as patterns, not benchmarks."
      figure: "full chain to domain takeover in four to five minutes; a full run cost about USD 12, falling to about USD 4; a failed run that kept iterating cost USD 25"
      measures: "Silverfort's simulator runs in its own lab: time for the agent swarm to go from initial credentials to domain takeover; equivalent cost per run. Number of runs not stated."
      provenance: vendor-published
      source_ref: SILVERFORT-ASSUMPTIONS-2026
  prerequisites:
    - "A contained lab and identity-attack expertise; the post is from research, incident-response and product staff."
  risks_and_guardrails:
    - "Silverfort says the lab is cleaner than most production networks, so results are patterns and not benchmarks (SILVERFORT-ASSUMPTIONS-2026, 'How we tested')."
  human_checkpoints:
    - "Not described."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: SILVERFORT-ASSUMPTIONS-2026, title: "5 cybersecurity assumptions AI attacks break", publisher: Silverfort, type: vendor, url: "https://www.silverfort.com/blog/5-cybersecurity-assumptions-ai-attacks-break/", date: 2026-10-13, access: full, locator: "'How we tested how AI attackers work' and Assumptions 1-4" }
  last_reviewed: 2026-10-17
  notes: "Pattern is `other`: parallel multi-agent adversary simulation used as a defensive test. Describes attacker capability only at the level defenders need; no technique detail recorded. Strictly this is security testing (see Routed: vulnerability-exposure/ai-security). The post's sentence that one assumption holds and 'is where defenders get their advantage back' was in the part I did not fully read."

- id: security-identity-access-13
  title: Agentic threat hunting and detection engineering for identity-targeting browser attacks
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [research-synthesis, software-systems]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Attack techniques against identities (AiTM phishing kits, device-code phishing, OAuth abuse, ClickFix and similar) change weekly or daily and indicators are cheap to rotate, so human-only detection engineering takes days or weeks per technique."
  solution: "Push Security built a pipeline in which agents ingest new research, form hunt hypotheses, write and test queries against stored browser-session metadata, triage matches, run deeper analysis with a researcher's toolkit, and draft detections that researchers ship. Hunts are for techniques, not indicators."
  outcomes:
    - lever: capacity
      description: "Detection output after adopting the pipeline."
      figure: "tripled the number of new detections shipped each month; 'already this year' tripled the cumulative number of detections shipped to customers; one hunt turned 12 meaningful results from trillions of browser events, one of them novel"
      measures: "Push's own count of detections shipped to customers (monthly and cumulative); hunt results are counts from Push's install base. Baseline period and quality of the extra detections are not stated."
      provenance: self-reported
      source_ref: PUSH-AGENTICHUNT-2026
  prerequisites:
    - "Rich first-party telemetry; Push says its extension records browser-session metadata locally and queries it only during hunts, and that it does not train models on customer data."
    - "Researcher-curated context: 'Agents are only as good as the context you give them' (PUSH-AGENTICHUNT-2026, section 'Core principles')."
  risks_and_guardrails:
    - "Queries are refined to reduce false positives and back-tested on stored data before becoming scheduled detections (PUSH-AGENTICHUNT-2026, 'Example 1' and 'Example 2')."
  human_checkpoints:
    - "Researchers ship the detection; in the human-initiated hunt, researchers and agents formulate the query together (PUSH-AGENTICHUNT-2026, 'Example 2')."
  role_evolution: "Push says the goal is to scale a seasoned hunter's expertise and not to replace researchers (PUSH-AGENTICHUNT-2026, opening)."
  evidence_grade: B
  sources:
    - { ref: PUSH-AGENTICHUNT-2026, title: "Can AI replace a threat researcher? What we learned building an agentic threat hunting pipeline", publisher: Push Security, type: vendor, url: "https://pushsecurity.com/blog/can-ai-replace-a-threat-researcher-what-we-learned-building-an-agentic-threat-hunting-pipeline", date: 2026-05-12, access: full, locator: "opening, 'Core principles for agentic threat hunting', 'Example 1', 'Example 2'" }
    - { ref: PUSH-SHINYHUNTERS-2026, title: "How three techniques are behind ShinyHunters' 2026 campaigns", publisher: Push Security, type: vendor, url: "https://pushsecurity.com/blog/analyzing-the-instructure-breach", date: 2026-05-08, access: full, locator: "section on the three browser-based vectors" }
  last_reviewed: 2026-10-17
  notes: "Grade B and not A: the output measure is a count of detections without a quality measure, and the process (detection engineering for a browser security product) is adjacent to identity operations; it overlaps with the operations and threat-intelligence modules. The 37x rise in device-code phishing across Push's install base is the vendor's own measurement of the threat, quoted in the same post."

- id: security-identity-access-14
  title: AI reviewer for access requests that applies policy and escalates risky or ambiguous cases
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [transaction-processing, expert-judgment]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "Someone requests a role and a person should weigh who they are, what they already hold, how risky the request is and whether permanent access is warranted. Opal says most teams lack the time or context, so approval becomes the default."
  solution: "Opal's agent, Paladin, reads the request, gathers context from connected applications (policy documents, tickets, incident tools, device posture, an approvals channel), reasons against the customer's policy and returns a decision with a plain-language rationale. It can run as an advisor or, as trust grows, handle routine policy-conforming requests and escalate the rest."
  outcomes:
    - lever: speed
      description: "Baseline from the vendor's own platform; no result for Paladin is published."
      figure: "median approval time 15 minutes, over 24 hours at some enterprises; 43.5% of granted access unused for more than 90 days"
      measures: "Across about half a million access requests on the Opal platform in the prior year: median approval time; share of granted access unused for more than 90 days"
      provenance: vendor-published
      source_ref: OPAL-PALADIN-2026
  prerequisites:
    - "Connected data sources and a curated policy; Opal says customers choose what the agent reads (OPAL-PALADIN-2026, 'The context it reasons with')."
  risks_and_guardrails:
    - "Authority is graduated and the agent acts only within the role granted; every recommendation and decision is logged with its reasoning (OPAL-PALADIN-2026, 'Automate the routine, escalate the rest')."
  human_checkpoints:
    - "Risky, unusual or ambiguous requests go to a human; the customer decides where the line sits."
  role_evolution: "Opal says careful review does not scale by adding headcount and that routine work should stop consuming reviewers (OPAL-PALADIN-2026, 'The bigger picture')."
  evidence_grade: C
  sources:
    - { ref: OPAL-PALADIN-2026, title: "Paladin: AI that applies your policy to every request", publisher: Opal Security, type: vendor, url: "https://www.opal.dev/blog/paladin-policy-ai", date: 2026-08-06, access: full, locator: "sections 'Approval becomes the default', 'Meet Paladin', 'Automate the routine, escalate the rest'" }
  last_reviewed: 2026-10-17
  notes: "The Opal blog index lists posts saying Paladin reached general availability and a self-hosted option; I saw only titles, so the maturity stays 'announced'. The same post reports that non-human and agent identities on the platform grew 2,300% with 90% of that access unreviewed (routed to ai-security)."

- id: security-identity-access-15
  title: Spoofing-aware speaker verification using audio language models (idea)
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Text-to-speech and voice cloning make spoofing of voice authentication inexpensive and scalable, threatening automatic speaker verification."
  solution: "A July 2026 preprint evaluates large audio language models for spoofing-aware speaker verification under zero-shot prompting, supervised adaptation, reasoning-oriented training and reinforcement learning, noting the models can give natural-language rationales for auditing."
  outcomes:
    - lever: risk
      description: "none published for production use. The preprint finds pretrained models near chance zero-shot and competitive after task-specific adaptation."
      figure: "none published"
      measures: "n/a"
      provenance: independent
      source_ref: ARXIV-2607.14753
  prerequisites:
    - "Task-specific adaptation of the model (ARXIV-2607.14753, abstract)."
  risks_and_guardrails:
    - "The abstract says conventional cascade systems still lead in some settings."
  human_checkpoints:
    - "Not described."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: ARXIV-2607.14753, title: "Large Audio Language Models for Spoofing-Aware Speaker Verification", publisher: arXiv (preprint, not peer reviewed), type: academic, url: "https://arxiv.org/abs/2607.14753", date: 2026-07-16, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: "Idea: a research direction, not a deployment. Practitioners writing about the service desk advise removing voice and video judgment from the decision altogether (see security-identity-access-08)."

- id: security-identity-access-16
  title: LLM-synthesized access-control policies from natural-language requirements (idea)
  archetype: security
  module: identity-access
  function: technology-it
  work_types: [software-systems]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Manually written access-control policies in cloud policy languages become complex and error prone."
  solution: "A March 2025 preprint tests zero-shot prompting of language models to produce well-formed AWS-style access-control policies from either a concrete allow/deny request list or a natural-language description, and reports preliminary results that structured, syntax-based prompts are needed."
  outcomes:
    - lever: quality
      description: "none published for production use; the paper reports preliminary experimental results only."
      figure: "none published"
      measures: "n/a"
      provenance: independent
      source_ref: ARXIV-2503.11573
  prerequisites:
    - "Structured prompts based on the policy-language syntax (ARXIV-2503.11573, abstract)."
  risks_and_guardrails:
    - "The abstract motivates the work by error-prone manual policies; it does not discuss deployment guardrails."
  human_checkpoints:
    - "Not described."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: ARXIV-2503.11573, title: "Synthesizing Access Control Policies using Large Language Models", publisher: arXiv (preprint, not peer reviewed), type: academic, url: "https://arxiv.org/abs/2503.11573", date: 2025-03-14, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: "Idea: published slightly more than 18 months before the research date, kept as a foundation. Cloud IAM policy authoring overlaps with the cloud-infrastructure module. Gartner's 2026 IAM Summit lists runtime authorization and policy-based access control sessions (GARTNER-IAMSUMMIT-2026), which shows practitioner interest but not this specific use."
```

## 3. Module notes

### Processes and key steps (with work types)

- **Joiner-mover-leaver and lifecycle workflows:** provision, change and remove access from HR events (`transaction-processing`, `software-systems`). Discourse: Microsoft's Copilot-assisted workflow authoring (MS-ENTRA-LIFECYCLE-2025); NHIMG's summary says HR and IAM misalignment breaks identity automation (a headline in NHIMG's "Governance & Risk" list, title only).
- **Access request and approval:** weigh requester, existing access, sensitivity and justification (`transaction-processing`, `expert-judgment`). Discourse: Opal's baseline of 15-minute median approvals and 43.5% of granted access unused for over 90 days (OPAL-PALADIN-2026, "Approval becomes the default").
- **Access certification and role engineering:** periodic review, revoke excess, design roles (`review-assurance`, `expert-judgment`). Discourse centres on rubber-stamping and reviewer context (SAILPOINT-RECS-2022; OPAL-REVIEWS-2026).
- **Authentication and policy configuration:** MFA, passkeys, Conditional Access, session controls (`software-systems`). Discourse: Microsoft making passkeys the default in Entra from 2026-09-01 and retiring SMS and voice on 2027-02-01 (FORRESTER-MSPASSKEY-2026); policy-gap agents (MS-CAAGENT-2026).
- **Privileged access:** vaulting, just-in-time elevation, zero standing privilege, session monitoring (`software-systems`, `review-assurance`). Discourse: "every identity is privileged" and context-aware JIT (PANW-MODERNPAM-2026; PANW-DYNPRIV-2026).
- **Identity threat detection and response:** detect, contain, recover credentials and sessions (`transaction-processing`; pattern `monitor-diagnose-act`). Discourse: detect-to-contain gap (SANS-ITDR-2026) and closed-loop response (NETWRIX-ITDR-2026; PANW-IDSECOPS-2026).
- **Identity verification, onboarding, service desk and account recovery:** prove a person is who they claim (`transaction-processing`, `client-interaction`). Discourse: enforced verification and deepfake resistance (INFOSEC-SERVICEDESK-2026; NAMETAG-IMPERSONATION-2026; NIST-80063-2025).
- **Identity-related fraud (account takeover, impersonation, synthetic identity):** (`transaction-processing`, `data-reporting`). Discourse: behavioral biometrics and injection-attack defense (FORRESTER-BIOCATCH-2026; CFI-ENTRUST-2025). The landscape file says fraud is often run outside the CISO organization, which matches how thin the practitioner discourse is.

### Common pain points

- **Service desk and recovery are the weak link:** an FBI complaint describes a May 2025 intrusion where help-desk calls led to three compromised accounts, two of them IT administrators, in about two to three hours with no exploit (VECTRA-SPIDER-2026, "The attack, in the order it happened"; the account is an allegation). Okta says attackers target the weakest available factor, so strong factors do not help if a phishable fallback exists (OKTA-TI-MFADOWNGRADE-2026, "Executive summary").
- **Reviewer fatigue and missing context in certification** (SAILPOINT-RECS-2022; NHIMG-OMADA-2026, key questions).
- **Containment lags detection** (SANS-ITDR-2026, "Key Findings").
- **Impersonation of IT itself:** Petri's author cites Microsoft's April warning that attackers impersonated helpdesk staff over Teams to get employees to grant remote access, and a Mandiant red-team exercise using a cloned voice (PETRI-SERVICEDESK-2026, points 3 and 4).
- **Authentication friction and legacy defaults:** Okta and Yubico's survey says 52% received username-and-password credentials on day one, 76% use fragmented authentication methods across internal applications, and 43% of security professionals still rely on passwords to log in to work (OKTA-YUBICO-2026, "Legacy habits start on day one").
- **Third-party and recovery gaps:** per Help Net Security's summary of the 2026 DBIR, only 23% of third-party organizations fully remediated their MFA issues (HNS-DBIR-2026, paragraph on third-party involvement).
- **Phishing and vishing outpacing training:** in the Okta/Yubico test only 36% of respondents correctly identified the human-written message (OKTA-YUBICO-2026, "Why the human firewall cannot stop AI").

### Metrics and benchmarks (with sources)

| Metric | Value | What it measures (source's words, condensed) | Provenance | Ref and locator |
|---|---|---|---|---|
| Detect vs contain identity attacks | 68% vs 55% | Organizations that detect identity attacks within 24 hours vs contain them in that window | independent (sponsored survey) | SANS-ITDR-2026, Key Findings |
| ITDR tools vs identity breach | 85% deployed; 55% breached | Organizations reporting active ITDR tool use; organizations with at least one identity-related compromise in the past 12 months | independent (sponsored survey) | SANS-ITDR-2026, FAQs (page headline conflicts; see use case 05 notes) |
| Identity attack types | credential phishing 35%; compromised browsers 27%; MFA fatigue 26%; token hijacking 23% | Share of identity attacks by technique, as the SANS page states | independent (sponsored survey) | SANS-ITDR-2026, FAQs |
| Non-human credential rotation | 8% | Organizations that rotate more than 75% of non-human-identity credentials every 90 days | independent (sponsored survey) | SANS-ITDR-2026, FAQs |
| Account takeover prevented (counterfactual) | 88%; 99.75% | Share of ~6,000 analyzed social-engineering events where takeover would have been stopped by mandatory phishing-resistant enrollment; plus app sign-in enforcement | vendor-published | OKTA-TI-INVARIANTS-2026 |
| Factors in account-takeover sessions | password 87%; push 58%; app OTP 36%; SMS OTP 22% | Share of the analyzed takeover sessions that satisfied each factor | vendor-published | OKTA-TI-INVARIANTS-2026 |
| AI-driven attack and impersonation exposure | 44% successful AI-driven attack; 43% suspicious video, voice or phone impersonation | Share of ~2,000 surveyed technology and security professionals (nine countries) whose organization suffered each in the past year | vendor-published (Yubico/Okta) | OKTA-YUBICO-2026 |
| Biometric fraud with deepfakes | one in five attempts; selfie deepfakes +58%; injection attacks +40% YoY | See use case 07 | vendor-published | CFI-ENTRUST-2025 |
| Access request latency and unused access | 15-minute median; 43.5% unused over 90 days | About half a million requests on one vendor's platform | vendor-published | OPAL-PALADIN-2026 |
| Identity-related breaches | 9 in 10 organizations | Organizations reporting a successful identity-related breach in the last 12 months (2,930 leaders surveyed) | vendor-published | PANW-LANDSCAPE-2026 |
| Machine-to-human identity ratio | 109:1 | Average machine identities per human in the same survey | vendor-published | PANW-LANDSCAPE-2026 |
| Over-privileged human access | 96% | Respondents saying human identities have access far beyond what roles require | vendor-published | PANW-LANDSCAPE-2026 |
| Credential theft as top entry point | first time not #1 in the 19-year DBIR history | Vulnerability exploitation overtook stolen credentials as most common initial access vector (2026 DBIR) | independent | HNS-DBIR-2026 |

Quality evidence: **there is none for AI in human IAM operations.** No source gave an override rate, false-negative or false-approval rate, parallel-run result or inspection finding for AI-guided reviews, Conditional Access agents, risky-user summaries, access-request agents or ITDR automation. The measurements found describe threats, baselines or counterfactuals. Search-only figures (DBIR credential abuse at 13% of breaches as initial access and 39% overall; Entrust press-release numbers; vendor claims of 65-70% review-time cuts) were not opened in a primary document and are not used.

### Guardrails and regulatory points

- **NIST SP 800-63-4** (final July 2025) adds recommended continuous-evaluation metrics, expanded fraud requirements for identity proofing, controls for injection attacks and forged media, and integrates syncable authenticators (NIST-80063-2025, "Background").
- **FinCEN FIN-2024-Alert004** (2024-11-13) asks institutions to cite the key term "FIN-2024-DEEPFAKEFRAUD" in suspicious activity reports and lists red flags such as inconsistencies among submitted identity documents (FINCEN-DEEPFAKE-2024, p.1 and red-flag list).
- **CISA/NIST IR 8587** (2026-09-09) gives recommendations to agencies and cloud providers to protect identity tokens and assertions from forgery, theft and misuse, building on SP 800-53 control IA-13 (CISA-NIST-IR8587-2026).
- **Authentication baseline moves:** Microsoft Entra passkeys default from 2026-09-01 and SMS and voice retirement on 2027-02-01 (FORRESTER-MSPASSKEY-2026). A UK Cyber Essentials April 2026 update requiring MFA on all cloud services appears in a Push Security post title only (not opened; not relied on).
- **Human accountability for AI decisions:** vendors describing AI-guided reviews all keep a human signer for risky items and log reasoning (OPAL-REVIEWS-2026; SAILPOINT-RECS-2022). No regulator statement on AI-made access decisions was found.
- The landscape file lists EU AI Act and NIS2/DORA status (EC-AIACT-2026 and others); I did not find sources linking them specifically to IAM decisions, so I make no claim.

### Frontier signals (dated)

- 2026-03-31: Forrester says traditional cybersecurity vendors are "finally getting serious about identity security", citing Palo Alto Networks buying CyberArk for USD 25 billion, while warning that "identity is the new perimeter" is not new (FORRESTER-RSAC-2026).
- 2026-05-22: KuppingerCole's EIC 2026 wrap-up says the conference covered AI-driven identity, agentic AI and modern authorization, and quotes Martin Kuppinger on identity as the foundation of trust in autonomous systems (KC-EIC-2026).
- 2026-06-12 / 2026-06-25: independent and Forrester recaps of Identiverse (June 15-18) report passkeys moving to operational questions (recovery, enrollment), deepfakes versus identity verification, and session security and ITDR as large topics; Ping's CEO framed a move to "actions, not access" (SWI-IDENTIVERSE-2026; FORRESTER-IDENTIVERSE-2026). SC Media's CyberRisk TV opener lists AI agents, machine identities, shadow AI, deepfake-driven attacks and account takeovers, and "gaps in tools, processes, and operational support" among the themes (SC-IDV26-2026, key moments). Identiverse added a Washington DC event for 2026-11-09 to 10 on fraud, AI, regulation and trust (SWI-IDVPROFILE-2026; IDENTIVERSE-AGENDA-2026).
- 2026-03-23: the Identity at the Center podcast's Q1 2026 threat-report roundup reportedly covers AI-driven attack speed, deepfakes, stalled enterprise passkey adoption and zero standing privilege (IDAC-409-2026, search-only description).
- 2026-06-15 and 2026-08-06: Opal announces AI-guided reviews and an AI access-request reviewer, with role mining and policy suggestions as the stated next steps (OPAL-REVIEWS-2026; OPAL-PALADIN-2026).
- 2026-08-05: Visa announces intent to acquire BioCatch for USD 2.4 billion; Forrester calls it effectively the end of the standalone behavioral-biometrics market (FORRESTER-BIOCATCH-2026).
- 2026-08-06: Black Hat recap highlights two independent attacks on passkey implementations (cleartext storage, synced-passkey key extraction) that do not break the cryptography (SWI-BLACKHAT-2026).
- 2026-10-05 to 2026-10-07: Okta Threat Intelligence argues AI accelerates known tricks; policy enforcement is the defence (OKTA-TI-MFADOWNGRADE-2026; OKTA-TI-INVARIANTS-2026).
- Upcoming: FIDO Authenticate U.S. 2026 (2026-10-19 to 21) with a theme that includes "agentic authentication that ensures verified humans stand behind every AI agent" (FIDO-AUTH-2026); Identiverse in Washington DC (2026-11-09 to 10) on "Fraud, AI, Regulation, and Market Confidence"; Microsoft Ignite (2026-11-17 to 20) (MS-ENTRA-WHATSNEW-OCT-2026); Gartner IAM Summit from 2026-12-07 with an AI track and sessions on AI-enhanced IGA, deepfake-resistant identity verification, AI-powered IAM automation and secure service-desk authentication (GARTNER-IAMSUMMIT-2026); Identiverse 2027 on 2027-06-28 to 07-01; and RSAC 2027, which the landscape file says lists an "RSAC Cyber Fraud Day" (landscape file, RSAC-USA-2027).

### Workforce and role effects

- Forrester's RSAC read: vendors are still hiring early-career practitioners but in fewer numbers, worry mid- and senior staff will not embrace AI, and have no answer to the "five-year problem" (FORRESTER-RSAC-2026, "Staffing shortages have been eclipsed").
- Service-desk staff: move from judging callers to executing an enforced verification workflow (INFOSEC-SERVICEDESK-2026).
- Reviewers and approvers: attention is meant to concentrate on high-risk grants while routine grants are cleared or auto-approved; the vendors say this, no independent source tests it (OPAL-REVIEWS-2026; OPAL-PALADIN-2026).
- Identity and security operations teams: Palo Alto Networks argues for one operating loop; Forrester notes that IAM for humans and deterministic machines is already an organizational challenge before agents are added (PANW-IDSECOPS-2026; FORRESTER-IDENTIVERSE-2026).
- No hard data on identity-team headcount or skills was found.

### Objections and concerns practitioners raise

- **Hype and sameness:** Forrester says agentic AI was pasted into messages that "could have been from 2023, 2018, or ... 2006" (FORRESTER-RSAC-2026); a vendor session title at the Gartner IAM Summit asks whether AI will solve IAM challenges and answers "Think Again" (search-only; the page was blocked).
- **AI as accelerant, not catalyst:** Okta says threat actors use AI to scale known methods such as phishing and that security fundamentals matter more (OKTA-TI-INVARIANTS-2026, opening).
- **Detector decay and arms race** (HN-REALITYDEFENDER-2025; ARXIV-2609.09489).
- **Behavioral-biometric false positives and evasion** (FORRESTER-BIOCATCH-2026).
- **Automation lockouts and noisy rules** (NETWRIX-ITDR-2026).
- **Auto-approval accountability:** NHIMG's summaries repeat that recommendation quality and accountability are separate controls (NHIMG-SAILPOINT-2026, key questions).
- **Passkey implementation and recovery risk:** Black Hat attacks target implementations (SWI-BLACKHAT-2026); recovery and enrollment are where Scattered Spider strikes (SWI-IDENTIVERSE-2026, item 2). A separate consumer-facing debate asks whether passkeys are a trap (NONFUNCTIONAL-PASSKEYS-2026, 2026-10-10, which drew 1,142 points and 576 comments on Hacker News); Scott Helme rebuts its central attestation claim, saying synced passkeys give sites no attestation statement (SCOTTHELME-PASSKEYS-2026). This is adjacent to the AI theme.
- **Identity-provider-level flaws that policy cannot mitigate:** a researcher's 2025-09-17 post shows undocumented Entra "Actor tokens" were not subject to Conditional Access (DIRKJANM-ACTORTOKENS-2025, opening); Risky Business covered it on 2025-09-24 (RISKY-808-2025). Not an AI issue, but practitioners cite token-level risk as why session protection matters.
- **Cost and licensing of AI features:** the Conditional Access agent needs provisioned compute units billed monthly even if unused (MS-CAAGENT-2026, "Prerequisites").

### Interview probes for an advisor

1. When someone calls the service desk to reset MFA or recover an account, what decides the outcome: the agent's judgment, or an enforced verification step? What proportion of resets can you prove were verified?
2. In your last access certification, what share of items were approved unchanged, and how do you know reviewers had enough context? Would you let a model auto-approve low-risk items, and who owns the mistake?
3. Between detecting an identity attack and containing it, how long does it take today, and which response actions may run without a human?
4. Where do onboarding, step-up and recovery depend on a selfie, voice or video check, and has anyone tested them against injection or deepfake attacks?
5. Who owns the seam between the identity team and the SOC, and does entitlement data reach detection (and detection reach identity response) without a ticket?

## 4. Routed to other modules

- **ai-security (identities for AI agents):** Forrester's Identiverse and Oktane recaps (FORRESTER-IDENTIVERSE-2026; FORRESTER-OKTANE-2026: Okta's Blueprint Alliance, Cross App Access, SPIFFE gaps, "know-your-agent"); SANS's finding that 73% of organizations use agentic AI or automations that need credentials but no single governance control exceeds 40% (SANS-ITDR-2026); Palo Alto Networks' 109:1 machine-to-human ratio and 85% expected agent growth (PANW-LANDSCAPE-2026); Okta/Yubico on agent identity verification (91% essential, 57% critical) (OKTA-YUBICO-2026); Opal's 2,300% growth in agent and non-human identities (OPAL-PALADIN-2026); Gartner IAM Summit AI-agent tracks (GARTNER-IAMSUMMIT-2026); Black Hat agent identity launches (SWI-BLACKHAT-2026); Forrester on Anthropic's and OpenAI's own identity verification and hardware-passkey requirements for access to AI models (FORRESTER-CLAUDEIDV-2026; FORRESTER-OPENAIPASSKEY-2026); Microsoft's "Secure AI" framing and Agent ID (MS-ENTRA-WHATSNEW-OCT-2026).
- **human-risk:** AI-native insider-risk investigations correlating identity, application and data-movement behavior (Above Security, backed by the CrowdStrike Falcon Fund) (SWI-BLACKHAT-2026, item 4); North Korean IT-worker hiring fraud and video-call verification limits (NAMETAG-IMPERSONATION-2026, pp.9, 13); the finding that staff cannot reliably tell AI-written messages from human ones (OKTA-YUBICO-2026).
- **security-operations:** Push's browser-layer detection of phishing, ClickFix and device-code attacks (PUSH-PYRAMID-2026; PUSH-SHINYHUNTERS-2026); Blackpoint's identity-focused AI SOC agent (search-only).
- **vulnerability-exposure:** the 2026 DBIR finding that vulnerability exploitation overtook stolen credentials as the leading initial access vector, and median full-patch time of 43 days (HNS-DBIR-2026).
- **cloud-infrastructure:** Entra tenant-level token weakness (DIRKJANM-ACTORTOKENS-2025); LLM policy synthesis for cloud IAM (ARXIV-2503.11573).
- **incident-response:** details of the Scattered Spider help-desk intrusion timeline and recovery (VECTRA-SPIDER-2026).
- **security-governance-risk:** non-human credential rotation at 8% as a control gap (SANS-ITDR-2026).

## 5. Sources

Type counts are at the end of this section. "Access: full" means I opened and read the page or file; "search-only" means I saw it only in search results.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| FORRESTER-RSAC-2026 | RSAC 2026: An AI Coming-Of-Age Story Without The Romance | Forrester | firm | https://www.forrester.com/blogs/rsac-2026-an-ai-coming-of-age-story-without-the-romance | 2026-03-31 | full |
| FORRESTER-IDENTIVERSE-2026 | Identiverse 2026 Recap: Identity Security For Agentic AI Dominates | Forrester | firm | https://www.forrester.com/blogs/identiverse-2026-recap-identity-security-for-agentic-ai-dominates/ | 2026-06-25 | full |
| FORRESTER-OKTANE-2026 | Oktane 2026 Recap: Okta Announces A Unified IAM Control Plane, With Agent Governance And Identity Details Remaining Unclear | Forrester | firm | https://www.forrester.com/blogs/oktane-2026-recap-okta-announces-a-unified-iam-control-plane-with-agent-governance-and-identity-details-remaining-unclear/ | 2026-10-01 | full |
| FORRESTER-BIOCATCH-2026 | Visa To Acquire Behavioral Biometrics Specialist BioCatch For $2.4 Billion | Forrester | firm | https://www.forrester.com/blogs/visa-to-acquire-behavioral-biometrics-specialist-biocatch-for-2-4-billion/ | 2026-08-05 | full |
| FORRESTER-MSPASSKEY-2026 | Microsoft Makes Passkeys Default: What Identity And Security Leaders Need To Do | Forrester | firm | https://www.forrester.com/blogs/microsoft-makes-passkeys-default-what-identity-and-security-leaders-need-to-do/ | 2026-07-16 | full |
| FORRESTER-CLAUDEIDV-2026 | Anthropic's Claude Rolls Out End-User Identity Verification | Forrester | firm | https://www.forrester.com/blogs/anthropic-claude-rolls-out-end-user-identity-verification-idv/ | 2026-05-04 | full |
| FORRESTER-OPENAIPASSKEY-2026 | OpenAI Makes Hardware Passkeys Mandatory For Its Highest-End Cyber Model | Forrester | firm | https://www.forrester.com/blogs/openai-makes-hardware-passkeys-mandatory-for-its-highest-end-cyber-model/ | 2026-07-31 | full |
| SWI-IDENTIVERSE-2026 | Identiverse 2026 recap: agentic identity grows up, and passkeys get real | Start with Identity (SWI Community Team) | community | https://startwithidentity.com/blog/identiverse-2026-recap/ | 2026-06-12 | full |
| SWI-BLACKHAT-2026 | Black Hat USA 2026 recap: passkeys get broken (twice), and AI agents get an identity perimeter | Start with Identity (SWI Community Team) | community | https://startwithidentity.com/blog/black-hat-usa-2026-recap/ | 2026-08-06 | full |
| SWI-IDVPROFILE-2026 | Identiverse conference profile and 2026 recap | Start with Identity | community | https://startwithidentity.com/conferences/identiverse.md | 2026-09-30 | full |
| IDENTIVERSE-AGENDA-2026 | Identiverse 2026 and 2027 event page (DC event 2026-11-09 to 10; 2027-06-28 to 07-01) | Identiverse (CyberRisk Alliance) | conference | https://identiverse.com/agenda/ | 2026-10-17 | full |
| KC-EIC-2026 | EIC 2026 Concludes in Berlin: Europe's Leading IAM Conference Explores Digital Trust Through Intelligent Identity | KuppingerCole Analysts | conference | https://www.kuppingercole.com/press-release/eic-2026-wrapped | 2026-05-22 | full |
| GARTNER-IAMSUMMIT-2026 | Gartner Identity & Access Management Summit 2026 agenda and FAQ | Gartner | conference | https://www.gartner.com/en/conferences/na/identity-access-management-us/agenda | 2026-10-17 (retrieved; event starts 2026-12-07) | full |
| FIDO-AUTH-2026 | Authenticate U.S. 2026 event page | FIDO Alliance | conference | https://authenticatecon.com/event/authenticate-u-s-2026/ | 2026-10-17 (retrieved; event 2026-10-19 to 21) | full |
| SC-IDV26-2026 | Identity Security at Identiverse 2026: Navigating AI, Agents, and Emerging Threats - IDV26 #1 | SC Media / CyberRisk TV | podcast | https://www.scworld.com/podcast-segment/15388-identity-security-at-identiverse-2026-navigating-ai-agents-and-emerging-threats-idv26-1 | 2026 (month not shown) | full (show notes via text mirror; no audio) |
| IDAC-409-2026 | Identity at the Center #409: Q1 2026 Identity Threat Report Roundup | Identity at the Center | podcast | https://metacast.app/podcast/identity-at-the-center/gVq3FTis/409-q1-2026-identity-threat-report-roundup/E5A3tlCi | 2026-03-23 | search-only |
| RISKY-808-2025 | Risky Business #808: Insane megabug in Entra left all tenants exposed | Risky Business Media | podcast | https://risky.biz/RB808/ | 2025-09-24 | full (show notes only) |
| SANS-ITDR-2026 | SANS 2026 State of Identity Threat Detection and Response: Key Findings | SANS Institute | survey | https://www.sans.org/research/identity-threat-detection-response-report | 2026-03 | full (landing page; report not read) |
| OKTA-YUBICO-2026 | Survey: How friction, not ignorance, is stalling enterprise security (2026 Global State of Authentication) | Okta (with Yubico) | survey | https://www.okta.com/newsroom/articles/global-state-of-authentication-2026-ai-phishing-resistance/ | 2026-10-07 | full |
| PANW-LANDSCAPE-2026 | 2026 Identity Security Landscape, Chapter One (research excerpt) | Palo Alto Networks (Idira) | survey | https://www.paloaltonetworks.com/idira/identity-security-landscape-report | 2026 (month not shown) | full (excerpt only) |
| OKTA-TI-INVARIANTS-2026 | New speed, same tricks: Defend against AI threats with security fundamentals | Okta Threat Intelligence | vendor | https://www.okta.com/newsroom/articles/new-speed-same-tricks-defend-against-ai-threats-with-security-fundamentals/ | 2026-10-07 | full (partly form-gated) |
| OKTA-TI-MFADOWNGRADE-2026 | When enrollment isn't enough: How attackers trick users into MFA downgrades | Okta Threat Intelligence | vendor | https://www.okta.com/blog/threat-intelligence/when_enrollment_isnt_enough/ | 2026-10-05 | full |
| OKTA-DEX-2026 | Lessons learned from securing our digital workforce | Okta | vendor | https://www.okta.com/newsroom/articles/lessons-from-securing-our-digital-workforce/ | 2026-09-17 | full |
| PANW-IDSECOPS-2026 | IdentitySecOps for AI-Speed Defense | Palo Alto Networks (Idira blog) | vendor | https://www.paloaltonetworks.com/blog/identity-security/identitysecops-closed-loop-model-ai-speed-defense/ | 2026-08-05 | full |
| PANW-MODERNPAM-2026 | Modern Privileged Access Management (PAM) | Palo Alto Networks (Idira blog) | vendor | https://www.paloaltonetworks.com/blog/identity-security/modern-privileged-access-management/ | 2026-08-17 | full |
| PANW-DYNPRIV-2026 | Dynamic Privilege Control Beyond Login | Palo Alto Networks (Idira blog) | vendor | https://www.paloaltonetworks.com/blog/identity-security/dynamic-privilege-control-moment-of-action/ | 2026-09-23 | full |
| SILVERFORT-ASSUMPTIONS-2026 | 5 cybersecurity assumptions AI attacks break | Silverfort | vendor | https://www.silverfort.com/blog/5-cybersecurity-assumptions-ai-attacks-break/ | 2026-10-13 | full |
| PUSH-AGENTICHUNT-2026 | Can AI replace a threat researcher? What we learned building an agentic threat hunting pipeline | Push Security | vendor | https://pushsecurity.com/blog/can-ai-replace-a-threat-researcher-what-we-learned-building-an-agentic-threat-hunting-pipeline | 2026-05-12 | full |
| PUSH-SHINYHUNTERS-2026 | How three techniques are behind ShinyHunters' 2026 campaigns | Push Security | vendor | https://pushsecurity.com/blog/analyzing-the-instructure-breach | 2026-05-08 | full |
| PUSH-PYRAMID-2026 | Using the Pyramid of Pain for threat detection in the AI era | Push Security | vendor | https://pushsecurity.com/blog/the-pyramid-of-pain-in-the-ai-era | 2026-06-01 | full (introduction only) |
| VECTRA-SPIDER-2026 | The FBI wrote down the Scattered Spider playbook, and it starts with a phone call | Vectra AI | vendor | https://www.vectra.ai/blog/the-fbi-wrote-down-the-scattered-spider-playbook-and-it-starts-with-a-phone-call | 2026-07-06 | full |
| NETWRIX-ITDR-2026 | ITDR automation best practices for security teams | Netwrix | vendor | https://www.netwrix.com/en/resources/blog/itdr-automation-best-practices/ | 2026-06-05 | full |
| INFOSEC-SERVICEDESK-2026 | Your Service Desk Agents Can't Out-Talk an AI | Infosecurity Magazine (Specops author) | vendor | https://www.infosecurity-magazine.com/blogs/your-service-desk-agents-cant/ | 2026-10-06 | full |
| PETRI-SERVICEDESK-2026 | 5 Ways to Secure Your Service Desk Against AI-Enabled Attacks | Petri (Specops author) | vendor | https://petri.com/5-ways-to-secure-your-service-desk-against-ai-attacks/ | 2026-09-01 (updated 2026-10-01) | full |
| NAMETAG-IMPERSONATION-2026 | Rebuilding Trust in the Age of AI: The 2026 Workforce Impersonation Report | Nametag | vendor | https://www.go.nametag.co/hubfs/The%202026%20Workforce%20Impersonation%20Report.pdf | 2026 (month not found) | full |
| OPAL-REVIEWS-2026 | AI-Guided access reviews, now in Opal | Opal Security | vendor | https://www.opal.dev/blog/ai-guided-access-reviews | 2026-06-15 | full |
| OPAL-PALADIN-2026 | Paladin: AI that applies your policy to every request | Opal Security | vendor | https://www.opal.dev/blog/paladin-policy-ai | 2026-08-06 | full |
| SAILPOINT-RECS-2022 | AI-driven Access Recommendations: Less Certification. More Revocation. | SailPoint | vendor | https://www.sailpoint.com/blog/ai-driven-access-recommendations-less-certification-more-revocation | 2022-06-30 | full |
| MS-CAAGENT-2026 | Microsoft Entra Conditional Access Optimization Agent | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization | 2026-06-23 | full |
| MS-ENTRA-RISKYUSER-2025 | Respond to identity threats using risky user summarization | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/security-copilot/entra-risky-user-summarization | 2025-09-23 | full |
| MS-ENTRA-LIFECYCLE-2025 | Manage employee lifecycle using Microsoft Security Copilot | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/security-copilot/entra-lifecycle-workflows | 2025-09-23 | full |
| MS-ENTRA-WHATSNEW-OCT-2026 | What's new in Microsoft Entra: October 2026 | Microsoft Tech Community | vendor | https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-october-2026/4556460 | 2026-10-12 | full (text mirror) |
| NHIMG-SAILPOINT-2026 | AI-driven access recommendations expose the limits of certification | Non-Human Identity Management Group | community | https://nhimg.org/articles/ai-driven-access-recommendations-expose-the-limits-of-certification/ | 2026-06-24 | full |
| NHIMG-OMADA-2026 | AI augments IGA by fixing review fatigue and weak audit context | Non-Human Identity Management Group | community | https://nhimg.org/articles/ai-augments-iga-by-fixing-review-fatigue-and-weak-audit-context/ | 2026-06-24 | full |
| NHIMG-OZ-2026 | Industrialized fraud is breaking legacy identity verification controls | Non-Human Identity Management Group | community | https://nhimg.org/articles/industrialized-fraud-is-breaking-legacy-identity-verification-controls/ | 2026-07-11 | full |
| HN-REALITYDEFENDER-2025 | Launch HN: Reality Defender (YC W22) - API for Deepfake and GenAI Detection | Hacker News | community | https://news.ycombinator.com/item?id=44941580 | 2025-08-18 | full (comments via API) |
| SCOTTHELME-PASSKEYS-2026 | Passkeys Are Not a Trap | Scott Helme | community | https://scotthelme.co.uk/passkeys-are-not-a-trap/ | 2026-10-14 | full |
| NONFUNCTIONAL-PASSKEYS-2026 | Passkeys are a trap. Do not use them. | The Hack Non-Functional (Substack) | community | https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them | 2026-10-10 | full (opening only) |
| DIRKJANM-ACTORTOKENS-2025 | One Token to rule them all - obtaining Global Admin in every Entra ID tenant via Actor tokens | dirkjanm.io (Dirk-jan Mollema) | community | https://dirkjanm.io/obtaining-global-admin-in-every-entra-id-tenant-with-actor-tokens/ | 2025-09-17 | full (opening only) |
| CFI-ENTRUST-2025 | Deepfakes, Social Engineering, Injection Attacks On The Rise, Report Reveals | Crowdfund Insider | press | https://www.crowdfundinsider.com/?p=255847 | 2025-11-25 | full |
| HNS-DBIR-2026 | Verizon DBIR: Vulnerability exploitation is the dominant initial access vector | Help Net Security | press | https://www.helpnetsecurity.com/2026/05/20/verizon-2026-dbir-findings/ | 2026-05-20 | full |
| FINCEN-DEEPFAKE-2024 | FinCEN Alert FIN-2024-Alert004: Fraud Schemes Involving Deepfake Media Targeting Financial Institutions | FinCEN | regulator | https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf | 2024-11-13 | full |
| CISA-NIST-IR8587-2026 | CISA and NIST Release Guidelines to Protect Federal Cloud Identity Systems from Token Theft, Forgery, and Misuse | CISA | regulator | https://www.cisa.gov/news-events/news/cisa-and-nist-release-guidelines-protect-federal-cloud-identity-systems-token-theft-forgery-and | 2026-09-09 | full (text mirror) |
| NIST-80063-2025 | NIST SP 800-63 Digital Identity Guidelines, Revision 4 | NIST | standard-setter | https://pages.nist.gov/800-63-4/ | 2025-07 | full (text mirror) |
| ARXIV-2609.09489 | Audio Deepfake Detection Using Temporal Coherence Analysis | arXiv (preprint) | academic | https://arxiv.org/abs/2609.09489 | 2026-09-08 | full (abstract) |
| ARXIV-2607.14753 | Large Audio Language Models for Spoofing-Aware Speaker Verification | arXiv (preprint) | academic | https://arxiv.org/abs/2607.14753 | 2026-07-16 | full (abstract) |
| ARXIV-2503.11573 | Synthesizing Access Control Policies using Large Language Models | arXiv (preprint) | academic | https://arxiv.org/abs/2503.11573 | 2025-03-14 | full (abstract) |
| GARTNER-DEEPFAKE-2024 | Gartner Predicts 30% of Enterprises Will Consider Identity Verification and Authentication Solutions Unreliable in Isolation Due to AI-Generated Deepfakes by 2026 | Gartner | firm | https://www.gartner.com/en/newsroom/press-releases/2024-02-01-gartner-predicts-30-percent-of-enterprises-will-consider-identity-verification-and-authentication-solutions-unreliable-in-isolation-due-to-deepfakes-by-2026 | 2024-02-01 | search-only |
| PRACTICAL365-ENTRAAGENTS-2025 | Entra Agents are Promising but Could do More | Practical365 | community | https://practical365.com/entra-agents-could-do-more/ | 2025-10-07 | search-only (page returned a server error; date from text mirror header) |
| MSSP-BLACKPOINT-2026 | Blackpoint Cyber adds AI SOC agent for identity threat response | MSSP Alert | press | https://www.msspalert.com/brief/blackpoint-cyber-adds-ai-soc-agent-for-identity-threat-response | 2026 (month not shown) | search-only |

Type counts (60 listed refs): vendor 22, community 11, firm 8 (seven Forrester posts and one search-only Gartner release), conference 4, podcast 3, survey 3, press 3, academic 3, regulator 2, standard-setter 1. Search-only entries (4): IDAC-409-2026, GARTNER-DEEPFAKE-2024, PRACTICAL365-ENTRAAGENTS-2025, MSSP-BLACKPOINT-2026. Sources opened in full (56), several only in part as noted in the Access column.

## 6. Gaps

- **No quality evidence for AI in human IAM operations.** No override, false-approval, false-negative or parallel-run data for AI-guided certification, Conditional Access agents, risky-user summaries, access-request agents or ITDR automation. No named-customer case study with a metric for these was found; Opal's Mercari mention is about automated reviews at scale, not AI-guided decisions.
- **Primary reports not reached:** Gartner research and press releases (blocked; the 2024 deepfake prediction and the 2025-09-22 GenAI-attack survey are second-hand), Forrester paid research, the Entrust, Sumsub and Jumio identity-fraud reports (Entrust's page blocked; Sumsub and Jumio figures seen only in a secondary search result and not used), the SANS ITDR report body (only the landing page), the Verizon DBIR itself (read through Help Net Security; DBIR figures for credential abuse at 13% of initial access and 39% of breaches were search-only), and Omada's original post.
- **Podcast depth:** I read show notes only, no audio or transcripts. Identity at the Center pages were blocked (metacast 403, feed empty, Spotify/Amazon not opened), so the episodes (#398, #409, #410 and the Identiverse live episode) are search-only. Entra.Chat, Cloud Security Podcast and the Darknet Diaries feed gave nothing identity-and-AI specific (Cloud Security Podcast's feed returned 404).
- **Conference session detail:** official Identiverse, Black Hat, DEF CON and RSAC session lists were not retrievable. Identiverse coverage relies on independent and analyst recaps; the Gartner IAM Summit is an agenda for an event not yet held, so no content is yet available. Attendance figures for Identiverse 2026 conflict (3,274+ onsite on the organizer's page; more than 3,700 and more than 3,800 in other coverage), so I use none.
- **Community discussion:** Reddit was blocked (the text mirror reports an abuse block). Hacker News search through its API gave only two on-topic AI-and-identity threads plus the passkey debate. IDSA content was blocked by Cloudflare. No 2026 IDPro or IDSA survey was found, so there is no data on identity professionals' AI use or skills.
- **Fraud discourse is thin and vendor-led.** I found no bank-side practitioner discussion (FS-ISAC, fraud-conference sessions, FBI IC3 material not opened); the OWASP AppSec "When the Fraud Analyst Becomes an Agent" session listed in the landscape file is an unverified title and is not used. RSAC's "Cyber Fraud Day" for 2027 is mentioned in the landscape file only.
- **Dates not found:** Nametag report (month), SC World segment (month), Palo Alto Networks 2026 Identity Security Landscape excerpt (month), SANS ITDR report (day), MSSP Alert brief. NHIMG headline dates differ from underlying vendor posts (SailPoint blog is 2022-06-30, NHIMG says 2025-12-10; Omada and Oz Forensics originals not opened).
- **Source reliability:** a large share of the practical material is vendor-authored (22 of 60 sources) and several "independent" items (NHIMG summaries, Specops-authored articles on Infosecurity Magazine and Petri) are vendor-adjacent. The SANS ITDR page is internally inconsistent on the 85% figure. Okta's counterfactual analysis is partly form-gated, so only the visible portion was read.
- **Academic evidence is three arXiv preprints**; no peer-reviewed study of LLMs in IAM operations was found.
- **Search budget:** I used 21 web searches (more than a pure "plan carefully" budget would suggest); the rest of the work used direct fetches and text mirrors. Remaining leads: Opal's CPO post on requests, policy and investigation; SailPoint, Saviynt and Veza product announcements (SailPoint's 2026 pages not opened); CrowdStrike Falcon Identity and Microsoft ID Protection outcome claims; FIDO Authenticate 2026 talks after 2026-10-21; Identiverse DC and Gartner IAM Summit recaps after November-December 2026.
