# Customer service

Function id `customer-service`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:** this
function has the strongest controlled evidence of the commercial functions, and it is mixed. Agent assistance speeds up newer and
lower-rated agents; the most skilled gain little or lose quality [NBER-BRYNJOLFSSON-2023; NI-2026]. Speed and ratings can improve while
repeat contacts do not move [NI-2026]. Customer-facing automation works on routine questions and fails loudly at the edges (Air
Canada, Cursor, Klarna's 2025 reversal).

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

Contact with customers, clients, citizens or employees who need an answer or a fix: intake, triage, answering, case handling,
complaints, outreach, the knowledge behind answers, quality, workforce planning and voice of the customer. No archetype covers
contact-centre outsourcers; use this card. Tax-authority service is in the tax archetype (`controversy` module) and contact-centre
caller authentication in the security archetype (`identity-access` module).

## 2. Processes and key steps

The process list is a working grouping under the "manage customer service" category of a cross-industry process framework
[APQC-2015].

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| Contact intake and identification | Receive by channel; identify and authenticate | transaction-processing, client-interaction | No source-backed figure here; see the security archetype for authentication |
| Triage and routing | Classify intent and urgency; route to queue or self-service | transaction-processing, coordination-scheduling | Customers cannot reach a person: the CFPB describes "doom loops" with no offramp to a human [CFPB-2023] |
| Answer and resolve | Find the answer; respond; confirm resolution | client-interaction, research-synthesis | Wrong answers presented as policy (Air Canada, Cursor) [CRT-2024; ARS-2025] |
| Case handling and fulfilment | Refunds, returns, changes, claims; back-office actions | transaction-processing | No measured agent case found (§3) |
| Escalation, complaints, disputes | Judge exceptions; apply policy and law | expert-judgment, client-interaction | Advanced technologies may be less likely to waive fees, per the CFPB [CFPB-2023] |
| Knowledge management | Write and maintain answers; find gaps from failed contacts | document-production, research-synthesis | Some questions could not be answered because a source page was too long [GDS-2024] |
| Quality and coaching | Sample conversations; score; coach | review-assurance | Handle time hides quality: ratings can improve without fewer repeat contacts [NI-2026] |
| Workforce planning | Forecast volume; schedule; train | coordination-scheduling, data-reporting | New-agent ramp and attrition: $10,000-20,000 per agent, cited by one study [NBER-BRYNJOLFSSON-2023] |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **Agent assist: drafts and next-step suggestions inside the chat**
  ([grounded-knowledge-assistant](../patterns/grounded-knowledge-assistant.md); augment; step). Alibaba, Taobao after-sales
  (e-commerce): four-week randomized trial with 5,940 new agents; issue identification time -8.2%, chat duration -1.1%, dissatisfaction
  3.4% lower, ratings +1.2%; no significant effect on three-day repeat contacts; top-quintile agents saw lower quality. Independent
  (academic authors with an Alibaba co-author). Grade A [NI-2026]. An unnamed Fortune 500 software firm's staggered rollout to 5,179
  agents: about 14% more issues resolved per hour, about 34% for novice or low-skilled agents, minimal effect for experienced agents.
  Independent; firm unnamed. Grade B [NBER-BRYNJOLFSSON-2023].
- **Draft replies to written inbound messages** ([draft-review-loop](../patterns/draft-review-loop.md); augment; step). UC San Diego
  Health (healthcare, adjacent): AI-drafted replies to patient-portal messages in a randomized quality-improvement study; read time
  +21.8%, reply time -5.9% (not significant), replies 17.9% longer; physicians valued the drafts as a compassionate starting point.
  Grade B (adjacent) [TAISEALE-2024].
- **Analyze handoffs to find knowledge gaps** ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); augment; step). Salesforce
  says it analyzes the conversations its help-site agent hands to people; no measure. Grade B [SALESFORCE-2025].

**Automate the flow**

- **Customer-facing assistant for routine questions, with a measured handoff**
  ([service-agent-escalation](../patterns/service-agent-escalation.md); automate; process).
  - Klarna (fintech): in its first month, 2.3 million conversations, two-thirds of chats, errands resolved in under 2 minutes against
    11, a 25% drop in repeat inquiries and satisfaction on par with human agents; the profit figure is an estimate. Self-reported.
    Grade A [KLARNA-2024].
  - Salesforce help site (software): over 500,000 conversations in six months, more than 84% of questions "resolved" and 4% handed to
    a person; "resolved" is not defined publicly; renewal questions go to people. Self-reported. Grade A [SALESFORCE-2025].
  - GOV.UK Chat (public sector): in January 2024, nearly 70% found answers useful but accuracy was below the required level; a 2026
    press report of a GDS update gives expert-rated accuracy rising from 76% to 90% and 508 jailbreak attempts mitigated.
    Self-reported. Grade A [GDS-2024; GOVTRANS-2026].
