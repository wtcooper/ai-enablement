# Method topic: AI maturity and adoption-stage models

Stream M (method). Topic `ai-maturity-models`. Researched 2026-10-16.
Feeds the advisor's phases: **onboarding, frame, plan-and-control**.
Purpose: validate and sharpen the five journey stages (Curious, Experimenting, Adopting, Scaling, AI-native; spec §3.2, §6.7) with observable markers, diagnostic questions, blockers and emphasis.

Conventions used below:

- `[S]` = taken from a cited source (ref plus locator).
- `[P]` = proposed by the analyst as a synthesis. Not stated by any source. Needs testing before it ships.
- Refs follow `PUBLISHER-SHORT-YYYY`. Full list in section 9.
- "Illustrative" marks a constructed example that uses sourced facts. It is not evidence.

---

## 1. Summary

- **The five-stage ladder is defensible, and the stage boundaries are not equally firm.** A systematic review of 13 AI maturity studies found five-level models and maturity grids to be the prevailing designs, with no standard terminology and mostly descriptive, bottom-up construction (SADIQ-2021, abstract and Table 5 discussion). Practitioner models use 4 to 6 levels. Gartner's five levels (Awareness, Active, Operational, Systemic, Transformational) are the closest match to the advisor's names, but I could only reach a secondary description of them (GARTNER-MM).
- **The one boundary every model agrees on is Experimenting to Adopting.** It is the move from individual or pilot use to shared, owned, measured workflows in production. Sage (stage 2 to 3), Litify (Expand to Integrate), MIT CISR (stage 2 to 3), BCG (emerging to scaling), Lichtenthaler (level 2 to 3) and the MIT NANDA "pilot-to-production chasm" all put their sharpest break here. The advisor should spend the most diagnostic effort on this boundary.
- **Adopting versus Scaling is the blurriest boundary.** BCG's "scaling" tier covers both. MIT CISR stage 3 ("AI ways of working") adds reusable platforms, dashboards and a test-and-learn culture. A usable discriminator is *reuse and portfolio management*: a second workflow built from shared components, a named central owner, and value tracked across workflows (MITCISR-2024; BCG-2025 pp.11-14) `[P]` for the exact wording.
- **"AI-native" is rare and defined differently in each model.** Shares at the top tier: 5% (BCG-2025 Exh.1), 7% (MITCISR-2024 Fig.1), 8% "front-runners" (ACCENTURE-2025). In professional services the clearest marker is a change to the commercial model (pricing and services), not technology (SAGE-2026 stage 4). Treat a user's self-placement at AI-native with scepticism.
- **Self-placement runs high, so the advisor should place by evidence.** Deloitte finds more leaders calling strategy highly prepared while feeling less prepared on infrastructure, data, risk and talent (DELOITTE-2026 finding 7). Gallup finds 7% of leaders versus 26% of individual contributors saying they do not know whether their organization has implemented AI (GALLUP-2025). Individuals are often ahead of their organizations: 78% of AI users bring their own tools (MSFT-WTI-2024 §1), and workers at over 90% of surveyed firms use LLMs regularly while 40% of firms bought a subscription (MITNANDA-2025 §3.3).
- **Blockers shift from "should we and how safely" to "can we integrate and measure" to "can we run and fund it as a portfolio" to "can we change what we sell".** Early blockers are policy, literacy and confidentiality. Middle blockers are data, integration and measurement. Later blockers are operating model, talent, agent governance and pricing.
- **For professional services, efficiency without a pricing change is a stall, not progress.** Sage's worked arithmetic (8 hours cut to 3, same fixed fee or hourly billing) shows how "assisted productivity" can compress margin. Only 7% of surveyed UK firms call AI's impact transformational although 71% use external AI tools (SAGE-2026).
- **Evidence for "maturity predicts performance" is correlational and mostly vendor- or consultancy-published.** MIT CISR (2022 survey, analytical AI) is the best academic case. BCG, Accenture, Gartner and Cisco are consultancy or vendor surveys. No source tracks the same organizations through the stages.

---

## 2. Core concepts in plain language

### 2.1 Concepts the advisor must understand

1. **A maturity model is a staircase of descriptions, not a measured law.** Reviewers find most AI maturity models descriptive, built bottom-up, and designed for a specific domain, with different names for the same elements (SADIQ-2021, review findings). For knowledge work this means a stage is a *conversation structure*. It organizes questions and next steps. The advisor should never present a stage as a score or a verdict. For AI specifically: stage names in the advisor will not match any published model one-to-one, so the advisor should explain stages by their observable markers.

2. **The core transition is from individual use to organizational capability.** Individual use is now mainstream: 75% of knowledge workers in a 31-country survey (MSFT-WTI-2024 §1), 45% of US employees at least a few times a year and 10% daily (GALLUP-2025), and about 80% of law firms using or exploring generative AI (ILTA-2025 via Law360). Organizational capability is not: most firm-level adoption is in pilots (ILTA-2025), and few custom tools reach sustained production impact (MITNANDA-2025 §3.2). For knowledge work, the unit that moves is the *workflow*, not the tool. For AI, the question that separates the stages is "who owns this workflow, and what changed in the business?"

3. **Stage is multi-dimensional and scope-specific, and the weakest dimension binds.** BCG scores maturity across 41 dimensions (BCG-2025 Exh.1 note 1). Cisco uses six pillars (strategy, infrastructure, data, governance, talent, culture) (CISCO-2025 via RCR). Litify rates four variables (tools and investment, firm readiness, task scope, overall impact) (LITIFY-2026). A person can be a power user inside an immature team, and a team can be ahead of its firm. The advisor should place each scope separately (individual practice, team workflow, organizational enablers) and advise to the binding constraint. `[P]` for the scope split.

4. **Efficiency is not reinvention, and time saved is not value captured.** Productivity and efficiency top the benefits (66% of organizations) while revenue growth is mostly an aspiration (20% achieving it versus 74% hoping) (DELOITTE-2026 section "What does AI do for business?"). Deloitte splits organizations into 37% surface-level, 30% redesigning key processes and 34% deeply transforming. In fee-for-time professions, saved hours create a "capacity gap" unless pricing and services change (SAGE-2026). This is what separates Adopting and Scaling from AI-native in the advisor's ladder.

5. **People, trust and governance are stage enablers, not afterthoughts.** In Gartner's survey, 57% of high-maturity organizations have business units that trust and are ready to use new AI solutions, versus 14% of low-maturity ones (GARTNER-2025). Gallup associates broader adoption with manager support and strategic integration of AI in the role (GALLUP-2025). Wharton finds training investment softening (-8 points) while nearly half report skill gaps (WHARTON-2025 Key Takeaway on human capital). For knowledge work, adoption stalls on trust and verification habits before it stalls on technology.

6. **Stage claims age fast.** Distributions moved noticeably within a year in BCG's data (laggards 74% in 2024 to 60% in 2025; Exh.1), and KPMG reports agent deployment rising from 11% to 42% in two quarters (KPMG-2025). The older models (Gartner-era ML maturity, Lichtenthaler 2020, MIT SMR-BCG 2019) predate generative and agentic AI. Use them for structure, not for current benchmarks. The advisor should re-diagnose at each review.

7. **Agents are a later rung, not an entry point.** BCG says agentic AI is the next step in implementation, not the starting point, and lists prerequisites: strong data foundations, scaled AI capabilities and clear governance (BCG-2025 p.9). Deloitte finds only one in five companies has a mature model for governing autonomous agents (DELOITTE-2026 finding 5). This creates a tension with the spec's "Adopting: first delegated (agentic) workflows" (see 2.3).

8. **Vendor maturity models point at the vendor's product.** Litify's advice to "shift from generic to legal-specific" tools, Cisco's weighting toward infrastructure and Fieldguide's autonomy levels each align with what the publisher sells (LITIFY-2026; CISCO-2025; FIELDGUIDE-2025). That does not make them wrong. It means the advisor should take the *marker*, not the *prescription*.

### 2.2 How published models line up with the five stages

The mapping is approximate (`[P]` judgement); the stage names and counts are from the sources.

