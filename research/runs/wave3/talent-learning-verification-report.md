# Verification report: professional-services / talent-learning

Checked 2026-10-19 against `use-cases/talent-learning.yaml` (25 entries) and `modules/talent-learning.md`.
I opened all 106 cited URLs: 101 in the YAML and 5 cited only in the module. I also opened one new secondary source.
Most pages were fetched directly. When that failed, I used the r.jina.ai mirror for BCG, PwC Jobs Barometer, Colorado,
Illinois, Global Legal Post and Scottish Legal. Every figure, quote, date and attribution was checked against the page
text.

## Counts

| Action | Use cases |
|---|---|
| Kept | 8 (#04, #07, #12, #13, #16, #18, #23, #25) |
| Fixed | 17 (#01, #02, #03, #05, #06, #08, #09, #10, #11, #14, #15, #17, #19, #20, #21, #22, #24) |
| Rejected | 0 |

No grade changed. Final grade mix: **A 2, B 13, C 7, D 3** (60% A/B).

- **#11 (A).** This is a pre-registered randomised trial whose figures match the NBER abstract exactly.
- **#16 (A).** The firm reports a tracked count of 1 million Copilot prompts against a target. That meets the 2026-10-17
  rule, but the figure measures activity only, and the entry already says so.
- **Search-only sources.** ABA 512 and the SRA notice are search-only. Neither supports an A or B grade.

## Fixes and rejections

| Entry / location | Problem found | Fix |
|---|---|---|
| #01 problem | Claimed ILTA shows juniors forming habits and making errors before firm standards apply. ILTA says nothing about juniors (wrong document). | Re-sourced to TRI-ONBOARDING-2026 (associates form AI habits before firm guidance) and TR-FOP-2026 (34% use unsanctioned AI). Added TRI-ONBOARDING-2026 to the sources. |
| #01 guardrail; module §6 | ABA 512 claims had no source that was actually read. | The primary text is still blocked (403 direct, mirror and archive). Added CIVILITY-ABA512-2024 (Illinois Supreme Court Commission on Professionalism, 2024-08-15, read in full). Billing wording now matches it: no charge for learning tools the lawyer will "regularly use for clients". |
| #01 role_evolution and checkpoint | Deloitte's certified practitioners were said to "lead internal and client implementations". The source says they "help support Claude implementations" and internal transformation. | Changed to "support". Removed "client" (embellished). |
| #01, #03 sources | NONBILLABLE-RG-2026 was dated "2026"; the byline says 13 January 2026. | Date set to 2026-01-13. |
| #02 checkpoint and notes | "Human review of every AI-assisted first draft" overstated the source, which says a first draft is never a final submission. Notes said the ChatGPT tool was built at the prior firm, which the article does not say. | Reworded both to match the source. |
| #03 notes and solution | "Nearly 400 hours" was attributed to LawCareers.Net citing Reuters, but no Reuters citation exists. The "300-associate hackathon" was really a hackathon inside a retreat for more than 300 associates. | Corrected the attribution and the hackathon wording. |
| #05 | Harvey Academy was called "a free hub". The source says the certification course is free. | Reworded. |
| #06 | The High Rock CEO's RAG assistant is a proposal ("We could build"), but it was described as a "firm-built assistant". The Duane Morris tool's origin was misattributed. role_evolution said seniors move "from correcting basics" (not in the sources). | Reworded all three to match the sources. |
| #08 | The Bloomberg Law column, read in full on news.bgov.com, names Winston Taylor and Sheppard. The notes wrongly called these "mirror artefacts", and both names are current firm names. A prerequisite, a checkpoint and role_evolution were embellished ("PD budget", "actors and coaches give live feedback", "PD staff become designers"). | Named the firms and tied each line to the source text. |
| #09 | "Recording what a junior challenged and why" was cited to TRI-DESIGNJUDG and TRI-COGDEBT. It is actually in TRI-STANDARDS-2026 (wrong document). "Evidence from outside the professions" was vague. | Added TRI-STANDARDS-2026. Named the evidence: the MIT Media Lab study that TRI cites. |
| #10 | "Responsibility falls on trainees, supervisors and firm" was presented as a regulator position. It is DWF's view. The Legal Cheek source was typed "community". | Attributed to DWF. Type changed to press. |
| #11 | Said "five of the seven authors" have Google ties. The disclosures show six of seven (five employees and one paid contractor), plus Autor's Google fellowship support. | Corrected. |
| #14, #17; module §6 | Colorado: a human-review right "from 1 January 2027" is not in the bill summary, which dates only the developer duties. | Separated the developer-duty date from the right. |
| #15 | "Senior sceptics slow change (TRI-FOPTALENT-2025)" does not appear in the source. role_evolution said AI use is "a condition of progression for juniors and partners alike" (overstated). | Replaced with the source's 39% personal-goals figure. Narrowed role_evolution to what KPMG and PwC's US CEO said, and attributed the "not policing" quote to KPMG's global head of risk services. |
| #19 outcomes | KPMG "-29%" is the press figure, but 1,399 to 942 is -33%. "Latest full year" was vague. | Now shows both figures, for 2023 to 2024. |
| #19 risks | The "free-rider problem" was attributed to Vault and Consultancy.uk; neither says it. The hiring-cycle point left out the columnist's own view that this decline is AI-driven. | Rewrote both to match the sources. |
| #19 role_evolution | "Associate populations skew more senior" was cited to Vault but comes from Citi/Hildebrandt via Law360 (wrong document). "106% in 2025" has a period that SurePoint's report leaves unclear. Consultancy.uk's author was said to "argue for a diamond", but he calls the diamond the most-discussed model and floats flipping the pyramid. "EY and PwC US": the source does not say US. "UK junior hires": the source does not say UK. | Corrected all five. |
| #19 dates | ICAEW-EXPECT was "2026-02"; the page shows 03 Feb 2026. HIGHFLIERS was dated with its modified date. | Set to 2026-02-03 and 2026-02-05 (JSON-LD datePublished). |
| #20 | "64% of IT leaders in a TRI survey": TRI cites someone else's survey. | Reworded. Added source refs to the vendor-interest caveat. |
| #21 | "Skills change faster than it can retrain everyone" is not in Fortune (embellished cause). | Replaced with the source's own wording on non-viable reskilling and misaligned strategy, structure and performance measures. Noted that the USD 865m charges include two divestitures. |
| #22 | "Statutory consultation" (embellished qualifier). The "cause is mixed" line had no refs. | Reworded and added refs. |
| #24 | "Law professors quoted by Vault suggest funding development time outside billing and weighing client feedback and revenue". Vault says nothing of the kind (unsupported). "Inferred, not proven" misquotes TRI-DESIGNL, which says "largely inferential". | Removed the Vault sentence and corrected the quote. Named the author: Seyfarth's chair and managing partner. |
| Several (#01-#03, #15, #16, #18, #21) | Unsourced analyst caveats sat in risks_and_guardrails. | Labelled as "Reviewer note" or given a source ref. |
| Module §2 | Unsourced or embellished rows: "tool knowledge" (TAAP says technical aptitude), "reviewers who never did the work may miss AI errors", "so firms cannot say which tasks must be kept", "skills change faster than firms can retrain". | Rewritten to match the sources. |
| Module §5 | The High Fliers row said "survey of 100 employers" (not stated). The seniorised-roles row said "all sectors" (it is highly AI-exposed sectors). | Corrected. |
| Module §6 | The SRA line implied the 42 reports caused the notice and that the responsibility view was the SRA's. The AI literacy line lacked the Omnibus caveat. | Corrected both. |
| Module §7 | General Assembly was called "a survey vendor". Gilchrist's role was said to cover "learning, KM and AI"; the page body is paywalled and shows only the title. The PwC 67% premium was "advertised", but the source says AI-enabled roles "earn" it. | Corrected all three. |
| Module §9 | "'inferred'" misquote. The Zarwin Baum quote was not verbatim. The cause-of-cuts section left out the columnist's AI-driven view. Two misattributions: "If everyone buys experience, nobody trains juniors" (Vault) and "clients push back on junior hours" (TRI-LEGALWEEK-2026, which is about billing transparency). The probe cross-reference pointed to §9 instead of §7. | Corrected all of them. |

## Sources that could not be fully reached

- **ABA Formal Opinion 512.** Blocked (403 direct, via the r.jina.ai mirror and on the Wayback Machine). A secondary
  summary is now cited, and the source is still marked search-only.
- **SRA warning notice of 17 August 2026.** Blocked by a Cloudflare challenge. It is seen only through DWF and stays
  search-only.
- **Lawyers Weekly (Gilchrist Connell).** The article body is behind a paywall. Only the headline and first paragraph
  were read, and the claim is now limited to those.
- **Primary reports never opened.** The NALP Foundation full report (paywalled), the Citi/Hildebrandt report, the
  SurePoint and BCG Attorney Search reports, and the Telegraph original. Each is cited only through press that was
  read in full, and the YAML notes say so.

## Module targets

- **Use cases:** 25 (target 15-25). Met.
- **A/B share:** 15 of 25, 60% (target 50% or more). Met.
- **Dates:** every source has a URL and an ISO date. Ids are unique, and all vocabulary values pass `validate.py`
  (0 errors).
- **Cross-references:** all seven exist and match their described topics: assurance-quality-management-10 and -25,
  tax-research-advisory-08, tax-compliance-corporate-05 and -21, tax-compliance-individual-business-20, and
  security-governance-risk-21.
- **Quotations:** all under 25 words.

## Error patterns to fix in the briefs

1. **Claims cited to the wrong document from the same bundle.** Examples: ILTA used for a TRI point, Vault for a
   Citi/Hildebrandt point, TRI-DESIGNJUDG for a TRI-STANDARDS point. Briefs should require the locator text to contain
   the claim.
2. **Paraphrases turned into quotations.** Examples: "inferred", and "different, not wrong". Quotes must be copied,
   not reconstructed.
3. **Embellished causes and qualifiers.** Examples: "skills change faster than…", "statutory", "free-rider",
   "senior sceptics", and a proposal described as "firm-built".
4. **Unverified "artefact" judgements.** Real firm names (Winston Taylor, Sheppard) were flagged as mirror artefacts
   instead of being checked.
5. **Derived percentages taken from headlines without recomputing.** Example: KPMG -29% versus -33%.
6. **Regulatory effective dates spread across provisions.** Example: Colorado's 2027 date applied to the human-review
   right.
7. **Counts in disclosures and author lists.** Recount them (NBER: six of seven, not five).
8. **Unsourced reviewer caveats sitting among sourced guardrails.** Label them explicitly.
