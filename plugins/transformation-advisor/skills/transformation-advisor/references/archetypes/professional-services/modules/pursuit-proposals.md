# Pursuit and proposals (professional services)

Last reviewed 2026-10-19. Use cases live in `../use-cases/pursuit-proposals.yaml` (20 entries: A 0, B 10, C 7, D 3). Ids
are shortened here: `#06` means `professional-services-pursuit-proposals-06`; other modules' ids are in full. Source
keys in brackets are in the YAML or in §10 (keys marked * are only in §10). **Read this first:** pursuit is where AI is
most widely used and least measured. Loopio's survey of 1,533 bid professionals (all industries, run with APMP, the
Association of Proposal Management Professionals) finds 79% of teams use AI, yet only 17% name a better win rate as a
benefit, and the average win rate fell from 45% to 39% [LOOPIO-TRENDS-2026]. No firm publishes a measured outcome: every
firm figure is a recollection, estimate, projection or undefined vendor number, mostly in vendor case studies, so
nothing reaches grade A. No error rate, override rate or win-rate study of AI-drafted bids was found. Law and
engineering firms dominate the named examples; accounting has one (Cherry Bekaert) and consulting very few (Neudesic,
Versent, an unnamed Big 4 firm).

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

How a firm wins specific new work: deciding whether to bid (go/no-go), reading a request for proposals (RFP) or request
for information (RFI), finding credentials, bios and past answers, drafting with subject-matter experts (SMEs) and
reviewing the response, answering the client's questions about the firm's own AI use, preparing the pitch, and learning
from wins and losses. It also covers in-house buyers using AI to scope RFPs and compare proposals (tagged `in-house`).
Relationship intelligence and key-account work (business development, BD) sit in client-development; fee design in
scoping-pricing; conflicts and client terms after acceptance in acceptance-risk.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Qualify (go/no-go) | Decide whether to bid on fit, odds, cost and capacity | expert-judgment, data-reporting | Go/no-go use at its lowest since 2021 while volume rises [LOOPIO-TRENDS-2026] |
| Read the solicitation | List requirements, deadlines, mandatory terms; spot "wired" RFPs | review-assurance | A missed clause disqualifies; checking happens late (`#06`) |
| Screen client terms | Compare outside counsel guidelines (OCGs) and RFP terms with the firm's own | review-assurance | Deal-breakers found late, by hand (`#19`) |
| Find content and credentials | Past answers, matter experience, bios, CVs, case studies | research-synthesis | Ranked the most time-consuming stage, ahead of writing; 74% lack one source of truth [IKAUN-BENCH-2026] |
| Draft and coordinate | Answers, technical approach, SME input | document-production, coordination-scheduling | SME delays (48%) and locating content (46%) [QORUSDOCS-ITBRIEF-2026] |
| Shape the narrative | Executive summary, win themes, one voice | document-production | Multi-partner "Frankenstein" documents [ABA-LPMAI-2026] |
| Price and staff | Fee scenarios and team | expert-judgment | Held in scoping-pricing (professional-services-scoping-pricing-03) |
| Answer AI questions | Tools, governance, data use, savings; disclosure of AI in the bid | client-interaction, review-assurance | Firms "still gathering the data" clients ask for [TRI-LEGALWEEK-2026] |
| Review and approve | Accuracy, compliance, claims, partner or risk sign-off | review-assurance | One invented credential can disqualify (`#11`) |
| Produce and submit | Formatting, templates, portals | document-production, transaction-processing | 45% of RFPs go through online portals [LOOPIO-TRENDS-2026] |
| Prepare the pitch | Client research, orals rehearsal | research-synthesis, client-interaction | 24 hours of research at one firm before AI (`#08`) |
| Debrief and learn | Win/loss reasons, library updates, metrics | data-reporting | Lessons rarely reach the next bid (`#16`) |
| Buyer side (in-house) | Scope the RFP, compare responses, panel questions | review-assurance | More, and more similar, responses (`#20`) |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns an
outcome), reinvent (the service or operating model changes). **Automate:** `#03` is in production (B); `#05` has no
named customer (C). **Delegate:** only `#15` (C), with no firm running pursuit end to end through an agent.
**Reinvent:** no entry. The nearest signals are shifts in who drafts (partners, technical staff, practice groups; `#02`,
`#09`) and buyers reading bids with AI (`#13`, `#20`). No source shows a new service or pricing model born in pursuit.

