# Verification report: security / data-privacy

- **Verified:** 2026-10-17 (verifier brief `verify-data-privacy.md`, wave 4)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/data-privacy.yaml` (21 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/data-privacy.md`
- **Method:** I reopened every URL cited in the YAML (35 distinct) and in module §10 (22 more) with `curl` in a private
  working folder. I used `pdftotext` for PDFs: the Glyph paper, the OWASP guide (103 pages), the EDPB opinion, NIST AI
  600-1, and the PEPR talk slides for the Tandon and Bouzid talks. I used `r.jina.ai` for pages that block curl (Akamai,
  PwC, Proofpoint-Varonis on GlobeNewswire, OpenAI, Coinbase, Black Hat). Netskope blocked plain curl but opened with
  browser headers. I checked each figure, date, attribution and quotation against the source text. For dates I checked
  bylines, `article:published_time`, JSON-LD, `ms.date`, arXiv submission history, PDF metadata and the Greenhouse API
  for job postings.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it gives `21 use cases, 8 graded A/B (38%)`
  and the expected WARN that the A/B share is below 50%.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 9 (`#01`, `#03`, `#04`, `#09`, `#10`, `#16`, `#17`, `#18`, `#19`) |
| Fixed | 12 (`#02`, `#05`, `#06`, `#07`, `#08`, `#11`, `#12`, `#13`, `#14`, `#15`, `#20`, `#21`) |
| Rejected | 0 |

Every cited source exists and was reached, and every entry's core claim is supported once corrected. The module file
received 15 edits.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 2 (02, 14) | 1 (02) |
| B | 6 (01, 05, 07, 13, 20, 21) | 7 (`#14` added) |
| C | 10 | 10 |
| D | 3 (16, 17, 18) | 3 |

- **`#14` moved from A to B (the caller's flagged item).** The entry rests only on a PEPR '26 program abstract. No slides
  are posted for this talk, and I did not review the video. The abstract does report an evaluation by a named organization
  (Microsoft): nine production repositories, four languages, 183,000+ methods, and "more than twice as many confirmed
  privacy-relevant issues". But the figure compares two AI detector variants (RAG against a standalone LLM). It does not
  measure a change in privacy review work. It is relative only, with no counts, base or confirmation method, and the false-positive
  problem that motivated the change "did not improve significantly". The entry meets the letter of A but overstates it.
  This follows the precedent in earlier waves of downgrading named-organization experiments to B. The figures stay in
  the entry, labelled as abstract-level.
- **`#02` stays at A.** Meta reports the about 85% rules and 15% LLM routing split "in our production deployment" (Figure 7),
  and calls rule coverage "an important operational metric". That is a tracked metric from a named organization. The
  entry already says it is a routing and cost figure with no accuracy or error rate.
- **`#01` stays at B.** All three authors are at Apple, but the paper describes "a single organization's production
  catalog" without naming it. Every Glyph figure checked out against the PDF (63.3% to 99.8%, about 24,000 pairs, 21x, F2 0.890,
  0.880, 0.050, 0.238, 4 evaluation files, 1,905 and 15,205 tables, 57.8 s, about 30 person-years for about 3.4M columns
  across about 98,000 tables).
- **`#07` stays at B under the 2026-10-17 A rule.** OpenWeb's "probably a fifth" is the CISO's estimate, quoted in a
  vendor story, so it is B. It is already labelled as an estimate.
- **`#20` stays at B.** Capital One's work is an offline experiment, not a deployment. The notes now say so and cite the
  posted slides. B is consistent with how earlier waves graded named-organization experiments.
- No A or B entry uses a search-only source. All YAML sources are `access: full`. The only search-only item in the
  module is the Gartner abstract in the §8 frontier table, and it is labelled.

Ladder and change scope are unchanged: assist 2, augment 11, automate 8; step 12, process 9.

## 3. Fixes and rejections

### Use cases

