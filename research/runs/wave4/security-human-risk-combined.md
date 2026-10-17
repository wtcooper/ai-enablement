# Human risk: combined deep dive (practice, discourse, governance and evidence)

Archetype: security. Module: human-risk. Angle: combined. Compiled 2026-10-17. Working files were kept in a private `mktemp -d` folder. Web search was used 10 times (UCSD study location, Black Hat 2026 lineup, Ponemon/DTEX insider cost, human-risk analyst framing, SANS awareness report, fake-candidate hiring, deepfake payment fraud, one job posting, KnowBe4 agents, phishing-simulation criticism, DEF CON 34 vishing, help-desk social engineering, ScamBench results). Everything else was fetched with curl, `pdftotext` or the r.jina.ai mirror. Items marked `search-only` were seen only in search results.

## 1. Summary

- **Public evidence is thin and mostly vendor-authored on the defender side, and strong on the attacker side.** Peer-reviewed or regulator-grade measurement exists for what AI does to attackers' success (LLM spear phishing roughly 2.7 times the click rate of generic lures; AI voice scams with up to 36% compliance in one survey experiment). Independent measurement of AI-based defender tooling in this module (personalised training, AI phishing triage, AI insider detection) is close to absent.
- **The one rigorous field trial of classic training found little effect.** A randomised, 8-month study of about 19,500 UC San Diego Health employees found no significant link between recent annual awareness training and simulation failure, and embedded training reduced failure by only 2% in absolute terms (`UCSD-PHISHTRAIN-2025`). Vendors now answer with "human risk management" (behaviour signals, adaptive content, nudges), but the named-customer evidence for that shift is vendor-published (Qualcomm, Avanade, Uber, all via Hoxhunt pages).
- **Where AI changes defender work with the best evidence:** user-reported-phishing triage (Avanade: vendor-published 900 SOC hours a month saved), brand and executive impersonation takedown (ARK Invest with Doppel: median domain resolution 5.5 hours), and behavioural email security replacing a secure email gateway (Valvoline with Abnormal). All three are vendor-published customer stories.
- **Insider risk is split in two.** Cost and programme data come from a vendor-sponsored survey (Ponemon/DTEX: USD 19.5M average annual cost, 42% using AI for detection). The fastest-moving real-world case is the DPRK fake-IT-worker scheme: US charges on 2026-10-14 describe an operation that affected more than 70 US companies, and ENISA's 2026 landscape ties a rising insider share to it. Defender-side AI evidence there is absent; the sources recommend identity checks and HR/SOC coordination.
- **Governance is the clearest public signal.** NYDFS tells regulated firms to train all staff on AI-enhanced social engineering, including voice and video impersonation exercises (`NYDFS-AI-2024`); FinCEN issued a deepfake alert (`FINCEN-DEEPFAKE-2024`); the FBI recorded 22,364 AI-related complaints and USD 893M adjusted losses in 2025 (`FBI-IC3-2026`).

Use cases by grade: A = 6, B = 3, C = 7, D = 5 (21 total).

## 2. Use cases