**Qualification**
- Improve: `#07` go/no-go informed by experience data (law firm Stinson) and scoring of 30 to 40 past pursuits (B).
  `#06` also flags RFPs that look written for an incumbent (US government-contracting workshop; part of a B entry).

**Content, credentials and data**
- Improve: `#01` first drafts from an approved library at accounting firm Cherry Bekaert ("8 hours to 2", a manager's
  recollection), IT services firm Versent (600 hours a year, projected) and Serco (government services, adjacent) (B).
  `#02` archive search and chat: law firm Ballard Spahr ("X-Ray"; partners estimate about two hours saved per RFP),
  engineering firms Benesch and Woodard & Curran (B). `#04` lawyer bios rebuilt from time records (Baker Botts, B).
- Automate: `#03` pitchbooks, proposals and CVs generated from structured data at law firms Gordon Rees Scully
  Mansukhani (GRSM), Stinson and Gowling WLG, IT consultancy Neudesic and engineering firm Arup; GRSM reports "more than
  50%" less proposal time (B). `#05` reconciling duplicate and stale people and project records before retrieval (vendor
  to AEC firms, i.e. architecture, engineering and construction; C).

**Drafting and tailoring**
- Improve: `#09` partners drafting urgent responses on a legal AI platform; Harvey says law firm Lynn Pinker Hurst &
  Schwegmann answered in under 48 hours and won (vendor anecdote, B). `#10` executive summaries, win themes and one
  voice (C). `#13` tailoring when tailored text stops proving fit; independent platform studies (adjacent, B). `#14`
  proposal agents inside PSA (professional services automation) and experience platforms: Certinia, Kantata, Intapp
  (announced, C).

**Review and compliance**
- Improve: `#06` requirement extraction and compliance matrix (Benesch, B). `#11` accuracy, quality and claims check
  before submission (no named firm, C). `#19` idea: flag deal-breaker OCG and RFP terms before bidding (D).

**The client's AI questions**
- Improve: `#17` idea: a reviewed answer bank on AI use, governance and savings, backed by matter evidence (D). `#18`
  idea: a register of AI used in each bid for buyer disclosure questions (D). `#12` firm-approved assistants instead of
  personal chatbots, e.g. Ballard Spahr's "Ask Ellis" for awards and survey submissions (B).

**Pitch, learning and buyer side**
- Improve: `#08` client-needs and competitor brief; Baker Botts cut 24 hours of research by "more than half" (B).
- Improve (process): `#16` win/loss analytics linking AI use to outcomes (C). Delegate: `#15` agents directed across
  qualification, drafting and review (SMPS trend, Intapp Celeste claim; C).
- Buyer side (in-house), improve (process): `#20` RFP scoping and proposal comparison (Priori Scout announced;
  independent Ohio study of AI scoring of supplier bids; C).

**Held elsewhere (do not duplicate):** professional-services-client-development-05, -06, -07 (relationship intelligence,
briefs, BD assistants), -10 (Celeste playbooks), -12 (AI claims in marketing), -14 to -16 (value conversations, matter
evidence, AI terms), -17 (in-house OCG addenda), -18 (AI-moderated win/loss interviews), -19 (attribution);
professional-services-scoping-pricing-02, -03, -05, -09, -10, -12 (estimates, fee scenarios, SOWs, savings evidence,
public-sector AI declarations); professional-services-knowledge-management-04 (experience location);
professional-services-acceptance-risk-10, -11 (client terms, AI-restriction registers);
professional-services-work-production-11, -22, -25 (citation checks, tool rollout, per-matter AI records);
professional-services-talent-learning-06, -07, -11 (junior learning). No assurance, tax or security entry covers
pursuit.

## 4. Interview probes

Ask a head of bids or proposals, a CMO or BD director, a practice leader who signs off pitches, or (in-house) a
legal-operations lead who runs panels and RFPs.

1. **"Walk me through the last bid you declined. Who decided, on what data, and how much of it lived in a system?"**
   Reveals go/no-go maturity (`#07`) and whether experience and win/loss data exist to support it.
2. **"Where does approved content live, who owns each piece, and what stops AI drafting from something stale?"** Reveals
   library readiness for `#01`-`#03` and the stale-record risk (`#05`).
3. **"Which AI tools do bid writers use today, who approved them, and has any RFP, price or client content gone into a
   tool outside your contract terms?"** Reveals shadow use and the case for `#12`.
