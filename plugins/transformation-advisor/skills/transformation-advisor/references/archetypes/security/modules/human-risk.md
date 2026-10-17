# Human risk (security)

Last reviewed 2026-10-17. Use cases live in `../use-cases/human-risk.yaml` (18 entries). Ids are shortened here:
`#06` means `security-human-risk-06`. Source keys in brackets, such as [UCSD-PHISHTRAIN-2025], are given in full in the
YAML or listed in §10. **Evidence is thin and vendor-heavy on the defender side.** 9 of 18 entries are graded A or B;
the two A grades (`#01`, `#10`) rest on figures published only on the vendor's own customer pages. Independent,
peer-reviewed numbers exist mostly for what AI does for attackers, not for AI-based defences. Say so when you quote
a figure.

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

The people side of security: awareness training and phishing simulation, handling the suspicious emails employees
report, defending against impersonation, deepfakes and scams aimed at staff and the brand, verifying the identity of
new hires and of people asking for money or access, insider-risk detection, and testing staff with social-engineering
exercises. Fraud has no module of its own; the landscape scan folds scams and impersonation in here and into
identity-access. Help-desk reset verification, identity proofing and contact-centre voice security sit in
identity-access; the SOC side of phishing triage sits in operations.

Terms used below: phishing simulation (a fake phishing email sent to staff to test and teach), click or failure rate
(share of recipients who click or enter credentials), reporting rate (share who report the email), vishing (voice
phishing) and smishing (SMS phishing), deepfake (AI-synthesised voice or video of a real person), BEC (business email
compromise: fraudulent payment requests by email), OSINT (open-source intelligence: public information about a
person), LLM (large language model), human risk management (HRM: vendors' term for using behaviour data to target
training and nudges), SEG (secure email gateway, a filter in front of the mail server).

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Awareness programme design and content | Choose topics, build and localise modules, schedule | document-production | Library gaps for own policies and new attacks; modules take days to build [HOXHUNT-CONTENT-2026] |
| Phishing, vishing and deepfake simulation | Design lures, send, record clicks, reports and credential entry, compare cohorts | review-assurance, data-reporting | Results swing with lure difficulty: 1-2% clicks on banal lures, 30%+ on others [UCSD-PHISHTRAIN-2025]; staff cannot tell voice clones from real callers [BSIDESLV-2026] |
| Training delivery and follow-up | Embedded training after a failed simulation, annual courses, nudges | document-production | Over half of embedded-training sessions ended within 10 seconds; under 24% completed the material [UCSD-PHISHTRAIN-2025] |
| Reported-email handling | Intake from the report button, classify, remove or release, reply to the reporter | transaction-processing | Report volume rises as training works and swamps the SOC [HOXHUNT-AVANADE-2026] |
| Human-risk measurement and intervention | Combine simulation, ticket and security-tool signals into risk views; coach or escalate | data-reporting | Annual compliance training shows no risk reduction; small teams for large populations [HOXHUNT-UBER-2026] |
| Impersonation and scam takedown | Find lookalike domains, profiles and ads; file takedowns | transaction-processing | "Days to weeks" to find and remove scams by hand [DOPPEL-ARK-2026] |
| Identity and request verification | New-hire identity checks; verifying payment and credential requests | review-assurance | Checks built for false claims, not stolen real identities with AI-enhanced photos [KNOWBE4-NKHIRE-2024] |
| Insider-risk detection and investigation | Correlate user activity, open cases, escalate to HR or legal | review-assurance, data-reporting | Log volume beyond manual review [ARXIV-2503.02702]; 67 days average to contain (vendor-sponsored survey) [HELPNET-PONEMON-2026] |
| Social-engineering assessment | Authorised vishing and pretext tests of staff and help desk | expert-judgment | Human-caller testing is slow; AI callers are now cheap for attackers [ARXIV-2607.09970] |

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome with checkpoints), reinvent (the service or operating model changes).
Coverage: augment 11, automate 3, assist 3, delegate 1; step 9, process 9, model 0. **No source describes a
model-level change** (new services, sourcing or who does the work) in this module, and the only delegate entry is a
research system. Do not suggest otherwise.

