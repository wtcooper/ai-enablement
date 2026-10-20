# Knowledge management (professional services)

Sources checked and verified 2026-10-19. Use cases live in `../use-cases/knowledge-management.yaml` (23 entries:
A 0, B 12, C 10, D 1). Ids are shortened here: `#08` means `professional-services-knowledge-management-08`; other modules' and
archetypes' ids are in full. Source keys in brackets are in the YAML or in §10. No firm, consultancy or in-house team
publishes a measured result (search success, error or override rate, permission-leakage test) for its own knowledge
base, so nothing here is grade A. Named examples are mostly law firms and in-house legal teams, on vendor-hosted
pages; consulting rests on McKinsey's second-hand figures, accounting on one podcast. Say so when you quote a figure.

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

How a firm or in-house team captures, curates, finds and reuses what it already knows: precedents (past documents
reused as starting points), know-how, methods, past engagements and who has expertise. It includes the governance
that decides what an AI tool may see. Generating drafts and reviewing them is work-production; this module is reuse
of what exists. Audit methodology, tax research and security runbooks live in their own archetypes.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Capture | Close-out notes, retrospectives, call notes, decisions, departing experts' know-how | document-production, research-synthesis | Expertise stays locked in decks and heads; know-how leaves when people retire [KANTATA-ENGINE-2025; NETDOCUMENTS-CONTEXTGRAPH-2026] |
| Curate and validate | Decide what is final, exemplary or superseded; strip client detail; owners review on a cycle | review-assurance | Drafts, executed deals and counterparty markups mixed; nobody recorded why a document was "final" [DRAFTWISE-PRECEDENT-2025] |
| Organise and secure | Taxonomy (agreed categories), metadata, OCR, permissions, ethical walls (screens that block named staff from a matter) | data-reporting, software-systems | Two-decade taxonomies; files kept in separate team repositories and SharePoint libraries [IMANAGE-WOMBLE-2026; IMANAGE-DCB-2026] |
| Find and retrieve | Search, ask questions of documents, locate an expert or comparable matter | research-synthesis | Enterprise search and expertise management "dramatically underdeveloped" [ILTA-TECHSURVEY-2026] |
| Reuse and apply | Benchmark terms against deal history; ground drafts and client tools in approved precedent | research-synthesis, document-production | Risk that lawyers take the easiest template, not the best [IMANAGE-ALLENS-2025] |
| Transfer and onboard | Matter or engagement briefs for joiners; pre-call research | research-synthesis, coordination-scheduling | A new lawyer spends days reconstructing a matter's context [NETDOCUMENTS-CONTEXTGRAPH-2026]; customer success managers spent four to five hours a day on pre-call research [KANTATA-BASWARE-2026] |
| Govern AI access and use | Approved tools, connectors, policy, training, audit logs | review-assurance, coordination-scheduling | 34% of professionals use unsanctioned AI [TR-FOP-REPORT-2026]; no public leakage tests |
| Maintain and measure | De-duplicate, retire, analyse searches and reuse, re-test tools | data-reporting | KM impact hard to measure; firms "still gathering the data" [APQC-KMEXEC-2026; TRI-LEGALWEEK-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (`change_scope: model`). **Coverage:** assist 6, augment 14, automate
2, delegate 1; step 11, process 11, model 1. Automate has a private preview (`#06`) and a beta client portal (`#22`).
Delegate has one announced product pair (`#10`). Reinvent has one beta (`#22`). No firm reports a knowledge step that
has stopped existing. `#04` and `#15` are C: their named deployments do not show the AI step (see the YAML notes).

**Find and retrieve**
- Improve: `#01` AI search over a curated precedent library, under existing permissions (Allens and Womble Bond
  Dickinson UK, law firms). Access counts only; no search-success data.
- Improve: `#02` ask questions of the firm's own documents to find clauses (Chaffetz Lindsey and Bicalho Navarro, law
  firms; Digital Commerce Bank, in-house). Drafting from what is found is professional-services-work-production-05.
