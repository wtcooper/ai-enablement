# Firm finance and performance (professional services)

Last reviewed 2026-10-19. Use cases live in `../use-cases/firm-finance.yaml` (17 entries). Ids are shortened here: `#05` means
`professional-services-firm-finance-05`. Source keys in brackets are listed in §10; keys marked * there are not in the YAML. **Read this first:** no
firm or in-house team publishes a measured effect of AI on rates, realisation, margin, partner income or return on AI spend. Spending is measured;
return is not. Most figures are self-reported by firms, vendor-published, or Thomson Reuters Institute (TRI) data (TRI belongs to a group that sells
legal AI). There is no grade A entry; 9 are B, 7 C and 1 D (idea).

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

How a firm runs its own economics as AI changes the work: the fee mix and annual rate round, realisation (the share of worked value actually
collected) and write-downs, matter profitability and leverage (hours of juniors relative to equity partners), AI investment and its return, AI costs
that are turning from per-seat licences into usage-based (consumption) charges, partner economics, and outside capital. Examples come from law,
accounting, consulting and in-house legal teams. Deal-level scoping and fee design sit in scoping-pricing; time capture to cash sits in
billing-collections.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Fee-mix strategy | Decide the share of hourly, fixed, hybrid, subscription and outcome-linked fees | expert-judgment | About 90% of legal dollars still hourly [TRI-SOTLM-REPORT-2026]; efficiency lowers hourly revenue |
| Annual rate round | Set standard rates and discount policy; watch worked rates | expert-judgment, data-reporting | Rates rise faster than visible value; LFFI flat at 55 in Q1 2026 [TRI-LFFI-Q1-2026] |
| Realisation and write-downs | Partners decide what to bill; collect work in progress | data-reporting | 89% of firms report rising write-offs [BIGHAND-FINANCE-2026]; about 300 hours of own write-downs per partner a year [TRI-EFFICIENCY-2025] |
| Matter profitability and leverage | Cost against revenue by matter; who does the work | data-reporting | Losses found after the bill is out (`#03`); non-equity partner hours ratio highest since late 2018 [TRI-LFFI-Q2-2026] |
| Budgeting, forecasting, general ledger | Forecast from actuals; track rate changes | data-reporting | Context assembled by hand across billing, receivables and time (`#05`) |
| AI investment and return review | Set the AI budget; judge renewals | data-reporting, expert-judgment | 18% say their organisation tracks AI ROI [TR-AIPS-2026] |
| AI cost and vendor contracts | Licences, tokens and agents; allocate or absorb | data-reporting, coordination-scheduling | Lawyers cannot see spend; seat contracts meet consumption pricing [TRI-METER-2026] |
| Partner economics | Pay, origination credit, write-off policy, expectations | expert-judgment | Pay keyed to utilisation and hours [TRI-ILTACON-2025] |
| Capital and ownership | Private equity, MSOs (management services organisations), employee ownership | expert-judgment | Profit paid out yearly; Rule 5.4 and independence limits [HK-AMLAW-2026; NYSSCPA-APS-2025] |
| Client value reporting (shared) | Show clients what AI saved | client-interaction | Firms "still gathering the data" [TRI-LEGALWEEK-2026]; held in professional-services-scoping-pricing-09 |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns an outcome), reinvent (the service,
pricing, ownership or operating model changes). **Automate: no evidence in this module.** The nearest is PwC One, services clients use without a PwC
person in the loop, held in professional-services-scoping-pricing-22. **Delegate appears only as a whole-firm model (`#17`), never as an agent that
owns a finance task.** Ladder values for pricing and capital entries are nominal: AI changes the delivery effort, not the finance step.

**Fee mix and rates**
- Reinvent: `#01` move the firm's fee mix toward fixed, hybrid and outcome-linked fees. McKinsey (consulting) says about
  a quarter of global fees are outcome-based; Keypoint Law (Australia) prices fixed plus hourly; 46-86% of law firms,
  by size, have not changed pricing since adopting AI (B).
- Improve: `#02` model AI compression by type of work before the rate round; Legal Decoder's AIR announced, pricing
  roles advertised by unnamed global law firms; the rate-round step is an idea (C).