**Awareness training and simulation**
- Improve: `#01` adaptive, reward-based training aimed at repeat clickers first and tested on cohorts before rollout
  (Avanade: 11% lower failure and 27% higher reporting than its old tool over three months; Qualcomm; vendor pages).
  `#02` behaviour signals trigger just-in-time micro-training and nudges (Uber: 25,000+ users, two-person team;
  research prototypes put LLM coaching inside the browser). `#03` LLMs draft custom modules that a person publishes
  (vendor claims). `#04` LLM plus OSINT personalised simulations (a 7,700-person university study tripled click rates
  over generic lures). `#05` AI-voice vishing practice (vendor announcements, no results). `#06` deepfake and
  executive-impersonation drills, which NYDFS names as an option (no results).

**Reported email and email defence**
- Automate: `#07` the report button feeds automated triage (Avanade: "over 900 hours a month" by the vendor's
  calculation); the SOC agent view is `security-operations-04`. `#08` behavioural AI replaces the SEG and answers
  reporters (Valvoline: USD 600K loss avoided, 480 analyst hours a month, vendor page).
- Improve (idea): `#09` an LLM reads inbound email intent and warns the user (research only).

**Impersonation and scams**
- Automate: `#10` AI detection and automated takedown of brand and executive impersonation (ARK Invest: median 5.5
  hours to resolve a domain; vendor page). Evidence-packaging agents for takedown: `security-threat-intelligence-18`.
- Delegate: `#11` LLM scam-baiting runs weeks-long conversations with scammers to extract mule accounts (research,
  about 32% disclosure rate).

**Identity and request verification**
- Improve: `#12` HR, IT and SOC checks against fake remote workers (KnowBe4's own hire; Datadog's AI-assisted
  applicant hunting is `security-threat-intelligence-21`; ML identity proofing is `security-identity-access-19`).
  `#13` idea: out-of-band verification of voice or video requests for money or access (regulator advice; help-desk
  version is `security-identity-access-18`). Deepfake voice detection in calls is `security-identity-access-23`.

