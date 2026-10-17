# Synthesis report: security / application-security (wave 4)

Compiled 2026-10-17. Outputs:
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/application-security.md`
(283 lines) and `.../security/use-cases/application-security.yaml` (17 entries). `scripts/validate.py` reports no
errors for either file (remaining errors are pre-existing: `archetypes/tax/ARCHETYPE.md` and a duplicate id in
`security/use-cases/operations.yaml`).

## Counts in and out

| Input | Candidates |
|---|---|
| Practice deep dive (P) | 25 (A 8, B 12, C 5) |
| Discourse deep dive (D) | 23 (A 8, B 9, C 6) |
| Governance deep dive (G) | 22 (A 4, B 7, C 4, D 7) |
| Routed from other security files | 9 items, none a new use case (see below) |
| **Total in** | **70 candidates** |
| **Out** | **17 use cases** |

A first pass produced 25 merged entries. After the coordinator's note (and the vulnerability-exposure synthesis,
which finished first and set the split), nine merged entries already covered by vulnerability-exposure were removed
and are referenced by full id instead: frontier-model OSS discovery (security-vulnerability-exposure-01), curl and
AISLE audit (-03), Mandiant harness (-04), agent-built fuzzing (-05), AIxCC and automated patching limits (-13),
Patch the Planet (-12), patch validation (-14), dependency remediation (-15), bounty triage and PSIRT (-07, -08). The
AWS Security Agent, XBOW and PortSwigger parts of the dynamic-testing entry went the same way (-17, -18; PortSwigger
kept as a frontier note). Application-security keeps the SDLC: design, AI-written code, review, pipeline scanning
and testing, fixing in code, supply-chain intake and the team's operating model.

## Duplicates merged (final ids)

| Out | Merged from | Note |
|---|---|---|
| 01 Design review and threat modelling | P18, G20 (idea) | Cloudflare spec reviewer and Mandiant threat-model gate cited |
| 02 Guardrails for AI-written code | P14, D17, G16, G19 (D), G15 (D, NCSC) | C overall |
| 03 Kernel rules for AI contributions | G14 | |
| 04 AI review of every PR | D03, P13, D16 (PR-review part), G13 | A on Cloudflare telemetry and AgenticSCR |
| 05 Standards as machine-readable rules | D04 | split back out of 04 |
| 06 Risk-tiered auto-landing (Meta RADAR) | P02, D05, G04 | capped B, general code review |
| 07 Google pre-submit scanning | P01, D01, G01, G02 | kept here per vulnerability-exposure split |
| 08 Reasoning-based AI scanning vs SAST | P11, D19, D18, P09 | A rests only on GitHub's 24-vulnerability count |
| 09 Reachability-first triage and closure | P12, G22 (search-only, not used) | cross-ref VE-06, VE-11 |
| 10 Validator-gated testing (PageBreak) | D02, P10/D12/G11 (AWS part to VE-17), D13 (to frontier) | |
| 11 Agent-built audit tooling (Miden) | P20, D20 | kept here per split |
| 12 AI-drafted fixes for scanner alerts | P03, G03 | |
| 13 CodeMender hardening annotations | P24 | |
| 14 AI screening of packages, skills, outside PRs | P16, D22, D23, G17 (D), G18 (D) | |
| 15 Advisory curator assistance | P17 | cross-ref VE-24 |
| 16 Benchmarking AI tools | P23, G12 | BenchChecker routed in |
| 17 Team builds its own skills and agents | P22, D21 | D21 A lowered to B (rule of 2026-10-17) |

Removed for cross-reference (merged first, then dropped): P04/D09/G09, P05, P06/D07/G06, P07/D06/G05, P08/D08/G07,
P15/D11, P19/D14/P25/D15, P21/D10/G10, G08. Dropped outright: G21 (Kintsugi runtime-containment idea; results not
read) and G22's search-only figures.

## Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 15, 16 | 03 | | 3 |
| augment | 04, 12 | 01, 02, 05, 07, 08, 09, 13 | 17 | 10 |
| automate | 14 | 06 | | 2 |
| delegate | | 10, 11 | | 2 |
| Total | 5 | 11 | 1 | 17 |

Thin cells: delegate (two in-house or firm cases, both grade A); automate (Meta's general code review and intake
gates whose evidence is bypass research); model scope has one entry, a consultancy (Trail of Bits). No evidence was
found of an enterprise AppSec function changing its sourcing, pricing or service model; no delegate-level entry at
step scope or model scope. Delegate-level discovery and pentest work sits in vulnerability-exposure.

## Grade mix

A 5 (04, 07, 08, 10, 11), B 11, C 1 (02), D 0. A/B share 94%. Every A is self-reported by the deploying organisation
(Google, Cloudflare, Atlassian setting, GitHub, Trail of Bits); none is independent. Borderline: 07 (precision without
recall, "in some cases" false-positive figure) and 08 (A rests on one researcher's count; the product figures are
vendor-published). Under the 2026-10-17 rule, Trail of Bits' "200 bugs a week" and Stripe's "weeks to minutes" stay
at B. Grade D ideas were merged into stronger entries and labelled in notes (threat-model diffs, NCSC spectrum,
instruction files, registry checks, adversarial testing of review pipelines).

## Routed items picked up

- ai-security (agent identity and containment): agent skill and plugin scanning, AI-generated code risks -> 14, 02.
- ai-security (threats and red team): AI-generated code insecurity (ARXIV-2604.05292) -> 02; AI infrastructure
  vulnerabilities at DEF CON left to ai-security (no defender use case).
- identity-access governance: secrets in production web code (ARXIV-2609.23042) -> module §5.
- security-operations discourse: GM bug-bounty auto-triage -> now in security-vulnerability-exposure-07 (referenced).
- threat-intelligence discourse: adversaries tricking AI coding assistants and LLM scanners (GTIG-AITRACKER-2026) -> 14.
- vulnerability-exposure (all three angles): Google pre-submit scanning -> 07; Veracode security debt
  (REGISTER-VERACODE-2026) -> §5; SastBench -> 09; BenchChecker -> 16; Miden tooling -> 11; BSides CI
  metadata-injection talk not used (title only). The DBIR weakness-class line ("memory safety, 89% of organisations;
  median 50% survival 6 to 7 months") was too terse to restate without guessing its meaning, so it was not used.
- incident-response governance: patch-quality evidence -> covered by VE-13/14 and referenced.

## Routed from application-security inputs to other modules (for their synthesis)

- **vulnerability-exposure:** GTIG trend data and triage advice (GTIG-VULNTRENDS-2026); VulnCheck ledger reconciliation;
  NVD RFI and V-etalon (SOCKET-NVD-2026); CISA Gold Eagle abstract; Anthropic Critical Infrastructure Defense Program
  (OT); XBOW and Wiz Red Agent listings; NCSC patch-wave statements; PatchWeaver; the GTIG AI-discovered RCE share.
- **ai-security:** AppSec for agentic apps, MCP and A2A, and AI red-team postings (Datadog, Coinbase, Cloudflare); agent
  sandboxes and prompt-injected harnesses (GITHUB-TASKFLOW-2026, TOB-VMS-2026); package hallucination research;
  OpenAI agent incident; RSAC agent-security vendor map (NAND-RSAC-2026); NIST SP 800-218A, COSAiS and Cyber AI
  Profile "Secure" area; GTIG count of AI-related CVEs; GoodVibe.
- **security-operations:** metrics for production security agents ([un]prompted session); Cloudflare "agentic security
  operations harness" (title only); detection fidelity when agents use admin tools (TLDRSEC-348-2026).
- **incident-response:** Cloudflare incident-report reviewer (already security-incident-response-16); Mandiant harness
  after stolen repositories; BSides "After the Jailbreak".
- **governance-risk:** AI tool policy for client code (TOB-AINATIVE-2026); compliance without per-change review
  (SEMGREP-ENDCR-2026); mapping SSDF, CRA, NIS2, DORA and AI Act duties; BSIMM16; open-source retreat and AppSec budget
  argument (SEMGREP-MYTHOS-2026); maintainer funding.
- **cloud-infrastructure:** Wiz AI SAST code-to-cloud correlation (WIZ-AISAST-2026).

## Gaps

- No independent production measurement of any AI AppSec tool: no override rate for security findings, no parallel
  run of AI against human review, no false-negative rate, no cost per validated finding.
- Most "in-production" evidence comes from very large engineering organisations and security firms (Google,
  Cloudflare, Meta, GitHub, Trail of Bits); no mid-size or regulated-industry AppSec team account was found.
- Several key items are abstracts of talks not yet given ([un]prompted, 2026-10-27 to 29) or TLP:AMBER (FIRST PSIRT).
- Thin on SBOM generation, provenance, CI/CD hardening and IaC scanning with AI; on secrets detection with AI; and on
  junior-engineer pipeline effects.
- Model change scope rests on one consultancy; no evidence of AppSec services being priced or sourced differently.
- Source-key aliases across angles (TOB-MIDEN-2026 = TOB-AUDITING-2026 = TOB-AUDIT-2026; GITHUB-SECUREFUND-2026 =
  GITHUB-FUND-2026; the 1Password blog and PDF now have separate keys; Veracode's 2025 landing page and blog too).
- One factual conflict resolved: the governance angle read AIxCC's "68%" as a share of vulnerabilities found; DARPA's
  counts (43 patched of 63) make it a share of all 63 (now in security-vulnerability-exposure-13's domain).

## Suggested improvements to the briefs

1. Publish the module split before the deep dives run. Both vulnerability-exposure and application-security
   researched the same Glasswing, curl, Mandiant, fuzzing, patching and PSIRT sources; a written boundary
   (SDLC vs discovery and remediation programmes) would have saved roughly a third of the effort here.
2. Ask researchers to use landscape keys verbatim and to check a shared key registry before minting new ones.
3. Tell researchers that a conference abstract for an event not yet held cannot support an outcome figure above B,
   and to flag the event date in `notes` (the practice angle did this well).
4. Require `measures` to say whether a figure is precision, recall, a count or an estimate; "precision without
   recall" appeared several times without comment in the inputs.
5. Ask the governance angle to separate "regulator guidance" ideas from use cases; seven grade-D entries were
   guidance or research with no adopter and had to be folded into other entries.
6. Add a field or note convention for "general engineering evidence used for security" so the cap to B for
   adjacent evidence (Meta RADAR, Cloudflare Codex) is applied the same way in every angle.
