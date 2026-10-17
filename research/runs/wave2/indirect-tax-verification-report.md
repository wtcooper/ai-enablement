# Verification report: tax / indirect-tax

- **Verified:** 2026-10-17 (verifier brief `verify-indirect-tax.md`, wave 2)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/indirect-tax.yaml` (22 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/indirect-tax.md` (297 lines after edits)
- **Method:** I extracted all 74 distinct URLs in the two files and reopened every one with `curl` in a private working folder.
  I used `pdftotext` for the PDFs (KPMG survey, Werfel appendices, OECD report, Vertex data sheet, Tax Notes/CDTFA, Hadwick, and the
  full arXiv papers for Dell, Luketina, Santos and TaxCalcBench). I used the `r.jina.ai` mirror for the two paywalled Bloomberg Tax
  commentaries and the Thomson Reuters help page. I fetched the HMRC roadmap's full document page, because the landing page has no
  body text. I checked each figure, date, attribution and quotation against the page text. For dates I checked
  `article:published_time`, JSON-LD, on-page bylines, arXiv submission history, PDF metadata and page footers.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it gives `INFO ... 22 use cases, 4 graded A/B (18%)`
  and the expected WARN that the A/B share is below 50%.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 6 (`#04`, `#07`, `#13`, `#14`, `#17`, `#21`) |
| Fixed | 16 (`#01`, `#02`, `#03`, `#05`, `#06`, `#08`, `#09`, `#10`, `#11`, `#12`, `#15`, `#16`, `#18`, `#19`, `#20`, `#22`) |
| Rejected | 0 |

The 16 fixed entries break down as follows:
- **10 substantive fixes:** a misread source behind a grade (`#12`), claims attributed to the wrong document (`#08`, `#09`, `#20`), a misquoted statistic (`#11`), an overstated research finding (`#22`), and embellished problem statements (`#02`, `#19`, `#20`). Two more entries lost claims taken from an unreachable source (`#05`, `#09`).
- **6 date, title or qualifier fixes:** the Sovos docs date (`#01`), the ICAEW date (`#06`, `#15`, `#20`), the Werfel case-study context (`#15`, `#16`), the NEXT event wording (`#16`), and the Flowie deployment wording (`#18`).

No entry was rejected. All sources exist, and 73 of the 74 URLs were reached. Every entry's core claim is supported once corrected.

The module received 13 edits.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 2 (`#01`, `#06`) | 2 (unchanged) |
| B | 2 (`#05`, `#20`) | 2 (unchanged) |
| C | 16 | 15 |
| D | 2 (`#21`, `#22`) | 3 (`#12` added) |

- `#12` moved from C/piloting to D/emerging and is now labelled "(idea)". The entry cited "Deloitte proof-of-concept work in VAT" for
  upstream data validation. Deloitte's data section describes only potential uses. Its proof of concept is about gathering data and
  populating VAT returns, which is already the evidence for `#02`. No other deployment was found.
- `#01` stays at A. Dell's paper (Nath, Wadhwa, Perez, Dell Technologies) reports precision 70%, recall 61% and F1 65% on a test set of
  16,000 records labelled by experts (Table 1). This is a measured result from a named company. The paper does not say whether the
  model is in production.
- `#06` stays at A. The 16-of-20 result (RAG) on real ICON Wirtschaftstreuhand cases is confirmed: Fig. 5 and Table 6, McNemar p = 0.683.
  It is a research prototype, and the entry says so.
- `#05` stays at B. Singer Equipment's beta-customer quotation is confirmed in the Aviator release. The unreachable Florida source does
  not support the grade.
- `#20` stays at B, a weak B. Plusgrade's posting states in the present tense that "AI handles the first pass on recurring data
  analysis and month-end tax summaries". No outcome is claimed.
- No A or B entry rests on a search-only source. The only search-only source, FLSALESTAX-AI-2026, now supports one sentence in `#05`.

**Ladder (unchanged):** assist 1, augment 12, automate 5, delegate 4. **Change scope (unchanged):** step 9, process 10, model 3.

## 3. Fixes and rejections

### Use cases

