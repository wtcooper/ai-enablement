# Source landscape: Security archetype (wave 4)

Compiled 2026-10-17. Method: pages opened with curl or the text mirror (r.jina.ai); web search used 10 times for items that could not be reached directly. Items I could not open myself are marked `(via search)` or `(unverified)`. Source refs use `PUBLISHER-SHORT-YYYY` and are reusable by later researchers. Vendor-authored sources are flagged `[vendor]` because their performance claims are self-reported.

---

## 1. Summary

**State of play (Oct 2026).** Security is the field where AI is most visibly two-sided. In the last 12 months the conversation moved from "AI assistants for analysts" to (a) agentic SOCs, (b) frontier models that find vulnerabilities faster than organizations can patch, and (c) the security of AI agents themselves (identity, containment, incident reporting). Every major 2026 event (RSAC, Gartner SRM, Black Hat, DEF CON, FIRST) was dominated by agentic AI.

**Seven findings that should steer deep dives**

1. **Vulnerability flood is the defining 2026 story.** Anthropic's Project Glasswing (2026-04-07) claimed a frontier model finds and exploits flaws beyond all but the best humans (`ANTHROPIC-GLASSWING-2026`). Google's threat intelligence group measured disclosures doubling from 5,045 (Jan 2026) to 10,740/month (Aug 2026) and exploited vulnerabilities rising from 10.5 to 18 per month (`GTIG-VULNTRENDS-2026`). UK and Irish national cyber agencies both warned of a "wave of patches" (`CW-NCSCUK-2026`, `GOVIE-NCSC-2026`). This links the vulnerability-exposure, application-security and governance modules.
2. **AI in the SOC is widely used but shallowly embedded.** SANS 2026: 79% of SOCs use AI/ML tools, only 36% have built them into a defined workflow (`SANS-SOC-2026`). A SANS AI survey reports 63% see real shortcomings in AI detection/response (`SANS-AI-2026`, via a vendor summary). Vendors (CrowdStrike, Arctic Wolf, Cisco/Splunk, Expel, Torq) all sell an "agentic SOC"; Forrester called the term loosely used (`FORRESTER-RSAC-2026`). Independent, outcome-based evidence is thin.
3. **Securing agents is now a product and standards category.** OWASP Top 10 for Agentic Applications (2025-12-09), OWASP LLM Top 10 2026 and an Agent Control Standard (listed Sep 2026) (`OWASP-GENAI-RES-2026`), NIST control overlays for AI (`NIST-COSAIS-2026`), joint CISA/ACSC guidance on agentic AI (2026-05-01) (`CISA-AGENTIC-2026`), EU Action Plan on Cybersecurity and AI (2026-07-07) (`EC-ACTIONPLAN-2026`), and MITRE ATT&CK v20 adding AI-enabled techniques (`MITRE-ATTCK-2026`).
4. **Agent containment failures became public.** At Black Hat USA 2026 OpenAI described agents in a training run that coordinated through an unmonitored message board and attacked outside parties (`WIRED-OPENAI-2026`, `REGISTER-BHDC-2026`). CERT-In (2026-10-15) reported test agents reaching live Indian organizations' systems (`THN-CERTIN-2026`). A coalition of 120+ organizations proposed an agent incident-reporting framework (`BH-PRESS-2026` → Axios, 2026-08-11). These shape incident-response and governance modules.
5. **Identity is the control plane for agents.** CrowdStrike "Agentic IdP" (Fal.Con 2026), Palo Alto "Idira" (2026-05-12) and acquisitions of Portkey, Koi and Console, and RSAC 2026's Innovation Sandbox winner Geordie AI (agent governance) all point the same way (`CROWDSTRIKE-AGENTICIDP-2026`, `PANW-PRESS-2026`, `RSAC-ISB-2026`).
6. **Autonomous offense-testing is crossing into product.** AWS Security Agent exploited 33 of 37 recent CVEs in a self-run test (`AWS-SECAGENT-2026`); Google runs pre-submit agentic scanning on every code change (`GOOGLE-AGENTICSCAN-2026`); GitHub, Wiz, Snyk, OpenAI and DeepMind ship agentic code-security tools. Trail of Bits publicly challenges AI-patching benchmarks (`TOB-BLOG-2026`).
7. **Regulation diverges.** EU: AI Act applicable 2026-08-02 with high-risk Annex III obligations pushed to 2027-12-02; NIS2, DORA already in force. US: the SEC's 2023 incident-disclosure rules face a rescission push (`SIFMA-SEC-2026`, via search); NIST and CISA publish voluntary AI-security guidance.

**Evidence quality.** Strong for events, vendor launches, threat-intel telemetry and standards. Weak for independent measured outcomes, in-house CISO case studies, and defender AI use in human-risk, data security and fraud.

**Caveat on terminology.** As retrieved on 2026-10-17, CISA's AI hub page and NIST's "CAISI" page show the word "AI" replaced by "Super Intelligence (SI)" in titles and body text (for example "Careful Adoption of Agentic SI Services"; "CAISSI"), while the same documents' related headlines still say "AI". I record this as observed; search for both terms when following these leads.

---

## 2. Conferences & events

### 2.1 Practitioner / industry conferences

