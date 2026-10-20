# Journey stages: cross-industry research (stream B, shared backbone library)

Kind: journey stages. Items: curious, experimenting, adopting, scaling, ai-native. Run date: 2026-10-20.
Method: 42 sources opened and read (see section 7; two are search-only and are marked). Sources fetched with `curl`, `pdftotext` and the `r.jina.ai` text mirror into a private folder. Seven web searches were used, all on new directions.

Conventions used below:
- Refs follow `PUBLISHER-SHORT-YYYY`; locators are in brackets after the ref (page, section or exhibit). Keys reused from `onboarding.md` §11 keep their spelling.
- "Self-reported", "vendor-published" and "independent" follow the vocabulary. Government bodies are typed `regulator` in section 7 because the vocabulary has no public-body type.
- Where a statement is my own synthesis and not a source claim, it is labelled "advisor heuristic".
- Onboarding §5 already holds the stage cards and the five delegation gates. This file adds evidence, mechanisms and examples; it does not restate the cards.

---

## 1. Summary

- **Stage populations depend almost entirely on who was asked.** Vendor and consultancy surveys of senior leaders at large organizations say 88% use AI and about 38-44% are "scaling" [MCKINSEY-SOAI-2025 Exhibit 1; MCKINSEY-SOAI-2026 §Use of AI is deepening]. The US Census Bureau's nationally representative firm survey puts use at 17-20% of all firms, 37% of firms with 250+ employees, and 14% in retail (December 2025 to May 2026) [CENSUS-BTOS-2026 §BTOS data]. An advisor must always ask "what population?" before quoting a stage share.
- **The four published staged models line up on one structural break: pilots versus scaled, owned, measured use.** MIT CISR, BCG and McKinsey all find financial or value differences concentrate above that break and a small top tier (CISR stage 4: 7% in 2022, 18% in a 2025 sample of 152; BCG future-built: 5% in 2025, 7.5% in 2026; McKinsey high performers: about 6% in both 2025 and 2026) [MITCISR-2024; MITCISR-2025; BCG-GAP-2025; BCG-AIX-2026; MCKINSEY-SOAI-2026]. None follows the same organizations over time; the 2022 and 2025 CISR samples are different (N=721 vs N=152).
- **Individual gains run ahead of enterprise gains, in every stage.** In 2026, 80% of McKinsey respondents say AI improved their own productivity while the share reporting any EBIT contribution stayed at 37% [MCKINSEY-SOAI-2026 §Despite broader use]. Three UK government Copilot evaluations of one tool disagree on whether time saved became productivity: GDS reports 26 minutes a day (self-estimated), DWP estimates 19 minutes (against a comparison group), DBT "did not find evidence" it improved productivity [GDS-COPILOT-2025 §4; DWP-COPILOT-2026 §Time savings; DBT-COPILOT-2025 p.5].
- **"Pilot purgatory" is real but its measured size varies by 10x across surveys:** 5% of custom enterprise tools reached production (interview-based, preliminary) [MIT-NANDA-2025 §3.2]; 25% of Deloitte's respondents have moved 40%+ of experiments to production [DELOITTE-STATEAI-2026 p.8]; 54% of Wharton's US managers say more than half of last year's pilots reached production [WHARTON-2026 Exec Summary]. Definitions, populations and success criteria differ; none is audited.
- **The most consistent failure point is scaling autonomy faster than controls.** BCG reports 42% of companies expect to give agents genuine autonomy by 2030 and 5% have the full controls today; Deloitte reports 74% plan agentic deployment within two years and 21% have a mature governance model [BCG-AIX-2026; DELOITTE-STATEAI-2026 p.7]. Named cases show the cost of weak review: Klarna's CEO said AI service was cheaper but of "lower quality" and the firm resumed hiring humans (May 2025); Deloitte Australia agreed to refund part of a A$440,000 government report that contained fabricated references [ENTREPRENEUR-KLARNA-2025; CYBERDAILY-DELOITTE-2025].
- **A new tension for the delegation gates.** Wharton's 2026 survey finds transformation highest where AI only advises (25%) or acts with monitoring (31%) and lowest in the supervised middle (16% where every action is approved; 18% where a sample is checked) [WHARTON-2026 Exec Summary p.16]. It is correlational and self-reported. Read it as a reason to plan the path from approval-on-everything to monitored autonomy, not as a reason to skip the gates; IMDA and BCG both describe graduated, tiered autonomy [IMDA-MGF-2026 §2.1.2; BCG-AGENTS-2025 §Trust Protocol].
- **What separates movers is mostly organizational, not technical.** Across sources: redesigned workflows (McKinsey high performers: nearly three-quarters vs one-quarter of others, 2026), a named executive owner, one approved platform (Wharton: 50% strongly positive ROI vs 9% "still experimenting"), growth as well as efficiency metrics (35% vs 13%), and broad upskilling (BCG: more than 50% of staff vs 20% at laggards) [MCKINSEY-SOAI-2026 §High performers; WHARTON-2026 Exec Summary; BCG-GAP-2025 §What Value Generators Do Differently]. All are self-reported associations, not trials.
- **Quality evidence is thin.** No cross-industry source read publishes override, escalation or parallel-run rates for stage movers. The closest are one controlled field study (+14% issues resolved per hour, customer support), one randomised trial with a slowdown (19% slower, experienced open-source developers) and one department evaluation that saw hallucinations but gave no rate [NBER-BRYNJOLFSSON-2023; METR-2025; DBT-COPILOT-2025]. See sections 5 and 6.

---

## 2. Item profiles

### 2.0 Cross-stage reference tables

**Table A. How the published models line up (mapping is advisor heuristic; the models use four stages or fewer)**

| Advisor stage | MIT CISR (4 stages) [MITCISR-2024; MITCISR-2025] | BCG (4 tiers, 41 capabilities) [BCG-GAP-2025 App.; BCG-AIX-2026] | McKinsey phases [MCKINSEY-SOAI-2025 Ex.1] | Other |
|---|---|---|---|---|
| Curious | 1 Experiment and Prepare (education, acceptable-use policy, data access) | Stagnating (little or no action, no foundations) | Not using / experimenting | Wharton wave 1 "Exploration" (2023) [WHARTON-2025] |
| Experimenting | 2 Build Pilots and Capabilities (business cases, metrics, pilots) | Emerging (foundations and first experiments, struggling to scale) | Piloting | Wharton wave 2 "Experimentation" (2024) |
| Adopting | late 2 / early 3 (not separately named) | early Scaling | Scaling begins | Deloitte "redesigning key processes": 30% [DELOITTE-STATEAI-2026 p.7] |
| Scaling | 3 Develop AI Ways of Working (platform, reuse, dashboards, test-and-learn) | Scaling (strategy and advanced capabilities, starting to generate value) | Scaling and fully scaled | Wharton wave 3 "Accountable Acceleration" |
| AI-native | 4 Become AI Future Ready (AI in all decisions; sells AI-augmented services) | Future-built | "AI high performers" (5%+ of EBIT and "significant" value) | Deloitte "deeply transform": 34%; Wharton wave 4 "Success Through Transformation" [WHARTON-2026] |

Where they agree: (1) a break between pilots and scaled use; (2) a small top tier; (3) value tracked at enterprise level only in upper tiers; (4) workflow redesign, leadership ownership, governance and reuse separate the tiers. Where they differ: (a) the number of stages (four in CISR, BCG and McKinsey; five in 8 of the 15 models in the Sadiq literature review table [SADIQ-2021 Table 5, my count: 8 five-level, 4 four-level, one each six-level, nine-level and none]); (b) how they treat agents (BCG calls agents "the next step", Wharton finds the fullest agentic use correlates with the highest transformation); (c) thresholds: each uses its own scoring (CISR "Total AI Effectiveness" bands; BCG 41-capability score bands 0-25, >25-50, >50-75, >75-100; McKinsey self-reported phase; McKinsey high performers by EBIT share) [MITCISR-2024 fn.1; BCG-GAP-2025 p.19]. No standard terminology exists [SADIQ-2021 §Components].

