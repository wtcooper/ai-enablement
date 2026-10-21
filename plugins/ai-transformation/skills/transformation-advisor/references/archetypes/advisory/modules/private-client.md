# Private client (advisory)

Sources checked 2026-10-20 and re-verified 2026-10-21. Use cases live in `../use-cases/private-client.yaml` (17 entries). Ids are shortened
here: `#04` means `advisory-private-client-04`; other modules' ids are in full. Source keys in brackets, such as
[ARMANINO-FOTRENDS-2026], are in the YAML or in §10. **Evidence is thin and mostly self-interested.** No entry is
graded A. 6 of 17 are graded B, and those rest on named deployments without measured results (one carries a
practitioner's time estimate). 8 are C and 3 are D (ideas). Nearly every source is a vendor, bank, law firm or advisory firm that sells to family offices; every
family-office survey here is published by a bank, administrator or advisory firm. No source reports an error rate,
override rate, parallel run, client-satisfaction measure or inspection finding for this module. Say so when you
quote a figure.

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

Private client services for wealthy families and the businesses they own. That means family-office accounting and
close across many entities, alternative-investment administration (capital calls, distribution notices, valuation
statements and K-1s from private funds), consolidated reporting to principals (the family members the office serves),
payment controls, succession and governance advice, exit-readiness advice for owners, and the client experience. The
work is done by accounting firms (PKF O'Connor Davies, a large national firm; Armanino, Wiss and Kaufman Rossin, which
publish family-office positioning; GWCPA, which focuses on family-held businesses), family-office advisory firms (Wingspan), wealth platforms (Mercer
Advisors, Compound Planning; not accounting firms), vendors (Asseta AI, Masttro, Canoe) and family offices' own staff.
Some CAS (client accounting services) practices treat family offices as one of their verticals: Sweeney Conrad is one
[JOFA-CASTIPS-2025]. Estate and tax technical work is in the tax archetype. Regulated investment advice (portfolio
management, manager selection) is out of scope. How the firm prices and staffs this work is in professional-services.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Family-office accounting and close | Multi-entity general ledger, bank and brokerage feeds, bill pay and AP, intercompany entries, month-end close | transaction-processing, data-reporting | Lean teams across fragmented systems; "a lot of what makes a family office run lives in people's heads" [ARMANINO-FOTRENDS-2026] |
| Alternative-investment administration | Collect capital calls, distributions, valuation statements and K-1s from each manager's portal; enter them in one system | transaction-processing, data-reporting | Every manager has its own format and schedule; K-1s arrive late by design and push returns onto extension [ARMANINO-FOTRENDS-2026]; in one conference poll, 36% named collecting the documents as the main problem [CANOE-FOALTS-2026] |
| Consolidated reporting | Entity roll-up, commentary and dashboards for principals, family councils and advisors | data-reporting, document-production | 73% of RBC and Campden respondents say investment reporting is still too manual, a top concern three years running [RBC-CAMPDEN-2026] |
| Payment approval and controls | Approval hierarchies, dual authorization, vendor access reviews | review-assurance | Informal approvals by email [AGILLINK-FOPRED-2026]; AI-generated voice, video and text make payment requests look real [CFO-DEEPFAKE-2026] |
| Fund document reading | Read and compare LP (limited partnership) agreements and other fund documents | review-assurance, research-synthesis | Long agreements to compare against standard language during due diligence (`#06`) |
| Succession and governance advice | Succession plans, involving the next generation, decision rights | expert-judgment, client-interaction | Many families have no complete plan, but surveys define a plan differently (see §5) |
| Owner exit readiness | Value-building and readiness conversations with business owners | expert-judgment, client-interaction | Exits depend on leadership alignment, decision-making and institutional knowledge [EPI-AIWEBINAR-2026] |
| Client experience | Meetings, follow-up, service requests, portals and live views | client-interaction, coordination-scheduling | Principals expect timely insights rather than periodic summaries, per a Hubbis panel write-up [HUBBIS-ETON-2026] |
| AI policy for the family | Inventory uses, approve tools, vet vendors, train staff | expert-judgment, document-production | Exposure can happen through ordinary use with no breach event [SQUIRE-FOAIRISK-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step; "(process)" marks entries that also redesign the flow), automate (no
person on the normal path), delegate (an agent owns a multi-step outcome), reinvent (the service or operating model
changes). **No delegate entry exists.** Forum speakers say agents are moving from answering questions to executing
workflows [WISS-FOAI-2026], and Citi reports that some offices expect analysts to move to managing agentic workflows
[CITI-AIFO-2026], but no named deployment was found. Automate has one announced entry and one marketing tool.

**Accounting, close and alternative investments**
- Improve: `#02` document AI pulls capital calls, distributions and valuations into a draft that a person reviews
  (Masttro's Doc AI at Jefferson River Capital, a single family office; 200+ alternative investments tracked; vendor
  case study; B). `#04` AI codes transactions, reconciles across entities and banks and flags anomalies for review
  (practitioner and vendor statements, one family-office controller posting; C). `#16` (assist) modelling cash flow
  from five years of profit-and-loss statements with an enterprise assistant (Minot's Light Management, a family
  office; its CEO estimates about 45 minutes against "hours"; self-reported; B).
- Automate: `#01` (process) PKF O'Connor Davies announced a collaboration and says it plans to use Asseta AI's platform
  to help family offices modernize, from evaluation and implementation through ongoing financial operations. The
  vendor says the platform reconciles inter-company accounts automatically (announced; vendor figures only; C).
- Same steps in CAS: advisory-client-accounting-services-01 (categorization), -02 (reconciliation), -03 (close
  agents) and -07 (cash-flow forecasts). K-1 extraction for the tax return is tax-compliance-individual-business-02.

**Reporting and client experience**
- Improve: `#03` AI drafts reporting commentary and meeting material, and a person signs off (Armanino advice; 16% of
  family offices use AI for performance reporting per Citi; C). `#09` Compound Planning announced agents that draft
  follow-ups and agendas and turn requests into tickets for advisor sign-off (digital wealth firm; C).
- Improve (process): `#08` Mercer Advisors' Aspen, a knowledge graph that maps clients, teams and services across
  planning, custody and productivity systems, which the company says is deployed across 1,100+ wealth professionals
  (wealth platform, not an accounting firm; B). `#10` a live consolidated family view with AI summaries in place of
  periodic packages (vendor product listings and advisor positioning; C). Compare
  advisory-client-accounting-services-06.

**Controls, documents and office productivity**
- Improve: `#07` flags on payment anomalies and wire-instruction discrepancies; procedural controls carry the load
  (vendor feature; C). `#06` (assist) comparing LP-agreement language (Placements Italcan Inc., a family office;
  self-reported; B). `#05` (assist) general assistants for file conversion, building Salesforce automations and
  travel admin (Ford Estates LLC and Placements Italcan Inc.; B). `#11` (idea) capturing institutional knowledge to
  reduce key-person risk (D).
- Related: advisory-client-accounting-services-10 (fraud screening before payment release),
  advisory-forensic-disputes-12 (investigating AI-fuelled fraud, idea).

**Succession and owner advice**
- Automate: `#17` GWCPA's client-facing custom GPT (a ChatGPT version set up with the firm's own instructions and
  materials) answers basic ownership-transition questions. The marketing partner says it brought about 50 new
  mailing-list members in three months (CPA firm focused on family-held businesses; B). It is a marketing tool, not engagement work.
