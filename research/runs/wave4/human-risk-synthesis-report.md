# Human risk: synthesis report

Archetype: security. Module: human-risk. Compiled 2026-10-17.

Outputs:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/human-risk.md` (254 lines)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/human-risk.yaml` (18 entries)

## Counts in and out

- In: 21 candidates from the single combined deep dive (A 6, B 3, C 7, D 5), plus routed items from five other
  security files (identity-access discourse, governance and practice; threat-intelligence discourse and practice;
  governance-risk practice). The landscape scan's human-risk list added no new use case.
- Out: 18 use cases. A 2, B 7, C 5, D 4. A/B share 50% (meets the validator target exactly).

## Duplicates merged and entries dropped

| Out | Merged from | Why |
|---|---|---|
| `#01` | deep-dive 01 (Qualcomm) + the Avanade cohort benchmark outcome from deep-dive 02 | The benchmark measures training, not triage |
| `#02` | deep-dive 03 (Uber HRM) + deep-dive 18 (TrainShield/CyberGLA LLM coaching, idea) | Same change: risk events trigger just-in-time micro-training |
| `#08` | deep-dive 08 (Valvoline/Abnormal) + deep-dive 09 (Adaptive post-delivery email security) | Same change: an AI layer removes reliance on users noticing what filters miss |
| dropped | deep-dive 17 (deepfake voice/video detection) | Duplicates `security-identity-access-23` (C, more evidence); cross-referenced in the module |

Cross-references kept instead of duplicating: `security-operations-04` (phishing triage agent; `#07` keeps the
reporter-loop view), `security-threat-intelligence-18` (takedown evidence agents; next to `#10`),
`security-threat-intelligence-21` (Datadog fake-applicant hunting; source added to `#12`),
`security-identity-access-18` (help-desk verification; next to `#13`), `-19` (ML identity proofing; next to `#12`),
`-23` (synthetic-voice detection).

Routed items picked up: Above Security insider investigations (SWI-BLACKHAT-2026) into `#15`; Proofpoint's 37% AI
data-loss figure (PROOFPOINT-VOC-2026) into `#16`; Datadog FIRST session, Nametag video-verification limits and the
IC3 interview voice-spoofing point into `#12`; FBI voice-impersonation PSA (FBI-IC3PSA-2025) into `#13`; USENIX
romance-baiting study, Okta/Yubico survey, Pindrop readiness survey and ENISA 2025 into module metrics, frontier and
objections. Memcyco takedown agents stay in threat-intelligence (cross-referenced). Not used: IC3's "AI-involved
employment scams of almost USD 13 million" (it was unclear whether victims were employers or job seekers).

## Grade changes under the 2026-10-17 grade A rule

| Out | Deep-dive grade | Final | Reason |
|---|---|---|---|
| `#01` | A | A (low confidence) | Avanade's three-month, two 1,000-user cohort benchmark is a measured comparison the named organisation ran; vendor-published, not randomised, simulation metrics only. Qualcomm's figures alone are B (two inconsistent headline figures, no baseline) |
| `#02` Uber | A | B | Rounded figures, no baseline, period, population or method; cannot be told from estimates |
| `#07` Avanade triage | A | B | "Over 900 hours ... by one calculation" and a 98% reduction with no baseline: estimates |
| `#08` Valvoline | A | B | USD 600K loss avoided (no method) and 480 hours beside a director's recollection |
| `#10` ARK/Doppel | A | A (low confidence) | Tracked operating metrics (median 5.5 h resolution, 98% success) for a named customer, consistent with how `security-identity-access-21` was graded; ARK's own before/after figures are recollections (B), kept and labelled |
| `#14` RedChronos | A | B | Abstract only; "approximately 90%" with no baseline or method; production status unclear |

All figures were kept with their provenance.

## Coverage

- Ladder: assist 3, augment 11, automate 3, delegate 1. The only delegate entry (`#11` scam-baiting) is a research
  system; no organisation was found letting an agent own a human-risk outcome.
- Change scope: step 9, process 9, model 0. **No evidence of model-level change** (new services, sourcing, who does
  the work). Stated in the module; nothing invented.
- Maturity: in-production 6, piloting 3, announced 5, emerging 4.

## Ref normalisation

- NYDFS-AI-2024 to NYDFS-AIGUIDE-2024 and FBI-IC3-2026 to FBI-IC3-2025 (the 2025 Internet Crime Report), to match
  identity-access.yaml.
- FINCEN-DEEPFAKE-2024 in the deep dive is FinCEN's news release; renamed FINCEN-DEEPFAKE-NR-2024 because
  identity-access.yaml uses FINCEN-DEEPFAKE-2024 for the alert PDF.
- ADAPTIVE-BLOG-2026 named two pages in the deep dive; split into ADAPTIVE-HOME-2026 (homepage) and
  ADAPTIVE-BLOG-2026 (blog index).
- OKTA-YUBICO-2026 = OKTA-AUTHSURVEY-2026 (identity-access canonical key used).
- Missing sources added where the deep dive cited a ref in risks but not in the entry's sources (ARXIV-2608.02296 in
  `#03`; ICO-MONITORING-2023 in `#16`).

## Gaps

- No independent error, override or missed-attack rate for any AI defence in this module (triage, personalised
  training, insider detection, deepfake detection).
- Every named defender outcome is on a vendor page; case pages are mostly undated (years are estimates).
- ENISA 2025 conflict: the human-risk deep dive says over 80% of "observed social engineering activity" was
  AI-supported; the identity-access governance file says over 80% of "phishing emails" (citing KnowBe4). The module
  flags this; someone should check the report.
- Blocked or unopened: CISA Insider Threat Mitigation Guide (the landscape's item 3), SANS 2026 awareness report body,
  Proofpoint State of the Phish 2026, Verizon DBIR 2026 body, Ponemon/DTEX report, Gartner and Forrester HRM research.
- Not found: DEF CON 34 vishing-bot results, ScamBench scores, named customers for vishing or deepfake training,
  works-council or union positions on behaviour scoring, sector regulators other than NYDFS on awareness training.
- The landscape's novice-learner CTF study (ARXIV-2602.18172) was not examined by the deep dive.

## Suggested improvements to the briefs

1. Ask deep dives to apply the grade A rule themselves and to separate "tracked platform metric on a vendor page"
   from "customer estimate on a vendor page". This module's six A candidates needed re-grading, and the line between
   these two cases decided two of them.
2. Give low-density modules a list of the other modules' published ids at research time, so overlaps (phishing
   triage, voice deepfake detection, fake applicants) are cross-referenced at source, not at synthesis.
3. Require one key per document across the archetype (publish a shared ref register); this module needed four renames.
4. For "Routed to other modules" items, ask for the full source row and locator, not just the key, so the receiving
   synthesis does not have to search other files.
5. Ask for a deliberate search for in-house (non-vendor) accounts of AI in awareness programmes, such as conference
   talks by practitioners, since the vendor-only evidence base caps grades.