**Insider risk and shadow AI**
- Improve: `#14` LLM analysis of insider-threat logs (Xiaohongshu: about 90% less manual review, authors' abstract).
  `#15` insider-risk platforms with AI scoring and investigation (Purview; 42% of surveyed firms use AI here). `#16`
  "audit and educate" coaching on risky AI prompts instead of blocking (vendor claims).

**Social-engineering testing**
- Improve (ideas): `#17` AI voice agents in authorised vishing red teams (DEF CON 34 bot contest, ScamBench). `#18`
  sequence analysis of 1,200+ real call transcripts to design training and detection.

## 4. Interview probes

1. **How do you know awareness work lowers risk: click rate, report rate or incidents? Do you keep a no-training or
   delayed group and vary lure difficulty?** Reveals whether claims would survive the UCSD finding of little effect
   [UCSD-PHISHTRAIN-2025] and whether `#01`-style cohort tests are possible.
2. **Who are your repeat clickers and most-targeted roles, and do they get anything different?** Reveals readiness for
   risk-targeted training (`#01`, `#02`).
3. **How many suspicious emails do staff report each month, who triages them, and what share is still handled by
   hand? Does the reporter hear back?** Reveals the case for `#07`/`#08` and the SOC overlap.
4. **Which payment, credential-reset or data requests could be approved today on a voice or video call alone? What
   is the out-of-band check, and who can skip it?** Reveals deepfake exposure and the gap `#13` closes [CNN-ARUP-2024].
5. **Do your simulations include voice, SMS or deepfake scenarios, and do finance, help desk and executives get
   them?** Reveals coverage against NYDFS-style expectations [NYDFS-AIGUIDE-2024] (`#05`, `#06`).
6. **What behaviour data would a human-risk score use, and what have your privacy officer, works council or unions
   agreed?** Reveals whether `#02`, `#15` or `#16` are lawful and acceptable [ICO-MONITORING-2023].
7. **How do you verify remote candidates, contractors and vendor staff before shipping a laptop or granting access?
   Is HR part of the security process?** Reveals fake-IT-worker exposure (`#12`) [FBI-DPRK-2025].
8. **Who finds and removes lookalike domains and fake executive profiles today, and how long does it take?** Reveals
   the takedown baseline for `#10`.
9. **What do you know about staff pasting company data into AI tools, and do you block, warn or coach?** Reveals the
   shadow-AI stance (`#16`).
10. **If you use AI-written training or lures, who reviews them before they go out, and what pretexts are off
    limits?** Reveals content control and simulation ethics [SOPHOS-PHAKE-2025] (`#03`, `#04`).
11. **What metrics go to the board for human risk?** Reveals activity metrics versus outcome measures [NIST-SP80050-2024].

## 5. Metrics and benchmarks

| Measure | Typical figure | Source and provenance |
|---|---|---|
| Field trial of training (19,500 staff, 8 months) | Median 10% fail per exercise; 56%+ clicked at some point; embedded training cut failure by 2 points; annual training not linked to fewer failures | [UCSD-PHISHTRAIN-2025], independent, randomised |
| How embedded training works | Mainly through nudging; content rarely read; delayed training as effective as immediate | [ARXIV-2409.01378], independent |
| LLM-personalised lures | 10.0% click vs 3.7% (LLM generic) and 4.1% (manual generic); about USD 0.03 per email | [USENIX-CZYBIK-2026], independent, 7,700 people |
| AI vs human spear phishing | 54% click for both AI and human experts; control 12% | [ARXIV-2412.00586], independent, 101 people |
| AI voice scams | 16.5% overall compliance; up to 36% (relative in distress) | [ARXIV-2607.09970], independent, survey experiment N=4,100 |
| LLM romance-baiting agent | 46% compliance vs 18% for human operators; 87% of scam labour is systematised conversation | [USENIX-ROMANCE-2026], independent, blinded week-long study |
| Spotting AI-written messages | Only 36% identified the human-written message | [OKTA-AUTHSURVEY-2026], vendor survey, about 2,000 respondents |
| AI attacks experienced | 44% at least one successful AI-driven attack; 43% saw voice or video impersonation of executives or clients | [OKTA-AUTHSURVEY-2026], vendor survey |
| Deepfake readiness | 37% rely on legacy tools for deepfake detection | [PINDROP-DRI-2026], vendor survey, 250 US leaders |
| "Good" failure rate | 5-10% mature programme; 25-35% untrained (definitions vary) | [HOXHUNT-FAILRATE-2026], vendor dataset |
| Cohort benchmark | 43% higher resilience ratio, 11% lower failure, 27% higher reporting vs previous tool | [HOXHUNT-AVANADE-2026], vendor page, two 1,000-user cohorts |
| Report-triage time saved | Over 900 SOC hours a month "by one calculation"; 480 hours a month at Valvoline | [HOXHUNT-AVANADE-2026], [ABNORMAL-VALVOLINE-2026], vendor pages |
| Takedown speed | Median 5.5 hours per domain; 98% success | [DOPPEL-ARK-2026], vendor page |
| AI in cybercrime (US, 2025) | 22,364 complaints citing AI; USD 893M adjusted losses; AI-related BEC USD 30.3M of over USD 3.0B BEC | [FBI-IC3-2025], regulator; FBI says victims often miss AI's role |
| Phishing share (EU) | 77.8% of social-engineering techniques in the 2026 dataset | [ENISA-ETL-2026], regulator |
| AI-supported phishing | Over 80% by early 2025, per third-party reporting ENISA cites | [ENISA-ETL-2025]; the research files describe the base differently (phishing emails vs social-engineering activity); check before quoting |
| Insider-risk cost | USD 19.5M a year average; negligent insiders USD 10.3M; 42% use AI for detection | [HELPNET-PONEMON-2026], vendor-sponsored survey |
| AI tools in data loss | 37% of material data loss cases from misuse or misconfiguration of AI tools | [PROOFPOINT-VOC-2026], vendor survey |

Not found anywhere: independent error, override or missed-attack rates for AI phishing triage, AI-personalised
training, AI insider detection or deepfake detectors in production. Advise clients to measure their own, with a
control group.

## 6. Guardrails

**Standards and regulators**
- NYDFS (2024-10-16): train all staff, executives included, on AI-enhanced social engineering; training may use
  simulated phishing and voice and video impersonation exercises; cover verifying unexpected money-transfer requests
  and when human review is required; not all authentication factors resist deepfakes [NYDFS-AIGUIDE-2024].
- FinCEN (2024-11-13): alert on deepfake-media fraud, with more suspicious-activity reports citing deepfakes
  [FINCEN-DEEPFAKE-NR-2024]. FBI: verify through a known channel, do not rely on hearing an AI voice
  [FBI-IC3PSA-2025]; verify remote workers' identity across the whole employment lifecycle [FBI-DPRK-2025].
- NIST SP 800-50 Rev. 1 (2024-09-12): lifecycle approach to a learning programme, with metrics and evaluation
  [NIST-SP80050-2024].
- EU AI Act: AI literacy duties from 2025-02-02; transparency rules, including labelling AI-generated content, from
  August 2026; high-risk employment uses from 2027-12-02; emotion recognition at work is prohibited [EC-AIACT-2026].
- UK ICO guidance on monitoring workers applies to behaviour scores, insider-risk tools and prompt inspection; it is
  flagged as under review [ICO-MONITORING-2023].

**Design guardrails seen in practice**
- Human publishes every AI-drafted module [HOXHUNT-CONTENT-2026].
- Simulation ethics: staff-committee approval, briefing and debriefing [USENIX-CZYBIK-2026]; no "unfair" pretexts
  such as financial hardship or job security [SOPHOS-PHAKE-2025].
- Judge simulations with a control group and with reporting rate and difficulty, not click rate alone
  [UCSD-PHISHTRAIN-2025, HOXHUNT-FAILRATE-2026].
- Triage agents get their own least-privilege identity and explain each verdict [MSFT-PHISHTRIAGE-2026].
- Insider-risk tools pseudonymise users by default and restrict investigator access [PURVIEW-IRM-2026].

**Steps that need human judgment**
- Approving any payment, credential or data request that arrived by voice, video or email [NYDFS-AIGUIDE-2024].
- Selecting cohorts and deciding on rollout after a test [HOXHUNT-QUALCOMM-2023].
- Acting on insider-risk cases and escalating to HR or legal [PURVIEW-IRM-2026].
- Hiring and onboarding identity decisions; the SOC call on anomalous new-hire activity [KNOWBE4-NKHIRE-2024].
- Scenario approval for vishing and deepfake tests, including executive consent to use their likeness (`#06`, `#17`).

## 7. Roles and how they evolve

- **Awareness teams** move from running a training calendar to running a signal-and-intervention system; Uber covers
  25,000+ users with two people [HOXHUNT-UBER-2026]. Vendors pitch AI as an "on-demand instructional design team"
  [HOXHUNT-CONTENT-2026] and as freeing staff for higher-level risk decisions [SECURITYBRIEF-AIDA-2026].
- **SOC analysts** handling reported email: Avanade says the platform did the work of over 5 analysts a month
  [HOXHUNT-AVANADE-2026]; Valvoline says 4-5 analysts had spent 90% of each day on email tasks, now moved to other
  work [ABNORMAL-VALVOLINE-2026]. No source reports headcount cuts.
- **HR, hiring managers, finance and help desk** become part of the security perimeter and need training
  [FBI-DPRK-2025, NYDFS-AIGUIDE-2024].
- **Insider-risk programmes** are urged to treat AI agents as identities with defined access [HELPNET-PONEMON-2026].
- **Hiring signal**: a Johnson & Johnson awareness-lead posting asks for experience with human risk management
  platforms and behavioural analytics [JNJ-JOB-2026, search-only].

## 8. Frontier

- 2025-05: randomised trial at UC San Diego Health questions classic training [UCSD-PHISHTRAIN-2025].
- 2025-10-24: AI-voice phishing training announced [HOXHUNT-VOICE-2025].
- 2026-01-16: AI takedown case at ARK Invest published [DOPPEL-ARK-2026].
- 2026-01-30: KnowBe4 says seven AI agents are in market for human risk management [SECURITYBRIEF-AIDA-2026].
- 2026-02-26: few surveyed firms treat AI agents as insiders [HELPNET-PONEMON-2026].
- 2026-04-16 and 2026-08-26: an awareness vendor moves into agentic email security [ADAPTIVE-BLOG-2026].
- 2026-06-17: Datadog presents AI-assisted fake-applicant hunting at FIRST [FIRST-CON-2026].
- 2026-06-24: AI content generation for custom modules [HOXHUNT-CONTENT-2026].
- 2026-07-10: AI vishing judged economically viable where human vishing is not [ARXIV-2607.09970].
- 2026-08: USENIX papers measure LLM personalised phishing and LLM romance-baiting agents [USENIX-CZYBIK-2026,
  USENIX-ROMANCE-2026]; DEF CON 34 runs a vishing bot contest and BSides LV presents ScamBench
  [DEFCON-34-CONTESTS-2026, BSIDESLV-2026]; Black Hat recap names AI-native insider investigations
  [SWI-BLACKHAT-2026]; in-browser LLM coaching prototypes [ARXIV-2608.02296].
- 2026: SANS says AI moved from #4 to #2 among human risks in its awareness report (page only) [SANS-AWARENESS-2026].
- 2026-09-22: ENISA links a higher insider share to the DPRK actor Famous Chollima [ENISA-ETL-2026].
- 2026-10-07: Okta calls AI "the accelerant" and says identity fundamentals still decide outcomes [CSD-OKTA-2026].
- 2026-10-14: US charges and raids against DPRK IT-worker facilitators; more than 70 US companies affected
  [CSD-DPRK-2026].

## 9. Common objections

- **"Training doesn't work."** Partly fair: the largest field trial found little effect from annual or embedded
  training [UCSD-PHISHTRAIN-2025], and community debate echoes it [HN-PHISHTRAIN-2025]. Response: measure with a
  control group; shift toward targeted, behaviour-triggered interventions (`#01`, `#02`) and controls that do not
  depend on users (`#08`, `#13`).
- **"Simulations are unfair and breed resentment."** Sophos lists pretexts that cross ethical lines
  [SOPHOS-PHAKE-2025]. Response: staff-committee approval and debriefing, as in the university study
  [USENIX-CZYBIK-2026]; reward reporting rather than punish clicks (`#01`).
- **"Personalised AI training is just hype."** A controlled study found no measurable advantage for complex
  psychometric personalisation over good generic content [ARXIV-2512.01893]. Response: personalise by role and risk
  (who is targeted, who repeats), not by personality.
- **"People can learn to spot deepfakes and AI emails."** Evidence says no: 36% picked the human-written message
  [OKTA-AUTHSURVEY-2026]; persuasiveness, not robotic voice, drove compliance [ARXIV-2607.09970]. Response:
  verification procedures that work without spotting fakes (`#13`) [FBI-IC3PSA-2025].
- **"Behaviour scoring is surveillance."** It is workplace monitoring under ICO guidance, and emotion inference at
  work is banned in the EU [ICO-MONITORING-2023, EC-AIACT-2026]. Response: data minimisation, pseudonymisation,
  agreed purposes [PURVIEW-IRM-2026].
- **"All the success stories are vendors'."** True: every named defender outcome here is on a vendor page. Response:
  run a cohort comparison or proof of value on your own users and mail, as Avanade and Valvoline did (`#01`, `#08`).
- **"Click rate is falling, so we're fine."** Click rate depends on lure difficulty [UCSD-PHISHTRAIN-2025]; track
  reporting rate and difficulty too [HOXHUNT-FAILRATE-2026].

## 10. Sources

Keys cited above that are not in the YAML (all others are given in full there):

- ARXIV-2409.01378: "Content, Nudges and Incentives: Embedded Phishing Training", ACM CCS 2024 via arXiv, 2024-09-02, https://arxiv.org/abs/2409.01378
- NIST-SP80050-2024: NIST SP 800-50 Rev. 1, Building a Cybersecurity and Privacy Learning Program, 2024-09-12, https://csrc.nist.gov/pubs/sp/800/50/r1/ipd
- ENISA-ETL-2025: ENISA Threat Landscape 2025, 2025-10, https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025
- USENIX-ROMANCE-2026: "Love, Lies, and Language Models: Investigating AI's Role in Romance-Baiting Scams", USENIX Security 2026, 2026-08, https://www.usenix.org/conference/usenixsecurity26/presentation/gressel
- OKTA-AUTHSURVEY-2026: Okta with Yubico, 2026 Global State of Authentication survey, 2026-10-07, https://www.okta.com/newsroom/articles/global-state-of-authentication-2026-ai-phishing-resistance/
- PINDROP-DRI-2026: Pindrop, Deepfake Readiness Index 2026 (survey of 250 US security leaders), 2026-09-29, https://www.pindrop.com/resources/report/deepfake-readiness-index
- SANS-AWARENESS-2026: SANS 2026 Security Awareness and Culture Report webcast page (report not opened), 2026, https://www.sans.org/webcasts/sans-2026-security-awareness-culture-report
- CSD-OKTA-2026: Cybersecurity Dive, Okta report on AI and identity attacks, 2026-10-07, https://www.cybersecuritydive.com/news/phishing-authentication-ai-okta/832376/
- HN-PHISHTRAIN-2025: Hacker News discussion "Cybersecurity training programs don't prevent phishing scams" (community comments, not evidence), 2025-10-09, https://news.ycombinator.com/item?id=45529577
- JNJ-JOB-2026: Johnson & Johnson, Senior Manager, Cybersecurity Awareness Training (search-only; date not shown), 2026, https://www.careers.jnj.com/en/jobs/r-092295/senior-manager-cybersecurity-awareness-training/
