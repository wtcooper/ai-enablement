# Client and engagement acceptance and risk (professional services)

Last reviewed 2026-10-19. Use cases live in `../use-cases/acceptance-risk.yaml` (14 entries). Ids are shortened here:
`#03` means `professional-services-acceptance-risk-03`. Source keys in brackets are listed in §10 and given in full in
the YAML. **Read this first:** public evidence here is thin and mostly vendor-published, chiefly Intapp. No named
organisation reports an error, override or false-positive rate for AI in conflicts, KYC or acceptance, and no inspection
finding or independent benchmark exists. The measured gains (BDO Canada, Sandberg Phoenix, Loeb & Loeb) come from
replacing manual workflows, not from AI. There is no grade A entry; 6 are B, 6 C and 2 D.

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

How a firm decides whether to take on a client or matter: conflicts checks, client due diligence and KYC (know your
client: identity, ownership, sanctions and AML, meaning anti-money-laundering, checks), engagement risk assessment and
approval, engagement letters and client terms, ethical walls, and monitoring after acceptance. It also covers the new
thread of client AI terms: what clients allow the firm to do with AI on their work. Examples come mostly from law firms,
some accounting firms and in-house legal teams; no consulting-firm example was found. Audit-client independence sits in
the assurance archetype (§3, "Held elsewhere").

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Opportunity pre-screen | Check a prospect against conflicts before a pitch advances | review-assurance | Pursuit effort wasted on work that later fails conflicts (`#01`) |
| Intake request | Fee earner enters client, matter and parties; reviewers get the request | transaction-processing, document-production | Re-keying details; reviewers read long requests for their issue (`#02`) |
| Conflicts search and clearance | Build the search, read hits, resolve, record, decide waivers and screens | review-assurance, research-synthesis, expert-judgment | Deciding history sits in people's heads, not the database [TRI-PREMORTEM-2026] (`#03`, `#04`) |
| Lateral-hire conflicts | Check a candidate's client relationships before hiring | review-assurance | Confidential candidate data; volume during lateral growth (`#05`) |
| Client due diligence, KYC and AML | Identity, beneficial ownership, sanctions and politically exposed persons, adverse media; risk rating and routing | research-synthesis, review-assurance | Hours spent on low-risk clients; 39% of UK client and matter risk assessments found ineffective or incomplete [VINCI-SRA-2025] (`#06`, `#07`) |
| Engagement risk assessment and approval | Risk score, ethics checks, partner and risk-team sign-off | expert-judgment, review-assurance | Email chains, days to weeks, no status visibility, people bypass it [INTAPP-LOEB-2021; INTAPP-BDOCA-2025] (`#08`) |
| Engagement letter | Draft scope and terms, including AI disclosure and consent | document-production | Letters delayed or missed; boilerplate consent is not enough [ABA-OP512-2024] (`#09`) |
| Client terms and guidelines | Capture outside counsel guidelines (OCGs: a client's rules for the firms it hires) and apply them | document-production, review-assurance | Terms scattered in documents; slow to answer across clients (`#10`) |
| Client AI terms | Record which AI tools, consents and disclosures each client allows | client-interaction, review-assurance | Rules differ by client and contradict each other [TRI-LEGALWEEK-2026] (`#11`) |
| Ethical walls | Keep screened people (and now AI tools) away from a matter | review-assurance, software-systems | AI assistants can reach walled matters [ABA-OP512-2024] (`#12`) |
| Continuance and monitoring | Re-screen clients after ownership, sanctions or litigation changes | data-reporting, review-assurance | 92% screen new clients for sanctions, 79% re-check existing ones [VINCI-SRA-2025] (`#13`) |
| In-house request intake (in-house) | Business requests reach legal, are routed, answered and logged | transaction-processing, client-interaction | Incomplete requests; business proceeds without legal (`#14`) |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns an
outcome), reinvent (the service or operating model changes). **Reinvent has no evidence: no entry changes the service
or business model.** The only model-level statement is Intapp's conditional line that clearing 10 times the matters
would be a new business model [INTAPP-CELESTEGA-2026]. **Delegate appears once, as an announcement (`#05`). Assist has no
separate entry**; the nearest is staff asking an assistant about client terms inside `#10`.