| # | Action | Reason |
|---|---|---|
| `#02` | Fix (locator) | The "manual review cannot keep up with the volume and pace" statement and the "age" field example are in the introduction and Figure 1, not in "Why Asset Classification Matters". |
| `#05` | Fix (wording) | The entry said the pages give no AI detail beyond "AI-native". In fact Vetcor's story mentions "AI-driven automation". |
| `#06` | Fix (fact) | The entry said custom instructions accept "content conditions only". The current Microsoft Learn page (ms.date 2026-06-25) says custom instructions (preview) support both content- and metadata-based instructions, for example deprioritizing .pdf or .jpg files. |
| `#07` | Fix (attribution, unsourced checkpoint) | The role_evolution line attributed "trust alerts enough to use them for decisions and automation" to the CISO. The CISO says only that they see fewer alerts and can trust them; the decision-making and automation wording is the vendor's narrative. The human checkpoint "Security teams review remaining alerts" was not in either source. It now says what the sources actually describe. |
| `#08` | Fix (provenance) | The Hacker News commenter called a "practitioner" says their own team built the proxy ("We got it down to ~250ms"). The entry now says so. |
| `#11` | Fix (embellished qualifier) | "An administrator approves or edits each automated action before it takes effect" overstated the source. Microsoft says users "review, approve, or customize automated actions taken by AI agents" and that these are audited; it does not say approval always comes first. |
| `#12` | Fix (attribution) | "Data owners assign labels and review high-impact RAG corpora" was attributed to OWASP p. 11. Page 11 says only "Human review gates for high-impact RAG corpora". |
| `#13` | Fix (unsourced connective claims) | "Engineers review each suggested job, enforcement point and verification state" and the "instead of reading requirement text ... manually" contrast in role_evolution go beyond the abstract. Both were reworded to what the abstract says. Grade B kept (named Meta deployment, experience report). |
| `#14` | Fix (grade A to B) | Abstract-only evidence. The single figure is a relative comparison between two AI variants with no counts or method. See §2. The measures text now says it compares detectors and is not a before-and-after measure. |
| `#15` | Fix (wrong date, attribution) | The OneTrust Winter '26 post has an on-page byline of **March 4, 2026**. The 2026-06-10 date used was the metadata modification date, so the date is corrected to 2026-03-04. The entry also said "privacy teams describe 'assessment fatigue'". In fact OneTrust, the vendor, uses that phrase about privacy teams. |
| `#20` | Fix (notes, added source) | Made clear that this is an offline experiment, not a deployment. Added the posted slides (PEPR-BOUZID-SLIDES-2026), which give the setup: 24M transactions to 1.6K DP personas, XGBoost tested on 100K real transactions, epsilon 1, 5 and 10. |
| `#21` | Fix (added source) | Added the posted slides (PEPR-TANDON-SLIDES-2026). They confirm the Pixel Recorder production use (transcript classification) and say current production workloads run on CPUs in TEEs with Gemma 3 4B, up to O(100k) inputs per batch. The notes now give this, replacing "deployment scale is not stated". |

### Module file

