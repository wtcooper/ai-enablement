# Security x workforce-talent

Cross-cutting topic note for the security archetype (NIST CSF 2.0 value chain; in-house CISO organizations and security service providers). Research date: 2026-10-17. Topic: the security workforce, covering the ISC2 and ISACA workforce gap studies, SOC analyst roles and burnout, the entry-level pipeline under AI, new roles, skills and certifications, and how providers staff services.

Reading convention: every factual sentence carries a source ref in square brackets with a locator. "Self-reported" means a survey of practitioners or an organization describing itself. "Vendor-published" means the publisher sells related products. Forecasts are labelled with who made them. Module ids follow the new naming (governance-risk, operations, data-privacy). This topic mainly touches **operations** and **governance-risk**.

Disclosure: the model that wrote this note is made by Anthropic. Two sources below were published by Anthropic (`ANTHROPIC-JOBS-2026`, `ANTHROPIC-SKILLS-2026`); both are marked as author-side evidence.

---

## 1. Summary

- **The headline "gap" is no longer a single number, and the two big professional-body studies now point in different directions on hiring.** ISC2 stopped publishing a workforce-gap estimate in its 2025 study (fielded July-August 2025, 16,029 respondents) and says respondents rank skills above headcount [ISC2-WORKFORCE-2025, Research Note; Methodology]. Its last estimate, for 2024, was 4,763,963 people, up 19.1% on 2023 [ISC2-WORKFORCE-2024, Workforce Insights]. ISACA's 2026 survey (1,800+ respondents) reports 58% of organizations understaffed (55% in 2025), but its sponsor comments that organizations with no open cybersecurity positions increased year on year [ISACA-SOC-2026, press release 2026-09-22].
- **"Skills over headcount" is now consensus across sources, but each measures it differently.** SANS/GIAC reports 60% skills versus 40% headcount, up from 52% skills a year earlier [RSAC-WORKFORCE-2026, slide 17]; ISC2 reports skills deficits eclipse staff shortages [ISC2-WORKFORCE-2025, Key Findings]; the UK government's labour-market study sizes the UK workforce gap at about 3,800 people for 2024 [DSIT-CYBERSKILLS-2025, Details].
- **AI is widely used in security work but unevenly embedded, and the evidence on what it does to the entry-level seat is thin and mostly indirect.** 79% of SOCs use AI/ML tools, 36% have built them into a defined workflow [SANS-SOC-2026, Top Takeaways]. In SANS/GIAC's workforce survey, 32% of organizations say AI has reduced SOC/security analyst entry-level roles, and 39% report no role reductions yet [RSAC-WORKFORCE-2026, slide 7]. Independent labour-market data (ADP payroll, all occupations) shows employment of 22-25-year-olds in AI-exposed occupations 19% below trend [STANFORD-CANARIES-2026, Abstract]; I found no security-specific estimate there.
- **Hiring demand is shifting toward senior, engineering and "build" roles.** A vendor-published analysis of 665 US postings (August 2026) found entry-level roles at 5.9%, engineering-family roles outnumbering SOC analyst roles about three to one, and detections-as-code in 46% of plain SOC analyst postings [D3-SOCREBUILD-2026, one-pager; Finding on entry-level; skills section]. Fortinet's survey reports 51% need senior skills most versus 13% for entry-level [FORTINET-SKILLS-2026, p.4 and Conclusion].
- **Providers are positioning as "AI-augmented, human-led", and the analysts they hire are no longer zero-experience.** Gartner's 2026 MDR Market Guide (9 Sep 2026) added "AI-augmented" to its MDR definition and forecast that by 2029, 90% of initial MDR findings will be processed with AI support and no human action, up from 30% today [EXPEL-GARTNERMDR-2026, quoted passages; forecast by Gartner, relayed by a vendor]. An MDR provider's SOC analyst posting requires 2+ years of experience and AI use with output validation [JOBS-HUNTRESS-2026].
- **New roles are visible but small.** SANS/GIAC reports 34% of organizations creating AI/ML specialist roles, 32% AI security engineers and 30% AI governance analysts [RSAC-WORKFORCE-2026, slide 8]. D3 counted 25 "AI security engineer"-type postings out of 665 and no AI-titled analyst postings at end-user enterprises [D3-SOCREBUILD-2026, AI-title evidence].
- **Skill-formation risk is the live worry.** Practitioners, Gartner and an MDR provider all warn that automating junior work removes the learning path [GARTNER-SOC-2025; DEW-151; ARCTICWOLF-AURORA-2026]. Direct evidence is adjacent only: one randomized trial of software developers showed 17% lower quiz mastery with AI assistance [ANTHROPIC-SKILLS-2026], while a reverse-engineering study found novices' comprehension rose about 98% with LLM help [NDSS-2026].
- **Burnout and retention are measured, but not yet linked to AI by independent data.** 68% of ISACA respondents say their role is more stressful than five years ago; high stress is the top reason for leaving (52%) [ISACA-SOC-2026]. ISC2 reports 47% often feel overwhelmed by workload [ISC2-WORKFORCE-2025, Job Satisfaction section].

---

## 2. Findings

### 2.1 The workforce gap studies: what each measures

**ISC2 (professional body, survey of practitioners; self-reported).**
- The 2025 study is an online survey collected in July and August 2025 from 16,029 individuals responsible for cybersecurity across four regions [ISC2-WORKFORCE-2025, Methodology]. It was published 2025-12-04 [ISC2-WORKFORCE-2025, page header].
- ISC2 did not include a workforce-gap estimate in 2025, saying that respondents in 2024 and 2025 prioritized critical skills over more people [ISC2-WORKFORCE-2025, Research Note].
- The prior estimate (2024 study, published 2024-10-31): global workforce 5,468,173 and gap 4,763,963, a 19.1% rise on 2023. ISC2 defines the gap as the difference between the professionals respondents say their organizations need and the active professionals, and says it is not an estimate of job openings [ISC2-WORKFORCE-2024, Workforce Insights].
- In 2025, 36% of respondent organizations had budget cuts, 39% hiring freezes, 34% promotion freezes and 24% layoffs; ISC2 describes these as levelling off [ISC2-WORKFORCE-2025, Economic Factors section]. 33% said they lack budget to staff adequately and 29% cannot afford the skills they need [ISC2-WORKFORCE-2025, Economic Factors section].
- 34% said they have the right staffing level, up 4 points [ISC2-WORKFORCE-2025, Skills Shortages section].
- 88% reported at least one significant consequence of a skills deficiency and 69% more than one [ISC2-WORKFORCE-2025, Skills Shortages section].
- Sample caveat: 5% of 2025 respondents were entry/junior-level staff and 39% nonmanagerial mid/advanced staff [ISC2-WORKFORCE-2025, Appendix, Respondent Level]. The AI optimism below therefore comes mostly from people already established in the field.

