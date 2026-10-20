# Verification report: library patterns and index §3

Date: 2026-10-20. Scope: the 11 files in `references/library/patterns/` and §3 of `references/library/index.md`.
Method: every cited URL (157 unique, 244 source lines) was downloaded and converted to text. Blocked pages were read
through a text mirror, Europe PMC, the publisher's own PDF or scholarly APIs. Each attributed statement, figure, date,
grade, regulatory point and archetype id was checked against that text. Grades follow the vocabulary and the
2026-10-17 grade-A rule. `scripts/validate.py` ran after editing: 0 errors (23 warnings, all in archetype use-case
files outside this scope).

## Counts

| Item | Checked | Kept | Fixed | Removed |
|---|---|---|---|---|
| Cited statements in body text (a citation instance each) | ~536 | ~507 | 26 | 3 |
| Graded evidence rows (§9 tables) | 91 | 82 | 9 (1 grade change) | 0 |
| Source entries (key, title, date, URL) | 244 | 233 | 11 | 3 replaced or dropped |
| Archetype use-case ids cited | 88 | 88 | 0 | 0 |
| Index §3 rows | 12 | 11 | 1 | 0 |

The three removals are Ramp's "85% fewer manual reviews", which is not in the cited post; the claim that a court let
the UnitedHealth claims proceed, which the cited 2023 article on the filing does not contain; and the WUNC press
source, replaced by the VA inspector general's report itself. The only grade change is the Australian Treasury trial
from A to B. Every archetype id exists, carries the cited grade and, where tagged, the right pattern. Three ids are
cross-pattern references (`tax-research-advisory-12`, `tax-compliance-corporate-21`,
`professional-services-talent-learning-11`); their content fits the use made of them.

Structure: every body key resolves to a listed source with a URL and an ISO date, and every listed source is used.
All files are under 300 lines and have a table of contents. Relative links resolve. No file recommends a vendor:
product names appear only as cited evidence.

## Fixes and removals

