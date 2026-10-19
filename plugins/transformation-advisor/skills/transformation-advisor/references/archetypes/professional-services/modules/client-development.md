# Client development (professional services)

Last reviewed 2026-10-19. Use cases live in `../use-cases/client-development.yaml` (22 entries: A 0, B 11, C 10,
D 1). Ids are shortened here: `#06` means `professional-services-client-development-06`; other modules' and
archetypes' ids are in full. Source keys in brackets are in the YAML or in §10 (keys marked * are only in §10).
**Read this first:** no firm publishes a measured result for AI in client development: no revenue, retention,
win-rate, accuracy or override figure. The named deployments are relationship-data tools at law and accounting
firms, and every figure about them is vendor-published. The strongest evidence is about clients: they say AI
matters and that firms are not delivering or talking about it. Consulting firms publish almost nothing on this.

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

How a firm keeps and grows the clients it already has (business development, BD): relationship data and intelligence, key-account plans and
cross-sell, meeting preparation and outreach, the conversation with each client about AI (what it changed, what it
saved, what the terms are), client feedback and retention, and AI offered to clients as part of the relationship.
Examples come from law, accounting and consulting firms and from in-house legal teams as buyers (tagged `in-house`).
RFP and pitch response sits in pursuit-proposals; fee design in scoping-pricing; time capture and invoices in
billing-collections; conflicts and intake checks in acceptance-risk.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Capture relationship data | Contacts, meetings and emails reach the CRM (client relationship management system) | data-reporting | Partners do not log activity; CRM adoption "negligible" [INTROHIVE-LAWSITES-2026] |
| Map relationships and coverage | Who knows whom, strength, warm paths, gaps, departures | research-synthesis | 78% of 123 partners say their tools give relationship visibility that is hard to act on [INTROHIVE-PARTNER-2026] |
| Plan key accounts and cross-sell | Account plans, opportunity lists, service-line coordination | expert-judgment, coordination-scheduling | Partners name where to focus (50%) and cross-sell (43%) as top frictions [INTROHIVE-PARTNER-2026] |
| Find new opportunities | Signals from courts, news, filings and internal data | research-synthesis | Manual searching busy lawyers cannot sustain (`#05`) |
| Prepare and reach out | Meeting briefs, client notes and alerts, check-ins | research-synthesis, document-production | Senior lawyers skip client notes because they take billable time [TRI-CMBDO-2026] |
| Market capability and take enquiries | Credentials, thought leadership, website enquiries | document-production, client-interaction | AI claims are regulated marketing; chatbots can create relationships by accident (`#12`, `#13`) |
| Hold the AI value conversation | Disclose AI use, show what changed, agree terms and value sharing | client-interaction, expert-judgment | Firms "still gathering the data" [TRI-LEGALWEEK-2026]; partners rarely raise it [TRI-STANDOUT-2026] |
| Agree client AI terms | Engagement letters, outside counsel guidelines (OCGs), renewals | document-production, review-assurance | Boilerplate consent is not enough; clients send opposite instructions (`#16`, `#17`) |
| Listen and act on retention risk | Feedback, win-loss and matter-close debriefs, health alerts | data-reporting | Periodic, siloed programmes; quiet clients drift (`#03`, `#18`) |
| Measure BD return | Attribute mandates and revenue to relationships | data-reporting | 63% of firms have no revenue-linked measure [INTROHIVE-LAWSITES-2026] |
| Offer AI to clients | Labs, portals, licensed tools, AI advisory | client-interaction | No usage or revenue data; fear of clients doing it themselves [ABAJ-SHARE-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns an
outcome), reinvent (the service or relationship model changes). **Automate:** `#01` is in production (B); `#13`
has no named firm (C). **Delegate:** only a vendor announcement (`#10`, C) and an idea (`#11`, D); no firm runs
client development through an agent. **Reinvent:** `#21` and `#22` (B), with no usage or revenue figures.

