# Identity and access (security)

Last reviewed 2026-10-17. Use cases live in `../use-cases/identity-access.yaml` (24 entries). Ids are shortened here:
`#06` means `security-identity-access-06`. Source keys in brackets, such as [SANS-ITDR-2026], are in the YAML or in
§10. **Evidence is thin and vendor-heavy.** 11 of 24 entries are graded A or B; the one A (contact-centre caller
authentication) rests on the vendor's own case studies. No override rate, false-approval rate or error rate from
production was found for any AI feature in workforce IAM (access reviews, approvals, policy agents, risk scoring).
The independent numbers that exist measure threats, baselines or the limits of detectors. Say so when you quote a figure.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Identity and access management (IAM) decides who or what can use which systems: provisioning for joiners, movers and
leavers, access requests and approvals, access reviews (certifications), authentication (MFA, passkeys, Conditional
Access policies), privileged access, identity threat detection and response (ITDR), identity proofing, help-desk
account recovery, and identity-related fraud such as account takeover (ATO) and caller impersonation. Identities for
AI agents (agent registration, sponsors, agent credentials, MCP authorisation) are covered in the ai-security module;
general non-human identity hygiene and privileged access stay here. The security landscape scan notes fraud is
usually run by fraud and risk teams outside the CISO's organisation, so check who owns it before probing.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Joiner, mover, leaver | Grant, change and remove access from HR events; lifecycle workflows | transaction-processing, software-systems | Stale access: credentials active years after a project ended [PANW-IDLANDSCAPE-2026] |
| Access request and approval | Requester, context lookup, approval, provisioning | transaction-processing, expert-judgment | Approval becomes the default; median 15 minutes, over 24 hours at some firms; 43.5% of granted access unused for 90+ days (one vendor's platform) [OPAL-PALADIN-2026] |
| Access review (certification) and role design | Periodic campaigns, reviewer decisions, revocation, roles | review-assurance, expert-judgment | "Rubber stamping" claimed by vendors, no independent rate found [LUMOS-UAR-2025]; DORA requires yearly reviews, six-monthly for critical functions [DORA-RTS-2024] |
| Policy design | Conditional Access rules, role models, authorisation policy as code | software-systems | Policy sprawl and coverage gaps; one customer: "weeks of manual review" [MSFT-ENTRAGA-2025] |
| Privileged access | Vaulting, just-in-time (JIT) elevation, revocation, session control | software-systems, transaction-processing | 61% of privileged requests met with standing privilege (vendor figure, source unnamed) [PANW-IDIRA-2026]; 56% cannot enforce least privilege for service accounts [PANW-IDLANDSCAPE-2026] |
| Authentication and credentials | MFA and passkey roll-out, password rules, factor enrolment | software-systems | 76% use fragmented authentication across internal apps; 52% got a username and password on day one [OKTA-AUTHSURVEY-2026] |
| Account recovery and help-desk resets | Verify the requester, reset, re-bind MFA | transaction-processing, client-interaction | Social engineering of help desks [CISA-AA23-320A-2025]; an FBI complaint alleges calls led to three compromised accounts in two to three hours [VECTRA-SPIDER-2026]; Cisco staff waited three to four hours for an agent [PERSONA-CISCO-2026] |
| ITDR | Risk scoring, session and token revocation, containment | research-synthesis, transaction-processing | 68% detect identity attacks within 24 hours, 55% contain them in that window [SANS-ITDR-2026] |
| Identity proofing | Document check, selfie match, liveness, injection and deepfake detection | review-assurance, transaction-processing | Median presentation-attack detection 78% in a DHS test of vendors [DHS-RIVTD-2025] |
| Contact-centre authentication and identity fraud | Caller verification, call risk scoring, ATO and scam detection | transaction-processing, client-interaction | Fraudsters passed security questions 53% of the time (vendor data) [PINDROP-VEC-2025]; about 4,700 ATO complaints, USD 359.7M losses in 2025 [FBI-IC3-2025] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome), reinvent (the service or operating model changes). **Coverage:** automate-process is the
largest cell (8 entries), and three of those (`#04`, `#14`, `#15`) are largely rule-based controls with an AI label.
Delegate has two entries, one announced (`#02`) and one at a vendor's own detection team (`#17`). Reinvent has one
announced entry (`#16`). No evidence was found for assist at process or model level, or for delegate at model level.