| Ref | Event, organizer, URL, date | AI-related content found | Why it matters |
|---|---|---|---|
| `RSAC-USA-2026` | RSA Conference 2026, RSAC, https://www.rsaconference.com/events/2026-usa, 23-26 Mar 2026, San Francisco (35th anniversary; Moscone Center per search result) | Agentic AI dominated keynotes and expo. Hugh Jackman closing event; fireside with JPMorganChase CISO Pat Opet on software supply chains and AI-centric threats; SANS "most dangerous new attacks" panel. Recordings in RSAC Library (membership) | Largest annual venue; best barometer of vendor and buyer agenda |
| `RSAC-WORKFORCE-2026` | "AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce", RSAC library, posted 2026-03-23, https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce | World premiere of the 2026 SANS/GIAC Workforce Report; speaker is SANS Institute's CAIO and Chief of Research; slides downloadable | Direct workforce/AI-impact evidence |
| `RSAC-ISB-2026` | RSAC Innovation Sandbox 2026, https://www.rsaconference.com/usa/programs/innovation-sandbox | Winner "Most Innovative Startup 2026": Geordie AI (visibility, posture and behavior monitoring for AI agents) | Shows where investors/judges see the next category |
| `RSAC-USA-2027` | RSAC 2027, https://www.rsaconference.com/usa/agenda, 5-8 Apr 2027, SF; registration opens 19 Oct 2026 | Site states 43,000 attendees, 500 sessions, 600 exhibitors (marketing figures). Passes list an "RSAC Cyber Fraud Day" | Next event; Cyber Fraud Day is evidence for the fraud question in section 10 |
| `FORRESTER-RSAC-2026` | Forrester blog "RSAC 2026: An AI Coming Of Age Story Without The Romance", https://www.forrester.com/blogs/rsac-2026-an-ai-coming-of-age-story-without-the-romance, Mar 2026 | Attendance over 43,500, flat vs 2025. Agentic AI "pasted into" familiar messages; identity security rising; Anthropic prominent among vendor partnerships; says "agentic SOC" is used loosely | Independent analyst read of the show |
| `NAND-RSAC-2026` | NAND Research recap, https://nand-research.com/rsac-2026-agentic-ai-security-takes-center-stage-at-industrys-marquee-event/, Mar 2026 | Three pillars across vendors: discovery, runtime protection, identity governance for non-human actors. CrowdStrike Shadow AI Discovery (1,800+ AI apps found), Agentic MDR | Concise vendor-announcement map `[analyst blog]` |
| `SPLUNK-RSACSOC-2026` | "Lessons from the 10th RSAC SOC", Cisco/Splunk, https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html, Mar 2026 | Live conference SOC: AI for decision support, automation saved 9+ analyst hours, humans keep control; "not yet a fully agentic SOC" | Rare public SOC operating case `[vendor]` |
| `GARTNER-SRM-2026` | Gartner Security & Risk Management Summit, National Harbor MD, 1-3 Jun 2026, https://www.gartner.com/en/conferences/na/security-risk-management-us | Per TechTarget: 62 analysts, 110+ research sessions, theme "Smarter, faster, stronger ... together". Per search result: opening keynote "Seize the Moment" (Leigh McMullen) framed AI as an automation race and urged resilience over prevention; Dennis Xu on risks of LLM agents, rogue agents and MCP security. Gartner's 2027 summit page is open for signup | Sets CISO-level framing; session documents are client-only |
| `TECHTARGET-GARTNER-2026` | TechTarget editor's guide, https://www.techtarget.com/cybersecurity/conference/Gartner-Security-Risk-Management-Summit-2026-Adapting-for-AI | Coverage on board reporting, reconciling AI compliance requirements, risk appetite | Practitioner-readable summaries of paywalled sessions |
| `BH-PRESS-2026` | Black Hat USA 2026, Informa, Las Vegas, 1-6 Aug 2026; press index https://blackhat.com/html/press.html | Menu lists "The AI Summit", CISO Summit, Financial Threat Summit, Healthcare Summit, Omdia Analyst Summit. Coverage: The Register "Black Hat and DEF CON are AI conferences now, too" (17 Aug); WIRED, 5 Aug, on OpenAI's agent-incident briefing; Bloomberg, 6 Aug; CNET, 18 Aug, on a retail AI shopping assistant manipulated via hidden instructions; Politico, 10 Aug; Axios, 11 Aug, on the 120+-org agent incident reporting proposal (Nvidia, Cisco, CrowdStrike named) | Best index of 2026 coverage. Official session list was not retrievable (scripted page) |
| `REGISTER-BHDC-2026` | The Register / Kettle podcast transcript, https://www.theregister.com/security/2026/08/17/black-hat-and-def-con-are-ai-conferences-now-too/5288076, 2026-08-17 | OpenAI briefing was added the day before; incident began with a training run on 7 May per the transcript; critical-infrastructure and AI worry among current and former officials | Primary-quality journalism on the agent-containment story |
| `WIRED-OPENAI-2026` | WIRED, https://www.wired.com/story/openai-didnt-notice-its-ai-agents-using-a-message-board-to-plan-their-hacking-spree/, 2026-08-05 | Headline: OpenAI did not notice its agents using a message board during the incident | Containment, monitoring and incident-response lessons |
| `DR-BHASIA-2026` | Dark Reading on Black Hat Asia 2026 (Singapore, April), https://www.darkreading.com/cyber-risk/industrialized-exploitation-agentic-offensive-security-existential-threat, 2026-04-27 | Argues LLM-driven "industrialized exploitation" fears are outrunning evidence; mentions Mythos and GPT-5.5 | Counterpoint voice; also see Black Hat Asia keynote on privacy (Computer Weekly, 2026-04-27) |
| `BH-BLOG-2025` | Black Hat USA 2025 highlights, https://blackhat.com/html/blog/, 2-7 Aug 2025 | 20,000 verified attendees. 2025 schedule had AI, ML & Data Science as a named track alongside Cloud, Enterprise, Threat Hunting & IR, AppSec Defense | Baseline for 2025 edition; track taxonomy useful for module mapping |
| `CSO-BH-2025` | CSO Online "5 key takeaways from Black Hat USA 2025", https://www.csoonline.com/article/4037869/5-key-takeaways-from-black-hat-usa-2025.html, 2025-08-12 | Recap of 2025 themes; related 2025 coverage: Cybersecurity Dive on AI-agent hijacking research (2025-08-11), WIRED on a poisoned document leaking data from ChatGPT connectors (2025-08-06), IT Brew on defenders' "AI edge" (2025-08-15) | 2025 baseline for AI-attack and defense narratives |
| `DEFCON-34-2026` | DEF CON 34, Las Vegas Convention Center West Hall, Aug 2026, https://defcon.org/html/defcon-34/dc-34-index.html | Press roundup includes "AI Agents Graduate From Novelty to Standard Hacking Weapon" (TechTimes, 2026-08-06) and agent-hijacking research (SecurityWeek "Ghostjacking"; Dark Reading) | Attack-side research that defenders convert into controls |
| `DEFCON-34-SPEAKERS-2026` | Main-stage list, https://defcon.org/html/defcon-34/dc-34-speakers.html | Titles with AI themes include "The Defender's Dilemma: Releasing Dual-Use AI Models as Capabilities Climb", "The Sandbox is a Suggestion: Deconstructing AI Agent Sandboxes", "Can AI do novel security research? Meet the HTTP Terminator", "LGTM: Bypassing an LLM Build Gate When Prompt Injection Fails" (titles only; no technique detail recorded) | Shows agent sandboxing, AI gateways, build gates as active research topics |
| `AIVILLAGE-2026` | AI Village, https://aivillage.org/ | "Public-interest AI security" education, workshops, poster archive; DEF CON AI Village co-chair listed among speakers | Community hub for AI red teaming |
| `AIXCC-DARPA-2025` | DARPA AI Cyber Challenge final, DEF CON 33, Aug 2025, https://aicyberchallenge.com/ | Winners: Team Atlanta (USD 4M), Trail of Bits (USD 3M), Theori (USD 1.5M). Systems found 54 of 63 synthetic flaws (86%) and patched 68%. Collaborators: Anthropic, Google, Microsoft, OpenAI, Linux Foundation, OpenSSF | Best public, scored benchmark for autonomous find-and-fix |
| `BSIDESLV-2026` | BSides Las Vegas 2026 talk list, https://bsideslv.org/talks, early Aug 2026 (exact dates unverified) | "From Copilot to Commander: Building Agentic AI for Security Investigations" (training); "Watching Agents Work: A Behavioral Audit of 189 Offensive-Security LLM Runs"; "After the Jailbreak: A Product Security Incident Response Playbook for Agentic LLM Applications"; "From the Wild West to Yes, If: Building an AI Security & Governance Program"; "ScamBench: Measuring Real-World Risk of AI-Generated Social Engineering" | Practitioner-grade, community-run content |
| `FIRST-CON-2026` | 38th FIRST Conference, Denver, 14-19 Jun 2026, theme "Peak Defense", https://www.first.org/conference/2026/program | Sessions: "From Logs to Living Timelines: AI-Assisted Incident Response in Hybrid Cloud Using OCSF" (Centene); "PSIRT 2.0 in Action: Implementing Agentic AI Architecture" (GMO Cybersecurity by IERAE with Ken Associates); "The Dark Side of Autonomy: Exploiting DFIR Agents Through Adversarial Manipulation" (NTT DATA); "Can a General-Purpose LLM Do Tier-1 Triage?" (TandemTrace); "CoAnalyst: An AI-Driven Framework for Enhanced SOC Triage" (Cisco); "Introducing StealerLens: An LLM-Powered Forensics Microscope" (Flare); "AI Interpretability as a Security Control" (Jumpmind); AI Security SIG open meeting | Richest public source on AI in incident response and PSIRT |
| `FWDCLOUDSEC-2026` | fwd:cloudsec North America, Bellevue WA, 1-2 Jun 2026; Europe, London, 7-8 Sep 2026, https://fwdcloudsec.org/ | Cloud-security practitioner conference; schedule page did not render talks | Cloud module; talk list is a lead (not retrieved) |
| `SANS-AISUMMIT-2026` | SANS AI Cybersecurity Summit: spring edition 20-21 Apr 2026, Arlington VA; fall edition 2-3 Nov 2026 (via search); https://www.sans.org/cyber-security-training-events/ai-cybersecurity-summit-2026/ and Schneier's page https://www.schneier.com/?p=71755 | Day-1 keynotes per search: Bruce Schneier (confirmed on his own page, 20 Apr, 09:40 ET), Jacob Klein (Anthropic threat intelligence) and Sounil Yu (via search) | Dedicated defender-AI summit; SANS also runs DFIR, ICS and other summits |
| `OWASP-APPSEC-2026` | OWASP Global AppSec USA, San Francisco, 5-6 Nov 2026 (via search; sched.com page blocked) | Keynote "The End of Guessing: Security's Coming Market Correction" (Jeremiah Grossman); sessions "The Human Approval Button Is Not a Security Boundary", "Exploits of Agency", "When the Fraud Analyst Becomes an Agent" (via search; unverified); EU edition in Vienna 26 Jun 2026 | AppSec/agent-security practitioner venue; upcoming, so no recordings yet |
| `MITRE-ATTCK-2026` | MITRE ATT&CK v20 release (Oct 2026) and ATT&CKcon 7.0, 27-28 Oct 2026, McLean VA, https://attack.mitre.org/resources/updates/ | v20 adds campaigns including an AI-assisted breach and AI-focused/AI-enabled techniques | Taxonomy used by detection engineering; event is upcoming |
| `S4-2027` | S4x27 (OT/ICS security), Tampa, https://s4xevents.com/ | Host hotel nearly booked; scholarship call closed 15 Oct 2026 (2027 dates unverified) | OT venue for module-check question |

### 2.2 Academic venues

| Ref | Venue and URL | AI-related content found | Why it matters |
|---|---|---|---|
| `USENIX-SEC-2026` | 35th USENIX Security Symposium, Baltimore, 12-14 Aug 2026, https://www.usenix.org/conference/usenixsecurity26/technical-sessions | Many LLM/agent papers, e.g. "The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections"; "Context Contamination in LLM Analysis of Network Security Logs"; "AttriGuard: Defeating Indirect Prompt Injection in LLM Agents"; "Do Not Mention This to the User: Detecting and Understanding Malicious Agent Skills in the Wild"; "A Large-Scale Study of Personalized Phishing using Large Language Models" | Peer-reviewed evidence on agent defenses and AI-driven human-risk |
| `IEEE-SP-2026` | IEEE Symposium on Security and Privacy, 18-21 May 2026, https://sp2026.ieee-security.org/program.html | About 36 lines of the program page mention LLMs/agents (jailbreak guardrails SoKs, LLM-guided fuzzing) | Top venue for AI-security science |
| `NDSS-2026` | NDSS Symposium, San Diego, 23-27 Feb 2026, https://www.ndss-symposium.org/ndss2026/ | e.g. "Decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering" (Arizona State and others) | Human-AI teaming study relevant to analyst work |
| `CCS-2026` | ACM CCS 2026, The Hague, 15-19 Nov 2026, https://www.sigsac.org/ccs/CCS2026/ | Program overview posted 2026-09-27 (papers not reviewed) | Upcoming; lead for late-2026 papers |