**Relationship data and intelligence**
- Automate: `#01` email and calendar capture into the CRM at accounting firms Schneider Downs, KSM, LBMC and Grassi
  and law firm Thomson Snell & Passmore; figures are vendor activity counts (B).
- Improve: `#02` relationship maps and warm paths; law firm Thomson Snell & Passmore went from 47 to 97 employees
  connected to its Top 50 accounts (vendor-published, B). `#03` health scores and at-risk alerts (Howes Percival, B).

**Account planning and opportunity**
- Improve (process): `#04` key-account plans and cross-sell lists, with independence checks for CPA firms (C).
  `#05` opportunity scouting at law firms Akin Gump ('Moneyball') and Quinn Emanuel (daily deep-research scans) (B).

**Preparation and outreach**
- Improve: `#06` pre-meeting briefs (Grassi, LBMC, Thomson Snell & Passmore; B). `#07` partners move from
  general-purpose chatbots to assistants grounded in firm relationship data (Introhive's MCP connector, a standard way for assistants to query a system; Intapp
  Celeste; C). `#08` nudges and drafted client notes (C). `#09` call summaries and coaching (C).
- Delegate: `#10` Celeste runs origination and BD playbooks (announced, C). `#11` idea: agent-run outbound
  sequences (D).

**Marketing and enquiries**
- Improve: `#12` AI claims in marketing (Akin Gump, Debevoise and Parker Poe publicise their own AI tools); 52% of
  the largest law firms market their AI use versus 2% of the smallest (B). No firm describes drafting this content with AI. Automate: `#13` website intake chatbots under Oregon and Florida bar rules (C).

**AI value conversations and client terms**
- Improve (process): `#14` partner-led value conversations, sequenced from what changed to price (B). `#15`
  matter-level evidence of AI use (Legora and Laurel announced 2026-10-13; C). `#16` AI terms in engagement
  letters, e.g. Babst Calland's published consent terms (B). `#17` in-house teams add AI addenda to OCGs (in-house, C).

**Listening and measurement** - improve: `#18` AI-analysed client feedback (Shoosmiths, 2023; C); `#19` attribution (C).

**AI offered to clients (reinvent)**
- `#20` client AI labs and joint use cases (Parker Poe, Fasken; GSK as a client voice) (B). `#21` firm-built
  tools and portals: Debevoise STAAR, Cooley GO Lab, A&O Shearman with Harvey, Legora Portal (B). `#22` client
  AI-enablement roles (Latham & Watkins) (B); AI advisory for accounting clients is discussed at events but not
  evidenced as a delivered service.

**Held elsewhere (do not duplicate):** fee side of the value conversation (professional-services-scoping-pricing-10),
matter-level savings for pricing (professional-services-scoping-pricing-09), AI cost terms (-07), client savings
terms in OCGs (-11), licensing firm tools (-23); per-matter AI records and client terms at matter opening
(professional-services-work-production-25), shared workspaces (-20); audit engagement terms
(assurance-acceptance-independence-11) and AI services to audit clients (assurance-acceptance-independence-15);
tax client communications (tax-compliance-individual-business-15) and co-built client tax agents
(tax-research-advisory-24).

## 4. Interview probes

Ask a managing partner, CMO or BD director, key-account partner or (in-house) a GC or legal-operations lead.

1. **"What share of client meetings and emails reaches your CRM without anyone typing, and who can see it?"**
   Reveals data readiness for everything else (`#01`-`#03`) and the privacy and ethical-wall position.
2. **"Before your last three key-client meetings, who prepared the brief, how long did it take, and did the
   partner use it?"** Reveals whether `#06` saves time or adds a document nobody reads.
3. **"When a key client last asked how you use AI on their work and what they get from it, who answered, with
   what evidence?"** Reveals the conversation gap (`#14`) and evidence gap (`#15`).
4. **"When did a partner last raise AI with a key client unprompted? What did they lead with: value or
   discount?"** Reveals partner readiness; Thomson Reuters Institute (TRI) research finds many do not raise it [TRI-STANDOUT-2026].