**ISACA (professional body, survey; sponsor Wolters Kluwer TeamMate).**
- The 2026 State of Cybersecurity survey (12th annual) gathered responses from more than 1,800 cybersecurity professionals; press release dated 2026-09-22 [ISACA-SOC-2026, press release].
- 58% say their team is understaffed (55% last year). The press release says 49% report open cybersecurity positions [ISACA-SOC-2026, press release]. ISACA's own 2026-10-05 newsletter restating the findings says 61% [ISACA-ATISACA-2026]. I could not reconcile the two figures. The sponsor quote in the press release says there is a year-on-year increase in organizations with no open positions [ISACA-SOC-2026, press release].
- For comparison, the 2025 release reported 55% understaffed and 65% with unfilled positions [ISACA-SOC-2025, first paragraph].
- 55% report difficulty retaining qualified staff [ISACA-SOC-2026, press release].
- Biggest skills gaps named in 2026: LLM SecOps 45% (up 12 points on 2025, 21 on 2024), soft skills 57%, cloud 31%, data security 31%, ML SecOps 31% [ISACA-SOC-2026, press release].
- Only 13% of respondents do not use AI in security operations. Uses among AI users: automating threat detection/response 41% (32% in 2025), automating routine tasks 40% (28%), endpoint security 33% [ISACA-SOC-2026, press release].
- 51% are involved in developing, onboarding or implementing AI solutions (40% in 2025, 29% in 2024); 56% say they or their team helped write an AI-use policy [ISACA-SOC-2026, press release].
- Only 8% of organizations run AI-specific response exercises regularly; 64% have run none; 48% either do not know of or lack AI incident playbooks [ISACA-SOC-2026, press release].
- To fill technical skills gaps, 35% are raising reliance on AI or automation (up 12 points), 27% train non-security staff for security roles and 26% use contractors or consultants [ISACA-SOC-2026, press release].

**SANS/GIAC Workforce Report 2026 (premiered at RSAC 2026; third annual).**
- I could read only the presenters' slides (SANS CAIO/Chief of Research and SANS CEO), not the report; sample size is not on the slides [RSAC-WORKFORCE-2026, slides 1-3, 23].
- 60% see the problem as skills versus 40% headcount (52% skills a year earlier); 48% report a moderate to extreme skills gap [RSAC-WORKFORCE-2026, slide 17].
- Effects reported from the skills gap: 57% delayed projects, 47% increased burnout and slower incident response, 42% cannot adopt new technology or maintain adequate monitoring [RSAC-WORKFORCE-2026, slide 18].
- Career progression is the third largest hiring obstacle at 31% (9% the prior year); only 24% provide well-defined career progressions [RSAC-WORKFORCE-2026, slide 15].
- 53% say the cyber manager or senior leadership, rather than HR, is the primary hiring decision maker [RSAC-WORKFORCE-2026, slide 14].
- Internal inconsistency to flag: slide 10's title says regulatory impact on hiring "jumped from 40% to 95%" while its body says 68% report moderate-to-extreme impact; slide 12's title says 56% use workforce frameworks for job requisitions "up from 40%" while its body says "46% last year" [RSAC-WORKFORCE-2026, slides 10, 12]. Treat these two series as unverified until the full report is read.

**Other measurements of the gap.**
- WEF Global Cybersecurity Outlook 2026 (published 2026-01-12, with Accenture): 804 qualified survey participants from 92 countries [WEF-GCO-2026, Appendix: Methodology]. Among organizations reporting insufficient cyber resilience, 85% lack critical people and skills, versus 22% of highly resilient organizations [WEF-GCO-2026, Figure 43]. The top three roles in shortage were threat intelligence analysts, DevSecOps engineers and identity and access management specialists [WEF-GCO-2026, section on resilience and skills]. 54% cite insufficient knowledge or skills as a barrier to implementing AI for cybersecurity [WEF-GCO-2026, Figure 13].
- UK DSIT labour-market study (published 2025-09-19, covering calendar 2024): about 143,000 employed in cyber roles, a workforce gap of about 3,800 (3,500 the previous year and 11,100 in the 2023 report), and 32,370 core cyber job postings, down 33% [DSIT-CYBERSKILLS-2025, Details]. The method mixes business surveys, qualitative work and Lightcast postings data [DSIT-CYBERSKILLS-2025, Details]. The contrast with ISC2's global estimate shows how method-dependent "the gap" is.
- Fortinet 2026 Cybersecurity Skills Gap report (Sapio Research fieldwork December 2025; 2,750 IT and cybersecurity decision-makers; vendor-commissioned): 60% say finding candidates with AI cybersecurity experience is their top recruiting challenge, 63% expect more need for AI oversight and governance roles over three years, and 52% struggle to retain talent [FORTINET-SKILLS-2026, Methodology; p.4; "Finding candidates with AI experience" section].
- CyberSeek (supply and demand heat map) did not render usable figures with curl, so no US supply-demand ratio is reported here.

### 2.2 SOC analyst roles, AI adoption and burnout