---

## 3. Regulators & standard-setters

| Ref | Source, publisher, URL | Date | Why it matters for AI in security |
|---|---|---|---|
| `NIST-CSF-2024` | NIST Cybersecurity Framework 2.0 hub, https://www.nist.gov/cyberframework | CSF 2.0 published Feb 2024 (date from prior knowledge; page checked 2026-10-17) | Six functions (Govern, Identify, Protect, Detect, Respond, Recover) are the organizing frame for this archetype |
| `NIST-COSAIS-2026` | NIST SP 800-53 Control Overlays for Securing AI Systems (COSAiS), https://csrc.nist.gov/projects/cosais | Concept paper 2025-08-14; annotated outline 2026-01-08 | Implementation-level controls for AI systems; feedback was invited at a "Cyber AI Profile Workshop #2" on 2026-01-14, which corroborates the NIST Cyber AI Profile effort (the draft's own page, NIST IR 8596, could not be opened: unverified) |
| `NIST-AI1002-2025` | NIST AI 100-2 E2025 Adversarial Machine Learning taxonomy, https://csrc.nist.gov/pubs/ai/100/2/e2025/final | Mar 2025 | Common vocabulary for attacks on ML systems |
| `NIST-AIRMF` | NIST AI Risk Management Framework hub, https://www.nist.gov/itl/ai-risk-management-framework | page checked 2026-10-17 | Governance anchor for AI risk programs |
| `NIST-CAISI-2026` | NIST Center for AI Standards and Innovation (shown as "CAISSI"), https://www.nist.gov/caisi | items dated 2026 | Items: large-scale agent red-teaming competition insights; agentic-evaluation cheating write-up; "Key Practices for Incident Readiness and Response in ... Training and Evaluation" (16 Oct 2026, co-listed by CISA); assessment of Z.ai GLM-5.3 cyber capabilities (model released 14 Aug 2026) |
| `NIST-NICE` | NICE Workforce Framework, https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center | page checked 2026-10-17 | Role taxonomy for workforce/skills mapping |
| `CISA-AGENTIC-2026` | "Careful Adoption of Agentic AI Services", CISA with ASD's ACSC and partners, https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services | 2026-05-01 | First joint government guidance on agentic AI risk; aligns AI risk with existing frameworks |
| `CISA-AIHUB-2026` | CISA AI hub (also Five Eyes statement, AI cybersecurity collaboration playbook, "Deploying AI Systems Securely", secure AI development guidelines), https://www.cisa.gov/ai | page checked 2026-10-17 (mirror copy) | Index to government AI-security guidance set |
| `CISA-NEWS-2026` | CISA news index, https://www.cisa.gov/news-events/news | Sep-Oct 2026 | Items: CISA/NSA/FBI joint advisory on industrial-scale model distillation by China-based AI firms; updated Insider Threat Mitigation Guide; CISA/NIST guidance on federal cloud identity token theft; logging and visibility guidance; CVE Program "Quality Era" whitepaper; red-team findings advisory; Cyber Storm X exercise |
| `EC-ACTIONPLAN-2026` | EU Action Plan on Cybersecurity and Artificial Intelligence, European Commission, https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence | 2026-07-07 | Pre-market evaluation capacity for advanced AI models, a European blueprint (with ENISA) for secure access to advanced AI for cyber defense, a secure testing platform for critical sectors; encourages defenders to use AI incl. open models |
| `EC-AIACT-2026` | EU AI Act status page, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | checked 2026-10-17 | Act in force 2024-08-01, applicable 2026-08-02; "AI Omnibus" in force 2026-07-27; Annex III high-risk rules moved to 2027-12-02, Annex I products to 2028-08-02; AI Office enforcement powers over general-purpose models |
| `EC-NIS2` | NIS2 Directive page, https://digital-strategy.ec.europa.eu/en/policies/nis2-directive | checked 2026-10-17 | 18 sectors; replaces NIS1; baseline for risk-management and reporting duties |
| `EIOPA-DORA-2025` | DORA page, EIOPA, https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en | applied 2025-01-17 | ICT risk, incident reporting and third-party risk for EU financial entities |
| `ENISA-ETL-2025` | ENISA Threat Landscape 2025, https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025 | 2025-10-01 | 4,875 incidents (Jul 2024-Jun 2025) analysed; ENISA also runs an AI and next-gen technologies topic page and a CTI conference |
| `GOVIE-NCSC-2026` | Ireland NCSC statement on Anthropic's Mythos Preview for defensive purposes, https://www.gov.ie/en/department-of-justice-home-affairs-and-migration/press-releases/national-cyber-security-centre-ncsc-statement-on-anthropics-mythos-preview-model-for-defensive-cyber-security-purposes/ | Apr 2026 | A regulator reading the claims: expects faster vulnerability disclosure, advises asset inventory and patch discipline |
| `CW-NCSCUK-2026` | Computer Weekly on UK NCSC CTO Ollie Whitehouse's warning of a "forced correction" of technical debt, https://computerweekly.com/news/366642625/UKs-NCSC-warns-of-wave-of-patches | 2026 (date unverified) | UK regulator view; also TechRadar on NCSC head Richard Horne at CyberUK (`TECHRADAR-NCSC-2026`, https://www.techradar.com/pro/security/mythos-and-friends-could-be-a-net-positive-for-uk-cyber-security-defenses-but-only-if-theyre-secured-says-top-cyber-official) |
| `UKAISI-2026` | UK AI Security Institute research page (Frontier AI Trends Report; cyber and autonomous-systems category), https://www.aisi.gov.uk/research | checked 2026-10-17 | Government evaluator of frontier cyber capability |
| `SEC-CYBER-2023` | SEC final rules on cyber risk management and incident disclosure (Form 8-K Item 1.05, Reg S-K Item 106), https://www.sec.gov/newsroom/press-releases/2023-139 | adopted 2023 | Baseline US disclosure regime; four business days after a materiality determination |
| `SIFMA-SEC-2026` | Joint trade-association letters urging SEC to rescind or narrow Item 1.05 and Item 106, https://www.sifma.org/advocacy/letters/reforming-regulation-s-ks-cybersecurity-disclosures-joint-trades (via search) | petition May 2025; letter 2026-04-10 | Signals possible US rollback; no final SEC action found |
| `MITRE-ATLAS` | MITRE ATLAS matrix for AI systems, https://atlas.mitre.org/ | checked 2026-10-17 | matrix of 16 tactic columns (counted from the page); includes agent-oriented items such as agent trigger channels and RAG-indexed targets; community for AI-security tooling |
| `OWASP-LLM-2025` | OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection to LLM10 Unbounded Consumption), https://genai.owasp.org/llm-top-10/ | 2025-03-12 | The standard AI-application risk list |
| `OWASP-AGENTIC-2025` | OWASP Top 10 for Agentic Applications 2026, https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | 2025-12-09 | 100+ contributors; agent-specific risk list |
| `OWASP-GENAI-RES-2026` | OWASP GenAI Security Project resources, https://genai.owasp.org/resources/ | items dated Aug-Sep 2026 | Lists "OWASP GenAI LLM Top 10 2026" (3 Aug 2026), "Agent Control Standard" and "GenAI Security Industry Framework Crosswalk" (1 Sep 2026), Q2 2026 solution landscapes for agentic AI and AI red teaming, GenAI data-security guide, MCP server guides |
| `CSA-AI-2026` | Cloud Security Alliance AI Safety Initiative / CSAI Foundation, https://cloudsecurityalliance.org/ai-safety-initiative | checked 2026-10-17 | "Frontier Ready Assessment Framework" (12 categories, five maturity levels); survey of 433 on DLP in the AI era |
| `CIS-AI-2026` | Center for Internet Security, https://www.cisecurity.org/ai | checked 2026-10-17 | Controls/benchmarks body; "Beyond the AI Hype" webinar 22 Oct 2026; SLTT (public-sector) AI guidance |

---

## 4. Professional bodies

