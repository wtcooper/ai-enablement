# Scoping and pricing (professional services)

Last reviewed 2026-10-19. Use cases live in `../use-cases/scoping-pricing.yaml` (23 entries). Ids are shortened here:
`#05` means `professional-services-scoping-pricing-05`. Source keys in brackets are listed in §10 and given in full in
the YAML. **Read this first:** no source anywhere reports a measured result for AI-built estimates, scopes or fee
proposals (no estimate-versus-actual, override, win-rate or margin data). The evidence is strong on **pricing models
changing because AI compresses effort**, and thin on **AI tools that do the scoping and pricing**. Most figures are
vendor-published or stated by executives to reporters. There is no grade A entry; 14 are B, 8 C and 1 D.

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

How a firm turns a client request into a scope, an effort estimate, a price model and a fee proposal, statement of
work (SOW) or engagement letter, then holds the budget and learns from the result. It also covers the question AI
forces onto every fee: when AI makes the work faster, who keeps the saving, and what is the firm now charging for.
Examples come from law, consulting, accounting and tax, IT services and in-house legal teams (buyers). Firm-level
rates, realisation and AI return on investment sit in firm-finance; time capture to cash sits in billing-collections.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Scope capture | Turn a request, RFP or call into scope, assumptions and exclusions | client-interaction, research-synthesis | Senior people write scope documents by hand from transcripts (`#01`) |
| Effort estimate and budget | Effort by phase and staffing mix, usually from past matters or templates | data-reporting | Priced by habit: 35% default to standard rates, 28% copy a past matter unchanged (law) [BIGHAND-LF-2026] |
| Price-model choice | Hourly, capped, fixed, value, subscription, outcome-linked or hybrid | expert-judgment | Hours stop tracking effort once AI is used; outcome fees need attribution [STANFORD-DEL-2026] |
| Fee proposal, SOW, engagement letter | Draft the commercial document, now with AI-use and AI-cost terms | document-production | Deal context re-keyed by hand (`#05`); letters silent on AI use and cost (`#07`) |
| Negotiation and value conversation | Agree fee, discounts, client guidelines | client-interaction | Clients ask for AI savings; firms are "still gathering the data" [TRI-LEGALWEEK-2026] |
| Approval and reasonableness check | Partner or pricing sign-off; fee-rule and disclosure check | review-assurance | State bar positions on AI-assisted flat fees diverge (§6) |
| Budget monitoring and change control | Track work in progress (WIP) against budget, re-scope | data-reporting, coordination-scheduling | 23% of law firms actively monitor budgets throughout the matter [BIGHAND-LF-2026] |
| Post-matter review | Realisation (share of worked value collected), AI effect on effort | data-reporting | AI cost cannot usually be attributed to a project [BLOOMBERGTAX-PRICING-2026] |
| Pricing the firm's own AI products | Subscription, licence or per-document prices for productised services | expert-judgment | No published prices, uptake or margins (`#21`-`#23`) |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns an
outcome), reinvent (the service, pricing or operating model changes). **Automate has no evidence in this module. Delegate
appears only inside new service models (`#21`, `#22`), never as an agent that owns scoping or pricing.** For pricing-model
entries the ladder value is nominal: AI changes the delivery effort, not the pricing step.

**Scoping and estimating**
- Improve: `#01` Spaulding Ridge and Diabsolut (consultancies) draft solution architectures and scoping documents from
  transcripts with Certinia agents: roughly 80 hours to under 20; documentation time cut 70% (vendor-published, B).
  `#02` PSA (professional services automation) agents build estimates from prior-engagement actuals (vendor-described,
  C). `#03` law-firm fee proposals and budgets from comparable past matters (Ayora, Narrative, August; pricing job
  postings at three US firms; C).

**Price setting and the fee proposal**
- Improve: `#04` Goodwin (law) benchmarks fixed-fee quotes against anonymised market ranges with PERSUIT; buyers see
  the same data (B). `#05` Neocol's sales team went live on an SOW-drafting agent in nine days (vendor-published, B).
- Improve (rule-driven): `#06` hourly matters budgeted and billed on actual AI-assisted time; Norton Rose Fulbright
  (law) bills hours actually worked and redirects recovered time (B). `#07` fee agreements state AI use, client approval
  and AI-cost treatment; consumption-priced AI as a variable matter cost is an idea (C).