- SANS 2026 SOC Report (10th annual; 444 practitioners and 69 cyber leaders): 79% of SOCs use AI/ML, 36% have built it into a defined workflow, 32% of practitioners say management prioritizes SOC staffing, and 70% still cite incident count as the top metric [SANS-SOC-2026, Top Takeaways; page intro]. SANS notes sponsors had no role in questions or findings [SANS-SOC-2026, Vendor Neutrality].
- SANS also reports that meaningful work and career progression have outranked pay as top retention drivers for three straight years, and that SIEM is the most requested hiring skill [SANS-SOC-2026, More Key Findings].
- ISC2: 28% have integrated AI security tools, 19% are testing, 22% are in early evaluation; among active users, 63% report a significant productivity boost and 21% say no meaningful impact [ISC2-WORKFORCE-2025, AI section]. 40% expect network monitoring to see the largest near-term AI impact, 30% security operations [ISC2-WORKFORCE-2025, AI section].
- ISC2 says traditional roles such as SOC analyst and incident responder are evolving [ISC2-WORKFORCE-2025, Introduction]. In its survey, 73% say AI will create more specialized cybersecurity skills and only 18% are considering changing careers because of AI [ISC2-WORKFORCE-2025, AI section].
- Burnout measures: 48% exhausted by keeping up with threats and technology; 47% often overwhelmed by workload; 32% overworked due to shortages [ISC2-WORKFORCE-2025, Job Satisfaction section]. 68% (ISACA) say their role is more stressful than five years ago, 71% of those blaming the complex threat landscape; top stressors include unrealistic expectations/too much work (52%) and work-life balance (45%) [ISACA-SOC-2026, press release]. High stress is the leading reason people leave (52%), then limited promotion and development (47%) [ISACA-SOC-2026, press release].
- A Forrester Consulting study commissioned by NETSCOUT (October 2025) found 61% of respondents say analysts spend more than ten hours a week in the "analyze" phase; this reached me through a sponsored brand post, so treat it as vendor-published [CSO-NETSCOUT-2026, paragraph 1].
- Arctic Wolf's 2026 AI & Cybersecurity Trends Report (vendor-published) found security leaders spend 13-15 hours a week on each of nine tasks, roughly three full-time people of work; nearly 60% are investing in automation or AI and 57% in training and certifications [ARCTICWOLF-STRETCHED-2026, paragraphs 1-3].
- No independent study I found measures whether AI triage reduces analyst burnout or attrition. The practitioner newsletter Detection Engineering Weekly asks the question directly: if AI solves analyst burnout, what is lost when analysts live in summaries instead of raw telemetry [DEW-151, "Detection Engineering Gem" section].
- Quality evidence relevant to how much analysts must check agents: in a research benchmark of 1,247 alerts from a multi-stage attack scenario, every one of five LLM triage approaches studied missed at least 40.4% of attack-related alerts; the authors' multi-agent design with a judge cut false negatives to 3.1% (preprint, 7 Oct 2026, not peer reviewed) [ARXIV-2610.10608, Abstract]. A separate preprint shows log content can inject instructions into an LLM analyst: persona hijacks suppressed 68% of malicious logs under a naive classifier in a gpt-4o-mini test, and the strongest defense cut average injection success from 26.6% to 11.8% [ARXIV-2605.24421, Abstract]. These support a continuing human validation role.
- A mixed-methods study (survey N=248, interviews N=24) found SOC analysts accepted AI outputs even at lower accuracy when explanations were relevant and evidence-backed [ARXIV-2503.02065, Abstract].

### 2.3 The entry-level pipeline and apprenticeship under AI

**What the sources measure directly.**
- SANS/GIAC: asked where AI is affecting entry-level jobs (select all that apply), SOC and security analysts led at 32%, then threat intel analysts 26%, incident responders 22% and DevSecOps 19%; 39% reported no role reductions yet [RSAC-WORKFORCE-2026, slide 7].
- Fortinet: 51% need senior-level skills most, 32% mid-level, 13% entry-level; the report calls AI a "partial solution" to the skills gap at entry level and says entry-level positions are likely to change toward AI skills [FORTINET-SKILLS-2026, p.4; Conclusion]. The "partial solution" wording is Fortinet's interpretation, not a survey result.
- D3 Security (an AI SOC vendor) coded 665 in-scope US postings from August 2026: entry-level roles were 5.9% (39 postings); 67% of postings had no AI language; the classic zero-experience triage seat survives mainly at MSSPs, MDR providers, staffing contracts and state government, often on nights at $60k-$83k; some enterprise entry roles are now "Security Engineer I, Threat Hunting" style [D3-SOCREBUILD-2026, one-pager; entry-level finding]. This measures postings, not hires, in one month.
- ISACA 2025: 38% say entry-level hiring takes three to six months; just 29% of enterprises trained non-security staff for security roles versus 41% a year earlier; 46% say over half of current cyber staff transitioned from outside the field [ISACA-SOC-2025, paragraphs 1-3].
- ISC2 2025: IT is the main route in (56%); internships or apprenticeships were the route for 3% of respondents, who were the most likely (69%) to recommend their route [ISC2-WORKFORCE-2025, Is Cybersecurity Still Closely Tied to IT?]. Among 21-29-year-olds who entered via non-IT, non-education routes, 8% came through internships or apprenticeships [ISC2-WORKFORCE-2025, same section].
- UK DSIT: core cyber job postings fell 33% in 2024 [DSIT-CYBERSKILLS-2025, Details]. This is overall postings, not entry-level.
- Gartner (forecast, January 2025 summary): analysts Pete Shoard and Jeremy D'Hoinne say AI and automation may sharply reduce entry-level SOC roles, which would limit junior staff gaining the experience to reach senior roles, and predict that by 2028 one-third of senior security operations roles will stay vacant for over a year [GARTNER-SOC-2025, paragraphs 2-3]. This is a forecast relayed by a trade outlet; the primary Gartner document was not accessible.

**Adjacent economy-wide and learning evidence (cap: adjacent, not security).**
- Stanford (Brynjolfsson, Chandar and Chen, August 2026 version; ADP payroll data through June 2026): employment of ages 22-25 in AI-exposed occupations is 19% below where it would be versus less-exposed peers; the gap works mainly through reduced hiring; the authors call this descriptive, not causal [STANFORD-CANARIES-2026, Abstract]. Information Security Analysts appear in the top-50-by-ADP-employment list for the highest AI-exposure quintile, but the paper's headline estimates are pooled, not security-specific [STANFORD-CANARIES-2026, Appendix Table A.6].
- Anthropic randomized trial (2026-01-29; author-side evidence): software developers using AI assistance scored 50% on a mastery quiz versus 67% for those coding by hand; the largest gap was in debugging; interaction style mattered [ANTHROPIC-SKILLS-2026, results]. It is a coding task, not a security task.
- NDSS 2026 study of software reverse engineering (153-practitioner survey plus 48 participants over 109 hours): LLM help raised novices' comprehension by about 98%, matching experts, while experts gained little; hallucinations were also observed [NDSS-2026, Abstract].
- A case study of one novice using an agentic AI framework for CTF challenges (preprint, 2026-02-20, n=1) reported lower entry barriers alongside concerns about trust and dependency [ARXIV-2602.18172, Abstract].

