# Synthesis report: security / data-privacy

Compiled 2026-10-17.

Outputs:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/data-privacy.md` (273 lines)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/data-privacy.yaml` (21 entries)

`scripts/validate.py`: 0 errors. One expected warning: data-privacy has 8 of 21 entries graded A or B (38%), below
the 50% target. This is honest: the public evidence is thin, and no entry was padded or upgraded to meet it.

## Counts in and out

- In: 21 candidate use cases from the one combined deep dive (`security-data-privacy-combined.md`). The landscape scan
  (`landscape-security.md`) added no new use cases, only sources already used (CSA DLP survey, Black Hat Asia
  privacy keynote, OWASP guide).
- Routed in from other security files: 7 items, all baselines or signals rather than new use cases (see below).
- Out: 21 use cases, ids `security-data-privacy-01` to `-21`, in the deep dive's order.

## Duplicates merged

None. The deep dive had already deduplicated. Pairs checked and kept separate because they describe different
changes to the work: #06 (DLP alert triage) versus #07 (replacing pattern-matching DLP classification); #08
(vendor paste/upload controls) versus #18 (idea: LLM policy-file prompt blocking) versus #16 (idea: LLM PII
redaction); #10 (oversharing review before AI rollout) versus #12 (label enforcement at retrieval); #02 (Meta
classification) versus #13 (Meta requirements-to-controls workflow).

Cross-referenced instead of duplicated: #08 and #09 to `security-human-risk-16` and `security-ai-security-21`; #04 to
`security-ai-security-09`; #14 to `security-application-security-04` and `-08`; #17 to `security-ai-security-08`.
The OpenAI third-party data incident is pointed to `security-ai-security-17` and the Wiz Red Agent to
`security-vulnerability-exposure-21` (module Frontier section).

## Grade changes

- #01 (Glyph catalog tagging) moved from A to B. The figures are measured and tracked weekly, but the paper does not
  name the deploying organization ("a single organization's production catalog"; authors are Apple-affiliated), and
  grade A needs a named organization. Recorded in the entry's notes.
- #02 (Meta, routing and cost split) and #14 (Microsoft, PEPR abstract, more than 2x confirmed issues) stay A under
  the 2026-10-17 rule: both are figures the named organization reports as measured. Both are self-reported, and #14
  rests on a conference abstract only.
- #07 stays B: the OpenWeb figure ("probably a fifth") is a CISO estimate, labelled as such.

## Grade mix

A 2, B 6, C 10, D 3 (input was A 3, B 5, C 10, D 3).

## Coverage by ladder and change scope