**Policy and authentication**
- Improve: `#01` agent scans Conditional Access policies daily and drafts report-only fixes an admin approves
  (Microsoft: average 26 gaps per customer per month; grade B, vendor aggregates). `#11` LLM drafts policy as code
  checked by tests (idea; best research pipeline 50.3% fully correct vs 15.3% for one prompt).
- Delegate: `#02` agent plans and runs passkey roll-out campaigns for up to 200 admins (documentation only).

**Access requests and privilege**
- Automate: `#03` Instacart's LLM bot reads the request, a separate score decides, auto-approves above a threshold
  ("nearly 100%" accuracy in testing, no denominator; grade B). Opal announced a similar policy-applying agent (Paladin).
  `#04` zero standing privilege: context-based JIT grants and revocation (vendor claims; rules with an AI label).
- Improve: `#05` conversational front door for IT and access requests (Okta's Dex: 25% of staff in two weeks,
  23,500+ interactions; self-reported).

**Access review and governance**
- Improve: `#06` recommendations and an agent first pass on review items (Microsoft, SailPoint, Lumos, Opal; Lumos
  claims "up to 6x faster"; grade B via a Prosper quote). `#07` usage-based role mining and right-sizing (Google
  IAM recommender; Opal roadmap). `#09` natural-language governance queries, audit prep and workflow drafting.
  `#10` agentic onboarding of applications into governance (announcement). `#12` IAM engineers build automation with
  AI coding tools (Cloudflare's postings make it a requirement).
- Automate: `#08` continuous full-population posture checks with remediation and recorded evidence (SailPoint,
  Saviynt, Idira announcements; regulator-evidence idea). Audit-side testing of access reviews is in governance-risk
  (provisional id `security-governance-risk-07`).

**Identity threat detection and response**
- Improve: `#13` plain-language risky-user summaries and next steps (Microsoft documentation).
- Automate: `#14` ML risk scoring of sign-ins and sessions drives step-up, block or session end (Okta, Microsoft).
  `#15` closed-loop response on high-confidence detections, with a second threshold to a person.
- Delegate: `#17` Push Security's agents hunt for identity-targeting browser attacks and draft detections
  researchers ship (tripled detections shipped; self-reported, adjacent process). Compare `security-operations-18`.
- Reinvent: `#16` MDR (managed detection and response) extended to SaaS identity threats (CrowdStrike, announced);
  the wider MDR shift is `security-operations-23`. Containment playbooks: `security-incident-response-11`.

**Verification, recovery and fraud**
- Automate: `#18` enforced verification before help-desk resets (Cisco via Persona: "three-to-four-hour" wait to
  "as little as five minutes", a practitioner's description, grade B). `#19` ML identity proofing with liveness,
  injection and deepfake detection (Coinbase posting; DHS tests). `#20` identity-graph and 1:N biometric search for
  rings and duplicates. `#21` passive caller authentication: Michigan State University Federal Credit Union (MSUFCU) authentication time 90 to 45 seconds within 90
  days, HealthEquity IVR match 31% to 71% (grade A, vendor-published).
- Improve: `#22` real-time call risk scoring (HealthEquity's fraud head: voice fraud down "over 90%", metric
  undefined; grade B). `#23` synthetic-voice scoring for fraud triage (unnamed bank: about 960 of 1.7M calls scored
  synthetic). `#24` behavioural biometrics and continuous authentication (Visa-BioCatch deal; no result published).

## 4. Interview probes

1. **"In your last access review, what share of items was approved unchanged, and do you record overrides of any
   system recommendation?"** Reveals rubber-stamping and whether `#06` could be measured. Microsoft's tooling can
   query overrides [MSFT-GOVOPT-2026]; nobody publishes the rate.
2. **"When an access request reaches an approver, what context do they see and how long does it wait?"** Reveals
   the baseline for `#03`. Ask what score or threshold auditors would accept and who owns a wrong auto-approval.
3. **"When someone calls the help desk to reset MFA, what decides the outcome: the agent's judgement or an enforced
   verification step? Can you prove each reset was verified?"** Reveals exposure to the Scattered Spider pattern and
   fit for `#18` [CISA-AA23-320A-2025].
4. **"Where do onboarding, step-up and recovery rely on a selfie, voice, video, SMS or security questions? Has anyone
   tested them against injection or deepfake attacks, or only on the vendor's data?"** Reveals `#19`, `#21`, `#23`
   risk; NYDFS advises avoiding SMS, voice or video factors [NYDFS-AIGUIDE-2024].
5. **"How long from detecting an identity attack to containing it, and which actions (revoke tokens, end sessions,
   remove roles) can run without a ticket or a person?"** Reveals the detect-contain gap [SANS-ITDR-2026] and
   readiness for `#14` and `#15`.
6. **"Who owns the seam between the identity team and the SOC?"** Reveals whether identity data reaches detection
   and whether `#15` or `#16` (managed service) fits.
7. **"How many Conditional Access policies do you run, when were they last reviewed end to end, and where are the
   break-glass accounts?"** Reveals fit for `#01` and lockout risk.
8. **"How much standing admin access exists, and how do you find dormant, orphaned or over-privileged accounts
   today?"** Reveals the case for `#04`, `#07`, `#08`.
9. **"Which regulators ask for proof of access reviews (DORA, NIS2, NYDFS), and how much evidence is assembled by
   hand?"** Reveals the evidence burden behind `#08`.
10. **"What would tell you an AI step in identity is working: gaps closed, review time, recovery time, false
    positives, overrides?"** Reveals whether a pilot will produce any quality evidence; none is public.
11. **"Is identity fraud (ATO, caller impersonation) run by your team or a separate fraud function?"** Reveals
    whether `#20` to `#24` belong in this conversation.

## 5. Metrics and benchmarks

| Measure | Figure | Provenance |
|---|---|---|
| Detect vs contain identity attacks | 68% detect within 24 hours; 55% contain in that window [SANS-ITDR-2026] | independent survey (sponsored; page inconsistent on its 85% figure) |
| ITDR tools vs breaches | 85% use ITDR tools; 55% had an identity-related breach in 12 months [SANS-ITDR-2026] | independent survey |
| Non-human credential rotation | 8% rotate over 75% of non-human credentials every 90 days [SANS-ITDR-2026] | independent survey |
| Identity breaches and machine identities | 90% had at least one identity breach in 12 months; 109 machine identities per human; fragmentation adds 12 hours per incident [PANW-IDLANDSCAPE-2026] | vendor survey, n=2,930 |
| Incident-response actions | 51% include password reset; 45% MFA step-up; 41% token revocation; 36% end privileged sessions [PANW-IDLANDSCAPE-2026] | vendor survey |
| Conditional Access agent | 26 gaps per customer per month; 73% "meaningful improvements"; 83%+ of preview customers got actionable advice [MSFT-CAUPDATE-2025] [MSFT-ENTRAGA-2025] | vendor-published, no denominators |
| Caller authentication | 90s to 45s (MSUFCU); IVR match 31% to 71% (HealthEquity) [PINDROP-MSUFCU-2025] [PINDROP-HEALTHEQUITY-2026] | vendor-published |
| Security-question pass rate by fraudsters | 53% average over 2,500 fraud calls at 10 institutions [PINDROP-VEC-2025] | vendor data |
| Phishing-resistant policy (counterfactual) | Could have stopped 88% of ATO attempts, 99.75% with app sign-in enforcement, in ~6,000 events [OKTA-TI-2026] | vendor-published estimate |
| Factors in ATO sessions | password 87%; push 58%; app OTP 36%; SMS OTP 22% [OKTA-TI-2026] | vendor-published |
| AI-driven attacks | 44% had a successful AI-driven attack; 43% saw voice or video impersonation; 36% spotted the human-written message [OKTA-AUTHSURVEY-2026] | vendor survey, ~2,000 |
| Identity proofing (DHS test of vendors) | median presentation-attack detection 78%; genuine users validated 85% (median); errors 20% for 46+ vs 9% for 18-45 [DHS-RIVTD-2025] | independent, 2023 event |
| Deepfake-voice detectors | best equal error rate 13.50% of 12; others above 20% [USENIX-VOICEWUKONG-2025] | independent |
| Passkey implementations | 53 of 103 sites had at least one high-severity flaw [USENIX-PASSKEYS-2026] | independent |
| LLM-written policy code | 50.3% fully correct with a structured pipeline vs 15.3% single prompt [ARXIV-2609.24036] | independent preprint |
| AI-related fraud losses | 22,364 AI-related complaints, USD 893M adjusted losses in 2025 [FBI-IC3-2025] | regulator |
| Identity governance maturity | 87% rate human IAM capable; 43% prepared to give verifiable evidence in an AI audit [SAILPOINT-HORIZONS-2026] | vendor survey, 340 |
| Deepfake readiness | 37% rely on legacy detection tools [PINDROP-DRI-2026] | vendor survey, 250 |

NIST thresholds to test vendors against: 1:1 face false match 1:10,000 or better and false non-match 1:100 or
better; 1:N false positive identification 1:1,000 or better; presentation-attack accept rate below 0.07; document
false accept and reject 0.1 or less; no demographic group more than 25% worse [NIST-SP80063A-4-2025].
What to measure in a pilot: override rate on recommendations, share of items approved unchanged, time to approve,
time to contain, recovery time, false positives and lockouts. None has a published AI benchmark in this module.

## 6. Guardrails

- **NIST SP 800-63-4 (July 2025)** is the most concrete rulebook: any AI or ML in an identity system must be
  documented, disclosed to relying parties and risk-assessed, with training methods and test results available to
  customers [NIST-SP80063-4-2025]. Proofing must detect injected and forged media; automated media decisions should be
  augmented by manual review; 1:N matches cannot decline an enrolment without manual review [NIST-SP80063A-4-2025].
- **FinCEN FIN-2024-Alert004** asks institutions to tag deepfake cases in SARs, names phishing-resistant MFA and live
  verification as best practices, and warns criminals may claim technical glitches to avoid live checks
  [FINCEN-DEEPFAKE-2024].
- **NYDFS (2024-10-16):** MFA for all authorised users from November 2025; consider avoiding SMS, voice or video
  factors; use liveness detection; annual access reviews [NYDFS-AIGUIDE-2024].
- **EU:** DORA's standard requires least privilege, yearly access updates (six-monthly for critical functions) and
  automated lifecycle "where feasible and appropriate" [DORA-RTS-2024]. The NIS2 implementing regulation requires an
  access register, documented reviews and MFA or continuous authentication [NIS2-IMPL-2024]. The AI Act bans emotion
  inference at work and excludes pure 1:1 verification from the Annex III biometrics high-risk entry [EU-AIACT-2024].
  The payments deal would make providers refund staff-impersonation fraud; adoption pending [EP-PSR-2025].
- **CISA:** phishing-resistant MFA (FIDO/WebAuthn or PKI) against help-desk social engineering, MFA fatigue and SIM
  swap [CISA-AA23-320A-2025]; CISA and NIST IR 8587 on token theft and forgery [CISA-IR8587-2026] [NIST-IR8587-2026].
- **Product controls to look for:** report-only policies, explicit admin approval, read-only roles and audit logs
  [MSFT-CAAGENT-2026]; score-then-threshold decisions, a 90-day privilege cap and quarterly policy review
  [C1-INSTACART-2024]; a second threshold that routes to a person [NETWRIX-ITDR-2026].
- **Steps that need human judgement:** declining an enrolment or account on a biometric or media score; resetting a
  factor when verification fails; approving sensitive or unusual access; enforcing a new policy (after report-only);
  setting autonomy thresholds; deciding on fraud cases. Accountability for reviews stays with the regulated entity.

## 7. Roles and how they evolve

- **Administrators become approvers of agent output.** Conditional Access admins approve or reject suggestions
  instead of reading policy logic [MSFT-CAAGENT-2026]; reviewers check evidence and exceptions [LUMOS-UAR-2025].
- **Approvals move to code and bots.** At Instacart, staff engineers no longer approve requests; security engineers
  write the policy code and the bot [C1-INSTACART-2024].
- **Help desk stops interrogating.** Cisco's agents spend less time on verification calls [PERSONA-CISCO-2026];
  Specops argues staff should follow a process that holds even with a persuasive caller [PETRI-SERVICEDESK-2026].
- **New skills in hiring.** Cloudflare's IAM postings require hands-on LLM use [CLOUDFLARE-JOB-IAM-2026]; Elastic's
  ITDR product role asks for LLM and agentic fluency [ELASTIC-JOB-ITDR-2026]; Coinbase's identity ML engineers own
  vendor benchmarking and routing [COINBASE-JOB-IDVML-2026]; Coinbase's IAM lead covers human, agent, service and
  workload identity across 700+ systems [COINBASE-JOB-IAM-2026].
- **Proofing agents gain a media-forensics duty** under NIST [NIST-SP80063A-4-2025].
- **Bigger non-human population.** 109 machine identities per human in one survey [PANW-IDLANDSCAPE-2026]; OWASP's
  agentic maturity model adds registries and owners for agents as non-human identities [OWASP-STATE-AGENTIC-2026];
  IBM advises scoping and attributing agentic identities [IBM-CODB-2026].
- **Workforce data:** AI is the top skills need (41%) in ISC2's 2025 study [ISC2-WORKFORCE-2025]. Forrester says
  vendors hire fewer early-career staff and have no answer to the "five-year problem" [FORRESTER-RSAC-2026]. No data
  on identity-team headcount was found.

## 8. Frontier

- 2025-07: NIST finalises SP 800-63-4 with AI/ML disclosure and injection and forged-media rules [NIST-SP80063-4-2025].
- 2026-03-18: a vendor says it was the only one of 18 systems with zero attack acceptance in DHS's 2025 liveness
  rally [IDENTY-RIVR-2026].
- 2026-05-12: Palo Alto Networks launches Idira (on CyberArk) with zero standing privilege for every identity
  [PANW-IDIRA-2026].
- 2026-06-15: Saviynt adds biometric and liveness verification inside identity certification [SAVIYNT-IARA-2026];
  Opal announces AI-guided reviews [OPAL-REVIEWS-2026]. 2026-06-17: a FIRST talk (Datadog) on detecting DPRK fake
  applicants with AI risk assessment; no metrics in the abstract [FIRST-CON-2026].
- 2026-07-16: Microsoft passkeys default in Entra from 2026-09-01; SMS and voice retired 2027-02-01
  [FORRESTER-MSPASSKEY-2026].
- 2026-08: USENIX passkey study finds flaws on about half of 103 sites [USENIX-PASSKEYS-2026]; Black Hat shows two
  attacks on passkey implementations, not the cryptography [SWI-BLACKHAT-2026]; Visa to buy BioCatch [FORRESTER-BIOCATCH-2026].
- 2026-09-02 to 2026-10-06: CrowdStrike (Agentic IdP, SaaS identity MDR), Okta (AI agent updates), SailPoint
  (autonomous posture management, conversational requests) [CROWDSTRIKE-AGENTICIDP-2026] [OKTA-AGENTS-2026]
  [SAILPOINT-AUTONOMOUS-2026]. Forrester: agentic AI "pasted into" familiar messages [FORRESTER-RSAC-2026].
- 2026-09-15: CISA and NIST finalise IR 8587 on token theft [NIST-IR8587-2026].
- 2026-10-05 to 2026-10-13: Okta says AI accelerates known tricks, so policy enforcement is the defence [OKTA-TI-2026];
  Silverfort's lab agents went from initial credentials to domain takeover in four to five minutes, which it calls
  patterns rather than benchmarks [SILVERFORT-ASSUMPTIONS-2026].
- Upcoming: FIDO Authenticate (2026-10-19 to 21) on "agentic authentication" [FIDO-AUTH-2026]; Gartner IAM Summit from
  2026-12-07 with sessions on AI-enhanced IGA and deepfake-resistant verification [GARTNER-IAMSUMMIT-2026].

## 9. Common objections

- **"It's just old controls with an AI label."** Partly true: Forrester says agentic AI was "pasted into" familiar
  messages [FORRESTER-RSAC-2026], and several automate entries (`#04`, `#14`, `#15`) are rule-based. Response: judge
  each feature by what it decides and what it logs, and ask for an override or error rate; none is published.
- **"An LLM shouldn't approve access."** Instacart agrees: the LLM reads and interprets, a separate score decides,
  with a 90-day cap and quarterly policy review [C1-INSTACART-2024]. Opal keeps risky requests with a person
  [OPAL-PALADIN-2026]. Start in advisory mode and track overrides [MSFT-GOVOPT-2026].
- **"Deepfake detection will lose the arms race."** The evidence supports caution: best voice detector error 13.50%
  [USENIX-VOICEWUKONG-2025]; clones bypass speaker verification [ARXIV-2601.02914]. Response: use detection as a
  triage signal and move high-risk steps to factors deepfakes cannot copy, as NYDFS and FinCEN advise
  [NYDFS-AIGUIDE-2024] [FINCEN-DEEPFAKE-2024].
- **"Fundamentals matter more than AI."** Okta's estimate that phishing-resistant policies could have stopped
  99.75% of takeover attempts supports this [OKTA-TI-2026]. Response: AI fits around the fundamentals, for example
  `#02` planning passkey roll-out and `#18` enforcing verification at recovery, the residual gap Okta names.
- **"Passkeys solve it."** Implementations had high-severity flaws on 53 of 103 sites [USENIX-PASSKEYS-2026], and
  attackers push users to downgrade factors [OKTA-TI-MFADOWNGRADE-2026]. Recovery and enrolment remain the weak point.
- **"Auditors won't accept it."** Instacart says auditors raised no unanswered question about its audit path
  [C1-INSTACART-2024]; but only 43% feel ready to give verifiable evidence in an AI-related audit
  [SAILPOINT-HORIZONS-2026], and NIST requires disclosure of AI use [NIST-SP80063-4-2025].
- **"Behavioural signals will block real customers."** Forrester flags false positives and possible PII status
  [FORRESTER-BIOCATCH-2026]; DHS found higher errors for older users [DHS-RIVTD-2025]. Test on your own population.
- **"Cost."** The Entra agent bills at least one compute unit a month even if unused [MSFT-CAAGENT-2026]; Okta warns
  of a "tool tax" on tokens [OKTA-DEX-2026].

## 10. Sources

Keys used here but not in the YAML (full details for all others are in the YAML):

- [OKTA-AUTHSURVEY-2026] Yubico and Okta, 2026 Global State of Authentication (Okta Newsroom survey), 2026-10-07.
- [SAILPOINT-HORIZONS-2026] SailPoint, Horizons of Identity Security, fifth edition (press release), 2026-10-06.
- [PINDROP-DRI-2026] Pindrop, The Deepfake Readiness Index 2026 (survey of 250 U.S. security leaders), 2026-09-29.
- [USENIX-PASSKEYS-2026] Jannett et al., The State of Passkeys, USENIX Security 2026, 2026-08.
- [SWI-BLACKHAT-2026] Start with Identity, Black Hat USA 2026 recap, 2026-08-06.
- [FORRESTER-RSAC-2026] Forrester, RSAC 2026: An AI Coming-Of-Age Story Without The Romance, 2026-03-31.
- [ISC2-WORKFORCE-2025] ISC2, 2025 Cybersecurity Workforce Study, 2025-12-04.
- [SAVIYNT-IARA-2026] Saviynt release (agent access gateway; identity verification in certification), 2026-06-15.
- [OKTA-AGENTS-2026] Okta Newsroom, Okta for AI Agents innovations (Oktane 2026), 2026-09-22.
- [SILVERFORT-ASSUMPTIONS-2026] Silverfort, 5 cybersecurity assumptions AI attacks break, 2026-10-13.
- [FIDO-AUTH-2026] FIDO Alliance, Authenticate U.S. 2026 event page, retrieved 2026-10-17.
- [GARTNER-IAMSUMMIT-2026] Gartner, Identity & Access Management Summit 2026 agenda, retrieved 2026-10-17.
- [FIRST-CON-2026] FIRST, 38th annual conference programme, Denver, 2026-06-14 to 19.
- [OWASP-STATE-AGENTIC-2026] OWASP GenAI Security Project, State of Agentic AI Security and Governance v2.01, 2026.
- [VECTRA-SPIDER-2026] Vectra AI, The FBI wrote down the Scattered Spider playbook, and it starts with a phone call, 2026-07-06.
- [IBM-CODB-2026] IBM and Ponemon, Cost of a Data Breach Report 2026 (landing page), 2026-07.
