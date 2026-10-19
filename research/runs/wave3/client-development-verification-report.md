# Client development verification report (professional services)

Verified 2026-10-19 against `research/runs/wave3/briefs/verify-client-development.md`.
Files checked and edited:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/client-development.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/client-development.md`

Method: every cited URL (92 in the YAML and 11 more cited only in the module) was downloaded and read. Publication
dates were checked against JSON-LD, `article:published_time`, the WordPress REST API (Introhive client stories), PDF
metadata or the byline. Pages that blocked direct requests were read through the r.jina.ai mirror.

## Counts

| Action | Entries | Ids (`#NN` = professional-services-client-development-NN) |
|---|---|---|
| Kept | 6 | #09, #11, #13, #17, #21, #22 |
| Fixed | 16 | #01, #02, #03, #04, #05, #06, #07, #08, #10, #12, #14, #15, #16, #18, #19, #20 |
| Rejected | 0 | none |

## Final grade mix

A 0 · B 11 (#01, #02, #03, #05, #06, #12, #14, #16, #20, #21, #22) · C 10 · D 1 (#11). There were no grade changes.
Two B grades (#12, #16) rested on an anonymous ILTA survey, which names no organization, so they could not stay B on
that evidence. Both keep B only because a named-firm source was added (see the table).

## Fixes and rejections

| Entry / place | What was wrong | Fix |
|---|---|---|
| #01 solution, notes; module §3 | Howes Percival was listed as a zero-entry capture deployment, but its Intapp story describes an Outlook relationship panel and alerts, not automatic capture (an embellished example) | Replaced it with Thomson Snell & Passmore, whose story lists "zero-entry contact management" from email and calendar. Locator updated |
| #02 risks | LOUBAR-2025 was described as "in-house advisers"; the authors are Stoll Keenon Ogden lawyers writing for in-house counsel (wrong speaker) | Now "a bar-journal article for in-house counsel" |
| #02, #04, #19 (INTAPP-DEALCLOUD-2026) | Source was labelled "undated", but JSON-LD shows it was first published 2023-11-02 and modified 2026-10-19 | Date set to 2026-10-19; title records both dates |
| #03 prerequisites | "Agreed contact-frequency standards" was attributed to Introhive's accounting article, which does not say this (unsourced connective) | Split into two items: Howes Percival's interval alerts (INTAPP-HOWESPERCIVAL-2025) and a shared health view (INTROHIVE-ACCTXSELL-2026) |
| #04 solution | "Relationship health deciding which accounts are ready" was credited to the Accounting Today opinion piece; it is Introhive's argument (wrong speaker) | Credited to Introhive |
| #04 role_evolution; module §9 | The 90% remark came from one law-firm technology specialist, not from "panelists" | Corrected |
| #05 outcome, role_evolution | The Akin Gump page has no statement that "discussion moved from reviewing information to deciding". It does not say the director "owns the tool's design" (unsupported) | The outcome now uses the page's own claim: the tool helps people identify opportunities earlier and evaluate them better. The role is now "explained why the firm built it in-house" |
| #06 role_evolution | "Client-specific insight" was a paraphrase; TRI says "better client data and competitive intelligence" | Wording corrected |
| #07 solution, role_evolution | Forvis Mazars Capital Advisors selected Celeste for corporate-finance deal workflows, not client development (an adjacent process presented as the same use). Wotton Kearney's plain-language use is a future plan ("will") | Forvis is now marked as an adjacent use. The Wotton Kearney role sentence now reads "Intapp says ... will" |
| #08 role_evolution; module §7 | "'plant' tailored prompts" misquoted the panelist, who said "plant things in our lawyers' and partners' minds" | Quote corrected |
| #08 (INTAPP-ACTIVATOR-2026) | Source was labelled "undated", but the page was published 2025-02-10 and modified 2026-10-08 | Date set to 2026-10-08; title records both dates |
| #10 solution, role_evolution | Forvis Mazars was presented as a client-development selection. The Intapp chief product officer's "ten times the matters" line was a hypothetical, reported as if it described a team | Forvis is now qualified. The line is marked as a hypothetical |
| #12 grade basis, solution, sources | B rested on ILTA's anonymous survey, which names no organization. The "drafted with AI under editorial control" part had no evidence. A problem sentence (clients expect AI-savvy firms) had no source in the entry | Added named-firm marketing of their own AI tools (AKIN-MONEYBALL-2026, DEBEVOISE-BLOOMBERG-2026, PARKERPOE-LAWSITES-2026) and TRI-CMBDO-2026. The AI-drafting part is now stated as not evidenced. B kept on the named firms |
| #14 outcome, role_evolution, notes | The RSGI 61% vs 4% compared 60 Harvey-customer firms with 27 in-house teams, who are not each other's clients; it was presented as firms and clients disagreeing (a statistic reported as something it does not measure). GT and DLA officers were said to "speak in client conversations"; they spoke at Legalweek panels. VSCPA was cited as search-only and "42% of firms" | Added the survey base and the caveat. Role corrected. VSCPA opened: 42% of 144 respondents; source added with full access |
| #15 risks, role_evolution | "Firm leaders said measurement is still anecdotal": one managing director (Zarwin Baum) said it. "Client-relationship, pricing and finance roles share ownership of AI value reporting" had no source (unsourced connective) | Attributed to the right speaker. The unsourced role claim was removed |
| #16 grade basis, sources, risks, dates | B rested on ILTA's anonymous survey. The boilerplate risk omitted ABA 512's context (informed consent before entering client information into self-learning tools). LAWSOC-GENAI-2026 was dated "2026", but the page is dated 30 Jun 2026. Woodard's "update annually" is its summary of AICPA guidance | Added BABSTCALLAND-TERMS-2025, a named law firm's published AI consent terms (opened). Risk qualified. Date set to 2026-06-30. Woodard wording corrected. B kept on the named firm |
| #18 outcome, risks | Shoosmiths' remark was quoted by Edinburgh News from the firm's own manager but marked vendor-published. The "confirmation bias" claim was credited to the MyCustomerLens CEO; the article text says it, not a CEO quotation | Provenance changed to self-reported. Attribution corrected |
| #20 solution, role_evolution, source title | "The release says a similar lab with Fasken came first" is not in the release (an embellished qualifier). "Pricing and innovation officers span both sides of joint use-case work" had no source (unsourced connective). The release was posted on LawSites by BARBRI, owner of the Lega platform used; this was not disclosed | Now "mentions a similar Lega client AI lab with Fasken". The unsourced claim was removed. Source title discloses BARBRI (also in #08 and #12) |
| Module §2 | "78% say relationship data is hard to act on" | Changed to the release wording: tools give visibility that is hard to act on [INTROHIVE-PARTNER-2026] |
| Module §3 | #22 marked "AI advisory for accounting clients" as B; the accounting part is events and ideas | Corrected. #12 and #16 named firms added |
| Module §5 | FOP 32% wording and RSGI base | Aligned with the sources |
| Module §8 | "do not use AI" / "show us your AI" were shown as quotations; TRI paraphrases and does not use those words. MCA event date was 2026-11-26; the listing's event is 2026-11-06 | Rewritten without quotation marks. Date corrected |
| Module §9 | VSCPA "search-only ... 42% of firms"; "firms and clients disagree ... 61% vs 4%"; "prompts arrive in email" (the source says daily workflow) | Corrected as in #14; wording aligned with the source |
| Module §10 | 11 keys cited only in the module had no URL | Each was opened, and its publisher, date and URL were added inline. VSCPA moved into the YAML |

## Checks that passed (no change needed)

- All figures in #01 and #02 (Schneider Downs, LBMC, TSP 47→97 and 3→5, home-page 30%/36%/90%, Forrester 97%) match the pages. All Introhive client-story dates match the WordPress API.
- Survey figures match their sources: Introhive/LawSites partner survey (57%, 84%, 68%, 6.7, 63%, 15%, 28/22/13%, 54/49/46%, 44%, 8→40), TR FOP, TR AIPS (41%, 18%, 54/29/67%), TRI Great Disconnect (85%/75%), TRI Stand-out, ILTA Q3.18, ACC/Everlaw, BigHand, Intuit, Litera, CPA Practice Advisor, CustomerThink, VSCPA.
- Regulatory statements match page and section: CalBar 2026 (pp. 2, 5-8), Oregon 2026-208 (sections I-III.D), Florida 24-1 via the ezel.ai mirror, NYC Bar 2024-5 fn. 21, ICMCI code (3.3, 7.1, 7.3, 11.2), AI Act Art. 50 and the Commission timeline, FCC 24-17 para. 2, Law Society pages, JofA articles, ABA 512 summaries, Bloomberg Law Otter.ai analysis.
- Cross-references exist and match their topics: scoping-pricing-07/09/10/11/23, work-production-20/21/25, assurance-acceptance-independence-11/15, tax-compliance-individual-business-15, tax-research-advisory-24.
- Ids are unique. Vocabulary values are valid. Every YAML source has a URL and a date. No quotation reaches 25 words. `scripts/validate.py` reports no error or warning for these two files. The one remaining error is in `pursuit-proposals.md`, another module.

## Sources that could not be reached

- LATHAM-ADAI-2026 (iCIMS returns HTTP 410; the mirror shows only cookie text), BAKERMCKENZIE-CLIENTAIRISK-2026 (page not found, HTTP 403) and WOLFGREENFIELD-2026 (CAPTCHA). All three were already marked search-only and support no grade.
- AKIN-MONEYBALL-2026, DEBEVOISE-BLOOMBERG-2026 and EDINBURGHNEWS-SHOOSMITHS-2023 blocked direct requests; all were read in full through the r.jina.ai mirror. The Lawyer and Law.com articles behind the Akin, Cooley and ABA Journal items are paywalled and were not read; the entries rely only on the opened summaries.
- TR-FOP-2026 shows no publication date on the page, so it keeps the year-only date "2026".

## Targets

- Use cases: 22 (target 15-25). **Met.**
- Graded A or B: 11 of 22 = 50% (target at least 50%). **Met, with no margin.** It depends on the two added named-firm sources: without them #12 and #16 would be C and the share would be 41%.
- Every source dated: **met**, in the YAML (YYYY at minimum) and in the module (starred keys now carry a date and URL).

## Error patterns to fix in the briefs

1. **Anonymous surveys used as a B basis.** ILTA-style prevalence data names no organization. The briefs should state that B needs at least one named organization; survey prevalence only adds context.
2. **Vendor case-study examples stretched across use cases.** A firm named in one vendor story (Howes Percival: alerts and an Outlook panel) was reused as an example of a different capability (automatic capture). The brief should require the example's own source to describe that capability.
3. **Adjacent buyers counted as client-development deployments.** Forvis Mazars Capital Advisors bought Celeste for deal workflows. Selections should be checked for the process they were bought for.
4. **Group comparisons from unmatched samples.** The RSGI firm and in-house figures come from different respondents, not client-firm pairs. Ask agents to record the base and to avoid "X vs Y disagree" framing unless the samples are matched.
5. **Panel remarks attributed to the wrong speaker or number of speakers.** "Panelists" was used where one person spoke. "Firm leaders" was used for one managing director. Paraphrases were set in quotation marks ("show us your AI"). The briefs should require speaker-level attribution and verbatim quotation marks only.
6. **Unsourced connective sentences in `role_evolution` and `prerequisites`.** Examples are role ownership of AI value reporting and pricing officers spanning joint work. The rule that every attributed sentence needs a ref also applies to prerequisites.
7. **Product pages labelled "undated".** The Intapp pages and the Law Society guide carry JSON-LD or visible dates. The brief should tell agents to check JSON-LD, the WordPress REST API and visible page metadata before using "undated" or a month-only date.
8. **Module-only keys without URLs.** Keys marked * in a module §10 had a date but no URL. The synthesis brief should require a URL for every key not in the YAML.
9. **Sponsored press releases.** LawSites posts by BARBRI and by the Legal Futures associate channel are vendor-placed. Agents should note who posted the release.