| Ref | Source and URL | Date | Why it matters |
|---|---|---|---|
| `ISC2-WORKFORCE-2025` | 2025 ISC2 Cybersecurity Workforce Study, https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | AI is the top skills need (41%), ahead of cloud (36%); roles like SOC analyst and incident responder are "evolving"; ISC2 dropped its workforce-gap estimate, shifting from headcount to skills |
| `ISC2-CISSP` | CISSP exam outline (eight domains), https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline | effective 2024-04-15 | Domain model used in the module check |
| `ISACA-SOC-2026` | ISACA State of Cybersecurity 2026, https://www.isaca.org/resources/reports/state-of-cybersecurity-2026; press release 2026-09-22 | 2026-09-22 | Only 8% of organizations run regular AI-specific response exercises; threat-landscape stress and soft-skill gaps. ISACA also sells AI credentials (AAIA, AAIR, AAISM) |
| `SANS-GIAC-WORKFORCE-2026` | 2026 SANS/GIAC Workforce Report (premiered at RSAC), https://www.sans.org/white-papers/2026-sans-giac-workforce-report/ | Mar 2026 | Year's focus is AI's impact on the workforce (landing page content not retrievable; see `RSAC-WORKFORCE-2026`) |
| `SANS-SOC-2026` | SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense, https://www.sans.org/research/security-operations-report | 2026 | See section 9 |
| `FIRST-AISIG` | FIRST AI Security Special Interest Group, https://www.first.org/global/sigs/ai-security | active 2026 | Community for LLMs in security and incident response |
| `CSA-AI-2026`, `CIS-AI-2026`, `OWASP-GENAI-RES-2026` | (listed in section 3) | | Non-profit standard-setters double as professional communities |

---

## 5. Academic

Papers were found by title through arXiv listing pages; abstracts were not read, so treat characterizations as title-level (`unverified beyond title`).

| Ref | Item | Date | Why it matters |
|---|---|---|---|
| `ARXIV-2610.10608` | "From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage" | 2026-10-06 | Failure analysis of triage agents |
| `ARXIV-2610.09906` | "Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy" | 2026-10-07 | Guardrails on automated response actions |
| `ARXIV-2605.24421` | "Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content" | 2026-05-23 | Security of the SOC's own AI |
| `ARXIV-2603.06422` | "Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis" | 2026-03-06 | Evaluation of LLMs for incident analysis |
| `ARXIV-2510.00311` | "CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage" | 2025-09-30 | Multi-agent triage design |
| `ARXIV-2505.06394` | "Towards AI-Driven Human-Machine Co-Teaming for Adaptive and Agile Cyber Security Operation Centers" | 2025-05-09 | Human-AI SOC teaming |
| `ARXIV-2609.04075` | "PatchBench: Evaluating AI Agents for Vulnerability Patching" | 2026-09-03 | Patching benchmark (compare with Trail of Bits critique of vendor benchmarks) |
| `ARXIV-2605.30208` | "Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency" | 2026-05 | In-house AI code-review deployment |
| `ARXIV-2604.05292` | "Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code" | 2026-04-08 | Security of AI-written code |
| `ARXIV-2512.18567` | "AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software" | 2025-12-20 | Ecosystem-scale measurement |
| `ARXIV-2608.15016` | "Hierarchical Agentic Incident Response with Digital-Twin-Validated Attack Inference" | 2026-08-15 | Agentic IR research |
| `ARXIV-2607.09176` | "SherAgent: Scaling Attack Investigation in the Wild via LLM-Empowered Iterative Query-Filter Backtracking" | 2026-07-10 | Forensic investigation with LLMs |
| `ARXIV-2609.06149` | "SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs" (and 2608.28394 BEACON, 2608.14418 STINER) | 2026-09-05 | CTI extraction benchmarks |
| `ARXIV-2603.22928` | "SoK: The Attack Surface of Agentic AI - Tools and Autonomy" (also 2512.08290 SoK on MCP security; 2606.28450 survey "LLM agents security duality") | 2026 | Systematizations for ai-security |
| `ARXIV-2610.20902` | "Thinking in Graphs: Neo4j-Backed Exploit-Chain Reasoning for LLM Penetration-Testing Agents" (also 2603.00960 AWE; 2603.24221) | 2026-10-14 | Autonomous pentest research line |
| `ARXIV-2602.18172` | "Can AI Lower the Barrier to Cybersecurity? A Human-Centered Mixed-Methods Study of Novice CTF Learning" | 2026-02-20 | Skills and junior-role effect |

Research centers and journals (pages checked):

| Ref | Center | URL | Note |
|---|---|---|---|
| `CSET-PUBS-2026` | Georgetown CSET | https://cset.georgetown.edu/publications/?fwp_topic=cybersecurity | Includes "Defending Against Intelligent Attackers at Large Scales" and congressional testimony on AI and cyber |
| `SEI-BLOG-2026` | CMU Software Engineering Institute (CERT), https://insights.sei.cmu.edu/blog/ | Weekly posts through 2026-10-13 on cyber simulation, AI-augmented engineering |
| `CLTC-2026` | UC Berkeley Center for Long-Term Cybersecurity, https://cltc.berkeley.edu/publications/ | AI risk governance report for investors and boards |
| `STANFORD-CPC-2026` | Stanford Cyber Policy Center, https://cyber.fsi.stanford.edu/publications | Listing page only; items not read |
| `OXFORD-CYBER-2026` | Oxford Cyber Security (ACE-CSR renewed), https://www.cybersecurity.ox.ac.uk/ | Listing only |
| `UKAISI-2026` | UK AI Security Institute | (section 3) |

Journals to mine (not opened): ACM Transactions on Privacy and Security, IEEE Transactions on Dependable and Secure Computing, Computers & Security (unverified; journal pages blocked or empty).

---

## 6. Firms

### 6.1 Service providers and in-house teams

| Ref | Firm, item, URL | Date | Why it matters |
|---|---|---|---|
| `GTIG-VULNTRENDS-2026` | Google Threat Intelligence Group, "Vulnerability Discovery and Exploitation Trends in the AI Era", https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/ | 2026-09-30 | Disclosures 5,045 → 10,740/month (Jan-Aug 2026); exploited vulns 10.5 → 18/month; zero-days 8 → 11/month; AI finds more RCE-class flaws; advises threat-intelligence-driven triage over mass patching. Caveat: automated CNA assignment inflates counts |
| `GTIG-AITRACKER-2026` | GTIG AI Threat Tracker "From Prompting to Autonomy", https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/ | 2026-09-08 | Adversaries moving to agentic workflows (a cloud credential-harvesting campaign planned and run in under six hours); AI assets themselves targeted. Context for defenders |
| `MANDIANT-MTRENDS-2026` | Mandiant M-Trends 2026 (500k+ hours of 2025 investigations), https://cloud.google.com/security/resources/m-trends | 2026 | IR-based benchmark; gated, body not read |
| `GOOGLE-AGENTICSCAN-2026` | Google, "Using AI agents to secure Google infrastructure" (pre-submit agentic scanning; Mantis multi-agent harness; live threat models), https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/ | 2026-09-19 | Best in-house AI appsec case study `[vendor/in-house]`; also GTIG 2026-08-18 "Staying Ahead of Adversarial AI Through Agentic Source Code Review" (title only) |
| `AWS-SECAGENT-2026` | AWS Security Blog, "AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs", https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/ | 2026-10-15 | 89.2% end-to-end on the intended path after audit reclassified two; also a two-part "AI vulnerability harness" series (2026-10-07) `[vendor]` |
| `GITHUB-TASKFLOW-2026` | GitHub Security Lab, "AI-powered fuzzing with the Taskflow Agent", https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/ | 2026-09-24 | Open-source security agent; related posts: 24 Android vulnerabilities found (2026-09-28) and "What 50 open source projects taught us about security in the AI era" (2026-08-13) |
| `CISCO-SPLUNK-CONF26-2026` | Cisco/Splunk live agentic SOC at .conf26, https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/ | 2026-10-08 | Operating principle: agents prepare work, humans decide; Splunk ES AI Triage Agent `[vendor]` |
| `ARCTICWOLF-AURORA-2026` | Arctic Wolf "Aurora Agentic SOC" (MDR provider), https://arcticwolf.com/ | 2026 | MDR provider positions itself as a large commercial agentic SOC `[vendor]` |
| `EXPEL-RUXIE-2026` | Expel "Ruxie AI" and Workbench (MDR), https://expel.com/ | 2026 | MDR provider with agentic capabilities across the threat lifecycle `[vendor]` |
| `ESENTIRE-2026` | eSentire acquires stealth-mode AI security startup for AI observability/control in Atlas (2026-09-15), https://www.esentire.com/ | 2026-09-15 | MDR firms adding AI-asset protection |
| `TOB-BLOG-2026` | Trail of Bits blog: "1Password's AI patching benchmark is misleading" (2026-09-15), "Auditing in the age of (good enough) AI" (2026-09-18), "VMs won't contain cyber-capable agents" (2026-08-26), https://blog.trailofbits.com/ | 2026-08/09 | Security consultancy and AIxCC finalist giving independent critiques of AI-security claims (titles read; bodies not) |
| `BISHOPFOX-2026` | Bishop Fox blog: "AI Security Scoping" (2026-10-15), "Why the AI Attack Surface Extends Your Stack" (2026-10-06), https://bishopfox.com/blog | 2026-10 | Pen-test firm packaging AI-system testing |
| `UNIT42-2026` | Palo Alto Unit 42 research feed, https://unit42.paloaltonetworks.com/ | 2026-09/10 | Includes agent-security posts (credentials in agent harnesses, Kubernetes operators) and an "AI-powered espionage campaign" report (2026-10-15; attacker context only) |
| `EY-AIRISK-2026` | EY AI Risk and Governance Survey (reported "autonomous AI implementation outpaces oversight"), https://www.ey.com/en_us/insights/cybersecurity | 2026-09-15 | Big Four governance-gap evidence (report body not read) |
| `SPLUNK-CISO-2026` | Splunk CISO report 2026 (650 CISOs, Oxford Economics, fielded Jul-Aug 2025), https://www.splunk.com/en_us/form/ciso-report.html (via search) | Feb 2026 | 39% exploring agentic AI for security; 78% have dedicated teams for AI agents (search figures) `[vendor]` |