- Improve: `#03` firm-wide assistant over a consultancy's IP that also points to experts (McKinsey Lilli; Deloitte
  PairD; Infosys). Usage and "30% time saved" are self-reported, second hand.
- Improve: `#04` "who has done this before?" from matter, people and CV records (McKinsey, via a secondary report;
  Arup's CV platform, engineering, no AI claimed; Intapp, Litera and NetDocuments products). Grade C. Staffing use is
  staffing-resourcing; bid assembly is pursuit-proposals.
- Improve: `#09` governed connections (MCP, an open standard for linking AI tools to systems) so approved tools search
  and save back under each user's permissions, logged (iManage, Legora, Harvey, NetDocuments; announced).

**Curate and organise**
- Improve, process scope: `#12` curated, owned collections as the grounding set, with senior review before entry and
  client detail stripped (Womble Bond Dickinson; McKinsey data stewards). The core KM change.
- Improve, process scope: `#05` reclassification and summarisation of 400,000+ documents into a knowledge bank
  (Clifford Chance, law firm; launched, use not yet shown). `#08` context graph mapping matters, documents and people (Harvey, NetDocuments, iManage;
  vendor benchmarks only).
- Improve: `#07` duplicate finding and reorganisation applied only after a person confirms (Digital Commerce Bank).
- Automate: `#06` classification, extraction and summaries at the moment of filing (NetDocuments private preview).

**Capture**
- Improve, process scope: `#15` close-out capture and AI-drafted retrospectives (Alvarez & Marsal, Simon-Kucher,
  consulting, and AECOM, engineering, describe automated capture; the AI drafting step is only in Certinia's catalogue;
  grade C). `#14` in-house decisions turned into positions an attorney
  approves (Coheso; no customer named).
- Improve, process scope: `#19` reviewers' corrections and senior judgment captured for juniors, with unaided checks
  (Ascend's CEO on Ascend's own firms, accounting; NBER patent trial, adjacent). `#20` AI "twins" of individual professionals (Twin1; announced).
- Improve: `#16` call and meeting transcripts as capture, within consent rules (NYC Bar 2026-2).
- Idea: `#21` structured interviews with retiring experts, AI-drafted stories approved by the expert.

**Reuse, transfer and onboard**
- Improve: `#11` precedent database built from the firm's deal history (Ropes & Gray, law firm). Bulk extraction is
  professional-services-work-production-03.
- Improve: `#17` briefs for joiners and before client calls (Chaffetz Lindsey; Basware, a software company's services
  team, says managers once spent four to five hours a day on pre-call research).
- Improve: `#13` in-house knowledge base of standards and prior decisions, run by legal operations (BMW Group, Rio
  Tinto, GSK; in-house). Related professional-services-work-production-19.

**Govern and measure**
- Improve, process scope: `#18` KM teams curate the firm's AI know-how and gate rollout (Troutman Pepper Locke, Lewis
  Silkin, Ropes & Gray, Gowling WLG, Latham & Watkins). Gating as a work-production control is
  professional-services-work-production-22; firm-built playbooks are professional-services-work-production-17.
- Improve, process scope: `#23` search analytics, reuse measures and re-tests. Tool testing is
  professional-services-work-production-23; logging overrides is professional-services-work-production-24.
- Delegate: `#10` agents with scoped, logged access file work and update metadata between review gates (iManage MCP,
  Harvey orchestration; announced). Matter templates are professional-services-work-production-15.

**Reinvent**
- `#22` Debevoise sells STAAR, a client-facing portal built from its AI-risk work, at $150,000 a year in beta with about
  10 clients; partners act as content gatekeepers (law firm). Priced-service side: professional-services-scoping-pricing-23.