- Improve (ideas only): `#12` scenario modelling and assessment of successors (D). `#13` AI-supported exit-readiness
  conversations (D). No source reports AI used inside a succession or exit engagement.

**Service and operating model**
- Reinvent: `#15` the hybrid family office keeps strategy, relationships and decisions in-house and outsources
  accounting, reporting, technology, AI enablement and cybersecurity (Armanino describes the trend; PKF is the nearest
  named example; C). `#14` advising families on AI policy, data limits and vendor diligence (Northern Trust, Squire
  Patton Boggs, ArentFox Schiff, Armanino and Wiss publish frameworks; no source shows it sold as a paid service; C).
  Compare advisory-risk-controls-17 and -18, and advisory-client-accounting-services-20.

## 4. Interview probes

Ask in the person's setting (accounting firm, family-office advisory firm, wealth platform or in-house office).

1. **"Which steps in your family-office accounting (document intake, coding, intercompany, close, consolidation)
   does an AI tool touch today? Who reviews the output, and how many items get corrected?"** Reveals the ladder
   position (`#02`, `#04`) and whether anyone measures quality. No public source does.
2. **"How do capital calls, distribution notices and K-1s reach you, and from how many managers and portals?"**
   Reveals whether `#02` fits. In one poll, collecting documents was a bigger problem than extracting data
   [CANOE-FOALTS-2026].
3. **"What is the system of record for each workflow, and who owns the entity map?"** Reveals data readiness.
   Forum speakers say the data, not the AI, is the bottleneck [WISS-FOAI-2026].