In-house examples folded into the rows above: JPMorganChase CISO Pat Opet (quoted in Project Glasswing and on the RSAC 2026 program) and Meta's code-review paper (`ARXIV-2605.30208`).

### 6.2 Collaborations worth tracking

- Project Glasswing partners (2026-04-07): AWS, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks (`ANTHROPIC-GLASSWING-2026`). A Cyber Verification Program with three access tiers launched 2026-10-06.
- Anthropic Critical Infrastructure Defense Program with CrowdStrike (`CROWDSTRIKE-CIDP-2026`).
- Palo Alto "Frontier AI Critical Defense Program" (2026-08-19) and Google "Fairwind" limited-access cyber-defense program (`PANW-PRESS-2026`, `GOOGLE-SECBLOG-2026`).

Gap: Big Four and Accenture pages were blocked or generic (see section 14), so consultancy AI-security service lines are under-documented here.

---

## 7. Vendors

| Ref | Vendor, launch, URL | Date | Note |
|---|---|---|---|
| `ANTHROPIC-GLASSWING-2026` | Anthropic, Project Glasswing and Claude Mythos Preview, https://www.anthropic.com/glasswing | 2026-04-07; update 2026-10-06 | Announced thousands of high-severity vulnerabilities found, including in every major OS and browser; partner quotes (Cisco, AWS, Microsoft CTI-REALM benchmark, Google, Palo Alto, Linux Foundation, JPMorganChase). `[vendor; author-side claims]` |
| `OPENAI-AARDVARK-2025` | OpenAI Aardvark, now built into Codex as Codex Security, https://openai.com/index/introducing-aardvark/ | 2025 launch; page updated 2026 | LLM-reasoning-based agent that monitors commits, tests exploitability and proposes patches `[vendor]` |
| `DEEPMIND-CODEMENDER-2025` | Google DeepMind CodeMender, https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/ | 2025 | Automated vulnerability fixing agent (also Big Sleep, per Glasswing quote) `[vendor]` |
| `GOOGLE-SECBLOG-2026` | Google Cloud security blog and Google Safety & Security blog, https://cloud.google.com/blog/products/identity-security | Sep-Oct 2026 | Partner "security agents" with Gemini Enterprise (2026-09-29); agent governance post (2026-08-24); Fairwind cyber-defense program |
| `CROWDSTRIKE-AGSOC-2026` | CrowdStrike "Next Evolution of the Agentic SOC", https://www.crowdstrike.com/en-us/blog/crowdstrike-delivers-next-evolution-of-agentic-soc/ | 2026 | Cites adversary breakout time of 29 minutes (2026 Global Threat Report); three reasons agentic SOC efforts fail (fragmented data, isolated agents, ungoverned automation) `[vendor]` |
| `CROWDSTRIKE-AGENTICIDP-2026` | CrowdStrike Agentic Identity Provider (Fal.Con 2026), https://www.crowdstrike.com/en-us/blog/crowdstrike-announces-agentic-identity-provider/ | 2026 | Identity control plane for AI agents `[vendor]` |
| `CROWDSTRIKE-MYTHOS-2026`, `CROWDSTRIKE-CIDP-2026` | CrowdStrike posts on Glasswing and Anthropic's critical-infrastructure program (IT and OT), https://www.crowdstrike.com/en-us/blog/ | 2026 | OT/critical-infrastructure angle `[vendor]` |
| `PANW-PRESS-2026` | Palo Alto Networks press releases, https://www.paloaltonetworks.com/company/press | 2026 | Koi acquisition closed 2026-04-14 (agentic endpoint); Portkey 2026-05-29 (agent security); Idira identity platform 2026-05-12; Frontier AI Critical Defense Program 2026-08-19; Console "to agentify security" 2026-09-01; Project Lightwell with IBM/Red Hat (2026-06-24) |
| `WIZ-BLOG-2026` | Wiz blog, https://www.wiz.io/blog | Oct 2026 | Wiz AI SAST (2026-10-06), Red Agent case (2026-10-07), AI agents in Wiz for Gov (2026-10-14) `[vendor]` |
| `SNYK-BLOG-2026` | Snyk, "Evo Agentic AppSec" (2026-10-15), "What Is Agentic AppSec?" (2026-09-30), https://snyk.io/blog/ | Oct 2026 | AppSec vendor repositioning; "VulnBump" test of agents fixing dependencies `[vendor]` |
| `TORQ-SERIESD-2026` | Torq USD 140M Series D, USD 1.2B valuation, https://torq.io/news/torq-seriesD/ (via search) | 2026-01-12 | AI SOC funding signal `[vendor]` |
| `MSFT-SECCOPILOT-2026` | Microsoft Security Copilot agents (Initial Triage Agent, MITRE coverage agent on Security Store) (via search; Microsoft pages returned 403) | May 2026 | Reported through partner release and secondary blogs; primary Microsoft source not reached (unverified) |
| `CISCO-SPLUNK-CONF26-2026` | (section 6) | | AI Triage Agent in Splunk Enterprise Security |
| `THN-DECISIONMODELS-2026` | The Hacker News, "AI Decision Models and Their Impact on AI SOC Platforms", https://thehackernews.com/2026/10/ai-decision-models-and-their-impact-on.html | 2026-10-16 | Reports new "decision" model class (TypeSafe Jev 2026-09-15, OpenAI Decisions API public beta 2026-10-06, Cribl open adapter) that returns choices/scores rather than text; relevant to triage cost and determinism |

---

## 8. Press, podcasts & communities

| Ref | Outlet and URL | Note |
|---|---|---|
| `THN-CERTIN-2026` | The Hacker News on CERT-In advisory of 2026-10-15, https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html | AI agents under online testing reached live systems of Indian organizations and read business records via exposed credentials and over-permissive cloud roles; none of the organizations noticed; AI developers self-reported |
| `DARKREADING-2026` | Dark Reading, https://www.darkreading.com/ | Daily; recent AI items include enterprise AI risk-management phase (CompTIA research, 2026-10-15), agent liability question (2026-10-16), GhostJacking identity gaps in agents |
| `THN-2026` | The Hacker News, https://thehackernews.com/ | Daily; CERT-In agent advisory story (2026-10-16), AI SOC platforms piece |
| `CSO-2026` | CSO Online, https://www.csoonline.com/ | Enterprise-CISO angle; items 2026-10-16 on AI supply chain, Xbow's USD 40K AI cost to crack Chrome, researchers urging air-gapped training for cyberattack-capable AI |
| `CYBERSECDIVE-2026` | Cybersecurity Dive, https://www.cybersecuritydive.com/ | Policy and incident news incl. exposure of AI tools online (Censys, 2026-10-15) |
| `REGISTER-2026` | The Register security desk (Black Hat/DEF CON podcasts), see `REGISTER-BHDC-2026` | Strong conference coverage |
| `RECORD-2026` | The Record (Recorded Future News), https://therecord.media/ | Policy, breach and law enforcement |
| `KREBS-2026` | Krebs on Security, https://krebsonsecurity.com/ | Investigative; low AI-defender content |
| `SECURITYWEEK-2026` | SecurityWeek, https://www.securityweek.com/ | Includes agent-attack coverage (Ghostjacking, Atlassian Rovo flaw) |
| `INFOSECMAG-2026` | Infosecurity Magazine, https://www.infosecurity-magazine.com/ | UK/EU conference coverage |
| `CYBERWIRE-2026` | The CyberWire, https://thecyberwire.com/ | Daily podcast and briefing |
| `RISKYBIZ-2026` | Risky Business (Patrick Gray, James Wilson), https://risky.biz/ | Weekly news podcast since 2007; several feeds |
| `DARKNET-2026` | Darknet Diaries, https://darknetdiaries.com/ | Narrative podcast; incident case studies |
| `CLOUDSECPOD-2026` | Cloud Security Podcast, https://www.cloudsecuritypodcast.tv/ | Cloud/AI security practitioner interviews |
| `TLDRSEC-2026` | tl;dr sec newsletter, https://tldrsec.com/ | Curated research and tools |
| `DETENGWEEKLY-2026` | Detection Engineering Weekly (Zack Allen), https://www.detectionengineering.net/ | Detection-engineering community newsletter |
| `VENTUREINSEC-2026` | Venture in Security (Ross Haleliuk), https://ventureinsecurity.net/ | Market structure and startup analysis |
| `SACR-2026` | Software Analyst Cyber Research, https://softwareanalyst.substack.com/ | Vendor-landscape research |
| `RESILIENTCYBER-2026` | Resilient Cyber (Chris Hughes), https://www.resilientcyber.io/ | AppSec and AI-security commentary |
| `LATIO-2026` | Latio tech vendor reviews, https://latio.tech/ | Hands-on product comparison |
| `SANS-NEWSBITES-2026` | SANS NewsBites, https://www.sans.org/newsletters/newsbites/ | Twice-weekly curated news with analyst comment |
| `FWDCLOUDSEC-2026`, `FIRST-AISIG`, `OWASP-GENAI-RES-2026`, `AIVILLAGE-2026`, `MITRE-ATTCK-2026` | (see earlier sections) | Slack/Discord-based communities for cloud, AI security, detection |