- Reinvent (idea): `#14` choose the fee structure by how observable outcomes and costs are; design baselines and
  attribution before any outcome fee (Stanford framework, D).

**Negotiation, client demands and buyer terms**
- Improve (process): `#10` partners lead the AI-value conversation before conceding on fees (TRI survey, C). `#11`
  in-house teams write AI-savings terms into outside-counsel guidelines; KPMG pressed its auditor into a 14% fee cut
  (B; audit detail in assurance-acceptance-independence-21). `#12` public-sector buyers: Deloitte Australia repaid a
  final instalment after AI errors; Australia will ask panel suppliers to declare planned AI use in quotes (B).

**Budget monitoring and value evidence**
- Improve (process): `#08` predictive alerts on matters heading over budget (vendor-described, C). `#09` matter-level
  evidence of AI use and savings; Legora and Laurel draft time entries from AI work, with value measures announced (C).

**Pricing and service model (reinvent)**
- Law: `#15` flat fees and alternative fee arrangements (AFAs: any fee not based on hours) with AI savings priced in (C).
  `#18` Kopka Law's KPI-based retainer for insurance defence (B). `#21` AI-native firms Falcon and Crosby sell flat
  bundles or per-document rates with lawyer sign-off (delegate, B). `#23` Debevoise, A&O Shearman and Cooley license or
  share firm-built AI tools; STAAR 2.0 reported as a subscription (B).
- Accounting and tax: `#16` RSM, KPMG, PwC developing value pricing; RKL piloting it with several dozen clients (B).
  `#22` PwC One: agents do the work, professionals review; subscription or consumption pricing "may" follow (delegate, B).
- Consulting and IT services: `#19` McKinsey says about a quarter of global fees are outcome-based (B). `#20` TCS says
  about 80% of one segment's contracts use outcome measures; reported savings-split deals (B).
- Cross-cutting: `#13` Wipfli moves staff metrics to cycle time and client satisfaction (B). `#17` deciding where the
  AI time dividend goes: pass on, keep, resell or "Elevate" (C).

**Held elsewhere (do not duplicate):** audit fee pressure and pricing from acceptance data
(assurance-planning-risk-assessment-23, assurance-acceptance-independence-09 and -21); fixed-fee SOC bundles
(assurance-soc-attestation-14); tax value or fixed-fee pricing (tax-compliance-corporate-16,
tax-compliance-individual-business-22, tax-controversy-10, tax-research-advisory-25); platform-plus-experts fixed prices
(tax-transfer-pricing-22).

## 4. Interview probes

Ask a managing partner, pricing director, practice leader, CFO or legal-operations lead. Expect "we don't measure that"
on AI effects; note who would know.

1. **"Last year, what share of fees were hourly, capped, fixed, subscription or outcome-linked, and which way is it
   moving?"** Reveals the starting model and whether `#15`-`#20` are relevant or remote.
2. **"When AI cuts the effort on repeatable work, who keeps the saving today, who decided, and what does the client
   see?"** Reveals whether the time dividend is a decision or an accident (`#17`); most firms have no stated rule.
3. **"How do you estimate effort now: past matters, templates or judgment? When did you last update staffing
   assumptions for AI, and have you compared AI-assisted estimates with actuals?"** Reveals data readiness for `#02`,
   `#03` and the missing estimate-accuracy evidence.
4. **"Where do matter or project actuals live (time, cost by phase, outcomes), and could a tool or a client use them to
   propose a baseline price?"** Reveals the gating capability: clean actuals (`#03`, `#08`, `#15`).
5. **"For one recent matter, could you show the client what AI changed in hours, turnaround or quality? From which
   system?"** Reveals readiness for client questions (`#09`, `#11`).
6. **"Which clients have guidelines on AI use, permission, line items or pass-through? How do you handle clients who
   give opposite instructions?"** Reveals buyer pressure and compliance exposure (`#11`, `#07`).
7. **"Which fee rules apply to you (state bar, AICPA contingent-fee limits, IRS Circular 230), and who checks a proposal
   against them before it goes out?"** Reveals whether flat-fee and AI-cost decisions have an owner (`#06`, `#07`, §6).
8. **"Where you have offered outcome-linked fees, who set the baseline, who judges the result, and how did you decide
   attribution was clean enough?"** Reveals whether `#14`, `#19` and `#20` are workable or wishful.