**Table B. Survey evidence on how organizations are spread across stages (2025-2026)**

| Source | Population and size | Who measured | Stage-like split |
|---|---|---|---|
| MCKINSEY-SOAI-2026 [§Use of AI is deepening; About the research] | 1,719 respondents, 97 nations, fielded 2026-05-04 to 06-08; weighted by national GDP share | self-reported (consultancy survey) | 44% say AI is scaling across the enterprise (38% a year earlier); 54% in firms with revenue of $1bn+ vs one-third of smaller; high performers about 6% |
| MCKINSEY-SOAI-2025 [Ex.1; Ex.5] | 1,993 respondents, fielded 2025-06-25 to 07-29 | self-reported | 88% regular use in 1+ function; of organizations using AI, chart values 32 / 30 / 31 / 7 for experimenting / piloting / scaling / fully scaled (order inferred from the 2026 statement that 38% were scaling, i.e. 31 + 7) |
| BCG-AIX-2026 [press release; FAQ in publication page] | more than 1,300 CxOs and senior leaders, 20+ sectors (n=1,330 in the press release) | self-reported (consultancy survey) | stagnating 4.5%, emerging 47%, scaling 41%, future-built 7.5% |
| BCG-GAP-2025 [Ex.1; p.19] | 1,250 CxOs and senior executives, 68 countries, nine industries | self-reported; results "reflect the business area respondents know best" | 2025: stagnating 14%, emerging 46%, scaling 35%, future-built 5% (2024: 25 / 49 / 22 / 4) |
| MITCISR-2025 [Figure] | 2025 Real-Time Business Survey, N=152; 2022 Future Ready Survey, N=721 | self-reported, grouped by "Total AI Effectiveness" | 2022: 28 / 34 / 31 / 7%; 2025: 13 / 23 / 46 / 18% |
| DELOITTE-STATEAI-2026 [pp.7-8] | 3,235 leaders, 24 countries, fielded 2025-08/09; half IT, half line of business | self-reported (consultancy survey) | 37% surface-level use, 30% redesigning key processes, 34% deeply transforming; 25% have moved 40%+ of experiments to production |
| WHARTON-2026 [Exec Summary p.5, p.15-16] | about 1,400 US full-time private-sector employees at firms with 1,000+ staff and >$50m revenue (managers+ n=1,007; entry/mid-level n=409), fielded 2026-07-09 to 07-29 | self-reported (academic centre with a research firm that designs the sample) | 28% "fully embedded" in core workflows; 73% say workflows changed significantly; 80% positive return, 28% strongly positive |
| CENSUS-BTOS-2026 [§BTOS data; §Industry] and NBER-BONNEY-2026 [abstract] | nationally representative US firms; second AI supplement from 2025-11-17 | independent (statistical agency) | 17-20% of firms use AI in any business function (Dec 2025 to May 2026); 37% of firms with 250+ staff; Information 39.7%, Finance and Insurance 33.9%, Retail about 14%; among adopters, 57% use AI in three or fewer functions |
| GALLUP-2025 [Key findings] | 23,068 US employees, fielded 2025-08-05 to 08-19 | independent (poll) | 45% of employees use AI at work at least a few times a year; 10% daily; 37% say their organization has implemented AI, 40% say not, 23% do not know |
| MIT-NANDA-2025 [§3.2; Methodology] | 300+ public initiatives, interviews at 52 organizations, 153 leaders surveyed at four conferences (Jan-Jun 2025); "directionally accurate", not peer-reviewed | self-reported and anonymized | 5% of custom enterprise tools reach production; over 80% explored or piloted generic tools, nearly 40% report deployment |
| IBM-CEO-2025 [press release] | 2,000 CEOs, 33 countries, 24 industries, Feb-Apr 2025 | vendor-published | only 25% of AI initiatives delivered expected ROI over the last few years; 16% scaled enterprise-wide |
| STANFORD-AIINDEX-2026 [Top takeaways 1, 5] | compiled index | independent | "Organizational adoption reached 88%"; documented AI incidents 362 (233 in 2024) |

The Census versus consultancy gap (about 20% vs 88%) is a population and definition effect, not a contradiction: Census asks all firms about use in a business function (wording changed on 2025-11-17 from "in producing goods or services") while the consultancy samples are senior leaders, mostly of large organizations, asked about "regular use in at least one function" [CENSUS-BTOS-2026 §Background; MCKINSEY-SOAI-2025 Ex.1 note].

### 2.1 Curious

- **Observable markers (what a leader can show or count).**
  - Informal individual use exceeds what the organization can see: 78% of AI users bring their own tools (Microsoft and LinkedIn, 31,000 people, 31 countries, vendor survey) [MSFT-WTI-2024 §BYOAI]; workers at over 90% of surveyed companies reported regular personal-tool use while 40% of those companies had bought an official subscription (interview-based, preliminary) [MIT-NANDA-2025 §3.3].
  - What people can see depends on seat: 26% of individual contributors, 16% of managers and 7% of leaders said they did not know whether their organization had implemented AI (independent poll, US employees) [GALLUP-2025 Key findings].
  - Governance artefacts a leader can show or fail to show: a ban or acceptable-use rule, an inventory of AI systems (NIST AI RMF GOVERN 1.6 lists "mechanisms are in place to inventory AI systems") [NIST-AIRMF-2023 Part 2, Core, GOVERN table], a named owner. CISR's stage-1 descriptors: educating the workforce, setting acceptable-use policies, working on data access, deciding where humans must be in the loop [MITCISR-2024 §Stage 1].
- **Typical blockers (beyond the stage card).** Colleagues without access knew little about capabilities, limitations and security (DBT control-group interviews, n=6) [DBT-COPILOT-2025 p.5 Acceptable use]; users were anecdotally less likely to use the tool if line managers were hesitant [DBT-COPILOT-2025 p.5 Attitudes]; in BCG's laggards, top management "may talk the talk" but sets no value ambition and delegates to middle management [BCG-GAP-2025 p.5]; in immature sectors fewer than 50% of employees have access to generative AI tools vs 70%+ in mature sectors [BCG-GAP-2025 p.7 sidebar].
- **What to emphasize.** Make safe use possible rather than only prohibiting use; build literacy at board and top-team level and on AI inside existing software [MITCISR-2024 §Stage 1]; create the inventory. In the EU, Article 4 requires providers and deployers to "take measures to support the development of AI literacy" of staff; the explorer lists it as in force from 2 February 2025 and shows tracked amendments linked to the Digital Omnibus, so check the current text [EUAIA-EXPLORER-2024 Art. 4].
- **Investments and capabilities that move the scope on.** Sanctioned tools plus training. Evidence that access alone is not enough: Deloitte's surveyed organizations lifted worker access from under 40% to about 60% in a year, yet fewer than 60% of those with access use AI in a daily workflow [DELOITTE-STATEAI-2026 p.8]; BCG says access and training are "insufficient by itself" but a strong indicator of seriousness [BCG-GAP-2025 p.7]. Funding at this stage targets board and top-team literacy [MITCISR-2024 §Stage 1].
- **Exit criteria.** Keep the onboarding card ("a few named people use AI weekly on real work; an acceptable-use rule exists; one quick win has been shown"). Add, as advisor heuristic: an inventory exists (NIST GOVERN 1.6), and the scope can state its sanctioned tools and where unsanctioned use is likely.
- **Failure points.** (1) Ban without an approved alternative, which pushes use into personal tools (shadow AI) [MSFT-WTI-2024 §BYOAI; MIT-NANDA-2025 §3.3]. (2) Leaders judging from their own seat [GALLUP-2025]. (3) Waiting: 31% of 3,412 Gartner webinar attendees (January 2025 poll) were "wait and see" or unsure on agentic AI investment [GARTNER-AGENTIC-2025 §poll].
- **Survey evidence.** Stagnating share: BCG 14% (2025) to 4.5% (2026); CISR stage 1: 28% (2022, N=721) to 13% (2025, N=152). Both are large-organization self-reports; the Census figure for all firms is the better guide for small firms (Table B).