```yaml
- id: security-human-risk-01
  title: Targeting adaptive phishing training at the riskiest employees first, then rolling out company-wide
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "A small group of repeat clickers is said to cause most phishing incidents, and blanket annual training treats everyone the same. Qualcomm says 4% of users are responsible for 80% of its phishing incidents (the case page attributes the pattern to Cyentia research)."
  solution: "Qualcomm picked its 1,000 highest-risk employees (people who had failed 3 or more of the previous 6 exercises and who worked in frequently targeted roles such as accounts payable, sales/marketing or executive support) and enrolled them in Hoxhunt's gamified, reward-based adaptive phishing programme. Their results were compared with the rest of the company in periodic benchmark phishing tests. The result won support for a rollout to about 48,000 employees."
  outcomes:
    - { lever: risk, description: "Baseline phishing-simulation failure rate of the selected cohort before enrolment", figure: "30-50% failure rate, negligible reporting", measures: "failure rate of the 1,000 selected employees in Qualcomm's earlier simulations, as stated on the Hoxhunt case page; period not stated", provenance: vendor-published, source_ref: HOXHUNT-QUALCOMM-2023 }
    - { lever: risk, description: "Change in simulation failure rate after the company-wide rollout", figure: "6X improvement (case-page text); 3.5x drop in failure rate and 73% increase in reporting (summary card on the case-study index)", measures: "ratio of failure rate before versus after rollout on simulated phishing; the page gives two different headline figures and does not state the baseline, period or sample", provenance: vendor-published, source_ref: HOXHUNT-QUALCOMM-2023 }
  prerequisites:
    - "History of simulation results and role data to identify the highest-risk users"
    - "A training platform that supports gamified, reward-based programmes rather than penalties"
    - "Support from leadership obtained through a cohort experiment before the general rollout (HOXHUNT-QUALCOMM-2023, Solution)"
  risks_and_guardrails:
    - "The only large randomised field trial found (UCSD Health, 19,500 employees) reported limited value from embedded phishing training and stressed the need for a no-training control group; Qualcomm's page describes comparison against the rest of the company, not a randomised control (UCSD-PHISHTRAIN-2025, Abstract and Section 1)"
    - "Vendor's own blog says a failure rate only means something next to simulation difficulty and reporting rate (HOXHUNT-FAILRATE-2026, opening summary)"
  human_checkpoints:
    - "Security team selects the cohort and decides on the general rollout after the cohort comparison (HOXHUNT-QUALCOMM-2023)"
  role_evolution: "The page describes replacing 'phishing prison' with a reward-based programme for repeat clickers; it does not describe changes to security-team roles."
  evidence_grade: A
  sources:
    - { ref: HOXHUNT-QUALCOMM-2023, title: "How Qualcomm used Hoxhunt to turn their 1,000 highest-risk employees into their top performers", publisher: Hoxhunt, type: vendor, url: "https://hoxhunt.com/case-studies/how-qualcomm-used-targeted-security-awareness-training-for-employees", date: 2023, access: full, locator: "Challenge; Solution; 'How did Qualcomm start transforming their culture'; 'CSO50 Award-Winning Results'" }
    - { ref: UCSD-PHISHTRAIN-2025, title: "Understanding the Efficacy of Phishing Training in Practice", publisher: IEEE Symposium on Security and Privacy (UC San Diego, University of Chicago, UC San Diego Health), type: academic, url: "https://sysnet.ucsd.edu/~voelker/pubs/phishtrain-oakland25.pdf", date: 2025-05, access: full, locator: "Abstract; Section 1 findings list" }
    - { ref: HOXHUNT-FAILRATE-2026, title: "What is a good phishing failure rate?", publisher: Hoxhunt, type: vendor, url: "https://hoxhunt.com/blog/what-is-a-good-phishing-failure-rate", date: 2026-03-09, access: full, locator: "Opening summary" }
  last_reviewed: 2026-10-17
  notes: "Case page is undated; the year 2023 comes from its statement of a general rollout in August 2023. Publication date of the page was not found. Figures are vendor-published and no control group is described."

- id: security-human-risk-02
  title: Automated triage of employee-reported suspicious emails
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [transaction-processing]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Once training works, employees report more suspicious emails. Avanade says its people 'began reporting far more threats', a volume that was hard to analyse manually, and Microsoft describes analysts facing a continuous stream of user-reported emails."
  solution: "Avanade used Hoxhunt's response platform to categorise and prioritise reported messages (legitimate email, spam, threats, incidents) automatically. Microsoft documents a Phishing Triage Agent in Defender that uses LLM-based analysis, URL and file detonation, screenshot analysis and threat intelligence to classify user-reported phishing as real threat or false positive, with a natural-language rationale and analyst feedback."
  outcomes:
    - { lever: capacity, description: "Monthly SOC analysis time saved by automated response handling", figure: "over 900 hours a month; described as up to 5 full-time analysts", measures: "SOC analyst hours of analysis saved per month, as stated on the Hoxhunt case page for Avanade; method of calculation described only as 'by one calculation'", provenance: vendor-published, source_ref: HOXHUNT-AVANADE-2026 }
    - { lever: quality, description: "Reduction in false positives and incident escalations due to the response platform", figure: "98%", measures: "stated on the case page as a reduction in false positives and incident escalations; baseline and period not stated", provenance: vendor-published, source_ref: HOXHUNT-AVANADE-2026 }
    - { lever: quality, description: "Three-month benchmark of two 1,000-user cohorts, Hoxhunt versus Avanade's previous awareness tool", figure: "43% higher resilience ratio; 11% lower failure rate; 27% higher reporting rate; 37% more simulations sent", measures: "resilience ratio is defined on the page as engagement divided by phishing-simulation failure rate; cohorts of 1,000 users each; the comparison was run by Avanade as a proof of concept", provenance: vendor-published, source_ref: HOXHUNT-AVANADE-2026 }
  prerequisites:
    - "A one-click report button integrated with the mail platform (Microsoft: 'Monitor reported messages in Outlook' must be enabled)"
    - "For Microsoft's agent: Defender for Office 365 Plan 2, Security Copilot capacity (SCUs), unified RBAC and the 'Email reported by user as malware or phish' alert policy; alerts resolved by tuning rules are not triaged (MSFT-PHISHTRIAGE-2026, prerequisites)"
  risks_and_guardrails:
    - "Microsoft says the agent needs its own identity with least-privilege permissions and recommends a dedicated agent identity (MSFT-PHISHTRIAGE-2026, identity section)"
    - "Verdicts are explained in natural language and analysts can give feedback, so wrong classifications can be corrected (MSFT-PHISHTRIAGE-2026, key capabilities)"
    - "No independent false-negative or override-rate data was found for either product"
  human_checkpoints:
    - "Analysts review the agent's rationale and can feed back on classifications (MSFT-PHISHTRIAGE-2026)"
  role_evolution: "Avanade's page says the platform did the work of over 5 full-time threat analysts per month and let the team 'focus on real threats' (HOXHUNT-AVANADE-2026, Overview); no redeployment details are given."
  evidence_grade: A
  sources:
    - { ref: HOXHUNT-AVANADE-2026, title: "How Avanade reduces human cyber risk and saves over 900 hours of SOC analysis per month", publisher: Hoxhunt, type: vendor, url: "https://hoxhunt.com/case-studies/avanade-reduced-cyber-risk-and-saved-5-soc-analyst-ftes-with-hoxhunt", date: 2026, access: full, locator: "Key takeaways; 'The Hoxhunt challenge benchmark study'" }
    - { ref: MSFT-PHISHTRIAGE-2026, title: "Microsoft Security Copilot Phishing Triage Agent in Microsoft Defender", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/defender-xdr/phishing-triage-agent", date: 2026-07-02, access: full, locator: "Overview; key capabilities; prerequisites; agent identity" }
  last_reviewed: 2026-10-17
  notes: "Overlaps with the security operations module (the same Microsoft agent is covered there). Avanade page is undated; the year 2026 reflects only that the page is currently listed; first-publication date not found. Microsoft's page notes the expanded alert coverage of the agent is in preview; no Microsoft customer figures were found."

- id: security-human-risk-03
  title: Behaviour-signal-driven human risk management with just-in-time micro-training and nudges
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [data-reporting, document-production]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Compliance-based annual awareness training does not show risk reduction. Uber wanted a human risk management programme for over 25,000 users with a two-person team and no existing playbook."
  solution: "Uber and Hoxhunt co-developed a programme that takes behavioural signals (phishing simulation outcomes, incident response data, vulnerability and bug tickets, data-handling events, policy exceptions, endpoint and network telemetry, external threat intelligence) and triggers targeted micro-learning and nudges at the moment of risk. The page says content is selected 'with AI capabilities' by role, behaviour pattern and observed risk. Hoxhunt markets the resulting Behavior Risk Console, which combines Hoxhunt, Microsoft Defender, CrowdStrike, Zscaler and other signals into per-employee, team and organisation views."
  outcomes:
    - { lever: experience, description: "Training completion after moving from forced compliance to voluntary participation", figure: "60% to over 90%", measures: "security-training completion as stated on the case page; user base and period not stated", provenance: vendor-published, source_ref: HOXHUNT-UBER-2026 }
    - { lever: risk, description: "Simulated threat reporting", figure: "3-fold increase", measures: "simulated threat reporting as stated on the case page; baseline not stated", provenance: vendor-published, source_ref: HOXHUNT-UBER-2026 }
    - { lever: experience, description: "Programme sentiment", figure: "96% found training valuable; 98% reported confidence in making secure decisions", measures: "share of survey respondents, as stated on the case page; sample size and response rate not stated", provenance: vendor-published, source_ref: HOXHUNT-UBER-2026 }
  prerequisites:
    - "Integrations that bring security tooling signals into one behavioural view (HOXHUNT-BRC-2026)"
    - "Willingness to use employee behaviour data across detection, ticketing and endpoint systems"
  risks_and_guardrails:
    - "Combining behaviour signals about named employees is workplace monitoring; the UK ICO has monitoring-of-workers guidance under UK GDPR, currently flagged as under review after the Data (Use and Access) Act (ICO-MONITORING-2023, banner)"
    - "The EU AI Act prohibits AI that infers emotions of people in the workplace (EC-AIACT-2026, prohibited practices list); the Uber page does not describe such inference"
    - "Hoxhunt's product page says AI tools operate under the same governance framework as the rest of its platform (HOXHUNT-BRC-2026)"
  human_checkpoints:
    - "Security team defines escalation playbooks and intervention triggers (HOXHUNT-BRC-2026)"
  role_evolution: "Uber's two-person awareness team (Head of Security Diligence, Analytics, Vendor Risk, and Awareness and Head of Security, Global Risk & Compliance lead the programme) manages a signal-and-intervention system rather than a training calendar; self-service tools are said to cut tier-1 policy inquiries (HOXHUNT-UBER-2026)."
  evidence_grade: A
  sources:
    - { ref: HOXHUNT-UBER-2026, title: "Uber reduces human risk with CSO Award-winning signal-driven behavior management", publisher: Hoxhunt, type: vendor, url: "https://hoxhunt.com/case-studies/uber-reduces-human-risk-with-signal-driven-behavior-management", date: 2026, access: full, locator: "Challenge; Solution; Key takeaways; behavioural signals list" }
    - { ref: HOXHUNT-BRC-2026, title: "Behavior Risk Console", publisher: Hoxhunt, type: vendor, url: "https://hoxhunt.com/product/behavior-risk-console", date: 2026, access: full, locator: "Product description and integrations" }
    - { ref: ICO-MONITORING-2023, title: "Employment practices and data protection: monitoring workers", publisher: UK Information Commissioner's Office, type: regulator, url: "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/", date: 2023-10, access: full, locator: "Page banner and contents" }
    - { ref: EC-AIACT-2026, title: "AI Act (regulatory framework for AI)", publisher: European Commission, type: regulator, url: "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai", date: 2026-10-17, access: full, locator: "Unacceptable risk list; application dates" }
  last_reviewed: 2026-10-17
  notes: "Uber page is undated; the year 2026 comes from its reference to a 'CSO 2026 Expert Panel'. ICO guidance year is from prior knowledge (the page shows no date). EC page date is the check date."

- id: security-human-risk-04
  title: LLM-generated and AI-agent-built awareness content and campaigns
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Content libraries have gaps for organisation-specific policies, new attacks and incidents; building modules takes days and waiting on a vendor takes longer."
  solution: "Hoxhunt's Content Studio (page dated 2026-06-24) turns a prompt and the customer's own documents into a draft training module; it says every module stays a draft until a person reviews and publishes it. KnowBe4 said in January 2026 that it has seven AIDA agents in market for human risk management, listing contextual phishing simulations, automated remedial training, policy-based quizzes and customised deepfakes. A controlled academic experiment tested LLM-generated phishing training."
  outcomes:
    - { lever: speed, description: "Vendor claim that modules can be created in minutes instead of days", figure: "minutes (no measurement)", measures: "vendor statement about authoring time; no sample or comparison given", provenance: vendor-published, source_ref: HOXHUNT-CONTENT-2026 }
    - { lever: quality, description: "Two controlled online studies (N=480) found pre-post learning gains from AI-generated training and no measurable advantage for complex psychometric personalisation over well-designed generic content", figure: "N=480 (Study 1 N=80; Study 2 N=400); effect sizes not captured from the abstract", measures: "participants' pre-post accuracy gains in an online experiment; this is knowledge gain, not real-world click or incident behaviour", provenance: independent, source_ref: ARXIV-2512.01893 }
    - { lever: capacity, description: "KnowBe4 says its agents are in use across more than 70,000 organisations", figure: "70,000+ organisations", measures: "company statement about organisations in which its agents are available or in use; no customer names or seat counts given", provenance: vendor-published, source_ref: SECURITYBRIEF-AIDA-2026 }
  prerequisites:
    - "Source policy and procedure documents in usable form"
    - "An awareness manager who reviews and publishes drafts"
  risks_and_guardrails:
    - "Hoxhunt: AI drafts, admins decide; modules remain drafts until published (HOXHUNT-CONTENT-2026)"
    - "TrainShield authors flag difficulty aligning generated content with user expectations (ARXIV-2608.02296, abstract)"
  human_checkpoints:
    - "A person reviews and publishes every generated module (HOXHUNT-CONTENT-2026)"
  role_evolution: "KnowBe4 says the aim is for staff to spend more time on higher-level risk decisions (SECURITYBRIEF-AIDA-2026); Hoxhunt describes the tool as an on-demand instructional design team for awareness managers (HOXHUNT-CONTENT-2026)."
  evidence_grade: C
  sources:
    - { ref: HOXHUNT-CONTENT-2026, title: "Content Studio creates customizable security awareness content", publisher: Hoxhunt, type: vendor, url: "https://hoxhunt.com/blog/content-studio-creates-customizable-security-awareness-content", date: 2026-06-24, access: full, locator: "Opening paragraphs; publishing control" }
    - { ref: SECURITYBRIEF-AIDA-2026, title: "KnowBe4 marks AIDA decade, names AI innovation VP", publisher: SecurityBrief UK, type: press, url: "https://securitybrief.co.uk/story/knowbe4-marks-aida-decade-names-ai-innovation-vp", date: 2026-01-30, access: full, locator: "Paragraphs 1-6" }
    - { ref: ARXIV-2512.01893, title: "Improving Phishing Resilience with AI-Generated Training: Evidence on Prompting, Personalization, and Duration", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2512.01893", date: 2025-12-01, access: full, locator: "Abstract" }
  last_reviewed: 2026-10-17
  notes: "Only the abstract of the academic study was read. KnowBe4's own history reported eight agents in other coverage (search-only), so the agent count is unresolved. No named customer outcome was found."

- id: security-human-risk-05
  title: Personalised, OSINT-driven spear-phishing simulations inside awareness programmes
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [review-assurance, research-synthesis]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: "Generic simulations may under-represent what attackers can now do cheaply. Researchers note spear phishing is about 0.1% of phishing emails but is linked to 66% of data breaches in one cited vendor study (USENIX-CZYBIK-2026, Introduction)."
  solution: "In a study run inside the phishing-awareness training of a partner university (TU Braunschweig) with 7,700 participants, the authors fed each participant's email address into web searches, generated a tailored email with an LLM, and compared click rates with generic lures. Another study ran three simulations across organisations ranging from small businesses to a multinational (over 71,000 emails) including an LLM-plus-OSINT lure. A vendor (Adaptive Security) lists 'OSINT & AI Email Spearphishing' among its simulation products."
  outcomes:
    - { lever: risk, description: "Click rate of LLM-personalised spear phishing versus generic phishing", figure: "10.0% (330 of 3,177 delivered) versus 3.7% for LLM generic (65 of 1,735 delivered) and 4.1% for manual generic (79 of 1,918 delivered)", measures: "participants who clicked the phishing link divided by emails delivered, in the paper's campaign table; manual spear phishing (100 sent, 99 delivered) reached 24.2%", provenance: independent, source_ref: USENIX-CZYBIK-2026 }
    - { lever: cost, description: "Marginal cost of personalisation per email", figure: "approximately USD 0.03", measures: "authors' stated cost of generating a personalised email", provenance: independent, source_ref: USENIX-CZYBIK-2026 }
    - { lever: risk, description: "LLM plus OSINT lure in one of the organisations", figure: "over 30% of opened emails led to a visit to the landing page", measures: "share of opened emails in one company that led to landing-page visits; organisations unnamed", provenance: independent, source_ref: ARXIV-2505.12104 }
  prerequisites:
    - "Approval from security office, administration and staff committee as in the university study; briefing and debriefing of participants (USENIX-CZYBIK-2026, Section 5.1)"
    - "A policy on what public personal information may be used"
  risks_and_guardrails:
    - "The study's lures covered a university workplace and may differ from corporate or government settings (USENIX-CZYBIK-2026, Section 5.1)"
    - "Sophos warns that 'unfair' simulations that use pretexts such as financial hardship or job security cross ethical lines and can cause stress (SOPHOS-PHAKE-2025)"
  human_checkpoints:
    - "Ethics and staff-committee review before launch; participants are briefed and debriefed (USENIX-CZYBIK-2026, Section 5.1)"
  role_evolution: "Authors recommend incorporating personalised phishing into awareness training and limiting public information linkable to email addresses (USENIX-CZYBIK-2026, Abstract); no role change is described."
  evidence_grade: B
  sources:
    - { ref: USENIX-CZYBIK-2026, title: "A Large-Scale Study of Personalized Phishing using Large Language Models", publisher: USENIX Security Symposium (BIFOLD, TU Berlin, Inria, Ruhr-University Bochum), type: academic, url: "https://www.usenix.org/system/files/usenixsecurity26-czybik.pdf", date: 2026-08, access: full, locator: "Abstract; Section 5.1; Section 6.1 and campaign table" }
    - { ref: ARXIV-2505.12104, title: "The Impact of Emerging Phishing Threats: Assessing Quishing and LLM-generated Phishing Emails against Organizations", publisher: AsiaCCS 2025 via arXiv, type: academic, url: "https://arxiv.org/abs/2505.12104", date: 2025-05-17, access: full, locator: "Abstract" }
    - { ref: ADAPTIVE-BLOG-2026, title: "Adaptive Security: homepage and blog index", publisher: Adaptive Security, type: vendor, url: "https://www.adaptivesecurity.com/", date: 2026-10-15, access: full, locator: "Product menu: Phishing Simulations (Realistic Email Phishing, Voice Call & SMS Phishing, OSINT & AI Email Spearphishing)" }
    - { ref: SOPHOS-PHAKE-2025, title: "Phake phishing: Phundamental or pholly?", publisher: Sophos, type: vendor, url: "https://www.sophos.com/en-us/blog/phake-phishing-phundamental-or-pholly", date: 2025-10-31, access: full, locator: "Opening list of common mistakes" }
  last_reviewed: 2026-10-17
  notes: "Grade B rather than A: the named-organisation measurement shows how susceptible staff are to LLM-personalised lures, not that using them in training reduces risk. The ethics point comes from a Sophos post, not from Hoxhunt. Adaptive date is the latest dated item on its blog index; the product menu itself is undated."

- id: security-human-risk-06
  title: Conversational vishing and smishing practice with AI-voice scenarios
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [review-assurance, client-interaction]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Employees are trained to scrutinise emails, but a live call demands instant reaction. A survey experiment (N=4,100) found overall compliance of 16.5% across five AI voice scam categories and up to 36% for a relative-in-distress scenario, and judged AI vishing economically viable where human-operated vishing at US wages is not."
  solution: "Hoxhunt describes (blog dated 2025-10-24) an immersive voice-phishing training capability in which employees practise handling attackers' conversational tactics on live phone calls; Adaptive lists voice-call and SMS phishing simulations; Infosec markets AI agents that simulate deepfake voice attacks and give post-call coaching (the Infosec claim is search-only)."
  outcomes:
    - { lever: risk, description: "none published for the training itself; no customer names or results found", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: HOXHUNT-VOICE-2025 }
  prerequisites:
    - "Employee consent and notice for simulated calls"
    - "Out-of-band verification procedures that staff are trained to apply"
  risks_and_guardrails:
    - "Caller persuasiveness, not whether the caller was believed to be human, was the strongest predictor of compliance in the survey experiment, so training on spotting 'robotic' voices is unlikely to be sufficient (ARXIV-2607.09970, abstract)"
    - "Humans struggle to tell AI-generated scam calls from human voices (BSIDESLV-2026, 'Devising and Detecting Voice Phishing' abstract)"
  human_checkpoints:
    - "Awareness team reviews scenario design and results"
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
    - { ref: HOXHUNT-VOICE-2025, title: "Hoxhunt Voice Phishing Training", publisher: Hoxhunt, type: vendor, url: "https://hoxhunt.com/blog/hoxhunt-voice-phishing-training", date: 2025-10-24, access: full, locator: "Opening and 'Practice makes perfect' sections" }
    - { ref: ARXIV-2607.09970, title: "Evaluating AI Models' Capability to Automate Voice Phishing Attacks", publisher: Expert Systems with Applications vol. 332 via arXiv, type: academic, url: "https://arxiv.org/abs/2607.09970", date: 2026-07-10, access: full, locator: "Abstract" }
    - { ref: BSIDESLV-2026, title: "BSides Las Vegas 2026 talk list", publisher: BSides Las Vegas, type: conference, url: "https://bsideslv.org/talks", date: 2026-08, access: full, locator: "'Devising and Detecting Voice Phishing' (Ground Truth, Monday 10:00)" }
  last_reviewed: 2026-10-17
  notes: "BSides LV month is from the landscape file (early August 2026); exact dates were not verified. Infosec claim is search-only and not used as an outcome."

- id: security-human-risk-07
  title: Deepfake and executive-impersonation drills for finance, help desk and executive staff
  archetype: security
  module: human-risk
  function: finance-accounting
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Arup confirmed that a Hong Kong employee paid out about USD 25 million after a video call with deepfake colleagues; the police account says the worker's initial phishing suspicion was put aside after the call. The FBI recorded 135 BEC complaints that reference AI, with USD 30.3M in AI-related BEC losses, in 2025 (BEC overall: over USD 3.0 billion)."
  solution: "NYDFS tells regulated entities that social-engineering training, including on deepfakes, can be delivered through simulated phishing and voice and video impersonation exercises and should cover verifying unexpected money-transfer requests. Vendors (KnowBe4 'customised deepfakes for education'; Adaptive deepfake training) sell simulations; none reported outcomes."
  outcomes:
    - { lever: risk, description: "none published; no tested reduction in deepfake-enabled payment fraud from drills found", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: SECURITYBRIEF-AIDA-2026 }
  prerequisites:
    - "Documented verification procedures for payment, credential and data requests received by phone, video or email"
    - "Executive consent to use their likeness in simulations"
  risks_and_guardrails:
    - "NYDFS expects training to address when human review and oversight must be included in verification procedures (NYDFS-AI-2024, training section)"
    - "A callback or video check can itself be compromised when it uses a channel or number supplied by the requester (general practice; the sources read do not give a primary statement)"
  human_checkpoints:
    - "Human review and oversight inside verification procedures for money transfers (NYDFS-AI-2024)"
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
    - { ref: NYDFS-AI-2024, title: "Industry letter: Cybersecurity risks arising from artificial intelligence and strategies to combat related risks", publisher: New York State Department of Financial Services, type: regulator, url: "https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks", date: 2024-10-16, access: full, locator: "Training paragraphs; social engineering section" }
    - { ref: CNN-ARUP-2024, title: "Arup revealed as victim of USD 25 million deepfake scam involving Hong Kong employee", publisher: CNN, type: press, url: "https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk", date: 2024-05-17, access: full, locator: "Paragraphs 1-8" }
    - { ref: FBI-IC3-2026, title: "2025 IC3 Annual Report", publisher: FBI Internet Crime Complaint Center, type: regulator, url: "https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf", date: 2026-04, access: full, locator: "pp. 39-43, Artificial Intelligence (AI) Used in Cybercrime; AI references tables" }
    - { ref: SECURITYBRIEF-AIDA-2026, title: "KnowBe4 marks AIDA decade, names AI innovation VP", publisher: SecurityBrief UK, type: press, url: "https://securitybrief.co.uk/story/knowbe4-marks-aida-decade-names-ai-innovation-vp", date: 2026-01-30, access: full, locator: "Agent function list" }
  last_reviewed: 2026-10-17
  notes: "NYDFS date comes from the URL (il20241016); the page text did not show it. IC3 report date: PDF creation date 2026-04-16. Arup's figure (about USD 25 million) is the company-confirmed loss reported by CNN; HKD 200 million in 15 transfers per police via RTHK."

- id: security-human-risk-08
  title: Behavioural-AI email security that replaces the secure email gateway and answers employee reports
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [transaction-processing, review-assurance]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Valvoline used a secure email gateway plus Microsoft 365 native security plus an API-based tool, yet spear phishing and invoice fraud (from USD 5,000 to millions, per the quoted security director) still reached inboxes despite awareness training."
  solution: "Valvoline moved to Abnormal's API-based behavioural AI, removed its secure email gateway, and uses an AI Security Mailbox that gives users personalised replies to their report submissions."
  outcomes:
    - { lever: cost, description: "Loss avoided by stopping one recurring invoice fraud attack", figure: "USD 600K", measures: "figure shown as a headline metric on the customer story ('Saved by stopping a recurring invoice fraud attack'); method not described", provenance: vendor-published, source_ref: ABNORMAL-VALVOLINE-2026 }
    - { lever: capacity, description: "Analyst hours saved on email and solution management", figure: "480 hours per month", measures: "headline metric on the customer story; the security director also says 4-5 analysts had spent 90% of each day on email-related tasks", provenance: vendor-published, source_ref: ABNORMAL-VALVOLINE-2026 }
  prerequisites:
    - "Cloud mailbox API integration; a proof of value on the customer's own mail"
  risks_and_guardrails:
    - "All figures are vendor-published; no independent false-positive or missed-attack rates were found"
    - "Customer says awareness training did not stop mistakes ('humans will always make mistakes'), which is the argument for removing reliance on user judgement"
  human_checkpoints:
    - "Analysts still handle reports and dashboards; the security team uses the dashboard to identify attack trends (ABNORMAL-VALVOLINE-2026)"
  role_evolution: "Analyst time moves away from manual investigation and remediation to other tasks (ABNORMAL-VALVOLINE-2026)."
  evidence_grade: A
  sources:
    - { ref: ABNORMAL-VALVOLINE-2026, title: "Valvoline Replaces SEG with Autonomous AI to Stop Evolving Threats", publisher: Abnormal AI, type: vendor, url: "https://abnormal.ai/customers/stories/valvoline", date: 2026, access: full, locator: "Headline metrics; challenge; results quotes" }
  last_reviewed: 2026-10-17
  notes: "Page is undated; the year reflects only the page footer. First-publication date not found. The USD 600K and 480 hours figures were read from the page's embedded data and match the visible labels."

- id: security-human-risk-09
  title: Post-delivery agentic re-analysis and auto-remediation of inbound email
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [review-assurance, transaction-processing]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: "Messages that pass native filtering still reach inboxes and rely on users to notice them."
  solution: "Adaptive Security's blog index lists 'Adaptive Email Security (Beta)' on 2026-04-16, and a 2026-08-26 post calling it the company's fastest-growing product; the homepage says it re-analyses every inbound message after native filtering and remediates automatically."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: ADAPTIVE-BLOG-2026 }
  prerequisites:
    - "Mailbox API access (not detailed in the sources read)"
  risks_and_guardrails:
    - "No accuracy or false-positive data published; product described as beta in April 2026"
  human_checkpoints:
    - "Not described"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: ADAPTIVE-BLOG-2026, title: "Adaptive Security blog index and homepage", publisher: Adaptive Security, type: vendor, url: "https://www.adaptivesecurity.com/blog", date: 2026-08-26, access: full, locator: "Phishing Triage listing (2026-04-16 and 2026-08-26 items); homepage Agentic Email Security description" }
  last_reviewed: 2026-10-17
  notes: "Only titles and product summaries were read; post bodies were not opened."

- id: security-human-risk-10
  title: AI-driven detection and automated takedown of brand and executive impersonation
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [transaction-processing, research-synthesis]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "ARK Invest had a high-profile social media presence and faced impersonation across LinkedIn, Instagram, WhatsApp and Telegram. Before the tool, its brand marketing manager says it took 'days to weeks' to identify and remove many scams, and the firm received hundreds of calls and emails each year from concerned people."
  solution: "ARK adopted Doppel's platform, which detects impersonation across domains, social media and the dark web, links signals into a threat graph and acts on takedowns rather than only flagging."
  outcomes:
    - { lever: speed, description: "Median domain resolution time", figure: "5.5 hours", measures: "median time to resolve domain impersonation alerts for ARK, as stated on the case study", provenance: vendor-published, source_ref: DOPPEL-ARK-2026 }
    - { lever: quality, description: "Takedown success rate", figure: "98%", measures: "stated on the case study as takedown success rate; denominator not stated", provenance: vendor-published, source_ref: DOPPEL-ARK-2026 }
    - { lever: risk, description: "Impersonations and scams reported directly to ARK", figure: "about 400 in 2024; roughly halved in 2025", measures: "reports the firm heard about directly, as quoted from its brand marketing manager", provenance: self-reported, source_ref: DOPPEL-ARK-2026 }
  prerequisites:
    - "Defined brand and executive assets to protect; takedown authorisations and registrar/platform relationships"
  risks_and_guardrails:
    - "All figures come from the vendor's customer story; reported-case counts depend on public reporting and may not equal total impersonation"
  human_checkpoints:
    - "Not described beyond ARK choosing the partnership"
  role_evolution: "The case says the platform relieved the team of manual takedown work so it can focus on other work (DOPPEL-ARK-2026)."
  evidence_grade: A
  sources:
    - { ref: DOPPEL-ARK-2026, title: "From Weeks to Minutes: Why ARK Invest Chose Doppel to Automate Social Engineering Defense", publisher: Doppel, type: vendor, url: "https://www.doppel.com/customers/ark-invest", date: 2026-01-16, access: full, locator: "Sections 'Fighting Machine Speed with Machine Speed' and 'Quantifiable Risk Reduction'" }
  last_reviewed: 2026-10-17
  notes: "Sits between human-risk and fraud/brand protection; see routed items."

- id: security-human-risk-11
  title: LLM scam-baiting honeypots to extract mule accounts and map scam workflows
  archetype: security
  module: human-risk
  function: risk-compliance-legal
  work_types: [research-synthesis]
  pattern: research-brief
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Detection, user training and reactive takedown do not remove the infrastructure scammers rely on (mule bank accounts and wallets); long-running trust scams such as pig butchering are hard to study."
  solution: "A research system used LLMs to hold realistic conversations with scammers over weeks to months and extract payment details and tactics. Over five months it initiated more than 2,600 engagements (more than 18,700 messages). A BSides Las Vegas 2026 talk describes a similar system sustaining thousands of dialogues and finding that most scammers use a cross-platform jump."
  outcomes:
    - { lever: risk, description: "Information disclosure rate (sensitive financial information such as mule accounts extracted)", figure: "about 32%", measures: "share of scammer engagements in which the system extracted financial information, per the authors' IDR measure; 2,600+ engagements over five months", provenance: independent, source_ref: ARXIV-2509.08493 }
    - { lever: quality, description: "Human acceptance rate of LLM-generated replies", figure: "about 70%", measures: "alignment between LLM replies and human operator preferences, per the authors' HAR measure", provenance: independent, source_ref: ARXIV-2509.08493 }
    - { lever: quality, description: "Engagement takeoff problem", figure: "48.7%", measures: "share of scammers who responded to the initial seed message", provenance: independent, source_ref: ARXIV-2509.08493 }
  prerequisites:
    - "Legal and ethics review for deceptive engagement with criminals"
    - "A route to pass extracted accounts to banks, exchanges or law enforcement (not detailed in the sources read)"
  risks_and_guardrails:
    - "System struggled to get scammers to respond at all; authors call for refinement (ARXIV-2509.08493, abstract)"
  human_checkpoints:
    - "Human operators compared with LLM replies in the evaluation (ARXIV-2509.08493)"
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: ARXIV-2509.08493, title: "Send to which account? Evaluation of an LLM-based Scambaiting System", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2509.08493", date: 2025-09-10, access: full, locator: "Abstract" }
    - { ref: BSIDESLV-2026, title: "BSides Las Vegas 2026 talk list", publisher: BSides Las Vegas, type: conference, url: "https://bsideslv.org/talks", date: 2026-08, access: full, locator: "'Victim as a Service: Engaging with Trust Based Scams using AI' (Ground Truth, Monday 11:00)" }
  last_reviewed: 2026-10-17
  notes: "Graded B, not A: outcomes are measured but the deploying organisation was not captured from the sources read (affiliations not retrieved). Mostly consumer-scam context; relevant to organisations as banks, telcos and platforms. Possibly better placed with fraud or threat intelligence."

- id: security-human-risk-12
  title: LLM-based insider-threat log analysis
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Dedicated staff cannot manually examine the volume of logs needed to catch insider threats."
  solution: "RedChronos (authors' system) analyses logs with an LLM using weighted voting and a genetic algorithm with LLM mutations. A separate 2026 framework generates structured risk indicators from per-user timelines with retrieval of the user's history and classifies them zero-shot."
  outcomes:
    - { lever: capacity, description: "Reduction in the need for manual intervention in log review at Xiaohongshu's SOC", figure: "approximately 90%", measures: "authors' statement of reduced manual intervention in security log reviews at the Xiaohongshu Security Operation Center; baseline and period not given in the abstract", provenance: self-reported, source_ref: ARXIV-2503.02702 }
    - { lever: quality, description: "Benchmark F1 gain over the previous best LLM framework on a public insider-threat dataset", figure: "+11.40 percentage points on CERT r5.2", measures: "F1-score of the best configuration versus GABM on the CERT r5.2 benchmark dataset (a public benchmark, not production data)", provenance: independent, source_ref: ARXIV-2608.16508 }
  prerequisites:
    - "Centralised user-activity logs (endpoint, email, file, logon)"
    - "A legal basis and governance for monitoring staff"
  risks_and_guardrails:
    - "Benchmark datasets are not production data; no false-positive or override rates at the production site were published in the abstract"
    - "Workplace monitoring is regulated: ICO guidance on monitoring workers (ICO-MONITORING-2023); EU AI Act high-risk rules for employment-related use cases apply from 2027-12-02 (EC-AIACT-2026); whether a given insider-risk tool falls inside them is not addressed in the sources read"
  human_checkpoints:
    - "Not described in the abstracts"
  role_evolution: "Not described."
  evidence_grade: A
  sources:
    - { ref: ARXIV-2503.02702, title: "RedChronos: A Large Language Model-Based Log Analysis System for Insider Threat Detection in Enterprises", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2503.02702", date: 2025-03-04, access: full, locator: "Abstract" }
    - { ref: ARXIV-2608.16508, title: "LLMs for Zero-Shot Threat Detection via Structured Risk Indicators", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2608.16508", date: 2026-08-17, access: full, locator: "Abstract" }
    - { ref: EC-AIACT-2026, title: "AI Act (regulatory framework for AI)", publisher: European Commission, type: regulator, url: "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai", date: 2026-10-17, access: full, locator: "Application timeline" }
  last_reviewed: 2026-10-17
  notes: "Only abstracts were read. The abstract does not say whether RedChronos runs in production or in a trial at Xiaohongshu; maturity set conservatively to piloting. The grade A rests on a single self-reported figure; treat as a low-confidence A."

- id: security-human-risk-13
  title: Insider-risk programmes with AI-assisted detection and risk scoring
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "Negligent or mistaken insiders are the largest driver of insider-risk cost; incidents take on average 67 days to contain."
  solution: "Microsoft documents Purview Insider Risk Management, which correlates signals from Microsoft 365 and Microsoft Graph into policies, alerts and cases, pseudonymises users by default and applies role-based access and audit logs. In the Ponemon/DTEX survey, 42% of organisations use AI to detect or prevent insider risks."
  outcomes:
    - { lever: risk, description: "Organisations with a formal insider-risk programme avoided incidents and costs", figure: "average of 7 incidents and USD 8.2M in breach-related costs avoided per year", measures: "survey-based estimate among 354 organisations that had one or more material insider incidents in the past year; 63% have a formal programme", provenance: vendor-published, source_ref: HELPNET-PONEMON-2026 }
    - { lever: cost, description: "Average annual cost of insider risk", figure: "USD 19.5M per organisation", measures: "Ponemon Institute estimate for the 354 surveyed organisations in 2025; negligent insiders USD 10.3M, malicious USD 4.7M, credential theft USD 4.5M", provenance: vendor-published, source_ref: HELPNET-PONEMON-2026 }
    - { lever: risk, description: "AI use for detection or prevention", figure: "42%", measures: "share of surveyed organisations that use AI to detect or prevent insider risks; reduced false positives were among the benefits most often cited", provenance: vendor-published, source_ref: HELPNET-PONEMON-2026 }
  prerequisites:
    - "Policy templates and role-based access for investigators; privacy-by-design configuration (PURVIEW-IRM-2026)"
  risks_and_guardrails:
    - "Survey is sponsored by DTEX, a vendor of insider-risk software; Ponemon is the research firm"
    - "Dates conflict inside the same article: containment time falls from 86 days in 2023 to 67 days in 2025, while the DTEX CTO quote says 81 to 67 days"
    - "Monitoring-of-workers rules (ICO-MONITORING-2023)"
  human_checkpoints:
    - "Risk analysts act on cases and escalate to eDiscovery where needed (PURVIEW-IRM-2026)"
  role_evolution: "Not described beyond risk analysts managing cases."
  evidence_grade: C
  sources:
    - { ref: HELPNET-PONEMON-2026, title: "The USD 19.5 million insider risk problem", publisher: Help Net Security (reporting the Ponemon Institute and DTEX 2026 Cost of Insider Risks Global Report), type: survey, url: "https://www.helpnetsecurity.com/2026/02/26/insider-risk-costs-2026/", date: 2026-02-26, access: full, locator: "Paragraphs 1-4, 8-14" }
    - { ref: PURVIEW-IRM-2026, title: "Microsoft Purview Insider Risk Management", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/purview/insider-risk-management", date: 2026-06-26, access: full, locator: "Overview; workflow" }
    - { ref: ICO-MONITORING-2023, title: "Employment practices and data protection: monitoring workers", publisher: UK Information Commissioner's Office, type: regulator, url: "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/", date: 2023-10, access: full, locator: "Page banner and contents" }
  last_reviewed: 2026-10-17
  notes: "The original report and the DTEX press release were not opened (press release blocked); figures are from Help Net Security's report of the study."

- id: security-human-risk-14
  title: Shadow-AI visibility and point-of-risk coaching ("audit and educate" instead of block)
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [data-reporting, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: "Employees put internal documents, source code and meeting content into public AI tools and AI meeting assistants; AI browsers and agents can bypass traditional logging."
  solution: "DTEX's CTO describes shifting from a block-first approach to an audit and educate approach with prompt inspection and real-time nudges. Adaptive lists an 'AI Governance' product (live feed of risky prompts across AI tools, with policy enforcement and coaching). KnowBe4 lists an Agent Risk Manager browser extension that discovers new and unknown domains and lets admins block, warn or allow them."
  outcomes:
    - { lever: speed, description: "Claimed effect of audit-and-educate on containment time", figure: "17% reduction, from 81 to 67 days (CTO statement)", measures: "average days to contain an insider incident, as claimed by DTEX's CTO; the same article gives 86 days for 2023", provenance: vendor-published, source_ref: HELPNET-PONEMON-2026 }
  prerequisites:
    - "Inventory of sanctioned and unsanctioned AI tools; acceptable-use policy"
  risks_and_guardrails:
    - "Prompt inspection captures employee content; privacy and monitoring rules apply (ICO-MONITORING-2023)"
    - "Only a small share of surveyed organisations classify AI agents as equivalent to human insiders (HELPNET-PONEMON-2026)"
  human_checkpoints:
    - "Not described"
  role_evolution: "DTEX argues insider-risk programmes should treat AI agents as operational identities with defined access controls (HELPNET-PONEMON-2026)."
  evidence_grade: C
  sources:
    - { ref: HELPNET-PONEMON-2026, title: "The USD 19.5 million insider risk problem", publisher: Help Net Security, type: survey, url: "https://www.helpnetsecurity.com/2026/02/26/insider-risk-costs-2026/", date: 2026-02-26, access: full, locator: "Paragraphs on shadow AI and CTO quotes" }
    - { ref: ADAPTIVE-BLOG-2026, title: "Adaptive Security homepage", publisher: Adaptive Security, type: vendor, url: "https://www.adaptivesecurity.com/", date: 2026-10-15, access: full, locator: "AI Governance section" }
  last_reviewed: 2026-10-17
  notes: "Partly belongs to the data-privacy module; see routed items. KnowBe4 Agent Risk Manager is from the KnowBe4 press listing (not opened beyond its listing line)."

- id: security-human-risk-15
  title: Identity and liveness verification of remote candidates, new hires and contractors (fake IT worker defence)
  archetype: security
  module: human-risk
  function: people-hr
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "The FBI says North Korean IT workers have used AI and face-swapping technology during video job interviews. KnowBe4 hired one: four video interviews, a background check and reference checks passed because the identity was a real, stolen US identity and the photo was AI-enhanced."
  solution: "KnowBe4 detected the hire when EDR flagged malware loading on the shipped laptop; its SOC called the new hire, and the company then published a ten-point list of hiring-process changes (separate post, not opened). The FBI's advice: identity verification during interviewing, onboarding and throughout employment; cross-check HR systems for applicants with the same resume or contact details; educate HR staff and hiring managers; verify staffing firms' hiring practices. DPRK RevGen enforcement is continuing."
  outcomes:
    - { lever: risk, description: "none published for AI-based detection; the sources give process advice and enforcement results, not defender effectiveness figures", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: KNOWBE4-NKHIRE-2024 }
  prerequisites:
    - "HR, security operations and IT shipping addresses aligned; endpoint detection on new laptops from day one"
  risks_and_guardrails:
    - "Laptop-farm schemes route the work through US-based facilitators; GTIG also reports IT workers targeting bring-your-own-device setups from January 2025 (GTIG-DPRKIT-2025)"
    - "The US indictment describes a roughly six-year operation affecting more than 70 US companies (CSD-DPRK-2026)"
  human_checkpoints:
    - "HR interview and onboarding steps with identity checks; SOC call to the new hire on anomalous activity (KNOWBE4-NKHIRE-2024)"
  role_evolution: "HR staff and hiring managers become part of the security perimeter and need training on the threat (FBI-DPRK-2025)."
  evidence_grade: B
  sources:
    - { ref: KNOWBE4-NKHIRE-2024, title: "How a North Korean Fake IT Worker Tried to Infiltrate Us", publisher: KnowBe4, type: vendor, url: "https://blog.knowbe4.com/how-a-north-korean-fake-it-worker-tried-to-infiltrate-us", date: 2024-07-23, access: full, locator: "TLDR; summary; 'Story updated 10/19/2024'" }
    - { ref: FBI-DPRK-2025, title: "North Korean IT Workers Conducting Data Extortion", publisher: FBI Internet Crime Complaint Center, type: regulator, url: "https://www.ic3.gov/psa/2025/psa250123", date: 2025-01-23, access: full, locator: "Recommendations list" }
    - { ref: GTIG-DPRKIT-2025, title: "DPRK IT Workers Expanding in Scope and Scale", publisher: Google Threat Intelligence Group, type: firm, url: "https://cloud.google.com/blog/topics/threat-intelligence/dprk-it-workers-expanding-scope-scale", date: 2025-04-01, access: full, locator: "Europe expansion; facilitators; BYOD sections" }
    - { ref: CSD-DPRK-2026, title: "Feds crack down on North Korean IT-worker schemes with new raids, charges and arrests", publisher: Cybersecurity Dive, type: press, url: "https://www.cybersecuritydive.com/news/north-korea-it-worker-raids-arrests-charges/832968/", date: 2026-10-14, access: full, locator: "Paragraphs 1-6" }
    - { ref: ENISA-ETL-2026, title: "ENISA Threat Landscape 2026", publisher: ENISA, type: regulator, url: "https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026", date: 2026-09-22, access: full, locator: "Section 1, Overview & Trends" }
  last_reviewed: 2026-10-17
  notes: "Graded B: KnowBe4 is a named real case with process changes but no measured defender outcome. No source read describes defender-side AI (deepfake or liveness detection) with a named deployment. Vendor claims on candidate-fraud detection were seen only in search results and are not used."

- id: security-human-risk-16
  title: Out-of-band, deepfake-aware verification for payment and credential requests
  archetype: security
  module: human-risk
  function: finance-accounting
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Video, voice and email can now all be synthesised. FinCEN observed more suspicious-activity reports describing suspected deepfake media, particularly fraudulent identity documents used to circumvent verification; NYDFS lists AI-enabled social engineering among the most significant threats to financial services."
  solution: "idea (regulator-recommended): treat a voice or video request for money, credentials or data as unverified until confirmed through a separate channel, with defined points for human review. NYDFS says training should cover verifying unexpected money transfer requests by telephone, video or email and when human review must be part of verification procedures."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: NYDFS-AI-2024 }
  prerequisites:
    - "Named verification channels and contact data held independently of the request"
  risks_and_guardrails:
    - "NYDFS: not all authentication factors resist AI-manipulated deepfakes; consider factors that withstand them (NYDFS-AI-2024, access controls section)"
  human_checkpoints:
    - "Human review and oversight inside verification procedures (NYDFS-AI-2024)"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: NYDFS-AI-2024, title: "Industry letter: Cybersecurity risks arising from artificial intelligence and strategies to combat related risks", publisher: New York State Department of Financial Services, type: regulator, url: "https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks", date: 2024-10-16, access: full, locator: "Training and access control sections" }
    - { ref: FINCEN-DEEPFAKE-2024, title: "FinCEN Issues Alert on Fraud Schemes Involving Deepfake Media Targeting Financial Institutions", publisher: US Treasury FinCEN, type: regulator, url: "https://www.fincen.gov/news/news-releases/fincen-issues-alert-fraud-schemes-involving-deepfake-media-targeting-financial", date: 2024-11-13, access: full, locator: "News release paragraphs 1-3" }
  last_reviewed: 2026-10-17
  notes: "Labelled idea: it is a control discussed by regulators and advisors, and no named organisation's rollout or result was found. It is not AI use itself; it is the process change that AI-enabled impersonation forces."

- id: security-human-risk-17
  title: Automated detection of deepfake voice and video in calls and contact centres
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [review-assurance]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: "Humans struggle to distinguish AI-generated scam calls from human voices, so awareness alone is a weak defence."
  solution: "Vendors (Pindrop, others) sell audio and video deepfake detection and voice-intelligence layers for contact centres and meetings. The BSides vishing abstract describes detection strategies including human recognition and automated classification."
  outcomes:
    - { lever: risk, description: "none published from a named deployment; vendor landing page claims about contact-centre fraud (a figure of USD 12.5B lost in 2024 with an asterisk) are not independent", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: PINDROP-2026 }
  prerequisites:
    - "Call recording or streaming access; consent regimes for voice analysis"
  risks_and_guardrails:
    - "Audio deepfakes are described by the vendor as slipping past voice authentication; detection layers 'still appear to hold up' (PINDROP-2026, resource blurb)"
  human_checkpoints:
    - "Not described"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: PINDROP-2026, title: "Voice Intelligence & Security Report (landing page)", publisher: Pindrop, type: vendor, url: "https://www.pindrop.com/research/report/voice-intelligence-security-report/", date: 2026, access: full, locator: "Landing page blurbs" }
    - { ref: BSIDESLV-2026, title: "BSides Las Vegas 2026 talk list", publisher: BSides Las Vegas, type: conference, url: "https://bsideslv.org/talks", date: 2026-08, access: full, locator: "'Devising and Detecting Voice Phishing' abstract, last paragraph" }
  last_reviewed: 2026-10-17
  notes: "No independent detector test results and no named customer deployments were found. Landing page is undated; year is from the page footer only."

- id: security-human-risk-18
  title: Event-triggered LLM micro-coaching inside the user's workflow
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [document-production, client-interaction]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Traditional programmes are delivered outside real-world contexts; users prefer short, contextual guidance to long asynchronous modules."
  solution: "idea (research prototypes): TrainShield (ACM Hypertext 2026) embeds adaptive learning overlays in the browsing workflow, triggered by real-time risk detection such as phishing and data loss prevention, with LLM-based content generation. CyberGLA (2026) pairs a spoof-detection tool with an LLM security coach that selects training modules based on detection outcomes."
  outcomes:
    - { lever: experience, description: "none published beyond a preliminary perception study", figure: "none published", measures: "TrainShield preliminary study indicates perceived usefulness and a preference over lengthy asynchronous formats; sample and size not captured from the abstract", provenance: independent, source_ref: ARXIV-2608.02296 }
  prerequisites:
    - "Browser or mail-client integration that can raise the trigger event"
  risks_and_guardrails:
    - "Authors highlight challenges aligning generated content with user expectations (ARXIV-2608.02296, abstract)"
  human_checkpoints:
    - "Not described"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: ARXIV-2608.02296, title: "TrainShield: Targeted Awareness for Cybersecurity Training", publisher: ACM Hypertext 2026 via arXiv, type: academic, url: "https://arxiv.org/abs/2608.02296", date: 2026-08-03, access: full, locator: "Abstract" }
    - { ref: ARXIV-2608.21547, title: "Enhancing User Resilience Against AI-Augmented Phishing: A Two-Stage Framework for Detection and Personalized Training", publisher: Journal of the Colloquium for Information Systems Security Education via arXiv, type: academic, url: "https://arxiv.org/abs/2608.21547", date: 2026-08-21, access: full, locator: "Abstract" }
  last_reviewed: 2026-10-17
  notes: "Idea: research prototypes only. Hoxhunt and Uber describe similar triggered micro-learning in a production setting (see security-human-risk-03)."

- id: security-human-risk-19
  title: LLM as second reader of inbound email intent to warn users
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: "LLM-written, personalised lures remove the language errors users were trained to spot."
  solution: "idea (research): a study of 101 participants used language models to detect the intent of emails; Claude 3.5 Sonnet scored well above 90% with low false-positive rates and flagged some seemingly benign messages that passed human detection."
  outcomes:
    - { lever: quality, description: "Intent-detection accuracy of an LLM on the study's emails", figure: "well above 90%, low false-positive rates", measures: "authors' statement for Claude 3.5 Sonnet on detecting email intent; test set and exact rates not captured from the abstract", provenance: independent, source_ref: ARXIV-2412.00586 }
  prerequisites:
    - "Mail-flow integration; privacy review for sending mail content to a model"
  risks_and_guardrails:
    - "Adjacent measurement from a small study (101 participants for the human part); not a production result"
  human_checkpoints:
    - "Warning shown to user; user decides"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: ARXIV-2412.00586, title: "Evaluating Large Language Models' Capability to Launch Fully Automated Spear Phishing Campaigns: Validated on Human Subjects", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2412.00586", date: 2024-11-30, access: full, locator: "Abstract" }
  last_reviewed: 2026-10-17
  notes: "Older than 18 months; included because the authors are cited by practitioners (also behind ScamBench). Click rates reported: control 12%, human experts 54%, fully AI 54%, AI with human in the loop 56%."

- id: security-human-risk-20
  title: Sequence analysis of real social-engineering call transcripts to design detection and training
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [research-synthesis]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Social engineering is usually described as isolated techniques, while real interactions follow sequences."
  solution: "idea (conference talk): an empirical analysis of over 1,200 call transcripts to see whether interaction steps follow stable ordering patterns and how they relate to outcomes, to inform detection, red teaming and training."
  outcomes:
    - { lever: quality, description: "none published beyond the talk abstract", figure: "none published", measures: "not applicable", provenance: independent, source_ref: BSIDESLV-2026 }
  prerequisites:
    - "A corpus of recorded or transcribed calls with outcomes"
  risks_and_guardrails:
    - "Call recording consent and privacy"
  human_checkpoints:
    - "Not described"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: BSIDESLV-2026, title: "BSides Las Vegas 2026 talk list", publisher: BSides Las Vegas, type: conference, url: "https://bsideslv.org/talks", date: 2026-08, access: full, locator: "'Social Engineering Has a Grammar' (Ground Truth, Tuesday 17:00)" }
  last_reviewed: 2026-10-17
  notes: "Abstract only; the talk itself was not available. Whether AI is used in the analysis is not stated."

- id: security-human-risk-21
  title: AI voice agents in authorised vishing red-team tests of help desks and staff
  archetype: security
  module: human-risk
  function: technology-it
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: "Help desks and finance staff handle voice requests that attackers can now automate; testing them with human callers is slow and limited."
  solution: "idea (practitioner community): DEF CON 34 lists a 'Battle of the Bots: Vishing Edition' contest alongside the Social Engineering Community Vishing Competition; an IBM podcast episode revisits a DEF CON 2024 contest where a human competed against an AI vishing bot; a ScamBench benchmark of AI-generated social engineering (email, voice, multi-step scenarios such as pig butchering) is presented at BSides Las Vegas 2026, with collaboration with frontier AI labs described."
  outcomes:
    - { lever: quality, description: "none published; no results for the DEF CON 34 bot contest were found", figure: "none published", measures: "not applicable", provenance: independent, source_ref: DEFCON-34-CONTESTS-2026 }
  prerequisites:
    - "Written authorisation and rules of engagement; legal review of voice cloning and call recording"
  risks_and_guardrails:
    - "Same techniques can be misused; ScamBench authors propose uses in pre-deployment safety assessments of models (BSIDESLV-2026)"
  human_checkpoints:
    - "Red-team lead approves scenarios"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: DEFCON-34-CONTESTS-2026, title: "DEF CON 34 contest results index", publisher: DEF CON, type: conference, url: "https://defcon.org/html/defcon-34/dc-34-contest-results.html", date: 2026-08, access: full, locator: "Contest list: 'Battle of the Bots: Vishing Edition'; 'Social Engineering Community Vishing Competition (SECVC)'" }
    - { ref: IBM-JOHNHENRY-2026, title: "John Henry vs. the chatbot: Can humans outsmart AI scam artists?", publisher: IBM Think (Security Intelligence podcast), type: podcast, url: "https://www.ibm.com/think/podcasts/security-intelligence/john-henry-vs-chatbot-can-humans-outsmart-ai-scam-artists", date: 2026-01-30, access: full, locator: "Episode description" }
    - { ref: BSIDESLV-2026, title: "BSides Las Vegas 2026 talk list", publisher: BSides Las Vegas, type: conference, url: "https://bsideslv.org/talks", date: 2026-08, access: full, locator: "'ScamBench: Measuring Real-World Risk of AI-Generated Social Engineering' (Ground Truth, Tuesday 18:00)" }
  last_reviewed: 2026-10-17
  notes: "Idea: titles and abstracts only. DEF CON dates are Aug 2026 (the event ran 6-9 Aug per a search result). No ScamBench scores were found."
```

