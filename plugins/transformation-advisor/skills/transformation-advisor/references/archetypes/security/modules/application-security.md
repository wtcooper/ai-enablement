# Application security (security)

Last reviewed 2026-10-17. Use cases live in `../use-cases/application-security.yaml` (17 entries). Ids are shortened
here: `#05` means `security-application-security-05`; other modules' ids are given in full. Source keys in brackets,
such as [GOOGLE-AGENTICSCAN-2026], are in the YAML or in §10. Almost every outcome figure is self-reported by the
deploying organisation or published by a vendor about its own product; no independent production measurement of an
AI AppSec tool exists yet. Say so when you quote one. Claims from [un]prompted 2026 abstracts [UNPROMPTED-2026]
come from talks scheduled for 2026-10-27 and 2026-10-28 that have not yet been given; treat them as unpresented claims.

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

Security inside the software development lifecycle: secure design and threat modelling, code written with AI
assistants, code review, static and dynamic testing in the pipeline, fixing findings in code, intake of third-party
code (packages, agent skills, outside pull requests), and how AppSec teams reorganise around their own agents. The
2026 story is that finding flaws got cheap while verifying, reviewing and closing them did not
[ANTHROPIC-GLASSWINGUPDATE-2026, UNPROMPTED-2026]. Vulnerability
discovery programmes, consultant audits, fuzzing campaigns, bug-bounty and PSIRT intake, patching programmes and
pentest agents are in the vulnerability-exposure module; this file points to them by id.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Secure design and threat modelling | Intake questions, threat model, design review, risk tracking | expert-judgment, document-production | Specialists gather context by hand while developers wait (Stripe, abstract of a talk scheduled for 2026-10-28) [UNPROMPTED-2026] |
| Coding with AI assistants | Developers and coding agents write code; rules files and IDE checks | software-systems | 55.8% of 3,500 AI-generated artifacts had a flagged vulnerability (preprint) [ARXIV-2604.05292] |
| Code review | Human and automated review before merge; risk tiering | review-assurance | At Meta, lines per human-landed diff +105.9% in a year, over 80% of the growth from agentic AI [ARXIV-2605.30208] |
| Scanning in CI (SAST, SCA, secrets) | Pre-submit and nightly scans; reachability checks | review-assurance | Rules find only what someone wrote a rule for; false positives need costly manual triage [ARXIV-2601.02941] |
| Dynamic testing and audit | Test running apps; build tools for unfamiliar code | review-assurance, software-systems | Scanners give candidates, not proof of exploitability [GOOGLE-PAGEBREAK-2026] |
| Finding triage and closure | De-duplicate, rank by reachability, assign owner, track to fixed | review-assurance, data-reporting | "Opened" is not "fixed"; a passing build does not prove the path is gone (Rubrik, abstract of a talk scheduled for 2026-10-27) [UNPROMPTED-2026] |
| Fixing in code | Draft fix, review, merge; dependency upgrades | software-systems | Snyk data: about eight vulnerabilities introduced per one remediated [SNYK-AGENTIC-2026]; 12.5% of first fixes incomplete [TOB-1PASSWORD-2026] |
| Supply chain intake | Package intake, malware blocking, agent-skill vetting, advisory data | review-assurance, transaction-processing | Malicious packages run at install, before a PR scan [SNYK-AGENTIC-2026]; models invent package names [USENIX-SEC-2025-HALLUC] |
| Inbound reports and PSIRT | Bug bounty, product security incident response | transaction-processing | GitHub private reports ~550/week (Jan) to 3,000+/week (May 2026) [GITHUB-ADVDB-2026]; see security-vulnerability-exposure-07, -08 |
| Policy and programme reporting | Rules for AI contributions, tool evaluation, metrics | review-assurance, data-reporting | Vendor benchmarks overstate ability (§5) |

Semgrep describes AppSec as a broad remit held together by relationships with developers, processes that fit
existing work, and tools, "in that order of importance" [SEMGREP-APPSEC-2026].

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome), reinvent (the operating model changes). Improve is crowded; automate and delegate have few
entries; reinvent has one, at a consultancy.

