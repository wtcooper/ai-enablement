# Synthesis report: tax / compliance-individual-business

- **Prepared:** 2026-10-17 (wave 2)
- **Outputs:** `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/compliance-individual-business.md` (298 lines) and `.../tax/use-cases/compliance-individual-business.yaml` (25 entries, 81 distinct sources; 8 more sources cited only in the module's Sources list)
- **Validator:** `python3 scripts/validate.py` reports 0 errors. One warning for this module: 40% A/B, below the 50% target. Grades were not raised to meet it.

## 1. Counts in and out

| Input | Candidates | Grade mix in |
|---|---|---|
| Practice deep dive | 17 | A 1, B 9, C 7, D 0 |
| Discourse deep dive | 16 | A 0, B 3, C 10, D 3 |
| Governance deep dive | 15 | A 0, B 2, C 4, D 9 |
| Landscape scan | 0 YAML candidates (13 compliance leads, all already followed by the deep dives) | n/a |
| Routed in from other tax deep dives | 6 items used (see §6) | n/a |
| **Total in** | **48 candidates + 6 routed items** | A 1, B 14, C 21, D 12 |
| **Out** | **25 use cases** | A 1, B 9, C 12, D 3 |

## 2. Duplicates merged

No candidate was dropped outright: every one of the 48 is carried in at least one output entry (D01 and G01 were split across `#04` and `#05`). Merges either joined the same change described by several angles or folded a thin idea into the nearest evidenced entry.

| Out id | Merged from (P = practice, D = discourse, G = governance, R = routed) |
|---|---|
| 01 Organizers, document requests, missing-information follow-up | P04, D05, G12 |
| 02 Extraction and K-1 footnote mapping | P03, D03, G02 |
| 03 H&R Block office data entry | P05 |
| 04 Ready to Review simple 1040 | P01, the Thomson Reuters half of D01 and G01 |
| 05 End-to-end agent for complex individual returns | P02, the Black Ore half of D01 and G01, R: OpenAI Codex pilot with Crete firms (tax-data-technology practice) |
| 06 Partnership, S corporation and trust returns | P09, D02, R: Accounting Podcast episode 477 (compliance-corporate discourse) |
| 07 Trial balance to pass-through workpapers | P10 |
| 08 Agent inside the firm's tax software | P11, R: TaxGPT launch (controversy practice) |
| 09 General agents run taught routines | P17, R: Sam Leon / Claude Cowork episode (compliance-corporate discourse) |
| 10 Deterministic engine plus language model (idea) | G09, plus the TY2025 TaxCalcBench leaderboard from discourse |
| 11 Grounded preparer assistant and research for positions | P07, D08, G08 |
| 12 AI-assisted return review | P08, D07, R: TaxGPT return-review agent (controversy practice) |
| 13 Review controls (idea) | G04, G11 |
| 14 Second Look look-back review | P06 |
| 15 AI-drafted client communications | D06, G15, P12 |
| 16 Delivery, e-signature, Form 8879 | D09 |
| 17 UK self assessment and MTD | P16, R: HMRC generative-AI software guidelines (research-advisory governance) |
| 18 Phased adoption, gates and parallel runs | D04, D16, G03 |
| 19 Policy, approved tools, WISP, vendor diligence | D14, G05, G07, G10 |
| 20 AI pod, champions and training | P14, G14 |
| 21 Disclosure and section 7216 consent | D15, G06 |
| 22 Pricing (idea) | D13, G13 |
| 23 Offshore first-pass replaced by AI | D10 |
| 24 AI-native roll-ups | P13, D12 |
| 25 Taxpayer-side agents | P15, D11 |

Classification decisions where the inputs disagreed: `#02` kept at automate (practice) rather than augment (discourse, governance), because the named products route only exceptions; `#04` kept at augment/step (practice) although discourse and governance classed the combined Thomson Reuters plus Black Ore entry as delegate/process; `#05` kept at A (practice grade), now also supported by the routed Crete pilot, with a note that every figure is vendor-published; `#15` set to piloting because the practice file is internally inconsistent about whether WCG already uses return-based narratives.

## 3. Coverage by ladder and change scope

| Ladder \ scope | step | process | model |
|---|---|---|---|
| assist | 11, 21 | 19, 20 | 22 (idea) |
| augment | 01, 04, 07, 12, 15 | 10 (idea), 13 (idea), 17, 18 | none |
| automate | 02, 16 | 03, 14 | 23 |
| delegate | (n/a by definition) | 05, 06, 08, 09 | 24, 25 |

- Every ladder level and every change scope has at least one entry. **Augment at model scope has no evidence.**
- The automate and delegate entries rest on vendor claims, testimonials and management remarks. The only measured process-level effect is H&R Block's Second Look retention gap, which measures the service, not the AI.
- Model-scope evidence is one B (Multiplier, one adjacent boutique), one C (offshore displacement, commentators only), one C (consumer agents) and one idea (pricing).
- Seven entries (`#10`, `#13`, `#18`-`#22`) are controls, enablement or ideas rather than AI deployments; they are kept because governance is the main live discussion in this module.

## 4. Grade mix

A 1 (4%), B 9 (36%), C 12 (48%), D 3 (12%). A/B = 40%. The single A rests on vendor-published, named-firm figures (Boulay testimonial with "maybe", OpenAI's Crete pilot as summarised by another deep dive); treat it as the thinnest possible A. The module file says so in its header.

## 5. Gaps

- **No independent quality evidence** for AI-prepared returns: no error rate, override rate, parallel-run result, notice rate, inspection finding or disciplinary action. TaxCalcBench tests unaided models on calculation only and is authored by an engine vendor. The only human-preparer error baseline is GAO 2014.
- **Trusts (1041) and S corporations (1120-S):** 1041 evidence is Accrual's own pages and the Crete pilot line; 1120-S appears only as a prediction and a Basis product page.
- **UK and other markets:** one UK vendor (ApariPro), PCRT news items (the guidance itself was not opened) and HMRC's software guidelines; nothing on HMRC agent guidance for self assessment, Canada, Germany or India.
- **Engagement-letter and consent practice:** no firm has published AI consent wording; no AI-specific IRS section 7216 guidance; no IRS reply to the AICPA fee letter.
- **Practitioner communities:** r/taxpros and TaxProTalk were blocked in all three deep dives; Hacker News was the only open forum and its commenters are mostly self-filers.
- **Unverified items:** the OpenAI Crete pilot figures come from a one-line routing summary (the page was opened by the tax-data-technology researcher, not re-read here); whether Sidekick is the OpenAI-built tool; Ready to Review's actual general availability and K-1 roadmap; Black Ore customer-share claims.
- **Not opened anywhere:** CCH Axcess Expert AI news pages, Canopy and Accrual BusinessWire releases, the AICPA small-firm AI policy template, the Blue J/CPA.com and Thomson Reuters State of Tax Professionals reports, the CNBC disclosure article (4 Aug 2026), the AICPA's own AI FAQs.

## 6. Routed items

**Picked up from other tax deep dives and used here**
- OPENAI-CODEX-2026 and RUNTIMEWIRE-2026 (tax-data-technology practice): 1040 and 1041 pilot, 30+ Crete firms, 7,000 returns -> `#05`.
- TAXGPT-2026 (controversy practice): preparation and return-review agents, 45 minutes per 1040 claim -> `#08`, `#12`.
- ACCTPOD-477-2026 and ACCTPOD-SAMLEON-2026 (compliance-corporate discourse) -> `#06`, `#09`.
- HMRC-GENAI-2026 (research-advisory governance) -> `#17`.
- TaxCalcBench, Werfel's extraction risk, PwC K-1 agents, Ready to Review, OPR fee guidance and the AICPA tax software survey were routed here by several files; all were already in the inputs.

**Routed here but not used**
- IRS "Zero Paper" AI routing of paper returns (controversy governance): tax-authority intake, not preparer practice; better in controversy or a tax-authority lens.
- Bloomberg Tax Compliance Tracker AI Assistant (research-advisory discourse), Bloomberg Tax forum panel (controversy governance), Neo.Tax R&D credits (tax-data-technology discourse) and Avalara property tax agents (indirect-tax practice): corporate or indirect-tax compliance; belong in compliance-corporate.
- EY compliance agents and myRSM Tax (research-advisory practice): myRSM Tax is cited in the module's frontier only; EY agents belong in compliance-corporate.

**Routed out of this module's inputs, for other syntheses**
- **compliance-corporate:** KPMG Digital Gateway with Claude (KPMG-ANTHROPIC-2026, 2026-05-20); EY and PwC agent platforms (PWC-MEGNA-2025, Agent OS); Savant and Oxford Industries (SAVANT-2026, 2026-04-28); KPMG Germany tax-department survey; Thomson Reuters corporate tax reports; TEI Tax Tech findings on ownership, training and review (TEI-TAXTECH-2026); Sala's argument on corporate team size (SALA-TAXNOTES-2026).
- **controversy:** notice intake, response drafting and the powers-of-attorney step in Accrual Arc (ACCRUAL-ARC-2026); IRS AI audit selection and cross-matching and advice to build a notice-response workflow (ACCTODAY-2026, an opinion piece whose IRM and TIGTA claims were not checked); Taxpayer Advocate AI disclosures; *Clinco* procedural questions.
- **research-advisory:** CoCounsel, Blue J, Bloomberg Tax and CCH research tools and their accuracy; AICPA survey 65% research use (AICPA-TAXSW-2026); TaxGPT research episode (CPAPA-TAXGPT-2026); TR-CHEAP-2026; Blue J/CPA.com weekly-use figures seen only secondhand; the Stanford legal hallucination study (MAGESH-HALLUC-2024, used here as adjacent).
- **advisory / business model (cross-cutting):** 20% of surveyed firms expanding services, mostly tax advisory (AICPA-TAXSW-2026); "keep 1040 clients to feed advisory" (CPAPA-BLACKORE-2024); fee dispute and AI-native roll-ups.
- **cross-cutting professional responsibility:** OPR, PCRT, TPB, Werfel framework, CART.
- **Accounting archetype (client accounting services, close):** Baker Tilly with Basis (BAKERTILLY-BASIS-2026) and with HubSync (BAKERTILLY-HUBSYNC-2026); Wiss and Sikich with Basis (WISS-BASIS-2024, SIKICH-BASIS-2026); Mercor and Digits close and categorisation benchmarks and Digits Write MCP (ACCTODAY-AIBENCH-2026); BizBuyData paying firms for training data (headline only; a section 7216 concern if client data is supplied).
- **Governance and evidence:** the United States v. Heppner privilege point in a vendor blog (JUPID-7216-2026) was not verified and is not used.

## 7. Source-key consistency across tax modules

Aligned with sibling modules: AICPA-WERFEL-2026 now means the appendices PDF (landscape key) and TAXADVISER-WERFEL-2026 the article; PCRT-AI-2026 means the ICAEW news item and ATT-PCRTAI-2026 the ATT news item; PWC-MEGNA-2025 typed `firm`; TAXCT-CLINCO-2026 typed `professional-body`. Remaining collisions to settle at archetype level: TR-R2R-2025 names two different Thomson Reuters posts (this module: thomsonreuters.com, 2025-12-15; compliance-corporate: tax.thomsonreuters.com blog, 2025-12-19); AICPA-FEES-2026 here vs AICPA-FEE-2026 in compliance-corporate for the same Tax Adviser page, while research-advisory uses AICPA-FEES-2026 for a Journal of Accountancy page; HMRC-GENAI-2026 vs HMRC-GENAI-SW-2026; TPB-GS55-2026 vs TPB-GS-2026 and TPB-AI-2026 for the same guidance statement; MAGESH-HALLUC-2024 vs STANFORD-HALLUC-2024; JOFA-POLICY-2026 vs JOFA-AIPOLICY-2026; ICAEW news item dated 2026-01 in indirect-tax vs 2026-01-19 here.

## 8. Suggested improvements to the briefs

1. **Publish a canonical source-key register per archetype before deep dives start** (or have the landscape assign keys for every primary document). Three angle files and five sibling modules used different keys for the same Werfel, PCRT, TPB and AICPA documents.
2. **Give angle researchers each other's candidate titles** or a shared candidate list, so governance does not re-describe practice deployments as ideas (for example extraction verification, research for positions); 48 candidates collapsed into 25 entries.
3. **Ask routing notes to include the full source row** (title, URL, date, locator and the exact figure wording). The Crete pilot arrived as one line, which limited how precisely its figures could be stated.
4. **Define how to grade a named-firm testimonial estimate** ("maybe 15 or 20 hours", "about an hour"): the practice file graded one A and all three files graded the other B.
5. **Tell researchers to classify ladder and scope per product, not per bundle.** Two angles merged Ready to Review (a draft inside one step) with Black Ore (end to end), which forced a split at synthesis.
6. **Add a governance-only allowance**: let the module hold a fixed number of control entries (policy, consent, pricing, rollout) outside the 15-25 count, so deployments are not crowded out in thin modules.
7. **Budget searches per angle, not shared.** All three deep dives ran out of shared search budget, leaving H&R Block's OpenAI tool, UK practice and trusts unchecked.