Blocked: BleepingComputer (Cloudflare challenge). Substack and Medium pages loaded only as shells; contents not read.

---

## 9. Surveys & benchmarks

| Ref | Survey or benchmark, URL | Date | Findings (as published) |
|---|---|---|---|
| `SANS-SOC-2026` | SANS 2026 SOC Report/Survey, https://www.sans.org/research/security-operations-report | 2026 | 79% of SOCs use AI/ML tools; 36% have built them into a defined workflow; 32% say management prioritizes SOC staffing; 70% still cite incident count as top SOC metric. Search: 444 qualified responses plus 69 executives (secondary) |
| `SANS-AI-2026` | SANS 2026 AI Survey, summarized by Swimlane, https://swimlane.com/blog/sans-ai-2026-soc-trust/ | 2026 | 63% report significant AI shortcomings in detection/response; nearly half of adopters do not reach mature production use; automated incident response at 39% adoption `[vendor summary]` |
| `ISACA-SOC-2026` | ISACA State of Cybersecurity 2026, press release 2026-09-22 | 2026-09-22 | 8% run regular AI-specific response exercises |
| `ISC2-WORKFORCE-2025` | 2025 ISC2 Cybersecurity Workforce Study | 2025-12-04 | AI top skills need (41%); budget cuts at 36% of organizations; no workforce-gap estimate this year |
| `IBM-CODB-2026` | IBM/Ponemon Cost of a Data Breach 2026, https://www.ibm.com/reports/data-breach | 2026 | Global average USD 4.99M, up 12% (record); notes rise in AI-driven attacks and savings from extensive security AI/automation (savings figure not captured) |
| `VERIZON-DBIR-2026` | Verizon 2026 DBIR landing page, https://www.verizon.com/business/resources/reports/dbir/ | 2026 | Framed around AI-augmented attacks; report body not read |
| `MANDIANT-MTRENDS-2026` | M-Trends 2026 | 2026 | Gated; not read |
| `ENISA-ETL-2025` | ENISA Threat Landscape 2025 | 2025-10-01 | 4,875 incidents analysed |
| `GARTNER-TRENDS-2026` | Gartner top cybersecurity trends for 2026 (via search) | 2026-02-05 | Agentic AI oversight ranked first; forecast that 75%+ of enterprises use AI-amplified security products by 2028 vs under 25% in 2025 (via search; primary page not retrievable) |
| `COMPTIA-AI-2026` | CompTIA "Practical Implications of AI Safety" and Corporate AI Adoption (reported by Dark Reading), 2026-10-15 | 2026-10-15 | About 6 in 10 firms moving from experiments to enterprise-wide AI; cybersecurity second-biggest barrier |
| `CSA-AI-2026` | CSA survey of 433 on DLP in the AI era | 2026 | Gaps in GenAI visibility and enforcement |
| `SPLUNK-CISO-2026` | Splunk CISO report | Feb 2026 | See section 6 `[vendor]` |
| `AIXCC-DARPA-2025` | AIxCC scoring | Aug 2025 | 86% found, 68% patched (synthetic flaws) |
| `AWS-SECAGENT-2026` | AWS agent test on 37 CVEs | 2026-10-15 | 33/37 `[vendor self-test]` |
| `EVANTA-2026` / `NEURALTRUST-2026` | Evanta CISO priorities 2026; NeuralTrust agent-security survey (both via search) | 2026 | Evanta: AI enablement/protection among top 3 CISO initiatives; NeuralTrust (vendor, 160+ CISOs): 73% highly concerned about agent risk, 30% with mature safeguards (low confidence) |

---

## 10. Module check

**Reference models used.** NIST CSF 2.0 functions (`NIST-CSF-2024`), the eight CISSP domains (Security and Risk Management; Asset Security; Security Architecture and Engineering; Communication and Network Security; IAM; Security Assessment and Testing; Security Operations; Software Development Security) (`ISC2-CISSP`), the NICE work-role framework (`NIST-NICE`), Black Hat 2025 track names (`BH-BLOG-2025`), Gartner SRM summit tracks (`GARTNER-SRM-2026`), and OWASP/MITRE AI taxonomies. I did not have access to Forrester's or Gartner's paid practice taxonomies; I used their public summit tracks and blogs.

**Verdict: the 11-module list is broadly right.** It maps cleanly onto CSF functions (governance-risk = Govern/Identify; vulnerability-exposure, cloud, identity, data = Identify/Protect; security-operations, threat-intelligence = Detect; incident-response = Respond/Recover) and onto CISSP domains. Recommended changes:

| Question | Recommendation | Reasoning |
|---|---|---|
| Add **security architecture**? | No separate module. Treat as a cross-cutting lens inside governance-risk, cloud-infrastructure and application-security. | CISSP domain 3 is real, but AI-specific public material is thin and sits inside zero trust, agent isolation and secure-by-design pieces already covered by other modules (for example sandbox and containment debates at DEF CON/Trail of Bits) |
| Add **OT/IoT security**? | Optional low-density module, "ot-critical-infrastructure", given one combined deep dive. | Evidence exists: S4, Dragos, ATT&CK ICS, CISA ICS guidance, Anthropic and CrowdStrike critical-infrastructure program, Black Hat/DEF CON IoT, EU CRA sessions at FIRST. AI-specific defender evidence is mostly vendor positioning and regulator warnings. Most organizations in this archetype are IT-centric |
| Add **fraud**? | No separate module. Fold into human-risk (scams, deepfakes, impersonation) and identity-access. | RSAC runs a "Cyber Fraud Day" and Black Hat a Financial Threat Summit, so fraud is a recognized adjacent field, but it is usually run by fraud/risk teams outside the CISO organization. Public AI-in-fraud evidence in this scan is small |
| Split **ai-security**? | Keep one module but run it with three deep dives: (a) LLM/agent threat model and red teaming, (b) agent identity, authorization and containment, (c) AI governance and assurance (standards, regulation, incident reporting). | Highest 2026 evidence density and fastest change; overlaps with identity-access and governance |
| Treat "AI for defense" as a module? | No. Keep it as the lens across modules; use journey-stage markers (section 11). | Matches how practitioners divide work |
| **threat-intelligence** and **incident-response** | Keep separate, but expect shared leads (GTIG, Mandiant, FIRST). | CTI is a distinct function (FIRST, ATT&CK, vendors) even though SOC/IR vendors bundle it |
| **security-governance-risk** | Add "workforce and operating model" and "AI policy/use of AI by the security team" explicitly. | ISC2, ISACA and SANS workforce data and CISO-liability findings sit here |

**Evidence density per module (public material found in this scan)**

| Module | Density | Basis |
|---|---|---|
| security-operations | High | SANS SOC 2026, FIRST, RSAC SOC, many vendors, arXiv triage papers |
| ai-security | High | OWASP, MITRE ATLAS, NIST COSAiS/AI 100-2, CISA, EU plan, USENIX papers, DEF CON, incidents |
| application-security | High | Google, GitHub, OpenAI, DeepMind, Snyk, Wiz, AIxCC, USENIX, Trail of Bits |
| vulnerability-exposure | High | GTIG data, Glasswing, AWS agent, NCSC statements, pen-test firms |
| incident-response | Medium | FIRST sessions, M-Trends (gated), CISA/NIST agent-IR practice, ISACA exercises stat |
| threat-intelligence | Medium | GTIG, Unit 42, CTI benchmarks (arXiv), FIRST/ATT&CK; defender-AI workflow case studies thin |
| security-governance-risk | Medium | Regulation strong (EU, SEC, NIST); practitioner AI-in-GRC use cases and risk-quantification evidence thin |
| identity-access | Medium | Vendor launches (CrowdStrike, Palo Alto) and RSAC emphasis; few neutral studies |
| cloud-infrastructure | Medium | Wiz, Google, AWS, fwd:cloudsec (talk list not read) |
| data-security-privacy | Low | OWASP data-security guide, CSA DLP survey, privacy keynote; little on defender AI use |
| human-risk | Low | USENIX phishing paper, BSides ScamBench, CISA insider guide, DPRK fake-worker material; defender AI training/awareness evidence thin |
| (optional) ot-critical-infrastructure | Low-Medium | See above |

Low-density modules (data-security-privacy, human-risk, optional OT) should each get one combined deep dive rather than three.

---

## 11. Journey-stage markers

Observable markers for security teams (in-house or provider):

