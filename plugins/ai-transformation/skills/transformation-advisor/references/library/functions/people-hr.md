# People (HR)

Function id `people-hr`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:** HR has one
well-measured automation story (IBM's employee assistant) and one strong controlled trial (AI voice interviews with humans deciding),
and more regulatory and litigation exposure than any other function card. Screening and ranking people is where HR AI goes wrong in
public. No source reports error, override or reopen rates for an employee-facing HR assistant.

## Contents

1. [What this function covers](#1-what-this-function-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Metrics and benchmarks](#4-metrics-and-benchmarks)
5. [Interview probes](#5-interview-probes)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Sources](#8-sources)

## 1. What this function covers

The in-house people function of any organization: HR planning and policy, recruiting and selection, onboarding and development,
employee relations, reward, moves and exits, and employee inquiries and data. A professional-services firm's own talent and junior
pipeline is in the professional-services `talent-learning` module. No archetype covers firms that sell recruiting or HR outsourcing;
use this card.

## 2. Processes and key steps

The process list is a working grouping under the "develop and manage human capital" category of a cross-industry process framework
[APQC-PCF-2026].

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| HR planning, policy and strategy | Align staffing to workforce plan; set policies; define competencies and roles | expert-judgment, data-reporting, document-production | Compliance work grew with new laws while budgets shrank (IBM) [IBM-THINK-2025] |
| Recruit, source and select | Requisitions; source; screen and select; offers and hires; applicant records | transaction-processing, coordination-scheduling, client-interaction, expert-judgment | High volume: 12 days from application to start at Chipotle before its assistant (company statement) [NRN-CHIPOTLE-2025]; interview quality varies between recruiters [CHICAGO-JABARIAN-2026] |
| Onboarding, development, training | Onboard; learning; performance; careers and skills | document-production, client-interaction, expert-judgment | Unused talent data: AdventHealth's databases held talent for over 80% of requisitions it could not find (vendor-published) [WORKDAY-ADVENTHEALTH-2025] |
| Employee relations | Cases on conduct, grievances, policy exceptions; records | expert-judgment, review-assurance | No public AI evidence found |
| Reward and retain | Pay, benefits, recognition; retention | transaction-processing, data-reporting, expert-judgment | No measured case found |
| Redeploy and retire | Transfers, promotions, separations | transaction-processing, coordination-scheduling | No measured case found |
| Employee inquiries and data | Answer inquiries; maintain data and systems; time and attendance; surveys | client-interaction, transaction-processing, data-reporting | Repetitive questions and transactions under regional policy differences (IBM) [IBM-ASKHR-2025] |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **Structured interview scoring as one input, with every candidate still reviewed** ([intake-triage](../patterns/intake-triage.md);
  augment; step). Treasury Board Secretariat, Government of Canada (public sector): proposed pilot of a scored structured behavioural
  interview; TBS intends to review all candidates regardless of score; candidates can opt for an in-person assessment; planned tests of accuracy
  against human raters and score differences across groups. No outcome published. Grade B [TBS-AIA-2024].
- **Rediscover past applicants for new requisitions** ([intake-triage](../patterns/intake-triage.md); augment; process). AdventHealth
  (healthcare): 77% of nursing requisitions covered by past applicants; offer rate 50% higher for rediscovered candidates. Vendor
  page with an executive quote; baselines not defined. Grade B [WORKDAY-ADVENTHEALTH-2025].

**Automate the flow**

- **Employee HR assistant that answers from policy and completes transactions, routing the rest to HR partners**
  ([service-agent-escalation](../patterns/service-agent-escalation.md),
  [grounded-knowledge-assistant](../patterns/grounded-knowledge-assistant.md); automate; process). IBM (technology): in 2024, more
  than 11.5 million interactions, 94% contained in the platform (6% routed to an HR partner); about 90 automations; managers complete
  HR transactions 75% faster; net promoter score fell to -35 after IBM shut HR phone and email for all employees and HR partner support for
  21,000 first-line managers in 2018, and is +74 now. Self-reported. Grade A [IBM-THINK-2025; IBM-ASKHR-2025]. Bosch (manufacturing and technology): an HR assistant that points
  associates to specific policies, rolled out to most Bosch countries, no figures. Grade B [BOSCH-PT-2024].
- **Candidate assistant that answers questions, collects basics, schedules interviews and sends offers**
  ([service-agent-escalation](../patterns/service-agent-escalation.md); automate; step to process). Chipotle (restaurants): application
  to start from 12 days to four; applications nearly doubled; completion from about 50% to over 85%. Company statements via press and a
  vendor page. Grade B [NRN-CHIPOTLE-2025; WORKDAY-CHIPOTLE-2026].
- **AI voice interviewer collects structured information; recruiters evaluate and decide** (pattern `other`: information collection
  by an agent; automate; step). PSG Global Solutions (recruitment process outsourcing, a Teleperformance subsidiary, hiring in the Philippines): about
  70,000 applicants randomized to
  AI or human interviewers; offers 12% higher with AI, job starts and one-month retention about 18% higher; no significant difference in
  hires' customer-handling time, satisfaction or quality scores; 78% chose the AI when offered a choice, and those who did scored lower
  on language and analytical tests. Academic study; the partner supplied data only, and the lead author later took an unpaid
  chief-economist role there. Grade A [CHICAGO-JABARIAN-2026].

**Delegate the outcome**

- No measured public example of an agent owning an HR outcome was found. IBM describes moving its assistant to agents in 2025, with no
  figures [IBM-ASKHR-2025].

**Reinvent the work**

- **Simplify the policy set before automating it** (process). IBM's "eliminate, simplify, automate" rule consolidated over 25 leave
  types into one [IBM-THINK-2025].
- **Plan work, people and technology together** (model). Moderna (biotechnology) combined HR and digital technology under one chief
  officer to plan "work" rather than workforce or technology separately; no outcome published. Grade B [UNLEASH-MODERNA-2025].

**In the archetypes**: `professional-services-talent-learning-11` (A, juniors' expertise tested without AI after AI use),
`professional-services-talent-learning-16` (A), `professional-services-talent-learning-14` (B, AI-led graduate screening under
audit, notice and human-review rules), `professional-services-talent-learning-07` (B), `professional-services-talent-learning-15` (B),
`professional-services-talent-learning-22` (B), `assurance-quality-management-10` (B), `security-human-risk-12` (B, verifying remote
candidates' identity).

## 4. Metrics and benchmarks

- **Cost to recruit:** personnel cost of the recruit, source and select process group, median $1,879 per new hire across 1,251
  companies (benchmarking-body data) [APQC-PCF-2026].
- **Containment:** share of employee interactions contained and not routed to a person, 94% at IBM; IBM pages define it differently,
  so use the "contained, not routed" wording [IBM-THINK-2025; IBM-ASKHR-2025].
- **Employee satisfaction:** net promoter score before and after cutover (-35 to +74, IBM, self-reported) [IBM-THINK-2025].
- **Hiring quality, not only speed:** offers, job starts, retention at 30 to 120 days, and hires' handling time, satisfaction and
  quality scores [CHICAGO-JABARIAN-2026].
- **Fairness:** selection-rate comparisons across groups on identical inputs [UW-WILSON-2024]; accuracy against human raters and score
  differences by group (planned in Canada's pilot) [TBS-AIA-2024].
- **Adoption against value:** a Gartner survey of 110 heads of HR found 95% had implemented AI in some capacity and only one in
  five had realized significant or transformational value [GARTNER-HR-2026].

## 5. Interview probes

1. "Of the HR questions you get in a month, what share are lookups, what share transactions, and what share need judgment?" Reveals
   the containable share and whether anyone has counted; IBM's containment rests on automations, not only answers [IBM-THINK-2025].
2. "Which policies would you delete or merge before you automate anything?" Reveals whether the process owner can simplify
   [IBM-THINK-2025].
3. "When the assistant cannot answer, who picks it up, how fast, and how do you know the employee was not just frustrated?" Reveals
   the exit design; Oracle's IT desk turns "I still need help" into a ticket for a support engineer [IBM-THINK-2025;
   ORACLE-AISD-2025].
4. "Where in hiring does a person decide, and what does that person see?" Reveals whether AI filters candidates out unseen
   [CHICAGO-JABARIAN-2026; TBS-AIA-2024].
5. "Show me selection rates by group for last quarter, and who audited them." Reveals whether fairness is measured or assumed
   [NYC-DCWP-AEDT-2023; ICO-RECRUIT-2024; UW-WILSON-2024].
6. "What does a good hire look like 90 days later, and have you checked the faster process keeps it?" Reveals whether speed is bought
   at the cost of fit [CHICAGO-JABARIAN-2026; NRN-CHIPOTLE-2025].
7. "Which of your HR tools score, rank or filter people, where do those people live, and who owns the inventory?" Reveals shadow tools
   and vendor features turned on by default [EU-AIACT-ANNEX3-2024; HRDIVE-MOBLEY-2025].
8. "If HR gets time back, where does it go, and who decided?" Reveals whether capacity has a destination
   [GARTNER-HR-2026; IBM-THINK-2025].
9. "Who owns the content the assistant answers from, and how often is it checked against current law and policy?" Reveals the
   no-owner failure mode; a city's business chatbot gave wrong legal answers [MARKUP-NYCBOT-2024].

## 6. Guardrails

- **High-risk uses in the EU.** Annex III covers AI for recruitment or selection (targeting job ads, filtering applications,
  evaluating candidates) and for decisions on terms of work, promotion, termination, task allocation and monitoring
  [EU-AIACT-ANNEX3-2024]. A 2026-07-01 law-firm briefing says the AI Omnibus moves the deadline for these systems to 2 December 2027,
  pending publication in the Official Journal; confirm the date before advising [AG-OMNIBUS-2026].
- **Prohibited:** AI that infers emotions of a person in the workplace, with defined exceptions [EU-AIACT-ART5-2024].
- **Worker notice:** employers deploying a high-risk system at work must inform workers' representatives and affected workers first
  [EU-AIACT-ART26-2024].
- **New York City:** an automated employment decision tool needs a bias audit within the prior year, a public summary and candidate
  notices (enforced from 2023-07-05) [NYC-DCWP-AEDT-2023].
- **Audit any screening or ranking.** An audit study found white-associated names preferred in 85.1% of language-model resume-retrieval
  comparisons (race results replicated; the gender-only results were later corrected, so do not cite them) [UW-WILSON-2024]. The UK
  regulator found tools filtering by protected characteristics and inferring gender and ethnicity from names [ICO-RECRUIT-2024]. A US
  court preliminarily certified an age-discrimination collective action over an applicant-ranking product; the vendor says the case
  is without merit and merits are unresolved [HRDIVE-MOBLEY-2025; CLEARINGHOUSE-MOBLEY-2026].
- **Frameworks:** NIST AI RMF (govern, map, measure, manage) and its generative AI profile, which lists confabulation, harmful bias and
  data privacy among the risks [NIST-AIRMF-2023; NIST-AI600-1-2024].
- **Decisions that need human judgment:** hire or no-hire; promotion, discipline and termination; pay changes; accommodation requests
  and alternatives to automated assessment; investigations; policy exceptions; distressed or sensitive cases [TBS-AIA-2024;
  BOSCH-PT-2024].

## 7. Roles and how they evolve

- **HR partners handle the complex remainder:** 6% of IBM's 2024 interactions went to a specialized partner [IBM-THINK-2025].
- **Recruiters move from running first-round interviews to evaluating them** [CHICAGO-JABARIAN-2026].
- **HR and IT leadership can merge** around "work planning" (Moderna) [UNLEASH-MODERNA-2025].
- **Entry-level pipeline:** 22% of CHROs said at least one business leader had stopped hiring for entry-level roles because of AI
  automation [GARTNER-HR-2026]; the professional-services archetype holds the evidence on junior development.
- **Some pilots leave roles unchanged by design:** Canada's pilot states it is not designed to change HR staff roles [TBS-AIA-2024].

## 8. Sources

- **AG-OMNIBUS-2026**: Addleshaw Goddard, *EU AI Act: AI Omnibus formally adopted* (law firm briefing, 2026-07-01). https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/
- **APQC-PCF-2026**: APQC, *Process Classification Framework v8.0* and measure page on recruiting personnel cost (professional body, 2026-03). https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/personnel-cost-perform-process-group-7
- **BOSCH-PT-2024**: Personnel Today (written by Bosch UK), *Bosch UK: this is how our HR teams are using AI* (press, 2024-12-19). https://www.personneltoday.com/?p=329503
- **CHICAGO-JABARIAN-2026**: Jabarian, Henkel, *Voice AI in Firms: A Natural Field Experiment on Automated Job Interviews* (academic, arXiv 2607.28222 v2, 2026-09-11). https://arxiv.org/pdf/2607.28222
- **CLEARINGHOUSE-MOBLEY-2026**: Civil Rights Litigation Clearinghouse, *Mobley v. Workday, Inc.* case page (academic, 2026-09-17). https://clearinghouse.net/case/44074/
- **EU-AIACT-ANNEX3-2024**: Regulation (EU) 2024/1689, *Annex III: High-risk AI systems* (regulation text, 2024). https://artificialintelligenceact.eu/annex/3/
- **EU-AIACT-ART26-2024**: Regulation (EU) 2024/1689, *Article 26: Obligations of deployers of high-risk AI systems* (regulation text, 2024). https://artificialintelligenceact.eu/article/26/
- **EU-AIACT-ART5-2024**: Regulation (EU) 2024/1689, *Article 5: Prohibited AI practices* (regulation text, 2024). https://artificialintelligenceact.eu/article/5/
- **GARTNER-HR-2026**: Gartner, *Gartner Survey Finds AI Automation Is Reducing Some Entry Level Hiring at Nearly One-Quarter of Organizations* (survey release, n=110, 2026-07-27). https://www.gartner.com/en/newsroom/press-releases/2026-7-27-gartner-survey-finds-ai-automation-is-reducing-some-entry-level-hiring-at-nearly-one-quarter-of-organizations
- **HRDIVE-MOBLEY-2025**: HR Dive, *Judge allows Workday AI bias lawsuit to proceed as collective action* (press, 2025-05-19). https://www.hrdive.com/news/workday-ai-bias-lawsuit-class-collective-action/748518/
- **IBM-ASKHR-2025**: IBM, *IBM AskHR: Transforming HR support with agentic AI* (case study, 2025-08-21). https://www.ibm.com/case-studies/ibm-askhr
- **IBM-THINK-2025**: IBM (Nickle LaMoreaux, CHRO), *Embracing the future of HR by becoming an AI-first enterprise* (firm, 2025-04-29). https://www.ibm.com/think/insights/embracing-future-of-hr-ai-first-enterprise
- **ICO-RECRUIT-2024**: UK Information Commissioner's Office, *ICO intervention into AI recruitment tools leads to better data protection for job seekers* (regulator, 2024-11-06). https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/ico-intervention-into-ai-recruitment-tools-leads-to-better-data-protection-for-job-seekers/
- **MARKUP-NYCBOT-2024**: The Markup, *NYC's AI Chatbot Tells Businesses to Break the Law* (press, 2024-03-29). https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law
- **NIST-AIRMF-2023**: NIST, *AI Risk Management Framework 1.0* (standard-setter, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **NIST-AI600-1-2024**: NIST, *AI RMF: Generative AI Profile* (standard-setter, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **NRN-CHIPOTLE-2025**: Nation's Restaurant News, *Chipotle is going on a hiring spree with the help of AI* (press, 2025-02-19). https://www.nrn.com/fast-casual/chipotle-is-going-on-a-hiring-spree-with-the-help-of-ai
- **NYC-DCWP-AEDT-2023**: NYC Department of Consumer and Worker Protection, *Automated Employment Decision Tools* (regulator, 2023-07). https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
- **ORACLE-AISD-2025**: Oracle, *Transforming IT support: Introducing the generative AI-powered service desk* (vendor blog, 2025-10, inferred from image paths). https://blogs.oracle.com/ai-and-datascience/post/transforming-it-support-gen-aipowered-service-desk
- **TBS-AIA-2024**: Treasury Board Secretariat of Canada, *Algorithmic Impact Assessment: using AI to automate candidate evaluations* (government, 2024-02-28). https://open.canada.ca/data/dataset/52b8574d-5c95-463b-b375-8edd092cea30/resource/f7a43e13-44f3-4d43-b588-97aedb17c3f8/download/algorithmic-impact-assessment-using-artificial-intelligence-ai-to-automate-candidate-evaluations.pdf
- **UNLEASH-MODERNA-2025**: UNLEASH, *Why Moderna merged HR and IT to better 'architect the flow of work'* (press, 2025-06-27). https://www.unleash.ai/artificial-intelligence/why-moderna-merged-hr-and-it-to-better-architect-the-flow-of-work/
- **UW-WILSON-2024**: Wilson, Caliskan, *Gender, Race, and Intersectional Bias in Resume Screening via Language Model Retrieval* (academic, arXiv 2407.20371 v3, 2026-08-30). https://arxiv.org/pdf/2407.20371
- **WORKDAY-ADVENTHEALTH-2025**: Workday, *AdventHealth Fills Hard-to-Fill Roles at Record Speed* (vendor customer story, 2025-01-31). https://www.workday.com/en-us/customer-stories/a-h/adventhealth-fills-hard-to-fill-roles-at-record-speed.html
- **WORKDAY-CHIPOTLE-2026**: Workday, *Chipotle Cuts Time to Hire by 75% With AI Platform* (vendor customer story, 2026-01-30). https://workday.com/en-us/customer-stories/a-h/chipotle-leverages-conversational-ai-scales-hiring.html
