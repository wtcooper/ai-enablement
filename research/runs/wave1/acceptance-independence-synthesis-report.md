# Synthesis report: assurance / acceptance-independence

- **Date:** 2026-10-16
- **Inputs:** `landscape-assurance.md` (section 10 and 13 leads), `assurance-acceptance-independence-practice.md`,
  `-discourse.md`, `-governance.md` (all in `research/runs/wave1/`)
- **Outputs:** `plugins/.../archetypes/assurance/modules/acceptance-independence.md` (293 lines) and
  `plugins/.../archetypes/assurance/use-cases/acceptance-independence.yaml` (21 entries)
- **Validator:** `python3 scripts/validate.py` gives 0 errors. It warns that the A/B share (14%) is below the 50%
  target. The share was not raised: no grade was inflated (see "Why the A/B target is not met").

## 1. Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidates in | 16 (1 B, 8 C, 7 D) | 15 (4 B, 3 C, 8 D) | 14 (0 B, 6 C, 8 D) | 45 |
| Out | | | | 21 (0 A, 3 B, 12 C, 6 D) |

One candidate was dropped and routed elsewhere: discourse-15 (independence criteria for firms giving assurance over AI
developers). It goes to other-assurance (assurance over AI). Its sources are a technology commentator's Substack and a
press relay, so it does not meet the "practitioners or regulators discuss it" bar for a D entry here. All other
candidates were merged into the 21 entries.

## 2. Duplicates merged