## 3. Module notes

### Processes and key steps (with work types)

- **Awareness programme design and content production** (document-production): choose topics, build modules, localise, schedule. AI shows up as draft generation (Hoxhunt Content Studio, KnowBe4 agents) with human publication.
- **Phishing and vishing simulation** (review-assurance, data-reporting): design lures, send, record click/report/credential outcomes, compare cohorts. AI shows up in lure generation and personalisation.
- **Reporting and triage of user-reported messages** (transaction-processing): intake, classify, remove or release, give feedback to the reporter. AI shows up as triage agents.
- **Human-risk measurement and intervention** (data-reporting, monitor-diagnose-act): combine simulation, ticketing and security-tool signals into risk views, then coach or escalate.
- **Insider-risk detection and investigation** (review-assurance): log correlation, case management, escalation to HR/legal.
- **Impersonation and scam takedown** (transaction-processing): detect lookalike domains, profiles and ads; submit takedowns.
- **Identity and request verification** (review-assurance): new-hire identity checks, help-desk caller verification, payment callback.
- **Social-engineering assessment** (expert-judgment): vishing and pretext tests of staff and help desk.

### Common pain points

- Low engagement with training: in the UCSD study more than half of embedded-training sessions ended within 10 seconds and fewer than 24% of users completed the material (UCSD-PHISHTRAIN-2025, Section 1).
- Simulation results depend on lure difficulty: banal lures draw 1-2% clicks while others reach upwards of 30% (UCSD-PHISHTRAIN-2025, Section 1), which makes before/after comparisons weak without a control group.
- Report volume rises after training and then overwhelms the SOC (Avanade, HOXHUNT-AVANADE-2026).
- Staff cannot tell voice clones from real callers (BSIDESLV-2026, vishing abstract; ARXIV-2607.09970).
- Hiring and onboarding checks were designed for fraudulent claims, not for stolen real identities with AI-enhanced photos (KNOWBE4-NKHIRE-2024).