| # | Field | Problem found | Fix |
|---|---|---|---|
| `#01` | risks | "so expert review stays necessary" was presented as Dell's finding. The paper does not say it. | Labelled as an inference. |
| `#01` | sources | SOVOS-DOCS-AICLASS was dated with the retrieval date. The page footer reads "Last updated: September 17, 2026". | Date set to 2026-09-17. |
| `#02` | problem | "data import, validation and return mapping consume the compliance cycle" embellishes the release. | Reworded to the release's "heavy lifting" framing. |
| `#02` | solution | "Both vendors keep the tax calculation in a rule-based engine (TR-AGENTICIT-2026)". A Thomson Reuters blog cannot speak for Avalara. | Split into a Thomson Reuters claim and an Avalara claim, and added AVALARA-CRUSHEU-2026 ("deterministic technology"). |
| `#03` | risks | The Sales Tax Institute line ("agents cannot apply an exemption to products they cannot classify") is about sales tax holiday product exemptions, not exemption certificates. It was evidence from an adjacent process. | Removed, with its source. |
| `#05` | problem, risks, role_evolution | FLSALESTAX-AI-2026 returned 403 to direct, mirror and Wayback requests, and WebFetch failed on DNS. A search snippet confirms only the "about 5 rather serious errors" sentence, and that the draft was of the author's own post. | Kept that one sentence and marked the source `search-only` with date 2026-06 from the URL. Removed the unconfirmed claims about knowledge cutoffs and about a "growing number of business owners". Reworded "Avalara's own single test" to "a single example Avalara published": Avalara reports a third-party chatbot answer to a user. |
| `#06` | sources | ICAEW-PCRT-2026 date was "2026-01". The page shows "Published: 19 Jan 2026". | Date set to 2026-01-19 (also in `#15` and `#20`). |
| `#08` | problem | "Teams need to know why an invoice failed and which upstream process caused it" was attributed to SOVOS-SOVI-2026. It comes from the Blue dot release. | Re-attributed to SOVOS-BLUEDOT-2026. |
| `#08` | solution | "Sovi AI diagnoses root causes of e-invoice and filing errors". The March release never mentions e-invoices. E-invoice error diagnosis appears only in the Flowie release's description of Sovi Agent Studio. | Reworded, with that limit stated. |
| `#08` | risks | The quotation "current and planned" is not in the Sovos release. | Replaced with the release's actual wording ("available now or rolling out"; MCP Gateway "developing"). |
| `#08` | sources | The TR-WEBINAR-JLL title differed from the page title. | Title set to "Agentic AI transforms indirect tax compliance". |
| `#09` | risks | "A summary is a reading of the law, not the law" is in FONOA-MONITORING-2026, not FONOA-CITATION-2026. | Re-attributed, and added the accurate FONOA-CITATION claim about fluent wrong answers. |
| `#09` | prerequisites, risks | Two claims rested only on the unreachable Florida page: government sites inaccessible to AI, and the Oct 2025 lease-tax repeal example. | Removed, along with the source from `#09`. |
| `#09` | human_checkpoints | "The tax team decides whether a surfaced change matters" was cited to a page that does not say it. | Replaced with FONOA-STACK-2025's actual statement. |
| `#10` | problem | "Input VAT ... is lost because ..." states as fact what is Sovos's marketing framing. | Reworded as Sovos's statement. |
| `#11` | problem | "found at return time or after the authority asks (TR-BUSINESSCASE-2026)" is not in the source. The misapplied rates and address mismatches come from TR-INSTITUTE-2025. | Re-attributed, and the unsourced clause dropped. |
| `#11` | outcomes | The measures text said Fonoa compared "a reviewer 97% accurate on 10%" with AI at 93%. Fonoa says a human checking 10% "might be 100% accurate". | Corrected to 100%. |
| `#11` | prerequisites | "Consolidated ... ledger data (BTAX-VAT2026)" is not stated in the source. | Marked "(inferred)". |
| `#12` | solution, grade, maturity | The proof of concept was misattributed (see §2). The HMRC case study recommends an *accounting* category (capex vs cost of goods), not a tax category. The OECD "equally relevant to taxpayers' data" was an editorial inference. | Grade C→D, maturity piloting→emerging, "(idea)" added to the title, HMRC wording corrected, the OECD inference labelled, and notes updated. |
| `#15`, `#16` | risks | Werfel's vendor-diligence questions are written for a tax authority's chatbot (Case Study 1), not for a taxpayer's tools. | Context added. |
| `#16` | solution | "NEXT developer event ... focused on agent-based architectures" cites a pre-event announcement. | Reworded to "was billed as covering agent-driven architectures". |
| `#18` | risks | "no deployment evidence" understated the release. It says Flowie's agents already run processes end to end, that Flowie is immediately available, and that one unnamed customer saved 30 hours a week. | Reworded to "no named deployment" with those details. Grade C kept. |
| `#19` | problem, solution, outcomes | "without in-house staff" and "named humans" are not in Numeral's release, which says "access to a person". KPMG says co-sourcing grew but does not say outsourcing grew. | All three corrected. |
| `#20` | problem | "Small in-house teams ... scarce time" is not in the posting. | Replaced with what the posting says. |
| `#20` | prerequisites | "An approved-use policy, vetting of third-party tools" was attributed to TEI-TAXTECH-2026, which mentions neither. Both appear in the IRS OPR best-practice list. | Re-attributed to IRS-OPR-2026; the TEI source now supports only the ownership poll. |
| `#20` | solution | An unsourced recommendation read as if it came from the posting. | Labelled "Design recommendation (not from the posting)". |
| `#22` | solution | "an agent-design pilot [points] to language models plus law-based rules for the final decision" overstates Santos. The pilot used a rule engine only as the oracle and validator in a synthetic test harness. | Reworded. Luketina's recommendation is now cited separately. |