| Out | Merged from | Grade decision |
|---|---|---|
| 01 Conflicts and independence clearance (Crete PA, Intapp) | P01 | B kept |
| 02 Risk-scored acceptance workflow | P03, G01, G05 (ML acceptance-scoring prototype, D) | C. G05 folded in as the same change; no standalone D |
| 03 Grant Thornton UK and Fenergo onboarding platform | P02, D01 | C (announced, not shown live) |
| 04 AML onboarding: document classification, risk scoring, PEP/sanctions triage | D02, D03, G06 (D) | C (vendor pilot). The regulator material in G06 is used as guardrails |
| 05 Family-tree extraction | G02 (+ EY UK baseline from practice notes) | C |
| 06 Independence monitoring, breach handling, holdings checks | G03 (+ EY GMS and Intapp employee-compliance from practice notes) | C |
| 07 Rotation matching | G04 | C |
| 08 Engagement-letter automation | P05 (26% figure also in G08) | C |
| 09 Pricing and targeting from acceptance data | P04 | C |
| 10 Idea: client AI reliance at acceptance | P07, D04, G07 | D |
| 11 Idea: engagement terms on AI use and consent | P06, D05, G08 | D (LearnFormula dropped as low authority) |
| 12 Idea: audit-committee communication on auditor AI use | G14 | D |
| 13 Idea: AI tool-vendor contract and licence review | P11, P12, D09, G09 | D |
| 14 Idea: clearing AI alliances | P13, D10 | D |
| 15 Idea: permissibility gate for AI services to audit clients | P14, D11 (B), G10 | **D. Discourse graded B; downgraded** because the named deployment (Deloitte's pre-approval workflow) is not shown applied to AI services, and applying it to them is the whole use case |
| 16 PE/APS pre-transaction due diligence and governance safeguards | D06 (B), D14 (D) | B (Grant Thornton UK's completed Cinven structuring) |
| 17 Client screening against the investor group; regulator consultation | D07 (B), G11, P16, D08 (D) | B (Grant Thornton UK's stated practice and FRC case) |
| 18 Gtap inside an APS; shared-platform governance | P08, G12, D13 (D) | C |
| 19 Modus | P09 | C |
| 20 AI-native audit firms (Repodo, Oath) | P10, D12 (B), G13 | **C. Discourse graded Oath B; kept at C**, as practice and governance did. The firm and its APS are real, but no source shows AI delivering audits, which is what the use case describes |
| 21 Fee renegotiation | P15 | C |

**Source-key canonicalisation.** Where two inputs gave the same document different keys, one key was chosen. Keys
are reused from the controls-testing file where that file already holds the document.

| Canonical key | Input keys |
|---|---|
| IFIAR-2025F | IFIAR-SURVEY-2026 (practice) |
| AICPA-PA | AICPA-PA-2026 (all angles) |
| CPACOM-ATR | CPACOM-ATR-2025 (practice, governance) |
| VERDANTIX | VERDANTIX-KPMGFEE-2026 (practice) |
| FRC-GENAI | FRC-GENAI-2026 (governance) |
| KINGLAND-ACCEPT | KINGLAND-ACCEPT-2026 (practice), KINGLAND-ACCEPT (governance, landscape) |
| STARLING-HOHL-2026 | STARLING-HOHL-2026 (practice), STARLING-HOHLWSJ-2026 (governance) |
| JOFA-NILSEN-2025 | JOFA-OUTSIDEINV-2025 (practice), JOFA-NILSEN-2025 (discourse, governance) |
| JOFA-PEED-2025 | JOFA-PEED-2025 (practice), JOFA-ED-2025 (discourse) |
| JOFA-ETHAI-2026 | JOFA-ETHAI-2026 (practice, discourse; /news/ URL), JOFA-ETHICSAI-2026 (governance; /issues/ URL; same title and date) |
| ICAS-IESBASNAP-2026 | ICAS-IESBASNAP-2026 (discourse), ICAS-IESBA-2026 (governance) |
| AE-BEYONDPE-2025 | AE-BEYONDPE-2025 (discourse), ACCEU-PE-2025 (governance) |
| NYSSCPA-HOHL-2025 | NYCPA-HOHL-2025 (discourse) |
| IESBA-NAM-2026 | practice (landing page) and governance (PDF); the PDF URL is used |
| AICPA-APSED-2025 | practice (PDF, 2025-12-29) and governance (landing page, 2025-12); the PDF URL is used |
| KPMG-HOHL-2026 | typed `firm` (the publisher), not `regulator` as in practice |
| JOFA-* items | typed `professional-body` throughout (discourse and governance typed some as `press`) |

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 09, 10, 11, 12, 13, 15 | 14, 17 | 16, 21 | 10 |
| augment | 04, 05, 07, 08 | 01, 02, 03, 06 | 18, 19 | 10 |
| automate | none | none | none | 0 |
| delegate | none | none | 20 | 1 |
| Total | 10 | 6 | 5 | 21 |

- **Automate: no evidence.** No source describes an acceptance, KYC or independence step with no person on the normal
  path. The nearest is Kingland's check of new holdings within 24 hours of a trade, which the vendor describes as
  automation, not AI. It sits in entry 06.
- **Delegate: one case, grade C** (AI-native firms, entry 20). No AI agent is shown owning an acceptance or
  independence outcome.
- Ten `assist` entries are human control steps created by AI-related change. Their ladder value is nominal, and each
  entry's notes say so.

## 4. Grade mix

0 A, 3 B (14%), 12 C, 6 D. The three B entries are 01 (Crete PA's in-use conflicts tool, vendor-published, 2024) and
16 and 17 (Grant Thornton UK's PE structuring and investor screening, which involve no AI).

**Why the A/B target is not met.**
1. No angle found a measured outcome from a named organisation for AI in acceptance, KYC or independence work. So no
   A is possible.
2. There is only one named, in-use AI deployment (01). Every other direction-1 item is a vendor product page, a vendor
   pilot or a "selected" announcement (C).
3. Direction 2 has strong regulator and professional-body material. That material is guidance, a draft or a
   comment-letter debate, which is grade D by definition, or a funding announcement, which is grade C.
4. Two discourse B grades did not survive merging (entries 15 and 20, explained above). Keeping them would have raised
   the share to 24% by grading the wrong thing.

Raising the share would mean dropping the D and C entries that the advisor most needs as risk prompts. Instead, the
module says plainly where evidence is missing.

## 5. Gaps

- **No quality evidence of any kind:** no error, false-positive, override, missed-conflict, parallel-run or
  inspection result for AI in these steps.
- **No named Big Four or mid-tier case** of AI changing an acceptance decision, a client risk score or a fee. Big Four
  transparency reports describe their independence systems without AI.
- **Primary texts not read:** the AICPA practice aid (member-gated; press accounts used), PEEC's second exposure draft
  (meeting on 19 Oct 2026, after this date), SEC refreshed FAQs, PCAOB project pages (blocked), the IESBA AI-specific
  publication (due Q4 2026), the FRC Ethical Standard, and FATF guidance.
- **Unconfirmed:** the Financial Times report that AI alliances leave EY as Anthropic's likely auditor. It was read
  only through low-authority relays.
- **Thin source types for this module:** no job postings, no community forum discussion, one conference agenda (KU)
  with no slides, and no regulator primary speech texts.
- **Not used:** Intapp's claims of use at 16 of the top 20 firms and at 10+ of the top 25 (snippet or blocked);
  CAQ-PULSE-2026 client AI-governance figures (landscape only, no URL; routed to planning); IRBA-PA-10 and
  TR-ACCEPT-2025 (landscape leads with no AI content).
- **Disclosure:** entries 14 and 15 cite Anthropic releases for the fact and scale of alliances. Anthropic makes the
  model that produced this synthesis.

## 6. Routed to other modules (collected from the inputs)

| Item | Target | Sources |
|---|---|---|
| Independence of those auditing AI developers; AI assurance services as products; ISO/IEC 42006 rules; synthesis-dropped discourse-15 | other-assurance (assurance over AI) | GOPALAN-SUBSTACK-2026, CONSULTANCY-BIG4AI-2025, DELOITTE-UKTR-2025, KPMG-AUTR-2025, IESBA-EEA-2026, CSA-AIASSURE-2026 (landscape) |
| SOC 2 tool-provider arrangements, bundled fees, referral terms; peer-review alert; "fast and easy" SOC | other-assurance (SOC) | JOFA-SOCETH-2026, JOFA-PRB (= JOFA-PEERREV-2026), JOFA-FAST (= JOFA-SOCFAST-2026) |
| Firm AI tool approval, certification, monitoring; supervision of AI output; data-training rights in vendor contracts; SEC question on using AI to monitor quality control; QC 1000 amendments; PCAOB inspection shift to quality-management systems; regulators' own AI use in inspections | quality-management | AICPA-PA (Part 2), JOFA-ETHAI-2026, KPMG-HOHL-2026, TR-HOHLAGENDA-2025, JOFA-PCAOBQC-2026, IESBA-NAM-2026, AT-PCAOBPE-2025 |
| PCAOB quality-control inspections of PE and APS firms; Inspections Modernization Council | quality-management | AT-PCAOBPE-2025, BLOOMBERG-PCAOBPE-2025 |
| Understanding the entity's AI use; AI-operated controls; client AI governance maturity (6% advanced) | planning-risk-assessment; controls-testing | AT-AICPAPA-2026, CAQ-PULSE-2026 (landscape) |
| Gtap, EY Canvas agents and Modus workflows as audit-execution tools | planning-risk-assessment; controls-testing; substantive-testing | GT-GTAP-2026, EY-CANVAS-2026, AT-MODUS-2026 |
| Revised "attest engagement team" definition, which excludes external specialists (effective 15 Dec 2026); heavy client AI reliance compared with specialists and complex valuation models | specialists | JOFA-PEECTEAM-2026, AT-AICPAPA-2026 |
| Audit-committee communication about AI; PCAOB research project on audit-committee communications | completion-reporting | KPMG-HOHL-2026, JOFA-PCAOBAG-2026 |
| PE investment, fee pressure, AI-native entrants, junior skill erosion, graduate intake, "accountant engineers" | cross-cutting lens: audit firm business model and workforce | VERDANTIX, AT-PCAOBPE-2025, AT-MODUS-2026, FINSTORY-OATH-2026, EARMARK-2026, IRISHTIMES-GT-2026, AAA-CIIA-2025 |

## 7. Suggested improvements to the briefs

1. **Add a "control step created by AI change" marker to the vocabulary.** Half of this module's entries are human
   steps triggered by AI elsewhere, and `ladder: assist` with `pattern: other` misrepresents them. A field such as
   `ai_role: firm-tool | client-ai | vendor-ai | structural` would make coverage tables honest.
2. **Define B for model-level entries.** Angles disagreed on whether a named, licensed AI-native firm or a deployed
   non-AI workflow counts as a "named real deployment". State that the deployment must be of the change the entry
   describes.
3. **Give researchers a shared canonical-key list before the deep dives.** Fifteen documents arrived under two keys,
   and source types for JofA and the KPMG-hosted SEC Q&A differed across angles.
4. **Allow the A/B target to vary by module, or report it as density.** Modules where governance leads practice will
   always fail a fixed 50% target unless grades are inflated.
5. **Budget web searches per angle.** All three angles ran out of quota before reaching vendor customers, transparency
   reports and podcasts.
6. **Tell angles which landscape sources to reopen.** Discourse did not reopen Gtap, Modus or Repodo, and practice did
   not reopen the KU panel, which caused avoidable "unverified" notes.