**Design and threat modelling**
- Improve: `#01` agents run the security review lifecycle (Stripe, "weeks to minutes", from the abstract of a talk
  scheduled for 2026-10-28); Anthropic's AppSec team lists AI-drafted threat models and AI suggestions on which reviews need a human; Cloudflare's spec reviewer covered ~600 specs. Idea:
  threat-model diffs on every change (USENIX talk).

**Writing code with AI**
- Improve: `#02` scanners, rules files and package firewalls inside coding agents (Semgrep, Snyk; vendor figures,
  grade C), with NCSC's advice to set oversight by code criticality.
- Improve (policy across the process): `#03` Linux kernel rules: no AI Signed-off-by, an "Assisted-by" tag, reproducers for AI bug reports.

**Code review**
- Improve: `#04` a security reviewer agent on every pull request (Cloudflare: 131,246 runs in 30 days, 0.6% break
  glass, USD 1.19 a review; AgenticSCR at Atlassian: 54% of comments validated in shadow mode). `#05` standards
  rewritten as machine-readable rules review agents enforce (Cloudflare Codex).
- Automate: `#06` Meta's RADAR lands low-risk diffs with no human reviewer (revert rate one third of other diffs;
  general code review, not security-specific).

**Scanning and testing in the pipeline**
- Improve: `#07` pre-submit agentic scanning of every change with a reachability-proving triage agent (Google: over
  92% precision of its reachability verdicts, recall not stated). `#08` reasoning-based scanners beside SAST (Codex Security, Claude Code Security,
  Wiz, Semgrep, Snyk; GitHub Security Lab found 24 Android flaws with open-source taskflows).
- Delegate: `#10` Google's PageBreak hunts web flaws and only deterministically validated ones reach teams (over 500
  XSS). `#11` agents build a decompiler, analyser and Lean model before a manual audit (Trail of Bits: 95 proofs).
- Elsewhere: agent-built fuzzing campaigns security-vulnerability-exposure-05; pentest agents -17 and -18.

**Triage, closure and fixing**
- Improve: `#09` reachability-first triage with separate opened, reviewed and fixed states (Rubrik, abstract of a
  talk scheduled for 2026-10-27; grade C). `#12` AI-drafted fixes delivered as reviewable changes (Copilot Autofix,
  Google bug-fix agent; Meta's abstract for a talk scheduled for 2026-10-27 says over 40% of critical
  vulnerabilities were fixed by AI diffs, without faster fixing). `#13` CodeMender adds compiler bounds checks to
  remove a vulnerability class.
- Elsewhere: Patch the Planet security-vulnerability-exposure-12; patch validation -14; limits of automated patching
  -13; dependency upgrade agents -15; validation and VulnOps backlogs -06, -11.

**Supply chain and intake**
- Automate: `#14` AI screening of packages, agent skills and outside pull requests at intake; every tested skill
  scanner was bypassed, and OpenSearch's LLM build gate was bypassed at DEF CON.
- Improve: `#15` AI help for GitHub's advisory curators (1,560 reviewed advisories in May 2026, not attributed to AI).
- Elsewhere: bounty and PSIRT triage security-vulnerability-exposure-07, -08.

**Running the AppSec programme**
- Improve: `#16` test AI tools on contamination-reduced, audited benchmarks before trusting them (GitLab, AWS, Semgrep).
- Reinvent: `#17` the team builds and runs its own skills and agents (Trail of Bits: 94 plugins, 201 skills, 84
  agents; Anthropic engineers each own a Claude-powered system).

## 4. Interview probes

1. **"Where does AI-found or AI-written work queue today: triage, fix, review or release? How long from a confirmed
   finding to a merged fix?"** Reveals the real bottleneck. Discovery is rarely it; Anthropic reports about two weeks
   to patch a high or critical bug [ANTHROPIC-GLASSWINGUPDATE-2026] (`#09`).