**Other archetypes:** tax-research-advisory-05 (assistant over a tax team's own memos), tax-research-advisory-07,
tax-transfer-pricing-14 (connected knowledge model), assurance-quality-management-12 (guidance assistant grounded in
audit manuals), assurance-quality-management-02 (curated prompt library), security-operations-02 (how similar alerts
were closed before), security-governance-risk-01 (questionnaires answered from an approved knowledge base).

## 4. Interview probes

1. **"Who owns each part of your precedent and know-how library, and when was it last reviewed or retired?"** Reveals
   readiness for `#01` and `#12`; Allens relied on its existing curation and taxonomy, and Womble keeps curation with
   assigned owners.
2. **"When someone asks 'have we done this before?', how is it answered today, and how current is the answer?"**
   Reveals whether expertise lives in people (`#04`) and how stale directories are.
3. **"Whose permissions does your AI search run under, and how did you test that someone behind an ethical wall
   cannot see that matter in an answer?"** Reveals the main exposure; no public leakage test exists (`#01`, `#09`).
4. **"Who decides what counts as 'final' or 'good', and is that recorded anywhere a tool could use?"** Reveals
   whether `#12` is a real gate; DiDomenico says this is not a technology problem.
5. **"Which AI tools can reach your document system, and who approves each connection and what it may write back?"**
   Reveals connector sprawl and readiness for `#09` and `#10`.
6. **"What leaves with people today (retirements, laterals, engagement end), and would you allow an AI model of a
   person?"** Reveals appetite for `#19`-`#21` and the consent and ownership questions.
7. **"What happens at engagement close: who writes lessons learned, where are they filed, and does anyone find them?"**
   Reveals whether `#15` would feed a used base or a graveyard.
8. **"When a wrong answer or flawed precedent is filed as knowledge, who corrects it and how would you find where it
   was reused?"** Reveals the verification loop (`#12`); errors can repeat across matters.
9. **"What do you measure: failed searches, content that never surfaces, reuse rates, overrides, time to orient a
   joiner?"** Reveals whether `#23` has any baseline; no firm publishes one.
10. **"How do client confidentiality terms and AI restrictions reach the people reusing that client's material?"**
    Reveals the sanitisation step (`#12`, `#15`) and client-term gaps.
11. **"Where do people go when the sanctioned tool is not good enough?"** Reveals shadow AI (34% in TR-FOP-REPORT-2026) and
    whether `#18` is working.
12. **"Do clients ask for access to your know-how, and who would keep a client-facing tool current?"** Reveals `#22`;
    Debevoise's partner calls himself the gatekeeper and says it takes a lot of time.

## 5. Metrics and benchmarks

**Spend and staffing (law firms)**
- Law-firm technology spend rose nearly 11% and KM spend about 10% in 2025; from 2021 to 2025, technology rose 39.3%
  and KM 37.2% [TRI-SOTLM-2026].
- ILTA (508 firms): 94% engage with GenAI, up 14 points; many firms expect added headcount in KM among other functions
  [ILTA-TECHSURVEY-2026].
- AALL salary survey (257 organisations, 45% response): law libraries average 6.6 FTE staff, up from 4.6 in 2019;
  the survey does not attribute this to AI [LAWSITES-AALL-2025].

**Governance prevalence**
- ILTA by firm size: formal GenAI policy 57% (under 50 lawyers) to 98% (350-699); training before use 11% to 72%;
  client approval 8% to 38% [ILTA-TECHSURVEY-2026].
- Thomson Reuters (1,816 professionals; vendor): 34% use unsanctioned AI; 41% of AI users lack tools built on verified
  professional content; 94% say outputs must be grounded in authoritative content [TR-FOP-REPORT-2026].
- iManage (3,000+ decision makers, cross-industry; vendor): 85% at some stage of AI adoption; fully integrated AI 27%
  in the most mature tier versus 3% in the least; 36% policy violation; 25% public AI with little oversight
  [IMANAGE-BENCH-2026].
- APQC (164 participants, cross-industry; independent): 59% of KM programmes in the two earliest maturity stages; 40%
  say their culture does not incentivise sharing and reuse, the top-ranked threat to KM success [APQC-KM-2026].

**Usage at named organisations (not quality)**
- McKinsey Lilli: over 4 million prompts and about 150,000 a week (2024 interview) [BOERSEN-LILLI-2024]; over 75% of
  43,000 staff monthly and "30% of time saved", relayed by TheOutpost.ai from June 2025 reports (Entrepreneur,
  Bloomberg) with no method [THEOUTPOST-LILLI-2025]. Another relay gives 70% of 45,000 [OFFICECHAI-LILLI-2025].
- Allens 1,350 legal staff with access; Womble about 600 lawyers and 1,250 users connected to the platform
  [IMANAGE-ALLENS-2025; IMANAGE-WOMBLE-2026]. Rio Tinto legal 80% platform adoption in four months, not an AI measure
  [IMANAGE-RIOTINTO-2025].

**Vendor benchmarks**
- Harvey Graph: up to 30% higher rubric pass rate and up to about 50% lower task cost with a context graph; task count
  not given [HARVEY-GRAPH-2026]. NetDocuments: cost per correct answer $0.68 to $0.36 on 300 questions over public
  filings [NETDOCS-LCEB-2026].

**Adjacent independent evidence (tools or trials, not firm knowledge bases)**
- Document Q&A on one supplied document: best tools 94.8 and 89.6 against a lawyer baseline of 70.1 [VALS-VLAIRFEB-2025].
- Retrieval-based legal research tools hallucinated 17% to 33% of the time (2024) [STANFORD-MAGESH-2024].
- Patent drafting trial, 133 lawyers: quality +0.34 to +0.38 SD; unaided skill gain went to seniors; not independent: Google ran and funded it [NBER-AUTOR-2026].

**What to measure:** failed or zero-result searches; content that never surfaces; reuse rate of curated assets;
share of answers whose citations check out; time for a joiner to get oriented; curation backlog; results of
permission-leakage tests with a walled user. Access counts and prompt volumes say nothing about quality.

## 6. Guardrails

- **Ethical walls and confidentiality.** Where an AI system uses client information, the firm must apply required
  screens; confidential information must not go to systems that share it with third parties without consent
  [NYCBAR-OP2024-5-2024]. ABA Formal Opinion 512 says self-learning tools risk disclosing one client's information
  even when used only by lawyers at the same firm (p. 6) [ABA-OP512-2024; EZEL-ABA512-2024].
- **Agentic access (California, approved 2026-05-14).** Agents with standing access to document systems, email and
  knowledge bases create acute confidentiality risk; scope and monitor access; no autonomous external transmission of
  client information without safeguards and human review; oversight rises with autonomy [CALBAR-GENAI-2026].
- **Verification.** Lawyers must check AI research against authoritative sources, and leaders must take practical
  measures; the court may ask what they did [EWHC-AYINDE-2025]. Charlotin's database lists 2,202 cases of hallucinated
  content in court filings as of 2026-10-19, including some where AI use was alleged rather than confirmed
  [CHARLOTIN-DB-2026]. NIST AI 600-1 names confabulation, data privacy and IP risks [NIST-AI600-2024].
- **Templates and testing.** Do not use client confidential or personal data to create templates or test a system;
  use fictional data [LAWSOC-GENAI-2026].
- **Recording calls.** NYC Bar Opinion 2026-2: consent of all parties; default is not to record non-client
  conversations without good reason [NYCBAR-OP2026-2-2026].
- **Privilege.** In Heppner (S.D.N.Y., 2026-02) self-directed chats with a public AI tool were not privileged; one
  court's ruling [GOODWIN-HEPPNER-2026].
- **Policy and supervision.** Managerial lawyers set AI policy and training [CALBAR-GENAI-2026]; proposed California
  rule changes were out for comment to 2026-05-04, adoption not confirmed [CALBAR-RULES-2026]; the BSB lists data
  governance among good practice [BSB-AIGUIDANCE-2026]; the Bar Council told barristers to be extremely vigilant about
  sharing confidential information with an LLM [BARCOUNCIL-GENAI-2024].
- **People data.** Expertise location uses staff records. The EU AI Act's high-risk rules for employment and
  worker-management uses apply from 2027-12-02 [EC-AIACT-2026]; whether an expertise finder is in scope depends on its
  use (inference); California flags bias in employment uses [CALBAR-GENAI-2026]; the UK ICO's AI guidance is under
  review [ICO-AIDP-2023]. AI-literacy duties apply under the EU AI Act since 2025-02-02 [EC-AIACT-2026].

**Steps that stay with a person:** deciding what enters a curated collection and what is retired; stripping client
detail; approving each connector and what it may write back; checking cited sources before reuse; approving a
captured position, retrospective or "twin"; deciding whether to record a call; confirming expertise claims before
pitching or staffing; deciding what clients may see.

## 7. Roles and how they evolve

- **Knowledge teams become curators and gatekeepers.** Allens' team curates, pins standard documents, trains and
  recruits champions [IMANAGE-ALLENS-2025]; McKinsey's 2023 announcement describes data stewards as central to Lilli's
  quality (the page could not be re-opened to re-check this) [MCKINSEY-LILLI-2023];
  Debevoise partners curate a client product [BLOOMBERGLAW-DEBEVOISE-2026]. A vendor forecasts professional support
  lawyers (lawyers who maintain know-how rather than bill clients) becoming quality guardians of AI metadata
  [KMWORLD-LEXSOFT-2025].
- **KM merges with AI leadership.** Troutman Pepper Locke's KM and AI partner [TROUTMAN-KM-2026]; Eversheds
  Sutherland merged research and knowledge services into an AI-centric US innovation department [AL-EVERSHEDS-2026];
  K&L Gates' AI and innovation partner role covering data and KM [AL-X4-2026]; Gilchrist Connell's chief AI and knowledge officer [LAWYERSWEEKLY-GILCHRIST-2026];
  Gowling WLG's director of AI, innovation and knowledge [HARVEY-GOWLING-2025].
- **Knowledge lawyers and non-lawyers lead adoption.** Lewis Silkin put knowledge lawyers front and centre of its
  rollout, with a Harvey Lead in each team [HARVEY-LEWISSILKIN-2025]; Chaffetz Lindsey's non-timekeeping staff became champions [IMANAGE-CHAFFETZ-2026];
  Digital Commerce Bank's librarians govern AI use [IMANAGE-DCB-2026].
- **Template and agent owners.** Harvey names innovation and knowledge teams as authors of matter templates
  [HARVEY-ORCH-2026]. Hogan Lovells Cadwalader lawyers built custom agents for knowledge management [HARVEY-HLC-2026].
- **Talent view.** DiDomenico argues for growing existing KM, library and research staff and recruiting practising
  lawyers [AL-DIDOMENICO-2026]. A TRI column suggests junior rotations such as "knowledge operations curator"
  [TRI-AILAWPROF-JUNIOR-2026]. Vault, citing Axios, quotes Stanford's David Freeman Engstrom: firms are racing to
  "extract the knowledge of their lawyers" into AI workflows [VAULT-PYRAMID-2026]. Juniors' unaided outcomes split in the NBER trial [NBER-AUTOR-2026]; detail is talent-learning.
- **In-house.** Many legal operations leaders say their function is becoming "its own practice area", and the
  Thomson Reuters Institute calls it the default first line of defence against AI pressure [TRI-LDOR-2026].

## 8. Frontier

- **2025-11-11** Oz Benamram (SKILLS): firms have until end-2027 to share knowledge with clients via AI [AL-LAWPUNX-2025].
- **2026-02-20** TRI premortem (two fictional scenarios): agentic pilots fail on undocumented exceptions and fragmented storage [TRI-PILOTFAIL-2026].
- **2026-03-11** Legalweek sessions "What KM Must Still Control" and "KM, DMS, and LLMs in Harmony" (titles only) [EDRM-LEGALWEEK-2026].
- **2026-04-14** Law Society: accountability frameworks do not yet fit autonomous systems [LAWSOC-AGENTIC-2026].
- **2026-05-14** NetDocuments context graph, private preview; California approves agentic guidance [NETDOCUMENTS-CONTEXTGRAPH-2026; CALBAR-GENAI-2026].
- **2026-05-20** Harvey and DeepJudge target the "context tax" [LAWSITES-HARVEYDJ-2026].
- **2026-07-20** Clifford Chance launches its Knowledge Bank [ARTIFICIALLAWYER-CLIFFORDCHANCE-2026].
- **2026-08-06** Debevoise STAAR beta at $150,000 a year [BLOOMBERGLAW-DEBEVOISE-2026]. **2026-08-13** DeepJudge Agent Handoff Protocol [LAWSITES-DEEPJUDGE-2026].
- **2026-08-20** Twin1 launches AI twins after a $20m raise [AL-TWIN1-2026].
- **2026-09-04** eDiscovery Today on ILTACON, held the week before: "context" the word of the conference; talk of a shift from seat to consumption pricing [EDISCOVERYTODAY-ILTACON-2026].
- **2026-09-17 / 09-30** iManage plug-in for ChatGPT Enterprise; Harvey cross-system agentic search [LAWSITES-IMANAGECHATGPT-2026; HARVEY-AGENTICSEARCH-2026].
- **2026-10-08** Coheso Memory for in-house teams [AL-COHESO-2026]. **2026-10-15** Harvey Legal Work Orchestration; Microsoft Copilot for Legal draws on approved precedent in SharePoint [HARVEY-ORCH-2026; LAWSITES-MSFT-2026].
- **2026-10-16** Legora announces plans to connect to the iManage MCP Server [LEGORA-IMANAGE-2026].
- **2026-10-19** Harvey Graph results; Harvey plans firm-defined legal ontologies [HARVEY-GRAPH-2026].
- **Scheduled:** KM&I for Legal, 2026-10-21/22 [KMI-LEGAL-2026]; Kantata Converge, 2026-11-17 [KANTATA-CONVERGE-2026]. Signals only.

## 9. Common objections

- **"Our content is a mess; AI will surface junk."** Firms say so too: AI will not necessarily tell good from bad
  content [IMANAGE-WOMBLE-2026]. Answer: curate first, with owners and a short taxonomy (`#12`); Womble cut a
  two-decade taxonomy to at most four nodes.
- **"It could leak across ethical walls or to vendors."** A real duty [NYCBAR-OP2024-5-2024; CALBAR-GENAI-2026], and
  vendor permission claims have no public test. Answer: keep data in the governed store and let tools reach in
  [IMANAGE-CHAFFETZ-2026]; test with a walled user (`#01`, `#09`).
- **"Lawyers won't share."** "Old problems, new tools" [AL-DIDOMENICO-2026]; culture is APQC's top-ranked threat
  [APQC-KM-2026]. Answer: champions and practice leads (`#18`), capture inside the workflow (`#15`).
- **"It hallucinates."** Research tools did, 17% to 33% [STANFORD-MAGESH-2024]. Answer: cited answers checked
  before reuse, and validation before anything is filed as knowledge (`#12`).
- **"We can't prove value."** True so far [TRI-LEGALWEEK-2026; APQC-KMEXEC-2026]. Answer: baseline search failures
  and joiner orientation time now (`#23`).
- **"Too many tools."** Lawyers will only open so many tabs [DRAFTWISE-ILTACON-2025]. Answer: governed connectors
  rather than copies (`#09`); watch lock-in and consumption pricing [EDISCOVERYTODAY-ILTACON-2026].
- **"Clients get nothing from our AI."** A GC said so [AL-CLIENT-2026]. Answer: Debevoise's client portal (`#22`).
- **"It costs too much."** In an iManage story, an unnamed in-house legal operations team says it declined a
  competitor's expensive AI module with limited out-of-the-box features [IMANAGE-LEGALOPS-2025].
- **"It's hype."** An ILTA respondent expects it to pass [ILTA-TECHSURVEY-2026]; TRI warns of bubble risk
  [TRI-SOTLM-2026]; Kantata's CEO warns of "fast, mediocre decisions" without firm context (vendor) [KANTATA-SUPERAGENT-2026].
- **"Juniors won't learn."** A real risk [NBER-AUTOR-2026]. Answer: unaided checks (`#19`); detail in talent-learning.

## 10. Sources

Full details for YAML keys are in the YAML. Keys cited here but not in the YAML:
- ABA-OP512-2024: American Bar Association, Formal Opinion 512, 2024-07-29, https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf (americanbar.org blocks downloads; read in full from the LawNext-hosted copy, https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf, p. 6)
- BARCOUNCIL-GENAI-2024: Bar Council, New guidance on generative AI for the Bar, 2024-01-30, https://www.barcouncil.org.uk/resource/new-guidance-on-generative-ai-for-the-bar.html
- CALBAR-RULES-2026: State Bar of California, Proposed amendments related to AI, 2026-03-13, https://www.calbar.ca.gov/public/public-meetings-comment/public-comment/public-comment-archives/2026-public-comment/proposed-amendments-rules-professional-conduct-related-artificial-intelligence
- CHARLOTIN-DB-2026: Damien Charlotin, AI Hallucination Cases Database (read 2026-10-19), https://www.damiencharlotin.com/hallucinations/
- EDISCOVERYTODAY-ILTACON-2026: eDiscovery Today, My Five ILTACON 2026 Takeaways, 2026-09-04, https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/
- EZEL-ABA512-2024: Ezel, ABA Formal Op. 512 summary, 2024-07-29, https://ezel.ai/ethics-opinions/aba/512-generative-ai-tools
- HARVEY-HLC-2026: Harvey, Hogan Lovells Cadwalader adopts Harvey, 2026-10-16, https://www.harvey.ai/blog/hogan-lovells-cadwalader-adopts-harvey
- ICO-AIDP-2023: UK ICO, Guidance on AI and data protection (under review), 2023-03-15, https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/
- KANTATA-CONVERGE-2026: Kantata, Kantata Converge announcement (event 2026-11-17), 2026-10-08, https://www.kantata.com/blog/article/kantata-converge-where-ai-meets-expertise
- KANTATA-SUPERAGENT-2026: Kantata, More agents won't fix unpredictable projects, 2026-06-16, https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead
- KMI-LEGAL-2026: LegalTech Connect, KM and Innovation for Legal conference (scheduled 2026-10-21/22), 2026-10, https://kmiforlegal.com
- LAWSITES-AALL-2025: LawSites, What Do Law Librarians Earn? New AALL Salary Survey, 2025-11-25, https://www.lawnext.com/2025/11/what-do-law-librarians-earn-new-aall-salary-survey-provides-details.html
- LAWSITES-MSFT-2026: LawSites, Microsoft launches Copilot for Legal, 2026-10-15, https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html
- NIST-AI600-2024: NIST, AI 600-1 Generative AI Profile, 2024-07, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- STANFORD-MAGESH-2024: Magesh et al., Hallucination-Free? (arXiv 2405.20362), 2024-05-30, https://arxiv.org/abs/2405.20362
- TRI-AILAWPROF-JUNIOR-2026: Thomson Reuters Institute, The AI Law Professor: rethinking how we train junior lawyers, 2026-02-02, https://www.thomsonreuters.com/en/institute/articles/ai-law-professor-train-junior-lawyers
- VAULT-PYRAMID-2026: Vault, The Compressed Pyramid, 2026-08-11, https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/the-compressed-pyramid-what-ai-means-for-the-associate-career-ladder