5. **"Do you hold every client's instructions on AI (permitted, prohibited, disclosure, billing) in one place?
   Could two conflict on one matter?"** Reveals exposure under `#16`-`#17` and California's rule to follow
   client limits [CALBAR-GENAI-2026].
6. **"Which signals tell you a key account is cooling, where do they live, and what happens when one fires?"**
   Reveals whether `#03` has an owner and action, or only a dashboard.
7. **"How do you decide which clients to offer another service, and who checks conflicts or independence
   first?"** Reveals `#04` maturity and the attest-client constraint for accounting firms.
8. **"Do partners use ChatGPT or Copilot for BD research or drafting today? With client names in it?"** Reveals
   shadow use and the case for a governed assistant (`#07`).
9. **"Does any AI tool send messages, emails or chatbot replies to clients or prospects without a person reading
   them first? Where is the line?"** Reveals autonomy risk (`#10`, `#11`, `#13`).
10. **"How do you know whether relationship or BD tools lead to revenue, and what would partners accept as
    proof?"** Reveals the attribution gap (`#19`) and partner resistance.
11. **"How do you collect client feedback today, and have you asked clients what they think of AI-enabled
    work?"** Reveals listening maturity (`#18`).
12. **"Have you built anything with a client, or given clients access to firm AI? Who owns it, and how is it
    priced?"** Reveals appetite and governance for `#20`-`#22`.

## 5. Metrics and benchmarks

**Client pressure (survey perceptions, not outcomes)**
- 78% of corporate clients call AI-enabled quality gains very important or essential; 6% say most or all providers
  deliver them; 32% have reconsidered, or plan within 12 months to reconsider, firms they feel are falling behind, a third of those with more
  than $1 million of work at risk (1,816 professionals, Mar-Apr 2026; client subset size not stated) [TR-FOP-2026].
- In-house (657 respondents, 30 countries, 2025): 59% see no GenAI savings from law firms yet; 24% satisfied; 61%
  plan to push for change [ACCEVERLAW-2025]. Vendor co-published.
- 54% of corporate legal respondents say firms should use AI on their matters, 29% know it is used, 67% do not know;
  41% of law firms get both "use AI" and "don't" from different clients [TR-AIPS-2026].

**The conversation (law and accounting)**
- About one-third of heavy-AI-user stand-out partners had discussed AI with 60%+ of clients; more than one-third
  of stand-out lawyers with fewer than 20%. Embedded users report significant impact about nine times as often as
  minimal users [TRI-STANDOUT-2026].
- 61% of law firms say they proactively discussed Harvey efficiencies; 4% of in-house teams say firms approached
  them (Harvey-commissioned survey of 87 Harvey customers: 60 firms, 27 in-house teams, not matched pairs)
  [LEGALIT-RSGI-2026].
- 35% of legal-finance respondents name partner discomfort as the top communication barrier; 56% see more client
  demand for AI efficiencies or transparency [BIGHAND-LF-2026]. 32% of law firms cannot confidently show AI value
  to their most important client [LITERA-LAWSITES-2026].
- Accountants: 33% volunteer how they use AI; 60% say clients ask for proof of AI data protection always or
  frequently (725 respondents, Intuit) [INTUIT-AT-2026].
- Measurement: 18% of organisations collect AI ROI metrics [TR-AIPS-2026]; 85% of law firms and 75% of legal
  departments do not collect AI ROI data or are unsure [TRI-GREATDISCONNECT-2026].

**Relationship data and BD (123 partners in law, accounting and other firms; vendor-commissioned)**
- 57% of firms at basic data or visibility maturity; 84% expect structured or AI-driven BD within 18-24 months;
  68% of AI-using partners rely only on general-purpose tools (satisfaction 6.7/10); 63% have no revenue-linked BD
  measure, 15% strong attribution [INTROHIVE-LAWSITES-2026; INTROHIVE-PARTNER-2026].
- Law-firm AI policy by size: client approval required 8%-38%; formal policy 57%-98%; AI use marketed 2%-52%;
  training before access 11%-72% [ILTA-TECHSURVEY-2026].
