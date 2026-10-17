# Archetype synthesis report: security (wave 4)

Compiled 2026-10-17. Brief: `research/runs/wave4/briefs/archetype-synthesis-security.md`.

## Outputs

Eleven files in `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/`:

| File | Lines | Limit |
|---|---|---|
| ARCHETYPE.md | 100 | 100 |
| interview-guide.md | 171 | 300 |
| value-chain.md | 165 | 300 |
| economics.md | 181 | 300 |
| state-of-ai.md | 166 | 300 |
| frontier.md | 118 (44 dated signals plus a 9-row calendar) | 300 |
| guardrails.md | 163 | 300 |
| workforce.md | 157 | 300 |
| disruption.md | 137 | 300 |
| objections.md | 86 | 300 |
| sources.md | 195 (`last_researched: 2026-10-17`) | 300 |

`archetypes/index.md` updated: security moved to "Available archetypes" (Extends "—", cues, eleven module ids,
Available); its "Not yet available" row removed. The professional-services row now says it is also the base for
security service providers. `python3 scripts/validate.py`: 0 errors, 18 warnings (all in module YAML targets of
assurance, tax and three security modules; none in files written here).

Sourcing: 129 distinct keys cited. Keys cited in two or more files (85) are in `sources.md` Part B; keys cited in
one file only are listed at the end of that file. Every key resolves (checked by script). Part A of `sources.md`
uses links, not keys.

## What each file draws on

| File | Main inputs |
|---|---|
| ARCHETYPE.md | Landscape §1, §10 (module check), §11 (stage markers); module files §1; validator A/B counts; ISACA corrected wording (governance-risk verification report); state-of-ai and workforce cross-cutting files for marker figures |
| interview-guide.md | Interview probes in all four cross-cutting files; module §4 probes (summarised, not copied); tax guide as the structural model |
| value-chain.md | Landscape §10 (CSF mapping); NIST CSF 2.0; every module's §1-§2 step table (summarised to process level); data-layer evidence from state-of-ai file (SANS, CrowdStrike, Latio via Exaforce, Microsoft ISOC via Prophet) |
| economics.md | `security-x-economics-business-model.md` almost entirely (IANS, PwC, Wiz, ISC2, Gartner forecast, PANW, CRWD, M&A, pricing pages, insurance, IBM, D3, Intezer/Gartner) |
| state-of-ai.md | `security-x-state-of-ai-disruption.md` §2; ISACA global figures per the verification report; ISACA AI pulse from the regulation file |
| frontier.md | Frontier tables of all four cross-cutting files and landscape §12; operations and ai-security §8 for cross-checks |
| guardrails.md | `security-x-guardrails-regulation.md` (clocks, liability, AI rules, insurance, human judgment), with ISACA §2.7 replaced by the corrected global wording |
| workforce.md | `security-x-workforce-talent.md`; module §7 sections for role rows |
| disruption.md | State-of-ai file §2.7 scenarios A-E; economics file §2.7; added scenario F (in-house function as AI risk owner) from IANS, ISACA and Gartner trends |
| objections.md | Objection tables of all four cross-cutting files, merged and de-duplicated against operations §9 |
| sources.md | Landscape §2-§9, §14; source tables of the four cross-cutting files |

## Conflicts and how they were handled

- **ISACA 2026.** Used the corrected global wording throughout (8% regular AI incident exercises, 64% none, 17% in
  broader exercises, 16% plan to, 48% no or unknown playbooks, 56% helped write AI-use policy). European figures
  (71% none, 3% mature runbooks) appear once in state-of-ai §2, labelled European with their own key
  (`ISACA-SOCEU-2026`). The regulation file's 37% "AI to automate detection" (European) was not used; the global 41%
  was.
- **Key collision.** `ARCTICWOLF-AURORA-2026` names the 2026-08-03 press release in the economics and state-of-ai
  files but a 2026-09-25 blog in the workforce file. Kept the key for the press release and gave the blog a new key,
  `ARCTICWOLF-ANALYSTS-2026`.
- **"Super Intelligence (SI)" page wording.** Not repeated. The 2026-10-16 NIST, NSA and CISA practices are described
  by content, not title (the ai-security verifier found the issued PDF itself carries the SI wording), and cited via
  `NIST-CAISI-2026`; CISA's agentic guidance is cited by its published title.
- **Gartner "75%+ of enterprises on AI-amplified security products by 2028"** (landscape): not on the public press
  release per the state-of-ai file; not used.