2. **"Do you track opened, reviewed and fixed as separate states?"** Reveals whether pull-request volume hides a
   review backlog (Rubrik's point, `#09`).
3. **"What share of code is now written by agents, how do you know, and what ships without line-by-line review?"**
   Reveals exposure to insecure defaults (`#02`) and whether risk tiering exists (`#06`).
4. **"Is there a deterministic check (exploit, test, reachability proof) between the model and a developer's
   queue, or do findings arrive as prose?"** Reveals noise risk; Google's systems put validation first (`#07`, `#10`).
5. **"Which AI scanners or reviewers do you run, and what did you measure yourselves: false positives, missed
   findings, override rates? What happens when two runs disagree?"** Reveals reliance on vendor benchmarks (`#16`);
   AISLE's abstract for a talk scheduled for 2026-10-28 says one run can miss what the next finds [UNPROMPTED-2026].
6. **"For an AI-proposed fix, what do you check beyond 'the exploit no longer works'?"** Reveals PoC-only
   validation, which inflated agent results 1.83 times in PatchBench [ARXIV-2609.04075] (`#12`).
7. **"Do your reviewers and scanners know the product's authorization and tenancy rules?"** Reveals blind spots:
   Snyk argues agents omit ownership checks because the rule is not in the prompt [SNYK-BAC-2026].
8. **"Which coding-agent changes can merge without a human, who decided, and what revert or incident data backs
   it?"** Reveals governance of automation (`#06`); Meta used revert and incident rates.
9. **"How do packages and agent skills get in, and could a model gate in CI be talked past?"** Reveals intake risk
   (`#14`): scanners and an LLM build gate were bypassed in 2026.
10. **"If a frontier-model scan sent 1,000 findings tomorrow, who would triage them and what would you stop doing?"**
    Reveals capacity; see security-vulnerability-exposure-01 and -11.
11. **"Who on the team builds and maintains your agents, skills and rule packs, and how is that work recognised?"**
    Reveals operating-model readiness (`#17`) and the resistance Trail of Bits designed against.
12. **"Which products fall under the EU Cyber Resilience Act, and can you report an actively exploited flaw within
    24 hours?"** Reveals regulatory clock pressure on PSIRT and fix flow (§6).

## 5. Metrics and benchmarks

**Baselines to ask for first**
- Code volume: Meta +105.9% lines per human-landed diff, per-developer diff volume +51% [ARXIV-2605.30208];
  per-reviewer load roughly doubled at another company [ARXIV-2607.01904, abstract].
- Backlog: Snyk says 94% of 459 million findings had a known fixed version but about 10% were resolved over six
  months [SNYK-VULNBUMP-2026, vendor]. Veracode (as reported): 82% of companies carry known vulnerabilities unresolved
  for over a year, up from 74%; Veracode says more testing may explain part of the rise [REGISTER-VERACODE-2026].
- Fix quality: across 236 Trail of Bits assessments, developers' first fixes for 283 of 2,265 vulnerabilities (12.5%)
  did not fully resolve the issue [TOB-1PASSWORD-2026].
- Secrets: in one organisation 113 of about 2,000 assets (5.65%) served live credentials, and the best of nine
  scanners found 36.6% (static) or 77.8% (runtime-aware) of a ground-truth set [ARXIV-2609.23042, abstract].
- Disclosure volume: 5,045 (Jan 2026) to 10,740 (Aug 2026) CVEs a month; GTIG says automated CNA assignment inflates
  counts [GTIG-VULNTRENDS-2026].
- Maturity benchmark: BSIMM16 (111 organisations, Jan 2026) names AI adoption, SBOM growth and regulatory
  self-attestation as themes; body gated [BLACKDUCK-BSIMM-2026].

**Named outcomes (self-reported; most measure volume or effort, not quality)**

| Measure | Figure | Use case |
|---|---|---|
| Triage-agent precision (no recall published); false positives | over 92%; 3% "in some cases" (Google) | `#07` |
| Validated XSS found by agent | over 500 (Google PageBreak) | `#10` |
| AI review at scale | 131,246 runs, 48,095 MRs in 30 days; median 3m39s; break glass 0.6%; USD 1.19 average (Cloudflare) | `#04` |
| Security comments validated, shadow mode | 54% (Atlassian setting) | `#04` |
| Auto-landed diffs; revert and incident rates | 331K+ landed; one third and one fiftieth of non-RADAR diffs (Meta, observational) | `#06` |
| Standards violations flagged; approvals withheld | ~230,000; ~16,000 (Cloudflare) | `#05` |
| Android vulnerabilities found with taskflows | 24 (GitHub Security Lab, one researcher) | `#08` |
| Machine-checked proofs before an audit | 95 (Trail of Bits) | `#11` |
| Critical vulnerabilities fixed by AI diffs | over 40%, no faster fixing (Meta, abstract of a talk scheduled for 2026-10-27; not yet presented) | `#12` |

**Vendor claims (ask for named, measured cases)**: OpenAI Codex Security false positives down over 50% in beta
[OPENAI-CODEXSEC-2026]; AISLE best AI analyser 68% vs best SAST 12.1% on CVEs AISLE found [AISLE-SAST-2026]; Snyk fix
rate 74.6% to 85.4% with its context [SNYK-AGENTFIX-2026]; Semgrep over 3 million write-time scans a week
[SEMGREP-GUARDIAN-2026]; AWS agent 33 of 37 CVEs (security-vulnerability-exposure-17).

**Security of AI-generated code**: 55.8% of 3,500 artifacts flagged, security instructions -4 points, models caught
78.7% of their own flaws in review mode [ARXIV-2604.05292]; Veracode 56% average pass rate, best model 68%
[VERACODE-GENAI-2026]; CodeRabbit ~1.7x issues per AI-co-authored PR [CODERABBIT-2025]; 87.9% of 7,703 AI-attributed
GitHub files had no CWE-mapped flaw [ARXIV-2510.26103]. Studies disagree; quote the method with the number.

**Benchmark validity**: 53% of Opus 5.5's SusVibes solutions near-identical to real code [SEMGREP-SUSVIBES-2026];
PoC-only checks inflate patch results 1.83x [ARXIV-2609.04075]; removing contaminated samples cuts bug-fix scores
more than 20% relative [USENIX-BENCHCHECKER-2026]; graders matched humans on 65.9% of full outcomes [TOB-1PASSWORD-2026].

**What to measure**: confirmed-to-merged time; opened, reviewed and fixed counts (`#09`); false positives and missed
findings on a labelled set, as GitLab hires for (`#16`); override or break-glass rate (`#04`); reverts and incidents
of auto-landed changes (`#06`); share of fixes that pass variant and regression checks. No source publishes an
override rate for security findings or a parallel run of AI against human AppSec review.

## 6. Guardrails

**Regulation and standards (none is AI-specific for AppSec; the AI material is voluntary)**
- **EU Cyber Resilience Act**: reporting of actively exploited vulnerabilities from 2026-09-11 (early warning 24 h,
  notification 72 h, final report 14 days after a corrective measure, via ENISA's Single Reporting Platform); main
  obligations from 2027-12-11; guidance 2026-07-27; also reaches open-source stewards [EC-CRA-2026, EC-CRA-REPORTING-2026].
- **NIS2** Article 21(2)(e): security in development and maintenance, including vulnerability handling; recitals 51
  and 89 only encourage AI tools [EURLEX-NIS2-2022]. **DORA RTS** Article 16: source code review with static and
  dynamic testing, including open-source code where feasible; no AI text [EURLEX-DORA-RTS-2024].
- **NIST**: SSDF 1.2 draft (2025-12-17) has no AI text [NIST-SSDF-218R1-2025]; SP 800-218A covers developing AI models,
  not using AI to code [NIST-SSDF-218A-2024]; the Cyber AI Profile draft suggests extending AI checks to secure
  development and lists AI source-code vulnerability detection among examples [NIST-CYBERAI-2025].
- **UK**: Software Security Code of Practice, 14 principles (updated 2026-01-15) [UK-DSIT-SSCOP-2025]; NCSC "vibe
  coding spectrum": slide towards manual coding for authentication, authorisation, secrets, personal data and
  safety-critical code [NCSC-VIBE-2026]. **US**: CISA Secure by Design [CISA-SBD-2023].
- **Community**: OpenSSF guide for assistant instructions (developer stays responsible) [OPENSSF-AIGUIDE-2025];
  Linux kernel rules on AI contributions (`#03`). EU AI Act high-risk rules moved to 2027-12-02 [EC-AIACT-2026].
- A Semgrep blog quotes Amp saying SOC 2 does not require pull requests; that is a vendor's argument, not an auditor's
  statement [SEMGREP-ENDCR-2026].

**Design guardrails seen in deployments**
- Deterministic validation (reachability proof, non-AI exploit validator, rescan) before a human sees a finding (`#07`, `#10`).
- Keep generating, scanning and triage agents separate to avoid shared bias [GOOGLE-AGENTICSCAN-2026].
- Advisory first, blocking only after promotion; a break-glass override (`#04`, `#05`).
- Fixes arrive as reviewable changes; never auto-patch bug classes that cannot be cheaply validated (`#09`, `#12`).
- Run agent harnesses in throwaway environments; GitHub warns a prompt-injected agent can do what its user can
  [GITHUB-TASKFLOW-2026].
- Curated skill sources, sandboxing and an approved-tools handbook (`#14`, `#17`); red-team AI review before relying
  on it: crafted PR context beat two review pipelines in 32 of 33 cases [ARXIV-2603.18740].

**Steps that stay with a person**: high-risk architecture decisions; accepting a fix into the code base; formal risk
acceptance; promoting a rule to blocking; deciding which code is too critical for AI authorship; CVE and disclosure
decisions; certifying origin of contributed code.

## 7. Roles and how they evolve

- **AppSec engineers become builders and operators of agent systems.** Anthropic's engineers each own a
  Claude-powered system and the posting describes human work as the judgement layer [ANTHROPIC-JOB-APPSEC-2026]; GitLab
  expects all staff to use AI daily and wants engineers who evaluate AI detection on labelled data [GITLAB-JOB-CODESEC-2026].
- **AI skills in hiring.** Samsara, Cloudflare, Coinbase, Okta, MongoDB and Stripe postings ask for AI-driven triage,
  testing, detection or remediation work [SAMSARA-JOB-APPSEC-2026, CLOUDFLARE-JOB-PSE-2026, COINBASE-JOB-PSE-2026,
  OKTA-JOB-PSE-2026, MONGODB-JOB-PSE-2026, STRIPE-JOB-VM-2026]. Datadog hires AppSec for agentic apps (ai-security)
  [DATADOG-JOB-APPSEC-2026].
- **Reviewers carry more.** Reviewer load roughly doubled at one company; Semgrep says PRs with written human feedback fell
  from 39% to 21% (not verified in the paper) [ARXIV-2607.01904, SEMGREP-ENDCR-2026].
- **Experts encode themselves as skills.** Trail of Bits: about 5% on board a year earlier; four psychological
  barriers designed against; status moves to the people who build tools (`#17`).
- **Maintainers are the constraint.** curl's security team is six volunteers [CURL-TEAM-2026]; its maintainer
  reports security reports at 4-5 times the 2024 rate [STENBERG-PRESSURE-2026].
- **Professional body.** ISC2: AI is the top skills need (41%); roles evolve rather than disappear [ISC2-WORKFORCE-2025].
- **Juniors.** Coinbase asks engineers to mentor juniors on AI in offensive security; no hard data on entry-level
  AppSec hiring was found.

## 8. Frontier

- **2026-02-20 / 03-06** Claude Code Security and Codex Security previews: scan, validate, propose patches for human
  approval [ANTHROPIC-CCS-2026, OPENAI-CODEXSEC-2026].
- **2026-03-31** Trail of Bits describes an AI-native consultancy model [TOB-AINATIVE-2026].
- **2026-04-07; 10-06** Glasswing gates a frontier model for defenders; Cyber Verification Program gets three tiers
  [ANTHROPIC-GLASSWING-2026]. Ireland's NCSC noted the model was unavailable for independent testing [GOVIE-NCSC-2026].
- **2026-05-22** Anthropic says progress is limited by verifying, disclosing and patching [ANTHROPIC-GLASSWINGUPDATE-2026];
  2026-06-02 it predicts comparable models elsewhere within 6-12 months (vendor forecast) [ANTHROPIC-EXPAND-2026].
- **2026-06-18** NCSC publishes the vibe coding spectrum [NCSC-VIBE-2026].
- **2026-06-23 to 07-28** Semgrep Guardian (write-time scanning) and Agentic Workflows [SEMGREP-GUARDIAN-2026, SEMGREP-AGENTICWF-2026].
- **2026-08** DEF CON: an LLM CI gate bypassed; a PortSwigger researcher's autonomous system finds new HTTP desync
  triggers on bug-bounty targets and a behaviour he treats as evidence of a new desync class [DEFCON-34-2026, TLDRSEC-346-2026].
- **2026-08-06 / 09-15** 1Password's 26% clean-patch headline and Trail of Bits' rebuttal [ONEPASSWORD-FLAWED-2026, TOB-1PASSWORD-2026].
- **2026-09-11** CRA vulnerability reporting applies [EC-CRA-REPORTING-2026].
- **2026-09-19 / 09-24** Google publishes pre-submit agentic scanning and PageBreak (`#07`, `#10`).
- **2026-10-06 to 10-15** Wiz AI SAST, OSS Scanner, Semgrep in Cursor Origin, Snyk Evo Agentic AppSec [WIZ-AISAST-2026,
  ANTHROPIC-CYBERMISSION-2026, SEMGREP-CURSOR-2026, SNYK-AGENTIC-2026].
- **2026-10-27 to 10-28** [un]prompted talks by Meta, Google and Rubrik (27 October) and Stripe and AISLE (28 October)
  are scheduled on AI fixes, closure, repeatability and agent-run reviews; their claims are unpresented abstracts
  [UNPROMPTED-2026].
- **2027-12-11** CRA main obligations [EC-CRA-2026].

## 9. Common objections

- **"It's mostly marketing."** curl's maintainer cut one scan's five "confirmed" flaws to one low-severity CVE
  [STENBERG-MYTHOS-2026], yet the same maintainer credits AISLE's AI-assisted audit with 35 published curl CVEs
  (security-vulnerability-exposure-03).
  Ask for maintainer-confirmed counts, not model counts.
- **"AI only finds known bug types."** Stenberg's view (2026-05-11); a PortSwigger researcher's 2026 autonomous system
  found new desync techniques and what he treats as evidence of a new desync class [TLDRSEC-346-2026].
- **"Benchmarks prove it works."** Memorisation, PoC-only checks and grader disagreement inflate scores (§5); AWS says
  its own benchmark's controls "reduce contamination rather than eliminate it" [AWS-SECAGENT-2026]. Test on your own labelled set (`#16`).
- **"Results change run to run."** True; AISLE's abstract for a talk scheduled for 2026-10-28 reports it across
  25,000 trials [UNPROMPTED-2026], and GitHub's taskflows use repeated runs for the same reason [GITHUB-ANDROID-2026]. Deployments repeat runs
  and put deterministic validators in front (`#07`, `#10`).
- **"AI fixes will save us."** Meta's abstract for a talk scheduled for 2026-10-27 says its AI fixes did not by
  themselves speed fixing [UNPROMPTED-2026]; AI-assisted code-quality remediation (not security fixes) saturated CI
  and reviewers in one industrial study [ARXIV-2609.29172]. Budget review capacity (`#09`, `#12`).
- **"AI code is insecure, so adding AI review is circular."** Generation and review differ: models caught 78.7% of
  their own flaws in review mode [ARXIV-2604.05292]. Keep deterministic checks and human sign-off (`#04`).
- **"An AI gate is enough."** Skill scanners and an LLM build gate were bypassed in 2026 [TOB-SKILLS-2026,
  DEFCON-34-2026]; layer procedural controls (`#14`).
- **"Maintainers want our AI findings."** They want fewer, verified reports [OPENAI-CODEXSEC-2026, LF-GLASSWING-2026];
  include reproducers [LINUX-KERNEL-AI-2026].
- **"The vendor numbers are hype."** Mostly vendor-published with unnamed customers [SEMGREP-GUARDIAN-2026]; the
  measured cases are in-house (Google, Cloudflare, Meta) or firm-run (Trail of Bits).

## 10. Sources

Full details for every key used in the use cases are in the YAML. Keys cited only in this file (all opened by the
research angles unless marked):
- **Regulators and standard-setters:** EC-CRA-2026 (European Commission, *Cyber Resilience Act*, 2026-09-07, https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act); EC-CRA-REPORTING-2026 (*CRA reporting obligations*, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting); EURLEX-NIS2-2022 (Directive (EU) 2022/2555, 2022-12-27, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555); EURLEX-DORA-RTS-2024 (Delegated Regulation (EU) 2024/1774, 2024-06-25, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1774); EC-AIACT-2026 (AI Act status page, 2026-10, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai); NIST-SSDF-218R1-2025 (SP 800-218 Rev 1 ipd, 2025-12-17, https://csrc.nist.gov/pubs/sp/800/218/r1/ipd); NIST-SSDF-218A-2024 (SP 800-218A, 2024-07-26, https://csrc.nist.gov/pubs/sp/800/218/a/final); NIST-CYBERAI-2025 (IR 8596 iprd, 2025-12-16, https://csrc.nist.gov/pubs/ir/8596/iprd); CISA-SBD-2023 (Secure by Design, 2023-10-25, https://www.cisa.gov/resources-tools/resources/secure-by-design); UK-DSIT-SSCOP-2025 (Software Security Code of Practice, 2025-05-07, https://www.gov.uk/government/publications/software-security-code-of-practice); GOVIE-NCSC-2026 (Ireland NCSC statement on Mythos Preview, 2026-04-13, https://www.gov.ie/en/department-of-justice-home-affairs-and-migration/press-releases/national-cyber-security-centre-ncsc-statement-on-anthropics-mythos-preview-model-for-defensive-cyber-security-purposes/).
- **Firms and vendors:** GTIG-VULNTRENDS-2026 (Google Threat Intelligence Group, 2026-09-30, https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/); ANTHROPIC-GLASSWING-2026 (2026-04-07, https://www.anthropic.com/glasswing); SNYK-VULNBUMP-2026 (2026-10-15, https://snyk.io/blog/vulnbump/); SEMGREP-APPSEC-2026 (*What Application Security Actually Does All Day*, 2026-09-25, https://semgrep.dev/blog/2026/what-application-security-does); ONEPASSWORD-FLAWED-2026 (1Password Off-by-1 Labs, 2026-08-06, https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf); GITHUB-TASKFLOW-2026 (GitHub Blog, 2026-09-24, https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/); LF-GLASSWING-2026 (Linux Foundation, 2026-04-07, https://www.linuxfoundation.org/blog/project-glasswing-gives-maintainers-advanced-ai-to-secure-open-source).
- **Surveys, press, community:** BLACKDUCK-BSIMM-2026 (BSIMM16 landing page, 2026-01, https://www.blackduck.com/resources/analyst-reports/bsimm.html); ISC2-WORKFORCE-2025 (2025-12-04, https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study); REGISTER-VERACODE-2026 (The Register, 2026-02-26, https://www.theregister.com/software/2026/02/26/rapid-ai-driven-development-makes-security-unattainable/4285126); STENBERG-PRESSURE-2026 (2026-05-26, https://daniel.haxx.se/blog/2026/05/26/the-pressure/); CURL-TEAM-2026 (2026-10-12, https://daniel.haxx.se/blog/2026/10/12/the-2026-curl-team/).
- **Academic and job postings:** ARXIV-2609.23042 (*Secrets That Survive Everything*, 2026-09, https://arxiv.org/abs/2609.23042, abstract); OKTA-JOB-PSE-2026 (2026-09-17, https://www.okta.com/company/careers/opportunity/8156825?gh_jid=8156825); STRIPE-JOB-VM-2026 (2026-08-04, https://stripe.com/jobs/search?gh_jid=8089353); DATADOG-JOB-APPSEC-2026 (2026-09-25, https://careers.datadoghq.com/detail/8230663/?gh_jid=8230663).