| | step | process | model |
|---|---|---|---|
| assist | 2 (#04, #19) | 0 | 0 |
| augment | 5 (#03, #06, #14, #15, #20) | 6 (#01, #05, #07, #10, #11, #13) | 0 |
| automate | 5 (#08, #09, #16, #17, #18) | 3 (#02, #12, #21) | 0 |
| delegate | 0 | 0 | 0 |

Totals: assist 2, augment 11, automate 8, delegate 0; step 12, process 9, model 0.

**No evidence for delegate or for model-level change.** The nearest is #11 (agents take remediation actions, but each
needs approval). Nothing was invented to fill these cells.

## Routed to data-privacy from other files (picked up)

- IBM Cost of a Data Breach 2025: shadow-AI incidents exposed more personal data (65% vs 53%) and IP (40% vs 33%)
  (from `security-ai-security-governance-assurance.md`). Used in module §5.
- Okta AI Agents at Work 2026: among employees using unapproved tools, 54% share internal messages and emails, 45% HR
  information, 39% confidential documents (same file). Used in §5.
- OWASP GenAI resources library (OWASP-GENAI-RES-2026) (same file): not used separately; the specific guide
  (OWASP-DATASEC-2026) is already cited throughout.
- OpenAI disclosure that research agents sent data to third-party services, 53 user images posted as unlisted links
  (from `security-ai-security-threats-redteam.md`). Used in §8 with a pointer to `security-ai-security-17`.
- CSA DLP survey (from `security-cloud-infrastructure-governance.md`): already in the YAML as CSA-AI-2026.
- Wiz Red Agent classification and redaction of exposed data (from `security-cloud-infrastructure-practice.md`,
  `security-vulnerability-exposure-discourse.md`, `-practice.md`). Used in §8 with a pointer to
  `security-vulnerability-exposure-21`; not made a use case because it is an exposure-testing agent already covered there.
- PwC 2027 Global Digital Trust Insights: three of seven data risk measures, classification 49%, DLP on egress 48%
  (from `security-governance-risk-governance.md`). Used in §5.
- Proofpoint 2026 Voice of the CISO: AI tool misuse or misconfiguration caused 37% of material data loss cases (from
  `security-governance-risk-practice.md`). Used in §5.
- `security-human-risk-combined.md` routes shadow-AI leakage, prompt inspection and DLP here; covered by #08 and #09.

## Routed from data-privacy to other modules (for their synthesis)

- **ai-security:** OWASP DSGAI02 just-in-time data access for agents (short-lived per-task credential instead of
  standing database access) (OWASP-DATASEC-2026, p. 10); MIND agent discovery and risky-access detection
  (MIND-AGENTICDLP-2026); OneTrust agent detection for AWS Bedrock, Azure Foundry and Google Vertex
  (ONETRUST-W26-2026); Google Private AI Compute, announced 2025-11-11 (GOOGLE-PRIVATEAI-2025).
- **human-risk:** Purview Insider Risk Management triage agent (MSFT-PURVIEWAGENTS-2026); Netskope finding that 60% of
  insider threat incidents involve personal cloud app instances (NETSKOPE-CTR-2026).
- **governance-risk:** Anthropic agent-security policy and compliance hiring (ANTHROPIC-JOB-AGENTSEC-2026); EU AI Act
  and Digital Omnibus timing (EC-AIACT-2026; NOERR-OMNIBUS-2026); NIST AI 600-1 (NIST-AI600-2024).
- **incident-response:** Coinbase privacy incident analyst role (COINBASE-JOB-PRIVACYANALYST-2026); breach-cost
  context (IBM-CODB-2026).
- **application-security:** pull-request privacy-pattern detection (#14, PEPR-2026).

## Gaps

- No independent override, false-positive, miss or parallel-run result for LLM-based DLP, alert triage,
  classification or privacy assessment in production.
- Encryption and key management: one vendor announcement (#19), no deployment.
- Data access governance: no named-customer outcome for oversharing remediation or access-review automation.
- DSAR (data subject request), retention and deletion automation: no public deployment with results.
- Gated or partial reads: CSA report body (abstract only), IBM 2026 (landing page), PEPR (abstracts only), Gartner
  (search-only). IAPP, ISACA, CNIL, ICO and non-EU/US regulators not read.
- Undated vendor pages: Cyera (ChenMed, Paramount, Vetcor, unnamed financial institution) and MIND (OpenWeb) customer
  stories carry the retrieval date 2026-10-17, flagged in their titles and notes.
- Practitioner discourse is very thin (podcast titles, one two-comment Hacker News thread).

## Suggested improvements to the briefs

- State in the vocabulary how to grade a measured figure from a production system whose deploying organization is not
  named (the Glyph case). This report treated it as B.
- For low-density modules, ask the deep dive to try professional bodies (IAPP, ISACA) and DPAs through mirrors or
  cached copies early, since the main gap was gated content rather than absence of activity.
- Ask deep dives to put routed items' full source details (URL, date) in the routing section, so the receiving
  synthesis does not have to look them up in other files.
- Give low-density modules an explicit lower A/B target (or say the 50% target is reported, not required) so editors
  are not tempted to inflate grades.