| Section | Action | Reason |
|---|---|---|
| Header | Fix | "The two A entries" changed to one A entry, with a note that `#14` is B on abstract-level evidence. |
| §3 | Fix | `#14` changed from A to B. `#20` now labelled an offline experiment. `#21` now names the Pixel Recorder and the batch scale. |
| §5 Proofpoint row | Fix (statistic reported as something it doesn't measure) | "Misuse or misconfiguration of AI tools caused 37% of material data loss cases" was wrong. In fact 37% of surveyed CISOs cited it as a cause. Causes are multi-select, so the figure is not a share of cases. |
| §5 Okta row | Fix (qualifier) | The survey question asks what workers entered into "an AI tool or agent in the past 6 months". The base is knowledge workers who use unapproved tools (492 surveyed in total). |
| §5 Microsoft row | Fix | Says "in an evaluation" and "no counts given", and cites the abstract. |
| §5 IBM 2026 row | Fix (qualifier) | The US$1.93M saving is against organizations that use no AI and automation in security. |
| §7 DLP analysts | Fix (attribution) | Same CISO misattribution as `#07`. |
| §7 Privacy engineers | Fix (unsourced connective claim) | "A growing dedicated role" is not shown by three job postings. It now says that job postings show dedicated roles. |
| §8 Direction | Fix (unsourced connective claim) | "The market is consolidating" is now labelled as our reading. It names the two acquisitions and the funding round. |
| §9 Retrieval objection | Fix | Changed to "in Microsoft's evaluation ... confirmed issues". |
| §10 | Fix | Added the two slide keys. Okta date made exact (2026-05-27, the on-page date). The PwC entry notes it was read through a text mirror. |

All other module figures and statements were confirmed:
- CSA: 16%, 29%, 433 respondents, released 10/09/2026.
- PwC: three of seven measures, 49%, 48%, 3,934 leaders, 2026-10-01.
- IBM 2025: 65% and 53%, 40% and 33%.
- IBM 2026: US$4.99M.
- Netskope: 3% of users, 223 violations, 50% of organizations, 90%, 10 apps, 317 to 1,600+ apps, 78% to 47%, 25% to 62%; dated Jan 05 2026.
- Cyberhaven: 39.7%, 32.3%.
- Varonis: 99% of 1,000 environments, 1 in 10 labelled.
- Okta: 54%, 45%, 39%.
- EDPB: case-by-case anonymity and the three-step test.
- Noerr: Article 88c, Council compromise of 10 June 2026, recital 33a.
- EC AI Act page: applicable 2026-08-02; Annex III moved to 2027-12-02.
- NIST PF 1.1: still an initial public draft, page updated April 1, 2026.
- NIST AI 600-1: data privacy risk.
- OWASP: v1.0, March 17, 2026, 21 DSGAI risks, flat context window on pp. 6-7.
- Black Hat Asia "privacy theater" keynote (Violet Blue).
- Akamai and LayerX: US$205M announced May 14, completed July 2.
- Proofpoint and Varonis: US$6.3B, close expected in the first half of 2027.
- OpenAI: 53 user images, update dated September 25.
- Wiz: redacts raw values before alerting, 2026-10-07.
- MIND agentic DLP: 2026-01-28.
- Job postings: Anthropic 2026-08-07, Coinbase 2026-09-01 and Datadog 2026-06-04, from the Greenhouse API.
- Risky Business: 100 titles from 2025-04-09 to 2026-10-14, none on DLP or privacy.

## 4. Sources that couldn't be reached directly

All sources were reached. These needed another route:
- **Akamai** (Access Denied), **PwC** (Access Denied), and **Varonis announcement** (redirects to GlobeNewswire, Access Denied):
  read through `r.jina.ai`.
- **OpenAI**, **Coinbase** and **Black Hat**: page bodies are rendered client-side, so they were read through `r.jina.ai`.
- **Netskope**: Cloudflare challenge on plain curl. It opened with full browser headers; the Jina mirror and Wayback did not work.
- **Coinbase and Datadog postings**: no date on the page. Dates confirmed from the Greenhouse boards API.
- **PEPR #14 (Aloraini and Haslam)**: no slides posted; the YouTube video was not reviewed.
- **CSA report body**: login-gated. Only the landing page and abstract were read; the YAML already says so.
- **Gartner 7192130**: paywalled and search-only. It is labelled as such in §8 and used for no figure.
- **Cyera (4 stories) and MIND OpenWeb**: no publication date in the HTML or JSON-LD. The retrieval date is used and disclosed.

## 5. Targets

| Target | Result |
|---|---|
| 15-25 use cases | Met (21) |
| At least 50% graded A or B | **Not met: 8 of 21 (38%)**, the same share as before verification; only the mix changed (A 2 to 1, B 6 to 7) |
| Every source dated | Met (ISO dates throughout; undated vendor stories carry the retrieval date and say so) |
| Values from vocabulary, unique ids, URLs, quotations under 25 words | Met (validator 0 errors; no quotation is 25 words or longer) |

The A/B shortfall is real. Public evidence for AI in DLP, oversharing and key management is vendor documentation or
telemetry with no named user. Better grades would need named-customer case studies with measured results, which a
targeted search did not find.

## 6. Error patterns to fix in the briefs

1. **A grades from conference abstracts.** One abstract with a relative figure ("more than twice as many") was treated as A.
   Brief rule: an abstract-only result is at most B, unless the slides or paper give counts and method.
2. **Statistic reported as something it doesn't measure.** "Cited as a cause by 37% of CISOs" became "caused 37% of
   cases". Brief rule: for multi-select survey questions, report "X% of respondents cited" and never "X% of cases".
3. **Vendor narrative attributed to a customer quote.** The vendor's sentence about decision-making and automation was
   attributed to OpenWeb's CISO. Brief rule: attribute to the speaker only words inside quotation marks; other text is
   the vendor's.
4. **Embellished approval qualifiers.** Phrases such as "each action, before it takes effect" and "engineers review each" were added
   to human checkpoints that the sources describe loosely. Brief rule: copy the source's verbs for human checkpoints.
5. **Modified date used as published date.** OneTrust's `dateModified` was used although the page shows a byline date.
   Brief rule: the on-page byline beats metadata. Note the metadata date only when they differ.
6. **Unsourced connective claims in roles and direction** ("growing role", "market is consolidating"). Brief rule: label
   interpretation as such, or cut it.
7. **Product documentation drifts.** Microsoft Learn pages change (custom instructions widened in the 2026-06-25 revision).
   Brief rule: re-read product docs near the review date and record ms.date.
8. **Posted slides missed.** PEPR posts slides for some talks. Checking them added production-scale detail for `#21`.
   Brief rule: for conference talks, check the presentation page for slides before settling on abstract-level evidence.