4. **"After AI, did saved hours go into more bids, more tailoring or more senior review? How do you know, and has your
   win rate moved?"** Reveals whether speed turned into selectivity or just volume (`#13`, `#16`).
5. **"A client asks how you use AI on their matter and what it saves them. Who writes that answer, from what evidence,
   and who signs it off?"** Reveals the gap behind `#17` and the claims risk in §6.
6. **"When a tender asks whether you used AI to write the bid, who answers, from what record?"** Reveals `#18` readiness
   and certification exposure.
7. **"Who verifies credentials, past-performance claims and matter references before submission? What was the last error
   caught, and are references cleared for confidentiality?"** Reveals the checkpoint in `#03` and `#11`.
8. **"Who drafts first now: proposal staff, partners, SMEs? What happened to the bid work juniors used to do?"** Reveals
   role shifts (`#02`, `#09`) and the learning risk (talent-learning).
9. **"How do you check OCG and RFP terms before you commit to bid, and who can say no?"** Reveals `#19` and the handoff
   to acceptance-risk.
10. **"What do you record after each win or loss, and does anyone read it before the next bid?"** Reveals `#16`.
11. **(In-house) "How do you make bids comparable, and what would you let AI score?"** Reveals `#20` and where the buyer
    keeps judgment.

## 5. Metrics and benchmarks

All survey figures below are vendor-published unless marked independent.

**Cross-industry bid teams (Loopio with APMP, 1,533 respondents, March 2026)** [LOOPIO-TRENDS-2026]
- AI use 79% (68% in 2024, 34% in 2023); 84% of users weekly, 43% daily. Tools: ChatGPT 57%, Copilot 57%, RFP software
  with built-in AI 43% (from 33%).
- 166 RFPs submitted a year (153); 55% of RFPs received were answered, the lowest in the report's history. Management
  consulting answered the most: 229 on average in 2025 against 155 in 2024.
- 33 hours per RFP (35 for top performers); average win rate 39% (45%); shortlisting rate 46% (54%). RFPs influence 40%
  of revenue on average, about half in management consulting. AI benefits named: faster response 47%, quality or
  consistency 40%, win rate 17%.

**Law firms (ikaun, Am Law 100/200 and NLJ 500 marketing and proposal leaders; sample size not stated)**
- 2026: 69% say proposal volume rose and none say it fell; 27% actively use AI in proposals; 74% lack one current source
  of truth for matter experience; 7% find experience "very easy" to locate; over half still build in Word
  [IKAUN-BENCH-2026]. 2025: 79% rely on mostly or entirely manual processes; 68% bypass official tools
  [LEGALIT-IKAUN-2025*].

**AEC firms (Unanet, sample size not stated)** - 71% submit more proposals; win rates 56%, 52%, 50% for 2024-2026; 29%
have high confidence in the data under their AI; 17% build their own agentic workflows; 92% have a go/no-go process, 47%
a formal one [BDC-UNANET-2026].

**Other surveys** - QorusDocs (297 proposal professionals, half in professional or legal services): 60% say AI raised
volume handled, 35% credit higher win rates and revenue; most cannot answer 10-20% of incoming RFPs
[QORUSDOCS-ITBRIEF-2026]. Responsive and APMP 2025 (726): "Leaders" are likelier than "Novices" to use AI for workflow
orchestration (41% vs 17%), win/loss insight (37% vs 18%) and go/no-go (37% vs 26%) [RESPONSIVE-SRM-2025]; its 2026
report says 6 in 10 see positive ROI from most or all tools (detail gated) [RESPONSIVE-SRM-2026*].

**Price and effort:** a Perkins Coie pricing manager said lowest bids on reverse-auction platforms lose 54% of the time
and highest win 18% (panel remark, no denominator) [TRI-ILTACON-2025*]. A consulting vendor quotes 91 proposals a year
at about 24 hours each, seniors giving about 11 hours each; unsourced [PROJECTWORKS-BD-2026*].

**Independent evidence (all adjacent):** AI models aligned with human procurement staff on compliance signals but were
volatile on value-add claims across 123 Ohio IT bids [JBL-MCKINLEY-2026]; tailored cover letters lost signal value after
an AI tool arrived on a labour platform (51% weaker link to callbacks) [CUI-DIAS-YE-2025]; legal research tools
hallucinated 17-33% [STANFORD-MAGESH-2024].

