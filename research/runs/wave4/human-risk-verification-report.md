# Verification report: security / human-risk

Checked 2026-10-17 against the cited sources. Files edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/human-risk.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/human-risk.md`

All 56 cited URLs were fetched with curl. PDFs were converted with pdftotext, and blocked pages were read through the r.jina.ai text mirror. For the RedChronos and scambaiting papers, the arXiv HTML full text was also read, as were the ENISA 2025 and 2026 report PDFs. `scripts/validate.py` reports no errors for human-risk.

## Counts

| Action | Entries |
|---|---|
| Kept unchanged | 4 (`-03`, `-08`, `-15`, `-18`) |
| Fixed | 14 (`-01`, `-02`, `-04`, `-05`, `-06`, `-07`, `-09`, `-10`, `-11`, `-12`, `-13`, `-14`, `-16`, `-17`) |
| Rejected | 0 |

## Final grade mix

A 1 (`-01`), B 8, C 5, D 4. Before verification it was A 2, B 7, C 5, D 4. A or B: 9 of 18 (50%).

## The two low-confidence A grades

- **`-01` (Avanade benchmark plus Qualcomm): kept at A, with low confidence.**
  - **Avanade.** The page says Avanade itself performed a three-month proof of concept: two cohorts of 1,000 users, Hoxhunt against its previous tool. All four figures (43% / 37% / 11% / 27%) match the page. A study run by the named organisation meets the A rule.
  - **Caveats added to `measures`.** The two tools sent different simulations: Hoxhunt's adapt in difficulty, and it sent 37% more. So the failure rates are not like-for-like. The page also does not say whether "11%" is relative or in percentage points.
  - **Qualcomm.** The A is strengthened by a quote from Qualcomm's Global Head of Cybersecurity, now added as an outcome. The risky cohort went from double their colleagues' failure rate to roughly half over a 9-month enrollment, and company-wide failure rates then fell by a factor of 6.
- **`-10` (ARK Invest / Doppel): downgraded from A to B.**
  - **The ARK metrics are Doppel's.** The 5.5-hour median domain resolution time and the 98% takedown success rate appear in the vendor's narrative ("To date, Doppel has surfaced over 10,500 alerts for ARK Invest, with a median domain resolution time of 5.5 hours"). They are Doppel's own platform metrics and are not attributed to anyone at ARK.
  - **ARK's own figures are recollections.** "Days to weeks", and about 400 reports in 2024 roughly halved in 2025, come from a manager. Under the 2026-10-17 rule those are B.

## Fixes and rejections

| Entry / section | Fix | Reason (error pattern) |
|---|---|---|
| `-01` problem | "Qualcomm says 4% of users are responsible for 80% of **its** phishing incidents" changed to: the page cites general (Cyentia) research | The page presents a research statistic, not Qualcomm's own incident data (statistic reported as something it doesn't measure) |
| `-01` outcome 3 | Replaced "two inconsistent headline figures" with the CISO-quoted measured comparison; the index-card figures (3.5x, 73%) noted as differing | Better evidence was on the page |
| `-01` risk | "The only large randomised field trial found" changed to "A large randomised field trial" | "Only" is unsupported; the UCSD paper itself cites other controlled field studies (embellished qualifier) |
| `-01` source | Qualcomm date 2023 changed to 2024; key renamed HOXHUNT-QUALCOMM-2024 in both files | The page reports results "within 6 months" of an August 2023 rollout, so it cannot be from 2023 (wrong date) |
| `-02` solution | "Hoxhunt markets the **resulting** Behavior Risk Console" reworded | The Uber page says co-developed capabilities went into Hoxhunt's platform; it does not link them to that product (unsourced connective claim) |
| `-02` problem | Two claims re-attributed: to Uber's judgement and to the TrainShield authors (ref added) | Unattributed claims |
| `-04` risk | The Sophos guardrail now includes "lures built from personal information scraped from social media" | Sophos names OSINT-based lures as unfair, which is directly relevant to this entry and was omitted |
| `-05` problem | "Compliance of 16.5% / up to 36%" changed to "said they would **or might** comply"; recordings or transcripts, not live calls | A survey of stated intent was reported as compliance (statistic reported as something it doesn't measure) |
| `-05` solution | Hoxhunt training "on live phone calls" changed to AI-voice simulated conversations; the search-only Infosec claim removed | The page describes AI audio chats (embellished). The Infosec claim had no opened source (search-only figure) |
| `-06` risk | The unsourced "callback can be compromised" line replaced with the FBI's independent-verification recommendation; FBI-IC3PSA-2025 added to the sources | Unsourced claim in `risks_and_guardrails` |
| `-06` notes | NYDFS date: "page did not show it" changed to "confirmed on the page (October 16, 2024)" | Wrong statement about the date |
| `-07` measures, risk | The 900-hour method is described as on the page (a time value per report; 3-5 vs over 5 FTE stated in different places). "Agent **needs** its own identity" changed to "Microsoft **recommends** a dedicated identity; an existing account can be used" | Mischaracterised method; embellished qualifier |
| `-09` solution | "A study of 101 participants used language models to detect intent" reworded: the 101 were in the phishing experiment, and intent detection was a separate test | Statistic attached to the wrong part of the study |
| `-10` | Downgraded from A to B; outcome `measures` now say the figures are vendor metrics not attributed to ARK | Grade inflated (A rule) |
| `-11` notes | Added the first author's affiliation (Cybera Global Inc. / UNC Wilmington); the operator is not named | Gap closed; grade B unchanged |
| `-12` risk, role | ENISA: "linked to" changed to "**likely** due to" Famous Chollima. "HR becomes part of the security perimeter" changed to the FBI's actual recommendation (educate HR, hiring managers and development teams) plus KnowBe4's HR-IT-security coordination point | Dropped qualifier; embellished, unsourced `role_evolution` |
| `-13` risk | "FBI recommends ... **not relying on spotting AI voices by ear**" removed | The FBI PSA actually advises listening closely for voice cues, while warning that clones can sound nearly identical (claim attributed to the wrong source) |
| `-14` | Full paper read. Maturity changed from piloting to in-production (deployed in Xiaohongshu's SOC). The 90% is described as an estimate on historical log data. Human checkpoint and `role_evolution` sourced from Section 5.3 and the Conclusion | Previously abstract-only; grade B confirmed (estimate, not a tracked metric) |
| `-16` problem | Proofpoint "cause of 37% of material data loss cases" changed to "37% of CISOs cite AI tool misuse as **a** cause" | A share of respondents was reported as a share of cases (statistic reported as something it doesn't measure) |
| `-16` solution | The KnowBe4 Agent Risk Manager claim is now sourced to the 2026-09-23 press release (KNOWBE4-ARM-2026 added) | It was taken from a listing line only, with no source entry |
| `-17` source | URL changed from the DEF CON results index (which lists neither vishing contest) to `dc-34-contests.html` (which describes both) | The cited page does not support the claim |
| Module header, §3, §5, §9 | "Two A grades" changed to one; ARK figures relabelled as vendor metrics | Follows `-10` |
| Module §2 | Voice-clone row: "staff cannot tell" changed to the measured 24-45% recognition rate among US adults. Uber row: "annual training shows no risk reduction" changed to "Uber judged". KnowBe4 row reworded to match the source. Social-engineering row: "human-caller testing is slow" (unsourced) changed to the sourced economics finding | Embellishment; unsourced claims |
| Module §3 | Personalised-lure uplift "about 2.7x" changed to "2.4 to 2.7x". Xiaohongshu "90% less manual intervention" changed to "90% fewer samples, estimated on historical logs" | Overstated figures |
| Module §5 | UCSD "2 points" changed to "about 1.7 points". AI voice: "would or might comply". Okta: "security professionals". Proofpoint: share of CISOs. ENISA 77.8%: 2025 incident data. ENISA >80%: noted that the report gives two bases. Avanade: noted that the simulations differed | Statistics reported as something they don't measure; an unresolved figure resolved |
| Module §6 | FBI line corrected (see `-13`). NIST date 2024-09-12 changed to 2024-09 and URL changed from the draft (`/ipd`, superseded) to `/final`. Triage-agent identity worded as a recommendation. "Approving any payment request" changed to the NYDFS wording. Unsourced "executive consent" checkpoint replaced with the sourced simulation-approval guardrails | Wrong source; wrong document version; embellishment; unsourced claim |
| Module §7 | Uber claim attributed. HR / finance / help-desk "security perimeter" line replaced with the FBI and NYDFS wording. **Johnson & Johnson job posting removed** (search-only, now returns 404) | Embellishment; search-only source that cannot be reached |
| Module §8 | Voice-training line corrected. SANS dated 2026-08-31. ENISA "likely". KnowBe4 Agent Risk Manager (2026-09-23) added | Wrong or missing dates |
| Module §9 | "The largest field trial" changed to "a large randomised field trial". 36% attributed to security professionals. "Every outcome is on a vendor page" now notes the Xiaohongshu paper | Embellished qualifiers |
| Module §10 | Pindrop date 2026-09-29 (not found on the page) changed to 2026, with June 2026 fieldwork noted. SANS dated. NIST URL fixed. JNJ removed | Unsupported dates |

## Sources that couldn't be reached directly

- **dfs.ny.gov (NYDFS letter):** 403 to curl. Read in full through r.jina.ai, and the date was confirmed.
- **sophos.com:** empty reply. Read through r.jina.ai.
- **news.ycombinator.com:** 419. Read through r.jina.ai; dated 2025-10-09.
- **careers.jnj.com:** 403, then 404 through the mirror. **Removed.**
- **web.archive.org:** connection reset, so the undated Hoxhunt (Avanade, Uber) and Abnormal (Valvoline) case pages could not be dated. Their years reflect the current pages only.
- **Pindrop report page:** shows no publication date.
- **ICO monitoring-workers guidance:** shows no publication date. 2023-10 is kept from prior knowledge, and the page metadata shows only 2026-09-28.

## Targets

- 18 use cases (target 15-25): **met.**
- 9 of 18 graded A or B, exactly 50% (target at least 50%): **met, with no margin.** Any further downgrade would drop the module below target.
- Every source has a URL and an ISO date: **met.** The validator passes, and all `source_ref`s resolve.
- Quotations are under 25 words, ids are unique, and values come from the vocabulary: **met.**

## Error patterns to fix in the briefs

1. **Survey shares restated as case or behaviour rates.** Examples: Proofpoint 37%; stated "would or might comply" reported as compliance. Brief rule: copy the survey's denominator, meaning who answered and what they were asked.
2. **Vendor narrative metrics treated as customer-measured.** ARK's 5.5 hours came from Doppel. Brief rule: for A, the figure must be in the customer's voice or attributed to a study the customer ran.
3. **Qualifiers dropped or added.** "Likely due to" became "linked to"; "the only" and "the largest" trial were introduced; "needs" was used where the source said "recommends"; "live calls" was used for simulated conversations.
4. **Advice attributed to the wrong source.** The FBI was cited as saying "don't rely on spotting voices" when it says the opposite. Brief rule: quote the recommendation verbatim before paraphrasing it.
5. **Connective glue in guardrails and roles.** "Resulting" product; "HR becomes part of the security perimeter"; callback-compromise. Brief rule: no sentence in `risks_and_guardrails`, `role_evolution` or module §6-7 without a ref.
6. **Abstract-only reads of papers with full text available.** RedChronos's deployment status was only in Section 5.3. Brief rule: open the arXiv HTML before setting maturity or grade.
7. **Index or listing pages cited for claims made on a detail page.** DEF CON results index; KnowBe4 press listing; NIST draft instead of final.
8. **Dates inferred from page footers or "current listing".** Brief rule: say so in `notes`, and prefer internal evidence (for example, the rollout dates on the Qualcomm page).
