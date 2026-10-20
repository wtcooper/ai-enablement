# Journey stages: planning the move to the next stage

Last reviewed 2026-10-20. Source keys in brackets are listed in §10. This file is for **planning the move to the next stage**: what
to invest in and emphasize, how to tell the move is done, and where scopes fail. **Placing a scope** (stage cards, boundary probes) and
**the five delegation gates** are in `../method/onboarding.md` §5; this file adds to them and does not repeat them. Exit criteria are
working heuristics: no study was found that follows the same organizations through the stages, and one review found only 7 of 15 AI
maturity models empirically validated [SADIQ-2021].

## Contents

1. [How to use this file](#1-how-to-use-this-file)
2. [Curious](#2-curious)
3. [Experimenting](#3-experimenting)
4. [Adopting](#4-adopting)
5. [Scaling](#5-scaling)
6. [AI-native](#6-ai-native)
7. [Failure points between stages](#7-failure-points-between-stages)
8. [How organizations are spread across stages](#8-how-organizations-are-spread-across-stages)
9. [How published maturity models compare](#9-how-published-maturity-models-compare)
10. [Sources](#10-sources)

## 1. How to use this file

- Read the section for the scope's current stage and plan against the next stage only. **Show or count** is evidence beyond the
  stage card; **exit criteria** add to the card's "ready when" column. Quote stage shares only with their population (§8).
- Individual gains run ahead of enterprise gains: in 2026, 80% of McKinsey's respondents say AI improved their own productivity, while
  37% report any EBIT contribution, unchanged on the year [MCKINSEY-SOAI-2026]. What separates movers is mostly organizational:
  redesigned workflows, a named owner, one approved platform, growth measures and broad upskilling (self-reported survey
  associations, not trials) [MCKINSEY-SOAI-2026; WHARTON-2026; BCG-GAP-2025].

## 2. Curious

- **Show or count.** Which tools people used last week, including their own: 78% of AI users bring their own tools (vendor survey of
  31,000 people) [MSFT-WTI-2024]; workers at over 90% of surveyed companies used personal tools while 40% of those companies had
  bought a subscription (interview-based, preliminary) [MIT-NANDA-2025]. Whether an inventory of AI systems exists, including AI inside
  vendor software (NIST's AI RMF asks for mechanisms to inventory AI systems) [NIST-AIRMF-2023]. Who in the scope does not know whether
  the organization uses AI (a count by role) [GALLUP-2025].
- **Typical blockers.** Colleagues without access knew little about capabilities, limits and security [DBT-COPILOT-2025]; people used
  the tool less when line managers were hesitant (anecdotal) [DBT-COPILOT-2025]; in BCG's laggards top management "may talk the
  talk" but sets no value ambition [BCG-GAP-2025].
- **Emphasize.** Acceptable-use policies that make safe use possible; literacy for the board and top team, and skills for AI already
  inside existing software [MITCISR-2024]. In the EU, Article 4 requires providers and deployers to support staff AI literacy; the text
  carries tracked amendments, so check it before quoting [EU-AIACT-ART4-2024].
- **Investments that move the scope on.** Sanctioned tools plus training, knowing access alone is not enough: Deloitte's respondents
  lifted worker access from under 40% to about 60% in a year, yet fewer than 60% of those with access use AI in a daily workflow
  [DELOITTE-STATEAI-2026]. BCG calls access and training insufficient by themselves but a strong sign of seriousness [BCG-GAP-2025].
- **Exit criteria (added to the card).** An inventory exists; the scope names its sanctioned tools and likely unsanctioned use.
- **Failure points.** A ban with no approved alternative, which pushes use into personal tools [MSFT-WTI-2024; MIT-NANDA-2025];
  leaders judging from their own seat [GALLUP-2025]; waiting: 31% of 3,412 webinar attendees polled by Gartner in January 2025 were
  "wait and see" or unsure on agentic AI investment [GARTNER-AGENTIC-2025].
- **Examples.** Organizations rarely publish being here. Kaiser Permanente's seven principles for responsible AI use (August 2024) are
  cited as a stage-1 step (policy only; B) [MITCISR-2024].

## 3. Experimenting

- **Show or count.** The pilot-to-production ratio for the last 12 months, not the pilot count. Published ratios are not comparable:
  5% of evaluated enterprise-grade tools, custom or vendor-sold (interview-based, preliminary) [MIT-NANDA-2025]; 25% of respondents moved 40%+ of experiments to
  production [DELOITTE-STATEAI-2026]; 54% of US managers say over half of last year's pilots did [WHARTON-2026]. The measure each pilot
  uses: "time saved" is most common; those measuring growth report strongly positive returns more often (35% against 13%) [WHARTON-2026].
- **Typical blockers.** Unwillingness to adopt new tools leads a 52-organization barrier ranking, followed by concerns about output
  quality (reported frequency) [MIT-NANDA-2025]. A pilot can run with a small team in isolation while production needs infrastructure, integration and
  support; one interviewee described "pilot fatigue" [DELOITTE-STATEAI-2026].
- **Emphasize.** Fewer workflows, end to end: BCG says some leaders "experiment too widely" and end with disconnected initiatives
  [BCG-GAP-2025]. Expert-graded test sets as part of the pilot: Morgan Stanley ran evaluations graded by advisors and prompt engineers
  before each use case [OPENAI-MORGANSTANLEY-2024].
- **Investments that move the scope on.** A named owner, a baseline and a designed human check (stage card). One approved platform and
  packaged shared skills: 50% of organizations standardized on a single approved platform report strongly positive returns, against
  9% of those "still experimenting" (correlation, self-reported) [WHARTON-2026].
- **Exit criteria (added to the card).** Every open pilot has a dated scale, stop or hold decision; expert-graded test cases exist for
  the first workflow; the measure is not hours saved alone.
- **Failure points.** Pilot purgatory (above). Time saved absorbed with no destination: three UK government evaluations of one
  assistant disagree, from 26 minutes a day estimated by users [GDS-COPILOT-2025] and 19 minutes against a comparison group
  [DWP-COPILOT-2026] to "did not find evidence" that time savings improved productivity [DBT-COPILOT-2025]. Mandated use without
  redesign: Shopify made AI use a baseline expectation in April 2025 and reports no outcome measure [SHOPIFY-LUTKE-2025].
- **Examples.** DBT (public sector, 1,000 licences; diaries, observed tasks and interviews including six control-group staff): 72%
  satisfied, no evidence of productivity improvement, hallucinations observed and inconsistent quality assurance; department
  evaluation from self-reports (B) [DBT-COPILOT-2025]. DWP (public sector, 3,500+
  licences): an estimated 19 minutes a day against a comparison group, from categorical self-reports (B) [DWP-COPILOT-2026].

## 4. Adopting

- **Show or count.** AI inside the system where work is recorded, with use counts: Kaiser Permanente's medical group reports 7,260
  physicians using an ambient scribe in 2,576,627 encounters [KP-AISCRIBE-2025]; Morgan Stanley reports over 98% of advisor teams using
  its internal assistant [OPENAI-MORGANSTANLEY-2024]. An **autonomy register**: Dayos (software) scored each IT ticket type on severity,
  reversibility and whether a person can realistically check it, which fixed each tier's autonomy (about 60% of tickets fully automated
  with biweekly audits, 30% with human approval, 10% not touched) [IMDA-MGF-2026]. The reviewers' change or rejection rate, which no
  cross-industry source publishes, so ask whether the scope measures it at all. Cost per workflow, including tokens and review time.
- **Typical blockers.** Production exposes edge cases pilots hide [DELOITTE-STATEAI-2026]; 51% of AI-using respondents report at
  least one negative consequence, nearly one-third from inaccuracy [MCKINSEY-SOAI-2025]; about 20% say costs, including tokens, constrain use
  [MCKINSEY-SOAI-2026].
- **Emphasize.** Designed human checks and measurement: high performers are more likely to have defined processes for when outputs
  need human validation [MCKINSEY-SOAI-2025]. For any bounded delegated workflow (behind the onboarding gates): graduate autonomy from
  shadow mode, where agents run "until they prove they align" with the organization's risk appetite [BCG-AGENTS-2025]; roll out by
  users, tools and systems, as GovTech Singapore did (internal staff, no external tool connections, low-risk systems first, central
  logging built alongside) [IMDA-MGF-2026]; give oversight to people with the "necessary competence, training and authority" where the
  EU AI Act applies to high-risk systems [EU-AIACT-ART26-2024].
- **Plan the route to monitored autonomy, not a permanent stop at approval-on-everything.** In Wharton's 2026 survey, departments are
  "transformed" least where every agent action is approved (16%) or sampled (18%), and most where AI advises (25%) or acts with
  monitoring (31%); 11% say nobody is accountable for agent errors (correlational, self-reported) [WHARTON-2026]. Companies with all
  six agent controls report three times the agentic value of those with one [BCG-AIX-2026-PUB]. Neither justifies skipping the gates.
- **Investments that move the scope on.** Reusable parts ("architecting for reuse", shared data via APIs) [MITCISR-2024]; a
  value-tracking framework with hypotheses, tests and scale plans, and a two-track governance review with a fast track including risk,
  privacy and security members (Guardian Life) [MITCISR-2025]; a central owner (58% strongly positive returns where a chief AI officer
  was newly designated, 8% with no such role; correlation) [WHARTON-2026].
- **Exit criteria (added to the card).** The review step has a measured intervention rate; the cost of each workflow is known; any
  delegated workflow has passed the five onboarding gates.
- **Failure points.** Spreading across too many workflows [BCG-GAP-2025]; review that becomes a rubber stamp; extending a pilot design
  into production without redesign [DELOITTE-STATEAI-2026].
- **Examples.** Permanente Medical Group (healthcare): the scribe was offered after a 10-week pilot in 2023; users spent less time
  in the record outside 7am-7pm and on notes per visit; self-reported study (A) [KP-AISCRIBE-2025]. Dayos (software): legacy tool
  retired in 45 days, licensing cost down USD 121,000 a year; company-reported, no error or override rate (B) [IMDA-MGF-2026]. Archetype entries: `assurance-controls-testing-04` (A), `security-operations-02` (A),
  `assurance-controls-testing-05` (A, a bounded delegated workflow).

## 5. Scaling

- **Show or count.** A shared platform with reusable components: Ally's platform (July 2023) integrates several commercial models with
  the bank's data [MITCISR-2024]. Value tracked as a portfolio: DBS reports about SGD 1 billion of economic value in 2025 from data
  analytics and AI/ML across 430+ use cases and 2,000+ models [DBS-AR-2025]. AI spend outside IT: 3.3% of revenue, with more than 80%
  outside the enterprise IT budget (BCG 2026 index) [BCG-AIX-2026]. Protected learning time: future-built firms expect to upskill more
  than 50% of staff against 20% at laggards [BCG-GAP-2025].
- **Typical blockers.** Legacy systems and fragmented data (Guardian Life upgraded mainframe systems and consolidated data first)
  [MITCISR-2025]; operating costs [MCKINSEY-SOAI-2026]; agent governance maturity, with 21% reporting a mature model
  [DELOITTE-STATEAI-2026].
- **Emphasize.** MIT CISR names four challenges for the move from pilots to scale: strategy, systems, synchronization (roles and
  teams) and stewardship (monitoring and compliance) [MITCISR-2025]. Stop as well as start: DBS allocates capital "only to initiatives
  with proven traction" [DBS-AR-2025].
- **Investments that move the scope on.** A single enterprise platform with common architecture and controls (more than two-thirds of
  future-built firms are committing to one) and data transformation (95% are undertaking one); strategic workforce planning (55% of
  future-built firms against 17% of laggards); value measured at P&L (95% of future-built firms use clear KPIs or track P&L value)
  [BCG-AIX-2026-PUB]. CISR says the greatest financial impact comes from moving from stage 2 to stage 3, where growth against the industry
  average turns positive (-6.8 points at stage 2, +4.7 at stage 3) [MITCISR-2025].
- **Exit criteria (added to the card).** AI value appears in a P&L line, not only in surveys; cost per unit of AI work is tracked; an
  agent control set exists (BCG lists oversight and rollback gates, security, audit and cost guardrails) [BCG-AIX-2026].
- **Failure points.** Autonomy scaled ahead of controls (§7); customer-facing scale without a quality check (Klarna); unreviewed AI
  content in deliverables (Deloitte Australia); workforce expectations drifting: 14% report AI contributed to a workforce decline in the
  past year, against 32% who expected one a year earlier [MCKINSEY-SOAI-2026].
- **Examples.** Ally Financial (financial services): about three minutes saved per call on more than four million calls in 2023;
  creative campaigns 34% faster; self-reported via CISR (A) [MITCISR-2024]. Italgas (utilities): project completion 40% faster and
  inspections down 80% with one tool; self-reported via CISR (A) [MITCISR-2025]. Walmart (retail): the CEO said shopping-assistant users
  have average order value "about 35% higher" than non-users, a user against non-user gap, not an effect of the assistant (B)
  [WALMART-Q4FY26-2026].
  Archetype entries: `security-operations-01` (A), `assurance-controls-testing-08` (A).

## 6. AI-native

- **Show or count.** Pricing, services or cost base changed by AI, with figures: Ping An reported that by end-2022 49% of product sales
  and 82% of service interactions were handled by AI representatives, and it offered AI banking to 30 other banks (via CISR)
  [MITCISR-2024]; Italgas sells its AI tool WorkOnSite as software through group company Bludigit, which generated EUR 3 million revenue at
  over 50% margin in 2024 (company figures, not tool-level) [MITCISR-2025]. Enterprise P&L attribution: McKinsey's high performers attribute 5%+ of EBIT to AI and were about 6% of
  respondents in 2025 and 2026 [MCKINSEY-SOAI-2026]. Archetype entries: `security-vulnerability-exposure-01` (A),
  `professional-services-scoping-pricing-19` (B).
- **Typical blockers.** Workforce redesign; governance of increasingly autonomous systems; cost constraints, which high performers
  report on coding agents about three times as often [MCKINSEY-SOAI-2026].
- **Emphasize.** Test claims. Top tiers are small by every value-based definition, and "AI-first" statements are not evidence: Shopify's
  memo states expectations, not results [SHOPIFY-LUTKE-2025]. Ask for the metric that changed and who outside the team verified it.
- **Investments.** In-house AI infrastructure that integrates purchased models with enterprise APIs, data and processes; continuous
  experimentation (DBS's CEO set a KPI of 1,000 experiments a year, cited by CISR) [MITCISR-2024].
- **Exit criteria.** None: re-diagnose at each review. BCG moved from a 41-capability score (2025) to an "Applied AI Index" (2026), and
  the pages read do not say the series is like-for-like [BCG-GAP-2025; BCG-AIX-2026].
- **Failure points.** Over-rotation to cost (Klarna, §7); claims that outrun evidence; margins passed to clients while pricing stays
  time-based (see the archetypes' pricing use cases).

## 7. Failure points between stages

No cross-industry source read publishes override, escalation or parallel-run rates for organizations moving between stages.

| Boundary | What goes wrong | Evidence |
|---|---|---|
| Curious to Experimenting | Ban without an approved alternative; use goes to personal tools | 78% bring their own tools [MSFT-WTI-2024] |
| Experimenting to Adopting | Pilots never reach production; time saved has no destination | 5%, 25% and 54% production ratios on different definitions [MIT-NANDA-2025; DELOITTE-STATEAI-2026; WHARTON-2026]; department evaluations disagree [GDS-COPILOT-2025; DBT-COPILOT-2025] |
| Experimenting to Adopting | The problem is misunderstood or miscommunicated, the first of RAND's five root causes of failed AI projects | 65 practitioner interviews; the often-quoted "80%" failure figure is not RAND's own measure [RAND-2024] |
| Adopting to Scaling | Too many workflows at once; pilot designs carried into production | [BCG-GAP-2025; DELOITTE-STATEAI-2026] |
| Adopting to Scaling | Autonomy scaled ahead of controls | 42% expect to give agents genuine autonomy by 2030, 5% have the full controls [BCG-AIX-2026]; 74% plan agents within two years, 21% have mature governance [DELOITTE-STATEAI-2026]; Gartner predicts over 40% of agentic projects will be cancelled by end-2027 (analyst prediction) [GARTNER-AGENTIC-2025] |
| Scaling to AI-native | Customer-facing scale without a quality check | Klarna's 2024 assistant handled two-thirds of chats in its first month [KLARNA-2024]; in May 2025 its CEO said the approach was cheaper but "lower quality" and the firm resumed hiring people [ENTREPRENEUR-KLARNA-2025] |
| Scaling to AI-native | Unreviewed AI content in deliverables | Deloitte Australia agreed to refund part of a A$440,000 government report containing fabricated references; the firm said corrections did not change findings [CYBERDAILY-DELOITTE-2025] |
| Any | Initiatives that do not pay back | 25% of AI initiatives delivered expected ROI and 16% scaled enterprise-wide (CEO survey, vendor-published) [IBM-CEO-2025] |

## 8. How organizations are spread across stages

Stage shares depend almost entirely on who was asked. Always give the population.

| Source and date | Population | Who measured | Stage-like split |
|---|---|---|---|
| McKinsey, fielded 2026-05/06 [MCKINSEY-SOAI-2026] | 1,719 respondents, 97 countries, GDP-weighted | self-reported | 44% scaling across the enterprise (38% a year earlier); 54% at $1bn+ revenue firms; high performers about 6% |
| McKinsey, fielded 2025-06/07 [MCKINSEY-SOAI-2025] | 1,993 respondents | self-reported | 88% use AI regularly in at least one function |
| BCG, 2026 [BCG-AIX-2026; BCG-AIX-2026-PUB] | about 1,300 CxOs and senior leaders, 20+ sectors | self-reported | stagnating 4.5%, emerging 47%, scaling 41%, future-built 7.5% |
| BCG, 2025 [BCG-GAP-2025] | 1,250 senior executives, 68 countries | self-reported | stagnating 14%, emerging 46%, scaling 35%, future-built 5% (2024: 25 / 49 / 22 / 4) |
| MIT CISR, 2022 and 2025 [MITCISR-2025] | N=721 (2022), N=152 (2025); different samples | self-reported | stages 1-4: 28 / 34 / 31 / 7% (2022); 13 / 23 / 46 / 18% (2025) |
| Deloitte, fielded 2025-08/09 [DELOITTE-STATEAI-2026] | 3,235 leaders, 24 countries | self-reported | 37% surface-level use, 30% redesigning key processes, 34% deeply transforming |
| Wharton, fielded 2026-07 [WHARTON-2026] | about 1,400 US employees at firms with 1,000+ staff | self-reported | 28% "fully embedded" in core workflows; 80% positive return, 28% strongly positive |
| US Census Bureau, Dec 2025 to May 2026 [CENSUS-BTOS-2026; NBER-BONNEY-2026] | nationally representative US firms | independent (statistical agency) | 17-20% of all firms use AI in a business function; 37% of firms with 250+ staff; retail about 14%; 57% of adopters use it in three or fewer functions |
| Gallup, fielded 2025-08 [GALLUP-2025] | 23,068 US employees | independent poll | 37% say their organization has implemented AI, 40% say not, 23% do not know |

The gap between about 20% (Census) and 88% (McKinsey) is a population and definition effect, not a contradiction: Census asks all
firms about use in a business function, while consultancy samples are senior leaders, mostly of large organizations
[CENSUS-BTOS-2026; MCKINSEY-SOAI-2025]. For small firms the Census figure is the better guide.

## 9. How published maturity models compare

The mapping to the advisor's five stages is a working alignment that no source validates.

| Advisor stage | MIT CISR (4 stages) [MITCISR-2024] | BCG (4 tiers) [BCG-GAP-2025] | McKinsey phases [MCKINSEY-SOAI-2025] | Wharton waves [WHARTON-2025; WHARTON-2026] |
|---|---|---|---|---|
| Curious | 1 Experiment and Prepare | Stagnating | Not using or experimenting | 1 Exploration (2023) |
| Experimenting | 2 Build Pilots and Capabilities | Emerging | Piloting | 2 Experimentation (2024) |
| Adopting | Late 2 or early 3 (not named) | Early scaling (not a named tier) | Scaling begins | — |
| Scaling | 3 Develop AI Ways of Working | Scaling | Scaling and fully scaled | 3 Accountable Acceleration |
| AI-native | 4 Become AI Future Ready | Future-built | High performers (5%+ of EBIT) | 4 Success Through Transformation |

**Where they agree:** a break between pilots and scaled, owned, measured use; a small top tier; value tracked at enterprise level only
in the upper tiers; workflow redesign, leadership ownership, governance and reuse separating the tiers. **Where they differ:** the
number of stages (four here; five is the most frequent count among 15 models in one literature review) [SADIQ-2021]; how they treat agents (BCG calls them "the
next step"; Wharton finds the fullest agentic use alongside the most transformation) [BCG-GAP-2025; WHARTON-2026]; and thresholds, each
with its own scoring [MITCISR-2024; BCG-GAP-2025]. No standard terminology exists [SADIQ-2021]. The Adopting stage has no separate
label in the published models; it is where the advisor puts the first owned, measured workflows.

## 10. Sources

- **BCG-AGENTS-2025**: BCG, *How agents are accelerating the next wave of AI value creation* (consultancy, 2025-12-15). https://www.bcg.com/publications/2025/agents-accelerate-next-wave-of-ai-value-creation
- **BCG-AIX-2026**: BCG, *AI Is Starting to Pay Off* (press release, Applied AI Index 2026, n=1,330, 2026-09-30). https://www.bcg.com/press/30september2026-ai-starting-to-pay-off-companies-generate-value
- **BCG-AIX-2026-PUB**: BCG, *The Formula for Agentic AI Value* (consultancy survey publication, 2026-09-30). https://www.bcg.com/publications/2026/the-formula-for-agentic-ai-value
- **BCG-GAP-2025**: BCG, *The Widening AI Value Gap: Build for the Future 2025* (consultancy survey, n=1,250, 2025-09). https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf
- **CENSUS-BTOS-2026**: US Census Bureau, *Large Firms With at Least 20 Employees Biggest AI Users* (statistical agency, 2026-05-26). https://census.gov/library/stories/2026/05/ai-use-businesses.html
- **CYBERDAILY-DELOITTE-2025**: Cyber Daily, *Deloitte to refund government after using AI in $440k report* (press, 2025-10-08). https://www.cyberdaily.au/government/12737-deloitte-to-refund-government-after-using-ai-in-440-000-report
- **DBS-AR-2025**: DBS Group, *Annual Report 2025, CEO reflections* (firm, 2026). https://www.dbs.com/annualreports/2025/ceo-reflections.html
- **DBT-COPILOT-2025**: UK Department for Business and Trade, *Evaluation of the M365 Copilot pilot* (government evaluation, 2025-08-28). https://assets.publishing.service.gov.uk/media/68adbe409e1cebdd2c96a19d/dbt-microsoft-365-copilot-evaluation.pdf
- **DELOITTE-STATEAI-2026**: Deloitte AI Institute, *The State of AI in the Enterprise, 2026* (consultancy survey, n=3,235, 2026-01-20). https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf
- **DWP-COPILOT-2026**: UK Department for Work and Pensions, *An Evaluation of DWP's Microsoft 365 Copilot Trial* (government evaluation, 2026-01-29). https://www.gov.uk/government/publications/an-evaluation-of-dwps-microsoft-copilot-365-trial/an-evaluation-of-dwps-microsoft-365-copilot-trial
- **ENTREPRENEUR-KLARNA-2025**: Entrepreneur, *Klarna CEO Reverses Course By Hiring More Humans, Not AI* (press, 2025-05-09). https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
- **EU-AIACT-ART26-2024**: Regulation (EU) 2024/1689, *Article 26: Obligations of deployers of high-risk AI systems* (regulation text with tracked amendments, 2024-06-13). https://artificialintelligenceact.eu/article/26/
- **EU-AIACT-ART4-2024**: Regulation (EU) 2024/1689, *Article 4: AI literacy* (regulation text with tracked amendments, 2024-06-13). https://artificialintelligenceact.eu/article/4/
- **GALLUP-2025**: Gallup, *AI Use at Work Rises* (poll, n=23,068, 2025-12-14). https://www.gallup.com/workplace/699689/ai-use-at-work-rises.aspx
- **GARTNER-AGENTIC-2025**: Gartner, *Over 40% of Agentic AI Projects Will Be Canceled by End of 2027* (analyst prediction and poll, 2025-06-25). https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- **GDS-COPILOT-2025**: UK Government Digital Service, *Microsoft 365 Copilot Experiment: Cross-Government Findings Report* (government evaluation, 2025-06-02). https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report/microsoft-365-copilot-experiment-cross-government-findings-report-html
- **IBM-CEO-2025**: IBM Institute for Business Value, *CEOs double down on AI while navigating enterprise hurdles* (vendor survey, n=2,000, 2025-05-06). https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles
- **IMDA-MGF-2026**: IMDA Singapore, *Model AI Governance Framework for Agentic AI* v1.5 (regulator guidance with case studies, 2026-05-20). https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
- **KLARNA-2024**: Klarna, *Klarna AI assistant handles two-thirds of customer service chats in its first month* (firm release, 2024-02-27). https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
- **KP-AISCRIBE-2025**: Kaiser Permanente Division of Research, *AI-assisted notetaking gains steady support from Kaiser Permanente physicians* (firm, 2025-04-01). https://divisionofresearch.kaiserpermanente.org/ai-assisted-notetaking-gains-steady-support-from-kaiser-permanente-physicians/
- **MCKINSEY-SOAI-2025**: McKinsey, *The state of AI in 2025: Agents, innovation, and transformation* (consultancy survey, n=1,993, 2025-11). https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf
- **MCKINSEY-SOAI-2026**: McKinsey, *The state of AI in 2026: On the road to ROI* (consultancy survey, n=1,719, 2026-08-25). https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- **MIT-NANDA-2025**: MIT Project NANDA, *The GenAI Divide: State of AI in Business 2025* (preliminary, interview-based, 2025-07). https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- **MITCISR-2024**: Weill, Woerner, Sebastian, MIT CISR, *Building Enterprise AI Maturity* (academic, 2024-12-19). https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian
- **MITCISR-2025**: Woerner, Sebastian, Weill, Kaganer, MIT CISR, *Grow Enterprise AI Maturity for Bottom-Line Impact* (academic, 2025-08-21). https://cisr.mit.edu/publication/2025_0801_EnterpriseAIMaturityUpdate_WoernerSebastianWeillKaganer
- **MSFT-WTI-2024**: Microsoft and LinkedIn, *AI at Work Is Here. Now Comes the Hard Part* (vendor survey, 2024-05-08). https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part
- **NBER-BONNEY-2026**: Bonney et al., *The Microstructure of AI Diffusion*, NBER Working Paper 35141 (academic, 2026-04). https://www.nber.org/papers/w35141
- **NIST-AIRMF-2023**: NIST, *AI Risk Management Framework 1.0* (standard-setter, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **OPENAI-MORGANSTANLEY-2024**: OpenAI, *Morgan Stanley uses AI evals to shape the future of financial services* (vendor customer story; page shows no date, 2024 inferred from its assets). https://openai.com/index/morgan-stanley/
- **RAND-2024**: RAND, *The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed* (research report, 2024-08-13). https://www.rand.org/pubs/research_reports/RRA2680-1.html
- **SADIQ-2021**: Sadiq et al., *Artificial intelligence maturity model: a systematic literature review*, PeerJ Computer Science (academic, 2021-08-25). https://peerj.com/articles/cs-661
- **SHOPIFY-LUTKE-2025**: Tobi Lutke, *Reflexive AI usage is now a baseline expectation at Shopify* (CEO memo, 2025-04-07). https://x.com/tobi/status/1909251946235437514
- **WALMART-Q4FY26-2026**: MarketBeat, *Walmart Q4 2026 earnings call transcript* (press, 2026-02-19). https://www.marketbeat.com/earnings/reports/2026-2-19-walmart-inc-stock/
- **WHARTON-2025**: Wharton Human-AI Research and GBK Collective, *Accountable Acceleration: Gen AI Fast-Tracks Into the Enterprise* (survey, 2025-10-28). https://knowledge.wharton.upenn.edu/special-report/2025-ai-adoption-report/
- **WHARTON-2026**: Wharton Human-AI Research and GBK Collective, *The Adaptive Advantage: 2026 AI Adoption Report* (survey, 2026-10-13). https://knowledge.wharton.upenn.edu/wp-content/uploads/2026/10/Wharton-GBK-AI-Adoption-Report-2026.pdf