- **Pre-sale information chatbot** ([service-agent-escalation](../patterns/service-agent-escalation.md); automate; step). Up to 16.3%
  more sales against no support on an unnamed retail platform (randomized, independent). Grade B [FANG-2026].
- **Passive caller authentication and public-service voicebots**: archetype entries `security-identity-access-21` (A) and
  `tax-controversy-18` (A).

**Delegate the outcome**

- **An agent that resolves cases across systems** ([end-to-end-case-agent](../patterns/end-to-end-case-agent.md); delegate;
  process). No measured public evidence found; Klarna lists refunds and returns among the assistant's tasks [KLARNA-2024].

**Reinvent the work**

- **Service teams become selling teams.** Verizon (telecom): an assistant built on about 15,000 internal documents for 28,000 care
  agents; the consumer group CEO said sales through the service team were up nearly 40% since deployment (no definition or causal
  design). Grade B [REUTERS-2025].
- **Reversal as a warning.** In May 2025 Klarna's CEO said cost had been too predominant a factor and quality was lower, and the
  company was recruiting human agents again (secondary report of a Bloomberg interview). Grade B [MAGINATIVE-2025].

**In the archetypes**: `security-identity-access-21` (A), `tax-controversy-18` (A), `tax-controversy-20` (B, agent assist for
tax-authority staff).

## 4. Metrics and benchmarks

- **Throughput:** +0.37 chats per hour on a 2.6 baseline, about 14% (5,179 agents, independent) [NBER-BRYNJOLFSSON-2023].
- **Repeat contact:** no significant change in three-day repeat contacts despite faster, better-rated chats (independent) [NI-2026];
  25% fewer repeat inquiries (Klarna, self-reported) [KLARNA-2024].
- **Escalation requests:** about 25% fewer customer requests to speak to a manager, from a baseline of about 6 percentage points;
  requests, not actual escalations [NBER-BRYNJOLFSSON-2023].
- **Adherence and use:** agents initially followed suggestions 30-37% of the time, converging after about five months
  [NBER-BRYNJOLFSSON-2023]; 17.9% of treated Alibaba agents never used the tool, and use fell from 39.3% in the lowest-rated quintile
  to 18.3% in the highest [NI-2026].
- **Containment and handoff:** more than 84% "resolved", 4% handed to a person (definition unpublished) [SALESFORCE-2025].
- **Answer accuracy rated by experts:** 76% rising to 90% (self-reported; the only expert-rated accuracy series found)
  [GOVTRANS-2026].
- **Customer attitude:** 64% of 5,728 customers would prefer companies did not use AI in service; 53% would consider switching
  [GARTNER-2024].

## 5. Interview probes

1. "What share of contacts are routine and answerable from approved content, and how do you know?" Sizes the automation ceiling;
   Salesforce grounded its agent in about 740,000 content items [SALESFORCE-2025].
2. "How do you define a resolved contact, and do you track repeat contact within three days?" Reveals whether quality is measured
   beyond speed [NI-2026; SALESFORCE-2025].
3. "What is the route to a person, and how long does it take?" Reveals the doom-loop risk [CFPB-2023; GARTNER-2024].
4. "Which topics must always go to a person?" Reveals risk judgment; Salesforce sends renewals to people [SALESFORCE-2025].
5. "Who owns what the bot says when it is wrong?" Reveals accountability; Air Canada lost the argument that its chatbot was a separate
   entity [CRT-2024].
6. "How would you split rollout between new and top-rated agents?" Reveals whether rollout is tailored to skill
   [NBER-BRYNJOLFSSON-2023; NI-2026].
7. "What is the plan for the agent workforce: hiring, ramp, attrition, redeployment?" Reveals whether savings are planned as capacity;
   Klarna reversed course [MAGINATIVE-2025].
8. "What do you do with conversations where customers asked for a person?" Reveals whether the best training signal is used
   [SALESFORCE-2025].
9. "What in your knowledge base is out of date, contradictory or private?" Reveals the stale-content failure mode; GDS removed pages
   with personal data [GDS-2024].
10. "Do customers know they are talking to an AI?" Reveals disclosure and trust; Cursor's customer believed a human had replied
    [EU-AIACT-ART50-2024; ARS-2025].

## 6. Guardrails

- **The company owns what its chatbot says.** A tribunal held Air Canada liable for negligent misrepresentation by its website
  chatbot [CRT-2024]. Cursor's support agent invented a one-device policy; a company developer said the response was incorrect
  [ARS-2025].
- **Keep a path to a person and disclose AI.** The CFPB says deficient chatbots that block access to live support can lead to law
  violations [CFPB-2023]; EU deployers must tell people they are interacting with an AI system [EU-AIACT-ART50-2024].
- **Ground answers in approved content and test before release.** GDS removed personal data from the knowledge base, ran a red-team
  exercise and recorded jailbreak attempts [GDS-2024; GOVTRANS-2026]. Treat confabulation and over-reliance as risks to manage
  [NIST-AI600-1-2024].