### 2.2 Experimenting

- **Observable markers.**
  - Usage is high among licensed users: DWP 65% daily and 30% weekly (treatment survey) [DWP-COPILOT-2026 §2.3]; GDS 39% multiple times a day and 43% at least multiple times a week [GDS-COPILOT-2025 §4.1].
  - Gains are felt by individuals but not visible in a business measure: 80% report individual productivity gains vs 37% EBIT contribution [MCKINSEY-SOAI-2026]; DBT "did not find evidence that time savings have led to improved productivity" and control-group colleagues had not observed it [DBT-COPILOT-2025 p.4].
  - Count the pilot-to-production ratio, not pilots: Deloitte (25% moved 40%+ of experiments to production; 54% expect to within three to six months) [DELOITTE-STATEAI-2026 p.8 Fig.1]. The expectation is a forecast, not an outcome.
  - Measures used are mostly efficiency: in Wharton 2026, "time saved" is the most common investment metric and organizations measuring growth outcomes report strong ROI more often (35% vs 13% efficiency-only) [WHARTON-2026 Exec Summary].
- **Typical blockers (beyond the stage card).** Change management, executive sponsorship, user experience and output quality head the 52-organization barrier ranking [MIT-NANDA-2025 §4]. A pilot "typically can run with a small team" in an isolated setting while production needs infrastructure, integration and support, and models that test well can fail on edge cases at scale; one interviewee described "pilot fatigue" [DELOITTE-STATEAI-2026 p.8]. Data-security concern reduced benefits in a minority of GDS participants and limits were seen on "complex, nuanced, or data-heavy" work [GDS-COPILOT-2025 §Key findings]. Self-led learning raised satisfaction more than formal sessions in DBT [DBT-COPILOT-2025 p.5].
- **What to emphasize.** Fewer workflows, end to end: BCG says some leaders "experiment too widely, spreading their resources over scores of complex workflows" and end with disconnected initiatives [BCG-GAP-2025 p.5]. Pick measures beyond time saved. Treat expert-graded evaluation sets as part of the pilot: Morgan Stanley describes evals run before each use case, graded by advisors and prompt engineers [OPENAI-MORGANSTANLEY §Building a foundation].
- **Investments and capabilities that move the scope on.** A named owner, baseline and designed human check (onboarding card). Packaged shared skills and one approved tool: Wharton 2026 finds 50% strongly positive ROI among organizations standardized on a single approved platform vs 9% among those "still experimenting" (correlation, self-reported) [WHARTON-2026 Exec Summary]. NANDA's interview data say external partnerships succeed twice as often as internal builds, with an explicit caveat that figures are "directionally accurate" [MIT-NANDA-2025 §1; §3.2 Limitations]; treat as a weak signal.
- **Exit criteria.** Keep the card. Add, advisor heuristic: every open pilot has a dated scale / stop / hold decision; expert-graded test cases exist for the first workflow; the measure is not hours saved alone.
- **Failure points.** Pilot purgatory (measured size varies: 5% NANDA, 25% Deloitte, 54% Wharton; see Table B). Time saved absorbed without a destination (DBT found some tasks took extra time and "additional workload only completed due to users having" the tool) [DBT-COPILOT-2025 p.4]. Mandated use without redesign: Shopify's April 2025 memo made AI use a baseline expectation and added AI questions to performance reviews, but it reports no outcome measure [SHOPIFY-LUTKE-2025 §memo].
- **Survey evidence.** Emerging (BCG) 46% (2025) and 47% (2026); CISR stage 2: 34% (2022) and 23% (2025); McKinsey experimenting or piloting 62% of AI-using organizations in 2025 (32 + 30, see Table B note).

### 2.3 Adopting

- **Observable markers.**
  - AI inside the system where work is recorded, with owners: Kaiser Permanente's Permanente Medical Group reports 7,260 physicians used an ambient AI scribe in 2,576,627 encounters between October 2023 and December 2024 [KP-AISCRIBE-2025]; Morgan Stanley reports over 98% of wealth-management advisor teams use its internal assistant [OPENAI-MORGANSTANLEY §98% adoption].
  - A tiered autonomy register: Dayos (a software company) scored every IT ticket type on severity, reversibility and feasibility of human oversight, which fixed each tier's autonomy (Tier 1 about 60% of tickets, fully automated with biweekly audits; Tier 2 about 30%, human approval; Tier 3 about 10%, agent does not touch) [IMDA-MGF-2026 case study "Dayos"].
  - Sanctioned access and use counts (Deloitte: around 60% with access, fewer than 60% of those using daily) [DELOITTE-STATEAI-2026 p.8].