### Module

| Section | Problem found | Fix |
|---|---|---|
| §2 Determination | "Stays rule-based by consensus" generalises from two vendor sources. | Changed to "Vendors keep it rule-based". |
| §3 intro | "Every vendor design reviewed puts a person's approval before filing, rule activation or correction". The claim is too broad: Flowie's agents run AP end to end, and Thomson Reuters suggests auto-processing classifications at 90%+ confidence. | Scoped to filing, rule-activation and correction designs. |
| §3 Data foundation | `#12` was labelled "Improve ... (Deloitte proof of concept)". | Changed to "Idea ... (Deloitte describes it as a potential use)". |
| §4 probe 2 | "most teams cannot [produce a decision record within a day] (57.4% not confident)". That statistic measures confidence in defending AI decisions, not whether a record can be produced. | Reworded to what the figure measures. |
| §5 Surveys | Avalara/Censuswide: "30% have not updated controls" omitted the source's "in the past year". | Corrected. The §10 date changed from 2026-08-10 to 2026-08-11 (the displayed date; the 18:30Z timestamp is midnight IST). |
| §6 ViDA | "1 Jul 2028 platform deemed-supplier rules" omitted the directive's derogation: Member States apply Article 28a "at the earliest from 1 July 2028 and at the latest from 1 January 2030" (transposition article, para. 3). | Added. |
| §6 UK tribunal | *Rafique v HMRC*: the appeal was struck out automatically for breaching unless orders, and reinstatement was refused. The AI-fabricated citations were context, not the stated cause. "The judge said there is no bar on AI" is not in the cited summary. | Rewritten to match the Ross Martin summary. |
| §6 | "Design guardrails seen in practice" describes vendor designs, not observed practice. | Renamed "in vendor designs". |
| §7 | "Tax technology roles are growing" is a trend claim built from three job postings. | Changed to "appear in job postings". |
| §7 | The Vertex reduction in force was set beside AI support gains without the CEO's statement that he "won't categorize" the cost action as AI-related. | Qualifier added. |
| §8 | "Research on rule-checked VAT agents" mischaracterised Santos. | Reworded to "a pilot on splitting VAT determination across agents". |
| §9 | "nobody serious asks it to" was rhetorical and unsourced. | Changed to "the vendors and researchers reviewed don't ask it to". |