**Realisation, profitability and finance operations**
- Improve (process): `#03` passively captured work data shows leakage, matter margin and leverage while work runs
  (Aprio, Bonadio, Warren Averett in accounting; Tonkon Torp in law; vendor-published, B). `#04` every line of legal
  bills checked against 45 flags; fee examiners in four named bankruptcy cases use the method; UBS's legal department
  (in-house) via UnitedLex (B).
- Improve (step): `#05` Aderant Rates and GL Forecasting agents draft, the team decides (product page, C). `#06` aim AI
  at the research and drafting time that gets written down; modelled by a vendor-commissioned study (C).

**AI investment and return**
- Improve (process): `#07` a firm-level AI budget reviewed against utilisation, margin, revenue per head and EBITDA;
  PwC $3 billion network investment, RSM $1 billion commitment, KPMG usage tracking to value its investment (B).
  `#09` track where freed hours go and decide in advance to resell or reprice them (SPI's "leak", C).
- Improve (step): `#08` pilot-to-licence gate at more than 70% weekly active users (Holland & Hart, law, B).
- Reinvent: `#10` build a firm-owned platform: Kirkland & Ellis's reported $500 million commitment, Palantir among its partners (B).

**AI cost**
- Improve (process): `#11` read the meter by tool and user, set model-choice defaults and budgets, renegotiate terms;
  named practitioners at Littler, Barnes & Thornburg, Ogletree, Taft and Lawfront (B). `#12` meter consumption-priced
  AI by matter, decide overhead versus recovery under fee rules, re-test fixed-fee margins (Legora Agent Pro; C, with
  the pass-through and margin parts as ideas).

**Partner economics and leverage**
- Improve (process): `#13` partner expectations, credit and pay for AI and non-hourly work (PwC statement; TRI survey;
  no firm reports a changed pay formula, C).
- Reinvent (idea): `#14` model leverage and partner income under AI scenarios; leverage data exist, AI attribution
  does not (D).

**Capital and ownership (reinvent)**
- `#15` Crowe (accounting) takes KKR capital for talent, technology and innovation and splits attest from non-attest
  work (B). `#16` law firms use MSOs or Arizona-style licensed structures; a reported $700 million letter of intent (C).
  `#17` AI-native firms: General Legal (law, about 400 clients, self-reported), Norm Law, Falcon, Queen's Tower Advisory
  (consulting target), Ascend (accounting) (delegate, B).

**Held elsewhere (do not duplicate):** hourly billing on actual AI-assisted time (professional-services-scoping-pricing-06); AI cost terms in fee
agreements (-07); matter-level AI value evidence (-09); partner AI-value conversations (-10); in-house AI-savings terms in outside-counsel guidelines
(-11); staff metrics off billed hours (-13); accounting and tax value pricing (-16, tax-compliance-corporate-16,
tax-compliance-individual-business-22); where the AI time dividend goes (-17); AI-native law-firm pricing (-21); PwC One (-22); licensing firm-built
tools (-23). PE independence (assurance-acceptance-independence-16, -17); AI-native audit firms (-20); AI-justified audit fee cuts (-21); AIUC-1
certification of AI agents (assurance-assurance-over-ai-19).

## 4. Interview probes

Ask a managing partner, CFO or COO, pricing director, innovation or knowledge lead, or a legal-operations head. Expect
"we don't measure that" on AI return; note who would know.

1. **"When AI saves hours on a matter, what happens to the time entry, the write-down and the partner's credit? Who
   decides, and is it tracked?"** Reveals whether the saving leaks (`#09`, `#06`) and whether fee rules are applied
   (§6).
2. **"What share of last year's fees was hourly, fixed, capped, subscription or outcome-linked, and which way is it
   moving?"** Reveals the fee-mix starting point (`#01`) and how exposed revenue is to AI efficiency.
3. **"How do you know an AI investment worked? Which measure: weekly active users, hours, realisation, margin? Who owns
   it?"** Reveals the measurement gap (`#07`, `#08`); most will name usage only.
4. **"What did AI cost last quarter across seats, tokens and agents, per lawyer and per matter? Who sees the meter?"**
   Reveals cost visibility and readiness for consumption pricing (`#11`, `#12`).
5. **"What happens at renewal if a vendor moves from seats to usage? Do your contracts cover allowances, overages and
   price changes?"** Reveals contract exposure (`#11`) [BAKERDONELSON-TOKENS-2026].
6. **"Is any AI cost billed to clients today? On what basis, and what do your engagement letters say?"** Reveals the
   overhead-versus-recovery decision and compliance with fee rules (`#12`).
7. **"When do you learn a matter lost money: during the work or after the bill? From which system?"** Reveals readiness
   for in-flight profitability and leakage analysis (`#03`, `#04`).
8. **"Which of your fixed or capped fees would lose money if AI cost doubled, or gain if effort halved, and how would
   you know before the work starts?"** Reveals margin-model maturity (`#12`, `#02`).
9. **"Did AI change anything in the last rate round: standard rates, discounts or fee language?"** Reveals whether rates
   and AI savings are decided together (`#02`); TRI warns rate rises without visible value are exposed.
10. **"What has changed in utilisation targets, origination credit, write-off policy or partner pay since AI arrived?"**
    Reveals the main internal brake (`#13`).
11. **"If work below equity partner shrinks, what would you change first in leverage, partner income or intake, and
    what data would you need?"** Reveals whether `#14` is on the agenda; route training questions to talent-learning.
12. **"Would you take outside capital (private equity, an MSO) to fund AI? What would it pay for, and what control,
    independence or insurance limits apply?"** Reveals the capital path (`#15`-`#17`) and blockers (§6).

## 5. Metrics and benchmarks

**Market and firm performance (US law unless stated; none attributed to AI by its source)**
- Q1 2026 LFFI 55, its long-run average, despite Am Law 100 worked-rate growth of almost 10% and overall demand growth of 2.7%
  [TRI-LFFI-Q1-2026]; Midsize worked rates grew 5.3% against 9.8% for the Am Law 100 [TRI-LFFI-MIDSIZE-2026]. Q4 2025 index 61, worked-rate
  growth 7.1% [TRI-LFFI-ELASTICITY-2026]. Q2 2026: index up sharply; associates +4.3%, non-equity partners +6.0%,
  equity partners -1.2% in demand; technology plus KM spend +11.6% [TRI-LFFI-Q2-2026; TRI-LFFI-COSTS-2026].
- Associate demand leverage 1.55 in Q4 2025 (record), 1.47 in Q1 and Q2 2026 [TRI-LFFI-LEVERAGE-2026].
- End-2025: profit per lawyer 8.4% and fees worked per lawyer 16.8% above pre-2022 levels, mostly from rate rises;
  technology spend +39.3% and KM +37.2% since 2021 [TRI-SOTLM-2026].
- Citi H1 2026: demand for Big Law hours +4.2% against a normal of about 1.5% [BLOOMBERG-AICOST-2026].
- BigHand (800+ senior finance and legal leaders; vendor survey): 96% raised rates, 89% report rising write-offs, 90%
  higher lockup, 46% use advanced business intelligence [BIGHAND-FINANCE-2026].
- MSO screens (a law firm's view, not a benchmark): leverage of 4:1 or higher favourable; realisation below 85% and
  overhead above 55% of revenue flagged as improvement opportunities [WINSTON-PE-2026].

**Pricing mix**
- 90% of legal dollars hourly [TRI-SOTLM-REPORT-2026]; almost two-thirds of 736 law-firm professionals say pricing is
  unchanged [TRI-FOP-LAW-2026]; 86% of solo and 46% of enterprise law firms have not changed pricing since adopting AI
  [CLIO-SOLO-2026]. Tax firms: 78% bill hourly; return preparation margin 28% against 20-24% for advisory
  [TRI-CHARGING-2026]. McKinsey: about a quarter of global fees outcome-based (rounded, self-reported) [BI-MCKINSEY-2025].

**AI investment, value and cost**
- PwC network: $3 billion invested in AI and other key areas in FY to 30 June 2026; revenue $60.2 billion; 330,000+
  people AI-trained [AT-PWC-2026]. Kirkland: $500 million commitment, no ROI benchmarks [BLOOMBERGLAW-KIRKLAND-2026].
- 18% track AI ROI, 40% do not know [TR-AIPS-2026]; 85% of law-firm and 75% of corporate-legal respondents collect no
  AI ROI data or are unsure [TRI-GREATDISCONNECT-2026]. 22% of firms have a GenAI strategy; those with one said to be
  3.9 times more likely to achieve ROI (no base given) [TRI-LEGALWEEK-2026].
- 84.8% of 245 services firms say AI saves time; the revenue share is withheld [SPI-AI-2026]. About a third of small
  law firms using AI have grown revenue from it [CLIO-SOLO-2026]. 38% of A&E firms report measurable benefit
  [DELTEK-CLARITY-2026].
- AI cost: about 1% of revenue as the level firms are settling on (one officer's statement) [TRI-METER-2026]; $50-$350
  per attorney a month, about 30% added to tool cost (one estimate) [BLOOMBERGLAW-TEXAS-2026]; Harvey tokens 14x in six
  months [ARTLAW-HARVEY14X-2026]; one firm spends about $30,000 a year on AI products [HBJ-BILLABLE-2026].
- Adoption gate: more than 70% weekly active users (Holland & Hart) [TRI-ILTACON-IMPL-2026].
- Tool claims (vendor-published, one named customer): Tonkon Torp 21 minutes a day more captured, about $20,000 more
  revenue per timekeeper, 20% faster collection [LAUREL-TONKON-2026].

**What to measure (recommend; nobody publishes these yet):** realisation and write-offs on AI-assisted versus other matters; AI cost per matter and as
a share of revenue; revenue per head and margin against AI spend; where freed hours went (resold, repriced, given back); share of fees by pricing
model; forecast error of any AI forecast; override rate of AI billing flags.

## 6. Guardrails

**Hourly fees (US legal ethics).** Bill only time actually spent; time saved by AI cannot be billed; time spent
refining and checking AI output can be [CALBAR-GENAI-2026; TXETHICS-OP705-2025; DCBAR-OP388-2024]. Flat-fee positions
differ by state; see scoping-pricing §6.

**AI costs.** General AI subscriptions are overhead; matter-specific AI costs may be charged only with disclosure in
the fee agreement, at actual cost, with no markup without informed written consent [CALBAR-GENAI-2026]. Texas
generally limits recovery to the amount actually paid [TXETHICS-OP705-2025]. A practitioner's opinion in an Illinois State Bar Association newsletter
recommends absorbing ordinary AI use as overhead [ISBA-ELEFANT-2026].

**Client instructions.** Some clients demand AI use and savings targets; others bar AI without permission or refuse
to pay for AI-done work [TRI-LEGALWEEK-2026]. California requires following client guidelines that restrict AI
[CALBAR-GENAI-2026].

**Ownership and independence.** ABA Model Rule 5.4 bars fee-sharing and partnerships with non-lawyers; Colorado enacted a
fee-sharing ban in August 2026 and Illinois requires MSO disclosure to clients [BESTLAW-WSHB-2026]. An April 2026 academic
essay argues no state bar has issued MSO governance standards [COLUMBIA-BREYDO-2026]. Arizona licenses alternative business structures
[AZ-ABS-2025]. For accounting firms, the AICPA sought comment on alternative-practice-structure rules for PE-backed
firms (comments due 30 April 2026) [NYSSCPA-APS-2025]; detail in assurance-acceptance-independence-16.

**People data.** AI used for employment and worker management is a high-risk use under the EU AI Act; obligations apply from
2 December 2027 [EC-AIACT-2026]; California flags bias risk in AI-assisted employment actions [CALBAR-GENAI-2026]. Passive activity
capture (`#03`) needs a privacy review; vendor security claims need checking [LAUREL-WORKSTUDIO-2026].

**Data in finance analytics.** Legal Decoder replaces firm, timekeeper, matter and client names with tokens before an
LLM sees billing data [LAWSITES-DECODER-2026].

**Insurance.** The Law Society's study reports that professional indemnity insurance rarely covers AI-related
mistakes [LAWSOC-AGENTICFULL-2026].

**Steps that need human judgment:** rates and discount policy; the target fee mix; whether an AI cost is overhead or
recovered, and its disclosure; write-down decisions; renewal and budget decisions on AI tools; partner pay and credit
rules; acceptance of outside capital and its governance; any use of AI data to evaluate people.

## 7. Roles and how they evolve

- **Pricing professionals** model margins and fee structures for GenAI-assisted matters (unnamed global law firms'
  postings) [AMBITION-PRICINGMANAGER-2026]. Greenberg Traurig has a Chief Pricing and Innovation Officer
  [TRI-LEGALWEEK-2026].
- **Knowledge and innovation leads** add AI cost management; TRI names roles such as chief data and AI officer and
  knowledge and AI solutions manager [TRI-METER-2026].
- **Finance teams** move toward in-flight margin views; Aprio's CFO uses work data to staff, protect margins and plan
  [LAUREL-SIGNAL-2026]. COOs at a roundtable expected fewer billing administrators and more technology, data and AI
  enablement roles [WESTERNALLIANCE-COO-2026].
- **Partners**: PwC's US CEO said partners who resist AI "have no place at the firm" [CPAPA-PWC-2026]; only 25% of
  stand-out lawyers strongly agree their firm has a plan to monetise AI [TRI-STANDOUT-2026]; INSIDE Public Accounting
  says the fastest-moving firms are expanding partner tracks in operations and technology enablement [IPA-2026].
- **Associates and non-equity partners** carry most extra demand [TRI-LFFI-Q2-2026]; Legalweek panels treated the
  associate's future as the open question [TRI-LEGALWEEK-ASSOC-2026]. Intake and training: talent-learning.
- **Engineers inside firms**: Kirkland reports 180+ AI engineers and data scientists and an AI infrastructure
  director opening [BLOOMBERGLAW-KIRKLAND-2026].
- **In-house legal operations** is moving into strategy; the share of GCs naming technology a strategic priority doubled
  from 2025 to 2026 [TRI-LDOR-2026].

## 8. Frontier

- 2025-10-31: KPMG to rate staff on AI use and track it to value its investment [BLOOMBERG-KPMG-2025].
- 2025-11-17: McKinsey says about a quarter of fees are outcome-based [BI-MCKINSEY-2025].
- 2025-12-22: AICPA asks for comment on PE-backed practice structures [NYSSCPA-APS-2025].
- 2026-03-25: PwC's US CEO on subscription services and partners who resist AI [CPAPA-PWC-2026].
- 2026-04-30: legal academic warns MSO governance is not ready [COLUMBIA-BREYDO-2026].
- 2026-05: California guidance covers agentic AI, fees and AI costs [CALBAR-GENAI-2026].
- 2026-06-11: Crowe announces KKR investment; closed August; CroweONE reported 2026-10-19 [AT-CROWE-KKR-2026; AT-CROWE-2026].
- 2026-06-15: Kirkland's $500 million AI platform reported [BLOOMBERGLAW-KIRKLAND-2026].
- 2026-06-16: PE investors re-examine hourly-billed accounting revenue (FT via a Dutch outlet) [VANMORGEN-SUPERRETURN-2026].
- 2026-06-23: Legora prices Agent Pro by consumption with matter attribution [LEGORA-CBP-2026].
- 2026-07-08: Harvey tokens up 14x in six months [ARTLAW-HARVEY14X-2026].
- 2026-07-15: Legal Decoder launches Aperture; announces AIR and an AFA builder [LAWSITES-DECODER-2026].
- 2026-07-16: Intapp Celeste generally available, with pricing among its playbooks [LAWSITES-CELESTE-2026].
- 2026-08: Colorado fee-sharing ban; 2026-09-16: Charlesbank letter of intent for Wood Smith reported [BESTLAW-WSHB-2026].
- 2026-08-20: Baker Donelson token-pricing guide for general counsel [BAKERDONELSON-TOKENS-2026].
- 2026-08-23: Stanford: AI pushes consulting toward hybrid and asset-based pricing [STANFORD-DEL-2026].
- 2026-09-09: ILTACON practitioners "reading the meter" [TRI-METER-2026].
- 2026-10-13: Legora and Laurel link AI work to time entries, value measures to follow [LAWSITES-LAUREL-2026].
- 2026-10-19: PwC reports $3 billion AI and capability investment [AT-PWC-2026]; AICPA and AIUC announce a SOC 2 plus
  AIUC-1 certification piloted at CPA firms including PwC, full launch planned early 2027 [AT-AIUC-2026].
- Scheduled, not evidence: TRI's 25th Law Firm COO & CFO Forum, 21-22 Oct 2026 [TRI-EVENTS-2026].

## 9. Common objections

- **"We're having record years; why change?"** True: rates and demand are strong [TRI-LFFI-Q2-2026;
  BLOOMBERG-AICOST-2026]. But Q1 2026 output was only average despite near-record inputs [TRI-LFFI-Q1-2026], TRI warns
  firms using AI mainly to justify higher rates are exposed if the AI bubble bursts [TRI-SOTLM-2026], and 32% of
  corporate clients have reconsidered, or plan to reconsider, providers they see as falling behind [TR-FOP-REPORT-2026].
- **"AI efficiency will cut our revenue."** On hourly work it can: saved time cannot be billed [TXETHICS-OP705-2025].
  That is why the fee mix matters (`#01`): California allows flat fees that build in AI savings [CALBAR-GENAI-2026],
  and McKinsey prices about a quarter of fees on outcomes [BI-MCKINSEY-2025]. Plan where freed hours go (`#09`).
- **"We can't measure AI return."** Almost nobody can: 18% track it [TR-AIPS-2026]. Start with an adoption gate (`#08`)
  and tie spend to finance measures the board already watches (`#07`) [SPI-AI-2026].
- **"AI is a small overhead line."** Not for long: vendors are moving to consumption pricing [LEGORA-CBP-2026], at least
  one major model vendor changed rates in ten of the last 13 months [BAKERDONELSON-TOKENS-2026], and one PowerPoint cost $2 [TRI-METER-2026].
- **"We'll just pass AI costs to clients."** Only matter-specific costs, disclosed, at cost, no markup without consent
  [CALBAR-GENAI-2026]; Keypoint's CEO expects clients to be annoyed [LAWYERSWEEKLY-KEYPOINT-2026].
- **"Cut AI spend by limiting the expensive models."** Artificial Lawyer argues lawyers will pick the costlier model when
  accuracy matters [ARTLAW-HARVEY14X-2026]; a speaker noted a firm cannot tell a client it ran out of tokens [TRI-METER-2026].
- **"We should build our own, like Kirkland."** Kirkland gave no ROI benchmarks [BLOOMBERGLAW-KIRKLAND-2026]; Ropes &
  Gray's CIO said building did not make sense for that firm at present [AIWEEKLY-KIRKLAND-2026].
- **"Outside capital will pay for it."** Crowe did it [AT-CROWE-KKR-2026], but fewer UK mid-tier firms are considering
  PE [ICAEW-MIDTIER-2026], law-firm rules are tightening in some states [BESTLAW-WSHB-2026], and one commentator argues
  PE is not designed to reinvent a billing model [BLAKEOLIVER-PE-2026].
- **"Partners will never change how they are paid."** Pay is keyed to hours [TRI-ILTACON-2025], so pricing will not
  move on its own; PwC's US CEO said partners who resist AI have no place at the firm [CPAPA-PWC-2026].
- **"Passive time capture is surveillance."** Treat it as a privacy decision and verify vendor security claims
  [LAUREL-WORKSTUDIO-2026].

## 10. Sources

Full details (title, URL, date, locator, access) are in the YAML. Keys marked * are not in the YAML; their date and URL are given here.

- **Regulators and professional bodies:** CALBAR-GENAI-2026, TXETHICS-OP705-2025, DCBAR-OP388-2024, ISBA-ELEFANT-2026, AZ-ABS-2025, NYSSCPA-APS-2025, EC-AIACT-2026, LAWSOC-AGENTICFULL-2026,
  ICAEW-MIDTIER-2026, ILTA-TECHSURVEY-2026.
- **Academic:** STANFORD-DEL-2026, NBER-AUTOR-2026, COLUMBIA-BREYDO-2026.
- **Surveys and market data:** TR-FOP-REPORT-2026, TR-AIPS-2026, TRI-FOP-LAW-2026, TRI-STANDOUT-2026, TRI-SOTLM-2026, TRI-SOTLM-REPORT-2026, TRI-LFFI-Q1-2026, TRI-LFFI-Q2-2026, TRI-LFFI-COSTS-2026,
  TRI-LFFI-LEVERAGE-2026, SPI-AI-2026, LITERA-LAWSITES-2026, TRI-LFFI-MIDSIZE-2026* (TRI, Q1 2026 LFFI analysis on Midsize firms, 2026-05-26, https://www.thomsonreuters.com/en/institute/articles/q1-2026-lffi-analysis-midsize-law-firms), TRI-LFFI-ELASTICITY-2026* (TRI, Q4 2025 LFFI analysis,
  2026-03-02, https://www.thomsonreuters.com/en/institute/articles/lffi-q4-2025-analysis-rate-elasticity), TRI-GREATDISCONNECT-2026* (TRI, "The great AI disconnect", 2026-03-18, https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect), BIGHAND-FINANCE-2026* (BigHand 2026 Annual Law Firm Finance Report landing page, 2026-01-21, https://www.bighand.com/en-us/resources/whitepapers/2026-annual-law-firm-finance-report/),
  DELTEK-CLARITY-2026* (Deltek Clarity A&E study release, 2026-05-12, https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/), TRI-LDOR-2026* (TRI 2026 Legal Department Operations Report page, 2026-09-22, https://www.thomsonreuters.com/en/institute/reports/legal-department-operations-report-2026).
- **Firms:** BAKERDONELSON-TOKENS-2026, WINSTON-PE-2026, HK-AMLAW-2026, RADIANT-TOKENS-2026.
- **Vendors:** LAUREL-SIGNAL-2026, LAUREL-WORKSTUDIO-2026, LAUREL-TONKON-2026, LAUREL-WARREN-2026, LEGORA-LAUREL-2026, LEGORA-CBP-2026, ADERANT-AGENTS-2026, NETDOCUMENTS-TOKENS-2026,
  LEXIS-FORRESTER-2025, CLIO-SOLO-2026.
- **Conference coverage:** TRI-LEGALWEEK-2026, TRI-LEGALWEEK-ASSOC-2026, TRI-METER-2026, TRI-ILTACON-IMPL-2026, TRI-ILTACON-2025, TRI-COOCFO-AI-2025, EDISCOVERYTODAY-ILTACON-2026, TRI-EVENTS-2026*
  (TRI events page listing the 25th Law Firm COO & CFO Forum, read 2026-10-19, https://www.thomsonreuters.com/en/institute/events).
- **Press, podcasts and commentary:** BI-MCKINSEY-2025, RESULTSENSE-2026, FORRESTER-BLOG-2025, CTV-DELOITTE-2025, CPAPA-PWC-2026, AT-PWC-2026, AT-CROWE-2026, AT-CROWE-KKR-2026, AT-AINATIVE-2026,
  BLOOMBERG-KPMG-2025, BLOOMBERGTAX-PRICING-2026, BLOOMBERGLAW-KIRKLAND-2026, BLOOMBERGLAW-TEXAS-2026, BLOOMBERGLAW-BILLABLE-2026, BLOOMBERGLAW-GCXAI-2026, AIWEEKLY-KIRKLAND-2026, BESTLAW-WSHB-2026,
  ARTLAW-HARVEY14X-2026, NONBILLABLE-2026, LAW360-LEGORA-2026, LAWSITES-DECODER-2026, LAWSITES-LAUREL-2026, LAWSITES-ILTASURVEY-2026, LAWSITES-HARVEYDJ-2026, LAWSITES-GENERAL-2026,
  LAWYERSWEEKLY-KEYPOINT-2026, CONSULTANCYUK-BONE-2026, HBJ-BILLABLE-2026, MONDAQ-GGI-2026, IPA-2026, VANMORGEN-SUPERRETURN-2026, BLAKEOLIVER-PE-2026, WESTERNALLIANCE-COO-2026, TRI-CHARGING-2026,
  TRI-EFFICIENCY-2025, TRI-ROI-2025, TRI-RETHINKING-2025, BLOOMBERG-AICOST-2026* (Bloomberg Law, Big Law AI cost savings column, 2026-09-03, https://news.bgov.com/business-and-practice/big-law-ai-cost-savings-remain-a-mystery-as-billable-hours-jump), LAWSITES-CELESTE-2026* (LawSites, Intapp Celeste general
  availability, 2026-07-16, https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html), AT-AIUC-2026* (Accounting Today, SOC 2 and AIUC-1 certification, 2026-10-19, https://www.accountingtoday.com/news/new-ai-assurance-certification-combines-soc-2-aiuc-1).
- **Job postings:** AMBITION-PRICINGMANAGER-2026, AMBITION-PRICINGADVISOR-2026.