| Model (ref) | Stages as published | Rough alignment to Curious / Experimenting / Adopting / Scaling / AI-native |
|---|---|---|
| MIT CISR 2024 (MITCISR-2024) | 1 Experiment and Prepare (28%); 2 Build Pilots and Capabilities (34%); 3 Develop AI Ways of Working (31%); 4 Become AI Future Ready (7%) | S1 ≈ Curious + early Experimenting; S2 ≈ Experimenting to Adopting; S3 ≈ Scaling; S4 ≈ AI-native. Adopting is not a separate stage |
| BCG 2025 (BCG-2025) | Stagnating 14%; Emerging 46%; Scaling 35%; Future-built 5% | Stagnating ≈ Curious; Emerging ≈ Experimenting; "Scaling" ≈ Adopting + Scaling; Future-built ≈ AI-native |
| Gartner (GARTNER-MM, secondary) | Awareness; Active; Operational; Systemic; Transformational | Closest to the advisor's five. Description is ML-era, secondary only |
| Lichtenthaler 2020 (LICHTENTHALER-2020) | 0 Isolated Ignorance; 1 Initial Intent; 2 Independent Initiative; 3 Interactive Implementation; 4 Interdependent Innovation; 5 Integrated Intelligence | L0 ≈ pre-Curious; L1 ≈ Curious/Experimenting; L2 ≈ Experimenting; L3 ≈ Adopting/Scaling; L4 ≈ AI-native; L5 not reached by "hardly any" firm |
| Accenture 2025 (ACCENTURE-2025) | Four company groups; 15% "reinvention-ready"; 8% "front-runners" | Only the top two groups are named in the page I read |
| Cisco 2025 (CISCO-2025) | Pacesetters 13%, then Chasers, Followers, Laggards (per search summary) | Readiness tiers rather than stages |
| Deloitte 2026 (DELOITTE-2026) | Depth of use: surface-level 37%; redesigning key processes 30%; deep transformation 34% | Depth axis, not a ladder. Useful for Adopting versus AI-native |
| Wharton 2025 (WHARTON-2025) | Exploration (2023), Experimentation (2024), Accountable Acceleration (2025) | Cohort-level eras of one panel, not firm stages. Markers are useful |
| Litify 2026 (LITIFY-2026) | Explore; Expand; Integrate; Transform | Curious/Experimenting; Experimenting; Adopting; Scaling/AI-native |
| IR Global / Clio-originated 2025 (IRGLOBAL-2025) | Skeptics; Explorers; Experimenters; Integrators; Innovators (top 5-10% of legal adopters) | Pre-Curious; Curious; Experimenting; Adopting/Scaling; AI-native |
| Sage 2026, accounting (SAGE-2026) | 1 Awareness and experimentation; 2 Assisted productivity; 3 Workflow integration; 4 Commercial transformation | Curious+Experimenting; late Experimenting; Adopting; Scaling/AI-native (commercial) |
| "National" 2026, legal (CBA-2026) | Experimentation; Structured Adoption; Workflow Integration; Organizational AI Maturity | Experimenting; Experimenting-to-Adopting; Adopting; Scaling |
| UpLevel Ops 2023, legal (UPLEVEL-2023) | Ad hoc; Defined; Tactical; Strategic | Names only; stage text not in the page I read |
| Fieldguide 2025, audit (FIELDGUIDE-2025) | Six levels of AI autonomy, "fully manual" to "fully Agentic AI-orchestrated engagements" | Autonomy axis; level names not given in the blog post |
| Individuals: MS Work Trend Index 2024 (MSFT-WTI-2024) | Skeptics; Novices; Explorers; Power users (by frequency, familiarity, time saved) | Individual-level only |
| Foundations: CMMI (CMMI-WIKI); diffusion of innovations (ROGERS-WIKI) | Initial, Repeatable, Defined, Managed, Optimizing; awareness, interest, evaluation, trial, adoption | Generic process-maturity and adoption-process logic |

Observation `[P]`: the models that name a separate "awareness" or "pre-use" stage (Gartner, Lichtenthaler L0, IR Global "Skeptics" and "Explorers") support keeping **Curious** distinct. Models built for professional services fold awareness and first use into one stage (Sage stage 1, CBA "Experimentation"). The advisor's Curious stage should therefore be defined by *absence of sustained, shared use*, not by absence of any use.

### 2.3 Validation notes on the spec's stages (concise)

- **Keep the five stages.** Five levels are the most common design (SADIQ-2021), and the names map cleanly onto Gartner's and Lichtenthaler's structures.
- **Define Curious by evidence, not attitude.** Informal individual use, often unsanctioned, is usually present (MITNANDA-2025 §3.3; TR-2026 key findings: 34% of professionals use AI their organization has not approved; MSFT-WTI-2024 §1). Add an "unsanctioned use" probe at Curious.
- **Add "baseline and metric defined" to Experimenting.** MIT CISR makes defining metrics and tracking pilot value a stage 2 task; Gartner links metrics to project longevity (63% of high-maturity leaders run financial and ROI analysis, GARTNER-2025). Pilots without baselines are the typical stall.
- **Tension to resolve:** the spec lists "first delegated (agentic) workflows" under Adopting (spec §3.2). BCG puts agents after data foundations, scaled capabilities and governance (BCG-2025 p.9). Suggest: at Adopting, delegation only for bounded, low-risk workflows with explicit human checkpoints and a control plan. Broader delegation sits in Scaling. `[P]`
- **Make "pricing and service model" a named Scaling-to-AI-native topic for fee-based professions** (SAGE-2026 stage 4; the same logic applies to hourly legal work per SPICY-2026, low reliability).
- **Allow stage per scope.** An individual, a team and an organization can sit at different stages. Place each, then plan against the weakest. `[P]`

### 2.4 Proposed stage cards

Each card has observable markers (what the advisor can ask to see), scope variants, typical blockers, what to emphasize, and signals of readiness for the next stage. Diagnostic questions are in section 4. Professional-services flavor lines are `[P]`.

#### Curious

- **Observable markers**
  - AI use is informal and individual, on free or consumer tools, for emails, summaries and drafts. Firm sees no change in business outcomes. [S] LITIFY-2026 "Explore"; SAGE-2026 stage 1.
  - Leaders follow webinars and reports but are unsure how AI applies to their own work. [S] IRGLOBAL-2025 "Explorers".
  - Ideas rather than strategy. [S] GARTNER-MM "Awareness" (secondary). A named owner or budget line is absent `[P]`.
  - No policy, or only a prohibition. Concern about confidentiality, ethics and cost. [S] IRGLOBAL-2025 (Skeptics, Explorers).
  - Unsanctioned individual use is probably already happening. [S] MITNANDA-2025 §3.3; TR-2026.
- **Scope variants** `[P]`: *individual* uses chat a few times a month and cannot name a task where it helped (frequency bands in MSFT-WTI-2024 §3); *team* has no shared prompts or norms; *unit/org* has no AI policy, no owner and no budget line.
- **Typical blockers.** Unclear fit to specific work (IRGLOBAL-2025); confidentiality and accuracy worries (over 80% of ILTA respondents list them among the biggest, ILTA-2025 via Law360); fear of poor outcomes leading leaders to delegate AI downward (BCG-2025 p.6); no policy or training (LITIFY-2026: fewer than 50% of legal professionals report sufficient training or clear policies).
- **Emphasize.** Inspiration tour with archetype examples; a minimal safe-use policy and a short checklist (LAWSOC-GENAI checklist; ICAEW-GOV-2026 Q1-Q2); AI literacy for leaders (MITCISR-2024 stage 1 funds literacy for board and top team); two or three quick wins on low-risk, non-sensitive work (IRGLOBAL-2025 "start small"); make wins visible to peers (ROGERS-WIKI: observability and trialability drive diffusion). Keep mapping light (spec §3.2).
- **Ready for Experimenting when** `[P]`: at least a few named people use AI weekly on real work; an acceptable-use rule exists; one quick win has been shown to peers.
- **Professional-services flavor** `[P]`: partners or managers tried chat tools for emails and summaries; no engagement or matter workflow touches AI.

#### Experimenting

- **Observable markers**
  - Several individuals or teams use AI on real work, but usage is uncoordinated and tools are mixed. [S] IRGLOBAL-2025 "Experimenters"; CBA-2026 "Experimentation".
  - Pilots exist; many are discontinued without rollout because payoff is uncertain. [S] LICHTENTHALER-2020 level 1, p.42.
  - Gains are felt by individuals; the organization sees no measurable change in outcomes. [S] LITIFY-2026 "Explore"/"Expand".
  - Enterprise tools are licensed on request or to a subset: two-thirds of ILTA firms with Microsoft 365 Copilot issue it on request and 8% deploy to all employees. [S] ILTA-2025 via Law360.
  - Time saved is real but unallocated: "assisted productivity". [S] SAGE-2026 stage 2.
- **Scope variants** `[P]`: *individual* uses AI several times a week and saves time but works alone; *team* has pilot users and no shared workflow; *unit/org* has multiple unconnected pilots with no portfolio view.
- **Typical blockers.** Pilots that do not convert (MITNANDA-2025 §3.2: 5% of custom enterprise tools reach production in interview-based, directional data); tools that do not retain context or fit the workflow (MITNANDA-2025 §4); extra silos and limited staff adoption (IRGLOBAL-2025 "Experimenters"); skills and training (DELOITTE-2026 finding 3); freed capacity absorbed invisibly (SAGE-2026).
- **Emphasize.** Move from individual use to shared team workflows; find repeatable high-volume steps (spec §3.2); fix a baseline and a success metric before each pilot `[P]` with MITCISR-2024 stage 2 and GARTNER-2025 support; use power users as champions (MSFT-WTI-2024 §3: frequent experimentation is the top predictor of becoming a power user); ask what happens to time saved (SAGE-2026).
- **Ready for Adopting when** `[P]`: one workflow has a named owner, a baseline, a human checkpoint design and an approved tool.
- **Professional-services flavor** `[P]`: associates use AI for drafting and research with ad hoc review; engagement or matter methodology has not changed.

#### Adopting