All other module figures were traced and confirmed: the KPMG percentages and page placement, the Fonoa survey figures, the
Thomson Reuters vendor claims, the Forrester composite figures, Numeral, Sovos, Vertex, the Luketina, Santos, TaxCalcBench and Dell
results, the ViDA dates (EC page and directive), France, IRS OPR, PCRT, EU AI Act Art. 4 and Recital 59, Hadwick's 85 systems in 26
Member States, CDTFA Publication 70, the Hungary AI risk analysis at invoice issuance, CART, and Vertex Exchange.

## 4. Sources that couldn't be reached

| Source | Routes tried | Outcome |
|---|---|---|
| FLSALESTAX-AI-2026 (floridasalestax.com, June 2026) | curl with browser and bot user agents (403, Cloudflare challenge); r.jina.ai (403); web.archive.org (blocked); WebFetch (DNS failure) | One web search confirmed the page exists and the "about 5 rather serious errors" claim. Marked `search-only`; claims it alone supported were removed. |

Partly reachable: the Bloomberg Tax commentaries (BTAX-AGENTICCOMMERCE-2026, BTAX-VAT2026) were read in full through the text mirror.
BTAX-OECDVAT-2026 shows only its opening paragraphs, as the YAML already says. Fonoa's full 2026 report is gated, and the figures come
from its landing page and blog, as the YAML says.

## 5. Targets

| Target | Status |
|---|---|
| 15–25 use cases | Met (22) |
| At least 50% graded A or B | **Not met:** 4 of 22 (18%). The module header discloses this. Public indirect-tax AI evidence is almost all vendor launches with unnamed customers. |
| Every source dated | Met. Every source has an ISO date. Two pages (TR-HELP-PRODCLASS, TR-WEBINAR-JLL) carry no date and use the retrieval date, as disclosed in their locators. |
| Ids unique; vocabulary values valid | Met (validator: 0 errors). |
| Quotations under 25 words | Met. The longest is the TEI panelist's 14-word quotation. |

Format note for the archetype pass: three refs do not follow `PUBLISHER-SHORT-YYYY` (TR-HELP-PRODCLASS, SOVOS-DOCS-AICLASS,
HADWICK-EUAIACT). They are left unchanged because the controversy files and wave 2 research files use the same keys.

## 6. Error patterns to fix in the briefs

1. **Wrong-document attribution between sibling vendor pages** (`#08`, `#09`, `#20`). When one vendor publishes several releases or
   blogs in a series (Sovos Sovi, Blue dot and Flowie; Fonoa Monitoring and Citation; two TEI recaps), synthesis attached sentences to
   the wrong sibling. Briefs should require the locator to quote a distinctive phrase from the cited page.
2. **Illustrative or "potential" language read as a deployment** (`#12`, and the §3 intro). A firm's "illustrative example" or "can be
   positioned" text was promoted to "proof of concept" and graded C/piloting. Briefs should tell researchers to grade only from
   sentences that say something happened.
3. **Numbers changed in paraphrase** (`#11` 100%→97%; §4 57.4% turned into "most teams cannot"). Figures inside `measures` text and
   probes need the same check as headline outcomes.
4. **Embellished problem statements** (`#02`, `#19`, `#20`). The `problem` field drifted into plausible but unsourced context, such as
   "small teams" or "without in-house staff". Briefs should ask that every sentence in `problem` carry a ref, or be marked as inferred.
5. **Causal compression in regulatory and case summaries** (*Rafique*; the ViDA dates; the Vertex reduction in force). Summaries
   dropped qualifiers that change the meaning: an automatic strike-out, an optional deferral to 2030, "not AI-related".
6. **Adjacent-process evidence** (`#03` holiday exemptions used for certificates; Werfel's tax-authority chatbot questions used for
   taxpayer tools; `#12` HMRC direct-tax categorisation). Briefs should ask for an explicit adjacency label.
7. **Retrieval dates where the page has one** (`#01` Sovos docs footer; ICAEW byline). Check page footers ("Last updated") before
   falling back to the retrieval date.
8. **Unreachable sources recorded as `access: full`.** The Florida page was marked full but cannot be reached from this environment.
   Researchers should save a text snapshot, or mark the source `search-only` when only a mirror or snippet was seen.
