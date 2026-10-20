# Function cards, commercial functions: sales-marketing-bd, customer-service, product-service-development

Stream B backbone library. Researched 2026-10-20. In-house functions in any organization; firms that sell these services as their product are covered by the archetypes.

Conventions used below:

- Grades follow the vocabulary (A = a figure the named organization reports as measured; B = named real deployment or study without a usable measured figure, or measured but the organization is unnamed or the process is adjacent; C = announcement or vendor claim; D = idea). Where a study is strong but the organization is anonymous, the grade is B and the note says so.
- Provenance is `self-reported`, `vendor-published` or `independent`. "Independent" is used only for tribunal, regulator, or academic measurement where the authors are not the deploying organization.
- Process lists and step-to-work-type tags are the advisor's own synthesis of how the work is organized, informed by the process frameworks named in the Sources (APQC top-level categories, Stage-Gate, Double Diamond). They are not claims about any named organization and carry no framework ids. Anything not tied to a source ref is marked "synthesis".
- Statistics state what they measure in the source's terms. Quotations are under 25 words.

---

## 1. Summary

- **Customer service has the strongest quality evidence of the three, and it is mixed.** Randomized or staggered-rollout studies of agent assistance show faster handling and better ratings, concentrated in newer or lower-rated agents (NBER-BRYNJOLFSSON-2023 abstract; NI-2026 abstract). The same studies show the most skilled agents gaining little or losing quality. Rollout should be tailored by skill, not uniform.
- **Objective quality often does not move even when speed and ratings do.** In the Alibaba trial, the rate of customers returning within three days with the same issue showed no significant change, while chat time and customer ratings improved (NI-2026 §1). Measure repeat contact, not only handle time.
- **Customer-facing automation works on routine questions and fails loudly at the edges.** Klarna (KLARNA-2024), Salesforce's own help site (SALESFORCE-2025) and GOV.UK Chat (GDS-2024, GOVTRANS-2026) report measured results. Air Canada (CRT-2024), Cursor (ARS-2025) and Klarna's 2025 reversal (MAGINATIVE-2025) show what happens when handoff, accuracy or customer preference is mis-judged. The CFPB (CFPB-2023) and Gartner (GARTNER-2024) document the "no way to reach a person" risk from the customer side.
- **Sales and marketing evidence is thinner and more self-reported.** The one randomized set is from an unnamed cross-border retail platform: sales effects from 0% to 16.3% by workflow, with no deterioration in returns or ratings (FANG-2026 abstract). Named in-house outbound results are self-reported (SAASTR-2025a) and come with 15-20 hours a week of human oversight. The best-known failure is a vendor's overstated customer claims (TECHCRUNCH-2025).
- **Product and service development is where AI changes who can do what, and where evidence is weakest on production outcomes.** A pre-registered field experiment at P&G found individuals with AI matched teams without it (NBER-DELLACQUA-2025 abstract), and a drug candidate discovered with generative AI has completed a randomized phase 2a trial (INSILICO-2025). The author of Stage-Gate states that most commonly cited benefits rest on opinion and single-case anecdotes (COOPER-2024 section "Evidence").
- **Synthetic respondents are promising on one retrospective test and discouraged by usability practitioners.** A Colgate-Palmolive data set shows 90% of human test-retest reliability for ranking concepts (MAIER-2025 abstract); NN/g found synthetic users gave shallow or over-favorable feedback (NNG-2024). Use for screening, not for the final decision.
- **Legal exposure is concrete in all three.** A company was held liable for what its website chatbot said (CRT-2024 paras 27-28); AI-generated voices count as "artificial" under US robocall law (FCC-24-17); the FTC treats AI claims and AI-written fake reviews as enforceable (FTC-AICOMPLY-2024; FTC-FAKEREVIEWS-2024); the EU AI Act requires people to be told they are dealing with an AI system (EU-AIACT-2024 Art 50(1)).
- **Role effects point three ways:** novice agents ramp faster and leave less (NBER-BRYNJOLFSSON-2023 §4, §6.3), service agents are being reskilled toward selling (REUTERS-2025), and AI-outbound programs shift human work to coaching and spot-checking (SAASTR-2025a).

---

## 2. Item profiles

### 2.1 sales-marketing-bd

**Main processes and key steps (synthesis; top-level category "Market and Sell" per APQC-2015).**

| Process | Key steps | Work types |
|---|---|---|
| Market and customer insight | Segment markets; research needs and competitors; set positioning | `research-synthesis`, `data-reporting` |
| Marketing planning and content | Plan campaigns; write copy, images, product descriptions; schedule and publish; measure | `document-production`, `coordination-scheduling`, `data-reporting` |
| Lead capture and management | Capture inbound interest; enrich and score; route to owner | `transaction-processing`, `data-reporting` |
| Prospecting and outreach | Choose accounts and contacts; research; personalize; send and follow up sequences | `research-synthesis`, `client-interaction`, `document-production` |
| Qualification and pursuit | Discovery calls; qualify; scope; quote or answer RFPs; negotiate; close | `client-interaction`, `expert-judgment`, `document-production` |
| Account management and growth | Account plans; renewals; cross-sell; relationship health | `client-interaction`, `coordination-scheduling` |
| Sales operations and forecasting | Keep CRM records complete; forecast; report pipeline | `data-reporting`, `transaction-processing` |
| Enablement | Customize decks and collateral; train sellers | `document-production` |

**Typical pain points.**

- Account and customer research before outreach is slow: Lumen's chief revenue officer is reported as saying it typically took a seller about four hours (MICROSOFT-2024, section on sellers). Company statement, not a measurement.
- Records are incomplete: SaaStr found opportunities had never been logged in its CRM and had to fix its revenue-operations process before agents could help (SAASTR-2025a, "Top 5 learnings", item 1).
- Online conversion is held back by search and information friction for buyers, especially across languages (FANG-2026 §1, findings).
- Outbound volume per human is low compared with what an agent can send: SaaStr reports 3,000 emails a month from its agent against 75-285 a month from its previous human reps (SAASTR-2025a, "Core performance metrics"). Self-reported.
- Buyer claims about tools can be inflated by vendors; a prospective customer's one-month trial found the product "significantly worse" than its own SDR employees (TECHCRUNCH-2025, ZoomInfo section; quoting that organization's spokesperson).

**Top AI opportunities (ladder x change scope), with graded evidence.**

| # | Opportunity | Ladder | Scope | Best evidence (grade) |
|---|---|---|---|---|
| S1 | Account research and pre-meeting prep | assist to augment | step | Lumen, company estimate of seller time saved (B, MICROSOFT-2024); archetype entry (below) |
| S2 | Call and email capture into the CRM, with next steps and contacts created automatically | automate | step | SaaStr describes it, no measure (B, SAASTR-2025b item 5); archetype entry |
| S3 | Personalized outbound sequences run by a background agent, with human spot checks | automate | process | SaaStr tracked metrics (A, SAASTR-2025a); counter-evidence in TECHCRUNCH-2025 |
| S4 | Website agent that answers, qualifies, books meetings and sells low-priced items directly | automate to delegate | process | Randomized pre-sale chatbot, +16.3% sales (B, FANG-2026, organization unnamed); SaaStr (A, self-reported) |
| S5 | Marketing content generation: copy, images, push messages, product descriptions | augment | step to process | Klarna (B, VERDICT-2024); randomized results by workflow (B, FANG-2026) |
| S6 | Service representatives turned into sellers with an on-screen assistant | augment | process | Verizon (B, REUTERS-2025) |
| S7 | Proposal and RFP drafting from an approved content library | augment | step | Archetype entries (below) |
| S8 | Win/loss analysis and revenue attribution | augment | step | Archetype entries (below), mostly C |