- **Route by topic as well as by confidence** (Salesforce sends renewals to people) [SALESFORCE-2025].
- **Decisions that need human judgment:** refunds and fee waivers outside policy; complaints with a legal or regulatory dimension;
  vulnerable customers; anything irreversible.

## 7. Roles and how they evolve

- **Newer agents ramp faster:** treated agents with two months of tenure performed like untreated agents with over six months;
  attrition among agents under six months' tenure was about 40% lower (authors urge caution) [NBER-BRYNJOLFSSON-2023].
- **Top performers can be hurt:** top-quintile agents saw lower quality, consistent with workflow disruption [NI-2026].
- **Agents move to higher-touch work and, at Verizon, to selling** [SALESFORCE-2025; REUTERS-2025].
- **Knowledge owners matter more:** handoff analysis and content upkeep become ongoing work [SALESFORCE-2025; GDS-2024].

## 8. Sources

- **APQC-2015**: APQC, *Process Classification Framework, cross-industry overview, v6.1.1* (professional body, 2015-07). https://www.forgov.qld.gov.au/__data/assets/pdf_file/0027/319842/apqc_pcf_ver_6.1.1-final.pdf
- **ARS-2025**: Ars Technica, *Company apologizes after AI support agent invents policy that causes user uproar* (press, 2025-04-17). https://arstechnica.com/ai/2025/04/cursor-ai-support-bot-invents-fake-policy-and-triggers-user-uproar/
- **CFPB-2023**: Consumer Financial Protection Bureau, *Chatbots in consumer finance* (regulator, 2023-06-06). https://www.consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance/chatbots-in-consumer-finance/
- **CRT-2024**: British Columbia Civil Resolution Tribunal, *Moffatt v. Air Canada, 2024 BCCRT 149* (tribunal decision, 2024-02-14). https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do
- **EU-AIACT-ART50-2024**: Regulation (EU) 2024/1689, *Article 50: Transparency obligations* (regulation text via artificialintelligenceact.eu, 2024). https://artificialintelligenceact.eu/article/50/
- **FANG-2026**: Fang et al., *Generative AI and Firm Productivity: Field Experiments in Online Retail* (academic, arXiv 2510.12049 v3, 2026-02-10). https://arxiv.org/pdf/2510.12049v3
- **GARTNER-2024**: Gartner, *64% of Customers Would Prefer That Companies Didn't Use AI For Customer Service* (survey release, n=5,728, 2024-07-09). https://www.gartner.com/en/newsroom/press-releases/2024-07-09-gartner-survey-finds-64-percent-of-customers-would-prefer-that-companies-didnt-use-ai-for-customer-service
- **GDS-2024**: Government Digital Service, *The findings of our first generative AI experiment: GOV.UK Chat* (public body, 2024-01-18). https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/
- **GOVTRANS-2026**: Government Transformation, *GDS reports improved accuracy and user satisfaction in GOV.UK Chat pilots* (press, 2026-03-20). https://www.government-transformation.com/data/gds-reports-improved-accuracy-and-user-satisfaction-in-gov.uk-chat-pilots
- **KLARNA-2024**: Klarna, *Klarna AI assistant handles two-thirds of customer service chats in its first month* (firm release, 2024-02-27). https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
- **MAGINATIVE-2025**: Maginative, *Klarna Dials Back its AI Customer Service Strategy: Now It's Hiring Humans Again* (press, 2025-05-08). https://www.maginative.com/article/klarna-dials-back-its-ai-customer-service-strategy-now-its-hiring-humans-again/
- **NBER-BRYNJOLFSSON-2023**: Brynjolfsson, Li, Raymond, *Generative AI at Work*, NBER Working Paper 31161 (academic, 2023-11). https://www.nber.org/papers/w31161
- **NI-2026**: Ni et al., *Generative AI in Action: Field Experimental Evidence from Alibaba's Customer Service Operations* (academic, arXiv 2603.29888, 2026-07). https://arxiv.org/pdf/2603.29888
- **NIST-AI600-1-2024**: NIST, *AI RMF: Generative AI Profile* (standard-setter, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **REUTERS-2025**: Reuters via AOL, *Verizon says Google AI for customer service agents has led to sales jump* (press, 2025-04-09). https://www.aol.com/news/verizon-says-google-ai-customer-120648406.html
- **SALESFORCE-2025**: Salesforce, *Lessons from 500,000 Agentforce Customer Conversations* (firm, 2025-04-22). https://www.salesforce.com/news/stories/agentforce-customer-support-lessons-learned/
- **TAISEALE-2024**: Tai-Seale et al., *AI-Generated Draft Replies Integrated Into Health Records and Physicians' Electronic Communication*, JAMA Network Open (academic, 2024-04). https://pmc.ncbi.nlm.nih.gov/articles/PMC11019394