- **Typical blockers (beyond the stage card).** Production exposes edge-case failures that pilots hide [DELOITTE-STATEAI-2026 p.8]. 51% of McKinsey's AI-using respondents report at least one negative consequence, with nearly one-third reporting consequences from inaccuracy [MCKINSEY-SOAI-2025 §Efforts to mitigate AI risks, Ex.19]. About 20% of 2026 respondents say operating costs including tokens constrained AI use [MCKINSEY-SOAI-2026 §While AI investments are increasing].
- **What to emphasize.** Designed human checks and measurement. High performers are more likely to have "defined processes to determine how and when model outputs need human validation" [MCKINSEY-SOAI-2025 Ex.14]. For the first bounded delegated workflows: graduate autonomy from shadow mode (BCG's four tiers: shadow, supervised, guided, full; agents "run in Tier 1 (Shadow Mode) until they prove they align with your organization's risk appetite") [BCG-AGENTS-2025 §Trust Protocol]; roll out gradually by users, tools and systems (GovTech's phased rollout: internal staff only, no external tool connections, low-risk systems first, with central logging built in parallel) [IMDA-MGF-2026 §Gradual deployment]; and, for high-risk systems under the EU AI Act, give oversight to people with "necessary competence, training and authority" (Article 26(2); explorer shows applicability from 2 December 2027 for Annex III systems) [EUAIA-EXPLORER-2024 Art. 26].
- **Investments and capabilities that move the scope on.** Reusable parts ("architecting for reuse", shared data via APIs) [MITCISR-2024 §Stage 2-3]; a value-tracking framework with hypotheses, tests and scale plans (Guardian Life) and two-track governance review (formal board plus a fast-track board with risk, privacy and security members) [MITCISR-2025 §Guardian]; a central owner (Wharton 2026: 58% strongly positive ROI among organizations with a newly designated chief AI officer vs 8% with no such role; correlation, self-reported) [WHARTON-2026 Exec Summary].
- **Exit criteria.** Keep the card. Add, advisor heuristic: the review step has a measured intervention rate; costs per workflow are known. For delegation, the five gates in onboarding stand.
- **Tension to surface with delegation.** Wharton 2026: where agents act with every action approved, 16% of departments are "transformed"; with sample checking, 18%; advise-only, 25%; fullest agentic use with monitoring, 31%; only 17% of departments permit genuine autonomy; 11% say nobody is clearly accountable for agent errors [WHARTON-2026 Exec Summary pp.16-17]. The survey cannot say whether autonomy causes transformation. It does support planning the route to monitored autonomy (BCG: companies with all six agent controls generate three times the agentic value of those with one) rather than parking at approval-on-everything [BCG-AIX-2026-PUB §Applied AI].
- **Failure points.** Spreading across too many workflows [BCG-GAP-2025 p.5]. Rubber-stamp review (see archetype use cases below; the cross-industry sources read give no rate). Extending a pilot design into production without redesign [DELOITTE-STATEAI-2026 p.8].
- **Survey evidence.** BCG scaling tier 35% (2025) and 41% (2026); CISR stage 3: 31% (2022) and 46% (2025); Deloitte "redesigning key processes" 30%.

### 2.4 Scaling

- **Observable markers.**
  - A shared platform with reusable components and value tracked as a portfolio: Ally's Ally.ai platform (launched July 2023) houses tools and integrates several commercial large language models with the bank's data [MITCISR-2024 §Stage 3]; DBS tracks economic impact (it was "one of only two banks globally" to disclose it in 2021) and reports about SGD 1 billion in 2025 from data analytics and AI/ML initiatives, 430+ use cases, 2,000+ models [DBS-AR-2025 CEO reflections].
  - Spending outside IT: BCG reports AI spend at 3.3% of revenue with more than 80% sitting outside the enterprise IT budget (2026 index) [BCG-AIX-2026].
  - Dedicated leadership: chief AI officer roles present in 61% of Wharton 2025 respondents' enterprises [WHARTON-2025 Key Takeaways].
  - Workforce capability: future-built firms expect to upskill more than 50% of staff vs 20% at laggards and are four times as likely to carve out time for structured learning [BCG-GAP-2025 §What Value Generators Do Differently, Upskilling]; Italgas's academy delivered over 30,000 AI and data training hours in 2024 [MITCISR-2025 §Italgas].
- **Typical blockers (beyond the stage card).** Legacy systems and fragmented data (Guardian had to upgrade mainframe systems and consolidate data first) [MITCISR-2025 §Guardian Systems]; costs (McKinsey 2026: about one in five constrained); the gap between conviction and financial return (37% EBIT contribution, flat) [MCKINSEY-SOAI-2026]; agent governance maturity (21% mature) [DELOITTE-STATEAI-2026 p.7].
- **What to emphasize.** CISR names four challenges for the move from pilots to scale: strategy, systems, synchronization (roles and teams), stewardship (monitoring and compliance) [MITCISR-2025 §Four Challenges]. Add cost management and portfolio decisions (stop as well as start): DBS says capital is allocated "only to initiatives with proven traction" with course-correction for those that fall short [DBS-AR-2025 CEO reflections].
- **Investments and capabilities that move the scope on.** A single enterprise-wide platform with common architecture and controls (more than two-thirds of future-built firms are committing to one) and data transformation (95% of future-built firms are undertaking one) [BCG-AIX-2026-PUB §Applied AI]; strategic workforce planning (55% of future-built vs 17% of laggards) [BCG-AIX-2026-PUB]; value measured at P&L (95% of future-built use clear KPIs or track P&L value) [BCG-AIX-2026-PUB §Strategic Clarity]. The largest financial step in CISR's 2025 data is from stage 2 to stage 3 (growth versus industry average: -6.8 points at stage 2, +4.7 at stage 3; profit -1.4 to +0.8) [MITCISR-2025 Figure].
- **Exit criteria.** Keep the card. Evidence-based additions (advisor heuristic): AI value shown in a P&L line, not only in surveys; cost per unit of AI work is tracked; an agent control set exists (BCG lists oversight and rollback gates, security, audit and cost guardrails) [BCG-AIX-2026 press release].
- **Failure points.** Scaling autonomy ahead of controls (BCG 42% expect autonomy by 2030, 5% have the full control set; Deloitte 74% plan agents, 21% mature governance); customer-facing scale without a quality check (Klarna); unreviewed AI content in deliverables (Deloitte Australia); expectation drift on workforce: 14% report AI contributed to a workforce decline in the past year vs 32% who expected it a year earlier [MCKINSEY-SOAI-2026 §Previous expectations].
- **Survey evidence.** Scaling and future-built together 48.5% (BCG 2026); CISR stage 3 plus 4: 64% (2025, N=152); McKinsey 44% scaling (2026); Gartner reports 45% of high-maturity organizations keep AI projects operational for three years or more vs 20% of low-maturity (432 respondents, late 2024; search-only) [GARTNER-MATURITY-2025].

### 2.5 AI-native

- **Observable markers.**
  - Pricing, services or cost base changed by AI, with figures: Ping An reported that by end-2022 49% of product sales were made by AI service representatives and 82% of service interactions handled by them, RMB 600 million saved in labour costs, and AI banking offered as a service to 30 other banks [MITCISR-2024 §Stage 4]; Italgas's Bludigit reported EUR 3 million revenue at a margin above 50% in 2024 from selling an AI-built remote-site tool as software [MITCISR-2025 §Italgas Stewardship].
  - Enterprise P&L attribution: McKinsey high performers (5%+ of EBIT and "significant" value) were about 6% of respondents in 2025 and 2026 [MCKINSEY-SOAI-2026 §High-performing organizations]. BCG's future-built: 2.4x revenue growth and 2.8x EBITDA growth vs laggards (self-reported maturity; financials from third-party data in the 2025 study) [BCG-AIX-2026; BCG-GAP-2025 p.19].
  - CISR stage 4 firms were above industry average in 2024 by 13.9 points on growth and 9.9 on profit (N=152) [MITCISR-2025 Figure].
- **Typical blockers.** Beyond the card: workforce redesign (BCG: 55% vs 17% do strategic workforce planning); governance of increasingly autonomous systems (above); cost constraints (high performers report cost constraints on coding agents about three times as often) [MCKINSEY-SOAI-2026 §Exhibit 14 text].
- **What to emphasize.** Test claims. Top tiers are small by every definition (5-18% across sources) and "AI-first" statements are not evidence. Shopify's memo is a statement of expectations, not a measured result [SHOPIFY-LUTKE-2025]. Ask for the metric that changed.
- **Investments and capabilities.** In-house AI infrastructure integrating purchased models with enterprise APIs, data and processes (CISR "proprietary AI") [MITCISR-2024 §Stage 4 fn.]; continuous experimentation (DBS's CEO set a KPI of 1,000 experiments a year, cited by CISR) [MITCISR-2024 §Your AI Maturity Stage Today].
- **Exit criteria.** None: re-diagnose each review. BCG's own index shifted from a 41-capability "Build for the Future" score (2025) to an "Applied AI Index" (2026); the pages read do not say the series is like-for-like [BCG-GAP-2025 App.; BCG-AIX-2026].
- **Failure points.** Over-rotation to cost (Klarna, below); claims that outrun evidence; margin pass-through when pricing stays time-based (see archetype pricing use cases).
- **Survey evidence.** CISR stage 4: 7% (2022) and 18% (2025, N=152); BCG future-built 5% and 7.5%; McKinsey 6%; Deloitte 34% "deeply transforming". The spread of 5-34% reflects definitions (value-based vs intention-based).

---

## 3. Examples

Grades per vocabulary. "Provenance" is who measured. Ladder and scope are my classification of the described change.

### 3.1 Curious

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| C1 | Kaiser Permanente (healthcare, US) | Defined seven principles for assessing responsible use of AI (privacy, reliability, high-quality and affordable outcomes, transparency, equity, customer prioritization, trust) in August 2024; CISR cites it as a stage-1 example | n/a (governance step) / step | None published; policy only | B | MITCISR-2024 [§Stage 1] |
| C2 | Shopify (technology) | Before the April 2025 mandate, AI use was encouraged. The CEO wrote that "the call to tinker with it was the right one, but it was too much of a suggestion" | assist / step | No figure; self-described voluntary phase | B | SHOPIFY-LUTKE-2025 [memo, para 2] |
| C3 | UK Department for Business and Trade (public sector) | During the Copilot pilot, colleagues without licences (control group, 6 interviewed) lacked knowledge of capabilities, limitations and security concerns | assist / step | Qualitative finding, department-run evaluation, self-reported | B | DBT-COPILOT-2025 [p.5 Acceptable use and accuracy] |

Archetype use cases showing this stage (id, grade): `assurance-assurance-over-ai-01` (D), `tax-data-technology-07` (C), `security-operations-12` (A).
Note: organizations rarely publish that they are at Curious; the three examples show the stage inside an organization that is further along elsewhere.

### 3.2 Experimenting

| # | Organization (industry) | What changed | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| X1 | UK Government Digital Service with 12 organizations (public sector) | 20,000 employees used a licensed AI assistant in office tools for three months (2024-09-30 to 12-31) | assist / step | Average 26 minutes a day saved, estimated by participants using ranges and midpoints; 39% used it multiple times a day; authors state it was "not possible to identify how time saved was spent". Self-reported (government evaluation) | B | GDS-COPILOT-2025 [§Key findings; §4.1; §Conclusion] |
| X2 | UK Department for Business and Trade (public sector) | 1,000 licences for the same tool, Oct-Dec 2024; diary study (32% response), observed tasks, 19 interviews (13 pilot participants, 6 control group) | assist / step | 72% satisfied, NPS 31; small time savings on most tasks, extra time on scheduling and images; "did not find evidence" time savings improved productivity; hallucinations seen and inconsistent quality assurance. Self-reported (department evaluation with control group) | A | DBT-COPILOT-2025 [pp.4-5] |
| X3 | UK Department for Work and Pensions (public sector) | 3,500+ staff with licences; survey of treatment (n=1,716, 48% response) and comparison group; Jan-Mar 2025 | assist / step | Estimated 19 minutes a day saved (regression against comparison group; outcome is categorical self-report); 73% say outputs improved; 65% report daily use. Self-reported (department evaluation) | A | DWP-COPILOT-2026 [§Findings; §2.3; §4] |
| X4 | Guardian Life (insurance, US) | Disability underwriting pilot with a partner: a generative tool summarizes documents and supports decisions | augment / step | Participating underwriters "saving on average five hours per day" (pilot; method not stated). Self-reported via CISR | B | MITCISR-2024 [§Stage 2] |
| X5 | Shopify (technology) | April 2025 memo: AI use is a baseline expectation; AI in the prototype phase; AI questions in performance and peer reviews; teams must show why AI cannot do the work before asking for headcount | assist / process | No outcome measure published. Company memo | B | SHOPIFY-LUTKE-2025 [memo §expectations]; CNBC-SHOPIFY-2025 |

Archetype use cases (id, grade): `professional-services-talent-learning-16` (A), `professional-services-work-production-06` (A), `professional-services-work-production-07` (A), `professional-services-talent-learning-11` (A).

### 3.3 Adopting

| # | Organization (industry) | What changed | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| A1 | Permanente Medical Group, Kaiser Permanente (healthcare, US) | Ambient AI scribe offered to physicians after a 10-week pilot in 2023; vendor changed between pilot and rollout | augment / step | 7,260 physicians, 2,576,627 encounters (Oct 2023-Dec 2024); users spent less time in the record outside 7am-7pm and less time on notes per visit; surveys: 102 physicians (88% said positive impact on visit interaction), 118 patients (two-thirds comfortable); article reports "nearly 16,000 hours" saved. Self-reported (study by the organization's authors; read via the organization's research summary, not the journal) | A | KP-AISCRIBE-2025 [paras 2-6] |
| A2 | Morgan Stanley Wealth Management (financial services) | Internal assistant for advisors answering from a document corpus; pre-deployment evals graded by advisors; daily regression suite; meeting-summary tool where advisors edit outputs | assist, augment / process | "over 98%" of advisor teams use the assistant; document access "from 20% to 80%" (measure not defined); coverage from 7,000 questions to a corpus of 100,000 documents. Vendor-published customer story; no quality rate | B | OPENAI-MORGANSTANLEY [§98% adoption; §Building a foundation; §Strengthening trust] |
| A3 | Dayos (software, IT service desk) | AI ticketing agent replaces the service tool; tickets tiered by severity, reversibility, oversight feasibility; Tier 1 audited biweekly | automate (Tier 1), augment (Tier 2) / process | Retirement took 45 days; legacy licensing cost down USD 121,000 a year; tier shares 60/30/10. Regulator-published, company-reported; no error or override rate | B | IMDA-MGF-2026 [case study Dayos] |
| A4 | GovTech Singapore (public sector) | Phased rollout of agentic coding assistants from October 2025: internal developers only, no external tool connections, low-risk systems; controls built during phase one | augment / step | Describes the approach; no productivity or incident figures. Regulator-published, organization-reported | B | IMDA-MGF-2026 [§Gradual deployment] |
| A5 | Schaeffler with Siemens (manufacturing) | Industrial assistant connected to the automation engineering portal for controller code generation and error finding (announced October 2024) | assist / step | "begun using"; no figures published in the article read. Press, vendor statements | B | AUTOMATIONWORLD-SCHAEFFLER-2024 [paras 1-4] |

Archetype use cases (id, grade): `assurance-controls-testing-04` (A), `assurance-controls-testing-11` (A), `security-governance-risk-01` (A), `security-application-security-04` (A), `security-operations-02` (A), `assurance-controls-testing-05` (A; bounded delegated workflow), `tax-compliance-corporate-21` (C; gated rollout with thresholds).

### 3.4 Scaling

| # | Organization (industry) | What changed | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| S1 | Ally Financial (financial services, US) | Ally.ai platform (July 2023) integrates commercial language models with bank data; call summarization on customer calls; marketing assistant | augment / process | Average three minutes saved per call on more than four million calls in 2023; creative campaigns 34% faster. Self-reported via CISR ("used with permission") | A | MITCISR-2024 [§Stage 3] |
| S2 | Italgas (energy utilities, Italy and Greece) | Cloud platform (IoT, data, 23 AI models) shared by an innovation unit and business units; business translators embedded; 18 cross-functional teams delivered MVPs in 2024 | augment, automate / process | WorkOnSite: project completion 40% faster, inspections reduced by 80%; 30,000+ training hours in 2024. Self-reported via CISR interviews and company reports | A | MITCISR-2025 [§Italgas] |
| S3 | Guardian Life (insurance, US) | Value-tracking framework, product-and-platform operating model, two-track governance review; RFP and quote automation piloted in employee benefits | augment / process | Proposal turnaround from "five to seven days" to "twenty-four hours" in the pilot; move to scale planned for 2026 ("will"). Self-reported via CISR interviews | B | MITCISR-2025 [§Guardian] |
| S4 | Walmart (retail, US) | Customer-facing shopping assistant in the app | automate (customer interaction) / process | CEO on the Q4 FY2026 call: users have average order value "about 35% higher" than non-users; about half of app users have used it. Self-reported earnings call; a user-versus-non-user gap, not a causal effect | A | WALMART-Q4FY26-2026 [CEO remarks, 00:05:46 and 00:21:22; EVP 00:21:53] |
| S5 | Klarna (fintech, payments) | AI assistant answering customer-service chats, with a handoff to humans | automate / process | Feb 2024 press release: 2.3 million conversations (two-thirds of chats in the first month), "25% drop in repeat inquiries", resolution under 2 minutes vs 11, estimated USD 40 million profit improvement in 2024 ("estimated"). May 2025: the CEO said the AI approach was cheaper but "lower quality" and the firm was hiring human agents again. Self-reported | A (2024 metrics); reversal is a failure point | KLARNA-2024; ENTREPRENEUR-KLARNA-2025 [paras 3-5] |

Archetype use cases (id, grade): `assurance-controls-testing-08` (A), `assurance-controls-testing-06` (A), `security-operations-01` (A), `security-operations-21` (A), `security-ai-security-08` (A), `security-ai-security-17` (A).

### 3.5 AI-native

| # | Organization (industry) | What changed | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| N1 | Ping An (financial services, China) | AI service representatives sell and service at scale; AI banking offered to other banks as a service | automate / model | By end-2022: 49% of product sales and 82% of service interactions by AI representatives; RMB 600 million labour cost saved; AI banking provided to 30 other banks. Self-reported (company results) as cited by CISR; underlying results not opened | A | MITCISR-2024 [§Stage 4] |
| N2 | DBS (financial services, Singapore) | AI embedded across the bank; economic impact tracked since at least 2021; gen-AI assistant open to employees in core markets | augment, automate / model | 2025: 2,000+ models, 430+ use cases, about SGD 1 billion economic value (data analytics and AI/ML combined, "approximately"). Self-reported annual report | A | DBS-AR-2025 [CEO reflections] |
| N3 | Italgas (energy utilities) | Remote-site tool commercialized as software through a group company | automate / model | 2024: EUR 3 million revenue, margin above 50%. Self-reported via CISR citing company pages | A | MITCISR-2025 [§Italgas Stewardship] |

Archetype use cases (id, grade): `security-vulnerability-exposure-01` (A), `security-vulnerability-exposure-12` (A), `assurance-soc-attestation-16` (B), `assurance-controls-testing-17` (B), `assurance-controls-testing-19` (B), `professional-services-firm-finance-17` (B), `professional-services-scoping-pricing-19` (B), `tax-compliance-individual-business-24` (B).

Totals: 21 examples. Grade A: 10 (X2, X3, A1, S1, S2, S4, S5, N1, N2, N3). Grade B: 11 (C1, C2, C3, X1, X4, X5, A2, A3, A4, A5, S3). No C or D examples. Industries: healthcare (2), public sector (5), financial services (4), insurance (2), technology and software (3), retail (1), manufacturing (1), energy utilities (2), fintech (1). Professional services appears only through archetype ids and the Deloitte Australia incident (section 5).

---

## 4. Expert moves and probes

### Curious
1. "Which AI tools did people use at work last week, including their own?" Reveals the gap between sanctioned and actual use (78% BYOAI, 90% vs 40% in the sources above) and whether the leader can see it at all.
2. "Is there a policy, and does it say what people may use?" A ban-only rule predicts shadow use; an acceptable-use rule with approved tools predicts visible use.
3. "Who in this scope would say they don't know whether the organization uses AI?" Gallup's 26% / 16% / 7% gradient shows seat-dependent visibility; ask for a count by role.
4. "Has the board or top team had any AI training?" CISR stage-1 funding priority; also the EU Article 4 literacy duty where it applies.
5. "Do you have a list of AI systems, including those embedded in vendor software?" Tests the NIST GOVERN 1.6 inventory idea and surfaces "invisible AI".
6. "What is the one task you would most like to hand over, and what stops you?" Finds the first quick win and the real blocker (confidentiality, accuracy, fit).
7. Heuristic: do not plan delegated workflows here; show examples as a target picture only (onboarding delegation rule).

### Experimenting
1. "List every pilot started in the last 12 months and what happened to each." Counts the pilot-to-production ratio and shows whether stops produced lessons (Deloitte, NANDA, Wharton ratios differ 5% to 54%, so ask for the scope's own).
2. "Where is the baseline for the workflow, and who owns it?" Without a baseline, "26 minutes a day" cannot become a business number (GDS vs DBT).
3. "What happened to the hours saved?" Captured value or absorbed time (DBT: extra tasks created by the tool; GDS could not say how time was spent).
4. "Who checks the output, and what would they catch?" Tests for a designed human check; DBT found inconsistent quality assurance.
5. "Do you have 20 to 50 expert-graded examples for the first workflow?" Morgan Stanley's eval-first approach; reveals whether quality can be measured before scaling.
6. "Is the metric hours saved, or something the business already tracks?" Wharton: growth measures 35% strongly positive ROI vs 13% efficiency-only.
7. "Which pilot would you stop today?" A learning loop versus a pilot graveyard; Deloitte's "pilot fatigue".
8. "Did a mandate or a champion drive use?" Shopify-style mandates raise usage but the memo reports no outcome; ask for evidence that use changed results.

### Adopting
1. "How many workflows run as normal work, and what does each measure?" Owned, measured workflows are the stage's defining marker.
2. "Where does the AI sit relative to the system of record?" Integration versus a side tool (KP's scribe in the visit workflow; Dayos's agent as the ticketing front end).
3. "What fraction of AI output is changed or rejected by reviewers?" No cross-industry rate is published; asking exposes whether the scope measures it at all (rubber-stamp risk).
4. "For each automated action, how bad is a mistake, can it be undone, and can a person realistically check it?" The Dayos three-question tiering; yields an autonomy register.
5. "Is the agent running in shadow mode with written rules for earning autonomy?" Delegation gate 4; BCG tiers.
6. "Who has the authority and competence to stop it?" EU Article 26(2) language; Wharton: 11% say nobody is clearly accountable for agent errors.
7. "What does one workflow cost to run, including tokens and review time?" Cost is a constraint for about one in five McKinsey respondents.
8. "What did the second workflow reuse from the first?" Early test of the Adopting-to-Scaling reuse criterion.

### Scaling
1. "Is there one place where value from all AI workflows is recorded, and who reads it?" Portfolio tracking (DBS economic-impact reporting; Guardian's three-phase value framework).
2. "Show me a line in the P&L, not a survey." McKinsey's gap between individual and EBIT impact; BCG's 95% of future-built using KPIs or P&L value.
3. "Who owns AI at your level: business, technology, both, or nobody?" Wharton chief-AI-officer and single-platform contrasts (correlational).
4. "Which controls exist for agents (oversight, rollback, audit, cost, security) and which are missing?" BCG: 5% have the full set; Deloitte: 21% mature governance.
5. "What is the decision path for a new use case, and how long does it take?" Guardian's fast-track review; shows whether governance enables or blocks.
6. "What have you stopped?" Portfolio discipline (DBS: capital only to initiatives with proven traction).
7. "What share of staff has had protected time to learn, and what do the managers think versus the staff?" BCG's learning-time contrast; Wharton reports a management versus employee alignment gap.
8. "Which customer-facing automation has a sampled quality review and a human fallback?" Klarna's reversal.

### AI-native
1. "What has changed in price, package or sourcing because of AI, and what are the numbers?" Tests commercial change (Ping An's service to other banks; Italgas's software revenue).
2. "Have you launched something you could not have delivered before?" New services as an exit marker.
3. "What fraction of enterprise EBIT can you attribute to AI, and how?" McKinsey's 5%-of-EBIT definition; shows rigor of attribution.
4. "Who is accountable when an agent errs?" Wharton: no single owner reaches 30%.
5. "What happens to pricing if the work takes a tenth of the time?" Time-based pricing exposure (archetype pricing use cases).
6. "What would make you step back a stage?" Klarna-type reversals; stage definitions age quickly (BCG changed its index between years).
7. "Which parts of the claim are verified by someone outside the team?" Separates measured from asserted AI-native status.

---

## 5. Evidence on what works and what fails

**Controlled or independent measurement**
- Field study, customer support at one firm (not named in the abstract): staggered rollout of an assistant to 5,179 agents raised issues resolved per hour by 14% on average and by 34% for novice and low-skilled workers, with minimal impact on experienced workers; also improved customer sentiment and retention. Independent academic; published in the Quarterly Journal of Economics in 2025 [NBER-BRYNJOLFSSON-2023 abstract].
- Preregistered experiment, 758 consultants, 18 tasks "within the frontier": AI users completed 12.2% more tasks and 25.1% faster with improved quality; on one task outside the frontier they were 19% less likely to produce correct solutions. Independent academic (with BCG as partner) [HBS-JAGGED-2023 abstract].
- Randomised trial, 16 experienced open-source developers, 246 issues, early-2025 tools: AI use took 19% longer; developers had expected a 24% speed-up and still believed AI had sped them up by 20% afterwards. Small sample; authors call it a snapshot of early-2025 tools [METR-2025 summary].
- Department evaluations of one assistant (UK government): GDS 26 minutes a day (self-estimated, no control); DWP 19 minutes (comparison group, self-reported categories); DBT no evidence of productivity improvement with hallucinations observed. Self-reported by the departments; designs differ [GDS-COPILOT-2025; DWP-COPILOT-2026; DBT-COPILOT-2025].
- Census Bureau: 18% of firms used AI in at least one function in Nov 2025 to Jan 2026 (32% employment-weighted); among adopters 57% use it in three or fewer functions. Independent [NBER-BONNEY-2026 abstract].
- Documented AI incidents rose to 362 in 2025 from 233 in 2024 (AI Index summary; the underlying incident database was not opened) [STANFORD-AIINDEX-2026 takeaway 5].

**Survey associations (self-reported)**
- McKinsey 2026: high performers redesign workflows (nearly three-quarters vs one-quarter of others), define processes to measure impact and show senior commitment (twice as likely); 14% of AI-using respondents saw workforce decline against 32% who expected it [MCKINSEY-SOAI-2026].
- Wharton 2026: organizations meeting all three "transformational success" components report strongly positive ROI at 67% vs 19%; single approved platform 50% vs 9%; automatic monitoring of agents 24% vs 9% transformed [WHARTON-2026 Exec Summary].
- BCG 2026: companies with all six agent controls generate three times the agentic AI value of companies with one (consultancy survey, self-reported) [BCG-AIX-2026-PUB].
- MIT CISR: financial performance below industry average in stages 1-2 and above in 3-4; the 2025 sample gives the largest step between 2 and 3 [MITCISR-2024; MITCISR-2025].

**Failure analyses and predictions**
- RAND (65 interviews with experienced AI practitioners, 2024) names five root causes of failed AI projects, the first being misunderstanding or miscommunicating the problem; the "80%" failure figure is quoted from other estimates, not measured by RAND, and the study is about AI/ML projects broadly rather than generative tools [RAND-2024 Summary].
- Gartner predicts over 40% of agentic AI projects "will be canceled by the end of 2027" because of cost, unclear value or inadequate risk controls, and estimates about 130 of thousands of agentic vendors are real. Analyst prediction, not a measurement [GARTNER-AGENTIC-2025].
- IBM: 25% of AI initiatives delivered expected ROI, 16% scaled enterprise-wide (CEO survey) [IBM-CEO-2025].
- NANDA: 5% of custom enterprise tools reach production; the authors state figures are directionally accurate and based on interviews [MIT-NANDA-2025 §3.2].
- Named incidents: Klarna (CEO said service quality was lower; hiring humans again, May 2025) [ENTREPRENEUR-KLARNA-2025]; Deloitte Australia (partial refund of a A$440,000 report after fabricated references and a fabricated court quote; the firm disclosed it used a GPT-4o-based tool chain hosted on the client's tenancy; the firm said corrections did not change findings) [CYBERDAILY-DELOITTE-2025]. Other professional-services incidents are in the archetype files (for example the ACS-EY-2026 key).
- Shadow AI: 78% of AI users bring their own tools (vendor survey); 90% of surveyed companies had employees using personal tools vs 40% buying subscriptions (interview-based) [MSFT-WTI-2024; MIT-NANDA-2025].

**Quality evidence, stated plainly.** For the five stages as a whole, the sources read contain no published override rate, escalation rate or parallel-run result from a named organization. Archetype files report the same absence (for example the assurance completion-reporting and tax compliance files note that no source publishes an override rate). The nearest measures are listed above. Tax archetype `tax-compliance-corporate-21` (C) records a worked-example gate set from an AICPA-published framework (for instance a hallucination rate of 2% or less for 60 consecutive days before the next phase); it is an illustration, not a tested standard.

---

## 6. Gaps

- **No longitudinal evidence.** CISR's 2022 and 2025 samples differ (N=721, N=152); BCG changed its index between 2025 and 2026; McKinsey's definitions changed over the years. No study follows the same organizations through stages, so "exit criteria" here are heuristics.
- **No audited pilot-to-production rate.** Figures range from 5% to 54% across incomparable definitions.
- **Curious is underdocumented.** Organizations rarely publish being at the lowest stage; the three examples are from organizations that are further along elsewhere. No named small-firm example was found.
- **Manufacturing and other physical-work industries are thin.** The only named example (Schaeffler with Siemens) has no figures. A search for named manufacturers with measured results found only vendor blogs, which were not used. The Deloitte industry-cut PDFs were not opened.
- **Override and escalation rates absent** (section 5).
- **Secondary reads.** Ping An and Ally figures were read through CISR, not the company reports; Italgas figures through CISR; the Kaiser Permanente study through the organization's research summary, not the NEJM Catalyst article; Morgan Stanley through a vendor customer story whose page carries no date.
- **Blocked or unread:** Gartner's AI maturity model page and the Gartner 45% press release (search-only); ISO/IEC 42001 standard page (blocked, so the standard's management-system clauses were not read; certification appears only through archetype use cases such as `assurance-assurance-over-ai-15`); McKinsey Superagency report (blocked); Australian DTA Copilot trial evaluation (page read gave no content); HBR "workslop" article (paywalled beyond the introduction, not used); the NEJM Catalyst and Quarterly Journal of Economics full texts (abstracts only for QJE/NBER).
- **Practitioner discourse is thin.** Only one practitioner newsletter [MOLLICK-2025] and one CEO memo were read; no conference proceedings, podcasts or community threads were reached in the allotted searches.
- **EU AI Act text.** The explorer pages show tracked amendments tied to the Digital Omnibus; the final adopted wording and dates for Articles 4 and 26 should be verified in the Official Journal before the advisor quotes them.
- **Population caveats for Table B.** Wharton, McKinsey, BCG, Deloitte and IBM sample leaders of large organizations; Census samples all firms. Gallup measures employees' perception, not organizational fact.
- **My mapping in Table A** between five advisor stages and four-stage models is not validated by any source.

---

## 7. Sources

Access: `full` = opened and read (a mirror counts as full where the text was complete); `search-only` = seen in search results only. Types use the vocabulary; government bodies are typed `regulator`.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| MITCISR-2024 | Building Enterprise AI Maturity | Weill, Woerner, Sebastian, MIT CISR | academic | https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian | 2024-12-19 | full |
| MITCISR-2025 | Grow Enterprise AI Maturity for Bottom-Line Impact | Woerner, Sebastian, Weill, Kaganer, MIT CISR | academic | https://cisr.mit.edu/publication/2025_0801_EnterpriseAIMaturityUpdate_WoernerSebastianWeillKaganer | 2025-08-21 | full |
| BCG-GAP-2025 | The Widening AI Value Gap: Build for the Future 2025 | BCG | survey | https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf | 2025-09 | full |
| BCG-AIX-2026 | AI Is Starting to Pay Off. Almost 50% of Companies Now Generate Value with It (press release, Applied AI Index 2026) | BCG | survey | https://www.bcg.com/press/30september2026-ai-starting-to-pay-off-companies-generate-value | 2026-09-30 | full (mirror) |
| BCG-AIX-2026-PUB | The Formula for Agentic AI Value (publication page and FAQ) | BCG | survey | https://www.bcg.com/publications/2026/the-formula-for-agentic-ai-value | 2026-09-30 (per press release; page shows no date) | full (mirror) |
| BCG-AGENTS-2025 | How agents are accelerating the next wave of AI value creation | BCG | firm | https://www.bcg.com/publications/2025/agents-accelerate-next-wave-of-ai-value-creation | 2025-12-15 | full (mirror) |
| MCKINSEY-SOAI-2025 | The state of AI in 2025: Agents, innovation, and transformation | McKinsey (QuantumBlack) | survey | https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf | 2025-11 | full (mirror) |
| MCKINSEY-SOAI-2026 | The state of AI in 2026: On the road to ROI | McKinsey (QuantumBlack) | survey | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 2026-08-25 | full (mirror) |
| DELOITTE-STATEAI-2026 | The State of AI in the Enterprise, 2026 (page and PDF) | Deloitte AI Institute | survey | https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf | 2026-01-20 | full |
| WHARTON-2026 | The Adaptive Advantage: Who's Winning With AI and How (2026 AI Adoption Report, Executive Summary and page) | Wharton Human-AI Research and GBK Collective | survey | https://knowledge.wharton.upenn.edu/wp-content/uploads/2026/10/Wharton-GBK-AI-Adoption-Report-2026.pdf | 2026-10-13 | full |
| WHARTON-2025 | Accountable Acceleration: Gen AI Fast-Tracks Into the Enterprise (2025 report page) | Wharton Human-AI Research and GBK Collective | survey | https://knowledge.wharton.upenn.edu/special-report/2025-ai-adoption-report/ | 2025-10-28 | full (page only) |
| GALLUP-2025 | AI Use at Work Rises | Gallup | survey | https://www.gallup.com/workplace/699689/ai-use-at-work-rises.aspx | 2025-12-14 | full (mirror) |
| MIT-NANDA-2025 | The GenAI Divide: State of AI in Business 2025 (preliminary) | MIT Project NANDA | academic | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf | 2025-07 | full |
| CENSUS-BTOS-2026 | Large Firms With at Least 20 Employees Biggest AI Users | US Census Bureau | survey | https://census.gov/library/stories/2026/05/ai-use-businesses.html | 2026-05-26 | full |
| NBER-BONNEY-2026 | The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks (NBER WP 35141) | Bonney, Breaux, Dinlersoz, Foster, Haltiwanger, Pande | academic | https://www.nber.org/papers/w35141 | 2026-04 | full (abstract) |
| STANFORD-AIINDEX-2026 | The 2026 AI Index Report (top takeaways page) | Stanford HAI | academic | https://hai.stanford.edu/ai-index/2026-ai-index-report | 2026 | full (summary page) |
| SADIQ-2021 | Artificial intelligence maturity model: a systematic literature review | Sadiq et al., PeerJ Computer Science | academic | https://peerj.com/articles/cs-661 | 2021-08-25 | full (mirror) |
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work (NBER WP 31161; published QJE 2025) | Brynjolfsson, Li, Raymond | academic | https://www.nber.org/papers/w31161 | 2023-04 | full (abstract) |
| HBS-JAGGED-2023 | Navigating the Jagged Technological Frontier (HBS WP 24-013) | Dell'Acqua et al. | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | 2023-09 | full (abstract) |
| METR-2025 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | METR | academic | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | 2025-07-10 | full |
| RAND-2024 | The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed | RAND | academic | https://www.rand.org/pubs/research_reports/RRA2680-1.html | 2024-08-13 | full (mirror) |
| GDS-COPILOT-2025 | Microsoft 365 Copilot Experiment: Cross-Government Findings Report | UK Government Digital Service | regulator | https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report/microsoft-365-copilot-experiment-cross-government-findings-report-html | 2025-06-02 | full |
| DBT-COPILOT-2025 | Evaluation of the M365 Copilot pilot in the Department for Business and Trade | UK Department for Business and Trade | regulator | https://assets.publishing.service.gov.uk/media/68adbe409e1cebdd2c96a19d/dbt-microsoft-365-copilot-evaluation.pdf | 2025-08-28 | full |
| DWP-COPILOT-2026 | An Evaluation of DWP's Microsoft 365 Copilot Trial | UK Department for Work and Pensions | regulator | https://www.gov.uk/government/publications/an-evaluation-of-dwps-microsoft-copilot-365-trial/an-evaluation-of-dwps-microsoft-365-copilot-trial | 2026-01-29 | full |
| IMDA-MGF-2026 | Model AI Governance Framework for Agentic AI, v1.5 | IMDA Singapore | regulator | https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf | 2026-05-20 (updated 2026-06-05) | full |
| NIST-AIRMF-2023 | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 2023-01 | full |
| EUAIA-EXPLORER-2024 | Regulation (EU) 2024/1689, Article 4 (AI literacy) and Article 26 (deployer obligations), explorer pages with tracked amendments | artificialintelligenceact.eu | regulator | https://artificialintelligenceact.eu/article/4/ ; https://artificialintelligenceact.eu/article/26/ | 2024-06-13 (regulation); explorer pages undated | full |
| OPENAI-GUIDE-2025 | A practical guide to building agents | OpenAI | vendor | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf | 2025-04 | full (skimmed: incremental approach, human intervention triggers) |
| MSFT-WTI-2024 | AI at Work Is Here. Now Comes the Hard Part (Work Trend Index) | Microsoft and LinkedIn | vendor | https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part | 2024-05-08 | full (mirror) |
| IBM-CEO-2025 | IBM Study: CEOs double down on AI while navigating enterprise hurdles | IBM Institute for Business Value | vendor | https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles | 2025-05-06 | full |
| GARTNER-AGENTIC-2025 | Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | 2025-06-25 | full (mirror) |
| GARTNER-MATURITY-2025 | Gartner Survey Finds 45% of Organizations With High AI Maturity Keep AI Projects Operational for at Least Three Years | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2025-06-30-gartner-survey-finds-forty-five-percent-of-organizations-with-high-artificial-intelligence-maturity-keep-artificial-intelligence-projects-operational-for-at-least-three-years | 2025-06-30 | search-only |
| KLARNA-2024 | Klarna AI assistant handles two-thirds of customer service chats in its first month | Klarna | firm | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ | 2024-02-27 | full |
| ENTREPRENEUR-KLARNA-2025 | Klarna CEO Reverses Course By Hiring More Humans, Not AI | Entrepreneur | press | https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 | 2025-05-09 | full |
| KP-AISCRIBE-2025 | AI-assisted notetaking gains steady support from Kaiser Permanente physicians | Kaiser Permanente Division of Research (summarizing NEJM Catalyst, doi 10.1056/CAT.25.0040) | firm | https://divisionofresearch.kaiserpermanente.org/ai-assisted-notetaking-gains-steady-support-from-kaiser-permanente-physicians/ | 2025-04-01 | full (summary; journal article not opened) |
| OPENAI-MORGANSTANLEY | Morgan Stanley uses AI evals to shape the future of financial services | OpenAI | vendor | https://openai.com/index/morgan-stanley/ | page carries no date (assets suggest 2024; accessed 2026-10-20) | full (mirror) |
| DBS-AR-2025 | DBS Annual Report 2025, CEO reflections | DBS Group | firm | https://www.dbs.com/annualreports/2025/ceo-reflections.html | 2026 (page last-modified 2026-07-30) | full |
| WALMART-Q4FY26-2026 | Walmart Q4 2026 earnings call transcript | MarketBeat (transcript of Walmart call) | press | https://www.marketbeat.com/earnings/reports/2026-2-19-walmart-inc-stock/ | 2026-02-19 | full |
| AUTOMATIONWORLD-SCHAEFFLER-2024 | Schaeffler Brings Siemens Industrial Copilot to its Shop Floor | Automation World | press | https://automationworld.com/factory/digital-transformation/news/55235167/schaeffler-brings-siemens-industrial-copilot-to-its-shop-floor | 2024-10-18 | full |
| SHOPIFY-LUTKE-2025 | Reflexive AI usage is now a baseline expectation at Shopify (internal memo posted by the CEO) | Tobi Lutke, Shopify | firm | https://x.com/tobi/status/1909251946235437514 | 2025-04-07 (date per CNBC) | full |
| CNBC-SHOPIFY-2025 | Shopify CEO says staffers need to prove jobs can't be done by AI before asking for more headcount | CNBC | press | https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html | 2025-04-07 | full (mirror) |
| CYBERDAILY-DELOITTE-2025 | Deloitte to refund government after using AI in $440k report | Cyber Daily | press | https://www.cyberdaily.au/government/12737-deloitte-to-refund-government-after-using-ai-in-440-000-report | 2025-10-08 | full |
| MOLLICK-2025 | Making AI Work: Leadership, Lab, and Crowd | Ethan Mollick, One Useful Thing | community | https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and | 2025-05-22 | full |

Archetype use-case ids cited in section 3 come from `references/archetypes/*/use-cases/*.yaml` and were not re-researched; the ids and grades are as in those files.