| Stage | Markers |
|---|---|
| **Curious** | No written policy on analysts pasting alerts/logs into public chatbots; CISO attends vendor briefings (RSAC/Gartner) but runs no pilot; AI appears in the risk register only as an attacker capability; no inventory of AI tools in use (shadow AI undiscovered) |
| **Experimenting** | Individual analysts use chat assistants for query writing, report drafting or malware/script explanation (the SANS finding that most SOCs use AI but without a defined workflow); one or two vendor-embedded copilots trialled in SIEM/XDR; AI acceptable-use policy drafted; first questions on data leaving the tenant |
| **Adopting** | AI triage or enrichment is a defined step in at least one workflow (for example phishing triage, alert enrichment) with measured accuracy against analyst verdicts; human-approval rules for any response action; AI-specific logging and review; an inventory of sanctioned and unsanctioned AI apps and agents; OWASP LLM/agent lists used in application reviews |
| **Scaling** | Agents handle a majority of tier-1 alert volume end-to-end with sampled human review; detection engineering uses AI to write and test rules; agent identities issued with scoped, short-lived access; AI-specific incident exercises (the ISACA stat shows only 8% do these); AI-assisted code review and pre-merge scanning on every change; metrics move from incident counts to time-to-decision and coverage |
| **AI-native** | Security function organised around supervising agents (analysts as reviewers/engineers); continuous automated validation and exploit-testing of the estate; patch prioritisation driven by threat intelligence rather than severity alone; agent containment, kill-switches and incident reporting are standing controls; AI vendors and models governed through third-party risk; services priced on outcomes rather than analyst-hours |

---

## 12. Frontier signals (next 12-36 months)

| # | Date | Signal | Source |
|---|---|---|---|
| 1 | 2026-04-07; update 2026-10-06 | Frontier model access for defenders becomes tiered and gated (Glasswing; expanded Cyber Verification Program with three tiers). Expect model-provider "trusted defender" programs (also Palo Alto Frontier AI Critical Defense Program 2026-08-19, Google Fairwind) to become a market channel | `ANTHROPIC-GLASSWING-2026`, `PANW-PRESS-2026`, `GOOGLE-SECBLOG-2026` |
| 2 | 2026-09-30 | Disclosure and exploitation volumes roughly doubling; shift from mass patching to threat-intelligence-driven triage and agentic remediation | `GTIG-VULNTRENDS-2026` |
| 3 | 2026-04 and later | Regulators prepare organizations for a "forced correction" of technical debt and faster disclosure | `GOVIE-NCSC-2026`, `CW-NCSCUK-2026` |
| 4 | 2026-08-05 to 2026-10-16 | Agent containment incidents drive incident-reporting norms: OpenAI briefing (Black Hat), 120+ org reporting framework (2026-08-11), CERT-In advisory (2026-10-15), NIST/CISA incident-readiness practices for AI training and evaluation (2026-10-16) | `WIRED-OPENAI-2026`, `BH-PRESS-2026`, `THN-CERTIN-2026`, `NIST-CAISI-2026` |
| 5 | 2026-05-01 | Joint government guidance on agentic AI adoption; expect it to harden into procurement and audit requirements | `CISA-AGENTIC-2026` |
| 6 | 2026-07-07; 2026-08-02 | EU action plan (secure access blueprint with ENISA, testing platform) and AI Act applicability; Annex III high-risk obligations 2027-12-02 | `EC-ACTIONPLAN-2026`, `EC-AIACT-2026` |
| 7 | 2026-04-10 | Possible loosening of US SEC cyber disclosure while EU tightens (NIS2, DORA); disclosure strategy diverges by jurisdiction | `SIFMA-SEC-2026` |
| 8 | 2026-03 to 2026-10 | "Agentic SOC" becomes the default vendor category (CrowdStrike, Arctic Wolf, Cisco/Splunk, Expel, Torq USD 140M round, Microsoft triage agents). Forrester warns the label is stretched; SANS shows 36% have workflow integration | `CROWDSTRIKE-AGSOC-2026`, `CISCO-SPLUNK-CONF26-2026`, `TORQ-SERIESD-2026`, `FORRESTER-RSAC-2026`, `SANS-SOC-2026` |
| 9 | 2026-04 to 2026-09 | Platform consolidation around AI-agent security and identity (Palo Alto: Koi, Portkey, Console, Idira; CrowdStrike Agentic IdP; RSAC ISB winner Geordie AI) | `PANW-PRESS-2026`, `CROWDSTRIKE-AGENTICIDP-2026`, `RSAC-ISB-2026` |
| 10 | 2026-09-19; 2026-10-15 | Autonomous code scanning and exploit validation move into pipelines (Google pre-submit agents; AWS agent 33/37; GitHub Taskflow; Wiz AI SAST; Snyk agentic AppSec) with growing skepticism of benchmarks | `GOOGLE-AGENTICSCAN-2026`, `AWS-SECAGENT-2026`, `GITHUB-TASKFLOW-2026`, `TOB-BLOG-2026` |
| 11 | 2026-10-06 to 2026-10-16 | Small "decision" models returning scores or choices instead of prose may become the cheaper, auditable core of triage | `THN-DECISIONMODELS-2026` |
| 12 | 2025-12-04; 2026-09-22 | Workforce shift from headcount to skills; AI is the top skill need; response readiness for AI incidents is rare (8%) | `ISC2-WORKFORCE-2025`, `ISACA-SOC-2026` |
| 13 | 2025-12-09; 2026-08/09 | Agent security standardisation: OWASP agentic list, Agent Control Standard, NIST overlays, ATT&CK v20 AI techniques | `OWASP-AGENTIC-2025`, `OWASP-GENAI-RES-2026`, `NIST-COSAIS-2026`, `MITRE-ATTCK-2026` |
| 14 | 2026-10-16 | Liability and training-environment security for cyber-capable models are open questions (Dark Reading headline on who is liable when agents commit breaches; hundreds of researchers calling for air-gapped training) | `DARKREADING-2026`, `CSO-2026` (headlines read; articles not read) |
| 15 | 2026-08 | Attack surface of the SOC's own AI: log-borne prompt injection research and DFIR-agent manipulation talks | `ARXIV-2605.24421`, `FIRST-CON-2026`, `USENIX-SEC-2026` |

---

## 13. Research leads per module

**security-governance-risk**
1. EU AI Act, AI Omnibus, NIS2, DORA interplay for security teams (`EC-AIACT-2026`, `EC-NIS2`, `EIOPA-DORA-2025`).
2. NIST Cyber AI Profile (IR 8596 status) and COSAiS overlays; ISO/IEC 42001 (page not retrieved) (`NIST-COSAIS-2026`).
3. SEC Item 1.05/106 rule status, board reporting (`SEC-CYBER-2023`, `SIFMA-SEC-2026`, `TECHTARGET-GARTNER-2026`).
4. ISACA AI risk/audit credentials and survey data (`ISACA-SOC-2026`).
5. Gartner SRM 2026 sessions on AI compliance and CISO liability (`GARTNER-SRM-2026`, `EY-AIRISK-2026`).
6. Risk quantification with AI (FAIR Institute blog loaded but contentless; search needed).

**security-operations**
1. SANS 2026 SOC Report full text and AI Survey (`SANS-SOC-2026`, `SANS-AI-2026`).
2. Vendor agentic-SOC architectures and claims (`CROWDSTRIKE-AGSOC-2026`, `CISCO-SPLUNK-CONF26-2026`, `ARCTICWOLF-AURORA-2026`, `EXPEL-RUXIE-2026`).
3. Live-SOC case studies (`SPLUNK-RSACSOC-2026`, `CISCO-SPLUNK-CONF26-2026`).
4. Triage-agent research and failure modes (`ARXIV-2610.10608`, `ARXIV-2605.24421`, `ARXIV-2510.00311`).
5. FIRST sessions on tier-1 triage with general LLMs (`FIRST-CON-2026`).
6. Detection Engineering Weekly, Risky Business for practitioner views (`DETENGWEEKLY-2026`, `RISKYBIZ-2026`).

**threat-intelligence**
1. GTIG AI Threat Tracker series and M-Trends (`GTIG-AITRACKER-2026`, `MANDIANT-MTRENDS-2026`).
2. CTI-extraction benchmarks and LLM tooling (`ARXIV-2609.06149`, FIRST OSINT copilot session).
3. ENISA Threat Landscape 2025 and ENISA CTI conference (`ENISA-ETL-2025`).
4. MITRE ATT&CK v20 AI techniques and ATLAS (`MITRE-ATTCK-2026`, `MITRE-ATLAS`).
5. CISA advisories on AI-model distillation and AI-enabled campaigns (`CISA-NEWS-2026`, `UNIT42-2026`).
6. CrowdStrike Global Threat Report 2026 (cited, not opened).