4. **"Which family data may go into which AI tool, who approved that list, and has a principal asked for a ban or
   an opt-in?"** Reveals policy maturity (`#14`) and the consent question [JOFA-ETHICSAI-2026].
5. **"Who can move money, and how do you check a payment request that arrives by email, voice or video?"**
   Reveals readiness for `#07`. Sources treat the control as procedure, not detection software [CFO-DEEPFAKE-2026].
6. **"When a principal asks for a live consolidated view, what has to be true of the data before you trust an AI
   summary?"** Reveals whether `#10` is realistic or premature.
7. **"Is any entity in the family's structure also an audit or attest client of your firm or an affiliate? Who
   checks before you add an AI-enabled accounting, hosting or reporting service?"** Reveals independence exposure
   (§6) and whether checks run in a system or from memory.
8. **"Do you or an affiliate give investment advice to these families?"** Reveals SEC and FINRA exposure (§6) and
   where this module stops.
9. **"In succession or exit work, where do you use AI and where do you refuse? How do you keep one family member's
   information from reaching another?"** Reveals readiness for `#12`, `#13` and `#17`. Estate and succession plans are
   sensitive: an estate plan can reveal inconsistent treatment of family members [AFS-FOAI-2024].
10. **"What do you keep in-house and what do you outsource: accounting, reporting, technology, cybersecurity?"**
    Reveals the operating model (`#15`) and who would own any AI.
11. **"Who reviews machine-prepared work now, who talks to the principals, and what are you hiring for?"** Reveals
    role change (§7) [JOB-FOCONTROLLER-2026; AICIO-FOOPTEST-2026].

## 5. Metrics and benchmarks

Survey figures are publisher-reported. Banks, administrators and advisory firms that sell to family offices publish
them, so none is independent, and their questions differ.

| Measure | Figure | What it counts, source |
|---|---|---|
| AI for operational tasks or investment analysis | 22%, up from 13% in 2024 | Share of family offices, Citi Wealth 2025 report; sample size not on the page [CITI-AIFO-2026] |
| AI for investment performance reporting | 16%, "more than doubling in one year" | Same source [CITI-AIFO-2026] |
| Biggest barrier | 57% cite lack of internal expertise | Same source [CITI-AIFO-2026] |
| AI embedded and essential to workflow | half of offices | RBC and Campden 2026; 155 responses from single- and private multi-family offices across the Americas [RBC-CAMPDEN-2026] |
| Investment reporting too manual | 73% | Same source [RBC-CAMPDEN-2026] |
| Cybersecurity and data breaches the top near-term operational concern | 59%, up from 16% | Same source [RBC-CAMPDEN-2026] |
| Already use AI technology | 86%; only 7% seek opportunities in the AI sector | Ocorian survey of family members and senior executives in 16 jurisdictions; sample size not stated [OCORIAN-IFC-2026] |
| Likely to use AI for financial reporting or data visualization within five years | 69% of 317 | UBS family-office clients; intent, not use [UBS-GFO-2025] |
| Exploring or frequently using AI | 50%; 36% say collecting alts documents is the main problem | Vendor-reported poll of 70+ offices at a late-2025 conference [CANOE-FOALTS-2026] |
| "Prioritise AI investments" | 65% | J.P. Morgan 2026 (n=333), via a secondary summary. It measures AI as an investment theme, not use in operations [PULSE2-JPMFO-2026; ARMANINO-FOTRENDS-2026] |
| Family businesses that see AI and genAI as growth opportunities | 65%; 28% cautious | PwC 2025 US Family Business Survey [PWC-USFB-2025] |
| Why offices outsource | 80% mainly for expertise; 31% cite cost savings | Armanino citing Campden Wealth and AlTi Tiedemann (2025); underlying report not read [ARMANINO-FOTRENDS-2026] |
| Succession plans | UBS: 53% have a wealth succession plan. RBC: half have an incomplete or no plan. J.P. Morgan: 86% lack a clear plan for key decision makers | Three different questions; do not compare [UBS-GFO-2025; RBC-CAMPDEN-2026; PULSE2-JPMFO-2026] |
| Deployment scale | Masttro: 200+ alternative investments at one office. Asseta: 8-12 weeks to go live, $125B+ assets, 50+ families. Mercer: 1,100+ professionals | Vendor- or company-published counts, no method [MASTTRO-JEFFERSON-2026; ASSETA-SITE-2026; MERCER-ASPEN-2026] |
| Succession chatbot reach | about 50 mailing-list sign-ups in three months | One firm partner's account [JOFA-REALLIFE-2025] |
| Time for one cash-flow model | about 45 minutes against "hours" | One family-office CEO's estimate for a single task, including spot checks [FOPRO-AITODAY-2026] |