### Metrics and benchmarks (with sources; provenance in brackets)

- Simulation failure rate in healthcare RCT: median of 10% failing per exercise; over 56% of users clicked at some point; embedded training cut failure by 2% in absolute terms; interactive training was associated with 19% lower likelihood of clicking a later lure among those who completed it (UCSD-PHISHTRAIN-2025, Section 1) [independent].
- LLM-personalised spear phishing: 10.0% click rate versus 3.7% (LLM generic) and 4.1% (manual generic), 7,700 participants (USENIX-CZYBIK-2026) [independent].
- Spear phishing with human experts versus AI: 54% versus 54%, control 12%, 101 participants (ARXIV-2412.00586) [independent].
- AI voice scams: 16.5% overall compliance across five categories, up to 36% for relative-in-distress, N=4,100 (ARXIV-2607.09970) [independent].
- Vendor benchmark: a "good" failure rate is 5-10% for a mature programme, 25-35% with no training; based on a vendor dataset of 50 million data points from 4 million users (HOXHUNT-FAILRATE-2026) [vendor-published; definitions of failure vary].
- FBI 2025: 22,364 complaints with AI references and USD 893,346,472 adjusted losses; AI-related BEC losses USD 30,256,592 versus USD 3,046,598,558 for BEC overall; AI-related investment complaints USD 632,041,188 versus over USD 8 billion for investment overall. The FBI says many victims do not realise the extent of AI involvement (FBI-IC3-2026, pp. 39-43) [regulator].
- ENISA: phishing about 60% of observed intrusion cases in the 2025 landscape, with AI-supported phishing said to represent over 80% of observed social engineering activity worldwide by early 2025 (ENISA-ETL-2025, executive summary) [regulator, relying on cited third-party reporting]; the 2026 landscape reports phishing at 77.8% of social engineering techniques in the EU dataset and a higher insider share linked to Famous Chollima (ENISA-ETL-2026, Section 1).
- Insider risk cost: USD 19.5M average annual; negligent insiders USD 10.3M; 67 days to contain (HELPNET-PONEMON-2026) [vendor-sponsored survey].
- Okta (via CSD-OKTA-2026): in about 6,000 social-engineering events, 87% of account takeovers involved compromised passwords; phishing-resistant authentication would have stopped 88% of attempts (99.75% when also applied to third-party app sign-ins) [vendor analysis; routed to identity-access].
- Grant Thornton (via CSD-GT-2026): 55% of 1,100 business leaders cite AI-enabled fraud as a major fraud concern; traditional phishing worried more respondents [firm survey].
- Microsoft and Health-ISAC (via CSD-MSFTTAKEDOWN-2026): three phishing marketplaces enabled more than one billion malicious messages since January 2026 [vendor/industry].
- No independent error rate, override rate or parallel-run result was found for AI triage of reported phishing, AI-personalised training, AI insider detection or deepfake detection.

