# Sales, marketing and business development

Function id `sales-marketing-bd`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:** the
evidence is thinner and more self-reported than in customer service. The one randomized set comes from an unnamed cross-border retail
platform, with sales effects from 0% to 16.3% depending on the workflow [FANG-2026]. Named in-house outbound results are
self-reported and came with 15-20 hours a week of human oversight [SAASTR-2025a]. McKinsey's 2026 survey finds revenue gains from AI
most often attributed to marketing and sales [MCKINSEY-SOAI-2026].

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

Marketing, sales and business development in any organization: insight, campaigns and content, lead management, prospecting,
qualification and pursuit, account growth, sales operations and enablement. For professional-services firms, the
professional-services `client-development`, `pursuit-proposals` and `scoping-pricing` modules cover this work in depth. No archetype
covers agencies that sell marketing or sales services; use this card.

## 2. Processes and key steps

The process list is a working grouping under the "market and sell" category of a cross-industry process framework [APQC-2015].

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| Market and customer insight | Segment; research needs and competitors; set positioning | research-synthesis, data-reporting | No measured case found |
| Marketing planning and content | Plan campaigns; write copy, images, product descriptions; publish; measure | document-production, coordination-scheduling, data-reporting | Advertising workflows showed no detectable sales effect in randomized tests [FANG-2026] |
| Lead capture and management | Capture inbound interest; enrich and score; route | transaction-processing, data-reporting | Buyers face search and information friction, especially across languages [FANG-2026] |
| Prospecting and outreach | Choose accounts; research; personalize; send and follow up | research-synthesis, client-interaction, document-production | Account research and follow-up drafting take seller time; Lumen estimates its assistant saves sellers four hours a week [MICROSOFT-2024] |
| Qualification and pursuit | Discovery; qualify; scope; quote or answer RFPs; negotiate; close | client-interaction, expert-judgment, document-production | Larger deals still need people: SaaStr's agents qualify $50-100K+ sponsorship deals, then hand them to humans [SAASTR-2025a] |
| Account management and growth | Account plans; renewals; cross-sell; relationship health | client-interaction, coordination-scheduling | No measured case found |
| Sales operations and forecasting | Keep CRM records complete; forecast; report pipeline | data-reporting, transaction-processing | Broken revenue-operations processes: SaaStr had to fix them before agents could help, and found about 1,000 leads its team never followed up [SAASTR-2025a] |
| Enablement | Customize decks and collateral; train sellers | document-production | No measured case found |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **Account research and pre-meeting preparation** ([research-brief](../patterns/research-brief.md); assist to augment; step).
  Lumen Technologies (telecom): sellers research customers, summarize 10-K reports and meetings and draft follow-ups; the company
  estimates four hours a week saved per seller, "equating to $50 million annually". Vendor-published estimate. Grade B [MICROSOFT-2024].
- **Marketing content: copy, images, push messages, product descriptions** ([draft-review-loop](../patterns/draft-review-loop.md);
  augment; step to process). Klarna (fintech) said generative AI saved $10 million in annual marketing costs and cut sales and
  marketing spend 11% in Q1 2024 (company statement relayed by press). Grade B [VERDICT-2024]. In randomized tests on an unnamed retail
  platform, product-description and search workflows lifted sales about 2-3% and advertising workflows showed no detectable effect.
  Academic authors; two consulted for the platform and one is its employee. Grade B [FANG-2026].
- **Service representatives turned sellers with an on-screen assistant** ([grounded-knowledge-assistant](../patterns/grounded-knowledge-assistant.md);
  augment; process). Verizon (telecom): the consumer group CEO said sales through the 28,000-person service team were up nearly 40%
  since deployment; no definition or causal design. Self-reported via press. Grade B [REUTERS-2025].
- **Proposal and RFP drafting from an approved content library**
  ([grounded-knowledge-assistant](../patterns/grounded-knowledge-assistant.md); augment; step). Archetype entry
  `professional-services-pursuit-proposals-01` (B).

**Automate the flow**

- **Calls and emails captured into the CRM with next steps and contacts created**
  ([bulk-transformation](../patterns/bulk-transformation.md); automate; step). SaaStr (B2B events and media) describes it as a "data
  quality revolution"; no measure. Grade B [SAASTR-2025b]. Archetype: `professional-services-client-development-01` (B).
- **Outbound sequences run by a background agent with human spot checks** (pattern `other`: an outbound agent with sampled review;
  automate; process). SaaStr: 19,847 messages in six months, a 6.7% response rate and 4% positive responses; the first 1,000 emails
  were reviewed by hand, then 20-30 minute daily spot checks. Self-reported tracked metrics; the "industry average ~3%" comparison is
  SaaStr's own claim. Grade A [SAASTR-2025a; SAASTR-2025b]. Counter-evidence: ZoomInfo's spokesperson said an AI SDR product performed
  "significantly worse" than its own SDRs in a one-month trial; Airtable said its trial was "very short" and never used in production
  (statements reported by press). Grade B [TECHCRUNCH-2025].
