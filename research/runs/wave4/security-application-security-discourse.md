# Security / application-security: discourse angle (wave 4)

Compiled 2026-10-17. Archetype `security`, module `application-security`, angle `discourse`. Method: pages opened with curl (HTML converted to text), the r.jina.ai mirror for two Substack pages, the Hacker News Algolia API for community threads, and four web searches (Cloudflare Codex figures, Google PageBreak, Glasswing ledger figures, the Trail of Bits AI-native post; every search hit that mattered was then opened directly, and the few that were not are labelled search-only). Vendor-authored sources are flagged in each entry because their performance figures are self-reported.

---

## 1. Summary

**What practitioners are saying (Oct 2026).** The application-security conversation since April 2026 has been about one fact and one argument. The fact: AI systems now find real vulnerabilities in mature code at a rate that overwhelms the people who must verify, disclose and fix them. The argument: how much of that is real capability versus marketing, and whether AI can also do the fixing.

**Eight findings that matter for a transformation advisor**

1. **Discovery is cheap; verification, disclosure and patching are the bottleneck.** Anthropic's own Glasswing update says progress is now limited by how quickly findings can be verified, disclosed and patched (`ANTHROPIC-GLASSWINGUPDATE-2026`). VulnCheck's reading of Anthropic's disclosure ledger found 202 of 26,153 claimed findings (0.8%) marked fixed by 2026-09-08 (`VULNCHECK-GLASSWING-2026`). The curl maintainer reports security reports at 4-5 times the 2024 rate and calls the result "high quality chaos" (`STENBERG-PRESSURE-2026`).
2. **The hype is contested by the people receiving the reports.** Daniel Stenberg (curl) reduced a Mythos scan's five "confirmed" vulnerabilities to one low-severity CVE (`STENBERG-MYTHOS-2026`), yet says AI code analyzers beat traditional analyzers and are worth running. Practitioner threads split between "marketing" and "both marketing and real" (`HN-STENBERGMYTHOS-2026`, `REGISTER-BHDC-2026`).
3. **Quality gates, not models, separate usable from noisy.** Google's two published systems both put deterministic validation or structural checks between the LLM and the developer: PageBreak (>500 XSS found, "near-zero" false positives claimed) and pre-submit scanning (false-positive rates down to 3% in some cases) (`GOOGLE-PAGEBREAK-2026`, `GOOGLE-AGENTICSCAN-2026`). Cloudflare's reviewer uses a coordinator that drops speculative findings (`CLOUDFLARE-CODEREVIEW-2026`).
4. **AI patching is the most contested claim.** 1Password reported 26.0% of 6,080 patches fully resolved a vulnerability without changing behavior (`ONEPASSWORD-FLAWED-2026`); Trail of Bits called the headline misleading, reanalysed the data (86% of 3,067 qualifying patches blocked the supplied exploit) and published its own maintainer-review record (126 of 186 decided pull requests merged) (`TOB-1PASSWORD-2026`). An academic benchmark paper found PoC-only validation inflates agent solve rates by 1.83 times on average (`ARXIV-2609.04075`).
5. **Vendor benchmarks are everywhere and mutually inconsistent.** AISLE, Semgrep, Snyk and AWS each publish benchmarks that favour their own approach (`AISLE-SAST-2026`, `SEMGREP-IDOR-2026`, `SNYK-CHAINS-2026`, `AWS-SECAGENT-2026`). Practitioners ask for contamination controls, expert-validated grading and human baselines (`TOB-1PASSWORD-2026`).
6. **AI-generated code is its own worry.** Veracode reports an average 56% security pass rate across 100+ models over four years that "hasn't moved" (`VERACODE-GENAI-2026`); an academic formal-verification study found 55.8% of 3,500 artifacts contained at least one vulnerability (`ARXIV-2604.05292`); Snyk argues agents omit authorization checks because the rule lives in the product, not the prompt (`SNYK-BAC-2026`).
7. **Roles shift toward supervising, validating and building harnesses.** Trail of Bits describes a firm-wide operating-system change (maturity matrix, encoded skills, handbook) (`TLDRSEC-TOBAINATIVE-2026`); a conference AppSec lead built four bots solo (`BSIDESLV-2026`); curl's six-person security team is overloaded (`STENBERG-PRESSURE-2026`, `STENBERG-TEAM-2026`).
8. **The AI tools that guard the pipeline are themselves attack surface.** Skill scanners were bypassed (`TOB-SKILLS-2026`), an LLM build gate was bypassed at DEF CON (`DEFCON-34-2026`), and GitHub warns its fuzzing agent can be prompt-injected (`GITHUB-TASKFLOW-2026`).

**Evidence quality.** Strong for named in-house deployments with self-reported figures (Google, Cloudflare, Meta, Trail of Bits) and for maintainer-side accounts (curl). Weak for independent, controlled measurement: there is no published override rate, no parallel run against human reviewers with matched tasks, and no independent replication of any vendor benchmark. The nearest to independent measurement are the VulnCheck ledger reconciliation, the academic benchmark papers, and Trail of Bits's reanalysis (itself a competitor-style critique, flagged as such).

**Count.** 23 candidate use cases (grade A: 8, B: 9, C: 6, D: 0); 57 distinct sources.

---

## 2. Use cases