- **AIxCC 68%.** Stated as 43 patched of all 63 (68%), following the application-security synthesis correction.
- **120+ organization agent-incident reporting proposal** (Axios 2026-08-11, via Black Hat's press index) is probably
  the same effort as the SAFE near-miss RFC dated 2026-08-05 in ai-security §8; frontier.md gives the month and
  points to ai-security §8. Worth confirming.
- **ISACA open positions** (49% in the release, 61% in ISACA's newsletter): carried as unreconciled.

## Gaps

- No independent production miss, override or error rate in any module; stated in ARCHETYPE.md, state-of-ai §8 and
  objections.
- Provider economics: no audited MDR or MSSP margins, analyst-to-customer ratios or renewal price changes; all
  margin and cost-per-investigation figures are vendor claims. No outcome-priced contracts found, only warranties.
- Security spend as a share of revenue: no current open benchmark.
- Entry-level hiring: survey perception, one vendor's posting sample and economy-wide payroll data only.
- Gated primaries: full ISACA, SANS SOC and AI surveys, ISC2 PDF, Verizon DBIR 2026, M-Trends 2026, Gartner research
  (MDR guide, SOC roles, forecasts known only via vendors or search results).
- Not covered by inputs: GDPR articles on automated decisions in security tools, provider liability caps and
  indemnities, APAC and Middle East regulators beyond CERT-In, ISO/IEC 42001 text, OT (no module).
- Consultancy and Big Four AI-security service lines: only Trail of Bits documented.

## Items routed from modules that were placed

The module syntheses routed regulation, workforce and economics items to governance-risk or "archetype level". Placed:

| Item (routed from) | Placed in |
|---|---|
| SEC Item 1.05/106 status and rescission push (operations, incident-response, threat-intelligence, vulnerability-exposure) | guardrails §2, frontier §5, objections §2 |
| EU AI Act, NIS2, DORA, CRA timelines (operations, identity-access, data-privacy, vulnerability-exposure) | guardrails §2, §4; frontier §5 |
| ISACA AI-exercise and AI-policy figures (governance-risk, operations, incident-response, ai-security) | state-of-ai §2, §7; guardrails §8; ARCHETYPE markers |
| ISACA AI pulse (halt time, accountability) (incident-response) | guardrails §3, §6, §8; ARCHETYPE quick check |
| ISC2 and SANS/GIAC workforce data; junior-pipeline worry (all modules) | workforce §2-§6 |
| Gartner "AI-augmented, human-led" MDR guide and agent washing (operations) | ARCHETYPE, workforce §8, disruption A, frontier §3 |
| MSSP margin, cost per investigation, "AI costs more than people" (operations) | economics §5-§6 (margin claims); per-alert cost pointed to operations §5 and §9 |
| AI insurance exclusions; AI credentials market (ai-security) | guardrails §5; workforce §5 |
| IBM breach-cost association with security AI (governance-risk, data-privacy) | economics §5; objections §3 |
| NCSC patch-wave statements; GTIG trends (several) | frontier §2; state-of-ai §6; objections §6 |
| CERT-In advisory (ai-security, cloud) | frontier §4; state-of-ai §6; objections §5 |
| OT items (Accenture-Dragos; PANW and Anthropic critical-infrastructure programmes) | value-chain §7 (Accenture only; programmes left as leads) |

Not placed: the NVD funding and BOD 26-04 items (federal-specific; left in vulnerability-exposure), Gartner board
"storytelling" and CISO business-acumen predictions (left in governance-risk), CRA reporting detail beyond the clock
(left in incident-response and vulnerability-exposure).

## Suggested module changes

1. **governance-risk.md** lines 10-11, 175 and 220 cite `research/runs/wave4/security-x-*.md` build paths in a product
   file. Point them to `../guardrails.md` and `../workforce.md` instead.
2. **incident-response.md** line 8 cites `research/runs/wave4/incident-response-verification-report.md`; remove.
3. **operations.md** §6 states that CISA pages show "AI" replaced by "Super Intelligence (SI)". Per this wave's note,
   drop it or cite documents by their published titles.
4. **Key aliases across modules:** `CISA-KEYPRACTICES-2026` (operations) and `NISTCISA-IRKEY-2026` (ai-security) are
   the same document; `EC-CRAREPORT-2026` (vulnerability-exposure) and `EC-CRAREPORTING-2026` (archetype files) the
   same page. Settle on one key each.
5. **Repeated regulation blocks.** Several module §6 sections repeat SEC, NIS2, DORA and AI Act lines. They could
   keep the module-specific point and link to `../guardrails.md` §2 and §4.
6. **ai-security §8** "SAFE request for comments ... 120+ members" (2026-08-05): check whether it is the Axios-reported
   120+ organization proposal of 2026-08-11 and say so in one place.
7. **cloud-infrastructure** stays thin (5 of 24 A/B); data-privacy (8 of 21) and identity-access (11 of 24) are
   moderate. Targeted research on named-customer outcomes would lift them; grades should not be raised otherwise.