- Accounting: net promoter score 37 at 6-9 years' tenure against 84 at 15+ years; 91% of clients want proactive
  advisory, 4% call their firm primarily advisory (180 clients, vendor-linked post) [CUSTOMERTHINK-2026].
- Consulting: tech-consulting spend forecast +7.5% in 2026, with needs differing by sector and budget holder
  [SOURCE-PRECISION-2026*]; 17% of firms continue the value conversation after the work (base not stated)
  [SOURCE-VALUE-2025*].

**Single-firm tool figures (all vendor-published, no baseline):** Schneider Downs 3.1 million meetings and emails
ingested; LBMC $197,115 "ROI from time savings"; Thomson Snell & Passmore 47 to 97 employees on Top 50 accounts
(`#01`, `#02`). Introhive's home page claims +30% referrals and cross-sell revenue and +36% win rates with no
cohort [INTROHIVE-HOME-2026]. Nearest independent evidence is adjacent: retail sales field experiments
[FANG-ARXIV-2026*].

**What to measure (recommend; nobody publishes these yet):** share of client activity captured automatically; key
clients with an AI conversation in 12 months; alert-to-action rate; partner overrides on AI briefs; cross-sell
conversion and key-account retention against a pre-AI baseline; client feedback on AI-enabled work.

## 6. Guardrails

**Confidentiality and agent access (law).** Persistent AI access to email and client files raises acute
confidentiality questions; limit scope and keep monitoring. No autonomous external transmission of client
information without safeguards and human review; supervision scales with autonomy [CALBAR-GENAI-2026].
Firm-wide tools can expose information across ethical walls, and duties extend to prospective and former clients
[LOUBAR-2025; FMG-ABA512-2024]. Intapp says its agent applies the same walls as staff (vendor statement)
[LAWSITES-CELESTE-2026]. Privacy law on firm-wide email-metadata capture rests on a vendor statement
[INTROHIVE-PRIVACY-2024]; no regulator analysis was found.

**Telling clients and following their instructions.** California: consider disclosing intended AI use and follow
client limits [CALBAR-GENAI-2026]. ABA 512 as summarised: boilerplate consent is not enough; consult the client
where AI bears on fees [2CIVILITY-ABA512-2024; FMG-ABA512-2024]. UK: no specific SRA guidance; the Law Society
says agree use with the client [LAWSOC-GENAI-2026]. Consultants must disclose material AI use [ICMCI-AICODE-2026].
CPAs: no specific federal or CPA-standard mandate [JOA-DISCLOSE-2025]. Disclosure lowers trust, but being exposed
later is worse [SCHILKE-OBHDP-2025]: decide how to disclose, not whether.

**Marketing and enquiries.** No unverifiable superiority claims about AI; chatbots must say they are AI
[FLBAR-OP241-2024]; consultants must not overstate AI expertise [ICMCI-AICODE-2026, s. 11.2]. Oregon allows intake
chatbots with monitoring, disclaimers, conflict entry and lawyer approval of autonomous actions [OSB-FO-2026-208].
EU AI Act Article 50 transparency duties apply from August 2026 per the Commission [AIACT-ART50; EC-AIACT-2026].

**Outreach and recording.** AI-generated voice calls generally need prior express consent under the US TCPA
[FCC-24-17]. AI notetakers face wiretap claims; disclose and get all-party consent [BLOOMBERGLAW-OTTER-2026]. An
unreviewed reply to a client is a "one-way door" [TRI-AGENTIC-2026].

**Accounting independence.** AI-related nonattest services to attest clients can raise independence concerns
[JOA-ETHICS-2026]; see assurance-acceptance-independence-15. Tax data disclosure engages 26 USC 7216 [WOODARD-2025].

**Steps that need human judgment:** what to say to a client and when; whether to raise a new service; any claim
about AI use or savings; acceptance of client AI terms; any message to a client or prospect that carries client
information or advice; whether an intake conversation formed a relationship; attribution rules used in pay.

## 7. Roles and how they evolve