9. **"How are partners and staff paid and promoted: hours, revenue, margin, client satisfaction?"** Reveals the main
   internal brake on pricing change (`#13`).
10. **"Do partners raise AI with clients before the client does? What do they say first: value or discount?"** Reveals
    the conversation gap (`#10`); TRI finds most do not.
11. **"Do you sell, or plan to sell, anything clients use without a professional in the loop? How would you price and
    insure it?"** Reveals appetite for `#21`-`#23` and unanswered liability questions.
12. **"What do you pay for AI tools (per seat or per use), and does any of it reach a client invoice?"** Reveals cost
    treatment and exposure to consumption pricing (`#07`).

## 5. Metrics and benchmarks

**Client pressure (law and corporate buyers)**
- 78% of corporate clients call AI-enabled quality gains very important or essential; 6% say most or all providers
  deliver them; 32% have reconsidered or plan to reconsider providers within 12 months (1,816 professionals,
  Mar-Apr 2026) [TR-FOP-2026].
- ACC-Everlaw (657 in-house legal professionals, 30 countries, 2025): 59% see no GenAI savings from law firms yet; 61%
  plan to push for change in delivery and pricing; 64% expect to bring more work in-house [ACCEVERLAW-2025;
  BLOOMBERGLAW-ACC-2025]. Vendor co-published.
- KPMG's audit fee from Grant Thornton fell about 14% after it argued AI should cut the work [YAHOO-KPMG-2026].

**How firms price today**
- BigHand (800+ legal-finance professionals, UK and North America; vendor): 35% default to standard rates, 28% copy a
  past matter, 1% use pricing-tool templates; on AI savings 30% keep the margin, 30% still evaluating, 25% discount when
  clients permit AI; 49% see rising AFA demand; 23% actively monitor budgets [BIGHAND-LF-2026].
- 54% of UK law firms expect more fixed-fee billing in the next 12 months (Clio, via CMS) [CMS-TRENDS-2026].
- Tax firms: 78% bill hourly; return preparation earns a 28% margin versus 20-24% for advisory [TRI-CHARGING-2026].
- AICPA 2025 survey (1,000+ firms): median net hourly rate up nearly 7% in two years to $170 [BLOOMBERGTAX-PRICING-2026].
- McKinsey: about a quarter of global fees outcome-based, a self-reported rough figure [BI-MCKINSEY-2025]. TCS: about
  80% of one segment's contracts on outcome measures [REUTERS-ITSERVICES-2026].

**Rates are rising, not falling (law, not attributed to AI by any source)**
- Q1 2026: Am Law 100 worked rates up nearly 10%, demand up 2.7%, Law Firm Financial Index flat at 55 [TRI-LFFI-Q1-2026].
- Profit per lawyer 8.4% and fees worked per lawyer 16.8% above pre-2022 levels by end-2025, mostly from rate rises
  [TRI-SOTLM-2026]. Citi H1 2026: demand for lawyer hours up 4.2% against a normal of about 1.5% [BLOOMBERG-AICOST-2026].

**AI value and readiness**
- 84.8% of 245 services firms say AI saves time; the share saying it generates revenue is gated; 43.6% of projects use
  AI, up from 23.1% [SPI-AI-2026]. 38% of 896 architecture and engineering firms report measurable benefit
  [DELTEK-CLARITY-2026].
- 7.3% of resource managers have outcome data routinely in staffing; about 1 in 2 are unsure their firm will adopt
  outcome pricing (vendor-commissioned) [KANTATA-RMI-2026].
- Law-firm AI policy: 8%-38% of firms (by size) require client approval before generative AI use [ILTA-TECHSURVEY-2026].

**Tool claims (vendor-published, no named customer for the figure):** proposal or SOW time 8 hours to 1
[CERTINIA-VEDA-2026]; realisation up 2-4% and about 10% more work won [NARRATIVE-ILTA-2026].

**What to measure (recommend; nobody publishes these yet):** estimate-versus-actual variance on AI-assisted work;
share of fees by pricing model; realisation and write-offs by model; request-to-proposal cycle time; win rate by
model; how often people override a tool's suggested price; share of AI time savings passed to clients.

## 6. Guardrails