**Pre-screen and intake**
- Improve: `#01` conflicts screen of opportunities before formal review, and a Celeste plug-in that sources
  opportunities on already-cleared work (Intapp, announced, C). `#02` intake requests prepopulated from emails and files,
  with role-based risk summaries for reviewers (Intapp, announced, C).

**Conflicts clearance**
- Improve: `#03` Celeste builds the search, triages high-risk hits for expert review and drafts clearance summaries;
  BakerHostetler (law) is the named early adopter, but its CIO's quote is forward-looking (piloting, B). `#04` a
  14-lawyer unnamed US firm's custom agent: 2-3 hours to 8 minutes per check, by the builder's own account; the first
  version flagged so much that it cost more time than manual checks (C).
- Delegate: `#05` Celeste's lateral-hire playbook covers research, conflicts pre-screen, clearance preparation and
  onboarding (law, announced, C).

**Due diligence, KYC and AML**
- Improve (process): `#06` Pinsent Masons (UK law) and Xapien co-developed an LLM-generated, sourced AML due-diligence
  report; low-risk clients pass with minimal oversight, medium go to the AML team, high need further verification or partner consultation.
  Results are stated as expectations (piloting, B). `#07` idea: an agent scores adverse media with a written
  justification (research prototype for banks, D).

**Acceptance workflow, letters and terms**
- Automate (process): `#08` risk-scored routing, connected checks, audit trail and generated documents. BDO Canada
  (accounting) processes more than 5,000 acceptances a month, a 38% improvement with the same resources; Sandberg Phoenix (law)
  opens three times as many matters; Loeb & Loeb (law) went from weeks to hours. These are workflow platforms, not AI (B).
- Automate (step): `#09` engagement letters generated from approved intake data and routed for signature (announced, C).
- Improve: `#10` Fredrikson & Byron (law) has AI take a first pass at categorising each obligation in a client's
  guidelines; the risk counsel confirms it; staff ask an assistant about client terms (in production, B).
- Improve (process), idea: `#11` a structured register of each client's AI restrictions, checked against the tool list
  before work starts. No firm describes one (D).

**Walls and monitoring**
- Automate (process): `#12` wall policies extended to AI tools; Nelson Mullins (law) points Microsoft Copilot only at
  matters a user may access (B). Intapp and Harvey announced a plan to enforce walls inside Harvey.
- Automate (process): `#13` alerts when a client's ownership, sanctions status or litigation exposure shifts (announced, C).

**In-house front door (in-house)**
- Improve (process): `#14` Legora and Harvey Intake read requests, ask for missing details, route them and draft from
  playbooks; a lawyer reviews by default and pre-approved routine items can skip review (B, design partners only).

**Held elsewhere (do not duplicate):** accounting conflicts and independence clearance
(assurance-acceptance-independence-01); accounting acceptance with independence and reputational signals (Kingland,
Intapp; -02); Grant Thornton UK's Fenergo platform joining KYC, due diligence and acceptance (-03); AML onboarding at
accounting firms (-04); entity family trees (-05); independence monitoring (-06); CPA engagement-letter automation (-08);
AI terms in audit engagement letters (-11); AI tool vendors as an independence question (-13); screening clients against
a firm's outside investors (-16, -17). Recording AI use per matter and applying client AI terms
(professional-services-work-production-25); gated AI rollout and approved tools (-22); Dentsu's in-house non-compete
checks on new customers (-18). AI inventory including shadow AI (security-ai-security-21); a tax firm's approved-tool
list and vendor due diligence (tax-compliance-individual-business-19).

## 4. Interview probes

Ask a general counsel, risk or conflicts lead, MLRO (money laundering reporting officer), COO or in-house legal-operations
lead. Expect "we don't measure that" on AI effects; note who would know.

1. **"Think of the last conflict that was missed or nearly missed. Where did the deciding knowledge live: the database,
   documents, or one person's head? Could a new analyst find it?"** Reveals whether an agent (`#03`) would fail the way
   the TRI premortem describes, and whether playbooks exist.
2. **"Who signs the acceptance decision, and what would they need to see in a generated summary or risk report to trust
   it? Do you track how often reviewers change a hit triage, risk rating or summary?"** Reveals the human checkpoint
   and whether an override rate could be measured (`#02`, `#03`, `#06`).