| File | Claim | Action | Reason |
|---|---|---|---|
| intake-triage | §3 delegate row said delegate triage was "only seen in security operations ... evidence-gated dismissal" | Fixed: the only delegate intake-triage use case is security-vulnerability-exposure-01; security-operations-01 is automate and closes only high-confidence false positives | YAML ladder values; unsupported "evidence-gated dismissal" |
| intake-triage | Copenhagen EMS trial provenance "independent" | Fixed to "peer-reviewed; run by the service's own researchers" | Lead author is at Copenhagen EMS; attribution |
| document-to-decision | Ramp "85% fewer manual reviews" and "policy citations" | Fixed: removed 85% (not in the cited post); outcome now 99% (undefined) and 10–15% escalated; "rationale ... logged" only | Figure not in source |
| document-to-decision | VA survivor-benefit row and §6 sourced to WUNC (attorney's paraphrase "8,000 of 8,100"; "98% of letters") | Fixed: replaced with the VA OIG report 25-00153-47 (2026-04-30): at least 8,000 decisions or letters deficient; at least 2% legal errors, about $2.7m improper payments | Better primary source; misread statistic (98% was a rounding of the decision count, not a letter count) |
| document-to-decision | "National random samples missed the automated VA claims" | Fixed: VA planned no check beyond possible random selection for routine quality review | Embellished; not what OIG says |
| document-to-decision | VBA 61.3 vs 25.1 days "no reliable timeliness study" | Fixed wording: in-house metrics, no specific study, so leaders could not know | Precision |
| document-to-decision | "Not where review is staffed and scored on speed" | Fixed: "set up for bulk sign-off at speed (1.2 seconds a case)" | Source does not say reviewers were scored on speed |
| document-to-decision | "Not when the builders are the only measurers of quality" | Fixed: quality check inside the project team; 100% internal accuracy unquestioned | Closer to source |
| document-to-decision | Kumar 99.1% at 80% coverage | Fixed: added "267 test fields" and "preprint" | Small test set; preprint |
| document-to-decision | UnitedHealth row "Court let contract claims proceed" | Fixed: source is a 2023 article on the filing; now "lawsuit alleges over 90% of appealed denials overturned" | Claim not in cited source (later event) |
| document-to-decision | 0.2% appeal rate | Fixed: attributed to a KFF analysis of 2021 denials, cited by the press | Attribution |
| document-to-decision | CFPB "no special exemption" quotation | Fixed: replaced with paraphrase of what the circular says | Quotation not in source |
| document-to-decision | California SB 1120 "licensed physician" | Fixed: "licensed physician or other competent health care provider" | Source wording |
| document-to-decision | GOV-CONSULT-2025 key | Fixed: renamed DSIT-CONSULT-2025 to match research-brief (same document) | One ref per document |
| draft-review-loop | 60% unchanged and median 23 seconds cited to the DSIT press release | Fixed: re-cited to IAI-SCOT-2025 (i.AI evaluation report), where the figures appear; press-release source dropped from this file | Attribution to wrong document |
| draft-review-loop | "checking can cancel the time saved" (Stanford pilot) | Fixed: "the time saved can fail to appear"; §6 failure renamed "No time saved end to end" | Unsourced cause; the study measured no change, not why |
| draft-review-loop | Stanford drafts "visible only to the clinician" | Fixed: clinicians chose to start from the draft or a blank reply | Not in source |
| draft-review-loop | Chen: "7.1% of drafts judged a severe-harm risk" | Fixed: 7.1% of assessments (11 of 156) | Misread denominator |
| draft-review-loop | UCLA scribe trial provenance "independent" | Fixed: academic; the health system's own researchers | Attribution |
| end-to-end-case-agent | "With three or fewer steps in one system, a workflow flow is enough" [ANTHROPIC-AGENTS-2024] | Fixed: "when the steps can be predicted and fixed in advance" | The three-step rule is not in the source |
| end-to-end-case-agent | Klarna 2025: "CEO said cost had dominated"; metric "a quality measure weighted equally with cost" | Fixed: CEO said AI was cheaper but gave "lower quality"; metric now "tracked alongside cost" | Embellished; "weighted equally" not in source |
| end-to-end-case-agent | Klarna 2024 assistant handles "disputes" | Fixed: refunds and returns | "Disputes" not in source |
| full-population-testing | "$454.0 million identified vs $133.2 million certified savings" (CMS Fraud Prevention System) | Fixed: $454.0m unadjusted vs $133.2m adjusted savings, both certified by HHS OIG | Misread statistic: OIG certified both figures |
| full-population-testing | Emett et al. reviewer finding | Fixed: "in two experiments" added | Qualifier: experimental, not field evidence |
| grounded-knowledge-assistant | Over-sharing claims ("can expose over-shared files", "surfaces files users should not have had", "permissions nobody cleaned") cited to the GDS Copilot report | Fixed: the report only says retrieval inherits user permissions; the over-sharing consequence is now marked guidance | Unsourced connective claim |
| grounded-knowledge-assistant | "Twelve UK government organizations" | Fixed: "UK government (cross-government trial)" | Count not in source |
| grounded-knowledge-assistant | Australian Treasury trial graded A | Fixed: B; the row carries no measured outcome figure | Grade A rule (needs a measured figure) |
| monitor-diagnose-act | CLOUDOPSBENCH-2026 dated 2026-03 | Fixed: 2026-02-28 (arXiv v1 submission date) | Wrong date |
| monitor-diagnose-act | DEEPMIND-BCOOLER-2022 dated 2022-12-15 | Fixed: 2022-11-11 (arXiv first version; v2 was 2022-12-14) | Wrong date |
| monitor-diagnose-act | GODDARD-AB-2012 URL differed from draft-review-loop | Fixed: same PMC URL in both files | One ref per document |
| research-brief | Consult row (60% unchanged, median 23 seconds) sourced to the DSIT press release | Fixed: re-sourced to IAI-SCOT-2025, the evaluation report that contains all three figures | Attribution to wrong document |
| research-brief | CJR: "Eight search tools wrong on over 60% of citation queries" | Fixed: "together answered over 60% ... incorrectly" (range 37% to 94% by tool) | Misread aggregate as per-tool |
| research-brief | "Not where the junior's own research is the learning" cited to a patent-drafting trial | Fixed wording: doing the work is how juniors build expertise; the use case measures this for drafting | Adjacent evidence stated precisely |
| bulk-transformation | Asana $6m estimate "back-of-envelope, per its own lead" | Fixed: the phrase is the newsletter author's; the lead described the per-file method | Attribution drift |
| bulk-transformation | Amazon Java upgrade row | Fixed: added "Amazon also sells the tool" | Vendor interest disclosed |
| bulk-transformation | IBM-2024 dated 2023-08 (key year 2024) | Fixed: ICSE '24, 2024-04 | Date and key consistent |
| service-agent-escalation | Probe answer "start read-only [OPENAI-AGENTS-2025]" | Fixed: the guide rates tools by read or write access, reversibility and financial impact | Paraphrase went beyond source |
| service-agent-escalation | "HMRC ... re-scores its test set" | Fixed: reports intent accuracy on a dated (March 2025) test set | Re-scoring cadence not in source |
| index.md §3 | `monitor-diagnose-act` usual ladder "automate → delegate" | Fixed: "augment → automate" | The pattern file's evidence is augment (Meta, Microsoft) and automate (BCOOLER); at delegate, sources describe plans only |
| 5 pattern files | NIST-SAMPLING-2026 pointed to two different URLs (pmc21, pmc22) | Fixed: one URL (pmc21, §6.2.1) in every file | One ref per document |
| draft-review-loop, grounded-knowledge-assistant | ASIC-AWS-2024 and FINRA-RN2409-2024 titles differed between files | Fixed: same title in every file | One ref per document |
| document-to-decision | Source list out of order after key changes | Fixed: sorted by key | Structure |

## Sources that couldn't be reached directly

All of these were eventually read by another route, so no claim was removed for lack of access.

| Source | Problem | Route used |
|---|---|---|
| PMC articles (Blomberg, Garcia, Chen, Goddard, Wong) | reCAPTCHA on pmc.ncbi.nlm.nih.gov; doi.org blocked | Europe PMC full-text API; text mirror |
| EMETT-CAR-2023 (Wiley) | Cloudflare block | Abstract via Semantic Scholar and OpenAlex (supports the claim; full text not read) |
| POLY-OVERRIDE-2020 | doi.org 403 | JMIR page via text mirror |
| ACM-TRICORDER-2018, PCAOB-AS1105-2026, UIPATH-CCA-2026, OPENAI-MORGANSTANLEY-2026, BCG-2023, ASIC-AWS-2024, FINTECHFUTURES-DANSKE-2017, GARTNER-CSAT-2024, GARTNER-AGENTIC-2025, CALEG-AB3030-2024, ROBODEBT-RC-2023, NEJMAI-LUKAC-2025 | 403 or WAF block | Text mirror |
| SEC-KNIGHT-2013 | 403 to a browser user agent | Direct download with a declared user agent |
| IMDA-2026, MARKUP-MYCITY-2024 | Page body not in the static HTML | Text mirror |
| NBER-BRYNJOLFSSON-2023, GOOGLE-2025, MSFT-RCACOPILOT-2024, DEEPMIND-BCOOLER-2022, STANFORD-LEGAL-2024, ARXIV-WANG-2026, MSR-PENG-2023 | The abstract page lacked the cited details | Full PDF |

## Error patterns seen

- **Attribution to the wrong document (3).** Figures from the i.AI Consult evaluation (60% unchanged, a median of 23
  seconds) were cited to the DSIT press release in two files. A press paraphrase ("8,000 of 8,100", "98% of
  letters") stood in for the VA inspector general's report. The same Consult press release had two different keys.
- **Figures or quotations not in the source (4).** Ramp's 85%, CFPB's "no special exemption", Klarna "disputes",
  and a "three or fewer steps" rule attributed to Anthropic's agent guidance.
- **Misread statistics (4).** HHS OIG's adjusted and unadjusted savings presented as identified and certified; the
  7.1% severe-harm rate's denominator (assessments, not drafts); CJR's aggregate 60% read as a per-tool figure; the
  WUNC "98%" (the decision count, rounded).
- **Embellished qualifiers or causes (6).** "Scored on speed" (Cigna), "cost had dominated" and "weighted equally"
  (Klarna), "checking can cancel the time saved" (Stanford), "national random samples missed" (VA), and "start
  read-only" (OpenAI).
- **Unsourced connective claims (3).** Permission over-sharing cited to the GDS Copilot report, a "twelve
  organizations" count, and "evidence-gated dismissal" in the intake-triage ladder.
- **Attribution drift (3).** A newsletter author's "back-of-envelope" assigned to Asana's lead; "independent"
  provenance for two trials run by the deploying health services' own researchers.
- **Wrong dates (3).** Cloud-OpsBench (2026-03, should be 2026-02-28), BCOOLER (2022-12-15, should be 2022-11-11),
  and IBM's key year against a 2023-08 date (now ICSE '24, 2024-04).
- **Grade inflation (1).** A row with no outcome figure was graded A (Australian Treasury, now B).
- **Vendor interest not stated (1).** Amazon's Java-upgrade figures come from the vendor of the tool used.
- **Inconsistent source entries across files (4 keys).** NIST sampling URL, ASIC, FINRA and Goddard titles or URLs.

No forecast was found presented as fact; the Gartner prediction is labelled as a forecast. Grade A rows were
re-read against the 2026-10-17 rule. The remaining A rows each carry a figure the named organization reports as
measured, or a peer-reviewed or regulator measurement.