**What to measure (recommend; nobody publishes these yet):** win and shortlisting rate for AI-assisted versus other bids
against a pre-AI baseline; hours and senior hours per bid; share of RFPs declined at go/no-go; errors caught at review
per bid; library freshness (share of content past its review date); time to answer a client's AI questions.

## 6. Guardrails

**Confidentiality and tools.** Do not draft on public large language models (LLMs) that train on inputs; ABA Law
Practice calls it an "absolute no-no" [ABA-LPMAI-2026]. ABA Formal Opinion 512: informed consent before putting
representation information into self-learning tools, boilerplate is not enough, and duties extend to prospective and
former clients; reusing one client's matter information in another's pitch may breach duties [ABA-OP512-2024].
California: no confidential input to risky tools without consent [CALBAR-GENAI-2026]. Check the solicitation's own
handling rules before uploading it [BIDLAB-2026]. A commentary on the SRA's 2026-08-17 warning notice puts tool approval
with the firm [JMW-SRA-2026].

**Accuracy and claims.** Check every word, including success stories, awards and bios [ABA-LPMAI-2026]; a named person
signs off each factual claim [BIDLAB-2026]. Claims about the firm's AI must be true: the SEC settled with two investment
advisers over false AI claims to prospects (USD 400,000) and the FTC says there is no AI exemption [SEC-2024-36;
FTC-AICOMPLY-2024]. Consultants must not overstate AI expertise in proposals [ICMCI-AICODE-2026, s.11.2]; Florida lets
lawyers advertise AI use but not claim superiority unless objectively verifiable [FLBAR-OP241-2024]. **Client
instructions:** disclose AI practices when a client asks or its guidelines require it [ABA-OP512-2024, p.8]; follow
client limits on AI [CALBAR-GENAI-2026]. Some clients demand AI savings while others forbid AI without permission
[TRI-LEGALWEEK-2026].

**Buyer rules.** UK PPN 017 (2025-02-17): supplier AI use "is not prohibited"; optional, unscored disclosure questions;
buyers may ask bidders to confirm AI text was checked [PPN-017-2025]. California requires disclosure of generative AI in
deliverables, with possible disqualification; it does not cover AI used to write the bid [CALDGS-SCM2302-2025]. No
general US federal rule requires disclosing AI used in drafting as of August 2026 [BIDLAB-2026]. Australia's public
service will require panel suppliers to advise planned AI use in quote responses [CANBERRATIMES-APSAI-2025].

**Evaluators and agents.** Federal evaluators may summarise proposals with undisclosed AI, a bid-protest risk per one
commentary [NATLAW-BRADLEY-2026]; NSF bars reviewers from uploading proposals to unapproved tools [NSF-GENAI-2023]. More
autonomy needs more oversight, and no autonomous external transmission of client information without safeguards and
human review [CALBAR-GENAI-2026]; barristers stay responsible when AI is used [MONDAQ-BSB-2026].

**Steps that need human judgment:** whether to bid; any claim about credentials, past performance or the firm's AI; use
of one client's matter as another's credential; acceptance of client terms; price; the final submission and any
certification; what to say in the pitch room.

## 7. Roles and how they evolve

- **Proposal function.** Cherry Bekaert replaced side-of-desk RFP work with a dedicated proposal function, built by its
  "Sr. Manager, Pursuit and Sales Asset Leader" [LOOPIO-CHERRYBEKAERT-2026]. A posting titles a role "Proposal Manager
  (RFX and AI Orchestration)", with human validation of AI output [RANDSTAD-PROPOSALMGR-2026]. Proposal staff are
  described as moving from doing tasks to directing agents (vendor summary) [KANTIV-SMPSQ2-2026]. Latham & Watkins'
  Innovation Attorney supports panels, pitches and RFPs [LATHAM-INNOVATIONATTY-2026]; BD leaders argue for a seat on the
  firm's AI council [PASSLE-EP177-2025*].
- **Who drafts widens.** GRSM says proposal work is spread more evenly [IKAUN-GRSM-2026]; Benesch's technical staff
  draft their own approaches [KANTIV-BENESCH-2026]; Harvey describes partners drafting without waiting for BD
  [HARVEY-BD-2026]; Ballard Spahr's IP group runs its own RFPs [TRI-INSIDELEGALAI-2025].
- **Reviewers become verifiers;** skills shift to strategy, storytelling and quality control [NYREJ-SMPSNY-2026]; 51% of
  teams say they will need AI and automation skills [LOOPIO-TRENDS-2026].
