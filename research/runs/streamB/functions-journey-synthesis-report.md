# Functions and journey synthesis report

Date: 2026-10-20. Brief: `research/runs/streamB/briefs/synthesis-functions-journey.md`.

## Files written or edited

| File | Lines | Inputs used |
|---|---|---|
| `library/functions/finance-accounting.md` | 177 | b-functions-finance-strategy-procurement §2.1, §3.1, §4.1, §5; archetype YAML (billing-collections, firm-finance, tax data-technology, indirect-tax, security human-risk) |
| `library/functions/strategy-planning.md` | 148 | b-functions-finance-strategy-procurement §2.2, §3.2, §4.2; b-functions-delivery-risk SD-3 (cross-reference); archetype YAML (firm-finance, talent-learning, scoping-pricing, transfer-pricing) |
| `library/functions/procurement-supply-chain.md` | 156 | b-functions-finance-strategy-procurement §2.3, §3.3, §4.3; b-functions-commercial (MCKINSEY-SOAI-2026 cost exhibit); archetype YAML (all six procurement entries) |
| `library/functions/sales-marketing-bd.md` | 162 | b-functions-commercial §2.1, §3.1, §4.1; archetype YAML (client-development, pursuit-proposals, scoping-pricing) |
| `library/functions/customer-service.md` | 171 | b-functions-commercial §2.2, §3.2, §4.2, §5; archetype YAML (all three customer-service entries) |
| `library/functions/product-service-development.md` | 158 | b-functions-commercial §2.3, §3.3, §4.3, §5; archetype YAML (all four product entries) |
| `library/functions/people-hr.md` | 181 | b-functions-people-technology §2.1, §3.1, §4.1, §5; archetype YAML (talent-learning, quality-management, human-risk) |
| `library/functions/technology-it.md` | 191 | b-functions-people-technology §2.2, §3.2, §4.2, §5; archetype YAML (security application-security, operations, incident-response; knowledge-management; tax data-technology) |
| `library/functions/service-delivery.md` | 185 | b-functions-delivery-risk §2.1, §3.1, §4.1, §5; archetype YAML (delivery-management, work-production, security operations) |
| `library/functions/risk-compliance-legal.md` | 186 | b-functions-delivery-risk §2.2, §3.2, §4.2, §5; b-functions-finance-strategy-procurement (Treasury); archetype YAML (governance-risk, ai-security, controversy, acceptance-risk, work-production, knowledge-management) |
| `library/journey-stages.md` | 250 | b-journey-stages §1-§6 (Tables A and B, stage profiles, examples, failure analyses); `method/onboarding.md` §5 (read to avoid repetition, linked not restated) |
| `library/index.md` | §7, §8 only | One sentence linking `journey-stages.md` in §7; each function id linked to its card in §8; the "not yet in this version" paragraph replaced. §3 and all other sections untouched |
| `method/onboarding.md` | 284 | One pointer line to `../library/journey-stages.md` at the end of §5 (file stays under 300) |

`python3 scripts/validate.py`: 0 errors (23 pre-existing warnings on archetype YAML targets). Every archetype id cited in the 11
files was checked against the YAML; all exist and every cited grade matches.

## Conflicts resolved

**Source keys unified across files** (the same document gets one key):

| Input keys | Key used | Reason |
|---|---|---|
| TREASURY-2024, TREASURY-FISCAL-2024 | TREASURY-2024 | Same press release |
| NIST-2023 (AI RMF plus 600-1 in one row), NIST-GENAI-2024 | NIST-AIRMF-2023, NIST-AI600-1-2024 | Two documents; one key each |
| EUAIA-2024, EUAIACT-ANNEX3-2024 | EU-AIACT-ANNEX3-2024 | Matches the archetype YAML key |
| EU-AIACT-2024 (Article 50), EUAIACT-ART14/ART26-2024, EUAIA-EXPLORER-2024 | EU-AIACT-ART50-2024, EU-AIACT-ART14-2024, EU-AIACT-ART26-2024, EU-AIACT-ART4-2024 | One key per article |
| MCKINSEY-2026, MCKINSEY-STATEAI-2026 | MCKINSEY-SOAI-2026 | Same survey; matches onboarding's MCKINSEY-SOAI-2025 style |
| HBS-2023, HBS-JAGGED-2023 | HBS-DELLACQUA-2023 | Archetype YAML key (onboarding §11 still uses HBS-JAGGED-2023; not edited) |
| IAI-2025 (Scottish consultation), IAI-CONSULT-2025 (DWP consultation) | IAI-CONSULT-SCOT-2025, IAI-CONSULT-DWP-2025 | Two different evaluations of the same tool |
| KP-TPMG-2025, KP-AISCRIBE-2025 | KP-AISCRIBE-2025 | Same page |
| GITHUB-PENG-2023, PENG-2023 | PENG-2023 | Same paper |
| METR-2025 (journey), METR-RCT-2025 | METR-RCT-2025 | Same study (journey file does not cite it after trimming) |
| OPENAI-MORGANSTANLEY | OPENAI-MORGANSTANLEY-2024 | Key needs a year; 2024 is the input's inference from page assets, stated in the source entry |