- **Website agent that answers, qualifies and books meetings** ([service-agent-escalation](../patterns/service-agent-escalation.md);
  automate; process). On the unnamed retail platform a pre-sale chatbot raised sales 16.3% against an automated "support
  unavailable" message, with no deterioration in returns or ratings. Platform unnamed; authors tied to it as above. Grade B [FANG-2026]. SaaStr says its inbound agent "closed over
  $1M in 90 days" (self-reported) [SAASTR-2025a].

**Delegate the outcome**

- No measured public example of an agent running a full sales cycle was found. SaaStr lets humans take over mid-conversation on its
  roughly $85,000 sponsorship deals [SAASTR-2025b].

**Reinvent the work**

- **Pricing and commercial model.** Archetype entries on moving fees from hours to outcomes: `professional-services-scoping-pricing-16`
  (B), `professional-services-scoping-pricing-20` (B). Firm-built AI tools offered to clients as relationship assets:
  `professional-services-client-development-21` (B).

**In the archetypes**: `professional-services-client-development-01` (B), `professional-services-client-development-05` (B, scheduled
opportunity scans), `professional-services-client-development-06` (B, pre-meeting briefs), `professional-services-pursuit-proposals-01`
(B), `professional-services-pursuit-proposals-06` (B, RFP requirement extraction), `professional-services-pursuit-proposals-07` (B,
go/no-go), `professional-services-scoping-pricing-05` (B), `professional-services-scoping-pricing-20` (B).

## 4. Metrics and benchmarks

- **Agent-run outbound:** messages, response rate, positive-response rate, meetings booked, revenue closed (SaaStr figures above;
  self-reported) [SAASTR-2025a].
- **Conversion and sales per consumer:** conversion rose 1-22% across randomized workflows while cart value and purchase frequency did
  not change (two authors consulted for the platform and one is an employee, per disclosures) [FANG-2026].
- **Counter-metrics that catch harm:** returns and ratings [FANG-2026]; sending-domain reputation, which needed a 2-3 week warm-up
  [SAASTR-2025b]; churn of customers who tried an AI SDR product (a former employee cites 70-80% lost; the company says retention is
  79%; not the same measure) [TECHCRUNCH-2025].
