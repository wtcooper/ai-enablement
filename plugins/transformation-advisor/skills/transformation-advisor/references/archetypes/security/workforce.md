# Security workforce

Last researched 2026-10-17. Use this when roles, capacity, hiring, skills or fear for jobs come up, and in Plan when
choosing between capacity and cost. Pair it with [people-and-change.md](../../method/people-and-change.md). Module
§7 sections cover role change step by step. Source keys in brackets resolve in §10 or in [sources.md](sources.md).

## Contents

1. [Headlines](#1-headlines)
2. [The gap studies and what each measures](#2-the-gap-studies-and-what-each-measures)
3. [Roles and how they evolve](#3-roles-and-how-they-evolve)
4. [The talent model and pyramid](#4-the-talent-model-and-pyramid)
5. [Skills and certifications](#5-skills-and-certifications)
6. [The apprenticeship question](#6-the-apprenticeship-question)
7. [Burnout and retention](#7-burnout-and-retention)
8. [How providers staff services](#8-how-providers-staff-services)
9. [Questions to ask](#9-questions-to-ask)
10. [Sources](#10-sources)

## 1. Headlines

- **"The gap" is no longer one number.** ISC2 stopped publishing a gap estimate in 2025 because respondents put skills
  ahead of headcount [ISC2-WORKFORCE-2025]; its last figure was 4,763,963 for 2024 [ISC2-WORKFORCE-2024].
- **Skills, more than headcount, are now the focus** of ISC2, SANS/GIAC and WEF, each measured differently; the UK
  government study measures both and finds the UK gap stable at about 3,800 [DSIT-CYBERSKILLS-2025].
- **Hiring demand shifts to engineers and senior staff.** In one vendor's sample of 665 US postings, entry-level roles
  were 5.9% and engineering roles outnumbered SOC analyst roles about three to one [D3-SOCREBUILD-2026].
- **The entry-level evidence is thin and indirect.** 32% of organizations say AI has reduced SOC and analyst
  entry-level roles; 39% report no reductions yet [RSAC-WORKFORCE-2026].
- **No source measures security headcount cuts caused by AI** beyond the self-reports above; 69% of CISOs do not
  expect AI to reduce existing headcount (expectation) [IANS-BUDGET-2026].

## 2. The gap studies and what each measures

| Study | Sample and method | What it says | Source |
|---|---|---|---|
| ISC2 Workforce Study 2025 | 16,029 people responsible for security; online, Jul-Aug 2025; 5% of respondents entry or junior level | No gap estimate; 88% report a significant consequence of skills deficits; budget cuts 36%, hiring freezes 39%, layoffs 24% | [ISC2-WORKFORCE-2025] |
| ISC2 2024 | Same method | Gap 4,763,963, up 19.1%; ISC2 says the gap is not job openings | [ISC2-WORKFORCE-2024] |
| ISACA State of Cybersecurity 2026 | More than 1,800 professionals, global | 58% understaffed (55% in 2025); 55% struggle to retain staff; 49% have open positions | [ISACA-SOC-2026] |
| SANS/GIAC Workforce Report 2026 | Slides only; sample not shown | 60% see the problem as skills, 40% headcount (52% skills a year earlier) | [RSAC-WORKFORCE-2026] |
| WEF Global Cybersecurity Outlook 2026 | 804 participants, 92 countries | 85% of organizations with insufficient resilience lack critical people and skills, against 22% of highly resilient ones; top shortages: threat intelligence analysts, DevSecOps engineers, IAM specialists | [WEF-GCO-2026] |
| UK DSIT labour market study | Surveys plus postings data, calendar 2024 | UK gap about 3,800; core cyber postings down 33% | [DSIT-CYBERSKILLS-2025] |
| Fortinet skills report (vendor-commissioned) | 2,750 IT and security decision-makers | 51% need senior skills most, 13% entry-level; 60% say AI experience is the hardest to recruit | [FORTINET-SKILLS-2026] |

## 3. Roles and how they evolve

| Role | How it is changing | Evidence |
|---|---|---|
| Tier-1 SOC analyst | From assembling context to reviewing agent-prepared findings; the classic zero-experience seat survives mainly at MSSPs, MDR firms and state government | [CISCO-SPLUNK-CONF26-2026; D3-SOCREBUILD-2026]; operations §7 |
| On-call engineer in an in-house team | From investigating from scratch to reviewing and correcting an agent's findings (Figma, self-reported) | [FIGMA-AGENTS-2026] |
| Detection engineer | Writes guides that agents follow, reviews generated rules; detections-as-code in 46% of plain SOC analyst postings | [D3-SOCREBUILD-2026]; operations §7 |
| Threat intelligence analyst | One of WEF's top three shortage roles; work moves from aggregation and first drafts to interpretation and validation | [WEF-GCO-2026]; threat-intelligence §7 |
| AppSec and product security engineer | Reviewing AI-written code and AI findings; finding got cheap, verifying and closing did not | application-security §1, §7 |
| GRC analyst | Reviewing AI-drafted questionnaires, assessments and evidence; AI governance work for the business | governance-risk §7 |
| AI security engineer (new) | 32% of organizations creating the role; 25 of 665 postings, a title absent 18 months earlier (vendor sample) | [RSAC-WORKFORCE-2026; D3-SOCREBUILD-2026] |
| AI governance analyst (new) | 30% of organizations creating the role | [RSAC-WORKFORCE-2026] |
| Owner of an agent | Named accountability for what an agent does (implied by NCSC advice) | operations §7; ai-security §7 |
| CISO | Answers for AI risk across the business, often without matching budget | governance-risk §2; [IANS-BUDGET-2026] |

Gartner (as relayed by a vendor) forecasts SOC teams with 50% more engineers than analysts by 2028, KPIs moving from
alert volume to case accuracy and decision confidence, and says "The SOC will not shrink by 2030"
[PROPHET-GARTNERROLES-2026].

## 4. The talent model and pyramid

- **In-house SOCs** traditionally run a tiered queue (tier 1 triage, tiers 2-3 investigation) with detection engineers
  beside it; continuous coverage needs more than four people per seat (arithmetic in [economics.md](economics.md) §5).
- **The pyramid narrows at the base.** Postings show engineering roles about three per analyst role; median advertised
  pay USD 125k for SOC analysts, 142k for SecOps engineers, 152k automation engineers, 161k detection engineers (US,
  one month, vendor analysis) [D3-SOCREBUILD-2026].
- **Respondents are mostly established.** Only 5% of ISC2's 2025 respondents were entry or junior level, so the AI
  optimism in surveys comes mostly from people already in the field [ISC2-WORKFORCE-2025].
- **Routes in:** IT is the main route (56%); internships or apprenticeships brought in 3%, who were the most likely to
  recommend their route [ISC2-WORKFORCE-2025]. In 2025, 46% of ISACA respondents said over half their staff came from
  outside the field [ISACA-SOC-2025].
- **Sourcing:** to offset shortages, 25% turn to AI and automation, 20% outsource, 19% use third-party providers
  [ISC2-WORKFORCE-2025]; 35% of ISACA respondents raise reliance on AI or automation for technical gaps [ISACA-SOC-2026].

## 5. Skills and certifications

- **AI is the top skills need:** 41% (ISC2), ahead of cloud security at 36% [ISC2-WORKFORCE-2025]; ISACA's largest
  rising gap is LLM security operations at 45% (up 12 points); soft skills 57% [ISACA-SOC-2026].
- **Hiring managers' top skills are non-technical:** problem solving 29%, collaboration 24%, communication 22%
  [ISC2-WORKFORCE-2025].
- **AI credentials assume experience.** CompTIA SecAI+ (launched 2026-02-17) recommends 2+ years hands-on security
  [COMPTIA-SECAI-2026]; ISACA's AAISM requires an active CISM or CISSP [ISACA-AAISM]; GIAC lists 12 AI-category
  certifications [GIAC-CERTS-2026]. That sits awkwardly with a shrinking entry seat (an inference, not a source claim).
- **Frameworks:** NIST's NICE said in 2025 it is adding an AI security competency area and AI tasks to work roles
  [NIST-NICE-AIBLOG-2025].

## 6. The apprenticeship question

If agents take the tier-1 queue, where do juniors learn what a bad alert looks like in raw telemetry?

**Evidence that the base is shrinking (mixed, mostly indirect)**
- 32% report AI-driven reductions in entry-level SOC and analyst roles; 39% none yet [RSAC-WORKFORCE-2026].
- Entry-level postings 5.9% in one vendor's one-month US sample [D3-SOCREBUILD-2026].
- Gartner analysts (via trade press) say AI may sharply reduce entry-level SOC roles and forecast one-third of senior
  security operations roles vacant for over a year by 2028 [GARTNER-SOC-2025].
- Economy-wide, not security-specific: employment of 22-25-year-olds in AI-exposed occupations is 19% below trend;
  the authors call it descriptive [STANFORD-CANARIES-2026].

**Evidence on learning with AI (adjacent, not security triage)**
- An Anthropic randomised trial (author-side): developers using AI scored 50% on a mastery quiz against 67% coding by
  hand [ANTHROPIC-SKILLS-2026].
- A reverse-engineering study: LLM help raised novices' comprehension by about 98% while experts gained little [NDSS-2026].

**What practitioners and providers do (self-described)**
- Arctic Wolf says it keeps new analysts close to decisions that need interpretation and has agents escalate when
  confidence is low [ARCTICWOLF-ANALYSTS-2026].
- Arizona State University runs a paid year-long student SOC programme in its live SOC, including an "AI in the SOC"
  month; six students in the first cohort [ASU-STUDENTSOC-2026].
- Gartner recommends faster junior-to-senior progression and manual verification built into training [GARTNER-SOC-2025].
- A practitioner newsletter asks what is lost when analysts live in summaries instead of raw telemetry [DEW-151].

**Design options to raise with a leader** (ideas, not tested): rotate juniors through sampled AI closures as graded
practice; keep manual investigation drills; have juniors write and test agent guides; track time-to-competence.

## 7. Burnout and retention

- 47% often feel overwhelmed by workload; 48% exhausted by keeping up [ISC2-WORKFORCE-2025].
- 68% say their role is more stressful than five years ago; high stress is the top reason for leaving (52%)
  [ISACA-SOC-2026].
- Meaningful work and career progression have outranked pay as retention drivers for three years [SANS-SOC-2026].
- No independent study links AI triage to lower burnout or attrition.

## 8. How providers staff services

- Gartner's 2026 MDR guide (quoted by a vendor) defines MDR as "AI-augmented, human-led" with 24/7 staffing and tells
  buyers to ask which services are AI-augmented versus analyst-delivered [EXPEL-GARTNERMDR-2026].
- A Huntress SOC analyst posting asks for 2+ years of SOC, IR or MDR experience and use of AI with output validation
  [JOBS-HUNTRESS-2026].
- Arctic Wolf says senior analysts spend more time on advanced investigations and codify techniques into the system
  [ARCTICWOLF-ANALYSTS-2026].
- An AI SOC vendor asserts provider analyst tenure under 18 months and turnover above 30% (claim) [D3-AGENTICMDR-2026].
- Not found: provider headcount, analyst-to-customer ratios or staffing changes from agentic MDR.

## 9. Questions to ask

1. Which three roles changed in the last year (tasks, title, pay), and which were redefined rather than newly hired?
2. Who reviews what the agents closed, and is that review part of someone's job description?
3. How will an analyst hired this year learn to read raw telemetry?
4. Who writes and maintains the guides and playbooks your agents follow?
5. (Providers) Which parts of your service would you call AI-delivered and which analyst-delivered, and what happens to
   your bench ratio in 24 months?

## 10. Sources

Keys not listed here are in [sources.md](sources.md).

- **ASU-STUDENTSOC-2026**: Arizona State University, *Junior Student SOC Analyst Program* (university programme page, undated; checked 2026-10-17). https://getprotected.asu.edu/communities/student-soc
- **DEW-151**: Detection Engineering Weekly (Zack Allen), *DEW #151: The Security Cognitive Rust Belt* (practitioner newsletter, 2026-04-08). https://www.detectionengineering.net/p/dew-151-the-security-cognitive-rust
- **FORTINET-SKILLS-2026**: Fortinet (Sapio Research fieldwork), *2026 Cybersecurity Skills Gap Global Research Report* (vendor-commissioned survey, 2026). https://www.fortinet.com/content/dam/fortinet/assets/reports/2026-cybersecurity-skills-gap-report.pdf
- **GIAC-CERTS-2026**: GIAC (SANS), *Certifications catalog* (certification body, checked 2026-10-17). https://www.giac.org/certifications/
- **ISACA-SOC-2025**: ISACA, *State of Cybersecurity 2025 global press release* (professional-body survey, 2025-09). https://www.isaca.org/about-us/newsroom/press-releases/2025/state-of-cybersecurity-2025-global-press-release
- **NIST-NICE-AIBLOG-2025**: NIST NICE, *The Impact of Artificial Intelligence on the Cybersecurity Workforce* (standard-setter blog, 2025-06-12). https://www.nist.gov/blogs/cybersecurity-insights/impact-artificial-intelligence-cybersecurity-workforce
- **STANFORD-CANARIES-2026**: Stanford Digital Economy Lab (Brynjolfsson, Chandar, Chen), *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI (Aug 2026 version)* (academic, 2026-08). https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf
- **WEF-GCO-2026**: World Economic Forum with Accenture, *Global Cybersecurity Outlook 2026* (international survey of 804, 2026-01-12). https://reports.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2026.pdf