**Hourly fees (US legal ethics, converging).** Bill only time actually spent; time saved by AI cannot be billed
[ABA-OP512-2024; DCBAR-OP388-2024; TXETHICS-OP705-2025; NCBAR-FEO1-2024; CALBAR-GENAI-2026]. North Carolina's example:
three hours of drafting that now takes one cannot be billed as three. Time spent crafting inputs and reviewing outputs
is billable [CALBAR-GENAI-2026; TXETHICS-OP705-2025]. US tax practitioners: billing unspent manual time may breach the
fee rule [IRS-OPR-2026].

**Flat and value fees (diverging; check the state).** California: flat fees may build in AI savings; fee agreements
should say how far AI factors into rates [CALBAR-GENAI-2026]. ABA 512, as quoted: charging the same flat fee when AI
makes work much faster may be unreasonable [TRI-ABA512-2025]. Virginia LEO 1901 (approved 24 Nov 2025): reduced time
does not mean a proportionally reduced fee; explain the fee basis [VSB-LEO1901-2025]. North Carolina: allowed if not
clearly excessive and the client consents [NCBAR-FEO1-2024].

**AI costs.** General AI subscriptions are overhead; matter-specific costs only with disclosure, at actual cost, no
markup without informed written consent [CALBAR-GENAI-2026]; Texas caps recovery at the amount paid
[TXETHICS-OP705-2025].

**Accounting.** AICPA Code 1.510.001 bars contingent fees for audit, review, certain compilation and prospective
financial information clients, and for tax-return preparation for any client; 1.230.030 limits how other services
influence the attest fee [AICPA-CODE-2026]. Outcome pricing cannot be copied from consulting. Detail: assurance and tax.

**Buyers.** A lawyer must follow client guidelines that restrict AI [CALBAR-GENAI-2026]. Australia will require panel
suppliers to declare planned AI use in quotes; consultants stay fully responsible [CANBERRATIMES-APSAI-2025]. No
consulting fee rule equivalent to the legal and accounting rules was found.

**Steps that need human judgment:** the final price and its reasonableness; whether and how to disclose AI use; which
AI costs reach the client; outcome baselines, attribution and who judges results; re-scoping triggers; acceptance of
client AI terms; partner sign-off on every fee proposal and SOW (`#05` and `#02` describe no review step).

## 7. Roles and how they evolve

- **Pricing professionals** combine modelling with AI and analytics tools and coach partners; postings at McDermott Will
  & Schulte, Husch Blackwell and Pillsbury ask for this [MCDERMOTT-JOB-2026; HUSCH-JOB-2026; PILLSBURY-JOB-2026]. The
  role moves toward a commercial, client-facing one; some firms hired more pricing staff [TRI-PRICINGPROS-2024].
- **New senior titles** speak for firms on AI value: Chief Pricing and Innovation Officer (Greenberg Traurig), AI
  innovation head (DLA Piper) [TRI-LEGALWEEK-2026]; Managing Director, Client Value (Goodwin) [GOODWIN-PERSUIT-2025];
  chief client value and innovation officer (Norton Rose Fulbright) [BLOOMBERGLAW-TEXAS-2026].
- **Partners** are the "commercial transmission mechanism" for billing strategy, yet many do not raise AI with clients
  [TRI-STANDOUT-2026]. PwC's US CEO said partners who resist AI "have no place at the firm" [CPAPA-PWC-2026].
- **Incentives**: Wipfli adds cycle time and client satisfaction [BLOOMBERGTAX-PRICING-2026]; PwC bonuses reported to
  track revenue and margin per professional (secondary) [RESULTSENSE-PWC-2026].
- **Resource managers** expect to shift from filling hours to maximising delivery success if outcome pricing grows
  [KANTATA-RMI-2026].
- **Juniors**: under AFAs work goes to the cheapest effective resource, which can cut training unless designed for
  [ILTA-PULSE-2025]; clients resist paying for junior-completed tasks [TRI-LAWYERDEV-2026]. Route to talent-learning.
- **Delivery models**: AI-native firms cast lawyers as reviewers and agent managers [CROSBY-SITE-2026]; TCS adds engineers
  embedded with clients [REUTERS-ITSERVICES-2026].

## 8. Frontier

