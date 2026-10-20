# Pattern: service-agent-escalation

Answers clients, citizens or staff directly and hands off to a person when needed. Read this when an option puts
AI in front of the people who contact the organization. Keys in brackets are listed in §11. Lines marked
*(guidance)* are design advice, not findings from a source.

## Contents

1. [What it is](#1-what-it-is)
2. [Where it fits](#2-where-it-fits)
3. [Up the ladder](#3-up-the-ladder)
4. [How it is built](#4-how-it-is-built)
5. [Prerequisites](#5-prerequisites)
6. [Failure modes and controls](#6-failure-modes-and-controls)
7. [Value and metrics](#7-value-and-metrics)
8. [Governance](#8-governance)
9. [Evidence](#9-evidence)
10. [Probes](#10-probes)
11. [Sources](#11-sources)

## 1. What it is

An assistant answers by chat, voice or messaging, gathers information, completes simple transactions where
permitted, and hands off to a person when it cannot help, when the sender asks, or when a rule fires. The handoff
design is the product: in a randomized field experiment, human takeover kept quality in technical escalations but
worked less well in emotional ones, and early intervention mattered [ARXIV-WANG-2026]. Its sibling,
`intake-triage`, sorts items without answering; `grounded-knowledge-assistant` answers staff from approved content.

**How to recognize it** *(guidance)*: "the same twenty questions make up most of our contacts"; "wait times at
peak"; "agents spend the day on password resets, order status, opening hours"; "people must reach a human when it
is complicated"; "we answer in several languages". Lyft says riders and drivers waited 30 to 40 minutes for an
agent before its change [LYFT-ANTHROPIC-2026].

## 2. Where it fits

- **Work type:** `client-interaction`, for high-volume, repeatable questions with approved answers.
- **Not to hold customers away from people.** Klarna's CEO linked a cost focus to "lower quality" and a return to hiring humans [ENTREPRENEUR-KLARNA-2025]; customers' top stated concern is difficulty reaching a person [GARTNER-CSAT-2024]; the CFPB describes "doom loops" with no off-ramp [CFPB-CHATBOTS-2023].
- **Not for questions whose wrong answer carries legal or financial liability** without approved, citable content [GUARDIAN-AIRCANADA-2024; MARKUP-MYCITY-2024].
- **Not with write or refund tools before reliability is shown on repeated trials** [SIERRA-TAUBENCH-2024].
- **Not for emotionally charged or vulnerable-person contacts without an early human path** [ARXIV-WANG-2026].
- **Not if success is counted as conversations handled or containment alone** [KLARNA-AIASSISTANT-2024; ATRS-NSI-2025].

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Suggests answers to a human agent (adjacent to this pattern) | Answers the customer | `personal-assistant`, `shared-team-skills` | Approved content with an owner; top contact reasons known |
| `augment` | Gathers the reason and facts, then transfers with the transcript (DVLA, HMRC) | Finishes the contact; does identity checks | `workflow-automation` | Resolution and repeat-contact figures for bot-started contacts |
| `automate` | Resolves defined intents end to end; escalates on rules | Takes escalations; reviews transcripts | `workflow-automation`, `background-agent` | Per intent: resolution, repeat contact and rating match the human baseline *(guidance)* |
| `delegate` | Acts with tools (refunds, rebooking) under checkpoints | Approves high-risk actions; audits | `managed-agent-runtime` | Reliability shown with repeated trials; scoped data access [SIERRA-TAUBENCH-2024; SALESFORCE-CRMARENA-2025] |

Expand by intent, not by channel *(guidance)*.

## 4. How it is built

- **Inputs.** A bounded body of approved content or intents: HMRC matches questions to curated answers linking to GOV.UK guidance [ATRS-HMRC-2025]; NS&I draws on about 200 web pages and documents [ATRS-NSI-2025].
- **The AI's role.** Intent detection with scripted answers ("classified into a predefined intent... deterministic dialogue" [ATRS-MOJ-2026]) or generation grounded on content. Intent-first designs trade flexibility for predictability.
- **Escalation triggers named in sources:** the bot does not understand, or the customer asks [ATRS-DVLA-CHATBOT-2025]; repeated failure to understand and high-risk actions such as large refunds [OPENAI-AGENTS-2025]; detected capability limits and customer frustration, plus human-initiated takeover [ARXIV-WANG-2026].
- **Handoff quality.** The adviser receives the transcript (HMRC, DVLA) [ATRS-HMRC-2025; ATRS-DVLA-CHATBOT-2025]; the person should pick up where the bot left off [GARTNER-CSAT-2024].
- **Monitoring and sampling.** HMRC monitors daily with dashboards and re-scores its test set [ATRS-HMRC-2025]; MoJ's supplier lists transcript review, live-call review and regression testing after each change [ATRS-MOJ-2026]. *(Guidance:)* sample conversations by outcome (resolved, escalated, abandoned) and by intent, with extra weight on conversations that ended without escalation.
- **Logging.** Store conversations for review [ATRS-HMRC-2025]. *(Guidance:)* log the answer, the content it used, the escalation trigger, who took over and the end outcome.

## 5. Prerequisites

- **Data.** Real contact logs to find top intents (HMRC trained on 28,575 unique samples [ATRS-HMRC-2025]); current, approved content with an owner.
- **Access.** Read access to the knowledge base; scoped tool permissions where the bot acts. In DVLA's design identity checks stay with the human adviser [ATRS-DVLA-CHATBOT-2025].
- **Policy.** Tell people they are talking to AI (EU AI Act Art. 50(1)) [EU-AIACT-2024]; accept that you are liable for what the bot says [GUARDIAN-AIRCANADA-2024]; jailbreak testing, knowing that no successful jailbreak cannot be guaranteed [ATRS-GOVUKCHAT-2025].
- **Skills** *(guidance)*: a content owner or conversation designer, a team that reviews transcripts weekly, and a person who can change escalation rules.

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Confident wrong answer with legal or financial effect | Air Canada held liable for its chatbot's fare advice [GUARDIAN-AIRCANADA-2024]; MyCity gave incorrect guidance on housing and worker rules [MARKUP-MYCITY-2024] | Answer only from approved content; no policy statements the bot cannot cite |
| Invented policy | A support agent told users a non-existent policy applied [ARS-CURSOR-2025] | Label bot answers; route policy and billing questions to people |
| Failure after an update | DPD's bot swore and criticised the company after an update [BBC-DPD-2024] | Regression tests after each change [ATRS-MOJ-2026]; a kill switch |
| No exit to a person | Complaints of loops [CFPB-CHATBOTS-2023] | Always-available human option and a failure-count trigger [OPENAI-AGENTS-2025] |
| Escalation too late; the person disengages | Weaker quality in emotional escalations [ARXIV-WANG-2026] | Trigger on frustration, not only capability limits; hand over early |
| Inconsistent rule-following | Pass^8 below 25% in a retail benchmark [SIERRA-TAUBENCH-2024] | Test with repeated trials, not one pass |
| Data leakage | "Near-zero" inherent confidentiality awareness in tested agents [SALESFORCE-CRMARENA-2025] | Scope data access; do not rely on the model to withhold |
| Injection through customer text | Hidden instructions in messages | Least privilege; human approval for high-risk actions [OWASP-LLM01-2025] |

## 7. Value and metrics

- **Levers:** `cost`, `capacity`, `speed`, `experience`, `quality`.
- **Typical figures:** Klarna, first month: two-thirds of chats, resolution under 2 minutes vs 11, repeat inquiries down 25%; "700 full-time agents" and $40 million are estimates (self-reported) [KLARNA-AIASSISTANT-2024]. Bank of America: IT service desk calls down 50% (self-reported) [BOFA-ERICA-2025]. NS&I: about 22.23% of calls contained, all simple queries (self-reported) [ATRS-NSI-2025].
- **Quality metrics to demand:** resolution, not containment; repeat contact within a fixed window (Taobao used re-contact on the same issue within seven days [ARXIV-WANG-2026]); ratings of AI-handled vs human-handled contacts; intent accuracy [ATRS-HMRC-2025]; "appropriate escalation rate" [ATRS-MOJ-2026]. *(Guidance:)* add the share of escalations that were warranted and of unescalated contacts that should have been escalated.
- **Caution.** In the Taobao experiment chat time fell while ratings fell 0.412 points for AI-eligible chats [ARXIV-WANG-2026]. Freed agent hours are not value until they have a destination (`../index.md` §5).

## 8. Governance

- **EU AI Act.** Art. 50(1): people must be told they are interacting with AI unless obvious [EU-AIACT-2024]; this duty stays on the 2 August 2026 timetable, per a law-firm summary [KLGATES-OMNIBUS-2026]. Annex III 5(d) makes classifying emergency calls high-risk [EU-AIACT-2024].
- **GDPR Art. 22** if the agent decides something with legal or similarly significant effect [EU-GDPR-2016].
- **NIST AI 600-1** names confabulation, human-AI configuration and information security among generative AI risks [NIST-AI600-2024].
- **ISO/IEC 42001** as the organization-level management system [BSI-ISO42001-2026].
- **Financial services.** The CFPB found all top 10 commercial banks use chatbots and reported complaints about loops [CFPB-CHATBOTS-2023].

## 9. Evidence

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| Alibaba Taobao | Retail e-commerce | Agentic AI resolves eligible chats under supervision; escalates on capability limits or frustration | Randomized, 680,676 chats: duration -16.8% in eligible chats; repeat contact not significantly changed; ratings -0.412 (independent, one Alibaba co-author) | A | ARXIV-WANG-2026 |
| Klarna | Fintech | Assistant handles service chats; a live agent remains available | Two-thirds of chats; under 2 vs 11 minutes; repeat inquiries -25% in month one (self-reported; method not given) | A | KLARNA-AIASSISTANT-2024 |
| Klarna, 2025 | Fintech | CEO said the firm was hiring human service staff again after AI gave "lower quality" | Statement, no metric (self-reported, via press) | B | ENTREPRENEUR-KLARNA-2025 |
| NS&I | Financial services | Voice assistant answers all inbound calls; escalates complex or sensitive issues | About 22.23% of calls contained (self-reported) | A | ATRS-NSI-2025 |
| Bank of America | Financial services | Employee assistant answers IT and other questions | IT service desk calls -50%; used by over 90% of employees (self-reported) | A | BOFA-ERICA-2025 |
| HMRC | Tax authority | Questions matched to curated answers; some escalate to web chat with transcript | 83.03% intent accuracy on a test set (self-reported; tool test, not resolution) | B | ATRS-HMRC-2025 |
| DVLA | Public sector | Chatbot collects reason and checks, then transfers to an adviser with transcript | About 300,000 users a month; accuracy figure is the supplier's generic one (self-reported) | B | ATRS-DVLA-CHATBOT-2025 |
| Lyft | Transportation | AI support assistant handles questions; agents take complex issues | Resolution time cut by over 87%; measures not defined (vendor-published) | B | LYFT-ANTHROPIC-2026 |
| Air Canada | Aviation | Website chatbot gave wrong bereavement-fare guidance | Tribunal held the airline liable (independent) | B | GUARDIAN-AIRCANADA-2024 |
| City of New York | Public sector | MyCity business chatbot | Press testing found wrong answers on rules; no error rate published (independent) | B | MARKUP-MYCITY-2024 |

**In the archetypes** (few entries carry this pattern): `tax-controversy-18` (A),
`professional-services-acceptance-risk-14` (B), `security-governance-risk-02` (B), `security-identity-access-05` (B),
`security-identity-access-18` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "What are your top 20 contact reasons, and which can be answered from an approved page?" | The bounded content that makes automation safe |
| "Which questions would be costly if answered wrongly?" | Liability exposure and the set to route to people |
| "How does a customer reach a human today, and what do you promise?" | Whether there is an off-ramp |
| "What triggers a handoff: failure count, request, risk, mood?" | Whether capability, frustration and high-risk-action triggers exist |
| "What does the person see when they take over?" | Handoff quality: transcript, facts gathered, identity status |
| "How do you define a resolved contact, and when do you count a repeat?" | Whether the metric is resolution, not containment |
| "Which actions can the agent take, and which need approval?" | Tool risk; start read-only [OPENAI-AGENTS-2025] |
| "Who reads transcripts each week, and what do they change?" | Whether monitoring exists |

## 11. Sources

- `ARS-CURSOR-2025` — Ars Technica, *Company apologizes after AI support agent invents policy*, 2025-04-17. https://arstechnica.com/ai/2025/04/cursor-ai-support-bot-invents-fake-policy-and-triggers-user-uproar/
- `ARXIV-WANG-2026` — Wang et al., *Agentic AI and Human-in-the-Loop Interventions: Field Experimental Evidence from Alibaba's Customer Service Operations*, 2026-05. https://arxiv.org/pdf/2605.14830
- `ATRS-DVLA-CHATBOT-2025` — DVLA, *Contact Centre Chatbot service* (transparency record), 2025-12-16. https://www.gov.uk/algorithmic-transparency-records/dvla-contact-centre-chatbot-service
- `ATRS-GOVUKCHAT-2025` — DSIT, *GOV.UK Chat* (transparency record), 2025-10-07. https://www.gov.uk/algorithmic-transparency-records/dsit-gov-dot-uk-chat
- `ATRS-HMRC-2025` — HMRC, *Ask HMRC online* (transparency record), 2025-06-26. https://www.gov.uk/algorithmic-transparency-records/hmrc-ask-hmrc-online
- `ATRS-MOJ-2026` — Ministry of Justice, *PolyAI / Luna* (transparency record), 2026-09-09. https://www.gov.uk/algorithmic-transparency-records/moj-polyai-slash-luna
- `ATRS-NSI-2025` — NS&I, *PolyAI* (transparency record), 2025-10-30. https://www.gov.uk/algorithmic-transparency-records/ns-and-i-polyai
- `BBC-DPD-2024` — BBC News, *DPD error caused chatbot to swear at customer*, 2024-01-19. https://www.bbc.com/news/technology-68025677
- `BOFA-ERICA-2025` — Bank of America, *A Decade of AI Innovation: Erica surpasses 3 billion client interactions*, 2025-08-20. https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/08/a-decade-of-ai-innovation--bofa-s-virtual-assistant-erica-surpas.html
- `BSI-ISO42001-2026` — BSI, *ISO/IEC 42001: AI Management System* (description), retrieved 2026-10-20. https://www.bsigroup.com/en-GB/products-and-services/standards/iso-42001-ai-management-system/
- `CFPB-CHATBOTS-2023` — CFPB, *Chatbots in consumer finance*, 2023-06-06. https://www.consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance/chatbots-in-consumer-finance/
- `ENTREPRENEUR-KLARNA-2025` — Entrepreneur, *Klarna CEO Reverses Course By Hiring More Humans, Not AI*, 2025-05-09. https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `EU-GDPR-2016` — European Union, *GDPR Art. 22*, 2016-04-27. https://gdpr-info.eu/art-22-gdpr/
- `GARTNER-CSAT-2024` — Gartner, *Survey finds 64% of customers would prefer companies didn't use AI for customer service* (n=5,728), 2024-07-09. https://www.gartner.com/en/newsroom/press-releases/2024-07-09-gartner-survey-finds-64-percent-of-customers-would-prefer-that-companies-didnt-use-ai-for-customer-service
- `GUARDIAN-AIRCANADA-2024` — The Guardian, *Air Canada ordered to pay customer who was misled by airline's chatbot*, 2024-02-16. https://www.theguardian.com/world/2024/feb/16/air-canada-chatbot-lawsuit
- `KLARNA-AIASSISTANT-2024` — Klarna, *AI assistant handles two-thirds of customer service chats in its first month*, 2024-02-27. https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
- `KLGATES-OMNIBUS-2026` — K&L Gates via National Law Review, *EU Digital Omnibus on AI enters into force*, 2026-07-31. https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force
- `LYFT-ANTHROPIC-2026` — Anthropic, *Lyft reduces customer support time by 87%* (customer story), retrieved 2026-10-20. https://www.anthropic.com/customers/lyft
- `MARKUP-MYCITY-2024` — The Markup, *NYC's AI Chatbot Tells Businesses to Break the Law*, 2024-03-29. https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-AGENTS-2025` — OpenAI, *A practical guide to building agents*, 2025-04. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `OWASP-LLM01-2025` — OWASP Gen AI Security Project, *LLM01:2025 Prompt Injection*, 2025. https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- `SALESFORCE-CRMARENA-2025` — Huang et al., Salesforce AI Research, *CRMArena-Pro*, 2025-05-24. https://arxiv.org/pdf/2505.18878
- `SIERRA-TAUBENCH-2024` — Yao et al., Sierra, *τ-bench: A Benchmark for Tool-Agent-User Interaction*, 2024-06-17. https://arxiv.org/pdf/2406.12045