**Metrics and benchmarks (with sources).**

- Outbound response rate, positive-response rate, meetings booked, revenue closed from agent-run channels. SaaStr reports 19,847 messages in six months, a 6.7% overall response rate and a 4% positive response rate; the "industry average ~3%" comparison is SaaStr's own claim (SAASTR-2025a, "Outbound AI SDR: real numbers"). Self-reported.
- Conversion rate and sales per consumer. In randomized experiments, conversion rose 1-22% across workflows while average cart value and purchase frequency did not change (FANG-2026 §1). Independent (academic; two authors consulted for the platform, one is an employee, per the paper's disclosures).
- Counter-metrics that catch harm: returns and customer ratings did not deteriorate in FANG-2026 abstract; sending-domain reputation needed a 2-3 week warm-up at SaaStr (SAASTR-2025b item 1); churn of customers who tried an AI SDR product (TECHCRUNCH-2025: a former employee cites 70-80% lost; the company says retention is 79%; these are not the same measure).
- Human oversight cost: 15-20 hours a week to coach five agents, and $50-100K a year per specialized platform, are SaaStr's own figures (SAASTR-2025a, learnings 2 and 5).
- Cost saving: Klarna said GenAI saved $10m in annual marketing costs and cut sales and marketing spend 11% in Q1 2024 (VERDICT-2024). Company statement, annualized.

**Interview probes for a function leader.** See section 4.1.

**Guardrails and decisions that need human judgment.**

- Marketing claims about what AI does must be substantiated; the FTC settled with a "robot lawyer" seller whose complaint alleged no testing against human-lawyer output (FTC-AICOMPLY-2024, DoNotPay section).
- Do not generate or buy fake reviews: the FTC's final rule covers reviews by someone who does not exist, such as AI-generated fake reviews, and allows civil penalties against knowing violators (FTC-FAKEREVIEWS-2024).
- Automated calls: calls made with AI-generated voices are "artificial" under the US Telephone Consumer Protection Act and need prior express consent (FCC-24-17 paras 1, 9).
- Customer claims and logos must be true; a prospect's lawyer cited false advertising and trademark causes of action over an unauthorized customer logo (TECHCRUNCH-2025).
- Interacting with an AI system must be disclosed to the person at first interaction (EU-AIACT-2024 Art 50(1), 50(5)). Dates have moved under the omnibus; see the archetype notes (assurance `frontier.md`).
- Human judgment: pricing and discounts, contract terms, strategic accounts and negotiations. SaaStr lets humans take over mid-conversation on its roughly $85K sponsorship deals (SAASTR-2025b item 2), and says a great human salesperson outperforms agents on complex deals (SAASTR-2025a).

**How roles change.**

- Sales development shifts from sending to coaching agents: SaaStr's two leaders spend 15-20 hours a week on it, and it reallocated budget from two human SDR roles (SAASTR-2025a, learnings 2 and 5).
- Service representatives are being reskilled into selling agents "in real time", per the Verizon consumer group CEO (REUTERS-2025).
- Marketing staff compete to share prompts; Lumen's marketing team built a prompt library (MICROSOFT-2024).

---

### 2.2 customer-service

**Main processes and key steps (synthesis; top-level category "Manage Customer Service" per APQC-2015).**

| Process | Key steps | Work types |
|---|---|---|
| Contact intake and identification | Receive request by channel; identify and authenticate customer | `transaction-processing`, `client-interaction` |
| Triage and routing | Classify intent and urgency; route to queue or self-service | `transaction-processing`, `coordination-scheduling` |
| Answer and resolve | Find the answer; respond; confirm resolution | `client-interaction`, `research-synthesis` |
| Case handling and fulfilment | Refunds, returns, changes, claims; back-office actions in other systems | `transaction-processing` |
| Escalation, complaints, disputes | Judge exceptions; handle complaints; apply policy and law | `expert-judgment`, `client-interaction` |
| Proactive outreach | Notify about issues, renewals or next steps | `document-production`, `client-interaction` |
| Knowledge management | Write and maintain answers; find content gaps from failed contacts | `document-production`, `research-synthesis` |
| Quality and coaching | Sample conversations; score; coach | `review-assurance` |
| Workforce planning | Forecast volume; schedule; train | `coordination-scheduling`, `data-reporting` |
| Voice of customer | Analyze reasons for contact, ratings, repeat contacts | `data-reporting` |

**Typical pain points.**

- New-agent ramp, attrition and training cost. The Brynjolfsson study cites $10,000 to $20,000 per agent and notes supervisors spend at least 20 hours a week on workforce challenges (NBER-BRYNJOLFSSON-2023 §2.1, citing others). Agents also face hostile customers and overnight shifts (same, §1).
- Customers cannot reach a person. The CFPB describes "doom loops" with no offramp to a human and cites a survey in which 78% needed a human after the chatbot failed (CFPB-2023, "Hindering access to timely human intervention"). Gartner's survey of 5,728 customers (Dec 2023) found 64% would prefer companies did not use AI in service; the top concern was harder access to a person (GARTNER-2024).
- Wrong answers presented as policy: Air Canada (CRT-2024), Cursor (ARS-2025).
- Hidden value is missed when only handle time is measured: customers can rate better without fewer repeat contacts (NI-2026 §1).

**Top AI opportunities (ladder x change scope), with graded evidence.**

| # | Opportunity | Ladder | Scope | Best evidence (grade) |
|---|---|---|---|---|
| C1 | Agent assist: drafts and next-step suggestions inside the chat | augment | step | Staggered rollout, 5,179 agents (B, org unnamed, NBER-BRYNJOLFSSON-2023); randomized, 5,940 agents (A, NI-2026) |
| C2 | Customer-facing assistant for routine questions with measured handoff | automate | process | Klarna (A), Salesforce help site (A), GOV.UK Chat (A) |
| C3 | Pre-sale and information chatbot | automate | step | Randomized, +16.3% sales vs no support (B, FANG-2026) |
| C4 | Passive caller authentication | automate | step | Archetype entry (A) |
| C5 | Draft replies to written inbound messages | augment | step | Patient-portal randomized QI study: no reply-time saving (B, adjacent, TAISEALE-2024) |
| C6 | Tax or public-service voicebots and agent assist | automate; augment | process; step | Archetype entries (A; B) |
| C7 | Analyze hand-offs to find knowledge gaps | augment | step | Salesforce says it does this (B, SALESFORCE-2025) |
| C8 | End-to-end agent that resolves cases across systems | delegate | process | No measured public evidence found; Klarna lists refunds and returns among tasks (KLARNA-2024) |

**Metrics and benchmarks (with sources).**

- Chats handled per hour: +0.37 on a baseline mean of 2.6, about 14%; the abstract reports the same size effect for issues resolved per hour (NBER-BRYNJOLFSSON-2023 §4.1). Population: 5,179 agents at one enterprise software firm, staggered rollout; independent.
- Customer requests to speak to a manager: about 25% decline from a baseline of about 6 percentage points (same, §6.2). This is requests, not actual escalations.
- Attrition among agents with under six months of tenure: about 10 points lower, a 40% decrease from a 25% baseline in that group; the authors say take with more caution (same, §6.3).
- Agents' adherence to AI suggestions: initially 30% for those with over a year of tenure and 37% for those under three months, converging about five months after deployment (same, §5.1).
- Alibaba after-sales: access cut issue identification time 8.2% and chat duration 1.1%, lowered dissatisfaction 3.4% relative to the 0.35 pre-treatment mean, raised ratings 1.2%, and had no significant effect on three-day retrials. 17.9% of treated agents never used the tool; usage fell from 39.3% (lowest-rated quintile) to 18.3% (highest) (NI-2026 §3.4, §5.2, §6.1, Table A7; usage rates §4.2). Independent.
- Containment and handoff: Salesforce reports more than 84% of questions "resolved" through its help-site agent and 4% handed to a human, which it says is deliberate; the definition of "resolved" is not published (SALESFORCE-2025). Self-reported.
- Repeat contact and satisfaction: Klarna reports a 25% drop in repeat inquiries and satisfaction on par with human agents in the first month (KLARNA-2024). Self-reported.
- Answer accuracy, rated by subject-matter experts against published content: GOV.UK Chat reports 76% rising to 90% (GOVTRANS-2026, secondary report of a GDS update). Self-reported.
- Customer attitude: 64% prefer no AI in service; 53% would consider switching (GARTNER-2024). Survey of customers, vendor-published research firm.

**Guardrails and decisions that need human judgment.**

- A company is responsible for its chatbot's statements on its website (CRT-2024 paras 26-28).
- Disclose AI interaction (EU-AIACT-2024 Art 50(1)); keep a path to a person. The CFPB says deficient chatbots that block access to live support can lead to law violations (CFPB-2023, conclusion).
- Treat confabulation and over-reliance as risks to manage (NIST-AI600-1-2024 §2.2, §2.7).
- Ground answers in approved content, remove personal data from the knowledge base, red-team before release, and expect jailbreak attempts: GDS removed pages with personal data, ran a red-team exercise, and recorded 508 attempted jailbreaks (GDS-2024; GOVTRANS-2026).
- Route by topic as well as by confidence: Salesforce directs renewal questions to a live engineer (SALESFORCE-2025).
- Human judgment: refunds and fee waivers outside policy (the CFPB notes advanced technologies may be less likely to waive fees, CFPB-2023), complaints with legal or regulatory dimension, vulnerable customers, anything irreversible.

**How roles change.**

- Newer agents reach experienced-agent performance sooner; treated agents with two months of tenure performed like untreated agents with over six months (NBER-BRYNJOLFSSON-2023 §1). The authors do not study aggregate employment or wages.
- Top performers can be hurt: in the Alibaba trial, top-quintile agents saw lower subjective and objective quality, consistent with workflow disruption (NI-2026 abstract).
- Klarna said in May 2025 it was recruiting human agents again and wanted customers to know a person is always available (MAGINATIVE-2025, reporting a Bloomberg interview; Bloomberg original not read).
- Service staff are expected to take on higher-touch work and, at Verizon, selling (SALESFORCE-2025; REUTERS-2025).

---

### 2.3 product-service-development

**Main processes and key steps (synthesis; top-level category "Develop and Manage Products and Services" per APQC-2015; staged decisions per STAGEGATE-2025; discover-define-develop-deliver per DESIGNCOUNCIL-2004).**

| Process | Key steps | Work types |
|---|---|---|
| Opportunity discovery and user research | Gather customer and market signals; interview and observe; synthesize needs | `research-synthesis`, `client-interaction` |
| Ideation and concept generation | Generate options; combine technical and commercial views; shortlist | `expert-judgment`, `document-production` |
| Concept testing and validation | Test concepts with consumers or users; read results | `data-reporting`, `research-synthesis` |
| Business case and gate decisions | Build the case; go/kill and resource decisions at gates | `expert-judgment`, `data-reporting` |
| Design and development | Design; build; configure; prototype | `software-systems`, `expert-judgment`, `physical-field` |
| Testing, validation and compliance | Test against requirements, safety and regulatory standards | `review-assurance` |
| Launch preparation and handover | Plan launch; hand to operations; document | `coordination-scheduling`, `document-production` |
| Lifecycle management | Collect feedback; manage roadmap and retirement; define service packaging and pricing | `data-reporting`, `coordination-scheduling` |

STAGEGATE-2025 describes stages of cross-functional work separated by gates at which senior leaders make go/kill and resource decisions.

**Typical pain points.**

- Function silos shape ideas: without AI, R&D staff proposed more technical solutions and commercial staff more commercial ones (NBER-DELLACQUA-2025 abstract).
- Consumer research is costly and noisy: the Colgate-Palmolive study says it costs companies billions annually and suffers panel biases and limited scale (MAIER-2025 abstract). Authors' framing.
- Long, uncertain cycles. In the Insilico trial the authors say few AI-designed drugs had reached human trials, and report 18 months from target discovery to preclinical candidate nomination (INSILICO-2025 abstract and discussion). Self-reported.
- Benefits are widely claimed but poorly measured: Cooper says commonly cited benefits rest on expert opinion, single-case anecdotes or broad surveys (COOPER-2024, section "Evidence"), and that only 13% of firms globally report using AI in new-product development, citing another study (same, section "Adoption").

**Top AI opportunities (ladder x change scope), with graded evidence.**

| # | Opportunity | Ladder | Scope | Best evidence (grade) |
|---|---|---|---|---|
| P1 | AI teammate in ideation and concept development | assist to augment | step | P&G pre-registered field experiment (A, NBER-DELLACQUA-2025) |
| P2 | Synthetic consumer panels to screen concepts before human research | augment | step to process | Colgate-Palmolive retrospective test (A, with caveat, MAIER-2025); practitioner caution (NNG-2024) |
| P3 | Generative discovery or design of candidate molecules, recipes or designs | augment to automate | step to process | Insilico phase 2a (A, INSILICO-2025); L'Oreal and Mondelez statements (B, RETAILGAZETTE-2026); Toyota Research Institute technique (C, announced) |
| P4 | Coding assistants in product engineering | assist to augment | step | Three field experiments, 4,867 developers (B, adjacent, CUI-2025) |
| P5 | Packaging firm expertise into an AI-delivered service | delegate | model | Archetype entries (below) |
| P6 | Stage-gate governance for AI adoption itself | n/a (method) | process | Cooper's staged adoption model (practitioner method, COOPER-2024) |

**Metrics and benchmarks (with sources).**

- Solution quality scored 1-10 by 22 blinded expert evaluators: individuals with AI +0.37 standard deviations, teams with AI +0.39 (NBER-DELLACQUA-2025 §5.1). Time spent 16.4% lower for individuals with AI and 12.7% lower for teams with AI (same, §5.1). Top-10% solutions: control mean 5.8%; teams with AI +9.2 points; the effect for individuals was not statistically significant (same, §6.1). Participants with AI were 9.2 points less likely to expect a top-10% result (same, §6.2). Independent (academic-led, with P&G co-authors and funding disclosed); an experimental task on real challenges, not a production rollout.
- Synthetic concept screening: 57 personal-care concept surveys (9,300 human responses); the method reaches 90% of human test-retest reliability with distributions similar to human data (Kolmogorov-Smirnov similarity above 0.85) (MAIER-2025 abstract). Self-reported by authors from PyMC Labs and Colgate-Palmolive.
- Clinical: phase 2a, 71 patients, 12 weeks; primary endpoint (any treatment-emergent adverse event) 72.2-83.3% across active arms and 70.6% on placebo; forced vital capacity +98.4 ml at 60 mg once daily vs -20.3 ml for placebo, in a trial the authors say warrants larger studies (INSILICO-2025 abstract). Self-reported, peer-reviewed.
- Cycle time and success rates in consumer goods: L'Oreal "four times faster" and Mondelez "months to weeks" are executive statements relayed by the press; Mondelez says 60% of AI-produced biscuit recipes performed better on nutrition, sustainability or cost (RETAILGAZETTE-2026, reporting Reuters).
- Software-delivery measures: completed tasks +26.08% (SE 10.3%) pooled over 4,867 developers (CUI-2025 abstract); task completed 55.8% faster in a 95-programmer trial (PENG-2023 abstract); 19% slower for 16 experienced open-source developers on 246 tasks in their own repositories (METR-2025 abstract). These are adjacent to product development and mostly belong to the technology function card.

**Guardrails and decisions that need human judgment.**

- Go/kill and resource decisions remain with gatekeepers (STAGEGATE-2025). In the P&G experiment AI users were less confident in solutions that scored better, so confidence is not a good signal (NBER-DELLACQUA-2025 §6.2).
- Synthetic users "cannot replace" real users; NN/g found them shallow or over-favorable and over-optimistic about behavior such as course completion (NNG-2024).
- Intellectual property, privacy and confabulation risks apply to generated designs and research outputs (NIST-AI600-1-2024 §2.2, §2.4, §2.10).
- Regulated products still need their own trials: the Insilico result is a randomized, placebo-controlled trial with safety as the primary endpoint (INSILICO-2025).
- AI-generated content shown to customers is subject to marking rules in the EU AI Act (Art 50(2); EU-AIACT-2024).

**How roles change.**

- R&D and commercial professionals produce more balanced solutions with AI, and individuals can do work previously done by pairs (NBER-DELLACQUA-2025 abstract).
- Cooper expects AI to alter how teams work and recommends a staged adoption program with gates (COOPER-2024).
- For software engineers in the three field experiments, less experienced developers had higher adoption and gains (CUI-2025 abstract).

---

## 3. Examples

Maturity words follow the source: "announced", "piloting", "in production" kept as stated.

### 3.1 sales-marketing-bd

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| S-E1 | SaaStr (B2B events and media) | Five specialized AI agents for cold outbound, lapsed customers, nurture, inbound qualification and ghosted-lead recovery; first 1,000 emails reviewed by hand, then 20-30 minute daily spot checks (SAASTR-2025b) | automate / process | 19,847 messages in six months, 6.7% response rate, 4% positive response; the inbound agent "closed over $1M in 90 days" per SaaStr; 15-20 hours a week of human oversight. Self-reported; "industry average" is SaaStr's claim | A | SAASTR-2025a, "Outbound AI SDR"; SAASTR-2025b item 1 |
| S-E2 | Unnamed cross-border online retail platform (retail, e-commerce) | Seven consumer-facing workflows run as randomized field experiments over six months in 2023-2024, including a pre-sale service chatbot, marketing push messages and product descriptions | automate; augment / step to process | Sales up to 16.3% (chatbot vs no support); search and product-description workflows about 2-3%; no detectable effect in advertising workflows; returns and ratings did not deteriorate. Independent. Platform not named, so B | B | FANG-2026 abstract, §1 |
| S-E3 | Lumen Technologies (telecom) | Sellers use an AI assistant to research customers, summarize 10-K reports and meetings, sync email into the CRM, and draft follow-ups | assist to augment / step | Company estimates four hours a week saved per seller, "equating to $50 million annually". Vendor-published estimate | B | MICROSOFT-2024, section on sellers |
| S-E4 | Klarna (fintech) | GenAI used in marketing campaigns and image creation; more campaigns run more often | augment / process | Klarna said it saved $10m in annual costs and cut sales and marketing spend 11% in Q1 2024. Company statement, annualized, relayed by press | B | VERDICT-2024 |
| S-E5 | Verizon (telecom) | AI assistant on service agents' screens; reps move from care to selling | augment / process | CEO of the consumer group said sales through the 28,000-person service team were up nearly 40% since deployment (started July 2024, full scale January 2025); no definition or causal design. Self-reported via press | B | REUTERS-2025 |
| S-E6 | ZoomInfo and Airtable (software) trials of an AI SDR product | Short trials of an AI outbound agent from an AI-sales vendor | automate / process | ZoomInfo's spokesperson said the product performed significantly worse than its SDR employees in a mid-January to mid-February trial; Airtable said its trial was "very short" and never used in production. Statements by the trialing organizations, reported by press | B | TECHCRUNCH-2025 |
| S-E7 | SaaStr (B2B events and media) | Sales calls transcribed and pushed to the CRM with next steps and contacts created; master sponsorship deck turned into prospect-specific 20-page decks | automate; augment / step | Described as a "data quality revolution"; no measure published. Self-reported | B | SAASTR-2025b items 4-5 |

Archetype use-case ids covering sales, marketing and BD in a professional-services setting (id and grade only; not re-researched):
professional-services-client-development-01 B, -02 B, -03 B, -04 C, -05 B, -06 B, -07 C, -08 C, -09 C, -10 C, -11 D, -12 B, -13 C, -14 B, -15 C, -18 C, -19 C, -20 B, -21 B, -22 B;
professional-services-pursuit-proposals-01 B, -02 B, -03 B, -04 B, -05 C, -06 B, -07 B, -08 B, -09 B, -10 C, -11 C, -12 B, -13 C, -14 C, -15 C, -16 C, -17 D, -18 D;
professional-services-scoping-pricing-01 B, -02 C, -03 C, -04 B, -05 B, -10 C, -15 C, -16 B, -18 B, -19 B, -20 B.

### 3.2 customer-service

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| C-E1 | Alibaba, Taobao after-sales (e-commerce) | Four-week randomized trial (23 Jan to 19 Feb 2024); 5,940 new agents (under one year) get AI-drafted issue diagnosis and solution proposals in the opening stage, free to adopt, edit or ignore | augment / step | Issue identification time -8.2%; chat duration -1.1%; dissatisfaction 3.4% lower relative to pretreatment mean; ratings +1.2%; no significant effect on three-day retrials; top-quintile agents saw lower quality. Independent (academic authors with an Alibaba co-author) | A | NI-2026 abstract, §3.4, §5.2, §6.1 |
| C-E2 | Klarna (fintech) | AI assistant, built with OpenAI, handles customer-service chats in its app; customers can still choose a live agent | automate / process | In its first month (announced 27 Feb 2024): 2.3 million conversations, two-thirds of chats; errands resolved in under 2 minutes vs 11; 25% drop in repeat inquiries; satisfaction on par. "Equivalent of 700 full-time agents" and "$40 million" profit are estimates. Self-reported | A | KLARNA-2024 |
| C-E3 | Salesforce, help.salesforce.com (software) | Agent on its own help site since 11 Oct 2024, grounded in about 740,000 pieces of help content; renewals questions sent to people; handoff conversations analyzed to improve the agent | automate / process | Over 500,000 conversations in six months; more than 84% of questions "resolved"; 4% handed to a human. Definition of "resolved" not published. Self-reported | A | SALESFORCE-2025 |
| C-E4 | UK Government Digital Service, GOV.UK Chat (public sector) | Retrieval-grounded assistant over published GOV.UK content; phased tests, red-teaming, private pilot, then public pilots | automate / step | Jan 2024 (n=157 survey): nearly 70% found responses useful, just under 65% satisfied, accuracy below GOV.UK's required level, a few hallucinations. March 2026 (press report of GDS update): accuracy 76% to 90%, 73% useful, 64% satisfied, 508 jailbreak attempts mitigated. Self-reported | A | GDS-2024; GOVTRANS-2026 |
| C-E5 | Unnamed Fortune 500 enterprise software firm (technology) | Staggered rollout of a conversational assistant giving real-time suggestions to chat agents | augment / step | About 14% more issues resolved per hour; about 34% for novice or low-skilled agents; minimal effect on experienced agents; ~25% fewer requests for a manager; attrition lower among new agents. Independent. Firm unnamed, so B despite the strong design | B | NBER-BRYNJOLFSSON-2023 abstract, §4, §5.1, §6 |
| C-E6 | Verizon (telecom) | AI assistant for 28,000 care agents built on about 15,000 internal documents; "cut down on call times" | augment / process | See S-E5. Self-reported via press | B | REUTERS-2025 |
| C-E7 | Academic health system, UC San Diego Health (healthcare) | AI-drafted replies to patient portal messages; randomized waiting-list QI study, June-Aug 2023, 52 randomized physicians plus 70 contemporary controls | augment / step | Read time +21.8%; reply time -5.9% (not significant); reply length +17.9%; physicians valued drafts as a compassionate starting point. Self-reported by the health system's researchers. Clinical messaging is adjacent to customer service, so capped at B | B | TAISEALE-2024 abstract |
| C-E8 | Air Canada (airline) | Website chatbot told a customer he could claim a bereavement fare after travel; the policy page said otherwise | automate / step (failure) | Tribunal found Air Canada liable for negligent misrepresentation and rejected the argument that the chatbot was a separate entity; fare difference at issue about C$870 (the tribunal's maximum). Independent | B | CRT-2024 paras 2, 24-28, 34 |
| C-E9 | Cursor (software) | Front-line support email agent "Sam" told a user a one-device policy existed | automate / step (failure) | Company's developer said there was no such policy and the response was incorrect; users posted cancellation threats. Press and community report, April 2025 | B | ARS-2025; HN-2025 |
| C-E10 | Klarna (fintech), follow-up | After the 2024 assistant, the CEO said in May 2025 cost had been too predominant a factor and quality lower, and the company was recruiting human agents | n/a (reversal) | Reported from a Bloomberg interview via a secondary article; no measurements. Press | B | MAGINATIVE-2025 |

Archetype use-case ids with `function: customer-service` (id and grade only):
security-identity-access-21 A; tax-controversy-18 A; tax-controversy-20 B.

### 3.3 product-service-development

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| P-E1 | Procter & Gamble (consumer goods) | Pre-registered field experiment, 776 professionals on real product-innovation challenges, randomized to AI or not, alone or in pairs | assist to augment / step | Individuals with AI matched teams without; solution quality +0.37 SD (individual) and +0.39 SD (team with AI); time -16.4% and -12.7%; more balanced R&D/commercial ideas. Academic-led, P&G co-authors; one-day task, not production | A | NBER-DELLACQUA-2025 abstract, §5.1, §6 |
| P-E2 | Insilico Medicine (biotechnology) | Generative AI used to find a target and design a small-molecule inhibitor; first randomized phase 2a trial | augment to automate / process | 71 patients over 12 weeks; adverse-event rates similar across arms; forced vital capacity +98.4 ml at 60 mg once daily vs -20.3 ml placebo; authors call for larger trials. Self-reported, peer-reviewed (Nature Medicine, June 2025) | A | INSILICO-2025 abstract |
| P-E3 | Colgate-Palmolive with PyMC Labs (consumer goods) | Retrospective test of LLM "synthetic consumers" against 57 past concept-test surveys | augment / step | 90% of human test-retest reliability, KS similarity above 0.85. Retrospective on historical surveys, not a production rollout. Self-reported by authors | A | MAIER-2025 abstract |
| P-E4 | Microsoft, Accenture and an anonymous Fortune 100 company (technology, professional services) | Randomized access to an AI code-completion assistant for developers | assist to augment / step | Completed tasks +26.08% (SE 10.3%) pooled across 4,867 developers; larger gains for less experienced. Adjacent to product development, so B. Academic-led with Microsoft authors | B | CUI-2025 abstract |
| P-E5 | L'Oreal and Mondelez (consumer goods) | AI used to find reusable molecules and to speed recipe development | augment / process | L'Oreal says "four times faster"; Mondelez says "months to weeks" and 60% of AI-produced biscuit recipes performed better on nutrition, sustainability or cost. Executive statements relayed by press (Reuters via Retail Gazette, 6 July 2026) | B | RETAILGAZETTE-2026 |
| P-E6 | Toyota Research Institute (automotive) | Announced (June 2023) a generative AI technique letting designers add sketches and engineering constraints such as drag to the generative process | augment / step | "Cutting down the iterations" per the announcement; no deployment or measurement published | C | AUTOMOTIVEWORLD-2023 |

Archetype use-case ids with `function: product-service-development` (id and grade only; these are firms packaging expertise as products):
professional-services-knowledge-management-22 B; professional-services-scoping-pricing-22 B; professional-services-scoping-pricing-23 B; professional-services-work-production-21 C.

---

## 4. Expert moves and probes

### 4.1 sales-marketing-bd

1. **"Walk me through one outbound sequence from account choice to meeting booked. Where does a person touch it?"** Reveals whether AI sits on one step or the whole flow, and who owns messaging quality. SaaStr needed proven messaging and a defined ICP before agents helped (SAASTR-2025a).
2. **"What does your CRM look like for the last 50 opportunities: complete, current, trusted?"** Reveals data readiness. Agents amplify what is in the record; incomplete logging was SaaStr's first blocker (SAASTR-2025a).
3. **"Which number would you show your CFO, and who counts it?"** Separates tracked metrics (response rate, meetings, revenue closed) from estimates like "hours saved equals dollars" (MICROSOFT-2024).
4. **"What will you do with the seller hours released?"** Hours are not value until they have a destination. Verizon pointed freed time at selling (REUTERS-2025).
5. **"What is the human review plan for the first thousand messages, and who reads replies?"** SaaStr reviewed its first 1,000 emails and then spot-checked daily (SAASTR-2025b item 1). No answer means quality risk.
6. **"Which claims about AI, customers or results appear in your marketing, and who substantiates them?"** Reveals exposure under FTC action on AI claims and fake testimonials, and the logo problem in TECHCRUNCH-2025.
7. **"Do any calls, texts or voice agents reach people who have not consented?"** Reveals telecom consent exposure (FCC-24-17).
8. **"Show me the control group."** Most sales AI evidence is before-and-after. Randomized results exist only for retail workflows and show effects from 0% to 16.3% (FANG-2026); a pilot without a control cannot separate the tool from seasonality.
9. **"Where do you hand a conversation to a human, and at what deal size?"** Reveals delegation boundaries; SaaStr allows takeover on large deals (SAASTR-2025b item 2).
10. **"What happened when you trialed an AI SDR product, and why did you stop or continue?"** Reveals real fit; the ZoomInfo and Airtable trials ended without roll-out (TECHCRUNCH-2025).

### 4.2 customer-service

1. **"What share of contacts are routine and answerable from approved content, and how do you know?"** Sizes the automation ceiling. Salesforce grounded its agent in about 740,000 content items before launch (SALESFORCE-2025).
2. **"How do you define a resolved contact, and do you track repeat contact within three days?"** Alibaba's speed and ratings improved while retrials did not (NI-2026); Salesforce's "resolved" is undefined in public (SALESFORCE-2025).
3. **"What is the route to a person, and how long does it take?"** The CFPB's doom loops and Gartner's top concern are both about this (CFPB-2023; GARTNER-2024).
4. **"Which topics must always go to a person?"** Reveals risk judgment; Salesforce sends renewals to engineers (SALESFORCE-2025).
5. **"Who owns what the bot says when it is wrong?"** Reveals accountability; Air Canada lost the argument that the chatbot was separate (CRT-2024).
6. **"How would you split rollout between new and top-rated agents?"** Effects differ by skill: novices gain most, top performers can lose quality (NBER-BRYNJOLFSSON-2023; NI-2026).
7. **"What is the plan for the agent population: hiring, ramp, attrition, redeployment?"** Reveals whether savings are planned as capacity, attrition or cuts. Klarna reversed course (MAGINATIVE-2025).
8. **"What do you do with the conversations where customers asked for a human?"** Salesforce analyzes handoffs to find gaps (SALESFORCE-2025); an unanalyzed handoff queue wastes the best training signal.
9. **"What is in your knowledge base that is out of date, contradictory or private?"** Stale or unapproved content is the main failure mode of grounded assistants; GDS removed pages with personal data and found some queries could not be answered because a GOV.UK page was too long (GDS-2024).
10. **"Do customers know they are talking to an AI?"** Legal disclosure and trust (EU-AIACT-2024 Art 50(1)); Cursor's customer believed a human replied (ARS-2025).

### 4.3 product-service-development

1. **"Show me the last concept that died at a gate. When was it found to be weak, and what would have found it sooner?"** Locates the step where AI could change timing, not just speed. Gates are go/kill points (STAGEGATE-2025).
2. **"Where do R&D and commercial views first meet on an idea?"** In the P&G experiment AI-supported individuals produced more balanced ideas (NBER-DELLACQUA-2025).
3. **"How do you choose among AI-generated options, and who judges?"** Participants with AI were less confident in better solutions (NBER-DELLACQUA-2025 §6.2); selection needs independent evaluation.
4. **"What decisions today rest on consumer panels, and what do they cost in time and money?"** Sizes synthetic-screening value; the Colgate result is on historical surveys (MAIER-2025).
5. **"Would you let synthetic respondents make the final call on anything?"** NN/g says they should complement, not replace, real research (NNG-2024). A yes means a governance gap.
6. **"What evidence do you have that earlier AI pilots shortened development, and was there a comparison?"** Cooper says the common claims are mostly anecdote (COOPER-2024).
7. **"Which of your products or services could be delivered by an agent with your expertise inside?"** The model-level question; see archetype entries on packaging expertise.
8. **"What approvals does a change need (safety, regulatory, IP), and how would AI-generated work show provenance?"** Insilico's route went through a randomized trial (INSILICO-2025); NIST flags IP and confabulation (NIST-AI600-1-2024).
9. **"How much of your engineering time is spent writing code versus specifying, reviewing and integrating?"** The field experiments show gains for newer developers but a slowdown for experienced ones in familiar repositories (CUI-2025; METR-2025).

---

## 5. Evidence on what works and what fails

**Controlled and large-sample studies**

| Study | Setting and population | What it measures | Result | Provenance |
|---|---|---|---|---|
| NBER-BRYNJOLFSSON-2023 | 5,179 chat-support agents, one Fortune 500 software firm; staggered rollout, bulk of adoption Nov 2020 to Feb 2021 (§3.1) | Issues resolved per hour | +14% average, +34% novice or low-skilled; minimal for experienced; suggestive evidence of lower quality for the most skilled | independent |
| NI-2026 | 5,940 new Taobao after-sales agents; four-week randomized trial, 2.56 million chats | Handle time, ratings, three-day retrials | Speed and ratings better; retrials no significant change; top agents worse | independent |
| FANG-2026 | Millions of consumers and products, cross-border retail platform; 7 randomized workflows | Sales, conversion, returns, ratings | Sales effects 0-16.3%; no deterioration in returns or ratings | independent (disclosures noted) |
| TAISEALE-2024 | 52 randomized physicians plus 70 contemporary controls | Read time, reply time, reply length | No reply-time saving; longer read time and replies | self-reported (health system authors) |
| NBER-DELLACQUA-2025 | 776 professionals at P&G | Blind-rated solution quality | AI individuals match teams without AI | independent (academic-led) |
| CUI-2025 | 4,867 developers at Microsoft, Accenture, a Fortune 100 firm | Completed tasks | +26.08% | independent (academic-led, Microsoft authors) |
| PENG-2023 | 95 professional programmers on a JavaScript task | Completion time | 55.8% faster | self-reported (GitHub and Microsoft authors) |
| METR-2025 | 16 experienced open-source developers, 246 tasks | Completion time | 19% slower with AI; developers had forecast 24% faster | independent |
| MAIER-2025 | 57 historical concept surveys, 9,300 responses | Reliability of synthetic ranking | 90% of human test-retest reliability | self-reported |
| INSILICO-2025 | 71 patients, randomized, placebo-controlled | Safety; lung function | Safety similar; FVC +98.4 ml at highest dose vs -20.3 ml | self-reported, peer-reviewed |

**Surveys and measurements**

- McKinsey's May-June 2026 survey (1,719 respondents, 97 countries): revenue gains from AI are most often attributed to marketing and sales, then product and service development and software engineering; cost reductions most often to supply chain, service operations and manufacturing; 37% report some EBIT impact, unchanged from last year (MCKINSEY-2026, exhibits 6-7 and key takeaways). Self-reported survey, weighted by national GDP share.
- Gartner (Dec 2023, 5,728 customers): 64% would prefer no AI in service; 53% would consider switching (GARTNER-2024). Research-firm survey.
- CFPB: 98 million users (about 37% of the US population) interacted with a bank's chatbot in 2022; all ten largest commercial banks use chatbots; the Bureau documents doom loops and warns deficient chatbots can lead to law violations (CFPB-2023). Regulator, independent.
- Cooper: only 13% of firms report using AI in new-product development (citing another study), and robust studies are few; one cited study of 558 projects associated AI use in ideation and design with higher success, which Cooper adjusts and caveats (COOPER-2024).

**Failures and incidents**

- Air Canada: negligent misrepresentation by a chatbot, company held liable (CRT-2024).
- Cursor: bot invented a policy (ARS-2025; HN-2025). In the thread a company developer said the response was incorrect and apologized.
- Klarna: May 2025 reversal toward human agents (MAGINATIVE-2025).
- An AI SDR vendor: former employees and named non-customers contest its customer and revenue claims; the company disputes aspects (TECHCRUNCH-2025). Allegations from press reporting, not findings.
- FTC cases: unsupported "robot lawyer" claims; a writing tool built to generate fake reviews (FTC-AICOMPLY-2024).
- GOV.UK Chat Jan 2024: answers not yet accurate enough, some users over-trusted the brand (GDS-2024).

**Quality evidence: what exists and what is missing**

- Override and adherence: agents followed AI suggestions initially 30-37% of the time, rising over five months (NBER-BRYNJOLFSSON-2023 §5.1); 17.9% of Alibaba treated agents never used the tool (NI-2026 §4.2).
- Accuracy: expert-rated accuracy at GOV.UK Chat (76% to 90%) is the only published expert-rated accuracy series found for a customer-facing assistant; self-reported.
- Escalation and handoff: Salesforce 4% (self-reported, not an error rate); manager-request decline of about 25% (NBER-BRYNJOLFSSON-2023 §6.2).
- Not found: any independent audit of an AI-handled contact "resolution rate"; parallel runs of AI versus human on the same contacts; a randomized trial of AI outbound sales messaging at a named company; independent confirmation of Klarna, Salesforce or Verizon numbers.

---

## 6. Gaps

- **Process frameworks.** APQC's current v8.0 definitions and measures documents are gated; only the v6.1.1 overview (top-level categories) was read (APQC-2015). Customer-service frameworks such as COPC and ITIL were not read. Process lists above are synthesis.
- **Delegate-level evidence.** No measured public example of an agent owning a multi-step case in customer service, an agent running a full sales cycle, or an agent progressing a product through gates.
- **Sales and marketing.** No independent randomized study of AI sales outreach at a named organization; campaign-effectiveness evidence is mostly vendor or self-reported. Not read: Salesforce, HubSpot or Gong research, Microsoft or LinkedIn buyer surveys.
- **Customer service quality.** No independent verification of company containment or resolution figures; the Bloomberg original behind the Klarna reversal was not read; Gartner's 2025 agentic-AI predictions could not be reached.
- **Product development.** No named-organization production measurements for consumer-research or design copilots beyond P&G, Colgate (retrospective) and pharma; Toyota Research Institute announcement has no outcome data. A search for Kia/Autodesk, GM and others surfaced only qualitative or unsourced claims and they were not used.
- **Standards.** ISO/IEC 42001 and the NIST AI RMF core were not read (only NIST AI 600-1). The EU AI Act Article 50 page was read, but Digital Omnibus timing changes are taken from archetype notes, not re-verified.
- **Jagged-frontier and other consultant studies** (BCG/Harvard) could not be opened and are not used.
- **Practitioner discourse** is thin: one Hacker News thread (606 comments, one incident) and SaaStr's own posts. No conference talks were used.
- Public sources only; Retail Gazette, Verdict, Maginative and AOL carry Reuters or Bloomberg reporting at second hand.

---

## 7. Sources

All accessed 2026-10-20. Access is `full` unless stated.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work (NBER Working Paper 31161), revised Nov 2023 | NBER; Brynjolfsson, Li, Raymond | academic | https://www.nber.org/papers/w31161 (PDF read: https://www.nber.org/system/files/working_papers/w31161/w31161.pdf) | 2023-11 | full |
| NI-2026 | Generative AI in Action: Field Experimental Evidence from Alibaba's Customer Service Operations | Ni, Wang, Feng, Lu, Wang, Zhou (arXiv 2603.29888) | academic | https://arxiv.org/pdf/2603.29888 | 2026-07 | full |
| FANG-2026 | Generative AI and Firm Productivity: Field Experiments in Online Retail (v3) | Fang, Yuan, Zhang, Donati, Sarvary (arXiv 2510.12049) | academic | https://arxiv.org/pdf/2510.12049v3 | 2026-02-10 | full |
| TAISEALE-2024 | AI-Generated Draft Replies Integrated Into Health Records and Physicians' Electronic Communication | JAMA Network Open (via PMC11019394); Tai-Seale et al. | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC11019394 | 2024-04 | full |
| NBER-DELLACQUA-2025 | The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise (NBER WP 33641) | NBER; Dell'Acqua et al. | academic | https://www.nber.org/papers/w33641 (PDF read: https://www.nber.org/system/files/working_papers/w33641/w33641.pdf) | 2025-04 | full |
| CUI-2025 | The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers | Cui, Demirer, Jaffe, Musolff, Peng, Salz | academic | https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf | 2025-02 | full |
| PENG-2023 | The Impact of AI on Developer Productivity: Evidence from GitHub Copilot | Peng, Kalliamvakou, Cihon, Demirer (arXiv 2302.06590) | academic | https://arxiv.org/pdf/2302.06590 | 2023-02-13 | full |
| METR-2025 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | METR (arXiv 2507.09089) | academic | https://arxiv.org/pdf/2507.09089 | 2025-07-25 | full |
| MAIER-2025 | LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings | PyMC Labs and Colgate-Palmolive (arXiv 2510.08338 v3) | academic | https://arxiv.org/pdf/2510.08338 | 2025-10 | full |
| INSILICO-2025 | A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial | Nature Medicine | academic | https://www.nature.com/articles/s41591-025-03743-2 | 2025-06-03 | full |
| COOPER-2024 | How to Transform Your New-Product Development with AI: From Vision to Deployment | Robert G. Cooper, ISBM (Penn State) | professional-body | https://isbm.org/wp-content/uploads/2024/01/Tranforming-NPD_Cooper_Jan-2024_rev2.pdf | 2024-01 | full |
| MCKINSEY-2026 | The state of AI in 2026: On the road to ROI | McKinsey and Company (via text mirror) | survey | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 2026-08-25 | full |
| GARTNER-2024 | Gartner Survey Finds 64% of Customers Would Prefer That Companies Didn't Use AI For Customer Service | Gartner (press release; read through a Gartner mirror host) | survey | https://www.gartner.com/en/newsroom/press-releases/2024-07-09-gartner-survey-finds-64-percent-of-customers-would-prefer-that-companies-didnt-use-ai-for-customer-service | 2024-07-09 | full |
| CFPB-2023 | Chatbots in consumer finance | Consumer Financial Protection Bureau | regulator | https://www.consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance/chatbots-in-consumer-finance/ | 2023-06-06 | full |
| CRT-2024 | Moffatt v. Air Canada, 2024 BCCRT 149 (decision SC-2023-005609) | British Columbia Civil Resolution Tribunal (read via text mirror) | regulator | https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do | 2024-02-14 | full |
| EU-AIACT-2024 | Article 50: Transparency Obligations for Providers and Deployers of Certain AI Systems, Regulation (EU) 2024/1689 (third-party reproduction of the Act's text) | artificialintelligenceact.eu | regulator | https://artificialintelligenceact.eu/article/50/ | 2024 | full |
| FTC-AICOMPLY-2024 | FTC Announces Crackdown on Deceptive AI Claims and Schemes | Federal Trade Commission (via text mirror) | regulator | https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes | 2024-09-25 | full |
| FTC-FAKEREVIEWS-2024 | Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials | Federal Trade Commission (via text mirror) | regulator | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials | 2024-08-14 | full |
| FCC-24-17 | Declaratory Ruling FCC 24-17: Implications of Artificial Intelligence Technologies on Protecting Consumers from Unwanted Robocalls and Robotexts | Federal Communications Commission | regulator | https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf | 2024-02-08 | full |
| NIST-AI600-1-2024 | Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1) | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | 2024-07 | full |
| KLARNA-2024 | Klarna AI assistant handles two-thirds of customer service chats in its first month (press release) | Klarna | firm | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ | 2024-02-27 | full |
| MAGINATIVE-2025 | Klarna Dials Back its AI Customer Service Strategy: Now It's Hiring Humans Again | Maginative (Chris McKay), reporting a Bloomberg interview | press | https://www.maginative.com/article/klarna-dials-back-its-ai-customer-service-strategy-now-its-hiring-humans-again/ | 2025-05-08 | full |
| VERDICT-2024 | Klarna says it has cut marketing costs by $10m with GenAI | Verdict | press | https://www.verdict.co.uk/klarna-says-it-has-cut-marketing-costs-by-10m-with-genai/ | 2024-05-28 | full |
| SALESFORCE-2025 | Lessons from 500,000 Agentforce Customer Conversations | Salesforce (news story) | firm | https://www.salesforce.com/news/stories/agentforce-customer-support-lessons-learned/ | 2025-04-22 | full |
| GDS-2024 | The findings of our first generative AI experiment: GOV.UK Chat | Government Digital Service, Inside GOV.UK blog | firm (public-sector body) | https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/ | 2024-01-18 | full |
| GOVTRANS-2026 | GDS reports improved accuracy and user satisfaction in GOV.UK Chat pilots | Government Transformation (Tim Coulthard), reporting a GDS update | press | https://www.government-transformation.com/data/gds-reports-improved-accuracy-and-user-satisfaction-in-gov.uk-chat-pilots | 2026-03-20 | full (GDS 2026 original not opened) |
| REUTERS-2025 | Verizon says Google AI for customer service agents has led to sales jump | Reuters (Kenrick Cai), read via AOL | press | https://www.aol.com/news/verizon-says-google-ai-customer-120648406.html | 2025-04-09 | full |
| MICROSOFT-2024 | How Lumen Technologies Is Using Microsoft Copilot to Drive Creativity and Digital Transformation | Microsoft Source (feature; read via text mirror) | vendor | https://news.microsoft.com/source/features/digital-transformation/the-only-way-how-copilot-is-helping-propel-an-evolution-at-lumen-technologies/ | 2024-07-25 | full |
| SAASTR-2025a | 6 Months of AI SDRs: What's Worked, How They Brought In $1M+ in 90 Days, and the Real Data | SaaStr (Jason Lemkin) | firm | https://www.saastr.com/6-months-of-ai-sdrs-whats-worked-how-they-brought-in-1m/ | 2025-11-20 | full |
| SAASTR-2025b | SaaStr's AI Agent Playbook: How We Deployed 20+ Agents | SaaStr (Jason Lemkin) | firm | https://www.saastr.com/saastrs-ai-agent-playbook-how-we-deployed-20-agents-to-scale-8-figure-revenue-with-single-digit-headcount | 2025-09-25 | full |
| TECHCRUNCH-2025 | a16z- and Benchmark-backed 11x has been claiming customers it doesn't have | TechCrunch (Davis, Temkin) | press | https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have/ | 2025-03-24 | full |
| ARS-2025 | Company apologizes after AI support agent invents policy that causes user uproar | Ars Technica | press | https://arstechnica.com/ai/2025/04/cursor-ai-support-bot-invents-fake-policy-and-triggers-user-uproar/ | 2025-04-17 | full |
| HN-2025 | Cursor IDE support hallucinates lockout policy, causes user cancellations (thread of 606 comments) | Hacker News, read through the public Algolia API | community | https://news.ycombinator.com/item?id=43683012 (data: https://hn.algolia.com/api/v1/items/43683012) | 2025-04-14 | full |
| NNG-2024 | Synthetic Users: If, When, and How to Use AI-Generated "Research" | Nielsen Norman Group | professional-body | https://www.nngroup.com/articles/synthetic-users/ | 2024-06-21 | full |
| RETAILGAZETTE-2026 | L'Oreal and Mondelez turn to AI to speed up product innovation | Retail Gazette, reporting Reuters | press | https://www.retailgazette.co.uk/blog/2026/07/loreal-and-mondelez-turn-to-ai-to-speed-up-product-innovation/ | 2026-07-06 | full |
| AUTOMOTIVEWORLD-2023 | Toyota Research Institute unveils new generative AI technique for vehicle design | Automotive World (reproducing a TRI announcement) | press | https://www.automotiveworld.com/news/toyota-research-institute-unveils-new-generative-ai-technique-for-vehicle-design/ | 2023-06-20 | full |
| STAGEGATE-2025 | The Stage-Gate Model: An Overview | Stage-Gate International (via text mirror) | firm | https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/ | 2025-12-15 | full |
| DESIGNCOUNCIL-2004 | Framework for Innovation (Double Diamond) | Design Council (via text mirror); the page is undated and says the Double Diamond launched in 2004 | professional-body | https://www.designcouncil.org.uk/our-resources/framework-for-innovation/ | 2004 | full |
| APQC-2015 | APQC Process Classification Framework, cross-industry overview, version 6.1.1 | APQC (hosted by Queensland Government) | professional-body | https://www.forgov.qld.gov.au/__data/assets/pdf_file/0027/319842/apqc_pcf_ver_6.1.1-final.pdf | 2015-07 | full (overview and top-level categories only; v8.0 definitions gated) |