- **Most surveyed teams are not cutting people:** 16% replaced internal people resources with AI, 32% say leadership
  expects new responsibilities [LOOPIO-TRENDS-2026]; more than half of AI adopters are adding staff
  [RESPONSIVE-SRM-2025]; 13% of AEC firms expect workforce reductions [BDC-UNANET-2026].
- **Juniors:** associates are likelier than seniors to say AI has not changed their role [LOOPIO-TRENDS-2026]; a
  patent-drafting trial found durable skill gains concentrated in seniors [NBER-AUTOR-2026*] (see talent-learning).
- **In-house:** legal operations moves from reading each bid to reviewing comparisons [ABA-LPMRFP-2026].

## 8. Frontier

- 2026-04-07: Priori announces Scout for outside-counsel selection (in-house) [PRIORI-SCOUT-2026]. 2026-04-16: Introhive
  MCP server (a standard connector for AI assistants) preview for pitch preparation [INTROHIVE-MCP-2026]. 2026-04-17:
  Stanford panel asks how in-house leaders judge firms' AI in pitches [STANFORD-GENLEGAL-2026*].
- 2026-06-08: commentary on undisclosed AI in federal proposal evaluation [NATLAW-BRADLEY-2026]. 2026-06-17: GSA draft
  clause on data in LLM systems [FEDREG-GSA-2026]. 2026-06-23: Harvey BD guide with a won-pitch story [HARVEY-BD-2026].
- 2026-07: ABA reports AI questions in law-firm RFPs and legal departments comparing bids with AI [ABA-LPMRFP-2026];
  2026-07-13: vendor summary says agentic AI for proposals topped the SMPS Foundation's Q2 2026 AI trends, with an "AI
  slop" backlash [KANTIV-SMPSQ2-2026]; 2026-07-15: Intapp Celeste generally available [LAWSITES-CELESTE-2026];
  2026-07-31: a job posting at legal-AI vendor Legora targets 90% of technical RFP response content automated in six
  months, with human review [LEGORA-JOB-RFP-2026*].
- 2026-08-17: SRA AI warning notice [JMW-SRA-2026; LGL-SRA-2026*]. 2026-08-25: adviser says vendors write bids for
  machine evaluators too [UPPEREDGE-PROPTRAP-2026]. 2026-09-11: Stinson partners in Law360: reinvest saved time in the
  client [STINSON-LAW360-2026].
- 2026-10-07: "Is this RFP wired?" capture-agent workshop [G2X-CAPTURE-2026]. 2026-10-08: Litera's CEO calls RFPs the
  first place clients feel a firm's AI investment [LAWSITES-LITERA-2026]. 2026-10-13: 84% of partners expect AI-driven
  BD within 18-24 months [INTROHIVE-LAWSITES-2026].
- Scheduled, not evidence: TRI CMBDO Forum, 2027-01-27 to 29, sessions on the firm's AI story in pitches and visibility
  in AI-driven discovery [TRI-CMBDO34-2027].

## 9. Common objections

- **"AI makes us faster, so we'll win more."** Not shown: win rates fell while AI use rose, and only 17% see a win
  benefit [LOOPIO-TRENDS-2026; BDC-UNANET-2026]. Use saved time to tailor and to say no more often (`#07`, `#13`).
- **"AI output all sounds the same."** Committees are said to spot generic text [KANTIV-SMPSQ2-2026], and independent
  studies show tailored text losing value as a signal [CUI-DIAS-YE-2025]. Ground drafts in the firm's own history and
  add evidence AI cannot invent (`#02`, `#13`).
- **"It will make things up."** It can: one invented credential can disqualify [KANTIV-TRUST-2026]. Retrieve approved
  content rather than generate freely, and keep a named verifier [LOOPIO-CHERRYBEKAERT-2026; BIDLAB-2026].
- **"We can't put RFPs into AI."** Not into public tools that train on inputs [ABA-LPMAI-2026]; approved tools with
  no-training terms are the route, as Ballard Spahr chose (`#12`). Check each solicitation's handling rules.
- **"Do we have to tell the buyer?"** No general US federal rule requires it for drafting as of August 2026, but read
  each solicitation; some disqualify for undisclosed AI in deliverables [CALDGS-SCM2302-2025; BIDLAB-2026]. Keep a
  record (`#18`).