- **Oversight cost:** 15-20 hours a week to coach five agents, and $50,000-100,000 a year per specialized platform (SaaStr's figures)
  [SAASTR-2025a].
- **Cost:** $10 million annual marketing saving and an 11% cut in sales and marketing spend in Q1 2024 (Klarna statements)
  [VERDICT-2024].

## 5. Interview probes

1. "Walk me through one outbound sequence from account choice to meeting booked. Where does a person touch it?" Reveals whether AI
   sits on one step or the flow; SaaStr needed proven messaging and a defined ideal customer before agents helped [SAASTR-2025a].
2. "What does your CRM look like for the last 50 opportunities: complete, current, trusted?" Reveals data readiness; SaaStr had
   to fix broken revenue-operations processes first [SAASTR-2025a].
3. "Which number would you show your CFO, and who counts it?" Separates tracked metrics from estimates such as "hours saved equals
   dollars" [MICROSOFT-2024].
4. "What will you do with the seller hours released?" Reveals the destination for capacity; Verizon pointed freed time at selling
   [REUTERS-2025].
5. "What is the review plan for the first thousand messages, and who reads replies?" Reveals quality risk [SAASTR-2025b].
6. "Which claims about AI, customers or results appear in your marketing, and who substantiates them?" Reveals exposure to FTC action
   and to false customer claims [FTC-AICOMPLY-2024; TECHCRUNCH-2025].
7. "Do any calls, texts or voice agents reach people who have not consented?" Reveals US telemarketing consent exposure [FCC-24-17].
8. "Show me the control group." Reveals whether a result can be separated from seasonality; randomized results exist only for retail
   workflows [FANG-2026].
9. "Where do you hand a conversation to a human, and at what deal size?" Reveals the delegation boundary [SAASTR-2025b].
10. "What happened when you trialled an AI SDR product, and why did you stop or continue?" Reveals real fit [TECHCRUNCH-2025].

## 6. Guardrails

- **Substantiate claims about AI.** The FTC settled with a "robot lawyer" seller whose complaint alleged no testing against human
  lawyers' output [FTC-AICOMPLY-2024].
- **No fake reviews.** The FTC's final rule covers reviews by someone who does not exist, such as AI-generated fake reviews, with civil
  penalties for knowing violators [FTC-FAKEREVIEWS-2024].
- **Automated calls.** Calls with AI-generated voices are "artificial" under the US Telephone Consumer Protection Act and need prior
  express consent [FCC-24-17].
- **True customer claims and logos.** A prospect's lawyer cited false advertising and trademark causes of action over an unauthorized
  logo [TECHCRUNCH-2025].
- **Disclose AI interaction:** in the EU, systems that interact with people must tell them they are dealing with an AI system, at the
  latest at first interaction [EU-AIACT-ART50-2024]. The AI Omnibus adds a grace period to 2 December 2026 for some transparency
  duties of systems already on the market, pending publication; confirm the date before advising [AG-OMNIBUS-2026].
- **Decisions that need human judgment:** pricing and discounts; contract terms; strategic accounts and negotiations; large or complex
  deals [SAASTR-2025a; SAASTR-2025b].

## 7. Roles and how they evolve

- **Sales development shifts from sending to coaching agents:** SaaStr's two leaders spend 15-20 hours a week on it, and budget moved
  from two human SDR roles to agents [SAASTR-2025a].
- **Service representatives become sellers** "in real time", per Verizon's consumer group CEO [REUTERS-2025].
- **Marketing teams share prompts:** Lumen's marketing team built a prompt library [MICROSOFT-2024].

## 8. Sources

- **AG-OMNIBUS-2026**: Addleshaw Goddard, *EU AI Act: AI Omnibus formally adopted* (law firm briefing, 2026-07-01). https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/
- **APQC-2015**: APQC, *Process Classification Framework, cross-industry overview, v6.1.1* (professional body, 2015-07). https://www.forgov.qld.gov.au/__data/assets/pdf_file/0027/319842/apqc_pcf_ver_6.1.1-final.pdf
- **EU-AIACT-ART50-2024**: Regulation (EU) 2024/1689, *Article 50: Transparency obligations* (regulation text via artificialintelligenceact.eu, 2024). https://artificialintelligenceact.eu/article/50/
- **FANG-2026**: Fang, Yuan, Zhang, Donati, Sarvary, *Generative AI and Firm Productivity: Field Experiments in Online Retail* (academic, arXiv 2510.12049 v3, 2026-02-10). https://arxiv.org/pdf/2510.12049v3
- **FCC-24-17**: Federal Communications Commission, *Declaratory Ruling FCC 24-17 on AI technologies and unwanted robocalls* (regulator, 2024-02-08). https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf
- **FTC-AICOMPLY-2024**: Federal Trade Commission, *FTC Announces Crackdown on Deceptive AI Claims and Schemes* (regulator, 2024-09-25). https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes
- **FTC-FAKEREVIEWS-2024**: Federal Trade Commission, *Final Rule Banning Fake Reviews and Testimonials* (regulator, 2024-08-14). https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials
- **MCKINSEY-SOAI-2026**: McKinsey, *The state of AI in 2026: On the road to ROI* (survey, n=1,719, 2026-08-25). https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- **MICROSOFT-2024**: Microsoft Source, *How Lumen Technologies Is Using Microsoft Copilot* (vendor feature, 2024-07-25). https://news.microsoft.com/source/features/digital-transformation/the-only-way-how-copilot-is-helping-propel-an-evolution-at-lumen-technologies/
- **REUTERS-2025**: Reuters via AOL, *Verizon says Google AI for customer service agents has led to sales jump* (press, 2025-04-09). https://www.aol.com/news/verizon-says-google-ai-customer-120648406.html
- **SAASTR-2025a**: SaaStr, *6 Months of AI SDRs: What's Worked, How They Brought In $1M+ in 90 Days, and the Real Data* (firm, 2025-11-20). https://www.saastr.com/6-months-of-ai-sdrs-whats-worked-how-they-brought-in-1m/
- **SAASTR-2025b**: SaaStr, *SaaStr's AI Agent Playbook: How We Deployed 20+ Agents* (firm, 2025-09-25). https://www.saastr.com/saastrs-ai-agent-playbook-how-we-deployed-20-agents-to-scale-8-figure-revenue-with-single-digit-headcount
- **TECHCRUNCH-2025**: TechCrunch, *a16z- and Benchmark-backed 11x has been claiming customers it doesn't have* (press, 2025-03-24). https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have/
- **VERDICT-2024**: Verdict, *Klarna says it has cut marketing costs by $10m with GenAI* (press, 2024-05-28). https://www.verdict.co.uk/klarna-says-it-has-cut-marketing-costs-by-10m-with-genai/