### Guardrails and regulatory points

- **NYDFS (2024-10-16)**: regulated firms should train all staff, including executives, on AI-enhanced social engineering; annual awareness training must include social engineering; training can use simulated phishing and voice and video impersonation exercises; risk assessments should cover deepfakes (NYDFS-AI-2024).
- **FinCEN (2024-11-13)**: alert on deepfake-media fraud with red flags and reporting duties (FINCEN-DEEPFAKE-2024).
- **FBI (2025-01-23)**: advice on identity verification through the whole employment lifecycle for remote workers (FBI-DPRK-2025).
- **NIST SP 800-50 Rev. 1** (final 2024-09-12 per its document history) sets a lifecycle approach to a cybersecurity and privacy learning programme with metrics and evaluation methods (NIST-SP80050-2024).
- **EU AI Act**: AI literacy obligations applied from 2025-02-02; transparency rules (including labelling of AI-generated content, with a voluntary code of practice) from August 2026; high-risk employment use cases from 2027-12-02; emotion recognition in workplaces is prohibited (EC-AIACT-2026).
- **Worker monitoring**: UK ICO guidance on monitoring workers applies to behaviour-signal and insider-risk tooling (ICO-MONITORING-2023).
- **Simulation ethics**: the "unfair simulation" critique (Sophos) and the Czybik study's briefing/debriefing and staff-committee approval show the accepted practice (SOPHOS-PHAKE-2025; USENIX-CZYBIK-2026).