- 2025-10-07: Deloitte to repay part of an AUD 440,000 Australian contract after AI-generated errors [CTV-DELOITTE-2025].
- 2025-11-13: Australia's Public Service AI plan sets AI-use declarations for consulting panels [CANBERRATIMES-APSAI-2025].
- 2025-11-17: McKinsey says about a quarter of fees are outcome-based [BI-MCKINSEY-2025].
- 2025-11-24: Virginia approves LEO 1901 on reasonable fees with generative AI [VSB-LEO1901-2025].
- 2025-12-17: Goodwin rolls out fixed-fee price benchmarking globally [GOODWIN-PERSUIT-2025].
- 2026-02: KPMG reportedly wins a 14% audit-fee cut from its auditor by citing AI [YAHOO-KPMG-2026].
- 2026-03-05: KPMG, PwC and RSM reported developing value and outcome pricing [BLOOMBERGTAX-PRICING-2026].
- 2026-03-13: Legalweek: clients ask for AI line items; some refuse to pay for AI-done work [TRI-LEGALWEEK-2026].
- 2026-03-19 to 25: PwC One introduced; CEO says some services may become subscription tools [PWC-ONE-2026; CPAPA-PWC-2026].
- 2026-04-15: Certinia launches Veda agents (estimate, SOW); August shows flat fees from billing history
  [CPAPA-CERTINIA-2026; ARTLAW-AUGUST-2026].
- 2026-05: California's revised guidance covers agentic AI and fees [CALBAR-GENAI-2026].
- 2026-06-25: Salesforce charges only for resolved cases on a help agent (software comparator) [SALESFORCE-AGENTFORCE-2026].
- 2026-08-21: Reuters reports outcome-based contracts spreading in Indian IT services [REUTERS-ITSERVICES-2026].
- 2026-08-23: Stanford framework: AI pushes consulting toward hybrid and asset-based pricing [STANFORD-DEL-2026].
- 2026-09-04: seat-to-consumption AI vendor pricing a hallway topic at ILTACON [EDISCOVERYTODAY-ILTACON-2026].
- 2026-09-17: BigHand: 63% of firms price by habit [BIGHAND-LF-2026].
- 2026-10-02: Falcon launches a flat-fee AI-native law firm [NONBILLABLE-FALCON-2026].
- 2026-10-13: Legora and Laurel announce AI-work time capture with value measures to follow [LEGORA-LAUREL-2026].
- Scheduled, not evidence: TRI's 25th Law Firm COO & CFO Forum, 21-22 Oct 2026 [TRI-EVENTS-2026].

## 9. Common objections

- **"Clients still pay by the hour; why change?"** True for now: rates rose nearly 10% in Q1 2026 [TRI-LFFI-Q1-2026], and
  panellists expect the billable hour to last at least five years [TRI-ILTACON-2025]. But 32% of corporate clients are
  reconsidering providers [TR-FOP-2026], and TRI warns firms using AI mainly to justify higher rates are exposed if
  budgets tighten [TRI-SOTLM-2026]. Offer hybrid options before clients demand them.
- **"If AI halves the work, we must halve the fee."** Not necessarily. On hourly matters, yes [ABA-OP512-2024]. On flat or
  value fees, California and Virginia allow the fee to reflect value and skill [CALBAR-GENAI-2026; VSB-LEO1901-2025];
  ABA 512 as quoted is stricter, so check the state and document the basis.
- **"Outcome pricing is the answer."** Only where results can be attributed to your work; elsewhere hybrid is the
  resting point [STANFORD-DEL-2026]. McKinsey's own AI leader says its outcome model predates AI [BI-MCKINSEY-2025].
- **"We can't measure AI savings."** Nobody can yet [TRI-LEGALWEEK-2026]; that is the gap. Start with time records that
  tag AI work and value measures clients care about: turnaround, consistency, risk found (`#09`) [TRI-STANDOUT-2026].
- **"Fixed fees on AI-assisted work are too risky."** The risk is real: Tech Mahindra declined to guarantee prices on
  assumed 70-80% gains, and Infosys walked away from uneconomic contracts [REUTERS-ITSERVICES-2026]. Kopka Law says AFAs
  built only to save clients money fail [TRI-KOPKA-2026]. Use phase-based scoping and re-scoping triggers [TRI-ILTACON-2025].
- **"Hold the price; AI makes our work better."** Clients disagree so far: 6% say most providers deliver AI quality gains
  [TR-FOP-2026]; nearly 60% of in-house teams see no savings [BLOOMBERGLAW-ACC-2025]. Premium holds only if clients see value.