3. **"How long does a request take from submission to cleared matter, and how many requests does each analyst handle a
   month?"** Reveals the baseline for workflow gains like BDO Canada's and Loeb & Loeb's (`#08`).
4. **"Where does acceptance run today: email, forms or a platform? Does anyone work around it?"** Reveals whether the
   workflow base exists; the AI features in `#02`, `#03` and `#13` sit on top of it.
5. **"For KYC and conflicts, what share of hits or alerts are false positives, who tunes thresholds, and what does a miss
   cost compared with a false flag?"** Reveals readiness for screening agents and the alert-fatigue risk (`#04`, `#06`, `#13`).
6. **"How often do you re-screen existing clients for sanctions, ownership or litigation changes?"** Reveals the
   continuance gap the SRA data points to (`#13`).
7. **"How do client AI restrictions in guidelines, engagement letters or consents reach the matter team and the tools
   they use? Who confirms a tool is on the client's list?"** Reveals whether `#10` and `#11` are needed and who owns them.
8. **"Which AI tools are people actually using, compared with the list you approved?"** Reveals shadow use; 34% of
   professionals use unsanctioned AI [TR-FOP-2026]. Without this, `#11` cannot work.
9. **"How do your ethical walls apply to AI assistants and agents? Can an assistant see across matters?"** Reveals the
   exposure in `#12`.
10. **"Do your engagement letters say how you use AI and get consent? Who approves a letter before it goes out?"**
    Reveals readiness for `#09` and the consent point in ABA Opinion 512.
11. **"Do prospects reach you through a website form or chatbot? Do those contacts enter the conflicts system?"**
    Reveals the Oregon point on chatbot intake (`#02`, §6).
12. **(In-house) "How do business requests reach legal, and which could be answered without a lawyer?"** Reveals fit for
    a front door (`#14`) and who owns each answer.

## 5. Metrics and benchmarks

**Workflow gains (vendor-published case studies; not AI)**
- BDO Canada (accounting): more than 5,000 acceptances a month on average since January 2025, a 38% improvement on what
  the same resources could process before [INTAPP-BDOCA-2025].
- Sandberg Phoenix (law): three times as many matters opened, "significantly" fewer errors (no error figure)
  [INTAPP-SANDBERG-2025].
- Loeb & Loeb (law, 2021): new business intake from weeks to hours; conflicts team from about 200 to sometimes 800
  requests a month, partly from firm growth [INTAPP-LOEB-2021].

**AI claims (no measured result)**
- Celeste surfaces matters and partner experience "in minutes rather than hours" (vendor) [INTAPP-CELESTEGA-2026].
- Pinsent Masons expects low-risk clients cleared in hours rather than days and a report in about 15 minutes
  (expectation) [XAPIEN-PINSENT-2026]. An ebook summary says fee earners lost 2.4 million hours to opening new matters
  (problem statement) [XAPIEN-PINSENT-EBOOK-2025].