**Provider and practitioner responses.**
- Arctic Wolf (MDR provider; blog dated 2026-09-25 in page metadata) says about a quarter of its SOC team is Gen Z and that it aims to keep new analysts close to decisions that need interpretation, while its agents escalate to humans when confidence is low [ARCTICWOLF-AURORA-2026, paragraphs 2-3, 11-13]. This is self-described practice, not measured outcome.
- Arizona State University runs a paid, year-long Junior Student SOC Analyst Program in its live enterprise SOC, with a funded Security+ path, 5-10 investigation reports a week in one phase, and a "Month 3: AI in the SOC" module; the inaugural cohort is six students; the page is undated and says applications closed Aug 20 [ASU-STUDENTSOC-2026, program phases; cohort FAQ].
- Gartner recommends accelerating junior-to-senior progression and building manual verification into training to limit skill erosion [GARTNER-SOC-2025, final paragraphs].
- ISACA says a Certified Cybersecurity Specialist credential for early-career professionals is slated for release in December 2026 [ISACA-SOC-2026, press release].
- Expel panelists (leaders from ZoomInfo, Riot Games and Markel) describe "human over the loop" supervision, keeping detection engineering and remediation changes under human control, and report automation incidents that deleted cloud accounts or banned a legitimate hash across 7,000 devices [EXPEL-HUMANS-2026, panel summary]. Vendor-hosted discussion.

### 2.4 New and changing roles

- SANS/GIAC (select all that apply): AI/ML specialists 34%, AI security engineers 32%, AI governance analysts 30% are new roles organizations are creating [RSAC-WORKFORCE-2026, slide 8].
- D3's posting analysis: 25 of 665 postings were "AI security engineer"-type, a title it says did not exist 18 months earlier; zero AI-titled analyst postings at end-user enterprises; 22.7% of postings carried an active AI or automation requirement (automation engineering 42%, detection engineering 31%, incident response 17%, triage-centered analyst roles 9%); 76 postings (11.4%) described agentic-era work; median advertised pay was $125k for SOC analysts, $142k for SecOps engineers, $152k for automation engineers, $161k for detection engineers [D3-SOCREBUILD-2026, one-pager; AI-title evidence; AI requirement section]. Vendor-published, US only, postings not hires.
- Detections-as-code appears in 31% of all postings, 90% of detection engineering roles and 46% of plain SOC analyst postings [D3-SOCREBUILD-2026, skills section]. A practitioner view in the same period called detection-as-code "overrated" in an issue title, so the practice is contested [DEW-154 title in the Detection Engineering Weekly archive, 2026-04-29; DETENGWEEKLY-2026].
- Named job postings, all dated Aug-Oct 2026 on public ATS boards: Anthropic seeks a Security Risk & Compliance lead for Agent Security (policy for how agents handle regulated data, human-approval criteria, mapping to ISO 42001 and the EU AI Act) and a Detection & Response engineer to build LLM-using tooling [ANTHROPIC-JOBS-2026, postings 5443871008 and 5448539008]. Cloudflare posted an AI Security Research & Red Team Engineer; Datadog a Senior Product Security Engineer for its coding agent; Robinhood a Staff Software Engineer, AI Security building a platform for security teams to build AI agents; SentinelOne a Staff Security Researcher for Detection AI [JOBS-ENTERPRISE-2026, titles and updated dates]. These show role design, not headcount.
- In-house design: Figma's security team built a triage agent (Panther SIEM alerts, Slack, Tines) and reports its on-call engineers' work shifted from "investigate from scratch" to reviewing and correcting the agent's findings; self-reported results: about 70% reduction in time-to-resolution on complex alerts and 20% fewer on-call pages (blog dated 2026-07-29) [FIGMA-AGENTS-2026, summary and results sections]. Figma uses on-call engineers rather than a tiered analyst queue.
- NICE (NIST) said in June 2025 it is developing an Artificial Intelligence Security Competency Area (out for public comment then) and will add AI-related task, knowledge and skill statements to work roles, covering security of AI and security through AI [NIST-NICE-AIBLOG-2025, "The NICE Framework and AI"]. I did not confirm its final status.
- SANS/GIAC: 56% say workforce frameworks define job requisitions (see inconsistency flagged above); 40% use NICE and 34% use the European ECSF in job descriptions [RSAC-WORKFORCE-2026, slide 12].

### 2.5 Skills and certifications

- ISC2: hiring managers' technical priorities were cloud security (29%), AI (27%), security engineering (24%); professionals saw AI (44%) and cloud (40%) as most in demand [ISC2-WORKFORCE-2025, Skills Prioritization section]. Hiring managers' top five skills overall were all nontechnical: problem solving 29%, collaboration 24%, communications 22%, willingness to learn 20%, strategic thinking 16% [ISC2-WORKFORCE-2025, same section].
- ISC2 AI skills: 48% building general AI knowledge; 35% learning AI risks; 22% learning to audit AI systems; 17% hold AI qualifications and 53% plan to [ISC2-WORKFORCE-2025, AI section]. Most-cited AI competencies: AI in threat detection and response (42%), threat modeling and risk assessment (39%), defending AI models (35%) [ISC2-WORKFORCE-2025, Key Skills for AI].
- ISACA: critical thinking (59%), communication (57%), problem solving (53%) are the soft skills in demand; employers paying for certification fees rose to 61% from 54% [ISACA-SOC-2026, press release].
- SANS/GIAC: 58% consider certifications very or extremely important; 43% use them for promotions; 37% for consulting or client requirements; 33% for audits [RSAC-WORKFORCE-2026, slide 19]. Fortinet: 91% of IT decision-makers prefer candidates with technology-focused certifications and 92% would pay for an employee to get certified [FORTINET-SKILLS-2026, p.4].
- Credential supply is moving toward AI. CompTIA SecAI+ (CY0-001) launched 2026-02-17; recommended experience is 3-4 years in IT and 2+ years of hands-on cybersecurity; objectives: securing AI systems 40%, AI-assisted security 24%, AI governance risk and compliance 19%, basic AI concepts 17% [COMPTIA-SECAI-2026, exam details; objectives]. ISACA's AAISM requires an active CISM or CISSP [ISACA-AAISM, eligibility]. GIAC's catalog lists 12 AI-category certifications, including AI Security Automation Engineer (GASAE, flagged "NEW"), AI Penetration Tester and AI Platform Security [GIAC-CERTS-2026, featured item; Artificial Intelligence filter].
- Note that several of these AI credentials assume prior experience, which sits awkwardly with the entry-level squeeze (inference from the stated prerequisites, not a source claim).