### Frontier signals (dated and sourced)

- 2026-08: peer-reviewed measurement that LLM personalisation almost triples click rates at about USD 0.03 per email (USENIX-CZYBIK-2026).
- 2026-07-10: AI voice phishing judged economically viable where human-run vishing is not (ARXIV-2607.09970).
- 2026-01-30: KnowBe4 says it has seven AI agents in market for human risk management (SECURITYBRIEF-AIDA-2026).
- 2026-04-16 and 2026-08-26: Adaptive Security moves from awareness training into agentic email security (ADAPTIVE-BLOG-2026).
- 2026-06-24: Hoxhunt adds AI content generation for custom modules (HOXHUNT-CONTENT-2026).
- 2026: SANS says AI moved from #4 to #2 in its ranking of human risks in the 2026 Security Awareness and Culture Report (1,700+ practitioners); full report not opened (SANS-AWARENESS-2026).
- 2026-02-26: only a small share of surveyed organisations classify AI agents as equivalent to human insiders (HELPNET-PONEMON-2026).
- 2026-08: DEF CON 34 lists a vishing bot contest; BSides LV presents ScamBench and a voice-phishing benchmark (DEFCON-34-CONTESTS-2026; BSIDESLV-2026).
- 2026-10-14: US charges and laptop seizures against DPRK IT-worker facilitators (CSD-DPRK-2026); 2026-09-22 ENISA ties a higher insider share to the same actor (ENISA-ETL-2026).
- 2026-10-07: Okta argues AI is "the accelerant" and that identity fundamentals still decide outcomes (CSD-OKTA-2026).