- One unnamed small firm: 2-3 hours to 8 minutes per conflicts check (builder's own account) [ADAI-CONFLICT-2026].

**Regulator and survey context**
- SRA 2025 AML report, via a VinciWorks summary: 935 supervisory engagements; 270 firms (32%) non-compliant; 39% of
  client and matter risk assessments ineffective or incomplete; 92% screen new clients against sanctions lists, 79%
  re-check existing clients [VINCI-SRA-2025]. Secondary; the SRA page was blocked.
- Law firms whose generative AI policy says "must obtain client approval": 8% (under 50 lawyers), 20%, 24%, 38%
  (350-699) and 34% (over 700) [ILTA-TECHSURVEY-2026].
- 657 in-house professionals: 61% plan to push for change in how outside counsel deliver and price; 59% see no GenAI
  savings from law firms yet [ACCEVERLAW-2025]. Client pressure behind AI terms, not an acceptance metric.
- Shadow AI: 34% of professionals use unsanctioned AI [TR-FOP-2026]; 54% of surveyed consultants use tools without
  approval [LEXISNEXIS-FOW-2026].
- Chaffetz Lindsey (law): more than 35% of matters carry ethical screens [IMANAGE-CHAFFETZ-2026].
- Vendor claims: Intapp Conflicts and Intake used by more than 10 of the top 25 accounting firms; Walls by more than 70
  Am Law 100 firms [INTAPP-CONFLICTSAI-2026; INTAPP-WALLS-2026].

**What to measure (recommended; nobody publishes these yet):** how often reviewers override AI hit triage or risk
ratings; false-positive and missed-conflict rates; request-to-clearance time; share of existing clients re-screened;
share of matters with client AI terms captured at opening; alerts per analyst.

## 6. Guardrails

**Supervision of agents (US law).** California (2026): lawyers must not let agentic systems make substantive legal
determinations without meaningful lawyer supervision; it names autonomously facilitating client intake as an agentic
example; agent access to client files must be scoped and monitored, since agents with persistent access can disclose
information across matters; AI used to screen clients or candidates may carry bias risk [CALBAR-GENAI-2026].
Oregon (Feb 2026): a prospect's disqualifying information gathered by a chatbot should promptly enter the conflict
system, and autonomous actions such as sending an engagement letter should need lawyer approval [OSB-FO-2026-208].

**Consent, disclosure and client instructions.** ABA Opinion 512 (2024-07-29): informed consent is needed before putting
client information into many self-learning tools; boilerplate engagement-letter wording is not enough; disclose AI use
when engagement terms or OCGs require it [ABA-OP512-2024]. California: follow client guidelines that restrict AI
[CALBAR-GENAI-2026]. ACCA (UK tax, Sept 2026): disclose AI use in the engagement letter and, where AI is fundamental,
tell the client first; a clause will not make an unsafe process safe [ACCA-ENGLETTERS-2026].

**Ethical walls.** Self-learning tools can disclose information to people barred by a wall [ABA-OP512-2024]. Systems that
keep inputs inside the firm must still stop information reaching colleagues behind a wall; shared knowledge bases that
mix clients can breach walls [NYCBAR-OP2024-5-2024].

**Accounting ethics.** IESBA (June 2026): the Code applies regardless of technology; accountants must assess the fitness
for purpose and bias of technology outputs; automation bias is named as a threat to objectivity; client data used for AI
training needs authorisation [IESBA-SNAPSHOT-2026]. PCAOB QC 1000 is scheduled to take effect on 15 Dec 2026
[PCAOB-QC1000-2025]; its acceptance provisions were not read. Detail: assurance archetype.

**UK AML and conduct.** Practitioners expect tougher evidence standards and keep acceptance decisions human-led; AI is
used for triage [VINCI-AML-2026]. The SRA issued an AI warning notice on 17 Aug 2026, covering confidential data in
unsafe tools (seen via a law-firm article) [DWF-SRA-2026].

**Insurance.** Insurers are expected to ask more about supervision of AI-enabled work, and cover is uncertain where a
service was largely AI-produced and weakly supervised [DACB-PI-2026; IAMAG-LAWPL-2026]. Detail: quality-review.

**Steps that need human judgment:** the acceptance or exit decision; waivers and screens; medium- and high-risk KYC
cases; which client AI restrictions the firm accepts and how it will comply; sending an engagement letter; triage of
monitoring alerts; any conflict that turns on relationship history.

## 7. Roles and how they evolve

- **Risk counsel and conflicts staff** move from doing the work to confirming AI output: Fredrikson & Byron's risk
  counsel confirms AI categorisations of client guidelines, and staff ask the assistant instead of her
  [INTAPP-FREDRIKSON-2024].
- **Intake and data-entry work** shrinks with workflow platforms: Loeb & Loeb says its paper "human workflow engine",
  which needed four people on data entry, became obsolete [INTAPP-LOEB-2021]. Sandberg Phoenix built a dedicated intake
  department as it grew [INTAPP-SANDBERG-2025].
- **AML analysts** focus on higher-risk cases under risk-tiered routing (vendor statement) [XAPIEN-PINSENT-2026].
- **Conflicts teams under lateral growth:** BakerHostetler's CIO believes Celeste can help the firm evaluate conflicts
  faster after many lateral-driven onboardings [INTAPP-CELESTEGA-2026].
- **Hiring signals show no AI duty yet:** one conflicts-analyst posting asks for Intapp, iManage and Aderant experience
  [VIRTUALVOCATIONS-2026]. A Baker McKenzie "Client AI Risk Lead" posting was seen in search only
  [BAKERMCKENZIE-CLIENTAIRISK-2026].
- **Firm general counsel** take on compliance with client AI guidelines (a roundtable topic) [JENNER-SANDPIPER-2026].
- **In-house lawyers** own each answer an agent gives the business; routine work stops landing on senior people
  (vendor statement) [LEGORA-INTAKE-2026].
- **Risk managers and insurers**: Swiss Re Corporate Solutions and Wickard announced AI risk education for law
  firms covering supervision, confidentiality and internal AI approval processes [SWISSRE-WICKARD-2026].

## 8. Frontier

- 2026-02: Oregon opinion on intake chatbots: conflicts entry, lawyer approval of agent actions [OSB-FO-2026-208].
- 2026-02-18: TRI premortem: an agent clears a conflict a veteran would have flagged (hypothetical) [TRI-PREMORTEM-2026].
- 2026-02-23: Intapp and Harvey announce plans to enforce ethical walls inside Harvey [INTAPP-HARVEY-2026].
- 2026-03-02: Intapp's COO says speed needs checks and safeguards [INTAPP-GLP-2026]. 2026-03-03: Grant Thornton UK
  selects Fenergo to unify KYC, due diligence and acceptance [FENERGO-GT-2026].
- 2026-03-13: Legalweek: some clients bar AI without permission or demand unbiased-model warranties [TRI-LEGALWEEK-2026].
- 2026-05: California guidance covers agentic AI, intake and cross-matter confidentiality [CALBAR-GENAI-2026].
- 2026-06: IESBA is not changing the Code further; plans guidance notes, not yet found published [IESBA-SNAPSHOT-2026].
- 2026-07-15: Celeste generally available with conflicts, intake and lateral-hiring playbooks [INTAPP-CELESTEGA-2026].
- 2026-07-23: Starbucks reported to strictly restrict vendor and outside-counsel AI use [EDT-CASEPOINT-2026].
- 2026-08-04: Intapp reports it is expanding its Moody's partnership for entity screening and ownership data [INTAPP-Q4-2026].
- 2026-08-17: SRA AI warning notice (secondary) [DWF-SRA-2026]. 2026-09-01: an article argues independence rules do
  not cover AI-tool vendors [ACCWEEKLY-INDEP-2026].
- 2026-09-17: Celeste plug-in for ChatGPT Enterprise, including checks against client guidelines [INTAPP-OPENAI-2026].
- 2026-10-08: Sandpiper roundtable on AI in OCGs and engagement letters [JENNER-SANDPIPER-2026]; Coheso launches Memory
  for its in-house front door [AL-COHESO-2026].
- 2026-10: Legora and Harvey launch in-house Intake products [LEGORA-INTAKE-2026; HARVEY-INTAKE-2026].
- Scheduled, not evidence: PCAOB QC 1000 effective 15 Dec 2026 [PCAOB-QC1000-2025].

## 9. Common objections

- **"Conflicts depend on what senior people remember; an agent can't do that."** That is the main worry, shown in a
  hypothetical premortem [TRI-PREMORTEM-2026]. Answer: write the playbooks first, start the agent on triage and
  summaries, and keep expert review of hits and partner decisions on waivers (`#03`).
- **"AI screening will bury us in false positives."** It can: one small firm's first version cost more time than manual
  checks until thresholds were tuned over three weeks [ADAI-CONFLICT-2026]; untuned tools cause alert fatigue
  [VINCI-AML-2026]. Calibrate, govern and measure the false-positive rate.
- **"Electronic checks miss context."** UK practitioners agree they are weaker on context and complex structures; they
  use AI for triage and keep decisions human-led [VINCI-AML-2026]. Risk-tiered routing sends high-risk cases to people (`#06`).
- **"The vendor numbers prove AI works here."** The measured gains are from workflow platforms, not AI
  [INTAPP-BDOCA-2025; INTAPP-SANDBERG-2025; INTAPP-LOEB-2021]. No AI accuracy figure is published; ask for a parallel run.
- **"Our engagement letter already has an AI clause."** A clause does not make an unsafe process safe
  [ACCA-ENGLETTERS-2026], and boilerplate is not informed consent for self-learning tools [ABA-OP512-2024].
- **"Clients contradict themselves on AI."** They do: some demand AI savings, others bar AI without permission
  [TRI-LEGALWEEK-2026]. Follow the restrictive guideline [CALBAR-GENAI-2026] and capture terms per client (`#10`, `#11`).
- **"Disclosing every AI use is impractical."** An EY tax innovation leader, in a 2023 piece on how much firms tell
  clients, spoke of "a ghost around every corner" [BLOOMBERGLAW-DISCLOSURE-2023]. But disclosure is required when terms
  or OCGs require it [ABA-OP512-2024], and up to 38% of law firms (by size band) list client approval in their generative
  AI policy [ILTA-TECHSURVEY-2026].
- **"Our walls live in the document system, so AI is covered."** Not automatically: bar opinions warn AI tools can
  bypass walls [ABA-OP512-2024; NYCBAR-OP2024-5-2024]; wall policy must reach each AI tool (`#12`).
- **"AI tools aren't an independence issue."** For accountants this is open; one article argues no standard has settled
  it [ACCWEEKLY-INDEP-2026]. See assurance-acceptance-independence-13.

## 10. Sources

Full details (title, URL, date, locator, access) are in the YAML. Keys not in the YAML are marked * with short details.

- **Regulators, standard-setters, professional bodies:** CALBAR-GENAI-2026, ABA-OP512-2024, NYCBAR-OP2024-5-2024,
  OSB-FO-2026-208, IESBA-SNAPSHOT-2026, ACCA-ENGLETTERS-2026, ILTA-TECHSURVEY-2026, PCAOB-QC1000-2025* (PCAOB, QC 1000
  effective-date postponement release, 2025-08).
- **Surveys:** TR-FOP-2026* (Thomson Reuters, Future of Professionals Report 2026), ACCEVERLAW-2025* (ACC and Everlaw,
  GenAI survey press release, 2025-10-14), LEXISNEXIS-FOW-2026* (LexisNexis, blog on Future of Work 2026 consulting
  report, 2026-04-16).
- **Firm and vendor case studies:** INTAPP-BDOCA-2025, INTAPP-SANDBERG-2025, INTAPP-LOEB-2021, INTAPP-BDOAU-2024,
  INTAPP-FREDRIKSON-2024, INTAPP-PRACTUS-2026, XAPIEN-PINSENT-2026, XAPIEN-PINSENT-EBOOK-2025, XAPIEN-IDD-2024,
  IMANAGE-CHAFFETZ-2026, FENERGO-GT-2026* (Fenergo, Grant Thornton UK selection release, 2026-03-03).
- **Vendor product pages and releases:** INTAPP-CELESTEGA-2026, INTAPP-CONFLICTSAI-2026, INTAPP-ONBOARDAI-2026,
  INTAPP-INTAKE-2026, INTAPP-TERMS-2026, INTAPP-WALLS-2026, INTAPP-HARVEY-2026, INTAPP-OPENAI-2026, LEGORA-INTAKE-2026,
  HARVEY-INTAKE-2026, LAYER3-OCG-2026, LITERA-GCRFP-2026, ADAI-CONFLICT-2026, INTAPP-Q4-2026* (Intapp, FY2026 results
  release, 2026-08-04), INTAPP-GLP-2026* (Global Legal Post excerpt on Intapp's site, 2026-03-02).
- **Press, conference and community:** TRI-PREMORTEM-2026, TRI-LEGALWEEK-2026, LAWSITES-CELESTE-2026,
  JENNER-SANDPIPER-2026, EDT-CASEPOINT-2026, AL-COHESO-2026, VINCI-AML-2026, VINCI-SRA-2025,
  ACCWEEKLY-INDEP-2026* (Accounting Weekly, "AI Audit Tools and the Independence Gap Nobody Fixed", 2026-09-01),
  DWF-SRA-2026* (DWF, guide to AI for trainees citing the SRA warning notice, 2026-08-21), DACB-PI-2026* (DAC
  Beachcroft, PI insurance and AI hallucinations, 2026-09-28), IAMAG-LAWPL-2026* (Independent Agent magazine, AI and law
  firm professional liability, 2026-03-09), SWISSRE-WICKARD-2026* (National Law Review release, 2026-08-27),
  BLOOMBERGLAW-DISCLOSURE-2023* (Bloomberg Law, firms on telling clients about AI use, 2023-11-29). Academic:
  ORBILU-ADVERSE-2025.
- **Job postings:** VIRTUALVOCATIONS-2026, BAKERMCKENZIE-CLIENTAIRISK-2026* (Baker McKenzie, Client AI Risk Lead,
  2026, search-only).