**What to measure.** Armanino suggests (as metrics to watch, not benchmarks) days to close, the share of reports
the system generates, the share of K-1s received before the filing deadline, the number of approved AI uses with
documented review controls, and rework hours per month [ARMANINO-FOTRENDS-2026]. In a pilot, also count how many
extracted or coded items a reviewer corrects; no source publishes that figure.

**Not found:** extraction accuracy, override rates, parallel-run results, client-satisfaction data or inspection
findings. Mercer's coverage says many wealth firms struggle to quantify what AI investment delivers
[MERCER-ASPEN-2026]. The nearest independent study covers SME bookkeeping, not family offices: it associates genAI
use with productivity gains, with no figure in the abstract [STANFORD-JAR-2026].

## 6. Guardrails

- **No regulator has issued AI guidance specific to family offices.** The texts below apply by analogy or to a
  regulated affiliate.
- **IRS OPR (Circular 230, the rules for tax practitioners).** Verify AI-created facts, citations and calculations
  before delivery (section 10.22). Billing for time not spent, or double billing for AI-assisted tasks, may violate
  section 10.27 depending on the facts, and cost savings should be passed on openly. Firms need procedures, training
  and vendor vetting (10.36). Written advice cannot rely on AI projections without verification (10.37). Client data
  goes only into secure, enterprise-approved AI (IRC 6713 and 7216; 10.51) [IRS-OPR-2026]. Tax detail:
  tax-compliance-individual-business-19 and -21.
- **FINRA 2026 report.** Rules are technology-neutral. Summarization and information extraction are the top GenAI
  use at member firms. Agent risks named: autonomy, scope and authority, auditability, data sensitivity, domain
  knowledge. Monitoring may include prompt and output logs [FINRA-OVERSIGHT-2026]. It addresses member firms only.
- **SEC FY2026 examination priorities.** Examiners review whether registrants' AI claims are accurate and whether
  policies supervise AI use, including back-office work; cyber reviews cover AI and polymorphic malware
  [SEC-EXAMPRI-FY2026]. Relevant to RIA (registered investment adviser) affiliates of accounting firms.
