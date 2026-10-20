# Billing and collections (professional services)

Last reviewed 2026-10-19. Use cases live in `../use-cases/billing-collections.yaml` (17 entries). Ids are shortened here: `#05` means
`professional-services-billing-collections-05`. Source keys in brackets are in the YAML unless marked * in §10. **Read this first:** the
evidence is mostly vendor-published. No firm or in-house team publishes a measured effect of AI on time capture, pre-bill review, rejections or
collections, and no source publishes an edit, override or error rate for AI-drafted entries or firm-side bill checks (Onit's
client-side accuracy claim is vendor research with no method on the page). There is no grade A entry; 5 are
B, 9 C and 3 D (ideas). Time capture is the only step with several named deployments.

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

Time capture to cash: how a day's work becomes a time entry, a narrative and task code that meet the client's billing guidelines, a pre-bill
(proforma: the draft bill partners review), an invoice that passes the client's e-billing checks, and cash collected. It also covers the client
side: in-house legal teams reviewing the bills. Examples come mostly from law firms, then accounting and advisory firms, consulting and
project-based firms, and in-house legal teams. Firm-level realisation, profitability, AI cost and AI return sit in firm-finance; fee design and
fee-agreement terms sit in scoping-pricing.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Time capture and entry | Recall or log activity; assign client and matter | transaction-processing, data-reporting | Time rebuilt from memory, short tasks missed [LEGORA-LAUREL-2026]; daily time due by 9:00 a.m. at one accounting firm [LAUREL-WARREN-2026] |
| Narrative and task coding | Write a description and UTBMS task code (a standard legal task code set) that meet the client's rules | document-production, review-assurance | Guidelines run 15 to 100 pages per client [LAUREL-BILLING-2026]; invoices without valid LEDES or UTBMS codes are rejected [LAYER3-BILLINGOCG-2026] |
| Client guideline rules | Read each client's outside counsel guidelines (OCGs) and turn them into rules | research-synthesis, review-assurance | Rules for hundreds of clients cannot be held in memory [LEGALIT-FOLEY-2024] |
| Pre-bill review and write-downs | Partner and biller check, edit, write down and approve | review-assurance, expert-judgment | Some partners spend up to a week a month cleaning up invoices (a vendor's product lead) [LEGALIT-FOLEY-2024]; 43% of partners always or usually reduce a bill when time exceeds their own expectations [TRI-WRITEDOWNS-2023] |
| Fixed-fee scope at bill time | Compare work against the agreed scope; raise a change order or absorb | data-reporting | Overruns absorbed as write-downs at close [LAUREL-BILLING-2026] |
| Invoice and e-billing submission | Assemble the invoice; submit in LEDES format to the client's platform | transaction-processing | Rejection rate up from 11% to 18% in 2025 in Elite's data [ELITE-REJECT-2026] |
| Rejections, reductions and appeals | Find why a line was cut; appeal or resubmit | review-assurance, document-production | Billers trained on dozens of client platforms and appeals teams [TRI-KOPKA-2026]; client AI decisions opaque [ELITE-IDEA-2026] |
| Collections | Chase overdue invoices; decide whom and how | coordination-scheduling, client-interaction | No one owns receivables; 97 days to get paid (secondhand) [ABAJ-TECHSHOW-2026] |
| AI-specific billing decisions | Record, disclose and charge for AI use | expert-judgment | Clients ask about AI savings; firms "still gathering the data" [TRI-LEGALWEEK-2026] |
| Client side (in-house) | Review outside-counsel invoices against guidelines | review-assurance | Hundreds of line items make problems easy to miss [ALBERTSONS-TR-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a multi-step outcome),
reinvent (the service, pricing or operating model changes). **Automate: one thin entry (`#11`).** **Delegate: no evidence.** A chain of agents
from staffing through time to billing is described only as a concept [ILTA-RISE-2025]; in a vendor survey, 26% of accounting firms would hand
"draft and send invoices" to an autonomous agent, but none fully trusts AI yet [UKU-AIACCOUNTING-2026]. **Model-scope change: none in this
module;** the nearest are held elsewhere (below). In every entry with a named user, a person reviews before anything goes to the client (see each entry's checkpoints).

**Time capture and entry**
- Improve (process): `#01` passive capture of email, document, call and application activity drafts entries the professional reviews and
  releases. Law: Lerners, Obermayer, Tonkon Torp, Berger Singerman; accounting: Warren Averett, GHJ; an unnamed Big Four tax division (B,
  vendor-published).
- Improve (step): `#02` work done in Harvey, Legora or Litify becomes a draft entry for the lawyer (announced, C). `#12` GHJ (accounting)
  extends capture to executives and administrative staff to show cost to serve (B). `#16` consulting and project-based firms: PSA agents for
  conversational timekeeping and missing time cards (Certinia, Kantata; zeb named, function not described; C).

**Narratives, codes and client guidelines**
- Improve (step): `#03` guidelines extracted into rules and checked as each entry is written, with suggested narratives and codes (Intapp,
  Laurel, Aderant, Elite; C). `#04` Linklaters (law) built a tool that checks narratives in bulk and proposes fixes; about a thousand a minute,
  by the builder's account (B).

**Pre-bill review and write-downs**
- Improve (step): `#05` pre-bill checked against guidelines and billing history, fixes accepted with one click; Foley Mansfield (law) went
  live firmwide in 2024 (B). `#06` Elite ranks proforma edits (C). `#07` fixed-fee scope-creep flags turned into change orders before close
  (Laurel Billing, unreleased; C). `#08` idea: score pre-bills for write-down risk (D).

**E-billing, rejections and AI terms**
- Improve (step): `#09` Aderant's Appeals Agent drafts appeals and ranks which are worth pursuing (early access, C). `#14` idea: tag
  AI-assisted work in entries and check it before billing against client AI terms and fee rules (D).

**Collections**
- Improve (step): `#10` prioritise overdue accounts by payment risk and draft follow-ups (Aderant, Oddr, Certinia; C).
- Automate (step): `#11` CollBox detects unpaid bills and sends reminders, with trained human collectors for calls and escalation (law; C).

**Accounting work-in-progress to invoice**
- Improve (process): `#17` flag work-in-progress (WIP) problems early and shorten finished-work-to-bill time (Aiwyn; one unnamed firm, 29 to
  18 days, credited to visibility rather than AI; C).

**Client side (in-house)**
- Improve (process): `#13` AI audits every submitted outside-counsel invoice (vendors contrast this with sampling) and routes flagged lines; Albertsons (retail, in-house)
  recalls almost $2 million saved with AI audit plus volume discounts (B). The firm's bills are now read by the client's AI.

**Reinvent (idea)**
- `#15` a single "services rendered" invoice in place of itemised time when AI compresses tasks (Legalweek panel; D).

**Held elsewhere (do not duplicate):** OCG extraction and categorisation (professional-services-acceptance-risk-10) and the matter-opening
register of client AI restrictions (professional-services-acceptance-risk-11); hourly billing on actual AI-assisted time (professional-services-scoping-pricing-06);
AI cost terms in fee agreements (professional-services-scoping-pricing-07); live WIP-against-budget alerts (professional-services-scoping-pricing-08); matter-level evidence of AI
savings for clients (professional-services-scoping-pricing-09); KPI-based retainer billing at Kopka Law (professional-services-scoping-pricing-18); fee-mix strategy
(professional-services-firm-finance-01); leakage, profitability and leverage from captured time (professional-services-firm-finance-03); line-by-line bill analytics
and query layer for in-house and pricing teams (professional-services-firm-finance-04); Aderant Rates and GL Forecasting agents (professional-services-firm-finance-05); aiming AI at
written-down work (professional-services-firm-finance-06); AI cost metering by matter and pass-through (professional-services-firm-finance-12). Tax: IRS rules on billing AI-assisted
work (tax-compliance-corporate-16, tax-compliance-individual-business-22).

## 4. Interview probes

Ask a billing or finance director, a billing partner, a controller, a timekeeper, a collections lead, or a legal-operations head (in-house).

1. **"Walk me through how a day of work becomes a line on a client invoice. Where does someone rewrite, recode or write down an entry, and
   who?"** Reveals where rework sits and which step to start with (`#01`, `#03`, `#05`).
2. **"How much time goes unrecorded or rewritten today, and how do you know? Does anyone track edits to entries?"** Reveals whether there
   is a baseline; without one, no capture tool's claim can be checked (`#01`).
3. **"Take the last invoice that was cut or rejected. Who found the problem, how long after the work, and what did it cost in write-down
   and delay?"** Reveals the cost of late checks (`#05`, `#09`).
4. **"Which client guidelines cause most rejections or reductions? Where are they held, and how do changes reach timekeepers and
   billers?"** Reveals readiness for rules at entry (`#03`; professional-services-acceptance-risk-10).
5. **"Where are write-down decisions actually made, by the billing team or the partner? Can you see write-down rates by client, practice
   and timekeeper?"** Reveals whether `#08` or professional-services-firm-finance-06 is feasible.
6. **"When AI shortens a task, what do the time entry and invoice show, and who decides? What do your engagement letters and your
   jurisdiction's rules say?"** Reveals exposure on AI-assisted billing (`#02`, `#14`; §6).
7. **"Which clients' guidelines mention AI (disclosure, no pass-through, approved tools, expected savings), and how do those terms reach
   the people who write entries and assemble bills?"** Reveals whether `#14` is needed now.
8. **"If a tool captured time from email, documents and calls, what would your data protection officer, employee representatives and
   clients say, and who decides?"** Reveals the monitoring question before any `#01` pilot (§6).
9. **"How many days pass from work done to cash at each stage: capture, pre-bill, issue, client approval, payment? Which would you measure
   first?"** Reveals where cash is stuck (`#10`, `#11`, `#17`).
10. **"Where does collections lose time: chasing, prioritising, or finding why a payment is stuck? What would you need to trust a drafted
    follow-up?"** Reveals fit for `#10`.
11. **"What share of your invoices go through a client's automated review, and do you know what it looks for?"** Reveals exposure to
    client-side AI (`#13`) and the case for pre-bill checks (`#05`).
12. **"On fixed-fee work, when do you learn a matter has run past scope: during the work or at the bill?"** Reveals fit for `#07`.

## 5. Metrics and benchmarks

**Time capture (vendor-published customer stories; no baselines or methods)**
- Lerners (law) +0.48 billable hours per lawyer a day; the Firm Chair recalls dockets falling from 30-45 minutes to about five
  [LAUREL-LERNERS-2026]. Tonkon Torp (law) 21 minutes a day (20 in the body text), about $20,000 more revenue per timekeeper a year, 20% faster
  collection cycle [LAUREL-TONKON-2026]. Berger Singerman (law) nearly 15 minutes a day; entries about two days faster [LAUREL-BERGER-2026]. GHJ
  (accounting) 0.42 hours a day [LAUREL-GHJ-2026]. Unnamed Big Four tax division +2.3 chargeable hours a week against a random control group
  [LAUREL-BIGFOURTAX-2026].
- Unrecorded time, vendor sizing on different bases: Laurel estimates 10-30% of billable work never reaches an invoice [TR-LAUREL-2026];
  Litify up to 30% [LAWSITES-LITIFY-2026]; Laurel's 11% is of unsubmitted time, not of billable work [LAUREL-SOW-2025].

**E-billing and rejections (Elite data, about 400 law firms, vendor-published)**
- Rejection rate 11% to 18% in 2025, which Elite links to client AI review as an inference; 71% of firms manage guideline compliance mainly
  by hand; days to payment for eBillingHub customers fell from 62 to 50 [ELITE-REJECT-2026]. Largest fee-reduction categories: rate deviation
  or unapproved rate 23.88%, administrative or clerical work 15.98%, vague description 7.57%, excessive or unsupported time 7.33%
  (count or value not stated) [ELITE-IDEA-2026].

**Realisation and write-downs (Thomson Reuters Institute data; TRI belongs to a group that sells legal AI)**
- Worked realisation (share of standard rates realised) up to 95% at firms with disciplined pricing against 75-80% with aggressive discounting;
  associates 91.5%, partners below 90%; long-term decline since 2021 [TRI-RATES-2026]. Market-standard realisation about 85% (source of the
  figure not stated) [TRI-MIDSIZE-2026].
- 2023 survey (245 respondents, firms of 11+ lawyers): the average partner wrote off over 300 hours of their own potentially billable time
  after it was reported, nearly $190,000 of fees per partner [TRI-WRITEDOWNS-2023].

**Cash cycle (secondhand)**
- Wells Fargo H1 2026 (140+ firms): inventories +17.7%, collection cycles slowed by 5%, unit not defined [LAWFUEL-WF-2026]. Clio figures
  relayed by Oddr: about 88% of billable work invoiced, about 93% of invoices collected, 43 days to bill and 32 to collect [ODDR-82CENTS-2026].

**Tool claims (vendor-published unless stated)**
- Verify: about 6% of revenue otherwise written off recovered, about 50% less pre-bill review time [LEGALIT-FOLEY-2024]. Laurel: 30-40% less
  pre-bill review at one unnamed customer [LAUREL-BILLING-2026]. Intapp: 75% faster time-entry release; 40% faster revenue cycles, 10% fewer
  write-offs [INTAPP-TIME-2026; INTAPP-TIMEBILL-2026]. Elite: up to 4 hours a month per lawyer on proformas, expected [CFOTECH-ELITE-2026].
  Certinia: 24 days faster from delivery to payment [CERTINIA-VEDA-2026]. Linklaters: about 1,000 narratives a minute, self-reported
  [NONBILLABLE-LINKLATERS-2025].
- Client side: Onit claims 92% invoice-level and 81% line-item accuracy against 72% and 43% for experienced lawyers [ONIT-SPEND-2026];
  Wolters Kluwer up to 10% lower spend [WK-LEGALSPEND-2026]; Albertsons almost $2 million year to date, recalled, combined with volume discounts
  [ALBERTSONS-TR-2026]. Nearly 60% of about 650 in-house respondents saw no noticeable savings from firms' AI yet [BLOOMBERGLAW-ACC-2025];
  68% of corporate legal professionals did not know whether their firms use AI [TRI-GREATDISCONNECT-2026].
- Accounting (vendor survey): 15% name slow or inaccurate billing as their biggest headache (missing deadlines lead, 32%); 62% say
  trust depends on a human approving before anything is sent [UKU-AIACCOUNTING-2026].

**What to measure (recommended; nobody publishes these yet):** edit and override rate on drafted entries; days from work to entry, entry to
bill and bill to cash; pre-bill review hours; rejections and reductions by rule and client; write-down rate by client, practice and timekeeper;
false-flag rate of bill checks; share of AI-assisted entries and how each was billed.

## 6. Guardrails

**Hourly bills reflect time actually spent.** California, DC, Texas and North Carolina all say so, and time saved by AI cannot be billed
[CALBAR-GENAI-2026; DCBAR-OP388-2024; TXETHICS-OP705-2025; NCBAR-FEO1-2024]; California adds that time crafting prompts and reviewing output can be. Australia: billed
time must accurately represent the work done [AUSLEG-AISTATEMENT-2024]. Under ABA Formal Opinion 512 lawyers may not charge for time learning a general
AI tool [ABA-BLT-2024]. Tax: the IRS Office of Professional Responsibility says billing manual time not spent, or double billing for AI-assisted
tasks, may breach Circular 230 depending on the facts [IRS-OPR-2026]. A drafted entry (`#01`, `#02`) is a proposal; the timekeeper's review is
the control.

**Flat fees: rules differ.** California allows flat fees that build in AI savings [CALBAR-GENAI-2026]; North Carolina allows a flat fee that
is not clearly excessive with consent [NCBAR-FEO1-2024]; ABA 512, as quoted, says the same flat fee may be unreasonable if a tool makes the
work much quicker [TRI-ABA512-2025]; Virginia's LEO 1901 (approved 2025-11-24) disagrees but requires the fee basis to be explained
[VACOURTS-LEO1901-2025]. Check the lawyer's state before invoicing an AI-assisted flat fee or change order (`#07`).

**AI costs.** General AI subscriptions are overhead; matter-specific costs may be charged only if the fee agreement discloses it, at actual
cost, with no markup without informed written consent [CALBAR-GENAI-2026]; Texas limits recovery to the amount paid [TXETHICS-OP705-2025].
One Illinois bar newsletter commentary argues ordinary AI use should be absorbed as overhead [ISBA-ELEFANT-2026*]. Detail: professional-services-firm-finance-12.

**Client instructions.** California requires following client guidelines that restrict AI [CALBAR-GENAI-2026]. Zscaler's guidelines ask for
AI use to be noted in the time entry and bar passing on AI time and cost; block-billed lines are rejected (resubmit at 15% less or be paid at
10% less) and invoices more than 60 days late lose 20% [ZSCALER-OCG-2025]. Australia: record and disclose AI use and its effect on costs if the client asks [AUSLEG-AISTATEMENT-2024]. The Law Society
says the SRA has no specific generative AI guidance on use or disclosure for client care [LAWSOC-GENAI-2026].

**Worker monitoring.** Passive capture reads email, documents and calls. The UK ICO's monitoring guidance is under review [ICO-MONITORING-2026];
the EU AI Act lists AI to monitor and evaluate workers as high-risk [EU-AIACT-ANNEX3-2024], with those obligations from 2 December 2027
[EC-AIACT-2026]. Whether a time-capture tool is in scope depends on intended use; no source tests it. Vendor security claims are unverified
[LAURELSITE-2026].

**Government contracts and standards.** US federal time-and-materials vouchers need individual daily job timekeeping records or other approved
substantiation [FAR-52.232-7]; no source says whether passive capture qualifies. The UTBMS code sets have no AI-specific code [LEDES-UTBMS-2026].
**Accounting:** the AICPA Code bars contingent fees for audit, review and certain other engagements and for preparing tax returns
[AICPA-CODE-2026*], so outcome-linked billing cannot be copied into those services.

**Steps that need human judgment:** releasing each time entry; approving rules extracted from guidelines; accepting or rejecting pre-bill
fixes and write-downs; raising a change order; deciding which appeals to file; whom to chase and in what tone; what AI use to disclose and
whether any AI cost is charged; flat-fee reasonableness; for in-house teams, which invoice lines to dispute.

## 7. Roles and how they evolve

- **Timekeepers** move from writing time from memory to reviewing a system record [LEGORA-LAUREL-2026]; Lerners' Firm Chair still reviews
  and finalises her dockets [LAUREL-LERNERS-2026].
- **Billing partners** review the items AI flags instead of whole pre-bills at Foley [LEGALIT-FOLEY-2024]; Laurel's product page tells
  partners to "approve decisions, not entries" (vendor description of an unreleased product) [LAUREL-BILLINGPAGE-2026].
- **Billers and coordinators** move from re-keying partner mark-ups to approving flagged fixes [LAUREL-BILLING-2026]; Elite says billing teams
  should move from correcting rejections to preventing them [ELITE-REJECT-2026]. Kopka Law describes billers trained on dozens of client
  platforms [TRI-KOPKA-2026].
- **Risk and billing administrators** approve machine-extracted guideline rules [LAUREL-COMPLIANCE-2026; INTAPP-TERMS-2026].
- **Collectors** spend less time chasing and more on relationships and judgment calls, per Oddr [ODDR-COLLECTIONS-2026]; CollBox moves calls to
  its own trained collectors [ABAJ-TECHSHOW-2026].
- **Rollout owners:** Obermayer's controller led its rollout [LAUREL-OBERMAYER-2026]; Warren Averett has an AI Strategy Manager
  [LAUREL-WARREN-2026]; a Linklaters managing associate built its narrative checker [NONBILLABLE-LINKLATERS-2025].
- **Pricing roles:** Greenberg Traurig's Chief Pricing and Innovation Officer and DLA Piper's AI innovation lead spoke on client AI value
  [TRI-LEGALWEEK-2026].
- **In-house legal operations** focus on firm negotiations while the tool flags lines and applies discounts [ALBERTSONS-TR-2026].
- **Talent:** Kopka Law's COO says the tedium of time capture is driving talent out of defense work [TRI-KOPKA-2026]. No source reports
  headcount changes in billing or collections teams.

## 8. Frontier

- 2024-05-15: Foley Mansfield goes live firmwide with gen AI pre-bill review [LEGALIT-FOLEY-2024].
- 2025-02-11: Elite Validate announced [ELITE-VALIDATE-2025]. 2025-04-07: Zscaler's revised guidelines include an AI section [ZSCALER-OCG-2025].
- 2025-08-07: Aderant signs a deal for HerculesAI's billing-compliance assets [ADERANT-HERCULES-2025].
- 2025-10-09: Linklaters' narrative checker reported in firmwide use [NONBILLABLE-LINKLATERS-2025].
- 2025-11-24: Supreme Court of Virginia approves LEO 1901 on fees and AI [VACOURTS-LEO1901-2025].
- 2025-12-10: Certinia's Winter release flags missing time cards (early adopters) [IA-CERTINIA-2025].
- 2026-02-27: Elite Intelligence added to 3E Proforma [CFOTECH-ELITE-2026].
- 2026-03-13: Legalweek panels on AI line items, "will not pay" guidelines and a single line-item bill [TRI-LEGALWEEK-2026].
- 2026-03-26: CollBox wins ABA Techshow Startup Alley [ABAJ-TECHSHOW-2026].
- 2026-05-12: Aderant AI Agent Center (Appeals, Collections); early access 2026-08-25 [ADERANT-AGENTCENTER-2026; ADERANT-AGENTSEAP-2026].
- 2026-05-14: Elite reports rejections up to 18%; California's revised AI guidance approved [ELITE-REJECT-2026; CALBAR-GENAI-2026].
- 2026-05-21: Intapp Time adds work-code prediction and narrative compliance [INTAPP-TIMERELEASE-2026].
- 2026-08-17: Aderant iTimekeep-Harvey integration announced as live [ADERANT-ITIMEKEEPHARVEY-2026].
- 2026-08-19: Oddr AI-drafted collection emails [ODDR-COLLECTIONS-2026]; Laurel Billing announced as coming soon [LAUREL-BILLING-2026].
- 2026-09-04: move from seat-based to consumption-based AI pricing discussed at ILTACON [EDISCOVERYTODAY-ILTACON-2026*].
- 2026-10-07: Kantata launches Agent Studio; Basware named as a user [ITBRIEF-KANTATA-2026].
- 2026-10-13: Legora and Laurel: Legora tasks to become draft time entries; AI-value measures in phase two [LEGORA-LAUREL-2026].
- Scheduled: 2027-12-02, EU AI Act Annex III obligations apply [EC-AIACT-2026].

## 9. Common objections

- **"Passive time capture is surveillance."** Treat it as a privacy decision: ICO guidance and the EU AI Act apply to worker monitoring
  [ICO-MONITORING-2026; EU-AIACT-ANNEX3-2024]. Ajax offers a pause function [LAWSITES-AJAX-2025]; vendor security claims need checking
  [LAURELSITE-2026]. GHJ frames its data as understanding, not evaluation [LAUREL-GHJ-2026].
- **"AI capture just pads the bill."** The rule is actual time [CALBAR-GENAI-2026]; vendors frame the gain as recovering unrecorded work
  [LEGORA-LAUREL-2026]. No source measures whether clients pay the extra hours; nearly 60% of in-house respondents see no
  savings from firms' AI yet [BLOOMBERGLAW-ACC-2025].
- **"The numbers are marketing."** Agreed: every time-capture figure is vendor-published, some conflict (Tonkon Torp 20 or 21 minutes on
  the same page) and sizing claims use different bases (10-30% of billable work; 11% of unsubmitted time) [LAUREL-TONKON-2026;
  TR-LAUREL-2026; LAUREL-SOW-2025]. Set your own baseline and track edit rates in a pilot.
- **"Clients will reject AI-drafted narratives."** Client AI already reads invoices; rejections rose from 11% to 18% [ELITE-REJECT-2026].
  Checks at entry and before billing (`#03`, `#05`) answer it with the client's own rules.
- **"If AI makes us faster, hourly revenue falls."** On hourly work, saved time cannot be billed [TXETHICS-OP705-2025]. Perlin argues AI may
  reinforce rather than disrupt the billable hour [LEGALFUTURES-PERLIN-2025]; fee-model choices sit in scoping-pricing.
- **"Disclosing AI use invites fee cuts."** It may: some clients use firms' AI adoption as leverage to cut costs [TRI-LEGALWEEK-2026], but some clients already require it (Zscaler) and California requires
  following client AI guidelines [ZSCALER-OCG-2025; CALBAR-GENAI-2026].
- **"Collections is relationship work."** The tools leave decisions with staff [ODDR-COLLECTIONS-2026]; some post-work discounting protects
  relationships [TRI-RATES-2026]; CollBox keeps human collectors on calls [ABAJ-TECHSHOW-2026].
- **"Adoption will stall."** Lerners calls the tool an up-front investment with a getting-used-to period [LAUREL-LERNERS-2026]; Obermayer and
  GHJ switched off the legacy system [LAUREL-OBERMAYER-2026; LAUREL-GHJ-2026].
- **"This is a law-firm story."** Mostly, yes. Accounting has Warren Averett, GHJ and an unnamed Big Four tax division (`#01`), and Aiwyn's
  WIP view (`#17`); consulting evidence is thin (`#16`).

## 10. Sources

Full details (title, URL, date, locator, access) are in the YAML. Keys marked * are not in the YAML.

- **Regulators, professional bodies and standards:** CALBAR-GENAI-2026, TXETHICS-OP705-2025, DCBAR-OP388-2024, NCBAR-FEO1-2024,
  VACOURTS-LEO1901-2025, VALAWYER-2026, ABA-BLT-2024, AUSLEG-AISTATEMENT-2024, LAWSOC-GENAI-2026, IRS-OPR-2026, ICO-MONITORING-2026,
  EU-AIACT-ANNEX3-2024, EC-AIACT-2026, FAR-52.232-7, LEDES-UTBMS-2026, ILTA-RISE-2025, JOFA-CAS-2026, AICPA-CODE-2026* (AICPA Code of
  Professional Conduct through July 2026, 1.510.001, 2026-07, https://mn.gov/boa/assets/AICPA%20Code%20of%20Professional%20Conduct_tcm1233-764395.pdf),
  ISBA-ELEFANT-2026* (Elefant, MyShingle Ethics Opinion 2026-1, ISBA newsletter commentary, 2026-07, https://www.isba.org/node/104199).
- **Academic:** GEORGETOWN-PERLIN-2025, WJLTA-RAPOPORT-2025.
- **Surveys and market data:** TRI-RATES-2026, TRI-WRITEDOWNS-2023, TRI-GREATDISCONNECT-2026, ILTA-TECHSURVEY-2026, UKU-AIACCOUNTING-2026.
- **Client documents (in-house):** ZSCALER-OCG-2025.
- **Conference coverage:** TRI-LEGALWEEK-2026, ABAJ-TECHSHOW-2026, KARBON-ENGAGE-2026, EDISCOVERYTODAY-ILTACON-2026* (eDiscovery Today,
  2026-09-04, https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/).
- **Press:** TRI-KOPKA-2026, TRI-MIDSIZE-2026, TRI-ROI-2025, TRI-ABA512-2025, LEGALIT-FOLEY-2024, NONBILLABLE-LINKLATERS-2025,
  CFOTECH-ELITE-2026, LAWFUEL-WF-2026, BLOOMBERGLAW-ACC-2025, LEGALFUTURES-PERLIN-2025, LAWSITES-AJAX-2025, LAWSITES-LAUREL-2026,
  LAWSITES-BILLABLESAI-2025, ITBRIEF-KANTATA-2026, SILICONANGLE-CERTINIA-2026, IA-CERTINIA-2025, ACCTODAY-BLUEJ-2026.
- **Vendors:** Laurel (LAUREL-LERNERS-2026, LAUREL-OBERMAYER-2026, LAUREL-TONKON-2026, LAUREL-BERGER-2026, LAUREL-WARREN-2026,
  LAUREL-GHJ-2026, LAUREL-BIGFOURTAX-2026, LAUREL-AMLAW200-2026, LAUREL-ALLENS-2026, LAUREL-WSGR-2026, LAUREL-FOSTERS-2026,
  LAUREL-TIMESHEETS-2026, LAUREL-SOW-2025, LAUREL-BILLING-2026, LAUREL-BILLINGPAGE-2026, LAUREL-COMPLIANCE-2026, LAUREL-TR-2026,
  LAURELSITE-2026), LEGORA-LAUREL-2026, TR-LAUREL-2026, Intapp (INTAPP-TIMERELEASE-2026, INTAPP-TIME-2026, INTAPP-TIMEBILL-2026,
  INTAPP-TIMEKEEPING-2026, INTAPP-TERMS-2026, INTAPP-BILLSTREAM-2026), Aderant (ADERANT-AGENTCENTER-2026, ADERANT-AGENTSEAP-2026,
  ADERANT-ITIMEKEEPHARVEY-2026, ADERANT-HARVEY-2025, ADERANT-HERCULES-2025), Elite (ELITE-VALIDATE-2025, ELITE-REJECT-2026, ELITE-IDEA-2026),
  FULCRUM-ILTACON-2026, LAWSITES-LITIFY-2026, ODDR-COLLECTIONS-2026, ODDR-82CENTS-2026, CERTINIA-VEDA-2026, CERTINIA-CUSTOMERS-2026,
  NTTDATA-ZEB-2026, AIWYN-2026, ALBERTSONS-TR-2026, BRIGHTFLAG-AIINVOICE-2025, BRIGHTFLAG-AI-2026, BRIGHTFLAG-NEXTGEN-2024, ONIT-SPEND-2026,
  WK-LEGALSPEND-2026, MILLIMAN-BILLREVIEW-2026, LAYER3-BILLINGOCG-2026, LAYER3-OCG-2026, EVERLAW-BLOG-2026.