### 2.6 How providers staff services

- Gartner 2026 MDR Market Guide (9 Sep 2026; quoted by Expel): MDR now means "remotely delivered, AI-augmented, human-led, turnkey, modern SOC functions"; it requires 24/7 staffing with customer-specific context and no limits on triage volume; Gartner says buyers should demand clarity on which services are AI-augmented versus analyst-delivered [EXPEL-GARTNERMDR-2026, quoted passages 1-2, 5, 8]. Forecast by Gartner: by 2029, 90% of initial MDR findings processed with AI support and no human action, up from 30% today [EXPEL-GARTNERMDR-2026, quoted passage 2].
- Expel markets "Ruxie AI" as making human analysts better, with 24x7 human analysts and a 14-minute mean time to remediate on fully automated high and critical incidents (vendor-published) [EXPEL-RUXIE-2026, homepage sections; EXPEL-GARTNERMDR-2026, paragraph 4].
- Arctic Wolf says it cannot be fully automated: agents are bounded, escalate to human experts when confidence drops, and are backtested by its analysts; senior analysts spend more time on advanced investigations and are expected to codify techniques into the system (vendor-published) [ARCTICWOLF-AURORA-2026, paragraphs 9-14].
- ReliaQuest's site headline offers to "Eliminate Tier 1 and Tier 2" with agentic AI (marketing claim, no staffing data) [RELIAQUEST-2026, hero].
- Huntress (MDR provider) posted a SOC Analyst role (remote Australia, AUD $110k-$140k base plus bonus and equity) that requires 2+ years of SOC, IR, MDR or forensics experience and use of AI tools with validation of outputs, and mentions "Human Led Agentic workflows" [JOBS-HUNTRESS-2026, What You'll Do; What You Bring].
- Live-SOC examples from vendors: Splunk's RSAC 2026 SOC credited an automation playbook with saving more than nine analyst hours [SPLUNK-RSACSOC-2026, automation section]; Cisco and Splunk's .conf26 SOC used a "blended analyst team" where the Triage Agent prepared findings and analysts of different specialization validated them (blog dated 2026-10-08) [CISCO-SPLUNK-CONF26-2026, paragraphs 1, 6-8]. Both are vendor-published event SOCs, not production customer SOCs.
- Enterprise demand reaches AI SOC capability through services first, per D3's reading that the highest-paid AI SOC jobs ($160k-$200k) sit at integrators and consultancies [D3-SOCREBUILD-2026, AI SOC platform section]. This is D3's interpretation of posting data.
- ISC2 2025: 20% outsource work, 19% bring in third-party service providers and 17% hire temporary contractors to offset skills shortages; 25% turn to AI and automation [ISC2-WORKFORCE-2025, Skills Shortages section]. ISACA 2026: 26% increase use of contractors or consultants for technical gaps [ISACA-SOC-2026, press release].
- No source I found publishes provider headcount, analyst-to-customer ratios, margins or pricing changes from agentic MDR.

---

## 3. What it means for an AI transformation conversation

### Implications

1. **Frame the problem as skills and judgment capacity, not headcount.** Four independent bodies (ISC2, SANS/GIAC, WEF, DSIT) point to skills; an AI plan that only counts alerts per analyst misses the constraint [ISC2-WORKFORCE-2025; RSAC-WORKFORCE-2026, slide 17; WEF-GCO-2026, Fig. 43; DSIT-CYBERSKILLS-2025].
2. **Design the human role before buying the agent.** Where AI is working in public examples, the analyst becomes a reviewer and supervisor with an explicit evidence chain (Figma, Cisco/Splunk, Arctic Wolf) [FIGMA-AGENTS-2026; CISCO-SPLUNK-CONF26-2026; ARCTICWOLF-AURORA-2026]. The write-ups describe escalation rules and review, which the leader should specify too.
3. **Plan the apprenticeship path deliberately.** If the tier-1 queue shrinks, juniors lose the learning route Gartner, DEW and Arctic Wolf all name [GARTNER-SOC-2025; DEW-151; ARCTICWOLF-AURORA-2026]. Evidence that the entry-level seat is already disappearing is mixed: 32% report analyst role reductions, 39% none, entry postings are 5.9% in one vendor's sample [RSAC-WORKFORCE-2026, slide 7; D3-SOCREBUILD-2026].
4. **New roles are mostly redesigned old ones.** AI security engineer, detection engineer and agent-governance roles recruit from senior engineering, GRC and IR backgrounds, with 7+ years of experience in at least one posting [ANTHROPIC-JOBS-2026; D3-SOCREBUILD-2026]. Reskilling existing staff (57% of Fortinet respondents expect it) may be a faster route than hiring [FORTINET-SKILLS-2026, p.60 area].
5. **Readiness lags adoption.** Only 8% run AI-specific response exercises, 20% give all staff comprehensive AI training, and 72% say AI governance is still in development [ISACA-SOC-2026; RSAC-WORKFORCE-2026, slides 5-6].
6. **For providers, the pricing and staffing model is the transformation.** Gartner expects AI to process most initial findings by 2029 while insisting the service stays human-led [EXPEL-GARTNERMDR-2026]. A provider leader should decide what the human-led part is, and how juniors are trained inside it.
7. **Budget, not talent supply, is cited as the main root cause by ISC2 respondents.** Budget cuts and hiring freezes drive staff shortages, so AI may be funded as a substitute for headcount, which raises the retention and risk questions in 2.1 [ISC2-WORKFORCE-2025, Economic Factors section].

### Interview probes

1. Who reviews the agent's closed alerts, how often, and what share of closures get sampled? (SANS: 36% have workflow integration; ALERT-BENCH miss rates) [SANS-SOC-2026; ARXIV-2610.10608]
2. If tier-1 triage is automated, how will an analyst hired this year learn what a bad alert looks like in raw telemetry? [DEW-151; GARTNER-SOC-2025]
3. Which three roles in your team have changed in the last 12 months (title, tasks, pay), and which were redefined rather than newly hired? [D3-SOCREBUILD-2026; ISC2-WORKFORCE-2025]
4. How do you measure whether AI changed analyst workload, attrition or time-to-decision, as opposed to alert counts? (SANS: 70% still use incident count) [SANS-SOC-2026]
5. For providers: which parts of your service would you describe to a buyer as AI-delivered versus analyst-delivered, and what happens to your analyst bench ratio over the next 24 months? [EXPEL-GARTNERMDR-2026]
6. Who in your security team is involved in AI governance and AI incident exercises today? [ISACA-SOC-2026]

### Objections and evidence-based responses

| Objection | Response from the evidence |
|---|---|
| "There is a 4-5 million person shortage, so AI will not cost jobs." | ISC2's last estimate (4,763,963 for 2024) was withdrawn as a headline in 2025 in favour of skills, and the UK's own method sizes the UK gap at about 3,800 [ISC2-WORKFORCE-2024; ISC2-WORKFORCE-2025, Research Note; DSIT-CYBERSKILLS-2025]. Shortage of senior skills can coexist with fewer entry seats. |
| "AI will replace SOC analysts." | No source here shows replacement. 79% use AI but 36% have a defined workflow; 39% report no entry-level role reductions yet; Gartner's own MDR guide keeps "human-led" [SANS-SOC-2026; RSAC-WORKFORCE-2026, slide 7; EXPEL-GARTNERMDR-2026]. Benchmarks show triage agents miss 40%+ of attack alerts in one test [ARXIV-2610.10608]. |
| "AI is just a tool; juniors will adapt fine." | One RCT (coding, Anthropic) found lower mastery with AI assistance, while an RE study found novices gained about 98% in comprehension; effects depend on how AI is used, and neither is security triage [ANTHROPIC-SKILLS-2026; NDSS-2026]. Design training explicitly. |
| "Practitioners are optimistic, so no workforce risk." | ISC2's sample is 5% entry/junior; 28% feel less confident about career longevity and 16% regret entering the field [ISC2-WORKFORCE-2025, Appendix; Job Satisfaction section]. |
| "We can buy an MDR and drop the staffing question." | Providers are hiring experienced analysts and keeping humans in escalation paths [JOBS-HUNTRESS-2026; ARCTICWOLF-AURORA-2026]. Gartner tells buyers to ask which parts are AI-augmented [EXPEL-GARTNERMDR-2026]. |
| "Certifications will fix the skills gap." | Employers value them (58% very or extremely important) but new AI certifications assume 2-3+ years of experience (SecAI+) or CISM/CISSP (AAISM) [RSAC-WORKFORCE-2026, slide 19; COMPTIA-SECAI-2026; ISACA-AAISM]. |

---

## 4. Frontier signals

| Date | Signal | Who said it / type | Source |
|---|---|---|---|
| 2025-06-12 | NIST NICE says it is adding an AI Security Competency Area and AI task, knowledge and skill statements to work roles | Government standard-setter, plan | [NIST-NICE-AIBLOG-2025] |
| 2025-12-04 | ISC2 drops the workforce-gap estimate and reports skills over headcount | Professional body, survey | [ISC2-WORKFORCE-2025] |
| 2026-01-12 | WEF GCO 2026 links skills shortage to low resilience (85% vs 22%) | International body, survey | [WEF-GCO-2026, Fig. 43] |
| 2026-01-29 | Randomized trial of AI assistance and coding skill mastery (author-side evidence) | Anthropic, research | [ANTHROPIC-SKILLS-2026] |
| 2026-02-17 | CompTIA SecAI+ exam launched | Certification body, in production | [COMPTIA-SECAI-2026] |
| 2026-03 | SANS/GIAC workforce report premiere at RSAC: AI reduces entry-level roles for 32%, creates AI security engineer roles for 32% | Training body, survey | [RSAC-WORKFORCE-2026, slides 7-8] |
| 2026-08 | Stanford update: 22-25-year-old employment gap in AI-exposed occupations at 19% | Academic, descriptive | [STANFORD-CANARIES-2026] |
| 2026-08-27 | D3 posting analysis: entry-level 5.9%, engineering roles 3x analyst roles | Vendor-published | [D3-SOCREBUILD-2026] |
| 2026-09-09 | Gartner MDR Market Guide adds "AI-augmented, human-led"; forecast 90% of initial MDR findings AI-processed by 2029 | Gartner forecast, via Expel | [EXPEL-GARTNERMDR-2026] |
| 2026-09-22 | ISACA: 8% regular AI response exercises; LLM SecOps skill gap 45% | Professional body, survey | [ISACA-SOC-2026] |
| 2026-09-25 | Arctic Wolf describes a Gen Z share of about a quarter and a design intended to keep juniors learning | MDR provider, self-described | [ARCTICWOLF-AURORA-2026] |
| 2026-10-20 (upcoming) | ISACA webinar "State of Cyber 2026" on workforce | Professional body, event | [ISACA-SOC-2026] |
| 2026-12 (planned) | ISACA Certified Cybersecurity Specialist for early-career professionals "slated" for release | Professional body, announced | [ISACA-SOC-2026] |
| Forecast, by 2028 | One-third of senior security operations roles vacant for more than a year | Gartner, forecast (Jan 2025) | [GARTNER-SOC-2025] |

---

## 5. Sources

Access: **full** = page or document body read; **partial** = only part readable (named in the note).

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ISC2-WORKFORCE-2025 | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | Professional body survey | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full (web version; PDF not read) |
| ISC2-WORKFORCE-2024 | 2024 ISC2 Cybersecurity Workforce Study | ISC2 | Professional body survey | https://www.isc2.org/Insights/2024/10/ISC2-2024-Cybersecurity-Workforce-Study | 2024-10-31 | full |
| ISACA-SOC-2026 | Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises (State of Cybersecurity 2026 press release) | ISACA | Professional body press release | https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises | 2026-09-22 | full (report itself gated; landing page read) |
| ISACA-ATISACA-2026 | ISACA State of Cybersecurity Report Tracks AI's Growing Influence on Security Landscape | ISACA @ISACA newsletter | Professional body | https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2026/volume-19/isaca-state-of-cybersecurity-report-tracks-ais-growing-influence-on-security-landscape | 2026-10-05 | full |
| ISACA-SOC-2025 | State of Cybersecurity 2025 Global Press Release | ISACA | Professional body press release | https://www.isaca.org/about-us/newsroom/press-releases/2025/state-of-cybersecurity-2025-global-press-release | 2025-09 (date not shown on page) | full |
| ISACA-AAISM | Advanced in AI Security Management (AAISM) | ISACA | Certification page | https://www.isaca.org/credentialing/aaism | checked 2026-10-17 | full |
| SANS-SOC-2026 | SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense | SANS Institute | Professional/training body survey | https://www.sans.org/research/security-operations-report | 2026 (month not shown) | partial (landing page; report gated) |
| RSAC-WORKFORCE-2026 | AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce (slides, SANS/GIAC Workforce Report premiere) | RSA Conference / SANS and GIAC | Conference slides | https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce | 2026-03 (posted 2026-03-23 per landscape) | partial (slides only; full report not retrieved) |
| NIST-NICE-AIBLOG-2025 | The Impact of Artificial Intelligence on the Cybersecurity Workforce | NIST NICE | Government standard-setter blog | https://www.nist.gov/blogs/cybersecurity-insights/impact-artificial-intelligence-cybersecurity-workforce | 2025-06-12 | full |
| WEF-GCO-2026 | Global Cybersecurity Outlook 2026 | World Economic Forum with Accenture | International body survey | https://reports.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2026.pdf | 2026-01-12 | full |
| DSIT-CYBERSKILLS-2025 | Cyber security skills in the UK labour market 2025 | UK DSIT | Government research | https://www.gov.uk/government/publications/cyber-security-skills-in-the-uk-labour-market-2025 | 2025-09-19 (updated 2026-02-02) | partial (summary page; full report not read) |
| STANFORD-CANARIES-2026 | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI (Aug 2026 version) | Stanford Digital Economy Lab | Academic working paper | https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf | 2026-08 | full |
| ANTHROPIC-SKILLS-2026 | How AI assistance impacts the formation of coding skills | Anthropic | Research (author-side) | https://www.anthropic.com/research/AI-assistance-coding-skills | 2026-01-29 | full |
| D3-SOCREBUILD-2026 | The SOC Rebuild Index: 2026 Edition | D3 Security | Vendor-published posting analysis | https://d3security.com/resources/soc-rebuild-index-2026/ | 2026-08-27 | full |
| FORTINET-SKILLS-2026 | 2026 Cybersecurity Skills Gap Global Research Report | Fortinet (Sapio Research fieldwork) | Vendor-commissioned survey | https://www.fortinet.com/content/dam/fortinet/assets/reports/2026-cybersecurity-skills-gap-report.pdf | fieldwork Dec 2025; published 2026 | full |
| GARTNER-SOC-2025 | Security skills gap to leave one-third of senior roles vacant by 2028 (Gartner analysts D'Hoinne and Shoard) | SecurityMEA (reporting Gartner) | Trade press on analyst forecast | https://securitymea.com/2025/01/27/security-skills-gap-to-leave-one-third-of-senior-roles-vacant-by-2028/ | 2025-01-27 | full (secondary; Gartner primary not reached) |
| EXPEL-GARTNERMDR-2026 | AI-augmented, still human-led: What changed in the 2026 Gartner Market Guide for MDR | Expel | Vendor blog quoting Gartner | https://expel.com/blog/what-changed-in-the-2026-gartner-market-guide-for-managed-detection-and-response/ | 2026-09-21 | full (Gartner report itself paywalled) |
| EXPEL-HUMANS-2026 | Why three security leaders still won't let AI make the call | Expel | Vendor webinar summary | https://expel.com/blog/why-three-security-leaders-still-wont-let-ai-make-the-call/ | 2026-10-02 | full |
| EXPEL-RUXIE-2026 | Expel homepage (Ruxie AI) | Expel | Vendor site | https://expel.com/ | checked 2026-10-17 | full |
| ARCTICWOLF-AURORA-2026 | How the Aurora Agentic SOC Is Building the Next Generation of SOC Analysts | Arctic Wolf | Vendor blog | https://arcticwolf.com/resources/blog/how-aurora-agentic-soc-is-building-next-generation-of-soc-analysts/ | 2026-09-25 (page metadata) | full |
| ARCTICWOLF-STRETCHED-2026 | Your Security Team Is Stretched Thin. Can AI Return the Hours? | Arctic Wolf | Vendor blog on vendor survey | https://arcticwolf.com/resources/blog/your-security-team-is-stretched-thin-can-ai-return-the-hours/ | 2026-09-17 (page metadata) | full |
| RELIAQUEST-2026 | ReliaQuest blog landing page | ReliaQuest | Vendor site | https://reliaquest.com/blog/ | checked 2026-10-17 | partial (headline only) |
| SPLUNK-RSACSOC-2026 | Lessons from the 10th RSAC SOC | Cisco/Splunk | Vendor blog | https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html | 2026-03 (per landscape) | full |
| CISCO-SPLUNK-CONF26-2026 | Splunk .conf26 live agentic SOC | Cisco | Vendor blog | https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/ | 2026-10-08 | full |
| FIGMA-AGENTS-2026 | How we secure Figma's internal systems with agents | Figma | In-house case study | https://www.figma.com/blog/how-we-secure-figmas-internal-systems-with-agents/ | 2026-07-29 | full |
| DETENGWEEKLY-2026 | Detection Engineering Weekly archive (issues #151, #154, #166) | Zack Allen | Practitioner newsletter | https://www.detectionengineering.net/archive | 2026-04-08; 2026-04-29; 2026-08-05 | full for #151 and #166; titles only for others |
| DEW-151 | DEW #151: The Security Cognitive Rust Belt | Detection Engineering Weekly | Practitioner newsletter | https://www.detectionengineering.net/p/dew-151-the-security-cognitive-rust | 2026-04-08 | full |
| ANTHROPIC-JOBS-2026 | Anthropic security job postings (Greenhouse API): 5443871008, 5448539008, 4982193008 | Anthropic | Job postings (author-side) | https://job-boards.greenhouse.io/anthropic/jobs/5443871008 | 2026-08-21 to 2026-10-09 | full |
| JOBS-ENTERPRISE-2026 | Postings: Cloudflare AI Security Research & Red Team Engineer (8097321); Datadog Senior Product Security Engineer - AI Agents (7993198); Robinhood Staff SWE AI Security (8214383); SentinelOne Staff Security Researcher, Detection AI (8003129003) | Cloudflare, Datadog, Robinhood, SentinelOne | Job postings | https://boards.greenhouse.io/cloudflare/jobs/8097321 | 2026-09-30 to 2026-10-13 | partial (opening text of each) |
| JOBS-HUNTRESS-2026 | Huntress Security Operations Analyst (Australia) posting 7998473003 | Huntress | Job posting (MDR provider) | https://job-boards.greenhouse.io/huntress/jobs/7998473003 | 2026-10-09 | full |
| COMPTIA-SECAI-2026 | SecAI+ Certification V1 | CompTIA | Certification page | https://www.comptia.org/en-us/certifications/secai/ | launch 2026-02-17 | full |
| GIAC-CERTS-2026 | GIAC certifications catalog | GIAC (SANS) | Certification page | https://www.giac.org/certifications/ | checked 2026-10-17 | full |
| ASU-STUDENTSOC-2026 | Junior Student SOC Analyst Program | Arizona State University | University program page | https://getprotected.asu.edu/communities/student-soc | undated (checked 2026-10-17) | full |
| CSO-NETSCOUT-2026 | The 10-hour problem: How visibility gaps are burning out the SOC | CSO Online (NETSCOUT brand post) | Sponsored post citing commissioned study | https://www.csoonline.com/article/4140738/the-10-hour-problem-how-visibility-gaps-are-burning-out-the-soc.html | 2026-03-04 | full |
| ARXIV-2610.10608 | From Investigation Failures to Reliable SOC Agents (ALERT-BENCH, AIDA) | arXiv preprint | Academic | https://arxiv.org/abs/2610.10608 | 2026-10-07 | abstract only |
| ARXIV-2605.24421 | Poisoning the Watchtower: Prompt Injection Against LLM-Augmented SOCs | arXiv preprint | Academic | https://arxiv.org/abs/2605.24421 | 2026-05-23 | abstract only |
| ARXIV-2505.06394 | Towards AI-Driven Human-Machine Co-Teaming for Adaptive and Agile Cyber SOCs | arXiv preprint | Academic | https://arxiv.org/abs/2505.06394 | 2025-05-09 | abstract only (vision paper; not cited in findings) |
| ARXIV-2503.02065 | Too Much to Trust? Measuring the Security and Cognitive Impacts of Explainability in AI-Driven SOCs | arXiv / ACM CCS 2025 | Academic | https://arxiv.org/abs/2503.02065 | 2025-03-03 (v2 2025-07-20) | abstract only |
| ARXIV-2602.18172 | Can AI Lower the Barrier to Cybersecurity? Novice CTF Learning | arXiv preprint | Academic | https://arxiv.org/abs/2602.18172 | 2026-02-20 | abstract only |
| NDSS-2026 | Decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering | NDSS Symposium | Academic | https://www.ndss-symposium.org/ndss-paper/decompiling-the-synergy-an-empirical-study-of-human-llm-teaming-in-software-reverse-engineering/ | NDSS 2026 (23-27 Feb 2026) | abstract only |

Source types read: professional bodies (ISC2, ISACA, SANS/GIAC, CompTIA), government and standard-setters (NIST NICE, UK DSIT), international body (WEF), academic (Stanford, arXiv, NDSS), vendors and providers (D3, Fortinet, Expel, Arctic Wolf, Cisco/Splunk, ReliaQuest, Huntress), in-house practice (Figma, Anthropic), job postings, practitioner newsletter (Detection Engineering Weekly), conference slides (RSAC), trade press and analyst forecast (SecurityMEA/Gartner). Distinct sources: 40 refs (ARXIV-2505.06394 and the ReliaQuest headline are read but only lightly used).

---

## 6. Gaps

- **No direct measurement of AI's effect on security entry-level hiring.** Evidence is survey perception (SANS/GIAC 32%), a vendor's one-month posting sample (D3), and economy-wide payroll data (Stanford) with no security-specific estimate. A security-specific series (for example CyberSeek, Lightcast or ADP by occupation) was not retrieved. CyberSeek's page returned no usable figures through curl.
- **SANS/GIAC 2026 Workforce Report body not retrieved** (404 on the landing URL; slides only), so sample size, definitions and the internally inconsistent figures on slides 10 and 12 are unresolved. SANS 2026 SOC Report body is gated, and its publication month is not shown.
- **ISACA 2026 full report is gated.** The 49% versus 61% open-position discrepancy between the press release and the newsletter is unresolved. Entry-level hiring figures for 2026 were not in the press materials.
- **Gartner primary documents not read.** The 2025 entry-level forecast and the 2026 MDR guide are known only through a trade outlet and an Expel blog respectively. A search-snippet claim that Gartner predicted GenAI would remove the need for specialized education in half of entry-level positions by 2028 was seen only in a search summary and is not used.
- **A claim in D3's report that ISC2's 2024 study found 31% of organizations have no entry-level security staff** could not be verified in the ISC2 2024 text I read, so it is not used.
- **Provider staffing economics are missing:** no published analyst-to-customer ratios, headcount changes, pricing moves or margins for agentic MDR; Big Four and consultancy staffing models were not reached.
- **Burnout and AI:** no independent before-and-after study on analyst burnout or attrition after AI triage. Burnout figures are survey self-reports from ISC2 and ISACA, and the NETSCOUT figure is vendor-commissioned.
- **Detection engineer as a role:** no workforce-size or career-path study found; evidence is postings, a vendor analysis and practitioner newsletters. Detection Engineering Weekly issues were read for two issues only.
- **Apprenticeship data:** only ISC2's 3% internship/apprenticeship share and one university program page. The UK apprenticeship posting surfaced by search had expired and was not used; claims about a Pentagon cyber apprenticeship were unconfirmed and are not used.
- **Not accessed:** BLS occupational outlook (403), CompTIA State of Cybersecurity, WEF Future of Jobs 2025, ISC2 full PDFs, Microsoft and Big Four pages, Reddit and LinkedIn discourse.
- **Non-US/UK/EU labour markets** (APAC, Middle East, Africa) appear only through WEF regional charts; none were analysed.
- **Anthropic is the author of two sources here** (`ANTHROPIC-SKILLS-2026`, `ANTHROPIC-JOBS-2026`); they are used as author-side evidence only.