- **"Our people are paid on hours."** Then pricing will not move. Wipfli is changing metrics [BLOOMBERGTAX-PRICING-2026];
  TR says mismatched billing and performance frameworks undermine AI strategy [TR-FOP-2026].
- **"Discounting AI work is the easy answer."** Leading with discounts can train clients to expect them; lead with what
  changed for the client [TRI-STANDOUT-2026].
- **"Clients contradict themselves."** They do: some demand AI savings, others ban AI without permission
  [TRI-LEGALWEEK-2026]. Follow the restrictive guideline [CALBAR-GENAI-2026] and set the terms first (`#10`).

## 10. Sources

Full details (title, URL, date, locator, access) are in the YAML. Keys not in the YAML are marked *.

- **Regulators, standard-setters, professional bodies:** CALBAR-GENAI-2026, ABA-OP512-2024, TRI-ABA512-2025 (quotes ABA
  512), DCBAR-OP388-2024, TXETHICS-OP705-2025, NCBAR-FEO1-2024, VSB-LEO1901-2025, IRS-OPR-2026, AICPA-CODE-2026,
  ILTA-TECHSURVEY-2026, ILTA-PULSE-2025, ICAEW-EXPECT-2026, ABA-LPMRFP-2026.
- **Academic and surveys:** STANFORD-DEL-2026, TR-FOP-2026, TRI-STANDOUT-2026, SPI-AI-2026, BIGHAND-LF-2026,
  ACCEVERLAW-2025, KANTATA-RMI-2026, FORRESTER-TECHSVCS-2026, TRI-SOTLM-2026, TRI-LFFI-Q1-2026* (Thomson Reuters
  Institute, Q1 2026 LFFI, 2026-05-13), DELTEK-CLARITY-2026* (Deltek Clarity A&E study, 2026-05-12),
  BLOOMBERG-AICOST-2026* (Bloomberg Law, Big Law AI cost savings column, 2026-09-03).
- **Firms:** GOODWIN-PERSUIT-2025, PWC-ONE-2026, CROSBY-SITE-2026, CMS-TRENDS-2026, DEBEVOISE-BLOOMBERG-2026,
  COOLEY-LAWCOM-2026.
- **Vendors:** CERTINIA-VEDA-2026, CERTINIA-CUSTOMERS-2026, AYORA-LTH-2026, NARRATIVE-ILTA-2026, LTHUB-PERSUIT-2026,
  LEGORA-LAUREL-2026, LEGORA-PORTAL-2026, SALESFORCE-AGENTFORCE-2026.
- **Conference coverage:** TRI-LEGALWEEK-2026, TRI-ILTACON-2025, EDISCOVERYTODAY-ILTACON-2026, TRI-EVENTS-2026* (Thomson
  Reuters Institute events page, read 2026-10).
- **Press and commentary:** BI-MCKINSEY-2025, AIWEEKLY-MCK-2026, RESULTSENSE-2026, RESULTSENSE-PWC-2026,
  RESULTSENSE-ACCENTURE-2026, FORRESTER-BLOG-2025, REUTERS-ITSERVICES-2026, BLOOMBERGTAX-PRICING-2026,
  BLOOMBERGLAW-ACC-2025, BLOOMBERGLAW-TEXAS-2026, BLAW-ROBB-2026, YAHOO-KPMG-2026, ONLYCFO-KPMG-2026, CPAPA-PWC-2026,
  CPAPA-CERTINIA-2026, ACCTODAY-PWC-2026, NEWSTACK-PWC-2026, NONBILLABLE-FALCON-2026, ARTLAW-AUGUST-2026, AL-CLIENT-2026,
  ABAJ-SHARE-2026, CTV-DELOITTE-2025, BNN-DELOITTE-2025, CANBERRATIMES-APSAI-2025, MONDAQ-GGI-2026, LEGALIO-AFA-2025,
  ATL-DEFENSE-2026, TRI-KOPKA-2026, TRI-AFA-2024, TRI-AIBIZ-2025, TRI-ALTPRICING-2025, TRI-CHARGING-2026,
  TRI-INTERDEP-2026, TRI-LEADFOLLOW-2025, TRI-LAWYERDEV-2026, TRI-PRICINGPROS-2024.
- **Job postings:** MCDERMOTT-JOB-2026, HUSCH-JOB-2026, PILLSBURY-JOB-2026.
