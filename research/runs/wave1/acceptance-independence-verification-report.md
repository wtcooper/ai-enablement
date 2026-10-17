# Verification report: assurance / acceptance-independence

Checked 2026-10-16 against the opened sources. Files edited in place:
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/acceptance-independence.yaml`
and `.../assurance/modules/acceptance-independence.md`. `scripts/validate.py`: 0 errors for these files (one WARN: A/B
share below target, which is expected and correct).

Method: every cited URL (71 in the YAML, 10 more listed only in the module) was fetched with curl and read as text
(pdftotext for PDFs). Claims, figures, speakers and dates were checked against the text, including byline,
`article:published_time` and JSON-LD dates. Four sources were added during checking (see below).

## Counts

| Action | Entries |
|---|---|
| Kept (no substantive change) | 2 (`07`, `11`; only locator or notes tidied) |
| Fixed | 19 |
| Rejected | 0 |

No entry needed rejecting: every source exists and was opened. Most fixes are wording, attribution and dates, not
the substance of the use case.

## Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 0 | 0 |
| B | 3 (`01`, `16`, `17`) | 4 (`01`, `16`, `17`, `21`) |
| C | 12 | 11 |
| D | 6 (`10`-`15`) | 6 |
| A/B share | 14% | 19% |

The one upgrade (`21`, C to B) comes from finding the primary report behind the analyst blog. It is not A: the AI
argument rests on unnamed sources and the 14% is a fee change, not a measure of AI efficiency. No grade was raised
to hit the target.

## Targets

| Target | Result |
|---|---|
| 15-25 use cases | Met (21) |
| At least 50% graded A or B | **Not met (19%)**. Expected for this module: no source measures AI in acceptance, KYC or independence work. The B grades are human control steps or a fee negotiation, not AI performance. |
| Every source dated | Met. Five dates are year-only or year-month because the source gives no finer date (`KINGLAND-WP-2024`, `CEBI-2024`, `JB-JAR-2004`, `IFAC-AQ-2026`, `KPMG-AUTR-2025`). |

## Fixes and rejections

| Entry | Fix | Reason |
|---|---|---|
| 01 | "analyse potential conflicts and independence impairments" changed to "analyse potential conflicts"; Intapp page date set from retrieval date to last-modified 2026-07-29; build-process notes removed | Release says AI analyses "potential conflicts". Pages carry `dateModified` metadata. |
| 02 | Role evolution now cites `INTAPP-WP-2018` for "routine tasks" | "Freed from routine acceptance tasks" is not on the Intake page (it says "freeing up your partners' time"). The white paper does say "routine tasks". |
| 02 | Dates: `KINGLAND-WP-2024` 2024-12-03 to 2024; `CEBI-2024` 2024-06 to 2024; `JB-JAR-2004` 2004-07-29 to 2004; `INTAPP-INTAKE-2026` to 2026-07-29 | The day and month were not on any opened page. The copyright line or index gives the year only. |
| 03 | `FENERGO-GT-2026` date 2026-03-04 to 2026-03-03; notes say the COO calls the platform "the first key stage" | Fenergo page shows "published date March 3, 2026". The firm release is 4 March. |
| 04 | "Its pilot firms are law, accounting and corporate-service practices" changed to say the trial firms are not named | Overstated. The vendor writes for those sectors but names no trial firms. |
| 04 | UK AML strategy: "expects digital identity and AI to play a larger part" changed to "will support the use of AI and digital ID to make customer due diligence quicker and easier"; locator now points to the strategy PDF paras 69-72, 84-85 | Embellished. The old locator paras 64-66 did not hold the claim. |
| 04 | `ZYGOS-AISENSE-2026` date 2026-02-10 to 2026-05-18 | The page as read was modified 2026-05-18 and describes the project ending March 2026, after the first-publication date. |
| 04 | Checkpoint reworded to what the vendor says (AI "does not replace the compliance officer") | "Decides on each screening case" is not in the source. |
| 05 | EY page 49 to printed p. 50 (PDF p. 51); "governance analyst infers..." role evolution removed | Wrong page. Unsourced connective claim. |
| 05, 06 | Starling quote given its context (partnerships with non-audit clients) | The "top of mind" remark is about partnerships, not monitoring in general. |
| 06 | Added that Kingland names AI for reading broker statements to extract holdings; EY page fixed; `INTAPP-EMPCOMP-2026` date to 2026-10-12 | The entry said Kingland did not say AI drives these functions. The page does name one AI function. |
| 08 | Added `INTAPP-INTAKE-2026` (automated engagement-letter creation) | Better source for a vendor offering. Grade stays C. |
| 09 | Ref renamed `INTAPP-WP-2024` to `INTAPP-WP-2018`, date 2024-02 to 2018-10, locator p. 5 to PDF p. 6; problem reworded to the source's question form; "practice analyst's observation" removed | PDF metadata shows creation in Oct 2018 (2024/02 is only the re-upload path). Page off by one. Unsourced attribution. |
| 10 | Added `AICPA-AIPAID-2026` (AICPA resource page, 2026-10-12: "nonauthoritative guidance"; download reserved for members); `JOFA-AIPA-2026` now cited for what it says | "Nonauthoritative" and "member-gated" were stated without a source. JofA was listed but never cited. |
| 12 | "governance analyst's framing" relabelled as an idea prompted by the SEC chief accountant's questions | Unsourced connective claim. |
| 13 | Added Kingland's business-relationship register as an existing (non-AI) tool; CL 25 dated | Better context for the prerequisite. |
| 14 | "long-standing alliance" (EY and Microsoft) changed to "strategic alliance"; "citing the Financial Times" changed to "one linking to an FT article that could not be opened"; analyst checkpoint relabelled as idea | Embellished qualifier. Crypto Briefing does not cite the FT; only FourthWeb links to it. FT returns 403. |
| 15 | "discourse angle infers..." role evolution removed | Unsourced connective claim. |
| 16 | Problem: "independence threats through investor holdings, network-firm status and shared services (JOFA-NILSEN-2025)" replaced with what Nilsen says. Solution: "map ... covered members" removed. The APS-capital remark is attributed to Thomson Reuters' narration, not to Hohl. Prerequisite "counsel experienced in the Code and in state or national law" changed to "legal counsel". Analyst checkpoints replaced with a sourced one (FRC early engagement, regulator approval) plus a labelled idea. `IFAC-AQ-2026` date 2026-06 to 2026. `AE-PE-2026` date 2026-07 to 2026-06. | Nilsen does not mention covered members or list those threat sources (embellishment). TR sentence is reporter narration (wrong speaker). IFAC page is undated, with data as of 2026-06-30, so June publication cannot be right. AE file name is dated 2026-06-29. |
| 17 | `ICAEW-PE-2024` date 2024-10 to 2024-10-25; ED locator now includes para 49 (the upstream-entity impairment) | Page reads "Published: 25 Oct 2024". The locator missed the operative paragraph. |
| 18 | Added `GT-GTAPPR-2026` (Grant Thornton's own release, 2026-05-07). Added that the release quotes the CIO of Grant Thornton Advisors LLC (the non-attest entity) on gtap, and that GT Ireland built it with GT's US technology team. The analyst proposal is labelled as an idea. | A primary source was one link away. The non-attest CIO's role bears directly on the shared-platform question. Grade stays C: no named audits use it yet, and the governance step is an idea. |
| 19 | "would apply to firms in this kind of structure (practice analyst...)" replaced with "no source addresses whether..." | Unsourced inference. |
| 20 | "building an AI-native audit methodology starting with private companies" changed to "building the methodology for an AI-native audit from the ground up"; title no longer implies Repodo keeps VC out of the attest entity; the combined funding outcome split so each figure has its own source | "Private companies" is not in `AT-PEEC-2026`. The $10M figure comes from `AT-PEEC-2026`, not `CFI-REPODO-2026`. |
| 21 | Added `IRISHTIMES-KPMG-2026` (FT syndication, 2026-02-06): KPMG International's audit fee fell 14% ($416,000 to $357,000) per its filing; the AI argument comes from people familiar; both firms declined to comment. Grade C to B; maturity emerging to in-production. | Verdantix linked to this report. Earlier notes said no primary was found. |
| Module | Removed build-only text: "synthesis report maps keys to input refs", "all opened by the deep dives", "vendor pilot" | Ships in the product. |
| Module | Frontier: Gtap 2026-05-11 to 2026-05-07; SEC "listening mode" 2026-06-04 to 2026-06-05; Hohl WSJ remarks re-dated to 2025-12 (reported 2025-12-12); Fenergo 2026-03-03/04; "PCAOB names PE and AI as the 2026 areas to watch" changed to "flag ... as areas inspectors will focus on"; "Repodo launches" changed to "raises EUR 8.2M to launch"; "PEEC expected to vote 19 Oct" changed to "interim meeting scheduled to continue discussing" | Wrong dates. Embellished "2026" and "vote", which are not in the sources. Repodo had not opened for clients. |
| Module | §2: "15 small-practice respondents" changed to "15 surveyed compliance professionals and managing partners"; §5: "Bloomberg Law" changed to "Bloomberg Tax"; §6: practice-aid line now cites `AICPA-AIPAID-2026`; §7: Intapp "routine tasks" now cited; §9: fee objection updated with the 14% figure | Statistic mislabelled. Wrong publisher. Unsourced qualifiers. |
| Module | `FRC-GENAI` was cited but listed nowhere in the module or YAML. Added to "Not in the YAML" with URL and date, and the claim re-checked: the guidance never mentions acceptance, and "independence" appears only in a generic sense. | Every source needs a URL and date. |

## Sources that could not be reached

- **All 81 cited URLs opened (HTTP 200), plus 4 added sources.** That is 85 opened and 0 unreachable.
- Primary documents behind the cited sources that could not be read:
  - The FT article on Anthropic's auditor (`ft.com/content/b93d8030-...`): 403, including via the text mirror.
  - The AICPA practice aid PDF: download reserved for members.
  - The WSJ interview with Hohl: not attempted; two secondary reports agree on it.

  The entries that rely on these say so.
- Process note: the shared scratchpad `src/` and `bin/` folders were being overwritten by other agents using the same
  ref filenames, which happened to `GT-GTAP-2026`. All final checks were re-run from a private folder.

## Known error patterns (checked explicitly)

| Pattern | Found |
|---|---|
| Statistic reported as something it doesn't measure | Module "small-practice respondents" (Zygos). The `21` fee cut is now labelled as a fee change, not AI efficiency. No other mismatch. |
| Claim attributed to wrong document or speaker | TR narration attributed to Hohl (`16`). FT attribution given to Crypto Briefing (`14`). $10M attributed to the Repodo article (`20`). Wrong EY page (`05`, `06`). Stale ED locator (`17`). |
| Embellished qualifiers or causes | "long-standing" (`14`). "covered members" and the threat-source list (`16`). "starting with private companies" (`20`). "larger part" (`04`). "pilot firms are law, accounting..." (`04`). Module "2026 areas to watch", "vote expected", "launches". |
| Unsourced connective claims in role_evolution / risks / checkpoints | Analyst or "angle" inferences in `05`, `09`, `12`, `14`, `15`, `16`, `18`, `19`. Each was removed or labelled as an idea. |
| Wrong or missing dates | 13 source dates corrected (see table). The biggest: `INTAPP-WP` is 2018, not 2024. 6 frontier dates corrected. `FRC-GENAI` had no URL or date in the module. |
| Grade inflated by evidence from an adjacent process | None upgraded wrongly. `15` stays D (the pre-approval workflow is real but not shown on AI services). `16` and `17` stay B as human control steps in named firms. Note that their AI link is indirect. |
| Search-only figure in an A or B entry | None. All sources are `access: full` and were re-opened. |

Format: ids unique; all values from the vocabulary (validator passes); every source has a URL and date; no
quotation of 25 words or more.

## Patterns to fix in the briefs

1. **Dates:** forbid using the retrieval date when the page has `dateModified` or `datePublished` metadata. Forbid
   inventing day or month precision. Treat upload-path dates as a hint only, and check PDF metadata.
2. **Follow the source's own links to the primary:** three upgrades were one click away (Verdantix to FT/Irish Times,
   consulting.us to the GT release, the AICPA release to its resource page). Require the researcher to open linked
   primaries before settling for C.
3. **No analyst voice in fields:** ban "the X angle/analyst infers/suggests" in `role_evolution`,
   `risks_and_guardrails`, `human_checkpoints` and `solution`. Use "Not stated in the sources" or "Idea:" instead.
4. **Speaker check:** require each attributed claim to be checked as the speaker's words, not the reporter's
   narration. Also check whether a secondary source actually cites the outlet it is said to cite.
5. **Paraphrase drift:** quote-check paraphrases of guidance for added items (lists of threats, extra steps,
   qualifiers like "long-standing", scope like "private companies").
6. **Page locators:** state printed vs PDF page.
7. **Frontier dates:** use the event or publication date of the primary, not the secondary's date.
8. **Shared scratch space:** give each verifier a unique working folder; refs collide across modules.
