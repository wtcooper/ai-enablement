# Synthesis report: advisory / forensic-disputes

Run date: 2026-10-20. Wave 5. Outputs:
- Module: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/forensic-disputes.md` (239 lines, table of contents at the top)
- Use cases: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/forensic-disputes.yaml` (15 entries; `scripts/validate.py` reports 0 errors and one warning: A/B share 40%, below the 50% target)

## 1. Counts in and out

| Input | Candidates | Used |
|---|---|---|
| adv-forensic-disputes-combined.md | 15 use cases (A0, B6, C4, D5) | all 15, renumbered in the same order |
| landscape-advisory.md | 0 use cases; forensic leads (FVS, ACFE, Rule 707, J.S. Held) | context only; its June 2026 Rule 707 "sent back" item stays replaced by the judiciary's September 2026 report |
| adv-x-independence-pricing.md | 0 forensic entries ("no pricing or data-handling entry") | SEC Rule 2-01(c)(4)(x) and the AICPA consent and hosting points, added to entries 01, 06, 07 and the module guardrails |
| adv-x-state-of-ai-disruption.md | 0 forensic entries | deal-tracker item (forensic-firm acquisitions) used as a frontier signal |
| Items routed in from other adv-* files | 5 items | 4 merged (see 2); 1 not usable (ISACA-AIPULSE-2026: the routed text holds no fraud or deepfake figure) |

Out: 15 use cases. A 0, B 6, C 4, D 5 (all D entries labelled "Idea").

## 2. Duplicates merged and normalisation changes

No two combined-file entries described the same change to the work, so none were merged among themselves. Routed items merged into existing entries:
- `-12` (AI-fuelled fraud and AI-washing investigations) took AFP-PAYFRAUD-2026 (from client-accounting-services governance), IAF-AIFRAUD-2026 (from risk-controls discourse) and SEC-AIWASH-2024 (from risk-controls governance) as demand-signal outcomes. Title widened to name payments fraud. Grade stays D.
- `-08` (red-flag screening) took DILIGENT-AUDITAI-2026 (from risk-controls practice) as an announced vendor signal. Grade stays C.

Normalisation changes (vocabulary fit, not new facts):
- `-02` ladder augment → automate (the source describes software matching every item and flagging gaps, people working the flags; the vocabulary's "matching with people reviewing exceptions" example).
- `-11` pattern intake-triage → document-to-decision; `-12` pattern end-to-end-case-agent → other (no source describes an agent).
- Missing source entries added where a ref was cited but not listed (VALID8-HUB-2026 in -01, OMRANI-BEYONDBAR-2024 in -04, AICPA-FVS-2026 in -06 and -07, KTS-EXPERTAI-2026 in -14, VALID8-WP-2025 in -09, SEC-RULE2-01-2026 in -01 and -07). All dates quoted as ISO strings.
- The independence note in the combined file ("likely restricted, not verified") replaced with the SEC rule text as summarised in the independence research; AICPA treatment for private attest clients is stated as unconfirmed.

## 3. Coverage by ladder and change scope

| | step | process | model |
|---|---|---|---|
| assist | 05, 07, 10, 14 | | 11, 12, 15 |
| augment | 01, 04, 06, 08, 09, 13 | 03 | |
| automate | | 02 | |
| delegate | | | |

- **Delegate: no evidence.** The only agentic mention is a scheduled AICPA FVS talk on blockchain tracing (`-13`), with no design described, so it was not labelled delegate.
- **Automate:** one entry (`-02`, B, self-reported narrative).
- **Model scope:** three entries, all D ideas (deepfake examination, AI-fuelled fraud and AI-washing investigations, validation studies under Rule 707).
- **Steps with no use case:** interviews and fact-finding; damages modelling beyond the Weber failure.

## 4. Grade mix

- A 0: no named organisation reports a measured AI outcome for forensic work. The measured figures (ACFE, Redgrave via the CGP re-analysis, FJC survey) are adjacent processes, so they cap at B.
- B 6 (01, 02, 03, 04, 06, 07). 06 and 07 rest on a single firm's own description (J.S. Held); flagged in notes.
- C 4 (05, 08, 09, 10): vendor claims, a recollection in an opinion column, a training deck.
- D 5 (11-15): ideas; three rest partly on scheduled conference sessions, which cannot support A or B.
- A/B share 40%, below the validator's 50% target. Not padded: the C and D entries each add a step or a model-scope idea the B entries do not.

## 5. Gaps

- No error, override or parallel-run figure for AI in accounting-firm forensic work; no survey of accounting-firm forensic teams.
- No Big Four, Kroll, FTI, A&M or Stout forensic AI case study opened (blocked or snippet-only).
- Primary court opinions (Weber, Kohls, Mendones) not read; they rest on law-firm and press summaries.
- AICPA Code treatment of forensic and expert services for private-company attest clients not confirmed; AICPA FVS AI guidelines are members-only.
- No pricing, staffing or junior-pipeline evidence specific to forensic practices.
- Routed but not researched: fraud and misrepresentation findings in diligence, and forged or deepfaked documents in data rooms (from transactions).
- UK Civil Justice Council material is search-only.

## 6. Routed to other modules (for their synthesis)

- **valuation:** IVSC exposure draft on AI disclosure; Valuation Performance Framework; AICPA FVS sessions FVC2631 and FVC2640 (scheduled); BVR report quality-control agents; the valuation side of J.S. Held's IP practice (`-06`).
- **risk-controls:** DOJ ECCP AI questions (DOJ-ECCP-2024); FinCEN deepfake alert (FINCEN-DEEPFAKE-2024); ACFE/SAS governance gaps (18% bias testing, 6% explainability confidence); ACFE Canada session 4C on AI and analytics for ethics and compliance programs; fraud-risk program design behind `-03`; disclosure-control review of a client's AI claims (prevention side of `-12`).
- **client-accounting-services:** payment-fraud screening before bill-pay release stays there (AFP-PAYFRAUD-2026); only investigation is here.
- **professional-services:** Deloitte Australia AU$440,000 report with AI-fabricated citations, after which Deloitte agreed to repay the final instalment (CITYAM-DELOITTE-2025) as a deliverable-quality case; pricing of AI-shortened tracing and review work; engagement-letter AI opt-out as a consent and pricing matter; forensic-firm acquisitions by PE-backed platforms (CPATRENDLINES-TRACKER-2026); junior pipeline in forensic practices (no source found).
- **assurance:** AICPA treatment of expert and litigation services for private attest clients; AI-in-audit guidance (FRC, AICPA practice aid).

## 7. Suggested improvements to the briefs

1. Ask module researchers to list every cited ref in each entry's `sources`; seven entries cited refs only in notes or guardrails.
2. Give a rule for pattern choice on new-service ideas (model scope with no agent): this run used `other` with a note.
3. Have the cross-cutting independence research map each module's services to the AICPA Code as well as the SEC rule, since most clients here are private.
4. Tell researchers that the target A/B share (50%) may be unreachable for thin modules, and that synthesis should report the shortfall rather than pad it.
5. Ask for "Routed to other modules" items to carry their full source line (title, URL, date, access), so the receiving synthesis does not have to search other files for it.
6. Note that ladder labels should follow the vocabulary's worked examples even when a source says "AI-assisted"; the combined file labelled full-population matching as augment.