### Workforce and role effects

- Awareness work is shifting from compliance administration to behaviour-signal management and content design; Uber runs a 25,000-user programme with a two-person team (HOXHUNT-UBER-2026).
- SOC load moves with reporting: Avanade says its response platform did the work of over 5 full-time analysts a month (HOXHUNT-AVANADE-2026); Valvoline says 4-5 analysts had spent 90% of each day on email tasks (ABNORMAL-VALVOLINE-2026).
- HR, finance and help-desk staff join the security perimeter (FBI-DPRK-2025; NYDFS-AI-2024).
- A Johnson & Johnson senior manager role for cybersecurity awareness training lists social engineering, phishing, insider risk and experience with human risk management platforms and behavioural analytics as qualifications (search-only; posting date not shown).

### Objections and concerns practitioners raise

- Training and simulations do not work well in practice (UCSD study; Hacker News discussion of the study, `HN-PHISHTRAIN-2025`, 97 comments by 2026-10-17). Commenters also argue training is a liability shield and that organisations send official emails that look like phishing. These are individual community comments, not evidence.
- Simulations can be unfair, tick-box and fatiguing (SOPHOS-PHAKE-2025).
- Click rate alone misleads; reporting rate and difficulty matter (HOXHUNT-FAILRATE-2026).
- Personalisation may not add value: complex psychometric personalisation showed no measurable advantage over well-designed generic content in a lab experiment (ARXIV-2512.01893).
- Behaviour monitoring invites privacy and works-council challenges (ICO-MONITORING-2023; EC-AIACT-2026).
- Most evidence for defender AI is vendor-authored; vendors also supply the benchmarks (this module's own source mix).

### Interview probes for an advisor

1. How do you measure whether awareness work lowers risk: click rate, report rate, or incidents? Do you keep a no-training or delayed-training group, and do you vary lure difficulty?
2. Which payment, credential-reset or data requests could be approved today on the strength of a voice or video call alone, and what is the out-of-band check?
3. How many suspicious emails do employees report each month, who triages them, and what share do people still handle by hand?
4. For insider-risk or behaviour-score tools: which data feeds them, who reviews alerts, and what has your privacy officer or works council agreed?
5. How do you verify the identity of remote candidates, contractors and vendor staff before shipping a laptop or granting access, and is HR part of the security process?

## 4. Routed to other modules

- Okta's finding that phishing-resistant authentication would have stopped 88% of account takeovers (CSD-OKTA-2026), BSides "Authorization phishing" talk (OAuth consent and device-code phishing, BSIDESLV-2026), and help-desk reset verification: identity-access.
- Microsoft and Health-ISAC takedown of three phishing marketplaces, which used AI tools to link infrastructure (CSD-MSFTTAKEDOWN-2026); ENISA threat-landscape data; GTIG DPRK reporting: threat-intelligence.
- Phishing Triage Agent product detail (MSFT-PHISHTRIAGE-2026) and Avanade's SOC time savings: operations (overlap with use case 02).
- Shadow AI data leakage, prompt inspection, DLP: data-privacy (use case 14).
- AI agents as insiders and agent identity (DTEX comment; KnowBe4 Agent Risk Manager): ai-security.
- Attacker-capability research (USENIX personalised phishing, vishing economics, ScamBench): threat-intelligence and ai-security.
- Grant Thornton governance-gap findings (CSD-GT-2026), EU AI Act dates, NYDFS letter: governance-risk.
- Brand and consumer scam takedown, scam-baiting, and investment-scam data: fraud is not a module; the landscape recommends folding it here and into identity-access.

## 5. Sources

Access is `full` unless stated. Types follow the vocabulary.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| USENIX-CZYBIK-2026 | A Large-Scale Study of Personalized Phishing using Large Language Models | USENIX Security Symposium | academic | https://www.usenix.org/system/files/usenixsecurity26-czybik.pdf | 2026-08 | full |
| UCSD-PHISHTRAIN-2025 | Understanding the Efficacy of Phishing Training in Practice | IEEE S&P / UC San Diego | academic | https://sysnet.ucsd.edu/~voelker/pubs/phishtrain-oakland25.pdf | 2025-05 | full |
| ARXIV-2512.01893 | Improving Phishing Resilience with AI-Generated Training | arXiv | academic | https://arxiv.org/abs/2512.01893 | 2025-12-01 | full |
| ARXIV-2608.02296 | TrainShield: Targeted Awareness for Cybersecurity Training | arXiv / ACM Hypertext 2026 | academic | https://arxiv.org/abs/2608.02296 | 2026-08-03 | full |
| ARXIV-2608.21547 | Enhancing User Resilience Against AI-Augmented Phishing (CyberGLA) | arXiv / JCISSE | academic | https://arxiv.org/abs/2608.21547 | 2026-08-21 | full |
| ARXIV-2509.08493 | Send to which account? Evaluation of an LLM-based Scambaiting System | arXiv | academic | https://arxiv.org/abs/2509.08493 | 2025-09-10 | full |
| ARXIV-2505.12104 | The Impact of Emerging Phishing Threats: Quishing and LLM-generated Phishing Emails | arXiv / AsiaCCS 2025 | academic | https://arxiv.org/abs/2505.12104 | 2025-05-17 | full |
| ARXIV-2607.09970 | Evaluating AI Models' Capability to Automate Voice Phishing Attacks | arXiv / Expert Systems with Applications | academic | https://arxiv.org/abs/2607.09970 | 2026-07-10 | full |
| ARXIV-2608.16508 | LLMs for Zero-Shot Threat Detection via Structured Risk Indicators | arXiv | academic | https://arxiv.org/abs/2608.16508 | 2026-08-17 | full |
| ARXIV-2409.01378 | Content, Nudges and Incentives: Embedded Phishing Training | arXiv / ACM CCS 2024 | academic | https://arxiv.org/abs/2409.01378 | 2024-09-02 | full |
| ARXIV-2412.00586 | Evaluating LLMs' Capability to Launch Fully Automated Spear Phishing Campaigns | arXiv | academic | https://arxiv.org/abs/2412.00586 | 2024-11-30 | full |
| ARXIV-2503.02702 | RedChronos: LLM-Based Log Analysis for Insider Threat Detection | arXiv | academic | https://arxiv.org/abs/2503.02702 | 2025-03-04 | full |
| BSIDESLV-2026 | BSides Las Vegas 2026 talk list | BSides Las Vegas | conference | https://bsideslv.org/talks | 2026-08 | full |
| DEFCON-34-CONTESTS-2026 | DEF CON 34 contest results index | DEF CON | conference | https://defcon.org/html/defcon-34/dc-34-contest-results.html | 2026-08 | full |
| FBI-IC3-2026 | 2025 IC3 Annual Report | FBI IC3 | regulator | https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf | 2026-04 | full |
| FBI-DPRK-2025 | North Korean IT Workers Conducting Data Extortion | FBI IC3 | regulator | https://www.ic3.gov/psa/2025/psa250123 | 2025-01-23 | full |
| FINCEN-DEEPFAKE-2024 | FinCEN alert on deepfake media fraud | US Treasury FinCEN | regulator | https://www.fincen.gov/news/news-releases/fincen-issues-alert-fraud-schemes-involving-deepfake-media-targeting-financial | 2024-11-13 | full |
| NYDFS-AI-2024 | Industry letter on cybersecurity risks from AI | NYDFS | regulator | https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks | 2024-10-16 | full |
| ENISA-ETL-2025 | ENISA Threat Landscape 2025 (v1.3) | ENISA | regulator | https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025 | 2025-10-01 | full |
| ENISA-ETL-2026 | ENISA Threat Landscape 2026 | ENISA | regulator | https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026 | 2026-09-22 | full |
| EC-AIACT-2026 | AI Act regulatory framework page | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-17 | full |
| ICO-MONITORING-2023 | Employment practices and data protection: monitoring workers | UK ICO | regulator | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/ | 2023-10 | full |
| NIST-SP80050-2024 | SP 800-50 Rev. 1, Building a Cybersecurity and Privacy Learning Program | NIST CSRC | standard-setter | https://csrc.nist.gov/pubs/sp/800/50/r1/ipd | 2024-09-12 | full |
| SANS-AWARENESS-2026 | SANS 2026 Security Awareness and Culture Report webcast page | SANS Institute | professional-body | https://www.sans.org/webcasts/sans-2026-security-awareness-culture-report | 2026 | full (page only; report not opened) |
| HOXHUNT-QUALCOMM-2023 | How Qualcomm used Hoxhunt... | Hoxhunt | vendor | https://hoxhunt.com/case-studies/how-qualcomm-used-targeted-security-awareness-training-for-employees | 2023 | full |
| HOXHUNT-AVANADE-2026 | How Avanade reduces human cyber risk... | Hoxhunt | vendor | https://hoxhunt.com/case-studies/avanade-reduced-cyber-risk-and-saved-5-soc-analyst-ftes-with-hoxhunt | 2026 | full |
| HOXHUNT-UBER-2026 | Uber reduces human risk... | Hoxhunt | vendor | https://hoxhunt.com/case-studies/uber-reduces-human-risk-with-signal-driven-behavior-management | 2026 | full |
| HOXHUNT-BRC-2026 | Behavior Risk Console | Hoxhunt | vendor | https://hoxhunt.com/product/behavior-risk-console | 2026 | full |
| HOXHUNT-FAILRATE-2026 | What is a good phishing failure rate? | Hoxhunt | vendor | https://hoxhunt.com/blog/what-is-a-good-phishing-failure-rate | 2026-03-09 | full |
| HOXHUNT-VOICE-2025 | Hoxhunt Voice Phishing Training | Hoxhunt | vendor | https://hoxhunt.com/blog/hoxhunt-voice-phishing-training | 2025-10-24 | full |
| HOXHUNT-CONTENT-2026 | Content Studio creates customizable security awareness content | Hoxhunt | vendor | https://hoxhunt.com/blog/content-studio-creates-customizable-security-awareness-content | 2026-06-24 | full |
| SOPHOS-PHAKE-2025 | Phake phishing: Phundamental or pholly? | Sophos | vendor | https://www.sophos.com/en-us/blog/phake-phishing-phundamental-or-pholly | 2025-10-31 | full (via r.jina.ai mirror) |
| MSFT-PHISHTRIAGE-2026 | Phishing Triage Agent in Microsoft Defender | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/defender-xdr/phishing-triage-agent | 2026-07-02 | full |
| PURVIEW-IRM-2026 | Microsoft Purview Insider Risk Management | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/purview/insider-risk-management | 2026-06-26 | full |
| ABNORMAL-VALVOLINE-2026 | Valvoline Replaces SEG with Autonomous AI | Abnormal AI | vendor | https://abnormal.ai/customers/stories/valvoline | 2026 | full |
| DOPPEL-ARK-2026 | From Weeks to Minutes: Why ARK Invest Chose Doppel | Doppel | vendor | https://www.doppel.com/customers/ark-invest | 2026-01-16 | full |
| ADAPTIVE-BLOG-2026 | Adaptive Security homepage and blog index | Adaptive Security | vendor | https://www.adaptivesecurity.com/blog | 2026-08-26 | full (index and summaries only) |
| PINDROP-2026 | Voice Intelligence & Security Report landing page | Pindrop | vendor | https://www.pindrop.com/research/report/voice-intelligence-security-report/ | 2026 | full (landing page only) |
| KNOWBE4-NKHIRE-2024 | How a North Korean Fake IT Worker Tried to Infiltrate Us | KnowBe4 | vendor | https://blog.knowbe4.com/how-a-north-korean-fake-it-worker-tried-to-infiltrate-us | 2024-07-23 | full |
| GTIG-DPRKIT-2025 | DPRK IT Workers Expanding in Scope and Scale | Google Threat Intelligence Group | firm | https://cloud.google.com/blog/topics/threat-intelligence/dprk-it-workers-expanding-scope-scale | 2025-04-01 | full |
| HELPNET-PONEMON-2026 | The USD 19.5 million insider risk problem | Help Net Security (Ponemon/DTEX study) | survey | https://www.helpnetsecurity.com/2026/02/26/insider-risk-costs-2026/ | 2026-02-26 | full |
| VERIZON-DBIR-2026 | 2026 Data Breach Investigations Report landing page | Verizon | survey | https://www.verizon.com/business/resources/reports/dbir/ | 2026 | full (landing page only; report body gated) |
| CSD-DPRK-2026 | Feds crack down on North Korean IT-worker schemes | Cybersecurity Dive | press | https://www.cybersecuritydive.com/news/north-korea-it-worker-raids-arrests-charges/832968/ | 2026-10-14 | full |
| CSD-GT-2026 | Grant Thornton risk-management report coverage | Cybersecurity Dive | press | https://www.cybersecuritydive.com/news/cybersecurity-risk-management-ai-governance-grant-thornton/832850/ | 2026-10-13 | full |
| CSD-OKTA-2026 | Okta report on AI and identity attacks | Cybersecurity Dive | press | https://www.cybersecuritydive.com/news/phishing-authentication-ai-okta/832376/ | 2026-10-07 | full |
| CSD-MSFTTAKEDOWN-2026 | Microsoft, Health-ISAC phishing marketplace takedown | Cybersecurity Dive | press | https://www.cybersecuritydive.com/news/phishing-marketplace-takedown-microsoft-health-isac/832965/ | 2026-10-14 | full |
| CNN-ARUP-2024 | Arup revealed as victim of deepfake scam | CNN | press | https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk | 2024-05-17 | full |
| SECURITYBRIEF-AIDA-2026 | KnowBe4 marks AIDA decade, names AI innovation VP | SecurityBrief UK | press | https://securitybrief.co.uk/story/knowbe4-marks-aida-decade-names-ai-innovation-vp | 2026-01-30 | full |
| IBM-JOHNHENRY-2026 | John Henry vs. the chatbot | IBM Think, Security Intelligence | podcast | https://www.ibm.com/think/podcasts/security-intelligence/john-henry-vs-chatbot-can-humans-outsmart-ai-scam-artists | 2026-01-30 | full (episode page only) |
| HN-PHISHTRAIN-2025 | Hacker News: "Cybersecurity training programs don't prevent phishing scams" | Hacker News | community | https://news.ycombinator.com/item?id=45529577 | 2025-10-09 | full (via Algolia API) |
| JNJ-JOB-2026 | Senior Manager, Cybersecurity Awareness Training | Johnson & Johnson careers | job-posting | https://www.careers.jnj.com/en/jobs/r-092295/senior-manager-cybersecurity-awareness-training/ | 2026 | search-only (page blocked; posting date not shown) |

Source count by type: vendor 15, academic 12, regulator 8, press 6, conference 2, survey 2, standard-setter 1, professional-body 1, firm 1, podcast 1, community 1, job-posting 1 (total 51). `ARXIV-2409.01378` and `VERIZON-DBIR-2026` are cited only in the notes below the table.

Notes on non-listed items: the Sophos post is a vendor blog. ARXIV-2409.01378 (CCS 2024) found embedded training works mainly through nudging, with content rarely consumed, and that delaying training is as effective as immediate delivery and rewards do not help (abstract). The DBIR 2026 landing page states that vulnerabilities now start more breaches than stolen passwords and that mobile threats have higher click rates; the figures themselves were not visible in the text read.

## 6. Gaps

- **No independent measurement** of AI-personalised training, AI phishing triage accuracy, AI insider detection in production, or deepfake detectors. No error, override or parallel-run rates were found.
- **Vendor case-study pages are undated** (Hoxhunt Avanade/Uber/Qualcomm, Abnormal Valvoline, Pindrop). Years in refs are best estimates and flagged.
- **Blocked or paywalled:** CISA Insider Threat Mitigation Guide and news pages (403, mirror blocked); Gartner press releases (403); Forrester and Gartner human-risk market research; Verizon DBIR 2026 body (gated); Proofpoint State of the Phish 2026 (only the 2024 landing page loaded); KnowBe4 phishing benchmark page (404); DTEX press release and Ponemon report (blocked); Johnson & Johnson posting (403); Covert Swarm DEF CON recap (blocked); NCSC phishing pages (404); UK Cyber Security Breaches Survey 2026 page (404); Sublime Security blog (429).
- **Not opened beyond abstract or landing page:** SANS 2026 Security Awareness and Culture Report (page says 1,700+ practitioners and AI jumping from #4 to #2 as a human risk; trade-press figures on team size and maturity were search-only and are not used); all arXiv papers except their abstracts; KnowBe4's "10 critical updates" hiring post; UCSD press release.
- **Not found:** results of the DEF CON 34 "Battle of the Bots: Vishing Edition"; ScamBench scores; Black Hat USA 2026 human-risk briefings (official lineup page not retrievable); named customers for vishing or deepfake training; ISO/IEC 27001 or sector regulator (FCA, MAS, HKMA) statements on awareness training; works-council or union positions on behaviour scoring.
- **Search-only claims not used as outcomes:** Gartner forecast that one in four candidate profiles could be fake by 2028; Experian and Keepnet statistics; Infosec deepfake-voice coaching agents; KnowBe4 "eight agents" count.
- **Adjacent fraud topics:** consumer scams, bank and telco scam defences, and takedown services are only lightly covered because they sit outside the CISO organisation.