- **"Clients only want a list of our tools."** Clients call a product name an unacceptable answer and want matter-level
  detail [PARKERPOE-TR-2026; LAWSITES-LITERA-2026] (`#17`).
- **"Vendor case studies prove the ROI."** They give recollections and projections with no baseline (§5). Ask for a
  before-and-after on your own bids; only 18% of organisations measure AI return on investment [TR-AIPS-2026*].

## 10. Sources

Full details (title, URL, date, locator, access) are in the YAML. Keys marked * are not in the YAML.

- **Regulators and professional bodies:** PPN-017-2025, PPN-0224-2024, CALDGS-SCM2302-2025, FEDREG-GSA-2026,
  NSF-GENAI-2023, NIH-NOTOD25132-2025, SEC-2024-36, FTC-AICOMPLY-2024, CALBAR-GENAI-2026, ABA-OP512-2024,
  ABA-LPMAI-2026, ABA-LPMRFP-2026, ICMCI-AICODE-2026, FLBAR-OP241-2024, LGL-SRA-2026* (Local Government Lawyer,
  2026-08-17). **Academic:** JBL-MCKINLEY-2026, CUI-DIAS-YE-2025, GALDIN-SILBERT-2025, NOY-ZHANG-2023,
  STANFORD-MAGESH-2024, NBER-AUTOR-2026* (NBER Working Paper 35720, 2026-09).
- **Surveys:** LOOPIO-TRENDS-2026, QORUSDOCS-ITBRIEF-2026, IKAUN-BENCH-2026, BDC-UNANET-2026, RESPONSIVE-SRM-2025,
  INTROHIVE-LAWSITES-2026, TR-FOP-2026, TRI-STANDOUT-2026, SOURCE-PRECISION-2026, DAYSHAPE-ONREC-2026,
  LEGALIT-IKAUN-2025* (Legal IT Insider, 2025-06-17), RESPONSIVE-SRM-2026* (Responsive report landing page, 2026),
  TR-AIPS-2026* (Thomson Reuters, 2026).
- **Conferences and events:** TRI-LEGALWEEK-2026, TRI-CMBDO34-2027 (scheduled), LMA-DECENT-2026, G2X-CAPTURE-2026,
  TRI-ILTACON-2025* (TRI, 2025-09-02), STANFORD-GENLEGAL-2026* (Stanford Law School, 2026-04-17).
- **Firms and job postings:** VERSENT-BIDASSISTANT-2025, STINSON-LAW360-2026, BROWNEJACOBSON-AIPROC-2025,
  UPPEREDGE-PROPTRAP-2026, UPPEREDGE-SI-2025, JMW-SRA-2026, MONDAQ-BSB-2026, RANDSTAD-PROPOSALMGR-2026,
  LATHAM-INNOVATIONATTY-2026, LEGORA-JOB-RFP-2026* (Legora job posting, 2026-07-31).
- **Vendors:** LOOPIO-CHERRYBEKAERT-2026, LOOPIO-BLOG-2026, KANTIV- (BENESCH, WOODARD, ROBINS, SMPSQ2, COPILOT, GONOGO,
  TRUST; all 2026), IKAUN- (GRSM, NEUDESIC, ARUP, STINSON, GOWLING; 2026), AUTOGENAI-SERCO-2025, AUTOGENAI-BIG4-2025,
  HARVEY-BD-2026, HARVEY-LPHS-2025, INTROHIVE-MCP-2026, CERTINIA-VEDA-2026, CERTINIA-SOA-2026, KANTATA-ENGINE-2025,
  INTAPP-EXPERIENCE-2026, INTAPP-DEALCLOUD-2026, PRIORI-SCOUT-2026, KOJI-PSDOCS-2026, BIDLAB-2026, LITERA-GCRFP-2026,
  PARKERPOE-TR-2026, PROJECTWORKS-BD-2026* (Projectworks blog, 2026-06-23).
- **Press, podcasts, community:** TRI-INSIDELEGALAI-2025, LAWSITES-CELESTE-2026, LAWSITES-LITERA-2026, LAWFUEL-2025,
  NYREJ-SMPSNY-2026, NATLAW-BRADLEY-2026, TGC-WK-2025, CANBERRATIMES-APSAI-2025, HINZ-BPCNASHVILLE-2025,
  PASSLE-EP177-2025* (Passle CMO Series podcast, 2025-08-12; show notes).