- **Independence (the firm's own audit and attest clients).** For SEC issuer audit clients, bookkeeping
  ((c)(4)(i)), investment-adviser services ((c)(4)(viii)) and services for a contingent fee or commission ((c)(5),
  subject to the rule's defined exceptions) impair independence [SEC-RULE2-01-2026]. Under PCAOB Rule 3523, a firm is
  not independent of an issuer audit client if it provides tax services to a person in a financial reporting
  oversight role there, or to that person's immediate family, with limited exceptions [PCAOB-RULES3520-2026]. Under the AICPA Code, a nonattest service needs the client to take management
  responsibility, oversee it through a skilled person and accept the results [JOFA-NONATTEST-2016]. IESBA treats
  hosting or storing an audit client's data as a management responsibility [IESBA-TECH-2023]. A Journal of
  Accountancy article by AICPA Professional Ethics Division staff says developing or hosting an AI system for an
  attest client can raise independence concerns [JOFA-ETHICSAI-2026]. No
  source addresses family offices directly. See advisory-client-accounting-services-24 and
  assurance-acceptance-independence-15.
- **Client data.** Ask whether consent is needed before client data goes into an AI tool [JOFA-ETHICSAI-2026]. Keep
  confidential family, financial, legal, tax, estate and security information out of tools the policy does not
  cover [NT-FOAIPOLICY-2026]. Public models may reuse what is submitted [AFS-FOAI-2024]. Citi says solutions that
  cannot guarantee data security are unlikely to be adopted [CITI-AIFO-2026].
- **Payments.** Dual authorization and checks outside the channel the request came through, because detection
  tools lag attackers [CFO-DEEPFAKE-2026; ARMANINO-FOTRENDS-2026].
- **Fiduciary duty is not displaced by AI** [AFS-FOAI-2024]. Watch for automation bias, where a support tool
  quietly becomes the decision-maker [SQUIRE-FOAIRISK-2026]. Responsibility should stay with named people or
  functions [SQUIRE-FOAIRISK-2026].
- **Steps that need human judgment:** posting to the books, moving money and final decisions
  [ARMANINO-FOTRENDS-2026]; investment decisions [CITI-AIFO-2026]; legal interpretation and anything relied on in
  investment, legal, tax or estate matters [NT-FOAIPOLICY-2026]; sign-off on reports and commentary (`#03`);
  relationships with principals [KAUFMAN-FO-2026].

## 7. Roles and how they evolve

- **From keying to reviewing.** Armanino and Citi describe staff time moving from assembling reports to review and
  strategy [ARMANINO-FOTRENDS-2026; CITI-AIFO-2026]. Extraction puts a reviewable draft in front of a person (`#02`).
- **A prediction of fewer basic roles.** The 2025 RBC and Campden report is quoted as predicting a significant
  reduction in staff doing basic accounting or administrative work [WSR-RBC-2025]. It is a prediction, not a
  measurement. No headcount data exists.
- **Managing AI.** Citi reports some offices expect analysts to be replaced by AI agents, with staff managing AI
  processes. GenTrust's CIO says family offices asked it to help find staff who can find AI to automate bill pay,
  concierge and similar work [AICIO-FOOPTEST-2026].
- **Controllers own the tooling.** A family-office controller posting asks the hire to assess AI-assisted tooling
  alongside the close calendar and an outsourced-accounting relationship [JOB-FOCONTROLLER-2026].
- **Generalists stretch.** Staff without development skills built Salesforce automations with assistants (`#05`).
  A family-office CEO built a cash-flow model himself with an enterprise assistant (`#16`). A marketing partner built
  and runs his firm's succession chatbot (`#17`).
- **The relationship stays human.** Kaufman Rossin's family-office director says clients still want to talk to a
  real human; the firm's own commentary adds that AI should free staff time for engagement [KAUFMAN-FO-2026].
  Compound's chief executive says its technology is built to "accelerate and augment" the advisor-client
  relationship, and its head of engineering says the goal is not to replace advisors [MERCER-ASPEN-2026].
- **Who pushes adoption.** Citi names younger generations and junior staff as the biggest advocates
  [CITI-AIFO-2026]. The president of Eton Solutions, a family-office software vendor, told a panel that tools lift
  morale when they remove low-value tasks and frustrate staff when poorly implemented [HUBBIS-ETON-2026]. For junior development, see professional-services-talent-learning-07.

## 8. Frontier

- 2025-11-17: SEC FY2026 priorities target AI claims and supervision of AI use, including back-office work
  [SEC-EXAMPRI-FY2026].
- 2025-11-18 (reported 2025-11-20): Asseta AI announces a $4.2M seed round and says it supports more than $10
  billion in assets [CPAPA-ASSETASEED-2025]. Its homepage now shows $125B+; no source reconciles the two [ASSETA-SITE-2026].
- 2025-12-09: FINRA adds AI agents to its oversight report as an emerging risk [FINRA-OVERSIGHT-2026].
- 2026-03-26: PKF O'Connor Davies announces its collaboration with Asseta AI [PKF-ASSETA-2026].
- 2026-04-10: Ocorian survey: 72% expect AI's most significant effects on operating models over two to five years; 26% strongly
  agree it will reshape how offices operate within a year [OCORIAN-IFC-2026].
- 2026-04 forum, reported 2026-05-13: speakers say AI has moved from answering questions to executing workflows
  through connected data, with clean data a precondition [WISS-FOAI-2026].
- 2026-04-16: Wealth.com raises a $65M Series B for AI estate and tax planning (vendor claims; routed to tax)
  [WEALTHCOM-SERIESB-2026].
- 2026-04-20: Holland & Knight's Eduardo Arista recaps an April forum panel: principals use AI to draft diligence
  questions, pressure-test legal and tax scenarios and benchmark advisors' recommendations. Risks named are
  hallucination, waiver of attorney-client privilege when principals paste legal, tax or trust information into AI
  tools, and correcting what clients learned from AI [HK-PRINCIPALS-2026].
- 2026-05-11: Citi says adoption is slow but accelerating [CITI-AIFO-2026].
- 2026-06-24: IRS OPR applies Circular 230 duties, including fees, to AI [IRS-OPR-2026].
- 2026-07-30: Mercer Advisors unveils Aspen's second generation; Compound Planning announces CompoundAI agents
  [MERCER-ASPEN-2026].
- 2026-08-05: AICPA says developing or hosting AI for an attest client can raise independence concerns
  [JOFA-ETHICSAI-2026].
- 2026-09-29: RBC and Campden: half of offices say AI is embedded and essential; cybersecurity is the top near-term
  concern [RBC-CAMPDEN-2026].

## 9. Common objections

- **"Our families' data is too sensitive."** Sources agree privacy is the gate: Citi says solutions that cannot
  guarantee security are unlikely to be adopted [CITI-AIFO-2026]. Response: write the policy first (approved tools,
  what data may go where, what needs review) [NT-FOAIPOLICY-2026], ask vendors whether client data trains models and
  where it is stored [ARMANINO-FOTRENDS-2026], then start with a reviewed step (`#02`).
- **"AI makes things up."** A vendor executive on a panel calls hallucination often a data-governance problem
  [HUBBIS-ETON-2026];
  forum speakers warn that models are trained to please and prompts should say what the AI must not do
  [WISS-FOAI-2026]; an estate-planning example shows a wrong legal explanation [AFS-FOAI-2024]. Response: drafts a
  person signs off, and no AI near money movement or posting [ARMANINO-FOTRENDS-2026].
- **"Our data isn't ready."** Agree. Forum speakers put data before tools [WISS-FOAI-2026]; Armanino asks for a
  system of record and owners first [ARMANINO-FOTRENDS-2026]. Response: map entities and the system of record as
  the first project.
- **"Everyone already uses AI, the surveys say so."** The figures measure different things: 22% use it for operations
  or investment analysis [CITI-AIFO-2026], half say it is embedded [RBC-CAMPDEN-2026], 86% say they use AI technology
  [OCORIAN-IFC-2026], and J.P. Morgan's 65% is about AI as an investment theme [ARMANINO-FOTRENDS-2026].
- **"There are too many vendors; we'll wait."** Squire Patton Boggs flags vendor opacity and dependence on external
  AI systems [SQUIRE-FOAIRISK-2026]; CIO, citing PwC, reports a crowded market driving wait-and-see [AICIO-FOOPTEST-2026].
  Response: pick one tedious task and start [WINGSPAN-FOREPORT-2026]; run vendor diligence before go-live
  [WISS-FOAI-2026].
- **"Families want a person, not a bot."** Agree: Kaufman Rossin says the human connection cannot be automated
  [KAUFMAN-FO-2026]. Response: use AI on the back office and preparation (`#02`, `#09`) so advisors spend more time
  with the family.
- **"Most AI projects fail."** A panel write-up gives the share as 70% or 95% without saying who cited it or where
  it comes from [HUBBIS-ETON-2026]; do not repeat it as a figure. Response: start narrow and measure (§5).
- **"AI fraud makes this riskier."** It raises the stakes for payment controls, which are procedural
  [CFO-DEEPFAKE-2026]. Response: dual authorization and call-backs before any automation (`#07`).

## 10. Sources

Full details for keys used in the use cases are in the YAML. Keys cited above that are not in the YAML:

- JOFA-CASTIPS-2025: "Tips for providing the CAS services clients want", Journal of Accountancy, 2025-07-01, https://www.journalofaccountancy.com/issues/2025/jul/tips-for-providing-the-cas-services-clients-want/
- OCORIAN-IFC-2026: "Family offices embrace AI for operations but hold back on investment" (reports an Ocorian study), IFC Review, 2026-04-10, https://www.ifcreview.com/?p=17434
- PWC-USFB-2025: "PwC 2025 US Family Business Survey", PwC US, page dated 2026-03-16, https://www.pwc.com/us/en/services/audit-assurance/private-company-services/library/family-business-survey.html
- PCAOB-RULES3520-2026: "PCAOB Rules, Section 3 (Rules 3520-3526)", PCAOB, 2026 (rules effective 2006-2014), https://pcaobus.org/about/rules-rulemaking/rules/section_3
- WEALTHCOM-SERIESB-2026: "Wealth.com: $65 Million Series B Raised To Accelerate AI-Powered Estate And Tax Planning Platform", Pulse 2.0, 2026-04-16, https://pulse2.com/wealth-com-65-million-series-b-raised-to-accelerate-ai-powered-estate-and-tax-planning-platform/
- HK-PRINCIPALS-2026: "When Principals Ask AI Instead Of Their Advisors" (Eduardo Arista, Holland & Knight, recapping a Family Office Fintech Forum panel), Family Wealth Report republication, 2026-04-20 (Holland & Knight date, seen in search; the firm URL https://www.hklaw.com/en/insights/publications/2026/04/when-principals-ask-ai-instead-of-their-advisors returned 404), https://www.familywealthreport.com/printarticle.php?id=207483 (read in full)
