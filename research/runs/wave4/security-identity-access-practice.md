# Identity and access management: practice deep dive

Archetype: security. Module: identity-access. Angle: practice. Compiled 2026-10-17. Working files were kept in a private `mktemp -d` folder. Web search was used 5 times (a contact-centre case-study scan, Microsoft's agent results, practitioner write-ups on LLM access reviews, the Instacart talk, and IGA customer results). Everything else was opened with `curl`, the `r.jina.ai` mirror (CISA, DHS, SailPoint, Persona, Microsoft Tech Community, GitHub), `pdftotext`, the public Greenhouse job-board API and the public arXiv pages.

## 1. Summary

- **Where AI is really changing identity work.** The best-evidenced changes are on the people-facing edge: contact-centre caller authentication and fraud scoring (HealthEquity, Michigan State University Federal Credit Union, Virginia Employment Commission, all via Pindrop case studies) and automated identity verification for help-desk account recovery at Cisco (via Persona). These give named organisations and figures, but every figure is vendor-published.
- **Inside the IAM team, the work is mostly first-pass assistance and agent suggestions with a person approving.** Microsoft's Conditional Access Optimization Agent is the most mature product (generally available since 2025-07-14; Microsoft reports an average of 26 policy gaps found per customer per month). The only first-party LLM approval bot found is Instacart's Gadjit for just-in-time privileged access, built on a ConductorOne policy engine and open-sourced.
- **The 2026 vendor wave is about identity for AI agents, not AI for identity teams.** CrowdStrike (2026-09-02), Okta (2026-09-22), SailPoint (2026-10-06), Saviynt (2026-06-15) and Palo Alto Networks (2026-05-12) lead with agent identity. Human-side AI claims (autonomous posture management, conversational access requests, zero standing privilege) are announcements without published results. Agent-identity items are routed to ai-security.
- **Quality evidence is the weakest part.** No override, false-positive or acceptance rate was found for AI access-review recommendations, Conditional Access suggestions or identity-threat response. The only independent measurements are adjacent: a DHS test of remote identity-validation vendors (median presentation-attack detection 78%) and academic papers showing voice-clone bypass of speaker verification, poor out-of-domain deepfake detection, and 50.3% end-to-end correctness for LLM-generated access policies.
- **Defence is leaning on architecture as much as on AI.** Okta's threat intelligence argues attackers use AI to speed up old methods and that phishing-resistant enrolment and sign-in policies could have stopped 99.75% of about 6,000 social-engineering events it analysed (counterfactual, vendor-published). FinCEN, NIST and the FBI point to phishing-resistant MFA, live verification and out-of-band checks.
- **IAM roles are shifting toward approving agent output and writing policy as code.** Cloudflare's IAM postings require hands-on LLM experience; Instacart moved approvals from staff engineers to a bot plus policy code.

Use cases by grade: A = 3, B = 7, C = 9, D = 1 (20 total). Sources: 56 distinct references (by type: vendor 30, job-posting 9, academic 5, regulator 4, survey 4, standard-setter 2, community 1, conference 1).

## 2. Use cases

```yaml
- id: security-identity-access-01
  title: Daily agent scan of Conditional Access policies for coverage gaps, with report-only fixes for an administrator to approve
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - review-assurance
  - software-systems
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Conditional Access policy sets grow over time. New users, apps and agent identities can fall outside MFA or device controls, policies overlap, and some carry too many or no exceptions. Finding these gaps meant reading policy logic by hand; one customer quoted by Microsoft says it used to take weeks of manual review (MSFT-ENTRAGA-2025, customer quotes).
  solution: A Security Copilot agent in the Entra admin center scans the tenant's Conditional Access policies every 24 hours (or on demand). It looks for users and apps with no MFA or device-control policy, legacy-authentication and device-code gaps, overlapping policies that could be consolidated, and outlier policies with too many or no exceptions. It proposes a new policy in report-only mode or an edit, shows its reasoning, and logs its activity. Later releases add chat with the agent, a five-phase rollout plan, Intune alignment, root-cause analysis of failed sign-ins and ServiceNow change requests.
  outcomes:
  - {lever: quality, description: Microsoft reports gaps found per customer since general availability, figure: 26 policy gaps per customer per month (average), measures: 'Average policy gaps the agent uncovered per customer per month since general availability, in Microsoft''s words; number of customers and period not stated', provenance: vendor-published, source_ref: MSFT-CAUPDATE-2025}
  - {lever: risk, description: Microsoft reports customers who improved their posture, figure: 73% of customers using the agent, measures: Share of customers using the agent that Microsoft says made 'meaningful improvements' in Zero Trust security posture; 'meaningful' is not defined and the denominator is not given, provenance: vendor-published, source_ref: MSFT-CAUPDATE-2025}
  - {lever: speed, description: Microsoft reports preview customers who got usable recommendations quickly, figure: More than 83% of preview customers, measures: Customers who used the agent during preview and received actionable recommendations in their first few runs; number of preview customers not stated, provenance: vendor-published, source_ref: MSFT-ENTRAGA-2025}
  - {lever: speed, description: A named customer's identity lead says the agent replaces review that used to take weeks, figure: weeks of manual review (qualitative), measures: Quote from Avanade's Global Security Technology Lead as printed by Microsoft; no measurement, provenance: self-reported, source_ref: MSFT-ENTRAGA-2025}
  prerequisites:
  - Microsoft Entra ID P1 or higher (P2 for risk-based policy suggestions)
  - Security Copilot security compute units provisioned; at least one SCU is billed monthly even if the agent uses none
  - Security Administrator role to activate the agent; Conditional Access Administrator or Security Administrator to act on suggestions
  - Intune licences for device-based control suggestions
  risks_and_guardrails:
  - The agent changes no existing policy unless an administrator explicitly approves, and every new policy it suggests is created in report-only mode (MSFT-CAAGENT-2026, 'How it works')
  - 'Documented limits: a run reviews up to 300 users and 150 applications and evaluates 40 policy pairs; scanning covers 24 hours; a started run cannot be stopped; suggestions cannot be customised or overridden (MSFT-CAAGENT-2026, ''Limitations'')'
  - Activity (install, enable, run history) is written to the Security Copilot audit log, and the agent gives plain-language explanations of each recommendation (MSFT-ENTRAGA-2025, 'What's new in GA')
  - Deep analysis flags missing break-glass accounts to prevent lockout (MSFT-CAUPDATE-2025, 'Always learning')
  human_checkpoints:
  - Administrator reviews each suggestion, its rationale and the policy contents before approving (MSFT-CAAGENT-2026)
  - Report-only mode and a phased rollout let administrators see the impact before enforcement (MSFT-CAUPDATE-2025)
  - Read-only roles (Security Reader, Global Reader) can see suggestions but not act (MSFT-CAAGENT-2026, Prerequisites)
  role_evolution: Conditional Access administrators move from hand-reading policy logic to approving or rejecting agent suggestions and writing custom instructions. Microsoft describes the aim as freeing admins for strategic improvements (MSFT-CAUPDATE-2025, introduction).
  evidence_grade: B
  sources:
  - {ref: MSFT-CAAGENT-2026, title: Microsoft Entra Conditional Access Optimization Agent, publisher: Microsoft Learn, type: vendor, url: 'https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization', date: '2026-06-23', access: full, locator: Overview; Prerequisites; Limitations; How it works}
  - {ref: MSFT-ENTRAGA-2025, title: 'Smarter identity security starts with AI (blog, A. Simons)', publisher: 'Microsoft Tech Community, Microsoft Entra Blog', type: vendor, url: 'https://techcommunity.microsoft.com/blog/microsoft-entra-blog/-/4429001', date: '2025-07-14', access: full, locator: Section 'Conditional Access Optimization Agent is now generally available' and customer quotes}
  - {ref: MSFT-CAUPDATE-2025, title: 'The Conditional Access Optimization Agent keeps getting better and making your life easier (blog, A. Simons)', publisher: 'Microsoft Tech Community, Microsoft Entra Blog', type: vendor, url: 'https://techcommunity.microsoft.com/blog/microsoft-entra-blog/-/4460535', date: '2025-10-14', access: full, locator: 'Introduction (26 gaps, 73%); sections on chat, phased rollout, deep analysis, ServiceNow'}
  - {ref: MSFT-ENTRAAGENTS-2026, title: Microsoft Entra agents (overview), publisher: Microsoft Learn, type: vendor, url: 'https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents', date: '2026-01-21', access: full, locator: '''Conditional Access Optimization Agent'' attribute table (trigger: every 24 hours or manual)'}
  last_reviewed: '2026-10-17'
  notes: 'Grade B, not A: the named customers (Avanade, Athora) give quotes only, and the figures are Microsoft aggregates across unnamed customers. No false-positive, acceptance or rejection rate for the agent''s suggestions was found. The ServiceNow integration and activity-based runs are marked preview in the Learn page (updated 2026-06-30).'
- id: security-identity-access-02
  title: Agent-planned passkey adoption campaigns for privileged administrators
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - coordination-scheduling
  - transaction-processing
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Moving administrators to phishing-resistant sign-in needs readiness checks on devices and operating systems, user nudges, grace periods and a final enforcement switch, which is manual coordination at scale.
  solution: The Conditional Access Optimization Agent identifies eligible privileged administrators (up to 200 users per campaign), assesses device and passkey readiness, generates a four-stage plan (target users, check device readiness, require passkey registration, enforce passkey usage), guides users through the steps, and applies Conditional Access enforcement as users become ready. It re-evaluates progress and advances users automatically.
  outcomes:
  - {lever: risk, description: none published, figure: none published, measures: No result figures in the documentation, provenance: vendor-published, source_ref: MSFT-PASSKEYCAMP-2026}
  prerequisites:
  - Entra ID P1 or higher and available security compute units
  - Passkeys enabled in the Authentication methods policy
  - Security Administrator role; the Conditional Access Administrator role cannot manage campaigns
  risks_and_guardrails:
  - Campaign settings can be edited only while the campaign is in the 'Not started' state (MSFT-PASSKEYCAMP-2026, 'Review and customize')
  - The documentation recommends excluding break-glass or emergency-access accounts (MSFT-PASSKEYCAMP-2026, tip under 'Review targeted users')
  - Users who lack a compatible device or OS are held in the device-readiness stage rather than enforced (MSFT-PASSKEYCAMP-2026)
  human_checkpoints:
  - Administrator reviews the proposed plan and can edit targeted users and grace periods before deploying (MSFT-PASSKEYCAMP-2026)
  - Suggestions can be dismissed like any other agent suggestion (MSFT-PASSKEYCAMP-2026)
  role_evolution: The identity administrator reviews and tunes a campaign plan rather than building the list, notices and enforcement steps by hand (MSFT-PASSKEYCAMP-2026, introduction).
  evidence_grade: C
  sources:
  - {ref: MSFT-PASSKEYCAMP-2026, title: 'Conditional Access Optimization Agent: passkey adoption campaigns', publisher: Microsoft Learn, type: vendor, url: 'https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization-passkeys', date: '2026-05-22', access: full, locator: Introduction; Prerequisites; 'How the agent identifies passkey campaign candidates'; campaign stages}
  last_reviewed: '2026-10-17'
  notes: 'Documentation only; it does not state preview or general availability and no customer is named. Context from an Okta analysis (vendor-published, measures the control not the agent): in about 6,000 real social-engineering events, requiring enrolment of phishing-resistant factors could have stopped 88% of account-takeover attempts, rising to 99.75% with app sign-in enforcement (OKTA-TI-2026, section ''How the security invariants performed'').'
- id: security-identity-access-03
  title: Natural-language risk summaries and investigation prompts for risky users, plus a continuous identity-risk agent
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Microsoft describes identity risk investigation as needing context that admins and SOC analysts must gather before deciding what to do with a flagged user (MSFT-RISKYUSER-2026, introduction).
  solution: In Entra ID Protection, Copilot summarises in natural language why a user's risk level was raised and lists next steps and documentation (for example, create sign-in-risk and user-risk Conditional Access policies). Admins can also ask Security Copilot to list risky users, show a user's risk history and investigate incidents. A separate Identity Risk Management Agent (preview) runs every 24 hours, on demand or as continuous monitoring.
  outcomes:
  - {lever: speed, description: none published, figure: none published, measures: Documentation says the feature 'helps reduce the time to resolution' but gives no measurement, provenance: vendor-published, source_ref: MSFT-RISKYUSER-2026}
  prerequisites:
  - Entra ID P2 licences for ID Protection risky-user summarisation
  - Security Copilot enabled in the tenant
  - At least Security Reader to view risky users; Security Administrator for the Identity Risk Management Agent
  risks_and_guardrails:
  - The agent has its own Entra Agent ID and a fixed set of permissions that cannot be changed or removed (MSFT-ENTRAAGENTS-2026, 'What are Microsoft Entra agents?')
  - When the Identity Risk Management Agent is on, a separate agent-written risky-user summary appears beside the Copilot one (MSFT-RISKYUSER-2026, Note)
  human_checkpoints:
  - Summary and recommendations are advice; the admin or analyst decides on remediation (MSFT-RISKYUSER-2026)
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
  - {ref: MSFT-RISKYUSER-2026, title: Respond to identity threats using Risky User summarization (Security Copilot in Microsoft Entra), publisher: Microsoft Learn, type: vendor, url: 'https://learn.microsoft.com/en-us/entra/security-copilot/entra-risky-user-summarization', date: '2025-09-23', access: full, locator: Introduction; 'Investigate risky users'; 'Investigate risky users using Copilot'}
  - {ref: MSFT-ENTRAAGENTS-2026, title: Microsoft Entra agents (overview), publisher: Microsoft Learn, type: vendor, url: 'https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents', date: '2026-01-21', access: full, locator: '''Identity Risk Management Agent (Preview)'' attribute table'}
  - {ref: MSFT-ENTRAGA-2025, title: 'Smarter identity security starts with AI (blog, A. Simons)', publisher: 'Microsoft Tech Community, Microsoft Entra Blog', type: vendor, url: 'https://techcommunity.microsoft.com/blog/microsoft-entra-blog/-/4429001', date: '2025-07-14', access: full, locator: Section 'Security Copilot in Microsoft Entra is now generally available'}
  last_reviewed: '2026-10-17'
  notes: Microsoft says Security Copilot in Entra became generally available on 2025-07-14. No named customer or measurement was found for this use. The Identity Risk Management Agent is labelled preview.
- id: security-identity-access-04
  title: Evidence-based recommendations and agent first pass on access review decisions
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Reviewers in periodic access certifications face long lists with little context on who uses what, and many default to approving everything. Lumos calls this 'rubber stamping' (LUMOS-UAR-2025); no independent rate was found.
  solution: The review screen carries system recommendations. Microsoft Entra marks users inactive for 30 days with a Deny recommendation and uses a machine-learning 'user-to-group affiliation' score based on reporting-structure distance to suggest Deny for outliers. Lumos describes an AI Identity Agent ('Albus') that makes a first pass on every identity using role, department, access sensitivity, last activity, peer-group alignment and separation-of-duties conflicts, separates low-risk common access from high-risk anomalies, and suggests what to keep or remove.
  outcomes:
  - {lever: speed, description: Lumos states review campaigns finish faster than manual spreadsheet reviews, figure: up to 6x faster, measures: 'Lumos''s claim for finishing review campaigns; baseline, sample and customer not stated', provenance: vendor-published, source_ref: LUMOS-UAR-2025}
  prerequisites:
  - Usage and last-sign-in data per entitlement, organisation hierarchy and manager attribute (Entra user-to-group affiliation needs both)
  - Entra ID Governance licence for user-to-group affiliation; groups over 600 users are not supported (MSFT-ARREC-2026)
  - Connectors that bring humans, service accounts and other non-human identities into one review (LUMOS-UAR-2025)
  risks_and_guardrails:
  - The reviewer still decides; recommendations are decision helpers (MSFT-ARREC-2026, introduction)
  - Admins can query which review decisions overrode AI-suggested actions, which gives a way to track override rates (MSFT-GOVOPT-2026, 'Access review decision analysis')
  - Lumos says the agent suggests what to keep or remove 'based on real-time evidence' and shows activity and last-login data in the review screen (LUMOS-UAR-2025, 'Agentic Autonomy' and customer quote)
  human_checkpoints:
  - Application owners and managers approve or deny each recommendation; Lumos describes the agent as running 'the first pass' (LUMOS-UAR-2025)
  role_evolution: Reviewers check evidence and exceptions instead of reading raw entitlement rows. Prosper's corporate IT manager says activity and last-login data inside the review screen turned a compliance task into a security check (LUMOS-UAR-2025, customer validation quote).
  evidence_grade: B
  sources:
  - {ref: LUMOS-UAR-2025, title: 'Lumos Launches Industry-First Agentic User Access Reviews, Moving Towards Autonomous Identity Governance', publisher: Lumos, type: vendor, url: 'https://www.lumos.com/blog/lumos-launches-industry-first-agentic-user-access-reviews', date: '2025-12-08', access: full, locator: Launch text; 'Customer Validation' (Prosper); 'Key Capabilities'}
  - {ref: MSFT-ARREC-2026, title: Review recommendations for access reviews (Microsoft Entra ID Governance), publisher: Microsoft Learn, type: vendor, url: 'https://learn.microsoft.com/en-us/entra/id-governance/review-recommendations-access-reviews', date: '2026-03-12', access: full, locator: '''Inactive user recommendations''; ''User-to-Group Affiliation'''}
  - {ref: MSFT-GOVOPT-2026, title: Governance and optimization with Security Copilot in Microsoft Entra, publisher: Microsoft Learn, type: vendor, url: 'https://learn.microsoft.com/en-us/entra/security-copilot/entra-governance-optimization', date: '2025-09-23', access: full, locator: '''Access review decision analysis'' prompts'}
  - {ref: SAILPOINT-HUMANFABRIC-2026, title: SailPoint Announces Modernization Capabilities for both Cloud and On-Premises Identity Security, publisher: SailPoint, type: vendor, url: 'https://www.sailpoint.com/press-releases/sailpoint-announces-modernization-capabilities-for-both-cloud-and-on-premises-identity-security', date: '2026-10-06', access: full, locator: '''Access certifications enhancements'' (re-platformed certification engine; context, not an AI claim)'}
  last_reviewed: '2026-10-17'
  notes: 'Grade B: Prosper is named but the evidence is a quote, and ''up to 6x'' has no stated baseline. No published override, acceptance or error rate for any AI access-review recommendation was found. A web search (search-only, not used as evidence) surfaced unattributed claims that over 90% of certifications are approved without meaningful review; treat as unverified.'
- id: security-identity-access-05
  title: LLM bot that scores just-in-time privileged access requests and auto-approves above a threshold
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - transaction-processing
  - expert-judgment
  pattern: document-to-decision
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Just-in-time access that needs manager approval sits in queues. Approvers lack the context to judge a request and Instacart's security lead says managers across the industry probably approve close to 100% of the time (C1-INSTACART-2024).
  solution: Instacart built Gadjit, an LLM-powered bot (later open-sourced). When a just-in-time request needing manager approval appears in the identity governance platform (ConductorOne), Gadjit pulls the entitlement description, its risk level and the people who hold it through the API. An LLM compares the requester's attributes with the entitlement description and with current holders. A separate scoring step estimates how likely the request is legitimate. Above a set threshold the bot approves and access is provisioned automatically.
  outcomes:
  - {lever: quality, description: Instacart says the bot's accuracy in testing is close to perfect, figure: consistently nearly 100% in testing, measures: 'Instacart''s description of Gadjit accuracy in testing as relayed in a ConductorOne customer story; test set, ground truth and sample size not stated', provenance: vendor-published, source_ref: C1-INSTACART-2024}
  - {lever: risk, description: 'Share of privileged permissions moved to automated just-in-time access by the policy engine before the bot (rule-based, not AI)', figure: 95%, measures: 'Share of Instacart''s privileged permissions moved to automated just-in-time access with the C1.ai policy engine; the same page also says 100% of privileged access moved, and does not explain the difference', provenance: vendor-published, source_ref: C1-INSTACART-2024}
  prerequisites:
  - Entitlement, HR and cloud data centralised in the governance platform and reachable by API (IdP, HRIS, AWS, GCP, Snowflake, internal apps)
  - Access policies written as code (Terraform) so conditions are reviewable
  - An LLM plugin (the README lists OpenAI GPT-4o) and a scoring plugin; Python 3.12; deployable as a Lambda webhook or a once-a-minute job (GADJIT-GITHUB-2024, 'Deployment')
  risks_and_guardrails:
  - Instacart states generative AI is not yet reliable enough to trust with objective approval decisions; it uses the LLM to read and interpret data and a separate computed score for the decision (C1-INSTACART-2024, 'Using AI to get to 100% JIT access automation')
  - Every step is visible in the platform audit log, and Instacart says auditors have raised no unanswered question about the audit path (C1-INSTACART-2024)
  - Privileged access is capped at a maximum of 90 days (C1-INSTACART-2024)
  human_checkpoints:
  - Policy-as-code configurations are reviewed by account owners every quarter (C1-INSTACART-2024)
  - What happens to requests that score below the threshold is not stated in the sources
  role_evolution: Before this, highly paid staff engineers approved sensitive requests and ran quarterly reviews. Security engineers now write the policy code and the bot (C1-INSTACART-2024, closing section).
  evidence_grade: B
  sources:
  - {ref: C1-INSTACART-2024, title: 'How Instacart is using AI to achieve zero standing privileges (customer story; undated, year inferred from the BSidesLV24 talk it describes)', publisher: ConductorOne (C1.ai), type: vendor, url: 'https://www.conductorone.com/customers/instacart', date: '2024', access: full, locator: Sections 'Automating JIT access with conditional policies' and 'Using AI to get to 100% JIT access automation'}
  - {ref: GADJIT-GITHUB-2024, title: 'instacart/gadjit: Automated Access Request Reviews (README; undated, year inferred from GPT-4o plugin and 2024 BSidesLV talk)', publisher: GitHub (Instacart), type: community, url: 'https://github.com/instacart/gadjit', date: '2024', access: full, locator: 'README: ''Plugin Architecture''; ''Deployment'''}
  - {ref: SECBOULEVARD-BSIDESLV24-2025, title: 'BSidesLV24 - Breaking Ground - JIT Happens: How Instacart Uses AI to Keep Doors Open and Risks Closed', publisher: Security Boulevard, type: conference, url: 'https://securityboulevard.com/2025/04/bsideslv24-breaking-ground-jit-happens-how-instacart-uses-ai-to-keep-doors-open-and-risks-closed/', date: 2025-04, access: search-only, locator: 'Title only: BSidesLV24 talk ''JIT Happens: How Instacart Uses AI to Keep Doors Open and Risks Closed'' (page blocked; seen in search results)'}
  last_reviewed: '2026-10-17'
  notes: 'Named deployment (Instacart) with the only first-party-built LLM approval bot found. Grade B, not A: ''nearly 100%'' has no denominator. Dates: the customer story and README are undated; 2024 is inferred from the BSidesLV24 talk the story describes and the GPT-4o plugin. The 95% figure belongs to the rule-based policy engine and is adjacent to the AI step.'
- id: security-identity-access-06
  title: Conversational assistant for employee IT and access questions and requests
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - client-interaction
  - transaction-processing
  pattern: service-agent-escalation
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: New hires and employees must already know which of about 1,500 applications to ask about access, devices and VPN, so requests go to the wrong place (OKTA-DEX-2026, Lesson 1).
  solution: Okta built Dex, an orchestrating agent on its Okta One platform that covers IT, people, travel and expense support and acts as 'one front door'. Dex is registered in Okta Universal Directory like a human identity and is checked against the signed-in user's access each time. SailPoint has announced a similar AI agent for natural-language access requests inside chat tools, with custom forms for business justification.
  outcomes:
  - {lever: experience, description: Employee adoption two weeks after launch, figure: 25% in two weeks, measures: Share of Okta employees using Dex within two weeks of launch (denominator not stated by Okta), provenance: self-reported, source_ref: OKTA-DEX-2026}
  - {lever: capacity, description: Interactions handled to date, figure: 'over 23,500', measures: Interactions Dex has fielded 'to date' (date of count not stated), provenance: self-reported, source_ref: OKTA-DEX-2026}
  prerequisites:
  - Agent identities in the central directory, with access capped at the signed-in human's access (OKTA-DEX-2026, Lesson 2)
  - Knowledge bases cleaned until the agent gives the right answer (OKTA-DEX-2026, Lesson 3)
  - Tool scoping per identity to control token cost (OKTA-DEX-2026, Lesson 3)
  risks_and_guardrails:
  - Okta says an agent should not have more access to systems and data than the human it acts for, and secure token storage replaces static credentials (OKTA-DEX-2026, Lesson 2)
  - '''You can''t have a compensation agent that''s only 80% accurate''; AI can be confidently incorrect (OKTA-DEX-2026, Lesson 3)'
  - SailPoint's conversational requests were announced on 2026-10-06; no availability date for general release is given in the release (SAILPOINT-HUMANFABRIC-2026)
  human_checkpoints:
  - Not described for Dex; SailPoint's agent collects justification and compliance details in the chat flow before the request proceeds (SAILPOINT-HUMANFABRIC-2026)
  role_evolution: Okta's SVP says IT risks becoming the 'Department of No' under AI pressure, and positions fewer, more capable agents on a governed identity base as the alternative (OKTA-DEX-2026, introduction and closing).
  evidence_grade: B
  sources:
  - {ref: OKTA-DEX-2026, title: 'Lessons learned from securing our digital workforce (J. Cline, SVP Technology, Data & Intelligence)', publisher: Okta Newsroom, type: vendor, url: 'https://www.okta.com/newsroom/articles/lessons-from-securing-our-digital-workforce/', date: '2026-09-17', access: full, locator: Lesson 1 (Dex adoption figures); Lesson 2; Lesson 3}
  - {ref: SAILPOINT-HUMANFABRIC-2026, title: SailPoint Announces Modernization Capabilities for both Cloud and On-Premises Identity Security, publisher: SailPoint, type: vendor, url: 'https://www.sailpoint.com/press-releases/sailpoint-announces-modernization-capabilities-for-both-cloud-and-on-premises-identity-security', date: '2026-10-06', access: full, locator: '''Conversational Access Requests'' bullet'}
  last_reviewed: '2026-10-17'
  notes: 'Grade capped at B: the measures describe general IT, HR, travel and expense support, not access requests alone. Okta is both the vendor and the deploying firm, so figures are self-reported. The agent-identity half of this case is routed to ai-security.'
- id: security-identity-access-07
  title: Natural-language governance queries, audit preparation and lifecycle-workflow drafting for identity admins
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - data-reporting
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Preparing for an annual governance audit means pulling access review status, entitlement catalogues and privileged-role settings from several admin screens, and building new lifecycle workflows takes configuration work.
  solution: Security Copilot in the Entra admin center answers governance prompts such as the top pending access reviews, who approved or denied in a review, which decisions overrode AI suggestions, what is in an entitlement catalogue, and PIM settings. For lifecycle workflows it gives step-by-step guidance for a new workflow from a prompt, lists templates, troubleshoots processing results and compares workflow versions. The admin still creates and enables the workflow in the portal.
  outcomes:
  - {lever: capacity, description: none published, figure: none published, measures: No measurements in the documentation, provenance: vendor-published, source_ref: MSFT-GOVOPT-2026}
  prerequisites:
  - Security Copilot enabled; Entra ID P2 and Identity Governance Administrator (or Security Administrator for PIM) depending on use (MSFT-GOVOPT-2026, Prerequisites)
  - Entra ID Governance licence and Lifecycle Workflow Administrator role for workflow prompts (MSFT-LIFECYCLE-2026)
  risks_and_guardrails:
  - If a prompt is blocked by missing permissions, Copilot shows the recommended role and can activate it through an eligible PIM assignment on request (MSFT-GOVOPT-2026, Note)
  - Verification testing happens before the workflow schedule is enabled (MSFT-LIFECYCLE-2026, 'Create step-by-step guidance')
  human_checkpoints:
  - Admin builds and enables the workflow; Copilot output is guidance (MSFT-LIFECYCLE-2026)
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
  - {ref: MSFT-GOVOPT-2026, title: Governance and optimization with Security Copilot in Microsoft Entra, publisher: Microsoft Learn, type: vendor, url: 'https://learn.microsoft.com/en-us/entra/security-copilot/entra-governance-optimization', date: '2025-09-23', access: full, locator: Introduction; 'Access review decision analysis'; PIM use cases}
  - {ref: MSFT-LIFECYCLE-2026, title: Manage lifecycle workflows using Security Copilot in Microsoft Entra, publisher: Microsoft Learn, type: vendor, url: 'https://learn.microsoft.com/en-us/entra/security-copilot/entra-lifecycle-workflows', date: '2025-09-23', access: full, locator: '''Create step-by-step guidance for a new lifecycle workflow''; ''Troubleshoot the processing results'''}
  last_reviewed: '2026-10-17'
  notes: Documentation only (ms.date 2025-09-23, updated 2026-02-26); no named customers. The same pages are the best source on how override rates could be tracked.
- id: security-identity-access-08
  title: Continuous session-risk evaluation with automated session termination and step-up
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - research-synthesis
  - transaction-processing
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Policies evaluated only at sign-in miss session hijacking and token theft that happen later in the session. Okta cites 1.9 billion session cookies stolen from Fortune 1000 employees in 2022, from a SpyCloud report (OKTA-ITP-2026).
  solution: Okta Identity Threat Protection keeps evaluating the user's session against risk signals (Okta risk engine, device context from Okta Verify and EDR, and third-party signals through the Shared Signals Framework). An entity risk policy can then run a delegated flow, require re-authentication, or end the session across apps through Universal Logout. Microsoft is adding user-risk and device-revocation signals to continuous access evaluation in Global Secure Access (preview, October 2026).
  outcomes:
  - {lever: capacity, description: A customer quote on time freed from threat investigation (organisation not named), figure: hours of daily investigation (qualitative), measures: Quote from an IT Systems Engineer on Okta's product page; no measurement and no organisation named, provenance: vendor-published, source_ref: OKTA-ITP-2026}
  prerequisites:
  - Integrated EDR or other security-event providers that support the Shared Signals Framework
  - Apps configured for Universal Logout
  - A configured entity risk policy per user group and risk level (OKTA-ITPDOCS-2026)
  risks_and_guardrails:
  - 'Response can be graded rather than a block: on-demand MFA, read-only access via Workflows, or session end (OKTA-ITP-2026)'
  - Actions follow policies the customer configures (OKTA-ITPDOCS-2026, 'How it works')
  - 'Residual risk sits in account bootstrapping: attackers who pass weaker enrolment can self-provision their own phishing-resistant factor (OKTA-TI-2026)'
  human_checkpoints:
  - Admins monitor the user risk profile, dashboard and System Log; response flows are delegated to Workflows the customer defines (OKTA-ITPDOCS-2026)
  role_evolution: Okta and Elastic are hiring product and engineering leaders for identity threat detection and response; Elastic's posting asks for fluency in anomaly detection, LLMs and agentic systems and for ownership of a non-human and AI-agent identity roadmap (ELASTIC-JOB-ITDR-2026, 'AI and ML Fluency'; OKTA-JOB-ITP-2026).
  evidence_grade: C
  sources:
  - {ref: OKTA-ITP-2026, title: 'Identity Threat Protection with Okta AI (product page; undated, date shown is retrieval date)', publisher: Okta, type: vendor, url: 'https://www.okta.com/products/identity-threat-protection/', date: '2026-10-17', access: full, locator: 'Product page: benefits, FAQ and customer quote'}
  - {ref: OKTA-ITPDOCS-2026, title: 'Identity Threat Protection (Identity Engine documentation; undated, date shown is retrieval date)', publisher: Okta Help Center, type: vendor, url: 'https://help.okta.com/oie/en-us/content/topics/itp/overview.htm', date: '2026-10-17', access: full, locator: 'Overview: ''How it works''; Benefits; Entity risk policy'}
  - {ref: MSFT-ENTRAWN-2026, title: 'What''s new in Microsoft Entra: October 2026', publisher: 'Microsoft Tech Community, Microsoft Entra Blog', type: vendor, url: 'https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-october-2026/4556460', date: '2026-10-12', access: full, locator: '''Device signals added to Continuous Access Evaluation (CAE) in Global Secure Access'' (public preview)'}
  - {ref: ELASTIC-JOB-ITDR-2026, title: Principal Product Manager - Identity Threat Detection & Response (job posting 8102960), publisher: Elastic, type: job-posting, url: 'https://jobs.elastic.co/jobs?gh_jid=8102960', date: '2026-08-11', access: full, locator: Role summary and 'AI and ML Fluency'}
  - {ref: OKTA-JOB-ITP-2026, title: 'Manager, Engineering - Identity Threat Protection (job posting 8242296)', publisher: Okta, type: job-posting, url: 'https://www.okta.com/company/careers/opportunity/8242296?gh_jid=8242296', date: '2026-10-15', access: full, locator: 'Role summary: ITP ''powered by cutting-edge Okta AI'''}
  - {ref: NIST-IR8587-2026, title: 'NIST IR 8587: Protecting Tokens and Assertions from Forgery, Theft, and Misuse', publisher: NIST, type: standard-setter, url: 'https://csrc.nist.gov/pubs/ir/8587/final', date: '2026-09-15', access: full, locator: 'Abstract: protecting identity tokens, access tokens and assertions from forgery, theft and misuse'}
  last_reviewed: '2026-10-17'
  notes: The documentation describes rules, risk scoring and signal sharing; it does not describe model types, so the 'AI' label comes from Okta's marketing. No named customer or detection-quality figures (false positives, time to revoke) were found. Both pages are undated; date shown is retrieval date.
- id: security-identity-access-09
  title: Managed detection and response extended to SaaS identity threats
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - research-synthesis
  - transaction-processing
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Compromised identities give attackers legitimate access to SaaS applications, which lets them operate without tripping endpoint tools.
  solution: CrowdStrike announced on 2026-09-02 that it is extending Falcon Complete MDR to Falcon Shield, giving 24/7 expert-led monitoring, investigation and response over identity and SaaS signals, using 'high-fidelity detections, agentic workflows, and expert-led operations'.
  outcomes:
  - {lever: risk, description: none published, figure: none published, measures: Announcement only; the post carries a forward-looking-statements notice, provenance: vendor-published, source_ref: CROWDSTRIKE-AGENTICIDP-2026}
  prerequisites:
  - Falcon Shield (SaaS security) within Falcon Next-Gen Identity Security
  risks_and_guardrails:
  - The post says unreleased features may change and buyers should rely on available features (CROWDSTRIKE-AGENTICIDP-2026, 'Forward-Looking Statements')
  human_checkpoints:
  - Response is expert-led (CROWDSTRIKE-AGENTICIDP-2026, MDR section)
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - {ref: CROWDSTRIKE-AGENTICIDP-2026, title: CrowdStrike Announces Agentic Identity Provider, publisher: CrowdStrike, type: vendor, url: 'https://www.crowdstrike.com/en-us/blog/crowdstrike-announces-agentic-identity-provider/', date: '2026-09-02', access: full, locator: Section 'MDR for the Modern SaaS Attack Surface'; 'Forward-Looking Statements'}
  last_reviewed: '2026-10-17'
  notes: Announced only. The same post's main announcement (Agentic IdP for AI agents) is routed to ai-security.
- id: security-identity-access-10
  title: Continuous identity-posture scanning with one-click or automatic remediation of dormant, orphaned and over-privileged access
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Periodic certifications and posture dashboards find stale access after the fact, and dashboards flag risks without fixing them.
  solution: SailPoint's Autonomous Identity Security Posture Management (announced 2026-10-06) uses live identity context to detect dormant accounts, partially offboarded identities, orphaned access, shadow admins and privileged outliers, then remediates from one-click fixes (revoke access, disable an identity, assign an owner) to fully automated policy enforcement. Saviynt (2025-10-15) and Palo Alto Networks' Idira (2026-05-12) describe similar AI-driven discovery and remediation across human and non-human identities.
  outcomes:
  - {lever: risk, description: none published, figure: none published, measures: Announcements carry no outcome figures, provenance: vendor-published, source_ref: SAILPOINT-AUTONOMOUS-2026}
  prerequisites:
  - A unified identity data layer (SailPoint Atlas) with connectors to apps and cloud
  - Policies that define when remediation may run without a person
  risks_and_guardrails:
  - Remediation 'on each organization's terms', from one-click to fully automated, so autonomy is a configured setting (SAILPOINT-AUTONOMOUS-2026, A-ISPM section)
  - SailPoint's own release says features not yet available may not be delivered (SAILPOINT-HUMANFABRIC-2026, forward-looking statements)
  human_checkpoints:
  - One-click remediation leaves the decision with an admin; fully automated enforcement is the opt-in end of the range (SAILPOINT-AUTONOMOUS-2026)
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
  - {ref: SAILPOINT-AUTONOMOUS-2026, title: 'From Chaos to Control: SailPoint Unlocks a Secure Agentic Era with Autonomous Identity Security', publisher: SailPoint, type: vendor, url: 'https://www.sailpoint.com/press-releases/sailpoint-unlocks-a-secure-agentic-era-with-autonomous-identity-security', date: '2026-10-06', access: full, locator: A-ISPM section}
  - {ref: SAVIYNT-AIONB-2025, title: Saviynt Unveils Major AI Capabilities for Identity Security, publisher: Saviynt, type: vendor, url: 'https://saviynt.com/press-release/saviynt-unveils-major-ai-capabilities-for-identity-security', date: '2025-10-15', access: full, locator: '''Secure All Identities'' section'}
  - {ref: PANW-IDIRA-2026, title: 'Palo Alto Networks Introduces Idira: the Next-Generation Identity Security Platform Built for the AI Enterprise', publisher: Palo Alto Networks, type: vendor, url: 'https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-introduces-idira--the-next-generation-identity-security-platform-built-for-the-ai-enterprise', date: '2026-05-12', access: full, locator: '''Discover Identity Risk'' bullet'}
  last_reviewed: '2026-10-17'
  notes: Announcements only. SailPoint's maturity survey (340 leaders) is in module notes.
- id: security-identity-access-11
  title: 'Zero standing privilege: context-based just-in-time grants and revocation for privileged access'
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - transaction-processing
  - software-systems
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Privileged access is still mostly standing. Palo Alto Networks states that 61% of privileged access requests are fulfilled with standing privilege rather than on demand (PANW-IDIRA-2026, opening paragraphs).
  solution: Vendors replace always-on admin rights with access granted for a task, re-evaluated while in use and revoked when risk changes. CrowdStrike (2026-09-02) extends this to Salesforce and GitHub, endpoints and servers, SSH and RDP workloads, and AWS through Entra. Palo Alto Networks' Idira (generally available 2026-05-12) applies zero standing privilege and just-in-time enforcement to every identity. SailPoint (2026-10-06) adds just-in-time provisioning with conditions and effective-privilege visibility.
  outcomes:
  - {lever: risk, description: 'Instacart moved most privileged permissions to automated just-in-time access using a rule-based policy engine (adjacent evidence, not AI)', figure: 95%, measures: Share of Instacart's privileged permissions moved to automated just-in-time access (the page also says 100% of privileged access); not an AI measurement, provenance: vendor-published, source_ref: C1-INSTACART-2024}
  prerequisites:
  - Inventory of privileged entitlements and an access policy engine
  - Context signals (device, threat, business) that can trigger revocation
  risks_and_guardrails:
  - Instacart's rollout kept a 90-day cap and policy-as-code review rather than removing oversight (C1-INSTACART-2024)
  - CrowdStrike's post notes unreleased features are subject to change (CROWDSTRIKE-AGENTICIDP-2026, 'Forward-Looking Statements')
  human_checkpoints:
  - A few sensitive entitlements at Instacart still needed manager approval before the LLM bot (C1-INSTACART-2024)
  role_evolution: Instacart's infrastructure security lead describes the change as freeing highly paid staff engineers from approvals and quarterly reviews (C1-INSTACART-2024, closing section).
  evidence_grade: C
  sources:
  - {ref: PANW-IDIRA-2026, title: 'Palo Alto Networks Introduces Idira: the Next-Generation Identity Security Platform Built for the AI Enterprise', publisher: Palo Alto Networks, type: vendor, url: 'https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-introduces-idira--the-next-generation-identity-security-platform-built-for-the-ai-enterprise', date: '2026-05-12', access: full, locator: Opening paragraphs (61% statistic); 'Control Every Privilege'; availability line}
  - {ref: CROWDSTRIKE-AGENTICIDP-2026, title: CrowdStrike Announces Agentic Identity Provider, publisher: CrowdStrike, type: vendor, url: 'https://www.crowdstrike.com/en-us/blog/crowdstrike-announces-agentic-identity-provider/', date: '2026-09-02', access: full, locator: Section 'Extending Modern Privileged Access Everywhere Work Happens'}
  - {ref: SAILPOINT-AUTONOMOUS-2026, title: 'From Chaos to Control: SailPoint Unlocks a Secure Agentic Era with Autonomous Identity Security', publisher: SailPoint, type: vendor, url: 'https://www.sailpoint.com/press-releases/sailpoint-unlocks-a-secure-agentic-era-with-autonomous-identity-security', date: '2026-10-06', access: full, locator: '''Zero Standing Privilege for humans and machines'' bullet'}
  - {ref: C1-INSTACART-2024, title: 'How Instacart is using AI to achieve zero standing privileges (customer story; undated, year inferred from the BSidesLV24 talk it describes)', publisher: ConductorOne (C1.ai), type: vendor, url: 'https://www.conductorone.com/customers/instacart', date: '2024', access: full, locator: Section 'Automating JIT access with conditional policies'}
  last_reviewed: '2026-10-17'
  notes: 'Grade C: the AI element is marketing language on a mostly rule-based control; the only named measurement (Instacart) is adjacent and not AI. The source and denominator of Palo Alto''s 61% figure are not named in the release. Much of this vendor messaging is about AI-agent privilege (routed to ai-security).'
- id: security-identity-access-12
  title: Agentic onboarding of connected and disconnected applications into identity governance
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - software-systems
  - coordination-scheduling
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Onboarding applications to governance is a long-running bottleneck. Saviynt cites a Ponemon study that 49% of organisations do not track how many disconnected apps they have (SAVIYNT-AIONB-2025).
  solution: Saviynt's Agentic AI Onboarding for Applications (announced 2025-10-15) uses agentic AI to speed integration of connected and disconnected applications across hybrid environments so they come under one governance platform.
  outcomes:
  - {lever: speed, description: none published, figure: none published, measures: The release gives no onboarding time or cost figures, provenance: vendor-published, source_ref: SAVIYNT-AIONB-2025}
  prerequisites:
  - Not described
  risks_and_guardrails:
  - Not described in the release
  human_checkpoints:
  - Not described
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - {ref: SAVIYNT-AIONB-2025, title: Saviynt Unveils Major AI Capabilities for Identity Security, publisher: Saviynt, type: vendor, url: 'https://saviynt.com/press-release/saviynt-unveils-major-ai-capabilities-for-identity-security', date: '2025-10-15', access: full, locator: Section 'Onboard All Applications with Agentic AI'}
  last_reviewed: '2026-10-17'
  notes: Announcement only; no named customer. The 49% figure is Saviynt's citation of a Ponemon study (sample and wording not checked).
- id: security-identity-access-13
  title: Passive, continuous caller authentication in the contact centre in place of knowledge-based questions
  archetype: security
  module: identity-access
  function: customer-service
  work_types:
  - transaction-processing
  - client-interaction
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Agents verify callers with security questions. Stolen breach data lets fraudsters answer them; Pindrop reports that across 2,500 fraud calls at 10 financial institutions fraudsters passed knowledge-based authentication 53% of the time on average (range 9% to 90%). Genuine members get frustrated, and authentication took about 90 seconds of an 8:30-minute call at one credit union (PINDROP-VEC-2025; PINDROP-MSUFCU-2025).
  solution: Pindrop Passport analyses voice, device and behaviour signals in the background of the call to build a profile match, so many callers are verified in the IVR or in seconds with the agent, and agents see risk notifications instead of asking questions. Michigan State University Federal Credit Union uses it in a Five9 contact centre without requiring members to enrol a voiceprint phrase; HealthEquity uses it in its voice channel.
  outcomes:
  - {lever: speed, description: MSUFCU average member authentication time, figure: 90 seconds to 45 seconds (-50%) within 90 days, measures: 'Average member authentication time at MSUFCU, as stated by Pindrop in the case study; call count and measurement method not stated', provenance: vendor-published, source_ref: PINDROP-MSUFCU-2025}
  - {lever: speed, description: MSUFCU calls with a full profile match, figure: 12 seconds (78-second reduction) for more than 40% of calls, measures: Authentication time on calls that achieved a full profile match; more than 40% of calls per Pindrop, provenance: vendor-published, source_ref: PINDROP-MSUFCU-2025}
  - {lever: experience, description: HealthEquity IVR profile match rate in the first month, figure: 31% to 71%, measures: Profile match rate in the IVR within the first month of Passport deployment; denominator (callers or calls) not stated, provenance: vendor-published, source_ref: PINDROP-HEALTHEQUITY-2026}
  - {lever: experience, description: HealthEquity authentication rate with agents, figure: over 91%, measures: 'Authentication rate once callers reach agents, as stated by Pindrop; definition and period not stated', provenance: vendor-published, source_ref: PINDROP-HEALTHEQUITY-2026}
  prerequisites:
  - Contact-centre platform integration (Five9 for MSUFCU) and agent-desktop integration
  - Enrolment/profile data for callers (profile match is built from prior calls)
  risks_and_guardrails:
  - Knowledge-based questions are described as no longer sufficient; HealthEquity moves from one-time 'stage-gate' verification to continuous verification (PINDROP-HEALTHEQUITY-2026)
  - Independent academic work shows cloned voices built from very small samples can bypass commercial speaker verification and anti-spoofing detectors generalise poorly, so voice should not be the only factor (ARXIV-2601.02914, abstract)
  human_checkpoints:
  - Agents receive risk notifications and route elevated-risk calls; low-risk, high-confidence callers move on without questions (PINDROP-HEALTHEQUITY-2026)
  role_evolution: Agents spend less of the call authenticating and more on service; HealthEquity's fraud head frames agents as there to help, not interrogate (PINDROP-HEALTHEQUITY-2026).
  evidence_grade: A
  sources:
  - {ref: PINDROP-MSUFCU-2025, title: Michigan State University Federal Credit Union Cuts Authentication Time in Half with Pindrop, publisher: Pindrop, type: vendor, url: 'https://www.pindrop.com/customer/michigan-state-university-federal-credit-union', date: '2025-01-09', access: full, locator: Opening summary; 'Challenges'; results paragraphs}
  - {ref: PINDROP-HEALTHEQUITY-2026, title: '90% Drop in Fraud and a Smoother CX: How HealthEquity Did It', publisher: Pindrop, type: vendor, url: 'https://www.pindrop.com/customer/healthequity-drop-fraud-smoother-cx', date: '2026-02-23', access: full, locator: Section 'The future of authentication starts with continuous risk assessments'}
  - {ref: PINDROP-VEC-2025, title: The Virginia Employment Commission Reduced Fraud by +$500K Within Months, publisher: Pindrop, type: vendor, url: 'https://www.pindrop.com/customer/virginia-employment-commission-reduced-fraud-within-months', date: '2025-06-13', access: full, locator: '''Before Pindrop Solutions'' (53% KBA pass rate statistic from Pindrop internal data)'}
  - {ref: ARXIV-2601.02914, title: Vulnerabilities of Audio-Based Biometric Authentication Systems Against Deepfake Speech Synthesis (Hong et al.), publisher: arXiv, type: academic, url: 'https://arxiv.org/abs/2601.02914', date: '2026-01-06', access: full, locator: Abstract}
  last_reviewed: '2026-10-17'
  notes: Named organisations with measured results, but every figure is in Pindrop's own case study (provenance vendor-published; the HealthEquity executive quotes are self-reported). No independent test of the deployments. 'AI' is the vendor's label for the risk analysis.
- id: security-identity-access-14
  title: Real-time call risk scoring to catch account-takeover and impersonation fraud in the voice channel
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types:
  - transaction-processing
  - research-synthesis
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Fraud checks in contact centres are slow, run after the fact and rely on knowledge-based quizzes that fraudsters pass. Virginia Employment Commission (VEC) lost an estimated $350M to fraud in three years after the pandemic (PINDROP-VEC-2025, 'Challenges').
  solution: Pindrop Protect scores risk throughout the call, from the IVR to the agent leg, using signals such as spoofing indicators, device anomalies and voice patterns. At VEC the IVR risk score decides whether a caller gets a callback or is routed to a fraud agent, and account-risk analysis links claims sharing addresses or phone numbers. HealthEquity runs it with Passport.
  outcomes:
  - {lever: risk, description: 'HealthEquity voice-channel fraud, year on year', figure: reduced by over 90%, measures: 'Fraud over the voice channel ''from last year to now'', in the words of HealthEquity''s head of fraud; the metric (counts or losses) and period are not defined', provenance: self-reported, source_ref: PINDROP-HEALTHEQUITY-2026}
  - {lever: risk, description: VEC potentially fraudulent calls detected, figure: over 800 in one year, measures: Calls Pindrop Protect flagged as potentially fraudulent in VEC's call centres in a year; not confirmed fraud, provenance: vendor-published, source_ref: PINDROP-VEC-2025}
  - {lever: cost, description: VEC fraud avoided, figure: over $500K within months; nearly $1M annualised (potential), measures: Pindrop's headline and summary of reduced fraudulent claims; basis for the estimate is not shown in the text read, provenance: vendor-published, source_ref: PINDROP-VEC-2025}
  prerequisites:
  - Telephony and IVR integration with real-time risk API
  - A fraud investigation team and case-management process to act on alerts
  - Custom attributes and policy rules for the organisation's own fraud patterns (PINDROP-VEC-2025)
  risks_and_guardrails:
  - VEC wanted to balance fraud detection with low friction for genuine claimants (PINDROP-VEC-2025)
  - 'Detection models for synthetic speech generalise poorly outside their training conditions: a multilingual in-the-wild benchmark shows significant degradation across languages and acoustic conditions, and an audit finds deepfake benchmarks may reward general representation quality (ARXIV-2603.05852, abstract; ARXIV-2606.26384, abstract)'
  human_checkpoints:
  - Agents see colour codes and screen pops; high-risk IVR calls go to a fraud agent; investigators run cases from the flagged call (PINDROP-VEC-2025)
  role_evolution: Contact-centre leadership moves from reviewing suspicious callbacks after the fact to setting real-time risk policies; VEC built case tracking through custom attributes (PINDROP-VEC-2025).
  evidence_grade: A
  sources:
  - {ref: PINDROP-HEALTHEQUITY-2026, title: '90% Drop in Fraud and a Smoother CX: How HealthEquity Did It', publisher: Pindrop, type: vendor, url: 'https://www.pindrop.com/customer/healthequity-drop-fraud-smoother-cx', date: '2026-02-23', access: full, locator: Quote 'we've reduced fraud over the voice channel by over 90%'; key results}
  - {ref: PINDROP-VEC-2025, title: The Virginia Employment Commission Reduced Fraud by +$500K Within Months, publisher: Pindrop, type: vendor, url: 'https://www.pindrop.com/customer/virginia-employment-commission-reduced-fraud-within-months', date: '2025-06-13', access: full, locator: Opening summary; 'ROI' sections; 'Fraud detection in the IVR'}
  - {ref: ARXIV-2603.05852, title: 'ML-ITW: A Multilingual in-the-wild Benchmark for Speech Deepfake Detection (Li et al.)', publisher: arXiv, type: academic, url: 'https://arxiv.org/abs/2603.05852', date: '2026-03-06', access: full, locator: Abstract}
  - {ref: ARXIV-2606.26384, title: 'What Do Deepfake Benchmarks Measure? An Audit Using Frozen Self-Supervised Representations (Pagon et al.)', publisher: arXiv, type: academic, url: 'https://arxiv.org/abs/2606.26384', date: '2026-06-24', access: full, locator: Abstract}
  last_reviewed: '2026-10-17'
  notes: Named organisations (HealthEquity, VEC) with figures, all via Pindrop's customer stories. VEC's $500K is the vendor's headline and its derivation was not found. No independent evaluation of detection error rates in these deployments.
- id: security-identity-access-15
  title: Synthetic-voice detection on contact-centre and meeting audio, with risk scores for triage
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - transaction-processing
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: A tier-one global bank saw deepfaked calls pass voice biometrics and callback checks (REALITYDEFENDER-BANK-2026). The FBI reports AI-generated voice messages used to impersonate senior US officials (FBI-IC3-2025).
  solution: Reality Defender analysed recorded customer calls across Zoom, Meet, NICE, Twilio and Five9, then moved to real-time detection for about 600 frontline staff. It returns probability-based risk scores per file rather than a binary result, which the bank's fraud team uses to triage and escalate against its own thresholds.
  outcomes:
  - {lever: risk, description: Synthetic voice calls found among calls analysed, figure: about 960 of more than 1.7 million, measures: 'Synthetic voice calls detected (Reality Defender''s figure, about 960) in more than 1.7M customer calls analysed in 2024 across US and LATAM operations; not confirmed fraud', provenance: vendor-published, source_ref: REALITYDEFENDER-BANK-2026}
  prerequisites:
  - Integration with the bank's call-recording and conferencing platforms
  - A triage and escalation process for scored calls
  risks_and_guardrails:
  - Scores are probabilities, not verdicts; thresholds are set by the bank (REALITYDEFENDER-BANK-2026)
  - Academic evidence that detectors degrade out of domain (ARXIV-2603.05852; ARXIV-2606.26384)
  - The FBI recommends verifying contacts independently through a known channel and not relying on spotting AI voices by ear (FBI-IC3-2025, Recommendations)
  human_checkpoints:
  - Fraud analysts triage scored calls; new internal process for escalation (REALITYDEFENDER-BANK-2026, 'Key Results')
  role_evolution: Frontline staff receive detection results in real time; fraud and risk teams own a new triage process (REALITYDEFENDER-BANK-2026).
  evidence_grade: C
  sources:
  - {ref: REALITYDEFENDER-BANK-2026, title: 'How a Global Bank Mitigates Contact Center Deepfake Threats with Reality Defender (anonymised case study; date is sitemap last-modified, publication date not shown)', publisher: Reality Defender, type: vendor, url: 'https://www.realitydefender.com/case-studies/how-a-global-bank-mitigates-contact-center-deepfake-threats-with-reality-defender', date: '2026-07-26', access: full, locator: Key Results; 'How Reality Defender Exposed AI Voice Threats'}
  - {ref: FBI-IC3-2025, title: Senior US Officials Impersonated in Malicious Messaging Campaign (Alert I-051525-PSA), publisher: FBI Internet Crime Complaint Center, type: regulator, url: 'https://www.ic3.gov/PSA/2025/PSA250515', date: '2025-05-15', access: full, locator: Campaign details; Recommendations}
  - {ref: PINDROP-DRI-2026, title: The Deepfake Readiness Index 2026 (survey of 250 U.S. security leaders; date is sitemap last-modified), publisher: Pindrop, type: survey, url: 'https://www.pindrop.com/resources/report/deepfake-readiness-index', date: '2026-09-29', access: full, locator: Key statistics (survey of 250 U.S. security leaders)}
  last_reviewed: '2026-10-17'
  notes: 'Grade C: the bank is anonymised, so there is no named organisation. A vendor page elsewhere cites 99.99% detection accuracy (search result only, not used as evidence). Pindrop''s survey (vendor-published, 250 U.S. security leaders): 37% rely on legacy tools for deepfake detection and 1 in 4 organisations hit by a deepfake attack lost $1M or more in a single incident (PINDROP-DRI-2026).'
- id: security-identity-access-16
  title: Machine-learning identity verification with liveness and deepfake or injection detection for sign-up, account recovery and high-risk actions
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - transaction-processing
  pattern: document-to-decision
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Forged documents, presentation attacks and injected deepfake video defeat one-time checks. FinCEN reports an increase in suspicious-activity reports describing deepfake media used to get past identity verification (FINCEN-DEEPFAKE-2024, p. 1).
  solution: Coinbase's identity verification team owns ML systems for document authenticity, 1:1 and 1:N face match, liveness, presentation-attack and deepfake/injection detection, plus a Coinbase-owned evaluation set to benchmark outside vendors and route between providers. The posting says every signup, account recovery and high-risk action depends on these models. NIST SP 800-63-4 (July 2025) adds controls for injection attacks and forged media.
  outcomes:
  - {lever: quality, description: 'DHS test: median presentation-attack detection among tested subsystems', figure: '78% of more than 1,200 attacks (best 100%, worst 0%)', measures: 'Share of presentation attacks detected by the median tested subsystem in DHS S&T''s Remote Identity Validation Technology Demonstration (2023 event); vendors'' systems, not Coinbase''s', provenance: independent, source_ref: DHS-RIVTD-2025}
  - {lever: quality, description: 'DHS test: usable-by-genuine-users rate of active presentation-attack detection', figure: 'median 85% of more than 600 bona fide users validated (best 94%, worst 41%)', measures: Share of bona fide users validated by the median of 6 active PAD subsystems; median error 9% for ages 18-45 and 20% for 46+, provenance: independent, source_ref: DHS-RIVTD-2025}
  prerequisites:
  - Vendor and in-house models benchmarked on an owned evaluation set
  - Device, document and compatibility testing across phones and issuing states (DHS-RIVTD-2025)
  risks_and_guardrails:
  - DHS recommends choosing systems with error rates below 10% and checking compatibility with users' documents and devices; errors varied by state of issue and by smartphone (DHS-RIVTD-2025, results)
  - FinCEN lists MFA including phishing-resistant MFA and live verification as best practices, notes criminals may avoid live checks, and lists declining MFA as a red flag (FINCEN-DEEPFAKE-2024, pp. 4-6)
  - Older users had higher error rates (median 20% vs 9%), a fairness and access risk (DHS-RIVTD-2025)
  human_checkpoints:
  - Not described in the posting; threshold tuning and 'production enforcement' sit with the ML team (COINBASE-JOB-IDVML-2026)
  role_evolution: Identity verification ML engineers own vendor benchmarking, routing and evaluation layers, not only models (COINBASE-JOB-IDVML-2026, 'What you'll do').
  evidence_grade: B
  sources:
  - {ref: COINBASE-JOB-IDVML-2026, title: 'Staff Machine Learning Engineer (Platform - Identity), Identity Verification (job posting 8211486)', publisher: Coinbase, type: job-posting, url: 'https://www.coinbase.com/careers/positions/8211486?gh_jid=8211486', date: '2026-09-17', access: full, locator: Role description and 'What you'll do'}
  - {ref: DHS-RIVTD-2025, title: 'Remote Identity Validation Technology Demonstration (DHS S&T; page last updated 2025-04-10, results summarised from the 2023 test event)', publisher: 'U.S. Department of Homeland Security, Science and Technology Directorate', type: regulator, url: 'https://www.dhs.gov/science-and-technology/remote-identity-validation-technology-demonstration', date: '2025-04-10', access: full, locator: 'Results infographics: Document Validation; Selfie Match; Presentation Attack Detection'}
  - {ref: NIST-SP80063-4-2025, title: 'NIST SP 800-63 Digital Identity Guidelines, Revision 4 (landing page)', publisher: NIST, type: standard-setter, url: 'https://pages.nist.gov/800-63-4/', date: 2025-07, access: full, locator: 'Background: revision 4 changes (injection attacks, forged media, fraud requirements)'}
  - {ref: FINCEN-DEEPFAKE-2024, title: FinCEN Alert on Fraud Schemes Involving Deepfake Media Targeting Financial Institutions (FIN-2024-Alert004), publisher: 'FinCEN, U.S. Treasury', type: regulator, url: 'https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf', date: '2024-11-13', access: full, locator: p. 1 (increase in SARs); p. 4 (best practices); p. 5-6 (red flags)}
  - {ref: INCODE-MONEY2020-2026, title: 'A Year on the Front Line of Deepfake Fraud: What We''re Bringing to Money 20/20', publisher: Incode, type: vendor, url: 'https://www.incode.com/blog/a-year-on-the-front-line-of-deepfake-fraud-what-we-re-bringing-to-money-2020', date: '2026-06-01', access: full, locator: 'Panel announcement: ''Fighting Deepfakes: A Bank''s Year on the Front Line'' (Money 20/20 Europe)'}
  last_reviewed: '2026-10-17'
  notes: 'Grade B with a cap: the Coinbase evidence is a job posting (named, in production, no measurements), and the only measurements are independent tests of other vendors'' technology on a 2023 test event (page updated 2025-04-10). The DHS summaries cover 12 document-validation systems, 16 selfie-match systems and 6 active plus 15 passive PAD subsystems as shown in the infographics.'
- id: security-identity-access-17
  title: Self-service identity verification for help-desk account recovery, triggered from an AI service chatbot
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - transaction-processing
  - review-assurance
  pattern: service-agent-escalation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: At Cisco, account recovery meant a help-desk agent opened a case, scheduled a video call, looked at the employee's face and ID and made a judgement. Practice varied across teams, and Cisco says social engineering such as Scattered Spider made individual agent judgement a risk (PERSONA-CISCO-2026, 'Problem').
  solution: 'When an employee locked out of Duo contacts AISERA, Cisco''s AI-powered IT service management chatbot, it triggers a Persona flow: government ID and selfie verification, after which the employee adds a working factor. Cisco also uses Persona for IAL2-compliant verification of US persons in a federal-contract division and plans to verify Duo admins before sensitive actions later in 2026.'
  outcomes:
  - {lever: speed, description: Time for an employee to regain access, figure: from a three-to-four-hour wait for an agent to as little as five minutes, measures: Cisco principal engineer's description of ticket response time before vs self-service verification time after; not a measured average, provenance: vendor-published, source_ref: PERSONA-CISCO-2026}
  - {lever: capacity, description: Cisco's stated aim for automated cases, figure: 'hopes to automate thousands of support cases each quarter (goal, not a result)', measures: Cisco's stated hope as reported by Persona; no count of cases automated is given, provenance: vendor-published, source_ref: PERSONA-CISCO-2026}
  prerequisites:
  - Vendor selection by RFP and proof of concept (Cisco shortlisted six vendors, two finalists)
  - Integration between the service chatbot, Persona and Duo
  - Role-based case views so support agents see only what they need
  risks_and_guardrails:
  - Persona's access to Duo is limited to what verification needs; support agents see only failed cases and guidance (PERSONA-CISCO-2026)
  - Okta's research recommends phishing-resistant verification, managed devices and third-party identity verification in account-management policies to stop attackers adding their own factors (OKTA-TI-2026)
  - Image-based verification can be attacked with deepfake injection; see use case 16 for independent test data
  human_checkpoints:
  - Failed verifications go to support agents for guidance (PERSONA-CISCO-2026)
  - Duo admin verification is planned, not live, as of the story
  role_evolution: Help-desk agents spend less time on verification calls and more on complex cases; one process replaces team-by-team practice (PERSONA-CISCO-2026, 'Results').
  evidence_grade: A
  sources:
  - {ref: PERSONA-CISCO-2026, title: 'How Cisco Automated Workforce Verification With Persona (customer story; undated, text refers to a use case planned for later in 2026)', publisher: Persona, type: vendor, url: 'https://withpersona.com/customers/cisco', date: '2026', access: full, locator: 'Sections ''Problem'', ''Solution'' and ''Results'''}
  - {ref: OKTA-TI-2026, title: 'New speed, same tricks: Defend against AI threats with security fundamentals (B. Winterford, Okta Threat Intelligence)', publisher: Okta Newsroom, type: vendor, url: 'https://www.okta.com/newsroom/articles/new-speed-same-tricks-defend-against-ai-threats-with-security-fundamentals/', date: '2026-10-07', access: full, locator: Section on Account Management Policies and bootstrapping}
  last_reviewed: '2026-10-17'
  notes: Named organisation, measured in terms of waiting time, but the figure is a quote in a vendor story; the page is undated (2026 inferred from 'later in 2026'). The AI parts are the chatbot (AISERA) and the ML-based document and face checks.
- id: security-identity-access-18
  title: Identity-graph and behavioural models to find account rings, bots and takeover at onboarding and in session
  archetype: security
  module: identity-access
  function: risk-compliance-legal
  work_types:
  - research-synthesis
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Fraud rings reuse biometric, device and document signals across accounts, and bots mimic humans. Cloudflare lists fraudulent signups, promo and trial abuse, payment fraud, chargebacks and account takeover as costs to revenue and support overhead (CLOUDFLARE-JOB-FRAUD-2026).
  solution: Coinbase builds identity-graph systems with graph neural networks that cluster accounts sharing biometric, device and document signals, plus behavioural and device models for capture-session anomalies, bot-vs-human classification and device-fingerprint risk scoring at real-time latency. Cloudflare's internal fraud platform team, built around data-science signals and models, is hiring its first software engineer to ingest events from billing, signup and support, route decisions and put case data in front of the people who act on them.
  outcomes:
  - {lever: risk, description: none published, figure: none published, measures: Job postings carry no outcome data, provenance: self-reported, source_ref: COINBASE-JOB-IDVML-2026}
  prerequisites:
  - Event feeds from signup, billing and support systems
  - A decisioning and case-management platform
  risks_and_guardrails:
  - Not described beyond the posting's use of generative AI 'with human oversight' wording
  human_checkpoints:
  - Decisions and case data are routed to the people who act on them (CLOUDFLARE-JOB-FRAUD-2026)
  role_evolution: Fraud teams add platform engineers to turn data-science models into operations (CLOUDFLARE-JOB-FRAUD-2026, 'About the Role').
  evidence_grade: B
  sources:
  - {ref: COINBASE-JOB-IDVML-2026, title: 'Staff Machine Learning Engineer (Platform - Identity), Identity Verification (job posting 8211486)', publisher: Coinbase, type: job-posting, url: 'https://www.coinbase.com/careers/positions/8211486?gh_jid=8211486', date: '2026-09-17', access: full, locator: '''What you''ll do'': identity-graph and behavioural models'}
  - {ref: CLOUDFLARE-JOB-FRAUD-2026, title: 'Senior Software Engineer, Internal Fraud Platform (job posting 8185561)', publisher: Cloudflare, type: job-posting, url: 'https://boards.greenhouse.io/cloudflare/jobs/8185561?gh_jid=8185561', date: '2026-09-14', access: full, locator: '''About the Role'''}
  last_reviewed: '2026-10-17'
  notes: 'Grade B from job postings only: named firms, no measurements. Whether these models are in production at each firm is inferred from the postings'' wording (Coinbase: ''protecting the integrity of millions of accounts''; Cloudflare: team ''built around data science'').'
- id: security-identity-access-19
  title: IAM engineers building identity automation with AI coding tools and LLMs
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - software-systems
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: IAM teams run SSO integrations, SCIM provisioning, role models, certification and privileged-access platforms with small staffs and many applications.
  solution: Cloudflare's IAM postings require hands-on engineering experience 'leveraging AI/LLMs to solve operational or technical challenges' and expect engineers to use AI tools from code generation to debugging 'and bring the judgment to know when to trust them'. Coinbase's IAM posting says staff use generative AI responsibly with human oversight to improve workflow efficiency, cost and quality.
  outcomes:
  - {lever: capacity, description: none published, figure: none published, measures: Job postings carry no outcome data, provenance: self-reported, source_ref: CLOUDFLARE-JOB-IAM-2026}
  prerequisites:
  - Production-grade automation scripting skills; judgement on when AI output is trustworthy
  risks_and_guardrails:
  - Human oversight of generative AI output is required wording at Coinbase (COINBASE-JOB-IAM-2026)
  human_checkpoints:
  - Engineers review and own AI-assisted changes (CLOUDFLARE-JOB-IAMSYS-2026, 'AI-assisted development')
  role_evolution: AI use is now a stated hiring requirement for IAM engineering roles at Cloudflare (CLOUDFLARE-JOB-IAM-2026, 'Desirable skills').
  evidence_grade: B
  sources:
  - {ref: CLOUDFLARE-JOB-IAM-2026, title: IAM Security Engineer (job posting 8157997), publisher: Cloudflare, type: job-posting, url: 'https://boards.greenhouse.io/cloudflare/jobs/8157997?gh_jid=8157997', date: '2026-09-11', access: full, locator: '''Desirable skills, knowledge and experience'''}
  - {ref: CLOUDFLARE-JOB-IAMSYS-2026, title: 'Senior Systems Engineer, Identity & Access Management (job posting 8104955)', publisher: Cloudflare, type: job-posting, url: 'https://boards.greenhouse.io/cloudflare/jobs/8104955?gh_jid=8104955', date: '2026-08-06', access: full, locator: '''AI-assisted development'' requirement'}
  - {ref: COINBASE-JOB-IAM-2026, title: 'Senior Staff Software Engineer, Platform - IAM (job posting 8155366)', publisher: Coinbase, type: job-posting, url: 'https://www.coinbase.com/careers/positions/8155366?gh_jid=8155366', date: '2026-09-09', access: full, locator: Role summary and generative-AI sentence}
  last_reviewed: '2026-10-17'
  notes: 'Pattern is ''other'': engineers use AI coding assistants and LLMs to build identity automation. Evidence of expectations, not measured productivity. Cloudflare''s postings were published 2026-08-06 and 2026-09-11; both were still open when checked on 2026-10-17 (updated 2026-10-13).'
- id: security-identity-access-20
  title: Translating natural-language access requirements into verified policy-as-code
  archetype: security
  module: identity-access
  function: technology-it
  work_types:
  - software-systems
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Access requirements are written in prose and must be turned into enforceable policies such as OPA Rego or Cedar; the RAISE authors say even frontier LLMs often produce policies that violate the intended authorisation semantics (ARXIV-2609.33796, abstract).
  solution: 'Idea under study: an LLM drafts policy code, then schema validation, linting, compilation and generated positive and negative tests (or a formal verifier) check it before a person reviews it. Two September 2026 papers test this.'
  outcomes:
  - {lever: quality, description: End-to-end correctness of generated Rego policies vs a single-prompt baseline, figure: 50.3% vs 15.3%, measures: 'Share of 372 access-control statements for which generated Rego compiled, linted and passed positive and negative tests (strict measure of deployable correctness), structured pipeline vs single prompt', provenance: independent, source_ref: ARXIV-2609.24036}
  - {lever: quality, description: 'Cedar policy synthesis: a small tuned model against zero-shot frontier models', figure: +13.33 and +16.26 percentage points over two named zero-shot models, measures: 'Semantic success on held-out scenarios in the authors'' CedarInstruct data (5,800 scenarios), as stated in the abstract', provenance: independent, source_ref: ARXIV-2609.33796}
  prerequisites:
  - A verifier or test harness for the target policy language
  - Annotated access-control statements
  risks_and_guardrails:
  - Authors report that untrained models rarely write valid Cedar (ARXIV-2609.33796, abstract) and that a direct single prompt is correct only 15.3% of the time on their test (ARXIV-2609.24036, abstract)
  human_checkpoints:
  - Not studied; both papers measure automated checks, not human review
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - {ref: ARXIV-2609.24036, title: 'Structured Decomposition for Reliable LLM-Generated Access Control Policies (Gupta, Sreenivasamurthy)', publisher: arXiv, type: academic, url: 'https://arxiv.org/abs/2609.24036', date: '2026-09-21', access: full, locator: Abstract}
  - {ref: ARXIV-2609.33796, title: 'RAISE: Reinforcing Access Control Policy Synthesis in LLMs via Symbolic Evaluation (Zhou, Vatsa, Eiers)', publisher: arXiv, type: academic, url: 'https://arxiv.org/abs/2609.33796', date: '2026-09-27', access: full, locator: Abstract}
  last_reviewed: '2026-10-17'
  notes: 'Idea (research only): no deployment found. Both are preprints and results come from the authors'' own datasets. Microsoft''s Copilot offers a product form of the idea for lifecycle workflows (use case 07) but not verified policy generation.'
```

## 3. Module notes

### Processes and key steps (work types)

- **Joiner, mover, leaver provisioning and lifecycle workflows** (transaction-processing): triggered from HR data; Entra lifecycle workflows and Copilot guidance are one example (`MSFT-LIFECYCLE-2026`).
- **Access request and approval** (transaction-processing, expert-judgment): request, context lookup, approval, provisioning; automated at Instacart (use case 05), conversational at Okta (06).
- **Access certification and review** (review-assurance): campaign set-up, reviewer decisions, remediation, audit evidence (04, 07, 10).
- **Policy design and tuning** (software-systems): Conditional Access, role models, authorisation policy-as-code (01, 20).
- **Privileged access** (transaction-processing, software-systems): vaulting, just-in-time elevation, revocation (11).
- **Authentication and credential lifecycle** (transaction-processing): MFA and passkey roll-out, account recovery, help-desk verification (02, 17).
- **Identity threat detection and response** (research-synthesis, monitor-diagnose-act): risk scoring, session revocation, investigation (03, 08, 09).
- **Identity proofing and verification** (review-assurance): documents, face match, liveness, deepfake/injection detection (16).
- **Contact-centre authentication and fraud/impersonation detection** (transaction-processing): caller authentication, risk scoring, synthetic-voice detection (13, 14, 15, 18).

### Common pain points

- Reviewers approving by default. Lumos calls it 'rubber stamping' and Instacart's security lead says managers across the industry probably approve close to 100% of the time; both are unmeasured claims (`LUMOS-UAR-2025`, `C1-INSTACART-2024`).
- Knowledge-based authentication no longer separates fraudsters from customers: fraudsters passed it 53% of the time on average in 2,500 fraud calls Pindrop analysed at 10 financial institutions (Pindrop internal data, `PINDROP-VEC-2025`).
- Fragmented, weak authentication: in the Yubico/Okta survey (nearly 2,000 respondents, nine countries), 76% of organisations use fragmented authentication methods across internal apps and 52% of respondents received username-and-password credentials when they started their roles (`OKTA-AUTHSURVEY-2026`).
- Help-desk bottlenecks and inconsistent verification (Cisco: three to four hours for an agent to respond, `PERSONA-CISCO-2026`).
- Policy sprawl and coverage gaps in Conditional Access (`MSFT-CAUPDATE-2025`).
- Application onboarding: Saviynt cites a Ponemon finding that 49% of organisations do not track their disconnected apps (`SAVIYNT-AIONB-2025`).

### Metrics and benchmarks (with sources)

- Conditional Access agent: 26 gaps per customer per month; 73% of customers made meaningful improvements; more than 83% of preview customers got actionable recommendations (`MSFT-CAUPDATE-2025`, `MSFT-ENTRAGA-2025`; vendor-published, denominators not given).
- Contact centre: authentication time 90 to 45 seconds (`PINDROP-MSUFCU-2025`); IVR profile match 31% to 71% and fraud down over 90% (`PINDROP-HEALTHEQUITY-2026`); 800+ flagged calls (`PINDROP-VEC-2025`).
- Account recovery: hours to as little as five minutes (`PERSONA-CISCO-2026`).
- Independent identity-validation test (DHS S&T, 2023 event): recommends error rates below 10%; median presentation-attack subsystem detected 78% of attacks, screen and printout attacks succeeded with error rates up to 88% on some systems (median 2%) (`DHS-RIVTD-2025`).
- Okta threat-intelligence counterfactual on about 6,000 events: 87% of account-takeover sessions involved passwords; mandatory phishing-resistant enrolment could have stopped 88% and app sign-in enforcement 99.75%; 0.25% remained because of account bootstrapping (`OKTA-TI-2026`; vendor-published).
- Okta/Yubico survey: 44% reported at least one successful AI-driven attack, 43% saw suspicious video, voice or phone impersonation of executives or clients, and only 36% of security professionals correctly identified the human-written message (`OKTA-AUTHSURVEY-2026`).
- SailPoint Horizons (340 senior identity, IT, cybersecurity and risk leaders): 87% rate human IAM capabilities as capable or better while 43% report mature processes for agentic access; 43% feel prepared to produce verifiable evidence in an AI-related audit; human-identity programmes at the lowest maturity tier fell from 45% (2022) to 23% (`SAILPOINT-HORIZONS-2026`; vendor survey).
- Pindrop survey of 250 U.S. security leaders: 37% rely on legacy tools for deepfake detection (`PINDROP-DRI-2026`; vendor survey).
- Verizon's 2026 DBIR landing page says 31% of breaches now start with software vulnerabilities, ahead of stolen passwords as the top entry route; only the landing page was read, so the denominator and definitions are unchecked (`VERIZON-DBIR-2026`).

### Guardrails and regulatory points

- **NIST SP 800-63-4** (final July 2025): recommended continuous evaluation metrics, expanded fraud requirements for identity proofing, controls for injection attacks and forged media (deepfakes), and syncable authenticators such as synced passkeys (`NIST-SP80063-4-2025`).
- **FinCEN alert FIN-2024-Alert004** (2024-11-13): financial institutions should reference the alert in SARs; best practices include MFA (including phishing-resistant MFA) and live audio or video verification; red flags include a customer declining MFA (`FINCEN-DEEPFAKE-2024`).
- **FBI IC3 (2025-05-15):** AI-generated voice messages used to impersonate senior US officials; verify contacts through a separately confirmed channel (`FBI-IC3-2025`).
- **NIST IR 8587 (2026-09-15) with CISA:** token and assertion protection for federal cloud identity systems, building on SP 800-53 control IA-13 (`NIST-IR8587-2026`, `CISA-IR8587-2026`).
- **Product-level controls:** report-only policies, explicit admin approval, role separation, audit logs and fixed agent permissions in Microsoft's agent (`MSFT-CAAGENT-2026`, `MSFT-ENTRAAGENTS-2026`); score-then-threshold design and full audit trail in Instacart's bot (`C1-INSTACART-2024`).
- DHS S&T advises deployers to check compatibility with users' documents and devices because errors varied by state of issue and by smartphone (`DHS-RIVTD-2025`).

### Frontier signals (dated, sourced)

- 2026-10-06: SailPoint announces Autonomous Agents, autonomous identity security posture management, just-in-time provisioning with conditions, conversational access requests and proactive separation-of-duties blocking at request time (`SAILPOINT-AUTONOMOUS-2026`, `SAILPOINT-HUMANFABRIC-2026`).
- 2026-09-22: Okta announces Okta for AI Agents updates and the Blueprint Alliance (`OKTA-AGENTS-2026`); 2026-09-02: CrowdStrike announces an Agentic Identity Provider, modern privileged access across SaaS, endpoints and cloud, and Falcon Complete MDR for SaaS identity (`CROWDSTRIKE-AGENTICIDP-2026`).
- 2026-08-04: SailPoint makes Agentic Fabric generally available and moves human governance toward continuous, real-time posture (`SAILPOINT-IDSEC-2026`).
- 2026-06-15: Saviynt adds biometric and liveness identity verification inside human identity certification (`SAVIYNT-IARA-2026`).
- 2026-05-12: Palo Alto Networks launches Idira on top of CyberArk, with zero standing privilege for every identity (`PANW-IDIRA-2026`).
- 2026-05-22 (docs): Microsoft's agent plans passkey adoption campaigns for administrators (`MSFT-PASSKEYCAMP-2026`).
- 2026-10-12: Microsoft reorganises its monthly Entra 'what's new' around customer outcomes, and says people and AI agents now both act for the business (`MSFT-ENTRAWN-2026`).
- 2026-10-07: Okta Threat Intelligence argues AI is an accelerant of existing attack methods, so fundamentals still apply (`OKTA-TI-2026`).

### Workforce and role effects

- IAM engineers are asked to use AI/LLMs for automation (Cloudflare postings, `CLOUDFLARE-JOB-IAM-2026`, `CLOUDFLARE-JOB-IAMSYS-2026`); Coinbase's IAM lead role covers one platform for human, AI-agent, service and workload identity across 700+ internal systems (`COINBASE-JOB-IAM-2026`).
- Product and engineering leadership for identity threat detection is being hired with AI/ML fluency (`ELASTIC-JOB-ITDR-2026`, `OKTA-JOB-ITP-2026`).
- Approvals move from managers and staff engineers to bots and policy code (`C1-INSTACART-2024`); administrators review agent suggestions rather than policy logic (`MSFT-CAAGENT-2026`); help-desk agents hand verification to a self-service flow (`PERSONA-CISCO-2026`).
- Fraud engineering postings now state that most pull requests are co-authored with AI (`AFFIRM-JOB-FRAUD-2026`, adjacent, routed).

### Objections and concerns practitioners raise

- Generative AI is not yet reliable enough for objective access decisions, so Instacart keeps the decision in a computed score (`C1-INSTACART-2024`).
- Voice biometrics can be bypassed by clones from small samples and deepfake detectors generalise poorly (`ARXIV-2601.02914`, `ARXIV-2603.05852`, `ARXIV-2606.26384`).
- Humans cannot be the control: only 36% correctly identified the human-written message in the Okta/Yubico test (`OKTA-AUTHSURVEY-2026`).
- Human-in-the-loop for high-stakes agent actions: 91% of respondents insist on it (`OKTA-AUTHSURVEY-2026`; routed context).
- Vendor concentration and cost: the Entra agent bills at least one SCU a month whether used or not (`MSFT-CAAGENT-2026`); Okta warns of a 'tool tax' on tokens (`OKTA-DEX-2026`).
- Audit evidence: only 43% feel prepared to produce verifiable evidence in an AI-related audit (`SAILPOINT-HORIZONS-2026`).

### Interview probes for an advisor

1. When an access request or review item reaches an approver today, what context do they see, what share is approved unchanged, and do you record overrides of any system recommendation?
2. If an LLM or agent drafted or approved low-risk requests, what data would it need (HR, usage, entitlement descriptions), what score or threshold would your auditors accept, and who owns the audit trail?
3. How does your help desk verify a person who has lost a factor? What would you do if voice and video can no longer be trusted, and who can override the process?
4. Which risk signals may trigger an automatic session revocation or step-up today, and which actions still need a person?
5. What would you measure to know an AI step in identity is working: coverage gaps found and closed, review completion time, recovery time, false positives?

## 4. Routed to other modules

- **ai-security (agent identity, authorisation and containment):** CrowdStrike Agentic IdP and Continuous Identity for AI Agents (`CROWDSTRIKE-AGENTICIDP-2026`); Okta for AI Agents, Agent Gateway, kill switch and Blueprint Alliance (`OKTA-AGENTS-2026`); World Central Kitchen (`OKTA-WCK-2026`); Okta's Dex agent registration in Universal Directory and tool scoping (`OKTA-DEX-2026`); SailPoint Agentic Fabric and Autonomous Agents (`SAILPOINT-IDSEC-2026`, `SAILPOINT-AUTONOMOUS-2026`); Saviynt Agent Access Gateway and intent-aware runtime authorisation (`SAVIYNT-IARA-2026`); Palo Alto Networks' agentic identity parts of Idira (`PANW-IDIRA-2026`); Microsoft Entra Agent ID permissions on the Entra agents (`MSFT-ENTRAAGENTS-2026`); SailPoint Horizons agent figures such as 79% running agents in production and 2% with purpose-built tools (`SAILPOINT-HORIZONS-2026`); Okta/Yubico agent-governance questions (`OKTA-AUTHSURVEY-2026`); Okta's internal Identity team role (`OKTA-JOB-IDENG-2026`).
- **human-risk (scams, deepfakes, impersonation awareness):** FBI warning on AI voice impersonation (`FBI-IC3-2025`); Okta/Yubico finding that people cannot reliably spot AI-written messages (`OKTA-AUTHSURVEY-2026`); Pindrop's deepfake readiness survey (`PINDROP-DRI-2026`).
- **operations (SOC):** Falcon Complete MDR for SaaS identity as a managed-detection service (`CROWDSTRIKE-AGENTICIDP-2026`); identity telemetry feeding SIEM (seen only in index listings, not read).
- **governance-risk:** NIST SP 800-63-4, FinCEN alert and NIST IR 8587 as constraints on how identity AI can be deployed (`NIST-SP80063-4-2025`, `FINCEN-DEEPFAKE-2024`, `NIST-IR8587-2026`).
- **vulnerability-exposure:** the DBIR landing-page claim that vulnerabilities now lead stolen passwords as an entry route (`VERIZON-DBIR-2026`).
- **Out of this module (transaction fraud, no clear home):** Affirm's real-time transaction fraud engineering, where 'most PRs are co-authored with AI' (`AFFIRM-JOB-FRAUD-2026`).

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| `AFFIRM-JOB-FRAUD-2026` | Senior Software Engineer, Back-end (Fraud) (job posting 7806679003) | Affirm | job-posting | https://job-boards.greenhouse.io/affirm/jobs/7806679003 | 2026-07-20 | full |
| `ARXIV-2601.02914` | Vulnerabilities of Audio-Based Biometric Authentication Systems Against Deepfake Speech Synthesis (Hong et al.) | arXiv | academic | https://arxiv.org/abs/2601.02914 | 2026-01-06 | full |
| `ARXIV-2603.05852` | ML-ITW: A Multilingual in-the-wild Benchmark for Speech Deepfake Detection (Li et al.) | arXiv | academic | https://arxiv.org/abs/2603.05852 | 2026-03-06 | full |
| `ARXIV-2606.26384` | What Do Deepfake Benchmarks Measure? An Audit Using Frozen Self-Supervised Representations (Pagon et al.) | arXiv | academic | https://arxiv.org/abs/2606.26384 | 2026-06-24 | full |
| `ARXIV-2609.24036` | Structured Decomposition for Reliable LLM-Generated Access Control Policies (Gupta, Sreenivasamurthy) | arXiv | academic | https://arxiv.org/abs/2609.24036 | 2026-09-21 | full |
| `ARXIV-2609.33796` | RAISE: Reinforcing Access Control Policy Synthesis in LLMs via Symbolic Evaluation (Zhou, Vatsa, Eiers) | arXiv | academic | https://arxiv.org/abs/2609.33796 | 2026-09-27 | full |
| `C1-INSTACART-2024` | How Instacart is using AI to achieve zero standing privileges (customer story; undated, year inferred from the BSidesLV24 talk it describes) | ConductorOne (C1.ai) | vendor | https://www.conductorone.com/customers/instacart | 2024 | full |
| `CISA-IR8587-2026` | CISA and NIST Release Guidelines to Protect Federal Cloud Identity Systems from Token Theft, Forgery, and Misuse | CISA | regulator | https://www.cisa.gov/news-events/news/cisa-and-nist-release-guidelines-protect-federal-cloud-identity-systems-token-theft-forgery-and | 2026-09 | full |
| `CLOUDFLARE-JOB-FRAUD-2026` | Senior Software Engineer, Internal Fraud Platform (job posting 8185561) | Cloudflare | job-posting | https://boards.greenhouse.io/cloudflare/jobs/8185561?gh_jid=8185561 | 2026-09-14 | full |
| `CLOUDFLARE-JOB-IAM-2026` | IAM Security Engineer (job posting 8157997) | Cloudflare | job-posting | https://boards.greenhouse.io/cloudflare/jobs/8157997?gh_jid=8157997 | 2026-09-11 | full |
| `CLOUDFLARE-JOB-IAMSYS-2026` | Senior Systems Engineer, Identity & Access Management (job posting 8104955) | Cloudflare | job-posting | https://boards.greenhouse.io/cloudflare/jobs/8104955?gh_jid=8104955 | 2026-08-06 | full |
| `COINBASE-JOB-IAM-2026` | Senior Staff Software Engineer, Platform - IAM (job posting 8155366) | Coinbase | job-posting | https://www.coinbase.com/careers/positions/8155366?gh_jid=8155366 | 2026-09-09 | full |
| `COINBASE-JOB-IDVML-2026` | Staff Machine Learning Engineer (Platform - Identity), Identity Verification (job posting 8211486) | Coinbase | job-posting | https://www.coinbase.com/careers/positions/8211486?gh_jid=8211486 | 2026-09-17 | full |
| `CROWDSTRIKE-AGENTICIDP-2026` | CrowdStrike Announces Agentic Identity Provider | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/crowdstrike-announces-agentic-identity-provider/ | 2026-09-02 | full |
| `DHS-RIVTD-2025` | Remote Identity Validation Technology Demonstration (DHS S&T; page last updated 2025-04-10, results summarised from the 2023 test event) | U.S. Department of Homeland Security, Science and Technology Directorate | regulator | https://www.dhs.gov/science-and-technology/remote-identity-validation-technology-demonstration | 2025-04-10 | full |
| `ELASTIC-JOB-ITDR-2026` | Principal Product Manager - Identity Threat Detection & Response (job posting 8102960) | Elastic | job-posting | https://jobs.elastic.co/jobs?gh_jid=8102960 | 2026-08-11 | full |
| `FBI-IC3-2025` | Senior US Officials Impersonated in Malicious Messaging Campaign (Alert I-051525-PSA) | FBI Internet Crime Complaint Center | regulator | https://www.ic3.gov/PSA/2025/PSA250515 | 2025-05-15 | full |
| `FINCEN-DEEPFAKE-2024` | FinCEN Alert on Fraud Schemes Involving Deepfake Media Targeting Financial Institutions (FIN-2024-Alert004) | FinCEN, U.S. Treasury | regulator | https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf | 2024-11-13 | full |
| `GADJIT-GITHUB-2024` | instacart/gadjit: Automated Access Request Reviews (README; undated, year inferred from GPT-4o plugin and 2024 BSidesLV talk) | GitHub (Instacart) | community | https://github.com/instacart/gadjit | 2024 | full |
| `INCODE-MONEY2020-2026` | A Year on the Front Line of Deepfake Fraud: What We're Bringing to Money 20/20 | Incode | vendor | https://www.incode.com/blog/a-year-on-the-front-line-of-deepfake-fraud-what-we-re-bringing-to-money-2020 | 2026-06-01 | full |
| `LUMOS-UAR-2025` | Lumos Launches Industry-First Agentic User Access Reviews, Moving Towards Autonomous Identity Governance | Lumos | vendor | https://www.lumos.com/blog/lumos-launches-industry-first-agentic-user-access-reviews | 2025-12-08 | full |
| `MSFT-ARREC-2026` | Review recommendations for access reviews (Microsoft Entra ID Governance) | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/id-governance/review-recommendations-access-reviews | 2026-03-12 | full |
| `MSFT-CAAGENT-2026` | Microsoft Entra Conditional Access Optimization Agent | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization | 2026-06-23 | full |
| `MSFT-CAUPDATE-2025` | The Conditional Access Optimization Agent keeps getting better and making your life easier (blog, A. Simons) | Microsoft Tech Community, Microsoft Entra Blog | vendor | https://techcommunity.microsoft.com/blog/microsoft-entra-blog/-/4460535 | 2025-10-14 | full |
| `MSFT-ENTRAAGENTS-2026` | Microsoft Entra agents (overview) | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents | 2026-01-21 | full |
| `MSFT-ENTRAGA-2025` | Smarter identity security starts with AI (blog, A. Simons) | Microsoft Tech Community, Microsoft Entra Blog | vendor | https://techcommunity.microsoft.com/blog/microsoft-entra-blog/-/4429001 | 2025-07-14 | full |
| `MSFT-ENTRAWN-2026` | What's new in Microsoft Entra: October 2026 | Microsoft Tech Community, Microsoft Entra Blog | vendor | https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-october-2026/4556460 | 2026-10-12 | full |
| `MSFT-GOVOPT-2026` | Governance and optimization with Security Copilot in Microsoft Entra | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/security-copilot/entra-governance-optimization | 2025-09-23 | full |
| `MSFT-LIFECYCLE-2026` | Manage lifecycle workflows using Security Copilot in Microsoft Entra | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/security-copilot/entra-lifecycle-workflows | 2025-09-23 | full |
| `MSFT-PASSKEYCAMP-2026` | Conditional Access Optimization Agent: passkey adoption campaigns | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization-passkeys | 2026-05-22 | full |
| `MSFT-RISKYUSER-2026` | Respond to identity threats using Risky User summarization (Security Copilot in Microsoft Entra) | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/entra/security-copilot/entra-risky-user-summarization | 2025-09-23 | full |
| `NIST-IR8587-2026` | NIST IR 8587: Protecting Tokens and Assertions from Forgery, Theft, and Misuse | NIST | standard-setter | https://csrc.nist.gov/pubs/ir/8587/final | 2026-09-15 | full |
| `NIST-SP80063-4-2025` | NIST SP 800-63 Digital Identity Guidelines, Revision 4 (landing page) | NIST | standard-setter | https://pages.nist.gov/800-63-4/ | 2025-07 | full |
| `OKTA-AGENTS-2026` | New Okta for AI Agents innovations increase visibility into agent behavior, secure connections at runtime, and enforce continuous agent governance | Okta Newsroom | vendor | https://www.okta.com/newsroom/press-releases/ai-innovations-oktane-2026/ | 2026-09-22 | full |
| `OKTA-AUTHSURVEY-2026` | Survey: How friction, not ignorance, is stalling enterprise security (2026 Global State of Authentication, Yubico and Okta) | Okta Newsroom | survey | https://www.okta.com/newsroom/articles/global-state-of-authentication-2026-ai-phishing-resistance/ | 2026-10-07 | full |
| `OKTA-DEX-2026` | Lessons learned from securing our digital workforce (J. Cline, SVP Technology, Data & Intelligence) | Okta Newsroom | vendor | https://www.okta.com/newsroom/articles/lessons-from-securing-our-digital-workforce/ | 2026-09-17 | full |
| `OKTA-ITP-2026` | Identity Threat Protection with Okta AI (product page; undated, date shown is retrieval date) | Okta | vendor | https://www.okta.com/products/identity-threat-protection/ | 2026-10-17 | full |
| `OKTA-ITPDOCS-2026` | Identity Threat Protection (Identity Engine documentation; undated, date shown is retrieval date) | Okta Help Center | vendor | https://help.okta.com/oie/en-us/content/topics/itp/overview.htm | 2026-10-17 | full |
| `OKTA-JOB-IDENG-2026` | Staff Identity Engineer (job posting 8171262) | Okta | job-posting | https://www.okta.com/company/careers/opportunity/8171262?gh_jid=8171262 | 2026-09-04 | full |
| `OKTA-JOB-ITP-2026` | Manager, Engineering - Identity Threat Protection (job posting 8242296) | Okta | job-posting | https://www.okta.com/company/careers/opportunity/8242296?gh_jid=8242296 | 2026-10-15 | full |
| `OKTA-TI-2026` | New speed, same tricks: Defend against AI threats with security fundamentals (B. Winterford, Okta Threat Intelligence) | Okta Newsroom | vendor | https://www.okta.com/newsroom/articles/new-speed-same-tricks-defend-against-ai-threats-with-security-fundamentals/ | 2026-10-07 | full |
| `OKTA-WCK-2026` | World Central Kitchen accelerates secure AI adoption with Okta | Okta Newsroom | vendor | https://www.okta.com/newsroom/articles/world-central-kitchen-accelerates-secure-ai-adoption-with-okta/ | 2026-09-24 | full |
| `PANW-IDIRA-2026` | Palo Alto Networks Introduces Idira: the Next-Generation Identity Security Platform Built for the AI Enterprise | Palo Alto Networks | vendor | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-introduces-idira--the-next-generation-identity-security-platform-built-for-the-ai-enterprise | 2026-05-12 | full |
| `PERSONA-CISCO-2026` | How Cisco Automated Workforce Verification With Persona (customer story; undated, text refers to a use case planned for later in 2026) | Persona | vendor | https://withpersona.com/customers/cisco | 2026 | full |
| `PINDROP-DRI-2026` | The Deepfake Readiness Index 2026 (survey of 250 U.S. security leaders; date is sitemap last-modified) | Pindrop | survey | https://www.pindrop.com/resources/report/deepfake-readiness-index | 2026-09-29 | full |
| `PINDROP-HEALTHEQUITY-2026` | 90% Drop in Fraud and a Smoother CX: How HealthEquity Did It | Pindrop | vendor | https://www.pindrop.com/customer/healthequity-drop-fraud-smoother-cx | 2026-02-23 | full |
| `PINDROP-MSUFCU-2025` | Michigan State University Federal Credit Union Cuts Authentication Time in Half with Pindrop | Pindrop | vendor | https://www.pindrop.com/customer/michigan-state-university-federal-credit-union | 2025-01-09 | full |
| `PINDROP-VEC-2025` | The Virginia Employment Commission Reduced Fraud by +$500K Within Months | Pindrop | vendor | https://www.pindrop.com/customer/virginia-employment-commission-reduced-fraud-within-months | 2025-06-13 | full |
| `REALITYDEFENDER-BANK-2026` | How a Global Bank Mitigates Contact Center Deepfake Threats with Reality Defender (anonymised case study; date is sitemap last-modified, publication date not shown) | Reality Defender | vendor | https://www.realitydefender.com/case-studies/how-a-global-bank-mitigates-contact-center-deepfake-threats-with-reality-defender | 2026-07-26 | full |
| `SAILPOINT-AUTONOMOUS-2026` | From Chaos to Control: SailPoint Unlocks a Secure Agentic Era with Autonomous Identity Security | SailPoint | vendor | https://www.sailpoint.com/press-releases/sailpoint-unlocks-a-secure-agentic-era-with-autonomous-identity-security | 2026-10-06 | full |
| `SAILPOINT-HORIZONS-2026` | SailPoint Report Finds 79% of Enterprises Run AI Agents in Production, Yet Only 2% Have Deployed Purpose-built Security (Horizons of Identity Security, fifth edition) | SailPoint | survey | https://www.sailpoint.com/press-releases/sailpoint-horizons-identity-security-ai-adoption-gap | 2026-10-06 | full |
| `SAILPOINT-HUMANFABRIC-2026` | SailPoint Announces Modernization Capabilities for both Cloud and On-Premises Identity Security | SailPoint | vendor | https://www.sailpoint.com/press-releases/sailpoint-announces-modernization-capabilities-for-both-cloud-and-on-premises-identity-security | 2026-10-06 | full |
| `SAILPOINT-IDSEC-2026` | SailPoint eliminates blind spots with unified protection across human, non-human, and AI agent identities | SailPoint | vendor | https://www.sailpoint.com/press-releases/sailpoint-identity-security-solution | 2026-08-04 | full |
| `SAVIYNT-AIONB-2025` | Saviynt Unveils Major AI Capabilities for Identity Security | Saviynt | vendor | https://saviynt.com/press-release/saviynt-unveils-major-ai-capabilities-for-identity-security | 2025-10-15 | full |
| `SECBOULEVARD-BSIDESLV24-2025` | BSidesLV24 - Breaking Ground - JIT Happens: How Instacart Uses AI to Keep Doors Open and Risks Closed | Security Boulevard | conference | https://securityboulevard.com/2025/04/bsideslv24-breaking-ground-jit-happens-how-instacart-uses-ai-to-keep-doors-open-and-risks-closed/ | 2025-04 | search-only |
| `VERIZON-DBIR-2026` | Verizon 2026 Data Breach Investigations Report (landing page; undated, report body not read) | Verizon | survey | https://www.verizon.com/business/resources/reports/dbir/ | 2026 | full |

Dates marked 'sitemap last-modified' or 'retrieval date' are not publication dates; the page did not show one. Search-only sources cannot support an A or B grade alone; use case 05's grade rests on the README and customer story, which were opened.

## 6. Gaps

- **No independent measurement of AI in access governance or identity threat response.** No override, acceptance, false-positive or error rate was found for AI access-review recommendations, Conditional Access suggestions, Okta Identity Threat Protection or Lumos. A search for named customer results with percentages returned only unattributed vendor claims.
- **Customer evidence is thin.** SailPoint's customer stories (Pima Community College, Temple Health, PACCAR, AES, Wipro, Salling Group, Best Buy) mention AI only as something being explored. ConductorOne's other stories (Brex, DigitalOcean) describe workflow automation without AI and carry no publication date, so they were left out. No bank or health-system IGA case with AI and figures was found.
- **Primary Microsoft customer data** behind the 26 gaps, 73% and 83% figures was not reachable; the Entra documentation lists only two agents (Conditional Access Optimization, Identity Risk Management), so other agents named in older material were not verified.
- **Blocked or unavailable:** Identiverse (Cloudflare block), Persona blog (403), Pindrop press page (404), DHS, CISA and Security Boulevard direct (403; DHS and CISA read through the mirror, Security Boulevard search-only), GitHub API (not enabled), the arXiv API (DNS failure; web pages used instead), BioCatch press releases (survey-style, not read), Silverfort and Semperis blog items (listings only; mostly about agents), the Verizon DBIR body, Gartner and Forrester reports, Okta's help pages on AI models behind Identity Threat Protection.
- **Undated pages:** the Instacart story, Gadjit README, Persona's Cisco story and the Okta product and help pages show no publication date; years are inferred and flagged in the sources.
- **Job-posting scan** covered 25 public Greenhouse boards that responded (three other boards returned 404); SailPoint, CyberArk and other Workday-hosted boards were not checked.
- **Practitioner discourse** (conference sessions, community threads) was outside this angle and only touched through the Instacart BSidesLV24 talk title.