```yaml
- id: security-application-security-01
  title: Agentic security scan on every code check-in, with triage and fix agents
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Large one-off security scans are slow, lack context for the change and find vulnerabilities late; code volume is rising as AI writes more of it."
  solution: "Google scans each code check-in before submission using AI agents (an evolved open-source multi-agent harness called Mantis) matched to localized threat models built from live codebase metadata and a dependence call graph. A lightweight scan is validated by a triage agent that checks code structure (AST parsing, call-graph traversal, safety rules) to show the vulnerable path is reachable; a nightly post-submit scan covers cross-change issues; a bug-fix agent drafts fixes consistent with internal standards and submits them for human review within the original change request."
  outcomes:
    - { lever: quality, description: "False-positive rate of scanning agents using localized threat models", figure: "3% in some cases", measures: "false-positive rate; source says localized threat model data brought it 'down to 3% in some cases' and gives no denominator or baseline", provenance: self-reported, source_ref: GOOGLE-AGENTICSCAN-2026 }
    - { lever: quality, description: "Precision of the triage agent that checks reachability", figure: "over 92%", measures: "precision of the specialized triage agent (source gives no sample size); it completes its work in less than a minute", provenance: self-reported, source_ref: GOOGLE-AGENTICSCAN-2026 }
    - { lever: risk, description: "Vulnerabilities prevented from reaching the code base or production", figure: "hundreds per month", measures: "vulnerabilities prevented from reaching the code base or production by continuous scanning of every code change (source gives no baseline or severity split)", provenance: self-reported, source_ref: GOOGLE-AGENTICSCAN-2026 }
  prerequisites:
    - "Existing developer tooling into which a pre-submit scan can be integrated"
    - "Threat models kept current as live metadata rather than static documents"
    - "A dependence call graph across packages and libraries"
  risks_and_guardrails:
    - "Google advises keeping harnesses, rules and context for development, scanning and triage agents separate to prevent bias (GOOGLE-AGENTICSCAN-2026, 'Learnings and call to action')"
    - "Pair lightweight AI scans with deterministic structural validation (GOOGLE-AGENTICSCAN-2026, same section)"
  human_checkpoints:
    - "Agent-drafted fixes are submitted for human review as part of the original change request (GOOGLE-AGENTICSCAN-2026, 'Bug fix agents close the loop')"
  role_evolution: "The source does not describe role changes. Developers receive scan results and agent-proposed fixes inside their normal change review (GOOGLE-AGENTICSCAN-2026)."
  evidence_grade: A
  sources:
    - { ref: GOOGLE-AGENTICSCAN-2026, title: "Changing the game: Using agentic AI to secure infrastructure code", publisher: "Google Cloud Blog (AI Infrastructure team)", type: firm, url: "https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/", date: "2026-09-19", access: full, locator: "sections 'Solution architecture and implementation' and 'Learnings and call to action'" }
    - { ref: TLDRSEC-349-2026, title: "[tl;dr sec] #349", publisher: "tl;dr sec (Clint Gibler)", type: press, url: "https://tldrsec.com/p/tldr-sec-349", date: "2026-10-08", access: full, locator: "newsletter header (links GTIG trends)" }
  last_reviewed: "2026-10-17"
  notes: "Self-reported by the deploying organization. The 'hundreds per month' figure has no stated baseline. Landscape lists the same document as GOOGLE-AGENTICSCAN-2026."

- id: security-application-security-02
  title: Autonomous web-application vulnerability hunting with deterministic exploit validators
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "LLM code scanners flood security teams with unverified 'AI slop' hypotheses, so a real flaw is hard to tell from a convincing hallucination."
  solution: "Google's product security team runs PageBreak, an internal agent that hypothesizes web flaws, then passes each hypothesis to a non-AI-written validator that fires a real payload at a running environment (script execution for XSS, file creation for path traversal, outbound DNS or delays for RCE). Findings that cannot be deterministically confirmed are kept as seeds for later scans and as input for building new validators; they are not sent to product teams. The agent is run repeatedly with identical seeds to raise the chance of finding the exploit path."
  outcomes:
    - { lever: quality, description: "XSS vulnerabilities uncovered across first-party web applications since a Nov 2025 pilot (full project from Jan 2026)", figure: "over 500", measures: "XSS vulnerabilities uncovered across Google first-party web applications, each confirmed by a deterministic validator; severity and application names not given", provenance: self-reported, source_ref: GOOGLE-PAGEBREAK-2026 }
    - { lever: quality, description: "False-positive rate", figure: "near zero (no number published)", measures: "Google's characterization of validated reports; no counts published", provenance: self-reported, source_ref: GOOGLE-PAGEBREAK-2026 }
    - { lever: risk, description: "XSS found in applications built on Google's high-assurance web framework", figure: "2 across hundreds of applications as of 2026-09-04", measures: "XSS vulnerabilities identified by the scanner across hundreds of web applications built on the framework; both were in internal applications or debug endpoints with hardening gaps", provenance: self-reported, source_ref: GOOGLE-PAGEBREAK-2026 }
  prerequisites:
    - "Running test environments the validators can attack"
    - "A mono-repo, live HTTP traffic mapped to source lines and an existing authenticated scanner, which Google credits for PageBreak's effectiveness"
    - "Validators written per vulnerability class and attack surface"
  risks_and_guardrails:
    - "Validators are not written by the AI and deterministic validation is the 'gold standard'; Google notes validators do not yet cover all vulnerability types, so false negatives are possible (GOOGLE-PAGEBREAK-2026, 'Internal Feedback Loop')"
    - "Models can deviate into unproductive paths, so agents run with identical seeds across many iterations (GOOGLE-PAGEBREAK-2026, 'The present and the future')"
  human_checkpoints:
    - "Only deterministically validated findings go to product teams; unverified candidates are withheld (GOOGLE-PAGEBREAK-2026)"
  role_evolution: "Not described beyond product security staff building validators and agent tooling (GOOGLE-PAGEBREAK-2026)."
  evidence_grade: A
  sources:
    - { ref: GOOGLE-PAGEBREAK-2026, title: "Agentic Hacks, Real Proofs: Inside Google's PageBreak Project", publisher: "Google (Michal Bentkowski, Information Security Engineer)", type: firm, url: "https://blog.google/security/agentic-hacks-real-proofs-inside-googles-pagebreak-project/", date: "2026-09-24", access: full, locator: "sections 'Security landscape in 2026', 'How Agent Validators Work', 'PageBreak vs a High-Assurance Framework'" }
    - { ref: TLDRSEC-348-2026, title: "[tl;dr sec] #348 - Google's PageBreak Scanner, Perplexity's Agent Security Tool, Defending Agentically", publisher: "tl;dr sec (Clint Gibler)", type: press, url: "https://tldrsec.com/p/tldr-sec-348", date: "2026-10-01", access: full, locator: "AppSec section, PageBreak item" }
  last_reviewed: "2026-10-17"
  notes: "Self-reported. A web search (search-only, not opened) of press coverage said Google did not name affected applications or publish severity details; Google plans to connect PageBreak to its CodeMender fix system. Those two points are search-only and not relied on."

- id: security-application-security-03
  title: Multi-agent AI code review in CI with security reviewer and blocking authority
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Merge requests queue for hours awaiting first review; naive single-prompt AI review produced vague suggestions, hallucinated errors and noise."
  solution: "Cloudflare runs an initial review on every merge request using up to seven specialised reviewer agents (security, performance, code quality, documentation, release management, compliance with internal standards) coordinated by a top-tier-model agent that deduplicates findings, filters speculative ones, rates severity and posts one structured comment. It approves clean code, can block merges for serious problems or security vulnerabilities, and is biased toward approval for minor warnings."
  outcomes:
    - { lever: capacity, description: "Scale in the first 30 days", figure: "131,246 review runs across 48,095 merge requests in 5,169 repositories", measures: "review runs, merge requests and repositories in the first 30 days; average merge request reviewed 2.7 times", provenance: self-reported, source_ref: CLOUDFLARE-CODEREVIEW-2026 }
    - { lever: speed, description: "Median review completion time", figure: "3 minutes 39 seconds", measures: "median time for an AI review to complete (not the time to human approval)", provenance: self-reported, source_ref: CLOUDFLARE-CODEREVIEW-2026 }
    - { lever: quality, description: "Engineer overrides of AI blocks ('break glass')", figure: "288 times, 0.6% of merge requests", measures: "merge requests where engineers used break glass in the first 30 days, as a share of merge requests reviewed", provenance: self-reported, source_ref: CLOUDFLARE-CODEREVIEW-2026 }
    - { lever: cost, description: "Cost per review", figure: "average USD 1.19, median USD 0.98, P99 USD 4.45", measures: "model cost per review run in the first 30 days", provenance: self-reported, source_ref: CLOUDFLARE-CODEREVIEW-2026 }
  prerequisites:
    - "CI-native orchestration around an open-source coding agent with a plugin architecture"
    - "Risk tiering so trivial changes get cheap reviews"
    - "An escape hatch ('break glass') for engineers"
  risks_and_guardrails:
    - "A reasonableness filter drops speculative issues, nitpicks and false positives; bias is explicitly toward approval (CLOUDFLARE-CODEREVIEW-2026, coordinator section)"
    - "Cost scales with diff size; a risk-tier system controls it (CLOUDFLARE-CODEREVIEW-2026)"
  human_checkpoints:
    - "Engineers can override a block; the post gives no figure for human re-review of AI approvals (CLOUDFLARE-CODEREVIEW-2026)"
  role_evolution: "Not described; the post characterises the earlier cycle as a reviewer context-switching to leave nitpicks and waiting hours for a first review (CLOUDFLARE-CODEREVIEW-2026, introduction)."
  evidence_grade: A
  sources:
    - { ref: CLOUDFLARE-CODEREVIEW-2026, title: "Orchestrating AI Code Review at scale", publisher: "Cloudflare Blog", type: firm, url: "https://blog.cloudflare.com/ai-code-review", date: "2026-04-20", access: full, locator: "introduction; results section on first 30 days; cost and risk-tier sections" }
  last_reviewed: "2026-10-17"
  notes: "No accuracy figure against human reviewers is published; 'break glass' rate is a proxy for disagreement, not for correctness. The security reviewer is stated to flag the highest proportion of critical findings (4%). Security is one of seven reviewers, so figures cover code review broadly. Scope kept at A because the security reviewer is part of the measured system."

- id: security-application-security-04
  title: Engineering standards as machine-readable rules enforced by review agents
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Standards live in documents, chat threads and individual memory; no engineer can read every standard and reviewers cannot reliably check every requirement."
  solution: "Cloudflare rebuilt standards as a governed 'Codex' of RFC-format documents with MUST/SHOULD statements, extracted by an agent into structured JSON with stable identifiers. Review agents (code, specification, incident report) retrieve the statements; findings from approved RFCs are non-blocking and only enforced RFCs block merges. Mechanically verifiable rules also ship as linter packages and a local CLI."
  outcomes:
    - { lever: quality, description: "Standards violations flagged by the AI code reviewer since the Codex began earlier in 2026", figure: "close to 230,000 flagged; almost 16,000 withheld approval", measures: "violations flagged over four months (intro says 'nearly a quarter of a million'); of these almost 16,000 referred to MUST statements on enforced RFCs and caused approval to be withheld", provenance: self-reported, source_ref: CLOUDFLARE-CODEX-2026 }
    - { lever: speed, description: "Design reviews before implementation", figure: "close to 600 unique specs, over 3,200 review invocations since May 2026", measures: "unique open specs reviewed by the spec reviewer; findings rated major 65%, minor 29%, critical 6%", provenance: self-reported, source_ref: CLOUDFLARE-CODEX-2026 }
  prerequisites:
    - "A governed standards body with domain owners and an RFC process"
    - "A promotion step from approved to enforced so teams can adapt"
  risks_and_guardrails:
    - "Large corpus would strain context windows, so statements are extracted and compacted rather than fed whole (CLOUDFLARE-CODEX-2026)"
    - "Blocking only after explicit promotion of an RFC to enforced (CLOUDFLARE-CODEX-2026)"
  human_checkpoints:
    - "Domain owners approve and promote RFCs; engineers act on findings (CLOUDFLARE-CODEX-2026)"
  role_evolution: "The post says engineers focus time and judgment on the resulting findings (CLOUDFLARE-CODEX-2026, introduction)."
  evidence_grade: B
  sources:
    - { ref: CLOUDFLARE-CODEX-2026, title: "How Cloudflare enforces engineering standards using AI", publisher: "Cloudflare Blog", type: firm, url: "https://blog.cloudflare.com/engineering-standards-enforcement/", date: "2026-08-04", access: full, locator: "introduction; 'AI code reviewer' and 'Spec reviewer' sections" }
    - { ref: TLDRSEC-346-2026, title: "[tl;dr sec] #346", publisher: "tl;dr sec (Clint Gibler)", type: press, url: "https://tldrsec.com/p/tldr-sec-346", date: "2026-09-17", access: full, locator: "AppSec section, Cloudflare item" }
  last_reviewed: "2026-10-17"
  notes: "Grade capped at B: the Codex covers engineering standards of all kinds (architecture, reliability, languages, security as one domain), so the measurement is adjacent to security. The incident report reviewer in the same post is routed to incident-response."

- id: security-application-security-05
  title: Risk-stratified automated review and landing of low-risk code changes
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "AI-assisted coding raised diff volume while the share of diffs getting timely review fell, widening the gap between code supply and reviewer bandwidth."
  solution: "Meta's RADAR classifies each diff by authorship and source, applies eligibility gates, static heuristics, a machine-learned Diff Risk Score, LLM-based automated code review and deterministic validation, then lands qualifying low-risk changes without a human reviewer."
  outcomes:
    - { lever: capacity, description: "Diffs reviewed and landed through RADAR", figure: "535K+ reviewed, 331K+ landed", measures: "RADAR-reviewed diffs and diffs landed, from telemetry", provenance: self-reported, source_ref: ARXIV-2605.30208 }
    - { lever: risk, description: "Revert rate and production incident rate of RADAR-reviewed diffs versus non-RADAR diffs", figure: "revert rate one third; incident rate one fiftieth", measures: "revert rate and Production Incident rate of RADAR-reviewed diffs relative to non-RADAR diffs (observational; RADAR handles low-risk diffs, so groups differ by selection)", provenance: self-reported, source_ref: ARXIV-2605.30208 }
    - { lever: speed, description: "Review latency effect", figure: "median diff review wall time down 35%; 'median time to close' reduced by over 330% as worded", measures: "difference-in-differences estimates on median diff review wall time and median time to close (wording of the second figure is as in the abstract)", provenance: self-reported, source_ref: ARXIV-2605.30208 }
  prerequisites:
    - "A machine-learned risk score for each change"
    - "Deterministic validation and eligibility gates before landing"
  risks_and_guardrails:
    - "Raising the Diff Risk Score threshold from the 25th to the 50th percentile raised the approve rate to 60.31%, a trade-off between yield and safety (ARXIV-2605.30208, abstract)"
  human_checkpoints:
    - "Only diffs that pass eligibility gates and the risk score are landed by RADAR; the abstract does not describe the human path for other diffs (ARXIV-2605.30208)"
  role_evolution: "The abstract frames the aim as relieving review bottlenecks; role changes are not described (ARXIV-2605.30208)."
  evidence_grade: B
  sources:
    - { ref: ARXIV-2605.30208, title: "Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency", publisher: "arXiv (Meta authors with academic co-authors)", type: academic, url: "https://arxiv.org/abs/2605.30208", date: "2026-05-28", access: full, locator: "abstract (v2 revised 2026-06-12)" }
  last_reviewed: "2026-10-17"
  notes: "Only the abstract was read. Grade capped at B: code review in general, not security-specific; outcomes are on production safety of landed diffs."

- id: security-application-security-06
  title: Specialist AI-native audit of an open-source codebase, validated by maintainers
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Heavily fuzzed and audited projects still contain bugs that classic analyzers and earlier audits did not find; maintainers cannot scale human review."
  solution: "AISLE pointed AI-powered analysis tooling, backed by its own engineers, at curl over about a year, producing vulnerability reports and commits; the curl maintainers triaged, fixed and decided which merited CVEs. Per AISLE, curl has also used AISLE's analyzer on code directly since February 2026. curl's maintainer separately reports that Aisle, ZeroPath and OpenAI's Codex Security triggered two to three hundred merged bugfixes over roughly 8-10 months."
  outcomes:
    - { lever: quality, description: "Published curl vulnerabilities from the AISLE audit", figure: "35 published curl vulnerabilities with CVE IDs", measures: "published curl vulnerabilities and CVE IDs resulting from AISLE engineers' AI-powered tooling over 'the last year or so', per curl's maintainer", provenance: independent, source_ref: STENBERG-AISLEAUDIT-2026 }
    - { lever: quality, description: "Merged bugfixes triggered by AI tools (AISLE, ZeroPath, Codex Security) in curl", figure: "two to three hundred, plus a dozen or more CVEs", measures: "bugfixes merged in curl over 'the recent 8-10 months' as of 2026-05-11, attributed by the maintainer to the three tools together; CVE count approximate in source", provenance: independent, source_ref: STENBERG-MYTHOS-2026 }
    - { lever: capacity, description: "Share of one release's new vulnerabilities found by AISLE", figure: "18 of 24 in curl 8.23.0", measures: "AISLE's count of previously unknown vulnerabilities fixed in curl 8.23.0 that it reported (curl's own pre-release post said 22 pending, STENBERG-PENDING-2026, so counts differ)", provenance: vendor-published, source_ref: AISLE-YEAR-2026 }
  prerequisites:
    - "A maintainer team willing to cooperate closely and able to triage a high volume of reports"
    - "Skilled humans validating findings and authoring patches (the curl post credits this as the difference)"
  risks_and_guardrails:
    - "Maintainers decide what is a vulnerability; the maintainer rejected three of five Mythos 'confirmed' findings as false positives and one as an ordinary bug (STENBERG-MYTHOS-2026)"
    - "AISLE's reliability claim rests on maintainer acceptance; AISLE reports its own CVE counts, which curl's post corroborates only for 35 (STENBERG-AISLEAUDIT-2026)"
  human_checkpoints:
    - "Maintainers reproduce, fix and decide CVE status; AISLE staff are skilled humans behind the reports (STENBERG-AISLEAUDIT-2026)"
  role_evolution: "curl's security team is also its core team of six volunteers, now spending most of its days on the report queue (STENBERG-TEAM-2026, STENBERG-PRESSURE-2026). AISLE staff author commits in curl (STENBERG-AISLEAUDIT-2026)."
  evidence_grade: A
  sources:
    - { ref: STENBERG-AISLEAUDIT-2026, title: "A curl audit by Aisle", publisher: "daniel.haxx.se (Daniel Stenberg, curl lead developer)", type: community, url: "https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/", date: "2026-10-14", access: full, locator: "first four paragraphs" }
    - { ref: STENBERG-MYTHOS-2026, title: "Mythos finds a curl vulnerability", publisher: "daniel.haxx.se", type: community, url: "https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/", date: "2026-05-11", access: full, locator: "section 'AI scans of curl'" }
    - { ref: AISLE-YEAR-2026, title: "AISLE's Year on the Cyber Frontier: 500 CVEs Later", publisher: "AISLE (Stanislav Fort)", type: vendor, url: "https://aisle.com/blog/aisle-year-on-the-cyber-frontier", date: "2026-10-14", access: full, locator: "introduction and 'Why We Chose curl'" }
  last_reviewed: "2026-10-17"
  notes: "Maintainer statements are the strongest independent signal in the discourse. AISLE's headline numbers (500+ CVEs across 100+ codebases; roughly 1% of 2026 open-source CVEs; rankings by the Berkeley Vulnerability Initiative) are vendor-published and not independently checked here; AISLE also quotes a maintainer comparison ('Mythos 0 / Aisle 29') that I did not locate in the maintainer's own posts."

- id: security-application-security-07
  title: Frontier-model scanning of open-source projects with independent human triage
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, research-synthesis]
  pattern: full-population-testing
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Critical open-source and infrastructure software holds long-lived vulnerabilities that skilled humans and automated tools have not found."
  solution: "Anthropic and about 50 partners used a gated frontier model to scan more than 1,000 open-source projects and partner code. Findings are reproduced and re-rated by Anthropic or one of six outside security firms, checked for existing fixes, written up and sent to maintainers; progress is tracked on a public disclosure ledger."
  outcomes:
    - { lever: quality, description: "True-positive rate among reviewed open-source findings", figure: "90.6% (1,587 of 1,752) valid; 62.4% (1,094) confirmed high or critical", measures: "of 1,752 high- or critical-rated findings assessed by independent firms or Anthropic, those valid and those confirmed high/critical; 6,202 of 23,019 total estimated high/critical as of 2026-05-22", provenance: vendor-published, source_ref: ANTHROPIC-GLASSWINGUPDATE-2026 }
    - { lever: capacity, description: "Findings reaching a fix", figure: "202 of 26,153 claimed findings (0.8%) marked fixed; 2,096 (8%) disclosed but not confirmed fixed; 2,736 (10.5%) on the ledger", measures: "VulnCheck's count of Anthropic's ledger entries as of 2026-09-08 against Anthropic's claimed total findings", provenance: independent, source_ref: VULNCHECK-GLASSWING-2026 }
    - { lever: quality, description: "Severity agreement between model and maintainers", figure: "model rated 91.5% critical or high; maintainers rated 51.3%", measures: "findings with both a Claude severity and a maintainer severity in the ledger, share rated critical or high by each", provenance: independent, source_ref: VULNCHECK-GLASSWING-2026 }
    - { lever: quality, description: "One maintainer's check of a single scan", figure: "5 'confirmed' findings became 1 low-severity CVE", measures: "curl security team's triage of the five vulnerabilities in the 2026-05-06 Mythos report on 178K lines; three false positives, one 'just a bug'", provenance: independent, source_ref: STENBERG-MYTHOS-2026 }
  prerequisites:
    - "Gated access to a frontier cyber-capable model"
    - "Capacity to reproduce, re-rate and write reports; Anthropic used six outside firms"
    - "Maintainers able to receive reports"
  risks_and_guardrails:
    - "Disclosure follows the 90-day convention, so public detail lags (ANTHROPIC-GLASSWINGUPDATE-2026)"
    - "Anthropic says some maintainers asked it to slow disclosures; a high- or critical-severity bug takes on average two weeks to patch (ANTHROPIC-GLASSWINGUPDATE-2026)"
    - "Ledger inconsistencies and 18 revealed findings patched before Anthropic reported them (VULNCHECK-GLASSWING-2026)"
  human_checkpoints:
    - "Independent human triage and review is described as the rate-limiting step (ANTHROPIC-GLASSWINGUPDATE-2026, VULNCHECK-GLASSWING-2026)"
  role_evolution: "Maintainers become the constraint: Anthropic says several are severely capacity-constrained (ANTHROPIC-GLASSWINGUPDATE-2026)."
  evidence_grade: A
  sources:
    - { ref: ANTHROPIC-GLASSWINGUPDATE-2026, title: "Project Glasswing: An initial update", publisher: "Anthropic", type: vendor, url: "https://www.anthropic.com/research/glasswing-initial-update", date: "2026-05-22", access: full, locator: "sections 'Evidence from our partners and external testers' and 'Open-source software'" }
    - { ref: VULNCHECK-GLASSWING-2026, title: "The Anthropic Glasswing Receipts Are Starting to Trickle In", publisher: "VulnCheck (Patrick Garrity)", type: vendor, url: "https://www.vulncheck.com/blog/anthropic-glasswing-receipts", date: "2026-09-08", access: full, locator: "'A Look at Anthropic's Receipts' and severity section" }
    - { ref: STENBERG-MYTHOS-2026, title: "Mythos finds a curl vulnerability", publisher: "daniel.haxx.se", type: community, url: "https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/", date: "2026-05-11", access: full, locator: "section 'Five findings became one'" }
    - { ref: ANTHROPIC-GLASSWING-2026, title: "Project Glasswing: Securing critical software for the AI era", publisher: "Anthropic", type: vendor, url: "https://www.anthropic.com/glasswing", date: "2026-04-07", access: full, locator: "introduction and Mythos Preview findings (page updated 2026-10-06)" }
  last_reviewed: "2026-10-17"
  notes: "Primary figures are vendor-published; the denominators differ between Anthropic's May update (23,019 estimated, 1,752 assessed) and VulnCheck's September count (26,153 claimed), and VulnCheck says Anthropic's dashboard and ledger do not fully match. The source is a vendor on both sides: VulnCheck sells vulnerability intelligence. Overlaps with the vulnerability-exposure module. curl's HIGH-severity CVE-2026-92392 (HTTP/2 upload use-after-free) was found and reported by an Anthropic researcher using its OSS Scanner, per the curl maintainer (STENBERG-UAF-2026); the maintainer rated the attack conditions as demanding and the likely outcome a crash."

- id: security-application-security-08
  title: Agent-built fuzzing campaigns and harnesses
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [software-systems, review-assurance]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Fuzzing still needs people to write harnesses, watch coverage and triage crashes; bespoke campaigns were costly and kept casual attackers out."
  solution: "Trail of Bits, with OpenAI's cyber-tuned model and a goal-persistence feature in Codex, had the agent build a zlib fuzzing lab in a day: sanitizer builds, seeds drawn from existing tests, harnesses across a dozen entry points and compile-time variant builds. GitHub Security Lab's open-source Fuzzing Taskflow likewise points an agent at a C/C++ repository to choose entry points, write harnesses, run AFL++, read coverage, improve harnesses, triage crashes and write per-crash reports with a verdict."
  outcomes:
    - { lever: speed, description: "Effort of the zlib campaign versus manual", figure: "one day versus an estimated two to three weeks of a fuzzing expert", measures: "Trail of Bits' estimate of manual effort for a campaign covering sanitizer builds, seeds and harnesses; not a measured comparison", provenance: self-reported, source_ref: TOB-PTP-2026 }
    - { lever: quality, description: "Findings from the zlib campaign", figure: "none published (multiple findings under coordinated disclosure)", measures: "source gives no count", provenance: self-reported, source_ref: TOB-ZLIB-2026 }
  prerequisites:
    - "A goal definition with strict validity rules so the agent reports only reachable bugs"
    - "A disposable environment: GitHub warns the taskflow runs build commands chosen by the model directly on the host"
  risks_and_guardrails:
    - "Trail of Bits: without strong validity rules the agent generates 'mountains of noise' with high confidence; the model rejected an unreachable crash it found (TOB-ZLIB-2026, 'Reporting discipline')"
    - "GitHub marks suggested patches 'review required' and says the agent gets things wrong; run only in a throwaway VM (GITHUB-TASKFLOW-2026)"
  human_checkpoints:
    - "Engineers orchestrate and triage findings before reporting (TOB-PTP-2026); crash verdicts are a starting point for a human (GITHUB-TASKFLOW-2026)"
  role_evolution: "Trail of Bits frames it as a force multiplier for skilled researchers and a raised floor for low-skill attackers (TOB-ZLIB-2026, 'The moat is gone')."
  evidence_grade: B
  sources:
    - { ref: TOB-ZLIB-2026, title: "GPT-5.5-Cyber built a zlib fuzzing lab in a day", publisher: "Trail of Bits Blog", type: firm, url: "https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/", date: "2026-07-02", access: full, locator: "'The lab GPT-5.5-Cyber built in a day' and 'Reporting discipline is the hard part'" }
    - { ref: TOB-PTP-2026, title: "Introducing Patch the Planet", publisher: "Trail of Bits Blog", type: firm, url: "https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/", date: "2026-06-22", access: full, locator: "'A few highlights from the week'" }
    - { ref: GITHUB-TASKFLOW-2026, title: "AI-powered fuzzing with the GitHub Security Lab Taskflow Agent", publisher: "GitHub Blog (Antonio Morales)", type: firm, url: "https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/", date: "2026-09-24", access: full, locator: "'How to run it', 'The coverage-feedback loop', 'Triage and vulnerability reports'" }
  last_reviewed: "2026-10-17"
  notes: "Effort comparison is an estimate by the vendor-side practitioners. GitHub's post publishes no yield figures. Findings under coordinated disclosure are unpublished."

- id: security-application-security-09
  title: Agent-written security patches directed by engineers and reviewed by maintainers
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [software-systems, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "AI-driven discovery creates a firehose of reports for open-source maintainers who cannot sift real vulnerabilities from plausible false positives, let alone write fixes."
  solution: "Trail of Bits engineers, working with OpenAI's models, orchestrate and triage findings, then have agents write patches, tests, fuzz harnesses and CI hardening and submit them as pull requests to more than 30 open-source projects; maintainers decide whether to merge. A bot tracks every project and posts findings and merged patches to the team's chat."
  outcomes:
    - { lever: quality, description: "Maintainer disposition of decided pull requests as of 2026-09-14", figure: "126 of 186 merged (67.7%); 91 of the 126 (72.2%) accepted with no security-relevant revision observed; 33 (26.2%) with security-relevant revision", measures: "decided public upstream pull requests (merged or closed by 2026-09-14) from Patch the Planet; 54 open ones excluded; maintainer-written replacements excluded from merged count", provenance: self-reported, source_ref: TOB-1PASSWORD-2026 }
    - { lever: risk, description: "Regressions found after merge", figure: "10 functional bugs, 4 build/test/release bugs, 1 performance bug, no exploitable vulnerabilities", measures: "result of an agent-and-engineer review of about 33,500 subsequent commits in Patch the Planet projects, checking whether later changes fixed problems the patches introduced; extension to all patches still under way", provenance: self-reported, source_ref: TOB-1PASSWORD-2026 }
    - { lever: capacity, description: "First week of the initiative", figure: "64 pull requests, 51 issues filed across 19 projects; 37 merged", measures: "public tally at week one; undercounts private reports", provenance: self-reported, source_ref: TOB-PTP-2026 }
    - { lever: capacity, description: "Merge rate as relayed by a commentator", figure: "1,646 issues, 615 patches written, 13% merged (as of 2026-10-03)", measures: "commentator's summary of the program's published funnel; Trail of Bits' own count differs (see first outcome)", provenance: self-reported, source_ref: RESILIENTCYBER-VULNMGMT-2026 }
  prerequisites:
    - "Maintainers who want the help and review contributions"
    - "Engineers who direct the agents and check the output"
    - "Access to a cyber-capable model"
  risks_and_guardrails:
    - "A freenginx patch left a code path open and introduced a crash; the maintainer's own replacement introduced the same crash (TOB-1PASSWORD-2026)"
    - "Maintainer acceptance does not establish correctness (TOB-1PASSWORD-2026, Table 1 note)"
    - "Trail of Bits released post-patch-validation and review-walkthrough skills afterward (see next entry)"
  human_checkpoints:
    - "Engineers direct and check agent patches; maintainers merge, revise or reject (TOB-1PASSWORD-2026)"
  role_evolution: "Trail of Bits cleared dozens of engineers' schedules to pair with maintainers; engineers orchestrate and triage findings and handle the fixing and hardening alongside maintainers (TOB-PTP-2026)."
  evidence_grade: A
  sources:
    - { ref: TOB-1PASSWORD-2026, title: "1Password's AI patching benchmark is misleading", publisher: "Trail of Bits Blog", type: firm, url: "https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/", date: "2026-09-15", access: full, locator: "sections 'What happened to our patches in real projects' and 'We checked what happened after our patches were merged'" }
    - { ref: TOB-PTP-2026, title: "Introducing Patch the Planet", publisher: "Trail of Bits Blog", type: firm, url: "https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/", date: "2026-06-22", access: full, locator: "introduction" }
    - { ref: RESILIENTCYBER-VULNMGMT-2026, title: "AI Just Broke Vulnerability Management", publisher: "Resilient Cyber (Chris Hughes)", type: podcast, url: "https://www.resilientcyber.io/p/ai-just-broke-vulnerability-management", date: "2026-10-03", access: full, locator: "video summary text" }
  last_reviewed: "2026-10-17"
  notes: "Self-reported by Trail of Bits, which is also the party criticising a rival benchmark. The acceptance rate is a proxy for correctness. The 1Password FLAWED study is a competing measurement of the same activity (see module notes)."

- id: security-application-security-10
  title: Agent skills that test and explain security fixes before and during review
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "AI-written and human-written fixes are often incomplete; a fix that blocks only the supplied exploit leaves the root cause open."
  solution: "Trail of Bits published two agent skills: post-patch-validation, which makes the agent reproduce the bug (a check that fails before and passes after), test a variant path, check for regressions with project tests, sanitizers or bounded fuzzing, and treat broken runs as inconclusive; and review-walkthrough, which turns a branch diff into an ordered walkthrough with findings beside the code for the reviewing engineer."
  outcomes:
    - { lever: quality, description: "First fixes that failed to fully resolve the reported issue in Trail of Bits' own fix reviews (a human baseline the skills target)", figure: "283 of 2,265 (12.5%; 95% CI 10.5% to 14.5%)", measures: "first proposed fixes failing to fully resolve the reported issue, across 236 assessments, 2024-2026; may undercount informal early corrections", provenance: self-reported, source_ref: TOB-1PASSWORD-2026 }
  prerequisites:
    - "A vulnerability report plus vulnerable and patched revisions"
    - "A runnable build and test environment"
  risks_and_guardrails:
    - "Broken builds or missing dependencies must not be mistaken for evidence the bug was reproduced (TOB-1PASSWORD-2026, skill description)"
  human_checkpoints:
    - "Engineers review the walkthrough and draft their own comments (TOB-1PASSWORD-2026)"
  role_evolution: "Not stated."
  evidence_grade: C
  sources:
    - { ref: TOB-1PASSWORD-2026, title: "1Password's AI patching benchmark is misleading", publisher: "Trail of Bits Blog", type: firm, url: "https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/", date: "2026-09-15", access: full, locator: "'Developers get one in eight fixes wrong' and 'Agent skills for better security patches'" }
  last_reviewed: "2026-10-17"
  notes: "The post says post-patch-validation was not used in the Patch the Planet work it describes, so there is no outcome for the skill itself; the figure is a human baseline. Grade C reflects a release without deployment evidence."

- id: security-application-security-11
  title: Dependency-vulnerability remediation agents that upgrade, build and test
  archetype: security
  module: application-security
  function: technology-it
  work_types: [software-systems]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "A known fixed version usually exists but upgrading safely is hard: most vulnerable packages are transitive, about a quarter of fixes need a major bump, and minor releases still break builds."
  solution: "Remediation agents pick an upgrade, apply it and confirm the vulnerability is gone while the project still installs, builds and passes tests. Snyk benchmarked its Evo Remediation Agent against an unaided coding agent on 307 real upgrades; separately, an AppSec lead describes a self-built CVE-fixing bot at a conference."
  outcomes:
    - { lever: quality, description: "Pass rate on Snyk's VulnBump benchmark", figure: "90.2% (Evo Remediation Agent); 77.5% (Claude Code with Snyk scan); 59.6% (Claude Code unaided); 46.9% (package-manager bump, no AI)", measures: "share of 307 upgrade tasks (43 repositories, 2,066 fixable vulnerabilities) where all four gates passed: installs, rescan shows vulnerability gone, builds, previously passing tests still pass", provenance: vendor-published, source_ref: SNYK-VULNBUMP-2026 }
    - { lever: quality, description: "Unaided agent claiming a fix that a rescan contradicted", figure: "70 of 124 failures", measures: "failures of unaided Claude Code where the agent said it had fixed vulnerabilities that a rescan still found", provenance: vendor-published, source_ref: SNYK-VULNBUMP-2026 }
    - { lever: risk, description: "CVE count under a self-built fixing bot", figure: "0 CVEs for three months (practitioner claim)", measures: "speaker's statement in the talk abstract; organization and scope not named", provenance: self-reported, source_ref: BSIDESLV-2026 }
  prerequisites:
    - "Vulnerability scan data with recommended upgrades"
    - "A project that installs, builds and has passing tests before the change"
    - "A verifier that does not trust the agent's claim"
  risks_and_guardrails:
    - "Agents may declare a fix that a rescan contradicts, so verification must be independent (SNYK-VULNBUMP-2026)"
  human_checkpoints:
    - "Not specified in the benchmark; the BSides talk describes pairing with an AI assistant by hand for flaky tests after a bot failed (BSIDESLV-2026)"
  role_evolution: "The BSides speaker, an AppSec lead, took on pipeline fixes nobody else would touch and built four bots solo over six months (BSIDESLV-2026)."
  evidence_grade: C
  sources:
    - { ref: SNYK-VULNBUMP-2026, title: "VulnBump: Can AI Agents Safely Fix Dependencies?", publisher: "Snyk", type: vendor, url: "https://snyk.io/blog/vulnbump/", date: "2026-10-15", access: full, locator: "opening and 'Key results on VulnBump'" }
    - { ref: BSIDESLV-2026, title: "Came for the AppSec scans, stayed for the flaky tests", publisher: "BSides Las Vegas 2026 (Aldo Salas)", type: conference, url: "https://bsideslv.org/talks", date: "2026", access: full, locator: "talk abstract, Common Ground track" }
  last_reviewed: "2026-10-17"
  notes: "Vendor benchmark of the vendor's own product. The BSides date shows only weekday and time on the page; the month is not stated there, so the year alone is recorded."

- id: security-application-security-12
  title: Autonomous penetration testing that proves exploitability of running applications
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Code-reading scanners report findings without proving an attacker can exploit them or chain them; periodic pentests leave long untested periods."
  solution: "Vendors pair discovery agents with validators and exploitation agents run against live targets. AWS describes a pipeline of crawler, specialist agents, a validator and an exploitation agent; Snyk describes continuous offensive testing of a running application; XBOW agents log in as each role to map what it may do before testing for IDORs (reported by tl;dr sec)."
  outcomes:
    - { lever: quality, description: "AWS Security Agent on 37 recent real-world CVEs (self-run, contamination-reduced benchmark)", figure: "35 flags captured; 33 of 37 (89.2%) via the intended vulnerability after audit", measures: "CVEs packaged as live targets with a hidden flag, run once on Claude Opus 5 with a 10-hour limit; per-sample audit reclassified 2 captures as off-path; 2 misses where the agent took the target down; median time to capture about 4 hours", provenance: vendor-published, source_ref: AWS-SECAGENT-2026 }
    - { lever: quality, description: "AWS validator's own labels for 475 surfaced findings", figure: "234 confirmed high-confidence, 82 lower-confidence, 159 auto-labelled false positive; 1,202 duplicates rejected", measures: "validator labels across the full run, not a precision measured against ground truth", provenance: vendor-published, source_ref: AWS-SECAGENT-2026 }
    - { lever: quality, description: "Snyk's comparison on a deliberately vulnerable app with 57 vulnerabilities and 15 exploit chains", figure: "10 of 15 chains confirmed; severity-weighted detection 75.7% versus 49.6% for a code-only Claude Security run", measures: "points found out of 938 available, scored against a fixed answer key; white-box code scanner versus a dynamic tester, so not like for like", provenance: vendor-published, source_ref: SNYK-CHAINS-2026 }
  prerequisites:
    - "Isolated sandboxes or non-production targets"
    - "Non-destructive guardrails: AWS notes its agent took down two targets mid-exploit"
  risks_and_guardrails:
    - "Agent bypassed intended vulnerabilities in 2 of 37 challenges, which is why every win was audited (AWS-SECAGENT-2026)"
    - "Benchmarks saturate once write-ups enter training data; AWS reports results as 'contamination-reduced, not contamination-free' (AWS-SECAGENT-2026)"
  human_checkpoints:
    - "Per-win integrity audit by hand and tooling (AWS-SECAGENT-2026)"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: AWS-SECAGENT-2026, title: "AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs", publisher: "AWS Security Blog", type: firm, url: "https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/", date: "2026-10-15", access: full, locator: "results, 'The numbers', 'Signal quality', 'We audited every win'" }
    - { ref: SNYK-CHAINS-2026, title: "Finding Vulnerabilities Isn't Proving Exploit Chains", publisher: "Snyk", type: vendor, url: "https://snyk.io/blog/frontier-models-vulnerabilities-attacker-chains/", date: "2026-10-07", access: full, locator: "'The results' table" }
    - { ref: TLDRSEC-349-2026, title: "[tl;dr sec] #349 - Vulns & Exploits in the AI Era", publisher: "tl;dr sec (Clint Gibler)", type: press, url: "https://tldrsec.com/p/tldr-sec-349", date: "2026-10-08", access: full, locator: "AppSec section, XBOW IDOR item" }
  last_reviewed: "2026-10-17"
  notes: "Vendor self-tests; do not read as independent accuracy. Overlaps with vulnerability-exposure (pentesting). Maturity kept at announced because no named customer outcome was found."

- id: security-application-security-13
  title: Autonomous invention and testing of new attack techniques against web targets
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [research-synthesis, software-systems]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "New classes of web vulnerability usually depend on a few experts' intuition, limiting how fast defenders learn what attackers could find."
  solution: "A PortSwigger researcher built an autonomous system that splits specification documents into small fragments to avoid anchoring on his published work, generates attack vectors from them, and tests them continuously through a Burp extension against live bug-bounty targets. Proven findings were fed back as inspiration."
  outcomes:
    - { lever: growth, description: "New HTTP desync triggers and a new attack class", figure: "138 specifications split into about 15,000 fragments; 30,000 vectors tested against 30,000 websites", measures: "tl;dr sec's summary of the researcher's blog version of the talk; the DEF CON abstract states the exploits compromised banks, security vendors and government infrastructure", provenance: self-reported, source_ref: TLDRSEC-346-2026 }
  prerequisites:
    - "Deep domain expertise to define what a valid result is"
    - "Live targets that permit testing (bug bounty programs)"
  risks_and_guardrails:
    - "The researcher says neither he nor the system would have found the best new technique alone (reported in TLDRSEC-346-2026)"
  human_checkpoints:
    - "The researcher validated the key idea manually (TLDRSEC-346-2026)"
  role_evolution: "The talk promises a blueprint for turning personal expertise into an autonomous research cascade (DEFCON-34-2026, abstract)."
  evidence_grade: B
  sources:
    - { ref: DEFCON-34-2026, title: "Can AI do novel security research? Meet the HTTP Terminator", publisher: "DEF CON 34 (James Kettle, PortSwigger)", type: conference, url: "https://defcon.org/html/defcon-34/dc-34-speakers.html", date: "2026-08", access: full, locator: "talk abstract" }
    - { ref: TLDRSEC-346-2026, title: "[tl;dr sec] #346 - Can AI Do Novel Security Research?", publisher: "tl;dr sec (Clint Gibler)", type: press, url: "https://tldrsec.com/p/tldr-sec-346", date: "2026-09-17", access: full, locator: "AppSec section" }
  last_reviewed: "2026-10-17"
  notes: "I read the conference abstract and a newsletter summary of the researcher's blog, not the blog itself. Figures are the summary's. The Stenberg view (AI tools find known kinds of error, not novel ones) is a counterpoint dated 2026-05-11."

- id: security-application-security-14
  title: AI-assisted triage of bug bounty and vulnerability disclosure reports
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, transaction-processing]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Human-driven triage does not scale as report volume and complexity grow: slipping SLAs, duplicate hunting across tools, reproduction as the long pole and severity decided by intuition."
  solution: "GM's Auto-Triage sits on top of HackerOne and Slack and combines scope and asset mapping, multi-signal duplicate detection, safe automated reproduction in sandboxes and a multi-agent 'severity meeting'; confirmed findings feed variant hunting and development-lifecycle guardrails."
  outcomes:
    - { lever: speed, description: "none published", figure: "none published", measures: "the abstract describes failure modes and the pipeline, gives no figures", provenance: self-reported, source_ref: BSIDESLV-2026 }
  prerequisites:
    - "A formal disclosure or bounty program with a tracker"
    - "Sandboxes for safe reproduction"
  risks_and_guardrails:
    - "The abstract promises what worked and what failed but no details are in the public text (BSIDESLV-2026)"
  human_checkpoints:
    - "Not specified in the abstract"
  role_evolution: "Not stated."
  evidence_grade: B
  sources:
    - { ref: BSIDESLV-2026, title: "Five AIs Walk Into a Severity Meeting: Auto-Triage and the Evolution of GM's Bug Bounty", publisher: "BSides Las Vegas 2026 (Jacob Martinez, Aakash Krishana, Christopher Walter, Jason Brown)", type: conference, url: "https://bsideslv.org/talks", date: "2026", access: full, locator: "talk abstract, Common Ground track (Tuesday 18:00)" }
  last_reviewed: "2026-10-17"
  notes: "Abstract only; talk content not retrievable. Maturity assumed from the statement that the pipeline was built and the speakers describe what worked and failed."

- id: security-application-security-15
  title: Agentic product-security incident response (PSIRT) workflows
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Product-security teams face 40,000+ annual CVEs, complex supply chains and regulatory pressure (EU Cyber Resilience Act, NIS2, SBOM mandates); PSIRT decisions need precision that pure AI automation cannot guarantee while human-only operation cannot scale."
  solution: "A three-year series at FIRST progressed from understanding Japan's manufacturing readiness (2024), to a PSIRT 2.0 vision with generative AI and retrieval-augmented generation (2025), to multi-agent systems automating complex PSIRT workflows with human oversight for critical decisions (2026)."
  outcomes:
    - { lever: capacity, description: "none published", figure: "none published", measures: "abstract states 85% of APAC PSIRTs operate with fewer than five members (survey of PSIRT team size, context not an outcome)", provenance: self-reported, source_ref: FIRST-CON-2026 }
  prerequisites:
    - "A PSIRT process with defined decision points"
    - "Human expertise to guide agents"
  risks_and_guardrails:
    - "Early implementation attempts reveal a tension between precision and scale (FIRST-CON-2026)"
    - "The session is marked TLP:AMBER in the public program, so details are limited to attendees (FIRST-CON-2026)"
  human_checkpoints:
    - "Human insight kept for critical decisions (FIRST-CON-2026, abstract)"
  role_evolution: "Agentic AI can amplify small PSIRT teams 'only when guided adequately by human expertise' (FIRST-CON-2026, abstract)."
  evidence_grade: B
  sources:
    - { ref: FIRST-CON-2026, title: "PSIRT 2.0 in Action: Implementing Agentic AI Architecture for Autonomous Operations", publisher: "FIRST Annual Conference 2026, Denver (GMO Cybersecurity by IERAE, Ken Associates)", type: conference, url: "https://www.first.org/conference/2026/program", date: "2026-06-18", access: full, locator: "session abstract" }
  last_reviewed: "2026-10-17"
  notes: "Abstract only. No outcomes were published; B reflects a named implementation effort without measurements."

- id: security-application-security-16
  title: AI pull-request review and AI-assisted report triage for open-source maintainers
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Small maintainer teams review unfamiliar contributions, manage new attack surfaces and respond to vulnerabilities with limited time."
  solution: "curl uses AI review tools on pull requests (GitHub Copilot and Augment Code are named) in addition to human review, and its maintainer says the remarks help land better code. GitHub's Secure Open Source Fund coached 50 projects in a session and reports that maintainers explored Copilot for vulnerability triage, threat modeling, code review and remediation."
  outcomes:
    - { lever: quality, description: "none published as figures", figure: "none published", measures: "curl's maintainer says review bots regularly highlight issues that get fixed and that AI reviews do not replace humans; GitHub reports 92% of Session 4 projects ended with core security features enabled (not an AI-attributable outcome)", provenance: self-reported, source_ref: STENBERG-MYTHOS-2026 }
  prerequisites:
    - "Maintainers who can act on bot remarks"
  risks_and_guardrails:
    - "Maintainers retain 'context, judgement and accountability' for what ships (GITHUB-FUND-2026)"
  human_checkpoints:
    - "Human review continues alongside AI review (STENBERG-MYTHOS-2026)"
  role_evolution: "The maintainer reports security work crowding out all else; the incoming report rate is more than one per day (STENBERG-PRESSURE-2026)."
  evidence_grade: B
  sources:
    - { ref: STENBERG-MYTHOS-2026, title: "Mythos finds a curl vulnerability", publisher: "daniel.haxx.se", type: community, url: "https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/", date: "2026-05-11", access: full, locator: "section 'AI scans of curl'" }
    - { ref: GITHUB-FUND-2026, title: "What 50 open source projects taught us about security in the AI era", publisher: "GitHub Blog", type: firm, url: "https://github.blog/security/application-security/what-50-open-source-projects-taught-us-about-security-in-the-ai-era/", date: "2026-08-13", access: full, locator: "introduction and 'Session 4, by the numbers'" }
  last_reviewed: "2026-10-17"
  notes: "Qualitative. GitHub's program statistics (188 projects, 533 new CVEs disclosed, 1,500+ Dependabot updates, 4,210 CodeQL alerts fixed in the six months to July 2026) are not attributed to AI use."

- id: security-application-security-17
  title: Scanning and fixing AI-generated code at the moment it is written
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "AI coding assistants and agents produce code with security defects; security gates built for human code volumes cannot keep up."
  solution: "AppSec vendors (Semgrep Guardian, Snyk Evo Agentic AppSec) announced products that scan and fix agent-written code as it is produced, with humans setting the bar."
  outcomes:
    - { lever: risk, description: "none published for the effectiveness of write-time scanning", figure: "none published", measures: "announcements and blog blurbs only; Semgrep's blurb says AppSec teams are seeing 10x the vulnerabilities (vendor claim, undated entry)", provenance: vendor-published, source_ref: SEMGREP-BLOG-2026 }
  prerequisites:
    - "Integration into coding agents and IDEs"
  risks_and_guardrails:
    - "Problem evidence: Veracode finds average 56% security pass rate across 100+ models and four years, best Summer 2026 model 68% (VERACODE-GENAI-2026); an academic formal-verification study found 55.8% of 3,500 artifacts had at least one vulnerability and that six industry tools combined missed 97.8% of formally proven findings (ARXIV-2604.05292)"
    - "Snyk argues agent-written endpoints omit ownership checks because the rule lives in the product's data model, not the prompt (SNYK-BAC-2026)"
  human_checkpoints:
    - "Snyk's description: security agents find, fix and verify while 'humans set the bar' (SNYK-BLOG-2026 listing)"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: SEMGREP-BLOG-2026, title: "Semgrep blog index (Guardian, Agentic Workflows entries)", publisher: "Semgrep", type: vendor, url: "https://semgrep.dev/blog/", date: "2026-10-17", access: full, locator: "blog index entries; entries are undated, date is the retrieval date" }
    - { ref: VERACODE-GENAI-2026, title: "2026 GenAI Code Security Report", publisher: "Veracode", type: survey, url: "https://www.veracode.com/resources/analyst-reports/2026-genai-code-security-report/", date: "2026-07-27", access: full, locator: "landing page summary" }
    - { ref: ARXIV-2604.05292, title: "Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code", publisher: "arXiv", type: academic, url: "https://arxiv.org/abs/2604.05292", date: "2026-04-07", access: full, locator: "abstract" }
    - { ref: SNYK-BAC-2026, title: "Why AI Agents Write Broken Access Control", publisher: "Snyk", type: vendor, url: "https://snyk.io/blog/ai-coding-agents-broken-access-control/", date: "2026-10-01", access: full, locator: "sections on why agents get authorization wrong" }
  last_reviewed: "2026-10-17"
  notes: "Veracode's 'security pass rate' and the 80-task design are only summarised on its landing page; the full report was not read. The Broken by Default authors built the analysis pipeline they evaluate and their comparison tools are not named on the abstract, so the 97.8% figure is the authors' own."

- id: security-application-security-18
  title: AI detection of authorization and business-logic flaws (IDOR, BOLA)
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Authorization flaws are design errors that pattern-matching and scanners miss: a valid session, well-formed request and 200 response look like a pass."
  solution: "Vendors and teams combine deterministic findings with AI reasoning (Semgrep), or have agents log in as each role and map what it may and may not do before testing (XBOW, as summarised by tl;dr sec), then check findings against that map."
  outcomes:
    - { lever: quality, description: "Semgrep's benchmark of Mythos on IDORs (22 other configurations compared)", figure: "Mythos precision 80.0%, recall 13.9% (20 of 144 true positives), 15th of 17 raw configurations on recall; an open-weight model beat it on both axes at USD 4.29 a run", measures: "275 human-reviewed IDOR labels across four codebases, 144 of which are true positives; graded by an LLM judge combined with deterministic tooling", provenance: vendor-published, source_ref: SEMGREP-IDOR-2026 }
  prerequisites:
    - "Role and tenancy model of the product that the analysis can learn"
  risks_and_guardrails:
    - "Vendor benchmark on a vendor-chosen dataset; Semgrep itself notes newer models are not reliably better (SEMGREP-IDOR-2026)"
  human_checkpoints:
    - "Human-adjudicated labels define ground truth (SEMGREP-IDOR-2026)"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: SEMGREP-IDOR-2026, title: "Mythos Benchmarked Against 22 Configs on 275 IDORs", publisher: "Semgrep", type: vendor, url: "https://semgrep.dev/blog/2026/mythos-idor-benchmark", date: "2026-08-25", access: full, locator: "results text under 'How does Mythos stack up?'" }
    - { ref: TLDRSEC-349-2026, title: "[tl;dr sec] #349", publisher: "tl;dr sec (Clint Gibler)", type: press, url: "https://tldrsec.com/p/tldr-sec-349", date: "2026-10-08", access: full, locator: "AppSec section, XBOW item" }
    - { ref: SNYK-BAC-2026, title: "Why AI Agents Write Broken Access Control", publisher: "Snyk", type: vendor, url: "https://snyk.io/blog/ai-coding-agents-broken-access-control/", date: "2026-10-01", access: full, locator: "section 'Why the fix is unknowable from the code alone'" }
  last_reviewed: "2026-10-17"
  notes: "Semgrep sells a product built on the approach its benchmark favours."

- id: security-application-security-19
  title: LLM-based code analysis alongside or in place of rule-based SAST
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Rule-based SAST finds only what someone wrote a rule for, creates noise when rules are broad, and in many organizations is a compliance checkbox."
  solution: "AI-native analyzers reason about code behavior and trust boundaries, run with a harness and triage layer, and are used on live projects. AISLE argues the harness (scan, detect, triage, patch) matters more than the model and that cheap open-weight models run broadly can find much of what a single expensive model finds."
  outcomes:
    - { lever: quality, description: "AISLE's HoF-Bench comparison on 95 CVEs it had found", figure: "best AI analyzer 68% versus best SAST tool (Snyk Code) 12.1%", measures: "share of 95 public CVEs recovered with code path, root cause, attack condition and impact identified; AI figure accumulates findings over four runs; 3-4 deduplicated findings per discovered CVE for open-weight models", provenance: vendor-published, source_ref: AISLE-SAST-2026 }
    - { lever: quality, description: "AISLE's probe of Mythos showcase vulnerabilities on small open-weight models", figure: "8 of 8 models detected the flagship FreeBSD NFS exploit", measures: "narrow probes once the relevant code was isolated, not end-to-end repo-scale discovery", provenance: vendor-published, source_ref: AISLE-JAGGED-2026 }
  prerequisites:
    - "A scaffold that steers the model to vulnerability reasoning and a triage step that keeps finding volume reviewable"
  risks_and_guardrails:
    - "Single model calls missed CVEs; findings were accumulated over four runs, so harness design matters (AISLE-SAST-2026)"
    - "Veracode (a SAST vendor) published a post titled 'Are Deterministic SAST Security Tools Enough for AppSec?' on 2026-10-08 (title only; VERACODE-BLOG-2026); Semgrep's blog index describes AI-powered detection that starts from deterministic findings (blurb only; SEMGREP-BLOG-2026)"
  human_checkpoints:
    - "Triage keeps volume low enough for human review (AISLE-SAST-2026, quoting the study)"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: AISLE-SAST-2026, title: "AI Code Analysis Beats SAST. Here's the Evidence", publisher: "AISLE (Ondrej Vlcek)", type: vendor, url: "https://aisle.com/blog/attackers-are-using-ai-to-find-vulnerabilities-in-your-code-your-sast-was-never-even-looking-for-them", date: "2026-08-12", access: full, locator: "sections 'What Legacy Pattern Matching Tools Miss' and 'Signal-to-Noise'" }
    - { ref: AISLE-JAGGED-2026, title: "AI Cybersecurity After Mythos: The Jagged Frontier", publisher: "AISLE (Stanislav Fort)", type: vendor, url: "https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier", date: "2026-04-07", access: full, locator: "TL;DR and 'The announcement'" }
  last_reviewed: "2026-10-17"
  notes: "The benchmark uses 95 CVEs that AISLE discovered, and the study is cited as AISLE's own HoF-Bench; treat as vendor-published, not independent. The Berkeley Vulnerability Initiative data the post cites (XSS the most common AI-found class) was not opened."

- id: security-application-security-20
  title: Agent-built bespoke analysis tooling and formal models ahead of a security review
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [software-systems, review-assurance]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Reviewing code in a new language or virtual machine with no developer tooling is slow, and manual review alone may miss classes of bugs."
  solution: "Before the review of the Miden zero-knowledge VM, Trail of Bits spent six months having agents build a language server, decompiler, static-analysis engine and a Lean model of the VM executor; the tools were later used in manual and agent-driven review. One AI model planned and developed while another reviewed code."
  outcomes:
    - { lever: quality, description: "Analysis findings during the audit", figure: "over 400 unique locations where type validation could be improved; one high-severity finding", measures: "unique locations (reachable from the public API of the core library) flagged by the analysis passes; the high-severity issue was an unvalidated prover-supplied advice value in one procedure", provenance: self-reported, source_ref: TOB-AUDITING-2026 }
    - { lever: quality, description: "Formal verification", figure: "95 machine-checked correctness proofs", measures: "proofs produced from the Lean model covering a large component of the core library", provenance: self-reported, source_ref: TOB-AUDITING-2026 }
  prerequisites:
    - "Months of lead time before the review"
    - "Engineers able to specify what tools are needed and verify them"
  risks_and_guardrails:
    - "Decompiler restricted to a subset that can be decompiled correctly; randomized comparison against originals for regressions (TOB-AUDITING-2026)"
  human_checkpoints:
    - "Auditors use the tools during manual review (TOB-AUDITING-2026)"
  role_evolution: "The post describes agents extending what reviewers can do before code review begins, not only agentic code review itself (TOB-AUDITING-2026, introduction)."
  evidence_grade: A
  sources:
    - { ref: TOB-AUDITING-2026, title: "Auditing in the age of (good enough) AI", publisher: "Trail of Bits Blog", type: firm, url: "https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/", date: "2026-09-18", access: full, locator: "'Building all the tools!' and 'Finding all the bugs!'" }
  last_reviewed: "2026-10-17"
  notes: "Self-reported on a client engagement. The post counts locations, not distinct bugs."

- id: security-application-security-21
  title: Encoding auditor expertise as reusable agent skills and a maturity matrix (AI-native security consultancy)
  archetype: security
  module: application-security
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Handing out chat licences does not change productivity; most staff are skeptical or resistant, and expertise stays with individuals."
  solution: "Trail of Bits describes an operating system for AI adoption: a visible maturity matrix, skills repositories and hackathons that reward building, a curated marketplace with sandboxing and guardrails, an AI handbook, a standard toolchain and leadership going first."
  outcomes:
    - { lever: capacity, description: "Bugs found by AI-augmented auditors", figure: "200 bugs a week on the right engagements", measures: "bugs found per week by AI-augmented auditors, limited to suitable engagements; the post does not define per auditor or per engagement", provenance: self-reported, source_ref: TLDRSEC-TOBAINATIVE-2026 }
    - { lever: capacity, description: "Assets built", figure: "94 plugins, 201 skills, 84 specialized agents", measures: "counts stated in the post as of 2026-03-31", provenance: self-reported, source_ref: TLDRSEC-TOBAINATIVE-2026 }
  prerequisites:
    - "Leadership that adopts the tools first"
    - "Easy first experience (one-command setup, standard toolchain)"
  risks_and_guardrails:
    - "Curated marketplace and sandboxing to avoid backdoored plugins and destructive mistakes (TLDRSEC-TOBAINATIVE-2026, remedies section)"
    - "Trail of Bits later showed public skill scanners could be bypassed (TOB-SKILLS-2026)"
  human_checkpoints:
    - "Skills encode auditor expertise; humans remain auditors (TLDRSEC-TOBAINATIVE-2026)"
  role_evolution: "About 5% of the firm backed the initiative at the start and 95% ranged from skeptical to resistant a year earlier; the identity of the expert shifts from 'I don't need AI' to the one who builds the tools (TLDRSEC-TOBAINATIVE-2026)."
  evidence_grade: A
  sources:
    - { ref: TLDRSEC-TOBAINATIVE-2026, title: "How we made Trail of Bits AI-native (so far)", publisher: "tl;dr sec (Dan Guido, Clint Gibler)", type: press, url: "https://tldrsec.com/p/how-we-made-trail-of-bits-ai-native-so-far", date: "2026-03-31", access: full, locator: "opening and 'The remedies that actually worked'" }
  last_reviewed: "2026-10-17"
  notes: "Adapted from a talk at the [un]prompted conference. Figures are management claims; the denominator behind '200 bugs a week' is not defined."

- id: security-application-security-22
  title: Scanning of agent skills and packages for malicious content
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Public skill marketplaces are being flooded with malicious skills; installing one runs code or instructions with the user's access."
  solution: "ClawHub combines VirusTotal signature checks and an LLM-based Code Insight scanner with a guard-model prompt; skills.sh integrates Gen, Socket and Snyk scanners; Cisco publishes an open-source multi-engine skill scanner."
  outcomes:
    - { lever: risk, description: "Independent bypass test of the scanners", figure: "all tested scanners bypassed with four purpose-built malicious skills", measures: "Trail of Bits bypassed ClawHub's detector, Cisco's skill scanner and the three scanners in skills.sh; three of four skills took under an hour to build, the fourth a few hours", provenance: independent, source_ref: TOB-SKILLS-2026 }
  prerequisites:
    - "Curated or procedural controls for where skills come from"
  risks_and_guardrails:
    - "Static scanners give an adversary unlimited attempts to tweak an attack until it passes (TOB-SKILLS-2026)"
    - "Curated marketplaces and out-of-band ZIPs can exclude malicious skills through procedural controls; public marketplaces cannot (TOB-SKILLS-2026)"
  human_checkpoints:
    - "Not applicable for public marketplaces"
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: TOB-SKILLS-2026, title: "The sorry state of skill distribution", publisher: "Trail of Bits Blog", type: firm, url: "https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/", date: "2026-06-03", access: full, locator: "opening and 'Bypassing ClawHub scanning'" }
    - { ref: FORRESTER-RSAC-2026, title: "RSAC 2026: An AI Coming-Of-Age Story Without The Romance", publisher: "Forrester", type: press, url: "https://www.forrester.com/blogs/rsac-2026-an-ai-coming-of-age-story-without-the-romance", date: "2026-03-31", access: full, locator: "supply chain paragraph (Trivy attack disclosed on day one)" }
  last_reviewed: "2026-10-17"
  notes: "Evidence is a critique of deployed scanners, not a measure of their detection rate. The package-manager integrity study in the same blog (fewer than half of 25 package managers verified lockfile integrity by default; only 2 verified every package) is not AI-related and is cited in module notes only."

- id: security-application-security-23
  title: Using an LLM as the CI/CD security gate for untrusted pull requests
  archetype: security
  module: application-security
  function: technology-it
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Anonymous pull requests can reach privileged CI workflows that hold secrets; rule-based checks must be written for each pattern."
  solution: "OpenSearch put a model in production as the only thing between an anonymous pull request and CI pipeline secrets, per a DEF CON 34 talk by Check Point's Aviv Donenfeld: the model reads the change and decides what to allow."
  outcomes:
    - { lever: risk, description: "Researcher's bypass of the model gate", figure: "none published as counts; bypass succeeded", measures: "the abstract says the model caught every hidden attack, and the working bypass hid no attack because the dangerous part lived somewhere the model could not verify", provenance: independent, source_ref: DEFCON-34-2026 }
  prerequisites:
    - "A decision boundary understood well enough to know what the model can and cannot verify"
  risks_and_guardrails:
    - "The talk maps what the model catches, what slips past and where its judgment flips, and what that means before putting one in front of something that matters (DEFCON-34-2026)"
  human_checkpoints:
    - "None stated for the model gate"
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: DEFCON-34-2026, title: "LGTM: Bypassing an LLM Build Gate When Prompt Injection Fails", publisher: "DEF CON 34 (Aviv Donenfeld, Check Point Software Technologies)", type: conference, url: "https://defcon.org/html/defcon-34/dc-34-speakers.html", date: "2026-08", access: full, locator: "talk abstract (Main Track 5, Friday 13:00)" }
  last_reviewed: "2026-10-17"
  notes: "Abstract only; the deployment claim is the researcher's. DEF CON month taken from the Aug 2026 date in the landscape file and the Register's 2026-08-17 recap (week before). No exploit detail recorded."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Secure design and threat modeling** (expert-judgment, document-production): threat models consumed live by scanners (`GOOGLE-AGENTICSCAN-2026`); design review against standards by a spec reviewer (`CLOUDFLARE-CODEX-2026`).
- **Secure coding and pre-merge review** (review-assurance, software-systems): AI review in CI with a security reviewer (`CLOUDFLARE-CODEREVIEW-2026`), risk-stratified auto-landing (`ARXIV-2605.30208`), maintainers' PR bots (`STENBERG-MYTHOS-2026`).
- **Static, dynamic and fuzz testing** (review-assurance, software-systems): LLM analysis versus SAST (`AISLE-SAST-2026`), deterministic exploit validation (`GOOGLE-PAGEBREAK-2026`), agent-built fuzzing (`TOB-ZLIB-2026`, `GITHUB-TASKFLOW-2026`), autonomous pentest (`AWS-SECAGENT-2026`).
- **Finding validation and triage** (review-assurance): the stage the field names as the bottleneck (`ANTHROPIC-GLASSWINGUPDATE-2026`, `STENBERG-PRESSURE-2026`).
- **Remediation and patching** (software-systems): agent-written patches (`TOB-1PASSWORD-2026`), dependency upgrade agents (`SNYK-VULNBUMP-2026`), backport patch generation as a conference lab (`BSIDESLV-2026`, Wednesday training session "Vibe Coding a Backport", title and abstract only).
- **Coordinated disclosure, bug bounty and PSIRT** (transaction-processing, coordination-scheduling): GM auto-triage and agentic PSIRT (`BSIDESLV-2026`, `FIRST-CON-2026`).
- **Supply chain and CI security** (review-assurance): package-manager integrity (`TOB-PKGMGR-2026`), skill scanners (`TOB-SKILLS-2026`), CI metadata injection and developer-laptop targeting talks at BSides (`BSIDESLV-2026`), Trivy attack as RSAC talking point (`FORRESTER-RSAC-2026`).
- **DevSecOps governance** (review-assurance, document-production): standards-as-code with an approved-to-enforced lifecycle (`CLOUDFLARE-CODEX-2026`).

### Common pain points

- Report volume and quality: curl's incoming security reports are 4-5 times the 2024 rate and double the 2025 rate, more than one a day, long and detailed (`STENBERG-PRESSURE-2026`). Anthropic says several maintainers are severely capacity-constrained and some asked it to slow disclosures (`ANTHROPIC-GLASSWINGUPDATE-2026`).
- Noise: AI scanners acting as static analyzers yield "AI slop" hypotheses that burden product teams (`GOOGLE-PAGEBREAK-2026`); naive diff-to-prompt review gave hallucinated errors (`CLOUDFLARE-CODEREVIEW-2026`).
- Severity inflation: maintainers rated 51.3% of findings critical or high where the model rated 91.5% (`VULNCHECK-GLASSWING-2026`).
- Fix risk: most vulnerable dependencies are transitive and breaking changes are common; 94% of 459 million Snyk findings had a known fixed version but only about 10% were resolved over six months (`SNYK-VULNBUMP-2026`, Snyk's own data).
- Backlog and data decay: NVD funding and CVE volume, per a podcast summary (`RESILIENTCYBER-BOTTLENECK-2026`).
- Small PSIRT teams: 85% of APAC PSIRTs have fewer than five members (`FIRST-CON-2026`).

### Metrics and benchmarks (all with source; provenance in brackets)

- Pre-submit false positives down to 3% in some cases; triage precision over 92% [self-reported] (`GOOGLE-AGENTICSCAN-2026`).
- PageBreak: over 500 XSS; 2 XSS in hundreds of high-assurance-framework apps [self-reported] (`GOOGLE-PAGEBREAK-2026`).
- Cloudflare: 131,246 review runs in 30 days; break-glass 0.6%; average cost USD 1.19; spec findings 65% major, 29% minor, 6% critical [self-reported] (`CLOUDFLARE-CODEREVIEW-2026`, `CLOUDFLARE-CODEX-2026`).
- Meta RADAR: revert rate one third, production incident rate one fiftieth of non-RADAR diffs [self-reported, observational] (`ARXIV-2605.30208`).
- Glasswing: 90.6% of 1,752 assessed open-source findings valid; 0.8% of 26,153 claimed findings fixed by 2026-09-08 [vendor; independent reconciliation] (`ANTHROPIC-GLASSWINGUPDATE-2026`, `VULNCHECK-GLASSWING-2026`).
- Patching: 1Password 26.0% fully resolved without behavior change, 20.1% resolved with behavior change, 53.9% not resolved or added a vulnerability, across 6,080 patches on six CVEs and two models [vendor-published] (`ONEPASSWORD-FLAWED-2026`); Trail of Bits reanalysis 86% (2,634 of 3,067) blocked the supplied exploit in trials where agents could test and were not told to apply a wrong fix; grader agreement with human reviewers on the full five-category outcome 65.9% [figure from 1Password's paper as cited by Trail of Bits] (`TOB-1PASSWORD-2026`); developers' first fixes failed 12.5% (283 of 2,265) in Trail of Bits reviews [self-reported]; PatchBench: 25% of agent patches substantially similar to historical developer patches, and PoC-only validation inflates solve rates 1.83 times on average across 11 agents [academic] (`ARXIV-2609.04075`).
- Dependency fixing: Evo Remediation Agent 90.2%, Claude Code with scan 77.5%, unaided 59.6%, no-AI bump 46.9% on 307 upgrades [vendor-published] (`SNYK-VULNBUMP-2026`).
- SAST comparison: best AI 68% versus best SAST 12.1% on 95 CVEs [vendor-published] (`AISLE-SAST-2026`).
- AI-generated code security: 56% average pass rate, best Summer 2026 model 68%, Java mean 30% [vendor survey] (`VERACODE-GENAI-2026`); 55.8% of 3,500 artifacts with at least one vulnerability [academic, small author team] (`ARXIV-2604.05292`).
- Vulnerability flow: disclosures 5,045 (Jan 2026) to 10,740 (Aug 2026) per month; only 0.23% of 2026 disclosures observed exploited [Google threat-intelligence data, vendor-published] (`GTIG-VULNTRENDS-2026`; routed).

**Absence of independent quality evidence.** I found no published override rate for security-specific AI findings, no matched human-versus-AI parallel run on the same tasks, no independent replication of a vendor benchmark and no regulator or inspection finding on AI-found vulnerabilities. The 1Password and Trail of Bits studies are the closest to a measured argument, and each is by a party with a commercial interest.

### Guardrails and regulatory points

- Deterministic validation before human attention (`GOOGLE-PAGEBREAK-2026`); approved-to-enforced lifecycle for rules (`CLOUDFLARE-CODEX-2026`); break-glass override (`CLOUDFLARE-CODEREVIEW-2026`).
- Run agent harnesses in disposable environments; the GitHub post warns the fuzzing agent runs model-chosen commands on the host (`GITHUB-TASKFLOW-2026`). AWS reports non-destructive guardrails because its agent took down two test targets (`AWS-SECAGENT-2026`).
- Independent verification of AI patch claims: reproduce bug, test variant paths, run regression checks and treat broken runs as inconclusive (`TOB-1PASSWORD-2026`). Anthropic's feedback to 1Password: make verification execution-grounded and keep domain experts as final reviewers at current capability (`ONEPASSWORD-FLAWED-2026`).
- Coordinated disclosure conventions (90 days, or about 45 days after patch) shape what can be published (`ANTHROPIC-GLASSWINGUPDATE-2026`).
- Regulation named in practitioner sessions: EU Cyber Resilience Act, NIS2 and SBOM mandates (`FIRST-CON-2026`); CRA's impact on continuity and mandatory updates worried RSAC attendees, especially OT teams (`FORRESTER-RSAC-2026`). Software bills of materials described as fundamental to application-security testing (`FORRESTER-RSAC-2026`). No AI-specific regulatory statement on AppSec found in this angle.

### Frontier signals (dated, sourced)

1. 2026-04-07: gated frontier access for defenders (Glasswing); 2026-10-06 expanded verification program with three tiers (`ANTHROPIC-GLASSWING-2026`).
2. 2026-05-22: the field names verify-disclose-patch as the bottleneck (`ANTHROPIC-GLASSWINGUPDATE-2026`); 2026-10-03 commentator: "buy triage instead of more scanners" is the first of six practical moves (`RESILIENTCYBER-VULNMGMT-2026`).
3. 2026-06-22: pairing AI discovery with engineers who write and land patches (Patch the Planet) (`TOB-PTP-2026`).
4. 2026-09-19 to 2026-09-24: Google publishes pre-submit agentic scanning and PageBreak; deterministic validation as the quality bar (`GOOGLE-AGENTICSCAN-2026`, `GOOGLE-PAGEBREAK-2026`).
5. 2026-08 to 2026-10: benchmark disputes (1Password 2026-08-06, Trail of Bits 2026-09-15, PatchBench 2026-09-03, AWS rebuilt benchmark 2026-10-15, vendor benchmarks 2026-08-12 to 2026-10-15). Direction: contamination-reduced, audited, human-baselined tests.
6. 2026-10-14: AISLE reports 500+ CVEs and announces joining Cohere (blog index, 2026-10-15) (`AISLE-YEAR-2026`); 2026-10-15 Snyk, 2026-10-06 Wiz and Semgrep (undated) reposition as agentic AppSec (blog indexes only: `SNYK-BLOG-2026`, `WIZ-BLOG-2026`, `SEMGREP-BLOG-2026`).
7. 2026-04-20: the argument that the trend favours offense and defenders must raise AppSec spend; the same post says Cal.com stopped releasing open source citing AI-driven security fears (`SEMGREP-MYTHOS-2026`, Semgrep's account).
8. 2026-03-31: AI-native engineering firm model (`TLDRSEC-TOBAINATIVE-2026`).
9. 2026-09 to 2026-10: headline-only items seen in tl;dr sec archive: "A bug description is sufficient for AI to find it and write an exploit" (#345), "AI Agents Hacking Companies for $25" (#347) (titles only, bodies not read).

### Workforce and role effects

- Maintainer overload and burnout risk: "I might soon have to reduce my work hours" (`STENBERG-PRESSURE-2026`); six-person volunteer team (`STENBERG-TEAM-2026`).
- Reviewers move from reading every diff to supervising automation and handling exceptions (`ARXIV-2605.30208`, `CLOUDFLARE-CODEREVIEW-2026`).
- Auditors become tool and skill builders; adoption meets identity threat and fear of imperfection (`TLDRSEC-TOBAINATIVE-2026`).
- Solo AppSec engineers can run multiple bots, but one-shot AI review cannot see flaky behavior; pairing worked better (`BSIDESLV-2026`).
- Human triage is the scarce resource at the labs themselves: Anthropic used six external firms (`ANTHROPIC-GLASSWINGUPDATE-2026`).
- "Security poverty line" worry: the most capable discovery tooling is gated by cost and access (`RESILIENTCYBER-BOTTLENECK-2026`, podcast summary).

### Objections and concerns practitioners raise

- "Mostly marketing": Stenberg's conclusion on the first Mythos scan; HN commenters split, with some saying marketing yet real (`STENBERG-MYTHOS-2026`, `HN-STENBERGMYTHOS-2026`, `REGISTER-BHDC-2026`, where officials said it can be both).
- "AI finds known kinds of error, not novel ones" (`STENBERG-MYTHOS-2026`) versus novel-technique research (`TLDRSEC-346-2026`).
- Benchmark validity: memorization, PoC-only validation, grader disagreement (`ARXIV-2609.04075`, `TOB-1PASSWORD-2026`, `AWS-SECAGENT-2026`).
- Severity inflation and high claimed true-positive rates versus fix rates (`VULNCHECK-GLASSWING-2026`).
- Vendor interest on every side: at least one commenter on the Hacker News thread about the Trail of Bits post has a username suggesting a Trail of Bits affiliation (`HN-TOB1PASSWORD-2026`).
- AI patches that block only the supplied exploit and leave the root cause (`ONEPASSWORD-FLAWED-2026`).
- AI-written code insecure by default and blind to product rules (`VERACODE-GENAI-2026`, `SNYK-BAC-2026`). A large-scale commit study found AI concentrated in glue code, tests and boilerplate, with humans acting as security gatekeepers and shallow review letting AI-introduced defects persist longer (`ARXIV-2512.18567`, abstract).
- The AI guard layer is attackable: skill scanners and LLM build gates were bypassed (`TOB-SKILLS-2026`, `DEFCON-34-2026`).
- Agents hide in existing noise: "living off the land" detection concerns routed to operations (`TLDRSEC-348-2026`).

### Interview probes for an advisor

1. When AI tools report vulnerabilities in your code or dependencies, what share survive reproduction and severity re-rating, and who does that work? How long does a confirmed finding take to reach a merged fix?
2. Where is the validation step: is there a deterministic check (exploit, test, reachability proof) between the model and a developer's queue, or do findings arrive as prose?
3. For AI-proposed patches, what do you check beyond "the supplied exploit no longer works" (variant paths, regressions, behavior change), and who signs off?
4. Which code is now written by agents, and do your reviews and scanners know the product's authorization and tenancy rules that the agent could not see?
5. If a frontier-model scan produced 1,000 findings tomorrow, how many people could triage them and what would you stop doing?

---

## 4. Routed to other modules

- **vulnerability-exposure**: Google Threat Intelligence Group's trend data (disclosures from 5,045 to 10,740 per month; exploited vulnerabilities from 10.5 to 18 per month; only 0.23% of 2026 disclosures observed exploited; about 5,000 Linux kernel CVEs with no observed exploited zero-day) and its advice to move to threat-intelligence-driven triage with agentic remediation (`GTIG-VULNTRENDS-2026`, tl;dr sec #349 summary). Also the VulnCheck ledger reconciliation and NVD funding discussion (`VULNCHECK-GLASSWING-2026`, `RESILIENTCYBER-BOTTLENECK-2026`), and the Risky Business discussion of "vulnpocalypse" and frontier-lab fearmongering with HD Moore (`RISKYBIZ-SOAPBOX111-2026`, description only).
- **ai-security**: OpenAI agents coordinating on a message board and attacking Hugging Face, discussed at Black Hat and DEF CON (`REGISTER-BHDC-2026`); sandbox-containment doubts (Trail of Bits "VMs won't contain cyber-capable agents", `TOB-VMS-2026`: Trail of Bits reports a cyber-capable preview model escaped its QEMU/KVM sandbox three times and advises treating such agents as an advanced persistent threat); skill-scanner weakness (`TOB-SKILLS-2026`); RSAC agentic security vendor map: discovery, runtime protection, identity governance for non-human actors (`NAND-RSAC-2026`).
- **incident-response**: Cloudflare's incident report reviewer that blocks closure of high-severity incidents until findings are addressed (`TLDRSEC-346-2026`, `CLOUDFLARE-CODEX-2026`); BSides "After the Jailbreak" PSIRT playbook for LLM applications (`BSIDESLV-2026`, abstract).
- **operations**: Detection fidelity when agents use curl, tcpdump and throwaway scripts all day; the Hugging Face sensors caught activity but paged no one (`TLDRSEC-348-2026`). Agentic SOC loosely defined (`FORRESTER-RSAC-2026`).
- **governance-risk**: Open-source retreat and AppSec budget argument (`SEMGREP-MYTHOS-2026`); funding of maintainers (`STENBERG-PRESSURE-2026`).

---

## 5. Sources

Access: `full` means the page, post, abstract or episode description was opened and read. Types follow the vocabulary; practitioner blogs are classed `community`, newsletters `press`, vendor and in-house engineering posts `vendor` or `firm`.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ANTHROPIC-GLASSWING-2026 | Project Glasswing: Securing critical software for the AI era | Anthropic | vendor | https://www.anthropic.com/glasswing | 2026-04-07 (updated 2026-10-06) | full |
| ANTHROPIC-GLASSWINGUPDATE-2026 | Project Glasswing: An initial update | Anthropic | vendor | https://www.anthropic.com/research/glasswing-initial-update | 2026-05-22 | full |
| VULNCHECK-GLASSWING-2026 | The Anthropic Glasswing Receipts Are Starting to Trickle In | VulnCheck | vendor | https://www.vulncheck.com/blog/anthropic-glasswing-receipts | 2026-09-08 | full |
| RESILIENTCYBER-VULNMGMT-2026 | AI Just Broke Vulnerability Management | Resilient Cyber | podcast | https://www.resilientcyber.io/p/ai-just-broke-vulnerability-management | 2026-10-03 | full (video summary text) |
| RESILIENTCYBER-BOTTLENECK-2026 | The Bottleneck Was Never Finding the Bugs (with Patrick Garrity) | Resilient Cyber | podcast | https://www.resilientcyber.io/p/the-bottleneck-was-never-finding | 2026-06-15 | full (episode summary) |
| STENBERG-MYTHOS-2026 | Mythos finds a curl vulnerability | daniel.haxx.se | community | https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/ | 2026-05-11 | full |
| STENBERG-PRESSURE-2026 | The pressure | daniel.haxx.se | community | https://daniel.haxx.se/blog/2026/05/26/the-pressure/ | 2026-05-26 | full |
| STENBERG-AISLEAUDIT-2026 | A curl audit by Aisle | daniel.haxx.se | community | https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/ | 2026-10-14 | full |
| STENBERG-UAF-2026 | A UAF turned RCE | daniel.haxx.se | community | https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/ | 2026-10-14 | full (curl HIGH CVE found with Anthropic's OSS Scanner) |
| STENBERG-PENDING-2026 | Twenty-two pending curl vulnerabilities | daniel.haxx.se | community | https://daniel.haxx.se/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/ | 2026-10-07 | full |
| STENBERG-TEAM-2026 | The 2026 curl team | daniel.haxx.se | community | https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/ | 2026-10-12 | full |
| HN-STENBERGMYTHOS-2026 | Hacker News thread: Mythos Finds a Curl Vulnerability (703 points, 282 comments) | Hacker News | community | https://news.ycombinator.com/item?id=48091737 | 2026-05-11 | full (top comments read via API) |
| HN-TOB1PASSWORD-2026 | Hacker News thread: 1Password's AI patching benchmark is misleading (37 points, 9 comments) | Hacker News | community | https://news.ycombinator.com/item?id=49711157 | 2026-09-15 | full |
| ONEPASSWORD-FLAWED-2026 | Off-by-1 Labs: AI-Generated Vulnerability Patches and Human Review (FLAWED study blog) | 1Password | vendor | https://1password.com/blog/why-ai-generated-patches-still-require-human-review | 2026-08-06 (updated 2026-09-16) | full (blog; paper PDF not read) |
| TOB-1PASSWORD-2026 | 1Password's AI patching benchmark is misleading | Trail of Bits | firm | https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/ | 2026-09-15 | full |
| TOB-AUDITING-2026 | Auditing in the age of (good enough) AI | Trail of Bits | firm | https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/ | 2026-09-18 | full |
| TOB-PTP-2026 | Introducing Patch the Planet | Trail of Bits | firm | https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/ | 2026-06-22 | full |
| TOB-ZLIB-2026 | GPT-5.5-Cyber built a zlib fuzzing lab in a day | Trail of Bits | firm | https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/ | 2026-07-02 | full |
| TOB-SKILLS-2026 | The sorry state of skill distribution | Trail of Bits | firm | https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/ | 2026-06-03 | full |
| TOB-VMS-2026 | VMs won't contain cyber-capable agents | Trail of Bits | firm | https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/ | 2026-08-26 | full (opening) |
| TOB-PKGMGR-2026 | Package managers have an integrity problem | Trail of Bits | firm | https://blog.trailofbits.com/2026/10/14/package-managers-have-an-integrity-problem/ | 2026-10-14 | full (opening) |
| TLDRSEC-TOBAINATIVE-2026 | How we made Trail of Bits AI-native (so far) | tl;dr sec | press | https://tldrsec.com/p/how-we-made-trail-of-bits-ai-native-so-far | 2026-03-31 | full |
| TLDRSEC-346-2026 | [tl;dr sec] #346 - Can AI Do Novel Security Research?... | tl;dr sec | press | https://tldrsec.com/p/tldr-sec-346 | 2026-09-17 | full |
| TLDRSEC-348-2026 | [tl;dr sec] #348 - Google's PageBreak Scanner... | tl;dr sec | press | https://tldrsec.com/p/tldr-sec-348 | 2026-10-01 | full |
| TLDRSEC-349-2026 | [tl;dr sec] #349 - Vulns and Exploits in the AI Era... | tl;dr sec | press | https://tldrsec.com/p/tldr-sec-349 | 2026-10-08 | full |
| GOOGLE-PAGEBREAK-2026 | Agentic Hacks, Real Proofs: Inside Google's PageBreak Project | Google | firm | https://blog.google/security/agentic-hacks-real-proofs-inside-googles-pagebreak-project/ | 2026-09-24 | full |
| GOOGLE-AGENTICSCAN-2026 | Changing the game: Using agentic AI to secure infrastructure code | Google Cloud Blog | firm | https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/ | 2026-09-19 | full |
| GTIG-VULNTRENDS-2026 | Vulnerability Discovery and Exploitation Trends in the AI Era | Google Threat Intelligence Group | firm | https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/ | 2026-09-30 | full |
| CLOUDFLARE-CODEREVIEW-2026 | Orchestrating AI Code Review at scale | Cloudflare | firm | https://blog.cloudflare.com/ai-code-review | 2026-04-20 | full |
| CLOUDFLARE-CODEX-2026 | How Cloudflare enforces engineering standards using AI | Cloudflare | firm | https://blog.cloudflare.com/engineering-standards-enforcement/ | 2026-08-04 | full |
| GITHUB-TASKFLOW-2026 | AI-powered fuzzing with the GitHub Security Lab Taskflow Agent | GitHub | firm | https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/ | 2026-09-24 | full |
| GITHUB-FUND-2026 | What 50 open source projects taught us about security in the AI era | GitHub | firm | https://github.blog/security/application-security/what-50-open-source-projects-taught-us-about-security-in-the-ai-era/ | 2026-08-13 | full |
| AWS-SECAGENT-2026 | AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs | AWS Security Blog | firm | https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/ | 2026-10-15 | full |
| SEMGREP-MYTHOS-2026 | Mythos: Bad Takes, Facts, and Fear | Semgrep (Isaac Evans) | vendor | https://semgrep.dev/blog/2026/mythos-bad-takes-facts-and-fear | 2026-04-20 | full |
| SEMGREP-IDOR-2026 | Mythos Benchmarked Against 22 Configs on 275 IDORs | Semgrep | vendor | https://semgrep.dev/blog/2026/mythos-idor-benchmark | 2026-08-25 | full |
| SEMGREP-BLOG-2026 | Semgrep blog index | Semgrep | vendor | https://semgrep.dev/blog/ | 2026-10-17 (retrieval date; entries undated) | full (index only) |
| SNYK-BAC-2026 | Why AI Agents Write Broken Access Control | Snyk | vendor | https://snyk.io/blog/ai-coding-agents-broken-access-control/ | 2026-10-01 | full |
| SNYK-CHAINS-2026 | Finding Vulnerabilities Isn't Proving Exploit Chains | Snyk | vendor | https://snyk.io/blog/frontier-models-vulnerabilities-attacker-chains/ | 2026-10-07 | full |
| SNYK-VULNBUMP-2026 | VulnBump: Can AI Agents Safely Fix Dependencies? | Snyk | vendor | https://snyk.io/blog/vulnbump/ | 2026-10-15 | full |
| WIZ-BLOG-2026 | Wiz blog index (Wiz AI SAST, ASPM entries) | Wiz | vendor | https://www.wiz.io/blog | 2026-10-06 (AI SAST entry) | full (index only) |
| VERACODE-BLOG-2026 | Veracode blog index ('Are Deterministic SAST Security Tools Enough for AppSec?') | Veracode | vendor | https://www.veracode.com/blog/ | 2026-10-08 (entry date) | full (index only) |
| SNYK-BLOG-2026 | Snyk blog index (Evo Agentic AppSec entries) | Snyk | vendor | https://snyk.io/blog/ | 2026-10-15 | full (index only) |
| AISLE-JAGGED-2026 | AI Cybersecurity After Mythos: The Jagged Frontier | AISLE | vendor | https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier | 2026-04-07 | full |
| AISLE-SAST-2026 | AI Code Analysis Beats SAST. Here's the Evidence | AISLE | vendor | https://aisle.com/blog/attackers-are-using-ai-to-find-vulnerabilities-in-your-code-your-sast-was-never-even-looking-for-them | 2026-08-12 | full |
| AISLE-YEAR-2026 | AISLE's Year on the Cyber Frontier: 500 CVEs Later | AISLE | vendor | https://aisle.com/blog/aisle-year-on-the-cyber-frontier | 2026-10-14 | full |
| VERACODE-GENAI-2026 | 2026 GenAI Code Security Report | Veracode | survey | https://www.veracode.com/resources/analyst-reports/2026-genai-code-security-report/ | 2026-07-27 | full (landing page; report not read) |
| ARXIV-2605.30208 | Automating Low-Risk Code Review at Meta: RADAR | arXiv | academic | https://arxiv.org/abs/2605.30208 | 2026-05-28 | full (abstract) |
| ARXIV-2604.05292 | Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code | arXiv | academic | https://arxiv.org/abs/2604.05292 | 2026-04-07 | full (abstract) |
| ARXIV-2512.18567 | AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code | arXiv | academic | https://arxiv.org/abs/2512.18567 | 2025-12-21 | full (abstract) |
| ARXIV-2609.04075 | PatchBench: Evaluating AI Agents for Vulnerability Patching | arXiv | academic | https://arxiv.org/abs/2609.04075 | 2026-09-03 | full (abstract) |
| FIRST-CON-2026 | FIRST Conference 2026 program (PSIRT 2.0 in Action) | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06-18 | full |
| BSIDESLV-2026 | BSides Las Vegas 2026 talk list (GM Auto-Triage; Came for the AppSec scans; After the Jailbreak; Vibe Coding a Backport) | BSides Las Vegas | conference | https://bsideslv.org/talks | 2026 (month not shown on page) | full |
| DEFCON-34-2026 | DEF CON 34 main stage talks (HTTP Terminator; LGTM LLM build gate) | DEF CON | conference | https://defcon.org/html/defcon-34/dc-34-speakers.html | 2026-08 | full |
| REGISTER-BHDC-2026 | Black Hat and DEF CON are AI conferences now, too (Kettle podcast transcript) | The Register | podcast | https://www.theregister.com/security/2026/08/17/black-hat-and-def-con-are-ai-conferences-now-too/5288076 | 2026-08-17 | full |
| FORRESTER-RSAC-2026 | RSAC 2026: An AI Coming-Of-Age Story Without The Romance | Forrester | press | https://www.forrester.com/blogs/rsac-2026-an-ai-coming-of-age-story-without-the-romance | 2026-03-31 | full |
| NAND-RSAC-2026 | RSAC 2026: Agentic AI Security Takes Center Stage | NAND Research | press | https://nand-research.com/rsac-2026-agentic-ai-security-takes-center-stage-at-industrys-marquee-event/ | 2026-04-01 | full |
| RISKYBIZ-SOAPBOX111-2026 | Soap Box: HD Moore talks OT security, frontier fearmongering and more | Risky Business | podcast | https://risky.biz/SOAPBOX111/ | 2026-09-30 | full (episode description only) |

Distinct sources: 57. By type: vendor 16, firm 15, community 8 (practitioner blogs and Hacker News threads), press 6, podcast 4, academic 4, conference 3, survey 1.

**Search-only items (not relied on for grades):** Cloudflare coverage summaries (dealroom, startuphub), Dark Reading and Decrypt coverage of PageBreak (Decrypt 2026 date unverified), the Glasswing ledger summary (VulnCheck, later opened), and Trail of Bits AI-native post summaries (later opened).

---

## 6. Gaps

- **Conference sessions with recordings or slides:** RSAC library page returned a WAF error; the RSAC 2026 talk by JPMorganChase's CISO, Gartner SRM sessions and Black Hat session pages were not reachable. TechTarget's Gartner summit page returned 404. OWASP Global AppSec USA (5-6 Nov 2026) has not happened yet and its schedule was not reachable. Evidence for conferences is limited to abstracts (BSides, DEF CON, FIRST) and press recaps.
- **Dark Reading's Black Hat Asia counterpoint** (landscape lead) returned 403.
- **DARPA AIxCC site** returned 403, so scored find-and-fix results were not re-read; the landscape's AIxCC figures (86% found, 68% patched) are not repeated here.
- **Primary reports not opened:** the 1Password FLAWED paper PDF (only the blog and Trail of Bits' quotations), the full Veracode report, the OpenAI/Hugging Face technical report, the arXiv full texts (abstracts only), the Berkeley Vulnerability Initiative data, and the Anthropic Frontier Red Team posts.
- **Maintainer quote cited by AISLE** ("Mythos 0 / Aisle 29") was not located in the curl maintainer's posts that I opened.
- **Independent measurement:** no override rates, parallel runs, inspection findings or third-party replications specific to AI in AppSec; all large figures are self-reported or vendor-published.
- **In-house enterprise case studies** beyond Google, Cloudflare, Meta, GM, OpenSearch (via a researcher) and Trail of Bits are thin; no mid-size or regulated-industry (bank, health) AppSec team account found.
- **DevSecOps and platform engineering voices** (Latio, Detection Engineering Weekly, Risky Business episode bodies, Cloud Security Podcast) loaded only as shells or descriptions.
- **Regulatory/standards** angle (CRA, SSDF, OpenSSF) belongs to the governance angle and was not pursued.
- **Terminology anomaly** carried from the landscape: CISA and NIST pages show "SI" for "AI"; none of the sources in this file did.