- **Partners** are the firm's "commercial transmission mechanism"; strategy fails unless they see how it changes
  client work [TRI-STANDOUT-2026]. They now take on BD once done by marketing [INTROHIVE-LAWSITES-2026].
- **BD and marketing** curate client lists and conversation openers ("plant things" in partners' minds, in one
  panelist's words) and train partners one-to-one [TRI-CMBDO-2026]; they take on claim substantiation (`#12`). AI purchasing is often led by IT or innovation, not
  BD [INTROHIVE-LAWSITES-2026].
- **New titles:** senior director of marketing and client intelligence (Akin Gump) [AKIN-MONEYBALL-2026]; chief
  pricing and innovation officer (Greenberg Traurig) and senior managing director of AI innovation (DLA Piper)
  [TRI-LEGALWEEK-2026]; Innovation Attorney - Client Team Enablement (Latham & Watkins)
  [LATHAM-INNOVATIONATTY-2026]; senior client culture manager (Shoosmiths) [EDINBURGHNEWS-SHOOSMITHS-2023].
- **In-house:** legal operations is the first line for AI pressure [TRI-LDOR-2026]; "legal engineer" has emerged
  as a profession, often non-lawyers [BLOOMBERGLAW-GCXAI-2026]. **Accountants** can become advisers on clients' AI
  adoption, says Ravical's CEO [RAVICAL-ACCOUNTANT-2025].

## 8. Frontier

- 2025-11-11: a Law Punx contributor predicts clients will consume legal services through AI; firms have to
  end-2027 to make knowledge AI-accessible [LAWPUNX-2025].
- 2026-02: Oregon opinion on intake chatbots and AI agents [OSB-FO-2026-208]; 2026-02-12: a GC says firms give
  clients nothing from AI [AL-INHOUSE-2026*] (in-house); 2026-02-18: panelists at TRI's chief marketing and BD officer (CMBDO) forum call BD a good starting
  point for agentic AI [TRI-CMBDO-2026].
- 2026-03-13: Legalweek: clients ask for matter-level savings; some refuse to pay for AI-done work [TRI-LEGALWEEK-2026].
- 2026-04-16: Introhive previews an MCP server for relationship data [INTROHIVE-MCP-2026].
- 2026-05: California guidance covers agentic AI; ICMCI publishes an AI code for consultants [CALBAR-GENAI-2026;
  ICMCI-AICODE-2026].
- 2026-07-14 and 07-15: firms reported sharing or licensing AI tools [ABAJ-SHARE-2026]; Intapp Celeste generally
  available with BD playbooks [LAWSITES-CELESTE-2026].
- 2026-08-06: firm leaders tell TRI that client pressure has reversed: a year earlier some clients asked firms not
  to use AI; now clients ask firms to demonstrate their AI capabilities [TRI-STANDOUT-2026].
- 2026-09-04: Litera announces firm AI search at ILTACON, routed here as BD intelligence from siloed data
  [LAWSITES-ILTACON4-2026*]; 2026-09-10: Parker Poe's client AI lab [PARKERPOE-LAWSITES-2026].
- 2026-09-14: ILTACON reversibility test; an Introhive speaker describes an agent watching for relationship change
  when a partner leaves [TRI-AGENTIC-2026]. 2026-09-28: corporate legal clients say judgment, transparency and
  speed now separate firms [TRI-AIFORUM-2026*] (in-house).
- 2026-10-13: Introhive partner survey; MCP server described as generally available; Legora and Laurel announce AI
  time capture with value measures to follow [INTROHIVE-LAWSITES-2026; LEGORA-LAUREL-2026].
- 2026-10-19: a CLO asks who will own the "legal memory" in shared AI environments [BLOOMBERGLAW-GCXAI-2026].
- Scheduled, not evidence: MCA "AI for SME Consultancies" 2026-11-06 [MCA-EVENTS-2026*]; TRI 34th CMBDO Forum
  2027-01-27 to 29, on the firm's AI story in pitches and visibility in AI-driven discovery [TRI-CMBDO34-2027*].

## 9. Common objections

- **"The relationship won the work, not the data."** Firms do contest attribution [INTROHIVE-LAWSITES-2026]. Agree
  attribution rules first and start with intermediate measures (`#19`); 63% have no revenue link at all.
- **"Partners will never use a CRM."** Then stop asking them to: capture runs without typing (`#01`) and prompts
  arrive in the daily workflow (`#08`). Then the data has to be accurate [INTROHIVE-LAWSITES-2026].
- **"Our clients aren't asking about AI."** Some are not yet: 42% of 144 respondents to a Virginia Society
  of CPAs survey say clients are not yet asking [VSCPA-AI-2026]. But 32% of corporate clients have reconsidered or
  plan to reconsider providers [TR-FOP-2026], and Harvey-customer firms and in-house teams report very differently
  on whether firms raised it: 61% vs 4% [LEGALIT-RSGI-2026].
- **"Telling clients about AI will cost trust."** It can [SCHILKE-OBHDP-2025], but being found out later is worse
  and the rules push disclosure of material use [CALBAR-GENAI-2026; ICMCI-AICODE-2026]. Design the wording (`#16`).
- **"If we show savings, they'll demand discounts."** Leading with concessions trains clients to expect them; lead
  with what changed for the client [TRI-STANDOUT-2026]. Fee options: professional-services-scoping-pricing-10.
- **"The billable hour isn't going anywhere."** One Legalweek partner sees no client-driven move to alternative fees
  [TRI-LEGALWEEK-CRISIS-2026*], and demand for Big Law hours rose 4.2% in H1 2026 [BLOOMBERG-AICOST-2026]. But 59%
  of in-house teams see no savings and 61% plan to push for change [ACCEVERLAW-2025].
- **"If we share our tools, clients will do the work themselves."** That fear is real [ABAJ-SHARE-2026], and one
  in-house participant valued building processes a team can run without the firm [PARKERPOE-LAWSITES-2026]. No data
  shows either loss or gain yet (`#21`).
- **"AI briefs are generic."** Use them as a foundation, not a script; one law-firm technology specialist put AI at about
  90% and judgment at the rest, and panelists urged one-to-one training [TRI-CMBDO-2026].
- **"Let an agent run BD."** Agents are limited by their data [TRI-CMBDO-2026]; California bars autonomous
  external transmission without review [CALBAR-GENAI-2026]. No firm runs it (`#11`).
- **"AI-enabled delivery wins work."** Reed Smith says so in a vendor customer story [HARVEY-REEDSMITH-2026*]; no
  win-rate data exists. Vendor ROI figures (`#01`, `#02`) have no baseline; ask for one.

## 10. Sources

Full details (title, URL, date, locator, access) are in the YAML. Keys marked * are not in the YAML; their publisher, date and URL are given inline. All sources were opened on 2026-10-19 except three job postings marked search-only in the YAML.

- **Regulators, professional bodies, academic:** CALBAR-GENAI-2026, OSB-FO-2026-208, WSBA-NWSIDEBAR-OSB-2026, FLBAR-OP241-2024, NYCBAR-OP2024-5, FMG-ABA512-2024, 2CIVILITY-ABA512-2024, LOUBAR-2025, LAWSOC-GENAI-2026, LAWSOC-AGENTIC-2026, JOA-DISCLOSE-2025, JOA-ETHICS-2026, ICMCI-AICODE-2026, AIACT-ART50, EC-AIACT-2026, FCC-24-17, SCHILKE-OBHDP-2025, SCHILKE-CONVERSATION-2025, STANFORD-DEL-2026, FANG-ARXIV-2026* (arXiv, Fang et al., v6 2026-06-29, https://arxiv.org/abs/2510.12049).
- **Surveys:** TR-FOP-2026, TR-AIPS-2026, TRI-STANDOUT-2026, TRI-GREATDISCONNECT-2026, TRI-LDOR-2026, TRI-VISIBILITY-2026, ILTA-TECHSURVEY-2026, ACCEVERLAW-2025, INTUIT-AT-2026, CPAPA-TECHSURVEY-2026, LITERA-LAWSITES-2026, BIGHAND-LF-2026, RAVICAL-ACCOUNTANT-2025, VSCPA-AI-2026.
- **Conferences and events:** TRI-CMBDO-2026, TRI-LEGALWEEK-2026, TRI-AGENTIC-2026, TRI-COOCFO-AI-2025, TR-NAVIGATING-2026, KARBON-ENGAGE-2026, TRI-LEGALWEEK-CRISIS-2026* (TRI, 2026-03-19, https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-new-existential-crisis), TRI-AIFORUM-2026* (TRI, 2026-09-28, https://www.thomsonreuters.com/en/institute/articles/what-ai-cant-replace), TRI-CMBDO34-2027* (TRI agenda, event 2027-01-27 to 29, https://www.thomsonreuters.com/en/institute/events/the-34th-annual-chief-marketing-business-development-officer-forum/), MCA-EVENTS-2026* (MCA events listing, event 2026-11-06, https://www.mca.org.uk/mca-events).
- **Firms and job postings:** AKIN-MONEYBALL-2026, PARKERPOE-LAWSITES-2026, DEBEVOISE-BLOOMBERG-2026, COOLEY-LAWCOM-2026, WOODARD-2025, BABSTCALLAND-TERMS-2025, LATHAM-INNOVATIONATTY-2026, LATHAM-ADAI-2026, BAKERMCKENZIE-CLIENTAIRISK-2026, WOLFGREENFIELD-2026.
- **Vendors:** INTROHIVE- (SCHNEIDERDOWNS-2026, KSM-2026, LBMC-2024, GRASSI-2026, TSP-2026, FORRESTER-2024, HOME-2026, PRIVACY-2024, MCP-2026, PARTNER-2026, ACCTXSELL-2026, SAM-2025, LAINGOROURKE-2025); INTAPP- (HOWESPERCIVAL-2025, DEALCLOUD-2026, ACTIVATOR-2026, PRACTUS-2026, WOTTONKEARNEY-2026, FORVISMAZARS-2026, Q3CALL-2026); HARVEY-BD-2026, CERTINIA-VEDA-2026, LEGORA-LAUREL-2026, LEGORA-PORTAL-2026, BRIDGENEXT-AGENTFORCE-2026, CONVENTUS-2026, MCL-SITE-2026, KOJI-LEGAL-2026, HARVEY-REEDSMITH-2026* (Harvey customer story, 2026-05-11, https://www.harvey.ai/customers/reed-smith).
- **Press, podcasts, community:** INTROHIVE-LAWSITES-2026, LAWSITES-CELESTE-2026, ABAJ-SHARE-2026, LEGALIT-RSGI-2026, BLOOMBERG-AICOST-2026, BLOOMBERGLAW-GCXAI-2026, BLOOMBERGLAW-OTTER-2026, TRI-INTERDEP-2026, AT-DECODE-2026, CUSTOMERTHINK-2026, EDINBURGHNEWS-SHOOSMITHS-2023, SJ-LISTENING-2024, SJ-LFMC-2026, LF-VALUEGAP-2026, LAWPUNX-2025, LPT-FEDER-2026, SOURCE-AI-2026, AL-INHOUSE-2026* (Artificial Lawyer, 2026-02-12, https://www.artificiallawyer.com/2026/02/12/we-get-nothing-from-law-firm-ai-use-client/), LAWSITES-ILTACON4-2026* (LawSites, 2026-09-04, https://www.lawnext.com/2026/09/iltacon-news-round-up-part-4-the-business-of-law-litera-aderant-oddr-tre-ai-intapp.html), SOURCE-PRECISION-2026* (Source Global Research, 2026-09-28, https://sourceglobalresearch.com/market-update/precision-segmentation-how-consulting-firms-can-target-clients-sector-and-functional-ai-budgets), SOURCE-VALUE-2025* (Source podcast page, 2025-09-09, https://sourceglobalresearch.com/podcast/how-to-talk-to-your-clients-about-value).