- **Observable markers**
  - ML adopted into day-to-day functions, with a team and infrastructure to maintain it (BMC's description of Gartner level 3 "Operational"; ML-era wording). [S] GARTNER-MM. Whether a workflow has a named owner and a measure is `[P]`, drawn from MITCISR-2024 stage 2.
  - AI is connected to client data and the systems where work happens, and standardized across the team. [S] SAGE-2026 stage 3; CBA-2026 "Workflow Integration".
  - Tools are tailored to workflows; policy, training and enablement programs exist; organizational metrics improve but financial ROI is not yet proven. [S] LITIFY-2026 "Integrate".
  - Metrics defined; processes being simplified; data silos being consolidated and served via APIs. [S] MITCISR-2024 stage 2.
  - Pilot-to-production rate is rising (BCG: 62% of future-built firms' initiatives deployed versus 12% for laggards, a benchmark for the Scaling end). [S] BCG-2025 p.14.
- **Scope variants** `[P]`: *individual* redesigns own routine around AI (power users are 66% more likely to redesign business processes, MSFT-WTI-2024 §3); *team* has shared skills and a documented workflow with checkpoints; *unit/org* has a policy, an approved-tool list and a small set of owned workflows.
- **Typical blockers.** Data availability and quality (34% of low-maturity and 29% of high-maturity leaders, GARTNER-2025); finding the right use case (37% of low-maturity leaders, GARTNER-2025); integration with practice or engagement systems (IRGLOBAL-2025); measuring ROI (IRGLOBAL-2025 "Integrators"; 78% of KPMG respondents say traditional business metrics are becoming insufficient, KPMG-2025); verification burden when tools sit outside the workflow (SAGE-2026); security threats (48% of high-maturity leaders, GARTNER-2025); spreading across too many workflows (BCG-2025 p.6).
- **Emphasize.** Full loop on a few processes (spec §3.2); data readiness; controls (ICAEW-GOV-2026 six questions); a few high-value workflows with workforce training rather than broad rollouts (BCG-2025 p.9); first delegated workflows only where prerequisites hold (see 2.3).
- **Ready for Scaling when** `[P]`: two or more workflows in production; a second workflow reused a component of the first; one place records value across workflows; a named central owner exists.
- **Professional-services flavor** `[P]`: AI first-pass review or drafting inside the engagement or matter file, with a documented review standard.

#### Scaling

- **Observable markers**
  - Platform for reuse; data and outcomes visible on dashboards; test-and-learn culture; expanding process automation. [S] MITCISR-2024 stage 3.
  - Dedicated AI leader (91% of high-maturity organizations, GARTNER-2025; chief AI officer in 60% of enterprises, WHARTON-2025 human-capital theme). [S]
  - Centralized strategy, governance, data and infrastructure (almost 60% of high-maturity leaders, GARTNER-2025). [S]
  - Value tracked rigorously (more than 60% of future-built firms versus 17% of stagnating, BCG-2025 p.14). [S]
  - Central AI platforms and reusable agents (3x more central AI platforms in operation than laggards, BCG-2025 Exh.6). [S]
  - ROI measured formally (72% in Wharton's panel of large US enterprises). [S] WHARTON-2025.
- **Scope variants** `[P]`: *team* is a contributor to a shared platform; *unit* has a portfolio and a roll-up; *org* has an operating model, a funded multi-year plan and an owner with decision rights.
- **Typical blockers.** Operating model and ownership (BCG: exclusive IT ownership is an indicator of stagnating firms; shared business-IT ownership 1.5x more likely at future-built, BCG-2025 pp.12-13); training investment softening and hiring difficulty (WHARTON-2025: -8 points; 49% cite recruiting advanced skills as a top challenge); governance for autonomy (DELOITTE-2026 finding 5); infrastructure and data debt (CISCO-2025 via RCR: 15% have networks fully ready; 19% have fully centralized data infrastructure); business-unit trust (GARTNER-2025); scaling only a minority of strategic bets even among leaders (ACCENTURE-2025: front-runners scaled 34%).
- **Emphasize.** Portfolio thinking, shared platforms, operating model, governance, measuring value (spec §3.2); workforce enablement at scale; role redesign; agent governance.
- **Ready for AI-native when** `[P]`: value is measured at P&L level; the team is asking what to sell, to whom and at what price, not only how to do the same work faster.
- **Professional-services flavor** `[P]`: engagement methodology, quality control and staffing models updated firm-wide; reviewers trained on AI outputs.

#### AI-native

- **Observable markers**
  - AI embedded in all decision-making; proprietary AI used internally; new AI-based services sold, or AI capability sold as a service. [S] MITCISR-2024 stage 4 (example: Ping An, 49% of product sales made by AI service representatives by end 2022 per the briefing).
  - Growth and innovation beyond optimization, combining AI with new services and business models. [S] LICHTENTHALER-2020 level 4, pp.42-43.
  - Impact becomes economic: service packaging and pricing shift from time-based to value-based; freed capacity redeployed to more clients or advisory work. [S] SAGE-2026 stage 4.
  - Workflows reshaped end to end with agents as digital workers under human oversight; more than 50% of staff upskilled; reinvestment of gains. [S] BCG-2025 pp.4, 7, 13.
  - A "human-agent ratio" is managed as a business metric. [S] MSFT-WTI-2025.
- **Scope variants** `[P]`: *team* has redefined its service or output; *unit* sells something new; *org* has changed its pricing, its offering or its cost base because of AI.
- **Typical blockers.** Pricing structures built on time (SAGE-2026); advisory skill-set and client-conversation gap (SAGE-2026); skill atrophy worries (43% of leaders, WHARTON-2025); accountability and professional obligations in regulated work (LAWSOC-GENAI checklist); unmanaged AI-security risk (72% of BCG respondents report unmanaged AI-security risks, BCG-2025 p.10).
- **Emphasize.** Business-model exposure, new services, pricing, AI-native competitors, workforce redesign (spec §3.2).
- **Caution.** Validate any AI-native claim with evidence: revenue or pricing change, not tools or headcount.
- **Professional-services flavor** `[P]`: outcome- or subscription-priced services; AI-enabled offerings the firm could not deliver before.

---

## 3. Expert moves

Format: **move** — when to use it — what it reveals — source ref.

1. **Ask to see the last time they used AI on real work, and look at the artifact** — onboarding, any stage — separates sustained use from awareness; reveals the individual's frequency band and task type — MSFT-WTI-2024 §3 (frequency and time-saved bands); GALLUP-2025 (frequency bands).
2. **Ask for a count of workflows in production, each with a named owner and a before/after measure** — onboarding, Experimenting versus Adopting — separates pilots from operation; reveals pilot purgatory — MITCISR-2024 stage 2; BCG-2025 Exh.8 (62% deployed versus 12%); ILTA-2025 via Law360 (nearly 60% of Copilot-using firms still piloting).
3. **Ask which pilots were stopped and why** — onboarding, Experimenting — reveals whether pilots feed a learning loop or die uncounted; surfaces hidden blockers such as data, trust or fit — LICHTENTHALER-2020 level 1, p.42.
4. **Ask what people use that has not been approved** — onboarding, especially Curious and Experimenting — reveals shadow AI, true individual maturity, and the policy gap — MITNANDA-2025 §3.3; TR-2026 key findings; MSFT-WTI-2024 §1.
5. **Triangulate the leader's self-placement against two or three staff or a different team** — onboarding — reveals awareness gaps and optimism bias — GALLUP-2025 (do-not-know shares by role); DELOITTE-2026 finding 7; BCG-2025 p.6 (operational management telling leaders value will come).
6. **Place each scope and each dimension, then plan against the weakest** — onboarding and frame — reveals mixed maturity, for example strong strategy but weak data — DELOITTE-2026 finding 7; BCG-2025 Exh.1; CISCO-2025 via RCR. `[P]` for the practice.
7. **Ask "what happened to the hours AI saved last quarter?"** — onboarding and frame, Experimenting and Adopting — reveals the capacity gap and whether value is captured — SAGE-2026.
8. **Ask how the work is priced and whether pricing has changed since AI** — frame, fee-based professions — reveals whether efficiency becomes margin compression; marks the AI-native boundary — SAGE-2026 stage 4.
9. **Ask who owns AI: business, IT, both or no one** — frame, plan — exclusive IT ownership indicates stagnation; shared ownership with clear decision rights marks leaders — BCG-2025 pp.12-13, Exh.7.
10. **Ask "would finance accept this number?"** — frame and plan-and-control — separates self-reported time saved from measured value — WHARTON-2025 (72% formally measuring ROI); KPMG-2025 (78% say traditional metrics insufficient); BCG-2025 p.14.
11. **Ask for the AI policy and the date of the last training, then ask one staff member to describe the policy** — onboarding, plan — separates paper governance from lived governance — LITIFY-2026 (training and policy gap); LAWSOC-GENAI checklist.
12. **Run the ICAEW six top-level governance questions as a ten-minute screen** — onboarding and plan-and-control — reveals whether governance is ready for the next stage — ICAEW-GOV-2026.
13. **Ask what managers do about AI: encourage, permit, ignore** — onboarding and plan — reveals the main adoption lever below leadership — GALLUP-2025 (adoption strongly associated with managerial support).
14. **Ask what the best user does differently and what share of the team does it** — onboarding, Experimenting — reveals habits to copy: frequent experimentation, pausing before a task to ask whether AI can help, retrying — MSFT-WTI-2024 §3. Use to choose champions.
15. **Ask "would you let it run without a check?" and map the checkpoints** — before proposing delegation — reveals readiness for agentic work — BCG-2025 p.9 (prerequisites); DELOITTE-2026 finding 5; ICAEW-GOV-2026 Q4.
16. **Ask where the AI sits relative to the system of record** — onboarding, Experimenting versus Adopting — tool count is not maturity; integration is — SAGE-2026 stage 3; CBA-2026.
17. **Ask for the last AI error that was caught, and who caught it** — onboarding and plan-and-control — reveals verification practice and whether staff know the "jagged" edge of AI — HBS-2023 (AI users 19% less likely to be correct on a task outside the frontier); ANTHROPIC-FLUENCY (discernment as a skill).
18. **Ask how long the last initiative took from pilot start to production** — frame, plan — reveals throughput and sets a realistic plan horizon — BCG-2025 Exh.8 (9-12 versus 12-18 months); MITNANDA-2025 §3.2 (90 days versus nine months or longer, directional).
19. **Ask "if this works, what changes about what you sell or who you serve?"** — frame — separates efficiency ambition from reinvention ambition — DELOITTE-2026 (66% efficiency gains versus 20% revenue); BCG-2025 p.6 (too incremental).
20. **Pick only the next stage and write three observable exit criteria** — plan — avoids stage-skipping and keeps progress countable — MITCISR-2024 (capabilities build cumulatively); FIELDGUIDE-2025 (progress without perfection). `[P]` for the three-criteria format.
21. **Ask "what would tell you that you are stuck here?"** — Experimenting and Adopting — names the comfort trap of assisted productivity — SAGE-2026 stage 2.
22. **Offer low-risk, visible quick wins at Curious** — Curious — builds trial and observability — IRGLOBAL-2025 (start with lower-risk applications); ROGERS-WIKI.
23. **Choose leading indicators the team can read monthly** — plan-and-control — for example share of staff using weekly, workflows in production, share with a measured baseline, pilot-to-production time, reuse count — BCG-2025 Exh.8; MITCISR-2024 (dashboards). `[P]` for the list.
24. **Count markers by evidence, then place at the highest stage where most markers hold, and flag exceptions** — onboarding — turns stage placement into an audit trail the user can edit. `[P]`
25. **Ask which roles will change and what staff have been told** — plan — reveals trust and skill-atrophy risks that stall scaling — WHARTON-2025 (43% of leaders warn of skill atrophy; mismatch of capability needs and training budget).
26. **Ask what the override and exception log shows** — plan-and-control — checks whether human checkpoints are real and feed improvement — ICAEW-GOV-2026 Q4 (overrides logged, reviewed, used to improve).
27. **Re-diagnose at a fixed cadence, such as each quarter or review** — plan-and-control — stage placements age fast — BCG-2025 Exh.1 (2024 versus 2025 distributions); KPMG-2025 (agent deployment 11% to 42% in two quarters).

---

## 4. Question bank

Tags: scope `[team]` `[unit]` `[org]`; journey stage in parentheses; `(all)` if stage-neutral.

### 4.1 Onboarding (placing the user, mostly stage diagnosis)

Opening, any scope:

1. In the last two weeks, who in your scope used AI on real work, and how often? Can you show me one example? `[team][unit][org]` (all). *Reveals frequency band and sustained use. Move 1.*
2. What do people use that you haven't approved or don't know about? `[team][unit][org]` (Curious, Experimenting). *Move 4.*
3. If I asked three people on your team what the AI policy says, what would they say? `[team][unit]` (Curious, Experimenting). *Move 11.*
4. Has your manager, or have you, said out loud that people should use AI, and what for? `[team][unit]` (all). *Move 13.*

Curious versus Experimenting `[P]` for the cut:

5. Is there any task where AI is part of how the work is *normally* done, not just tried? `[team]` (Curious vs Experimenting).
6. What was the last thing someone tried, and what happened to it? `[team][unit]` (Curious, Experimenting). *Move 3.*
7. What is holding you back from trying more: not sure where it applies, confidentiality, cost, skills, or something else? `[team][unit][org]` (Curious). *Source blockers: IRGLOBAL-2025.*

Experimenting versus Adopting:

8. How many AI workflows are in production, who owns each, and how do you know they work? `[unit][org]` (Experimenting, Adopting). *Move 2.*
9. Which pilots did you stop, and what did you learn from stopping them? `[unit][org]` (Experimenting). *Move 3.*
10. Where does AI sit relative to the system where the work is recorded: beside it, or inside it? `[team][unit]` (Experimenting, Adopting). *Move 16.*
11. What happened to the hours AI saved last quarter? `[team][unit]` (Experimenting, Adopting). *Move 7.*
12. Who would you call if an AI-assisted output turned out to be wrong, and how would you know? `[team][unit]` (Experimenting, Adopting). *Moves 15, 17.*

Adopting versus Scaling:

13. Has a second workflow reused anything from the first (data connection, prompt library, approval step, review checklist)? `[unit][org]` (Adopting, Scaling). `[P]`
14. Is there one place where value from all AI workflows is recorded? Who reads it? `[unit][org]` (Adopting, Scaling). *Moves 10, 23.*
15. Who owns AI at your level: business, IT, both or no one? Do they have decision rights and a budget? `[unit][org]` (Adopting, Scaling). *Move 9.*
16. How many people have had role-specific training in the last year, and who funds it? `[unit][org]` (Scaling). *WHARTON-2025, BCG-2025 Exh.6.*

Scaling versus AI-native:

17. Has AI changed how you price, package or sell any service? `[unit][org]` (Scaling, AI-native). *Move 8.*
18. Have you launched any service you could not have delivered before AI? `[unit][org]` (Scaling, AI-native). *MITCISR-2024 stage 4; SAGE-2026 stage 4.*
19. Who is your most AI-native competitor or new entrant, and what are they doing that you cannot? `[org]` (Scaling, AI-native). *spec §3.2.*

Individual-level (for a user who is the scope), `[P]` composed from MSFT-WTI-2024 §3 and ANTHROPIC-FLUENCY:

20. Before you start a task, do you stop and ask whether AI could help? If the first answer is poor, do you retry or change how you ask?
21. What do you hand to AI completely, what do you do together, and what do you never delegate? How do you check the output?

### 4.2 Frame

22. What does success look like in 12 months: hours saved, quality, growth, risk, a new service? Which one matters most? `[team][unit][org]` (all).
23. If everything works, what changes about what you sell or who you serve? `[unit][org]` (Adopting+). *Move 19.*
24. How is the work priced today? If your time per job halved, what would happen to revenue and margin? `[unit][org]` (Experimenting+, fee-based). *Move 8; SAGE-2026.*
25. What is the pressure to act now: talent, client demand, fee pressure, regulation, competitors? `[unit][org]` (all). *spec §3.1.*
26. How long did your last pilot take from start to production? `[unit][org]` (Experimenting+). *Move 18.*
27. Which of these is your binding constraint: data, integration, skills, governance, ownership, budget, trust? `[team][unit][org]` (Experimenting+). *Move 6; DELOITTE-2026; CISCO-2025.*
28. Which professional or regulatory obligations limit what AI may touch (confidentiality, independence, privilege, supervision)? `[team][unit][org]` (all). *LAWSOC-GENAI checklist; ICAEW-GOV-2026.*

### 4.3 Plan-and-control

29. What is the next stage for each scope, and what are three things we could see that prove you got there? `[team][unit][org]` (all). *Move 20.*
30. For each planned workflow: what is the baseline, who signs off the number, and when do we read it? `[team][unit]` (Experimenting+). *Moves 10, 23.*
31. Where do humans check, and what happens to overrides? `[team][unit]` (Adopting+). *Moves 15, 26; ICAEW-GOV-2026 Q4.*
32. Who is accountable for AI policy and risk, and is that written down? `[unit][org]` (Adopting+). *ICAEW-GOV-2026 Q2.*
33. What is the training plan, by role, and who protects the time? `[team][unit][org]` (all). *Move 25; WHARTON-2025.*
34. How will we tell staff what changes for their roles, and when? `[team][unit][org]` (Adopting+). *Move 25.*
35. What review cadence will we use to re-check stage placement? `[unit][org]` (all). *Move 27.*
36. What would make us stop or pause a workflow? Who decides? `[team][unit]` (Adopting+). *ICAEW-GOV-2026 additional considerations (incident handling).*

---

## 5. Common traps

1. **Placing by tool inventory instead of integration and outcomes.** Why: tools are easy to count; integration is not. Evidence: maturity is "not a measure of how many tools a firm has deployed" and experimentation is not integration (CBA-2026); Sage places the shift at connecting AI to client data and real workflows (SAGE-2026 stage 3). Avoid: ask for owned workflows, system-of-record integration and measured outcomes (Moves 2, 16).

2. **Taking the user's self-placement at face value.** Why: leaders are further from daily use and hear about adoption from others. Evidence: 7% of leaders versus 26% of individual contributors answer "do not know" on whether the organization has implemented AI (GALLUP-2025); more companies call strategy highly prepared while feeling less prepared on infrastructure, data, risk and talent (DELOITTE-2026 finding 7); BCG reports operational managers telling leaders they already use AI widely and value will follow (BCG-2025 p.6). Avoid: triangulate (Move 5), count evidence (Move 24).

3. **Treating "efficiency gain" as "progress up the ladder."** Why: assisted productivity feels like success and nothing breaks. Evidence: Sage calls stage 2 "dangerous" because it is easy to stay; 71% of firms use external AI tools, 7% call impact transformational (SAGE-2026). Deloitte: 66% report efficiency gains, 20% report revenue growth (DELOITTE-2026). Avoid: ask what happened to saved time and whether pricing or services changed (Moves 7, 8, 19).

4. **Pilot purgatory.** Why: enthusiasm and budgets launch pilots; conversion to workflow-integrated systems is rare. Evidence: nearly 60% of firms using Microsoft 365 Copilot are still piloting (ILTA-2025 via Law360); 5% of custom enterprise tools reach production in interview-based, directional data (MITNANDA-2025 §3.2); many experiments are discontinued without rollout (LICHTENTHALER-2020 level 1, p.42). BCG reports too-wide experimentation across scores of workflows as a laggard pattern (BCG-2025 p.6). Avoid: baselines and owners before pilots; limit the number of live pilots (Moves 2, 3, 20).

5. **Skipping rungs.** Why: ambition and vendor messaging. Evidence: agents need data foundations, scaled capabilities and governance first (BCG-2025 p.9); only one in five has mature agent governance (DELOITTE-2026 finding 5). Fieldguide says progress need not be all-or-nothing (FIELDGUIDE-2025). Avoid: pick only the next stage (Move 20); gate delegation on checkpoints (Move 15).

6. **Ignoring shadow AI.** Why: individuals adopt faster than organizations. Evidence: 34% of professionals use AI their organization has not approved (TR-2026); 78% of users bring their own tools (MSFT-WTI-2024 §1); workers at over 90% of firms surveyed use LLMs regularly while 40% of firms bought a subscription (MITNANDA-2025 §3.3). Avoid: ask (Move 4) and treat it as both a risk and a source of use cases.

7. **Neglecting the people layer.** Why: tools and policy are visible; manager behavior and training are not. Evidence: adoption associated with managerial support (GALLUP-2025); training investment down 8 points while skill gaps persist (WHARTON-2025); Prosci's vendor research reports human factors as the main challenge (PROSCI-AI, wording varies between its pages). Avoid: Moves 13, 25 and a training plan by role.

8. **Staging on a single score.** Why: dimensions differ. Evidence: BCG uses 41 dimensions; Cisco six pillars; reviewers find no standard terminology (BCG-2025; CISCO-2025; SADIQ-2021). Avoid: place per dimension and per scope (Move 6).

9. **Over-reading headline statistics.** Why: definitions are narrow and samples are small or vendor-run. Evidence: the "95%" in MIT NANDA is stated as organizations getting zero return in the executive summary, yet the pilot-to-production exhibit defines success narrowly (marked and sustained productivity or P&L impact for task-specific tools) and the report calls its figures directionally accurate and preliminary (MITNANDA-2025 pp.2, 6). KPMG's sample is 130 US leaders at $1bn+ companies (KPMG-2025). Avoid: quote the measure with the number; use ranges.

10. **Mistaking correlation for a stage effect.** Why: maturity and performance are measured in the same survey. Evidence: MIT CISR's financial comparison is from the 2022 survey, relates mainly to analytical AI, and compares stages in one cross-section (MITCISR-2024 intro and footnote). Avoid: describe stages as associated with, not causing, outperformance.

11. **Using a vendor's ladder as your own.** Why: each ladder leads to the product. Evidence: see 2.1 point 8. Avoid: use markers, then ask what the user needs, tool-neutrally.

12. **Capacity gap in fee-based professions.** Why: AI compresses the basis on which time-priced work is charged. Evidence: SAGE-2026 stage 4 arithmetic (8 hours down to 3, revenue falls by more than half if billed hourly; five empty hours if fixed fee). Avoid: put pricing into the Frame phase for Adopting and above (Moves 8, 19).

---

## 6. Evidence

Provenance codes: `independent` = academic or non-commercial; `vendor-published` = consultancy, vendor or analyst publication about its own research; `self-reported` = the respondent's own report of their own outcomes (nearly all of these surveys are self-reported at the respondent level; the code applies to the publisher where stated).

| # | Data point | What it measures (source's terms) | Who, when, n | Provenance | Source and locator |
|---|---|---|---|---|---|
| E1 | Stage shares 28% / 34% / 31% / 7% | Share of responding enterprises in each of four AI-maturity stages, assigned by "Total AI Effectiveness" (equal-weight effectiveness of AI to improve operations, customer experience, and ecosystem; stage cut-offs 0-49%, 50-74%, 75-99%, 100%) | MIT CISR 2022 Future Ready Survey, N=721; plus 16 interviews at nine enterprises in Aug-Nov 2024 | independent (academic centre; survey self-report) | MITCISR-2024 Fig.1 and footnote |
| E2 | Growth -12.6 / -3.5 / +11.3 / +17.1 pp; profit -9.6 / -2.2 / +8.7 / +10.4 pp by stage | Growth and profit in 2022, percentage points above or below industry average | Same sample | independent; correlational; mostly analytical AI as the survey predates generative AI | MITCISR-2024 Fig.1 |
| E3 | 14% / 46% / 35% / 5% (2025); 25% / 49% / 22% / 4% (2024) | Share of companies in Stagnating / Emerging / Scaling / Future-built by BFFxAI maturity score across 41 dimensions | BCG Build for the Future 2025 Global Study, n=1,250 | vendor-published (consultancy) | BCG-2025 Exh.1 |
| E4 | Future-built have 1.7x revenue growth, 1.6x EBIT margin, versus stagnating + emerging | Future-built versus the 60% in stagnating or emerging (revenue growth and EBIT margin); three-year TSR comparison (3.6x) uses external Capital IQ data | Same | vendor-published; correlational | BCG-2025 p.5 and Exh.1 |
| E5 | 62% of initiatives deployed (future-built) versus 12% (laggards); 9-12 versus 12-18 months to deploy | Share of AI workflows at deployed stage; average months to fully deploy | Same | vendor-published; self-reported | BCG-2025 Exh.8, p.14 |
| E6 | More than 60% of future-built track AI value versus 17% of stagnating | Share that "rigorously track" AI value | Same | vendor-published | BCG-2025 p.14 |
| E7 | Nearly 100% of future-built report deeply engaged C-suites versus 8% of laggards; exclusive IT ownership indicates stagnating | Share with deeply engaged C-suite; ownership model | Same | vendor-published | BCG-2025 p.11, Exh.7 |
| E8 | 45% of high-maturity organizations keep AI initiatives in production 3+ years, versus 20% of low-maturity | Share whose initiatives remain in production for three years or more | Gartner survey; a search summary gives 432 respondents in six countries, Q4 2024 (search-only detail) | vendor-published (analyst firm) | GARTNER-2025 (MHL reproduction, paras 1-3) |
| E9 | 57% versus 14% business units trust and are ready to use new AI solutions | High- versus low-maturity organizations | Same | vendor-published | GARTNER-2025 |
| E10 | Data availability and quality a top challenge: 34% low-, 29% high-maturity; security threats top-three barrier for 48% of high-maturity; right use case for 37% of low-maturity | Share of leaders identifying the barrier | Same | vendor-published | GARTNER-2025 |
| E11 | 63% of high-maturity leaders run financial analysis on risk factors, do ROI analysis and measure customer impact; 91% have dedicated AI leaders; almost 60% centralized strategy, governance, data and infrastructure | Share of high-maturity leaders | Same | vendor-published | GARTNER-2025 |
| E12 | 34% deep transformation / 30% redesigning key processes / 37% surface-level | Share of surveyed organizations by depth of AI use | Deloitte, 3,235 senior leaders, Aug-Sep 2025, 24 countries | vendor-published (consultancy) | DELOITTE-2026 "How is AI transforming business functions?" |
| E13 | 66% productivity/efficiency gains; 20% increased revenue; 74% hope to grow revenue | Share of organizations reporting benefit achieved so far | Same | vendor-published | DELOITTE-2026 "What does AI do for business?" |
| E14 | One in five has a mature model for governance of autonomous agents | Share of companies | Same | vendor-published | DELOITTE-2026 finding 5 |
| E15 | 42% say strategy is highly prepared for AI adoption but feel less prepared on infrastructure, data, risk and talent | Share rating strategy preparedness | Same | vendor-published | DELOITTE-2026 finding 7 |
| E16 | 82% use gen AI weekly; 46% daily; 72% formally measure ROI; nearly three-quarters see positive ROI; CAIO in 60%; training investment -8 pp; 43% warn of skill atrophy | Share of senior decision makers at US enterprises (1,000+ employees, over $50m revenue) | Wharton Human-AI Research and GBK Collective, ~800 respondents, 26 Jun-11 Jul 2025 | independent academic sponsor; survey self-report; US-only | WHARTON-2025 pp.5, 9-11 |
| E17 | 45% use AI at work at least a few times a year; 23% a few times a week or more; 10% daily; 23% do not know whether their org implemented AI (26% individual contributors, 16% managers, 7% leaders) | Share of employed US adults | Gallup Panel, n=23,068, 5-19 Aug 2025 | independent | GALLUP-2025 |
| E18 | 75% of knowledge workers use gen AI at work; 78% of users bring their own tools; 60% of leaders worry leadership lacks a plan and vision | Shares of survey respondents; BYOAI share is of AI users | Microsoft and LinkedIn, 31,000 people, 31 countries, 8 May 2024 | vendor-published | MSFT-WTI-2024 §1 |
| E19 | Power users 66% more likely to redesign business processes; frequent experimentation is the top predictor of power-user status | Relative likelihood versus other segments; power user = familiar with gen AI, uses it several times a week, saves over 30 min a day (self-reported) | Same | vendor-published; self-reported | MSFT-WTI-2024 §3 and definitions |
| E20 | 95% of organizations getting zero return; 5% of custom enterprise AI tools reach production | Executive-summary statement; "successfully implemented" for task-specific tools means users or executives report marked and sustained productivity and/or P&L impact | MIT NANDA, 300+ public initiatives, 52 organizations interviewed, 153 survey responses, Jan-Jun 2025; marked preliminary and directional | independent academic initiative; interview-based; not peer-reviewed | MITNANDA-2025 pp.2, 6 |
| E21 | Workers at over 90% of surveyed companies use LLMs regularly; 40% of companies purchased an LLM subscription | Share of companies | Same | independent; directional | MITNANDA-2025 §3.3 |
| E22 | 15% reinvention-ready; 8% front-runners; front-runners with revenue above $10bn grew revenue 7 pp faster than companies still experimenting; even front-runners scaled 34% of strategic bets | Share of companies; revenue growth gap; share of strategic bets scaled | Accenture, 2,000 companies surveyed (2025) | vendor-published | ACCENTURE-2025 |
| E23 | 42% have deployed at least some agents, up from 11% two quarters earlier; 78% say traditional business metrics are becoming insufficient for AI | Share of organizations; agreement | KPMG Q3 2025 AI Pulse, 130 US C-suite and business leaders at $1bn+ revenue organizations | vendor-published (consultancy); small sample | KPMG-2025 key takeaways and press release |
| E24 | 22% have a visible defined AI strategy; visible strategy: twice as likely to see AI-driven revenue growth than ad hoc adopters, 3.5x more likely to see critical benefits than no-plan; 80% expect high or transformational impact on profession in 5 years, 38% expect significant change at own org this year | Share of respondents and relative likelihood | Thomson Reuters, 2,275 professionals, Feb-Mar 2025, release 26 Jun 2025 | vendor-published; self-reported | TR-2025 |
| E25 | 66% say AI meets or exceeds expectations where a clear strategy exists versus 22% where none; 34% use unapproved AI; 41% lack tools that meet professional accountability standards | Share of professionals | Thomson Reuters Future of Professionals 2026 edition, 1,800+ professionals and executives, 60+ countries (page date not stated) | vendor-published | TR-2026 key findings |
| E26 | 80% of law firms using or exploring gen AI; Microsoft 365 Copilot: two-thirds on request, 8% to all employees; nearly 60% of Copilot-using firms still piloting; per-tool training offered 17% to 36% | Share of respondents (firms) | ILTA 2025 Legal Technology Survey, about 600 firms, reported 15 Sep 2025 | independent (industry association), via news report | ILTA-2025 via Law360 |
| E27 | 71% of firms use external AI tools; 7% describe impact as transformational | Share of accountancy firms | Sage research with AccountingWeb (sample not stated in the article), 2026 | vendor-published | SAGE-2026 |
| E28 | 78% of legal professionals use AI; fewer than 50% have sufficient training or clear AI policies | Share of legal professionals | Litify 2025 State of AI in Legal Report (n not stated in the blog) | vendor-published | LITIFY-2026 |
| E29 | 78% of respondents say their organizations use AI in at least one function (2024), up from 55%; gen AI in at least one function 71% from 33% | Share of survey respondents | McKinsey survey as reported in the Stanford AI Index | independent compilation of a consultancy survey | STANFORD-2025 chapter 4, Figure 4.4.1 |
| E30 | 88% regular AI use in at least one function; nearly two-thirds not yet scaling enterprise-wide; 39% report any enterprise-level EBIT impact; about 6% are high performers (5%+ of EBIT from AI) | As worded in a search summary of the McKinsey report | McKinsey State of AI 2025 | vendor-published; **search-only, not verified against the primary** | MCKINSEY-2025 |
| E31 | 13% Pacesetters; Pacesetters four times more likely to move pilots into production; 15% have fully AI-ready networks; 19% fully centralized data infrastructure globally | Share of organizations | Cisco AI Readiness Index 2025, 8,000 leaders in 30 markets, reported 9 Dec 2025 (secondary report) | vendor-published; secondary | CISCO-2025 via RCR |
| E32 | +14% issues resolved per hour on average; +34% for novice and low-skilled workers; minimal for experienced workers | Productivity with a gen AI assistant in customer support (adjacent to knowledge work; cap at B) | 5,179 agents, staggered rollout | independent (NBER working paper; not peer-reviewed at issue) | NBER-2023 abstract |
| E33 | Inside the frontier: 12.2% more tasks and 25.1% faster with better quality; outside the frontier: 19% less likely to produce correct solutions | Randomized experiment on 18 realistic consulting tasks and one managerial task | 758 BCG consultants, GPT-4 | independent academic working paper | HBS-2023 abstract |
| E34 | Directive conversations on Claude.ai 27% to 39%; 1P API use 77% automation versus about 50% on Claude.ai; later report: augmentation back to 52% | Share of sampled conversations by collaboration mode, Claude only | Anthropic Economic Index, Sep 2025 and Jan 2026 | vendor-published; one product's users | ANTHROPIC-EI-2025; ANTHROPIC-EI-2026 |
| E35 | 63% of organizations cite human factors as a primary challenge (also stated as 56%-64% of challenges); 38% of adoption challenges from insufficient training; 37% invest significantly in change management | As worded by Prosci | Prosci study of 1,107 professionals; other figures from Prosci research | vendor-published; wording varies between its pages | PROSCI-AI |
| E37 | 7 in 10 surveyed companies report minimal or no impact from AI so far (2019; pre-generative AI) | Share of companies surveyed | MIT SMR and BCG 2019 Global Executive Study, more than 2,500 executives | independent-academic with consultancy sponsor | MITSMR-2019 introduction |
| E36 | Five-level maturity grids prevail; 6 of 13 AI maturity studies (46%) assess the technology aspect | Systematic literature review | 13 AI maturity studies | independent, peer-reviewed | SADIQ-2021 abstract |

Reading guide for the advisor:

- Stage shares are not comparable across models (E1 versus E3 versus E22): different samples, years, definitions and tier cut-offs. Quote them with the model name.
- Use E8-E11 and E3-E7 for *what high-maturity organizations do*, not for causality.
- Use E16, E17, E18, E26 for *where the market is*; use E12-E14 for *depth of change*.

---

## 7. Worked examples

All four are short. A and B are real organizations as described in sources. C and D are illustrative constructions from sourced facts.

**A. Guardian Life, disability underwriting: a stage 2 pilot with measured value (MIT CISR).**
The underwriting team works with a partner to build a generative AI tool that summarizes documentation and augments decision-making. Participating underwriters are reported to save on average five hours per day (MITCISR-2024, Stage 2 example; a pilot figure as reported in the briefing, not independently measured). The pilot is positioned as part of reimagining end-to-end process transformation. Advisor lesson: this is a "Build Pilots and Capabilities" example, and the right question is what it takes to move the pilot into a shared, owned workflow, and whether the hours save is verified and what happens to them.

**B. Ally and DBS: what stage 3 and stage 4-leaning looks like (MIT CISR).**
Ally launched the Ally.ai platform in July 2023, integrating several commercial LLMs with its data in a safe environment, and reported saving an average three minutes per customer call on more than four million calls in 2023 and developing creative campaigns 34% faster (MITCISR-2024, Stage 3 example; company-reported). DBS set a KPI of one thousand experiments a year, doubled AI economic impact from SGD 150 million to SGD 370 million from 2022 to 2024, delivered over 350 use cases, and expected impact above SGD 1 billion in 2025 (MITCISR-2024, closing section; company-reported). These are banks rather than professional-services firms, but they show what "platform + dashboards + test-and-learn" looks like: a reuse platform, measurable per-use benefits and a managed experiment pipeline.

**C. A mid-size accounting firm at "assisted productivity" (illustrative, built on SAGE-2026 arithmetic).**
Partners and staff use AI daily for emails, summaries and tax queries. A recurring compliance job drops from eight hours to three. If billed hourly, revenue on that job falls by more than half. If fixed fee, five hours are free but nothing has been planned for them (SAGE-2026 stage 4 section, worked example). *Advisor moves:* place the firm between Experimenting and Adopting. Ask what happened to saved hours (Move 7). Ask how the work is priced (Move 8). Propose one connected workflow with a baseline, and one decision on what to do with freed capacity (Sage lists taking on more clients, shifting time from processing to interpretation, expanding into advisory, and moving to value-based pricing). Exit criteria for Adopting: one workflow connected to client data, an owner, a measured before/after, and a pricing decision on the freed time. `[P]` for the exit criteria.

**D. A tax leader who says "we are Adopting" (illustrative diagnostic walk-through).**
The leader reports that Copilot is "rolled out" to the practice. The advisor asks for a count of owned production workflows, and the answer is none: licenses were issued on request and a few staff use them for drafting. This matches the ILTA pattern (two-thirds on request, 8% to all, nearly 60% still piloting; ILTA-2025 via Law360). The advisor asks what staff use that is not approved (Move 4), and what the policy says (Move 11). It places the *team* at Experimenting, notes the *individual* power users are further ahead, and agrees one target: a single recurring return-review step with a baseline and a review checkpoint. The plan names three observable exit criteria for the next stage (Move 20). The advisor does not recommend agents (BCG-2025 p.9; DELOITTE-2026 finding 5).

---

## 8. Mapping to phases

### Onboarding (profile, journey stage, adapted path)

- **Stage diagnosis by evidence.** The stage cards (2.4) and onboarding questions 1-21 let the advisor place a scope without asking the user to self-rate. Stage is recorded per scope and per dimension, with the binding constraint named. `[P]`
- **Probes that correct over-optimism**: unapproved use, staff triangulation, owned production workflows, what happened to saved hours (Moves 4, 5, 2, 7).
- **Adapted path.** Where the evidence puts a user between two stages, choose the earlier stage's emphasis and add the later stage's first question. Curious: inspiration tour plus minimal safe-use rules; Experimenting: shared team workflows, baselines; Adopting: full loop, data, controls; Scaling: portfolio, platform, value measurement; AI-native: business model, pricing, workforce redesign (spec §3.2, sharpened by section 2.4 markers and blockers).
- **Quick governance screen** (ICAEW-GOV-2026) to detect whether policy and ownership are ready for the user's target stage.

### Frame (ambition, why now, success, value levers)

- **Ambition level matched to stage.** Efficiency ambition is typical (Deloitte: 66% report efficiency gains); reinvention ambition is rare. The advisor should ask the Frame questions that surface whether the user's ambition is efficiency or reinvention (Move 19), and make pricing and service model part of the frame for fee-based professions (Move 8).
- **Success measures tied to stage.** Early stages: weekly use, wins shown, policy in place. Middle stages: workflows in production, baselines, pilot-to-production time. Later stages: value tracked across a portfolio, new services, pricing change (BCG-2025 pp.14; MITCISR-2024).
- **Why-now framing** can draw on benchmarks (distribution of firms across stages, speed of change) but must carry the measure and the source (section 6).
- **Value levers per stage**: capacity and speed early; quality and risk in the middle; growth and new services later `[P]`.

### Plan-and-control (actions, owners, KPIs, control plan, rhythm)

- **Plan to the next stage only**, with three observable exit criteria (Move 20); avoid agentic delegation until checkpoints, data readiness and governance exist (BCG-2025 p.9).
- **KPIs as leading indicators** the team can read: share using AI weekly, workflows in production, share with a measured baseline, pilot-to-production time, reuse count `[P]` (Move 23).
- **Control plan** builds on ICAEW-GOV-2026: strategy, policy, proportionate risk management, human interaction points, monitoring and oversight, staff skills; higher-risk additions for explainability, data lineage, cyber and incident handling. The Law Society checklist (LAWSOC-GENAI) supplies a practical checklist for legal settings.
- **Rhythm.** Re-diagnose at each review (Move 27); stage placements age quickly.
- **People plan**: manager support, role-specific training, and communication about role change (Moves 13, 25).

---

## 9. Sources

Access: `full` = I read the document; `partial` = part of it only; `secondary` = read a reproduction or summary of the primary; `search-only` = only search-result summaries.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| MITCISR-2024 | Building Enterprise AI Maturity (research briefing; also press release and audio transcript) | Weill, Woerner, Sebastian; MIT CISR, MIT Sloan | academic research briefing | https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian ; press release https://cisr.mit.edu/sites/default/files/2024-12/EnterpriseAIMaturityModel_CISRpressrelease_121924_0.pdf | Dec 2024 (press release 19 Dec 2024) | full |
| BCG-2025 | The Widening AI Value Gap: Build for the Future 2025 | Boston Consulting Group | consultancy report | https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf | cover says September 2025 (file name says October 2025) | full |
| GARTNER-2025 | Gartner Survey Finds 45% of Organizations With High AI Maturity Keep AI Projects Operational for at Least Three Years | Gartner (press release) | analyst press release | Primary (403 to curl): https://www.gartner.com/en/newsroom/press-releases/2025-06-30-gartner-survey-finds-forty-five-percent-of-organizations-with-high-artificial-intelligence-maturity-keep-artificial-intelligence-projects-operational-for-at-least-three-years ; read via reproduction: https://mhlnews.com/technology-automation/news/55301034/companies-with-high-ai-maturity-keep-projects-operational-for-3-years | 30 Jun 2025 (reproduction 7 Jul 2025) | secondary |
| GARTNER-MM | Gartner's AI Maturity Model: Maximize Your Business Impact | BMC Software blog (describes Gartner's five-level model) | vendor blog, secondary on Gartner | https://www.bmc.com/blogs/ai-maturity-models/ (Gartner's own toolkit page returned 403) | 30 Jan 2025 | secondary |
| MSFT-WTI-2024 | 2024 Work Trend Index: AI at Work Is Here. Now Comes the Hard Part | Microsoft and LinkedIn | vendor research report | https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part | 8 May 2024 | full |
| MSFT-WTI-2025 | The 2025 Annual Work Trend Index: The Frontier Firm is Born (Source Asia edition) | Microsoft | vendor research summary | https://news.microsoft.com/source/asia/2025/04/24/the-2025-annual-work-trend-index-the-frontier-firm-is-born/ | 24 Apr 2025 | full (regional edition; regional figures not used) |
| DELOITTE-2026 | The State of AI in the Enterprise, 2026 AI report | Deloitte AI Institute | consultancy research page | https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html | survey Aug-Sep 2025; page date not stated | full (web page; full report not read) |
| LICHTENTHALER-2020 | Five Maturity Levels of Managing AI: From Isolated Ignorance to Integrated Intelligence | U. Lichtenthaler, Journal of Innovation Management 8(1), 39-50 | academic paper | https://journalengineering.fe.up.pt/index.php/jim/article/download/2183-0606_008.001_0005/401 | 2020 | full |
| SADIQ-2021 | Artificial intelligence maturity model: a systematic literature review | Sadiq, Safie, Abd Rahman, Goudarzi; PeerJ Computer Science 7:e661 | academic review | https://peerj.com/articles/cs-661 (read via Europe PMC full text, PMC8409328) | 25 Aug 2021 | full |
| MITNANDA-2025 | The GenAI Divide: State of AI in Business 2025 (preliminary findings) | MIT NANDA | academic-initiative report | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf (mirror) | Jul 2025 | full |
| WHARTON-2025 | Accountable Acceleration: Gen AI Fast-Tracks Into the Enterprise (Year Three full report) | Wharton Human-AI Research and GBK Collective | academic-sponsored survey report | https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf | Oct 2025 | full (exec summary and themes read in detail) |
| GALLUP-2025 | AI Use at Work Rises | Gallup, Andy Kemp | polling report | https://www.gallup.com/workplace/699689/ai-use-at-work-rises.aspx | 14 Dec 2025 | full |
| ANTHROPIC-EI-2025 | Anthropic Economic Index report (September 2025) | Anthropic | vendor research | https://www.anthropic.com/research/anthropic-economic-index-september-2025-report | 15 Sep 2025 | full |
| ANTHROPIC-EI-2026 | Anthropic Economic Index report (January 2026) | Anthropic | vendor research | https://www.anthropic.com/research/anthropic-economic-index-january-2026-report | 15 Jan 2026 | full (summary sections) |
| ANTHROPIC-FLUENCY | AI Fluency: Framework & Foundations (course page; four competencies named in the curriculum: Delegation, Description, Discernment, Diligence) | Anthropic with Feller and Dakan | course page | https://www.anthropic.com/ai-fluency | not stated | partial (curriculum outline only) |
| HBS-2023 | Navigating the Jagged Technological Frontier (HBS Working Paper 24-013) | Dell'Acqua, McFowland, Mollick, et al. | academic working paper | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | Sep 2023 | full (abstract) |
| NBER-2023 | Generative AI at Work (NBER WP 31161) | Brynjolfsson, Li, Raymond | academic working paper | https://www.nber.org/papers/w31161 | Apr 2023, rev. Nov 2023 | full (abstract and front matter) |
| KPMG-2025 | AI Quarterly Pulse Survey Q3 2025 (deck and press release) | KPMG US | consultancy survey | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/ai-quarterly-pulse-survey-q3-2025.pdf ; https://kpmg.com/us/en/media/news/q3-ai-pulse.html | 18 Sep 2025 | full |
| ACCENTURE-2025 | The Front-runners' Guide to Scaling AI | Accenture | consultancy research page | https://www.accenture.com/us-en/insights/ai-data/front-runners-guide-scaling-ai | 2025 (page undated) | full (web page; PDF not read) |
| CISCO-2025 | Cisco AI Readiness Index 2025 (coverage) | RCR Wireless reporting on Cisco | trade press on vendor research | https://www.rcrwireless.com/20251209/ai/cisco-ai-readiness-index-2025 (Cisco page returned 403) | 9 Dec 2025 | secondary |
| STANFORD-2025 | AI Index Report 2025 | Stanford HAI | academic compilation | https://hai-production.s3.amazonaws.com/files/hai_ai_index_report_2025.pdf | Apr 2025 | full (adoption sections) |
| MITSMR-2019 | Winning With AI | Ransbotham et al., MIT SMR and BCG | academic-consultancy report | https://sloanreview.mit.edu/projects/winning-with-ai/ | 15 Oct 2019 | partial (introduction only; rest paywalled) |
| MCKINSEY-2025 | The state of AI in 2025: Agents, innovation, and transformation | McKinsey & Company | consultancy survey | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai (curl failed) | 2025 | search-only |
| PROSCI-AI | AI adoption; Enterprise AI adoption best practices (two blog pages) | Prosci | vendor blog | https://www.prosci.com/blog/ai-adoption ; https://www.prosci.com/blog/enterprise-ai-adoption-best-practices | pages undated | full |
| AWSCAF-2024 | AWS Cloud Adoption Framework for AI, ML and Generative AI | Amazon Web Services | vendor whitepaper | https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.html | 13 Feb 2024 (marked "for historical reference only") | partial (introduction) |
| MSFT-CAF-2026 | AI adoption (Cloud Adoption Framework) | Microsoft Learn | vendor guidance | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/ | last updated 15 Oct 2026 | full |
| LITIFY-2026 | Beyond Adoption: Introducing the Litify Legal AI Maturity Scale | Litify | vendor blog, legal | https://www.litify.com/blog/the-litify-legal-ai-maturity-scale | 19 Mar 2026 | full |
| IRGLOBAL-2025 | The Legal AI Adoption Curve: Where Your Law Firm Stands (content refers to Clio products and reports) | IR Global, on Mondaq | practitioner-network article, vendor-originated in tone | https://www.mondaq.com/uk/new-technology/1623228/the-legal-ai-adoption-curve-where-your-law-firm-stands | 13 May 2025 | full |
| SAGE-2026 | Where is your accounting or bookkeeping firm on the AI maturity curve? | Sage (UK), Asavin Wattanajantra | vendor blog, accounting | https://www.sage.com/en-gb/blog/accounting-bookkeeping-ai-maturity-curve/ | 8 Apr 2026 | full |
| FIELDGUIDE-2025 | A Clear Path to AI Transformation: Why We Created the AI Maturity Framework | Fieldguide, Jin Chang | vendor blog, audit and advisory | https://www.fieldguide.io/blog/a-clear-path-to-ai-transformation-why-we-created-the-ai-maturity-framework | 9 Sep 2025 | full (blog only; framework document not read) |
| TR-2025 | The AI Adoption Reality Check (2025 Future of Professionals, press release) | Thomson Reuters | vendor press release | https://www.thomsonreuters.com/en/press-releases/2025/june/the-ai-adoption-reality-check-firms-with-ai-strategies-are-twice-as-likely-to-see-ai-driven-revenue-growth-those-without-risk-falling-behind | 26 Jun 2025 | full |
| TR-2026 | The Future of Professionals (2026 edition landing page) | Thomson Reuters | vendor research page | https://www.thomsonreuters.com/en/c/future-of-professionals | page undated | full (landing page; report not read) |
| ILTA-2025 | Law Firms Embrace AI, But Full Deployment Remains Rare (reporting on ILTA 2025 Legal Technology Survey) | Law360 Pulse, Steven Lerner | trade press on industry survey | https://www.law360.com/articles/2387443/law-firms-embrace-ai-but-full-deployment-remains-rare | 15 Sep 2025 | secondary |
| CBA-2026 | Beyond AI-driven use-case chaos (opinion) | "National" magazine, Yogendra Malav | opinion article, legal | https://nationalmagazine.ca/fr-ca/articles/opinion/2026/beyond-ai-driven-use-case-chaos | 17 Jul 2026 | full |
| UPLEVEL-2023 | Managing GAI Risk: Introducing The Generative AI Maturity Model | UpLevel Ops, via Above the Law | vendor article, legal ops | https://abovethelaw.com/legal-innovation-center/2023/09/26/managing-gai-risk-introducing-the-generative-ai-maturity-model/ | 26 Sep 2023 | full (stage names only) |
| SPICY-2026 | UK professional services AI adoption (Professional Services AI Adoption Curve) | Spicy Advisory | vendor blog | https://spicyadvisory.com/blog/uk-professional-services-ai-adoption | 15 Mar 2026 (page also shows items dated later) | full; **low reliability: statistics attributed to the Law Society, ICAEW and PwC UK could not be verified, so none are used** |
| LAWSOC-GENAI | Generative AI: the essentials (includes a checklist for generative AI use) | The Law Society of England and Wales | professional-body guidance | https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials | undated (refers to events to January 2025) | full |
| ICAEW-GOV-2026 | AI governance: 10 essential questions for responsible adoption | ICAEW | professional-body guidance | https://www.icaew.com/technical/technology/artificial-intelligence/managing-risks/ai-governance-10-essential-questions-for-responsible-adoption | 3 Jul 2026 | full |
| ROGERS-WIKI | Diffusion of innovations | Wikipedia (summarizing E. Rogers) | reference summary (foundations) | https://en.wikipedia.org/wiki/Diffusion_of_innovations | accessed 2026-10-16 | full |
| CMMI-WIKI | Capability Maturity Model | Wikipedia (summarizing SEI work) | reference summary (foundations) | https://en.wikipedia.org/wiki/Capability_Maturity_Model | accessed 2026-10-16 | full |

Count: 40 distinct source documents (39 read in full, partially or as a reproduction; 1 search-only, McKinsey). Gartner's primary pages were blocked and are represented through two secondary reproductions. AWSCAF-2024 and MSFT-CAF-2026 were read but are capability frameworks without stage markers, so they are not cited in the body. Types: academic or academic-sponsored (MIT CISR, Lichtenthaler, Sadiq, MIT NANDA, Wharton, HBS, NBER, Stanford, MIT SMR); consultancy and analyst (BCG, Gartner, Deloitte, Accenture, KPMG, McKinsey); vendor research or guidance (Microsoft x3, Anthropic x3, Cisco, AWS, Prosci, TR x2); professional-services vendor models (Litify, IR Global/Clio, Sage, Fieldguide, UpLevel Ops, Spicy Advisory); professional-body guidance (Law Society, ICAEW); polling and industry-survey reporting (Gallup, ILTA via Law360); opinion (CBA/"National"); foundations (Rogers, CMMI).

---

## 10. Gaps

- **Primary sources not reached.** Gartner's own AI maturity model and toolkit (403); McKinsey State of AI 2025 (connection failure; figures E30 are search-only); Cisco's own index page (403); PwC agent survey (403); ABA Formal Opinion 512 (403); Clio's Legal Trends Report 2025 (403); legaltechnology.com SKILLS 2025 survey (bot check); Law Society of Western Australia survey (404 on the file I tried). Gartner's levels are therefore described through a secondary blog and may be out of date.
- **Search budget ran out mid-task.** The shared web-search limit was used up before I could search for: ICAEW and ACCA/AICPA/CIMA maturity or adoption research; SRA and Law Society adoption surveys; Microsoft's AI Business School maturity model; IDC, Forrester and Info-Tech AI maturity models; IBM, EY, PwC and Capgemini adoption studies; Davenport's and Moore's classic works. Some professional-body pages were read by direct URL (ICAEW, Law Society), but no accounting-body maturity model (ICAEW, ACCA, AICPA, CIMA) was found.
- **No books or talks.** The brief asks for books and practitioner talks. None were read. Book-level sources (Davenport, Mollick, Moore, Rogers' original text) were represented only through Wikipedia summaries for foundations (Rogers, CMMI). Practitioner case write-ups are limited to vignettes inside MIT CISR, BCG and Prosci.
- **Professional-body maturity models are thin.** The only professional-body items are governance guidance (ICAEW) and a risk checklist (Law Society), not stage models. Every professional-services stage model found is vendor- or opinion-originated (Litify, Sage, Fieldguide, IR Global/Clio, UpLevel Ops, Spicy). The accounting/audit models published by Fieldguide describe six autonomy levels, but the level names and markers were not in the blog post and I did not find the framework document.
- **No longitudinal or validated stage transition data.** I found no study following the same organizations through the stages. BCG gives two annual distributions (E3) but does not say they are the same firms. Time-to-production figures (BCG; MIT NANDA) are survey- or interview-based and directional.
- **No team-level or individual-level validated stage model.** Individual segmentation is Microsoft's (E19), self-reported by users, with a vendor sponsor. The Anthropic AI fluency framework is a skills model, not a stage model, and I read only the curriculum outline.
- **Agentic-stage markers are thin.** Only BCG (prerequisites, agent value share), Deloitte (governance) and KPMG (deployment rate) speak to agents. None gives stage markers for "delegate the outcome" at the team level.
- **"AI-native" is not operationalized for professional services by any independent source.** The markers I give for AI-native are drawn from MIT CISR stage 4, Lichtenthaler level 4, Sage stage 4 and BCG's future-built practices.
- **Date gaps.** Deloitte 2026 and Thomson Reuters 2026 pages carry no publication date I could find. Accenture's page is undated. The Anthropic fluency page is undated.
- **Conflicting or loosely worded figures.** Prosci states its 63% as organizations in one place and 56%-64% of challenges in another. KPMG's summary page says 55% piloting agents while the deck's internal trend line shows 57% for Q3 (I did not use the piloting figure). BCG's 60% laggards equals stagnating plus emerging (14% + 46%). MIT NANDA's executive summary states 95% of organizations get zero return while the exhibit measures 5% of custom or task-specific tools reaching production; I report both with their definitions.
- **Proposed items are untested.** Everything marked `[P]` (the Curious-versus-Experimenting cut, the reuse discriminator for Adopting versus Scaling, the scope split, exit criteria, leading indicators) needs review with practitioners, ideally against two or three real engagements before shipping.