**Grades changed under the A rule (2026-10-17) and the "tool evaluation is not a work outcome" rule:**

| Item | Input grade | Grade used | Reason |
|---|---|---|---|
| Colgate-Palmolive synthetic consumers (MAIER-2025) | A "with caveat" | B | Retrospective test of a method on historical surveys, not a work outcome |
| Microsoft root-cause analysis (MS-RCACOPILOT-2023) | A | B | Accuracy is an offline evaluation on past incidents |
| DWP Copilot trial (DWP-COPILOT-2026) | A (journey input) | B | Outcome is categorical self-reported time; the delivery-risk input grades the GDS and HMRC trials of the same tool B for the same reason |
| Law-student randomized study (UMN-SCHWARCZ-2025) | ungraded | D (experiment only) | Follows the finance input's convention for experiments with no deployment |
| Legal research benchmarks (STANFORD-MAGESH-2024, VALS-VLAIR-2025) | ungraded | Presented as evaluations, not graded examples | Tool benchmarks, not deployments |

**Other conflicts:**

- **Experiment grading conventions differ between inputs.** The finance input grades experiments D; the commercial input grades the
  P&G field experiment A. Kept P&G at A (named organization, real challenges, measured) and said it was a one-day task, not a rollout;
  experiments with no deploying organization stay D.
- **Air Canada amount.** The commercial input gives a fare difference of about C$870; the delivery-risk input gives an award of $650.88.
  The risk card uses the award (MCCARTHY-MOFFATT-2024); the customer-service card states liability with no amount (CRT-2024).
- **Walmart routing figures** differ between the paper ($91.5 million, 98.6 million pounds CO2) and the award release ($75 million,
  72 million pounds). Both are shown, with the note that neither source explains the difference.
- **Klarna** appears in three inputs. The measured 2024 figures are used; the "700 agents" and "$40 million" estimates are not (estimates,
  and a headcount framing). The reversal uses MAGINATIVE-2025 in the customer-service card and ENTREPRENEUR-KLARNA-2025 in the journey
  file, as each input did.
- **Pattern assignments** where an input gave none (commercial and journey items) are the advisor's classification: agent assist and
  service-to-sales assistants as `grounded-knowledge-assistant`; handoff analysis as `monitor-diagnose-act`; CRM capture as
  `bulk-transformation`; outbound sequence agents, AI ideation teammates, synthetic panels, generative discovery and voice interviewers as
  `other` with a description; case summaries and free-text classification as `document-to-decision`.
- **Lens placement.** Augment-level items with process scope (for example close acceleration, generative discovery) are placed under
  "Improve the step" because a person stays on the path; scope is shown on each item.
- **Unsourced inferences in the inputs** (payment release as the control point; juniors' skill erosion from Bainbridge) are kept only
  where labelled as advisor rules or inferences.

## Gaps

- `library/patterns/bulk-transformation.md` did not exist when the cards were written; the finance, sales-marketing-bd and
  technology-it cards link to it. The other ten pattern files existed. Links in cards are not checked by the validator.
- Delegate-lens evidence is absent or archetype-only in every function card; each card says so.
- No function has published override, escalation or parallel-run rates from a named in-house team; cards say so in "Read this first".
- Strategy-planning and product-service-development have no measured in-house deployment beyond experiments and public-sector
  consultation analysis.
- Items dropped from the journey file to meet 250 lines: NANDA's partnership-versus-build signal, Guardian Life's underwriting pilot,
  Italgas training hours, Schaeffler, Gartner's search-only maturity survey, the AI Index incident count, and the controlled studies
  (Brynjolfsson, HBS, METR), which are in the function cards instead.
- Input gaps carried forward: APQC category files gated (process lists are working groupings); EU AI Act dates under the Digital
  Omnibus not verified in the Official Journal; several search-only items (Gartner HR, SupChains, IndiaMART) cited only as C or D or
  flagged search-only.
- The journey file's mapping of the five stages to published models is a working alignment that no source validates (stated in §9).