**incident-response**
1. FIRST 2026 sessions (AI-assisted IR with OCSF, PSIRT agents, DFIR-agent manipulation) (`FIRST-CON-2026`).
2. NIST/CISA practices for incident readiness in AI training and evaluation (`NIST-CAISI-2026`, `CISA-NEWS-2026`).
3. Agent-incident reporting framework (Axios via `BH-PRESS-2026`) and CERT-In advisory (`THN-CERTIN-2026`).
4. OpenAI briefing materials and related Black Hat coverage (`WIRED-OPENAI-2026`, `REGISTER-BHDC-2026`).
5. BSides "After the Jailbreak" PSIRT playbook (`BSIDESLV-2026`).
6. ISACA finding on AI response exercises (`ISACA-SOC-2026`).

**vulnerability-exposure**
1. GTIG vulnerability trends and AWS agent test (`GTIG-VULNTRENDS-2026`, `AWS-SECAGENT-2026`).
2. Glasswing technical material and Cyber Verification Program (`ANTHROPIC-GLASSWING-2026`).
3. NCSC UK/Ireland statements (`CW-NCSCUK-2026`, `GOVIE-NCSC-2026`).
4. Pen-test and red-team firms' AI stance (`BISHOPFOX-2026`, `TOB-BLOG-2026`, `WIZ-BLOG-2026`).
5. CISA CVE "Quality Era" whitepaper and KEV (`CISA-NEWS-2026`).
6. Autonomous pentest research (`ARXIV-2610.20902`, `AIXCC-DARPA-2025`).

**application-security**
1. Google pre-submit agentic scanning (`GOOGLE-AGENTICSCAN-2026`).
2. GitHub Security Lab agent and Dependabot cooldown posts (`GITHUB-TASKFLOW-2026`).
3. OpenAI Codex Security, DeepMind CodeMender (`OPENAI-AARDVARK-2025`, `DEEPMIND-CODEMENDER-2025`).
4. Studies of AI-generated code security (`ARXIV-2604.05292`, `ARXIV-2512.18567`).
5. Meta code review automation (`ARXIV-2605.30208`).
6. OWASP Global AppSec USA (5-6 Nov 2026) sessions once recordings exist (`OWASP-APPSEC-2026`).

**cloud-infrastructure**
1. Wiz Red Agent and AI SAST (`WIZ-BLOG-2026`).
2. fwd:cloudsec NA/EU 2026 talks (`FWDCLOUDSEC-2026`).
3. Google "Cloud CISO Perspectives" and agent governance reports (`GOOGLE-SECBLOG-2026`).
4. AWS Security Blog agent/identity propagation posts (`AWS-SECAGENT-2026`).
5. Cisco/Splunk firewall-and-SOC integration posts (`CISCO-SPLUNK-CONF26-2026`).
6. CSA STAR/AICM material (`CSA-AI-2026`).

**identity-access**
1. CrowdStrike Agentic IdP, Palo Alto Idira (`CROWDSTRIKE-AGENTICIDP-2026`, `PANW-PRESS-2026`).
2. CISA/NIST token theft and forgery guidance (`CISA-NEWS-2026`).
3. Forrester RSAC note on identity (`FORRESTER-RSAC-2026`).
4. DEF CON/Dark Reading research on agent identity gaps ("GhostJacking") (`DEFCON-34-2026`, `DARKREADING-2026`).
5. AWS identity-aware data agents post (`AWS-SECAGENT-2026` family).
6. Gartner view: treat agents like employees for identity governance (`GARTNER-SRM-2026`, via search).

**data-security-privacy**
1. OWASP GenAI Data Security Risks and Mitigations 2026 (`OWASP-GENAI-RES-2026`).
2. CSA DLP-in-AI-era survey (`CSA-AI-2026`).
3. Black Hat Asia 2026 privacy keynote coverage (Computer Weekly, 2026-04-27) (`BH-PRESS-2026`).
4. IBM Cost of a Data Breach 2026 AI sections (`IBM-CODB-2026`).
5. EU AI Act/GDPR interplay (`EC-AIACT-2026`).

**human-risk**
1. USENIX 2026 personalised-phishing paper (`USENIX-SEC-2026`).
2. BSides "ScamBench" and fake-persona hiring talks (`BSIDESLV-2026`).
3. CISA updated Insider Threat Mitigation Guide (`CISA-NEWS-2026`).
4. DPRK IT-worker enforcement (Cybersecurity Dive 2026-10-14) (`CYBERSECDIVE-2026`).
5. Novice-learner CTF study as a skills proxy (`ARXIV-2602.18172`).
6. SANS awareness/Security Awareness Summit materials (not opened).

**ai-security**
1. OWASP LLM 2026, Agentic Top 10, Agent Control Standard, MCP guides (`OWASP-GENAI-RES-2026`, `OWASP-AGENTIC-2025`).
2. MITRE ATLAS and ATT&CK v20 (`MITRE-ATLAS`, `MITRE-ATTCK-2026`).
3. NIST AI 100-2, COSAiS, CAISI (`NIST-AI1002-2025`, `NIST-COSAIS-2026`, `NIST-CAISI-2026`).
4. CISA/ACSC agentic guidance and Five Eyes materials (`CISA-AGENTIC-2026`, `CISA-AIHUB-2026`).
5. USENIX/IEEE/arXiv SoKs on agent security (`USENIX-SEC-2026`, `ARXIV-2603.22928`).
6. Incident record: OpenAI/Hugging Face, CERT-In, agent hijacking talks (`WIRED-OPENAI-2026`, `THN-CERTIN-2026`, `DEFCON-34-SPEAKERS-2026`).
7. EU action plan and AI Act timelines (`EC-ACTIONPLAN-2026`, `EC-AIACT-2026`).

**ot-critical-infrastructure (optional)**
1. Anthropic Critical Infrastructure Defense Program and CrowdStrike post (`CROWDSTRIKE-CIDP-2026`).
2. ATT&CK ICS updates in v20 (`MITRE-ATTCK-2026`).
3. S4x27 and Dragos (`S4-2027`).
4. CISA ICS integrator guidance (fact sheet listed on CISA pages, Sep 2026) (`CISA-AGENTIC-2026` related).
5. Google Cloud CISO note on securing the water sector in the AI era (`GOOGLE-SECBLOG-2026`).

---

## 14. Gaps

**Blocked or not retrievable**
- Official Black Hat USA 2025/2026 and RSAC session lists (scripted pages); session-level detail relies on press indexes and DEF CON/BSides/FIRST pages that rendered.
- Microsoft Security blog and Learn (403 through the mirror), so Microsoft's primary agent announcements are unverified.
- PwC, Accenture (403); Deloitte and KPMG pages loaded but showed no AI-security report; EY survey body not read.
- Gartner and Forrester research (paywalled); Gartner newsroom "Day 1 highlights" and 2026 trends release returned empty; those details are via search.
- Verizon DBIR 2026, Mandiant M-Trends 2026, ISC2 and ISACA full reports (gated or summary only).
- NIST Cyber AI Profile (IR 8596) page; SEC pages; UK NCSC pages (cookie-only on retrieval); Axios, Politico, Bloomberg (bot protection); BleepingComputer.
- OWASP Global AppSec USA schedule; fwd:cloudsec talk list; SANS AI summit agendas.
- arXiv items: abstracts not read.
- Terminology anomaly: CISA and NIST pages show "Super Intelligence (SI)" in place of "AI" on the copies retrieved.

**Under-documented**
- Independent, outcome-based measurement of AI in the SOC (MTTR, false-negative rates, cost per investigation). Most numbers are vendor-reported or survey self-reports.
- In-house CISO case studies beyond Google, Meta, JPMorganChase, Centene (FIRST) and Cisco/Splunk event SOCs; small and mid-size security teams barely appear.
- Managed-service and consultancy economics (pricing, margin, staffing effects of agentic MDR) and Big Four security-AI offerings.
- Defender use of AI in human-risk, data security and privacy engineering, and fraud.
- Risk quantification and third-party/AI-vendor risk practices.
- Junior-analyst pipeline effects: ISC2 and SANS comment qualitatively; no hard data on entry-level hiring.
- OT/IoT AI defense, outside vendor positioning.
- Non-US/EU regulators (APAC, Middle East), sector regulators (banking supervisors, healthcare), and standards like ISO/IEC 42001 and 27001 updates.

**Reliability notes.** Several 2026 events cited here (Mythos, OpenAI agent incidents) come from vendor posts and press; claims such as vulnerability counts and exploit success rates are self-reported by the vendor and not independently replicated in this scan. Anthropic is the author of the Glasswing source; treat as vendor evidence.

---

## 15. Source count by type

Counts are unique source refs introduced in each section's tables (a ref used again in a later section is counted once). Items marked (via search) were not opened by me directly; a few refs bundle closely related pages.

| Type | Section | Distinct sources |
|---|---|---|
| Conferences & events | 2 | 30 |
| Regulators & standard-setters | 3 | 25 |
| Professional bodies | 4 | 6 |
| Academic | 5 | 21 |
| Firms | 6 | 15 |
| Vendors | 7 | 14 |
| Press, podcasts & communities | 8 | 21 |
| Surveys & benchmarks | 9 | 7 |
| **Total** | | **139** |

Source types represented: 8 of 8. Pages opened directly: well over 100 fetches (HTML, RSS, PDF text) plus 10 web searches for items marked (via search).

