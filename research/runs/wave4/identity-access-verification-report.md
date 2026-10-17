# Verification report: security / identity-access

- **Verified:** 2026-10-17 (verifier brief `verify-identity-access.md`, wave 4)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/identity-access.yaml` (24 entries, 90 distinct sources)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/identity-access.md` (16 more sources in §10)
- **Method:** I extracted all 106 distinct source URLs (90 in the YAML, 16 module-only keys whose URLs I recovered from the angle
  files or found) and reopened every one with `curl` in a private working folder. I used `pdftotext` for the PDFs (Palo Alto Networks
  landscape report, NIST SP 800-63-4/63A-4/63B-4, FinCEN alert, FBI IC3 2025 report, Nametag report, OWASP report). For pages that
  blocked curl I used the `r.jina.ai` text mirror: EUR-Lex (DORA, NIS2, AI Act), NYDFS, DHS, Persona (browser engine), Identy.io
  (Business Wire), Hacker News, Security Boulevard and Gartner. I read job postings through the public Greenhouse API, which also gives
  `first_published` dates, and cloned the public Gadjit repository. I checked each figure, date, attribution and quotation against the
  page text. For dates I used bylines, `article:published_time`, JSON-LD, `ms.date`, "Last updated" stamps, arXiv submission history and
  PDF metadata.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it gives `INFO ... 24 use cases, 11 graded A/B (46%)`
  and the expected WARN that the A/B share is below 50%. The other warnings belong to other streams' files.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 9 (`#01`, `#02`, `#04`, `#10`, `#11`, `#12`, `#13`, `#15`, `#17`) |
| Fixed | 15 (`#03`, `#05`, `#06`, `#07`, `#08`, `#09`, `#14`, `#16`, `#18`, `#19`, `#20`, `#21`, `#22`, `#23`, `#24`) |
| Rejected | 0 |

The 15 fixed entries break down as follows:
- **8 substantive fixes:** a claim attributed to the wrong document (`#06`, `#07`, `#09`), a vendor statement attributed to the
  customer (`#18`), a recommendation reported as its opposite (`#23`), embellished causes or qualifiers (`#16`, `#19`), and an outcome
  figure replaced with the source's own numbers (`#22`).
- **7 wording, connective-claim, date or access fixes:** `#03`, `#05`, `#08`, `#14`, `#20`, `#21`, `#24`.

No entry was rejected. Every cited source exists and was reached, directly, through a mirror or (for one CISA advisory) through a copy
hosted by a co-author agency. Every entry's core claim is supported once corrected.

The module received 7 edits plus a rewrite of §10 (URLs added for all 16 module-only sources).

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 1 (`#21`) | 1 (unchanged) |
| B | 10 (`#01`, `#03`, `#05`, `#06`, `#12`, `#17`, `#18`, `#19`, `#20`, `#22`) | 10 (unchanged) |
| C | 12 | 12 (unchanged) |
| D | 1 (`#11`) | 1 (unchanged) |

No grade changed. The grades had already been applied under the 2026-10-17 rule, and I found nothing that justified moving one.
- **`#21` stays A.** The figures (average authentication time 90 to 45 seconds in 90 days; IVR profile match 31% to 71%) are tracked
  operating metrics for named organizations, not a practitioner's estimate. The MSUFCU page also gives tracked October 2024 volumes
  (49,907 calls authenticated, 92.99% overall rate). Caveat, already in the entry: every figure is in Pindrop's own case studies.
- **`#18` and `#22` stay B.** Cisco's "three or four hours" is a principal engineer's recollection. HealthEquity's "over 90%" is an
  executive's statement with an undefined metric. VEC's $560K is Pindrop's estimate of potential loss avoidance.
- **`#20` stays B, narrowly.** The Coinbase posting says the team owns production 1:1 and 1:N face match. The identity-graph models are
  work the new hire is to build. I made this explicit in the solution and notes.
- **`#12` stays B, borderline.** The evidence is job postings that make AI use a stated requirement for named IAM teams (Cloudflare,
  Coinbase). These show expectations, not measured use. A stricter reading would make it C.
- **Search-only sources:** two sources marked search-only (Security Boulevard BSidesLV page, Pathlock's summary of Gartner) were
  reachable through the mirror or directly. They are now `access: full` with exact dates. Neither supports a figure in an A or B
  entry.

**Ladder (unchanged):** assist 2, augment 11, automate 9, delegate 2. **Change scope (unchanged):** step 9, process 14, model 1.

## 3. Fixes and rejections

### Use cases

| # | Entry | Action | Reason |
|---|---|---|---|
| `#03` | LLM access-request reviewer (Instacart) | Fix | "Later open-sourced" was wrong: ConductorOne describes Gadjit as open source when it was introduced. `role_evolution` said "before the bot" staff engineers approved requests and "security engineers now write the policy code and the bot". The source says staff engineers did the approvals and reviews *before the move to just-in-time access*, and that account owners review the policy code quarterly. Reworded to match. The BSidesLV Security Boulevard page was reached through the mirror, so it is now `full`, dated 2025-04-08. |
| `#05` | Conversational IT and access assistant (Okta Dex) | Fix | "Including routing access requests" was embellished. Okta says Dex answers new hires who "need access to specific systems". Reworded. |
| `#06` | Access review recommendations | Fix | **Wrong document:** the claim that human sign-off keeps accountability is in NHIMG's summary of an *Omada* post, not its SailPoint summary. Re-cited to NHIMG-OMADA-2026 (source added). **Embellished qualifier:** Microsoft's example does not say the cross-division member's access is "legitimate". Reworded to what the example shows. |
| `#07` | Role mining and right-sizing | Fix | **Wrong document:** "role engineering is hand-curated" comes from Opal ("instead of hand-curating roles"), not the Omada summary. Re-cited. The Google page shows "Last updated 2026-10-13", so its date changed from 2026-10-17 and the "undated" label was removed. |
| `#08` | Continuous identity posture checks | Fix | The Pathlock page was opened (dated 2026-10-05) and quotes Gartner directly, so it is now `full`. The notes now say the Gartner guide itself was not read. Added that SailPoint's release expects A-ISPM in Q4 of its fiscal 2027 (not yet available). |
| `#09` | Natural-language governance queries | Fix | **Wrong document:** "saves administrators time and effort" is on the lifecycle-workflows page (MSFT-LIFECYCLE-2026), not MSFT-GOVOPT-2026. `source_ref` corrected. |
| `#14` | ML risk scoring of sign-ins and sessions | Fix | The CISA press release (CISA-IR8587-2026) was blocked at verification, so the problem statement now rests on the NIST IR 8587 abstract, worded to what it says. The Entra ID Protection page carries `ms.date` 2026-04-22, so the date changed from the retrieval date and the "undated" label was removed. |
| `#16` | SaaS identity MDR (CrowdStrike) | Fix | **Embellished cause:** "operate without tripping endpoint tools" changed to the source's "operate undetected". |
| `#18` | Enforced verification before help-desk resets | Fix | **Wrong speaker:** "Cisco says [agents] spend less time on verification calls" is Persona's statement ("every case automated through Persona saves time for help desk agents"). Re-attributed. **Misquotation:** the outcome now says "three or four hours", as quoted, and notes the Cisco project manager's 5-10 minutes. **Embellishment:** removed "rather than relying on help-desk judgement alone" from the CISA mitigation, which says FIDO/PKI MFA resists phishing, push bombing and SIM swap. Changed "support agents see only failed cases" to what Persona says (its case tool limits who sees personal data). The Nametag ServiceNow page is dated 2026-02-12 (it had been labelled undated). The Persona page notes it was read through the mirror. |
| `#19` | ML identity proofing | Fix | **Embellished qualifier:** FinCEN does not say metadata checks and deepfake software are used "more rarely". It says institutions "may also use more technically sophisticated techniques". **Overstated requirement:** NIST requires biometric test results to come from periodic independent testing that covers demographic groups, not that results be "made public". Both reworded. |
| `#20` | Identity-graph and 1:N biometric search | Fix | "Coinbase builds identity-graph systems" overstated a job posting that describes work for the new hire. Reworded. The notes now say the B grade rests on production 1:N face match, and that Cloudflare's models are general fraud models, not biometrics. |
| `#21` | Passive caller authentication (Pindrop) | Fix | `measures` said "call count ... not stated". The page gives October 2024 volumes, which are now quoted. Grade A unchanged. |
| `#22` | Real-time call risk scoring | Fix | The VEC outcome said "over $500K ... basis not shown in the text read". The page gives $560K potential fraud-loss avoidance since April 2024, $840K annualised, and potential fraud at 1 in 2,529 calls. Figures replaced. **Unsourced connective claim:** in `role_evolution`, "setting real-time risk policies" was replaced with what VEC actually changed (IVR risk score routes callbacks and fraud agents; custom attributes track cases). |
| `#23` | Synthetic-voice detection | Fix | **Reversed advice:** the entry said the FBI recommends "not relying on spotting AI voices by ear". The FBI in fact advises listening closely, says clones can sound nearly identical, and recommends independently calling back. Corrected. |
| `#24` | Behavioural biometrics | Fix | **Unsourced connective claim:** removed the uncited clause "one-time logins leave sessions exposed after a device or token is taken" from `problem`. The European Parliament release is dated 2025-11-27 on the page, so the date changed from 2025-11 and the "secondary reporting" note was removed. |

### Module

| Section | Change | Reason |
|---|---|---|
| §1 | "The security landscape scan notes" changed to "This project's security landscape scan judges" | It is an internal analyst judgement, not an external finding |
| §3 (`#18` line) | "three-to-four-hour" changed to "three or four hours", with the vendor's part of the claim flagged | Misquotation |
| §7 Instacart | Reworded to staff engineers no longer approving or reviewing; policy code reviewed by owners; the security team built the bot | Same unsourced connective claim as `#03` |
| §7 Help desk | "Cisco's agents spend less time" changed to "Persona says each case automated at Cisco frees help-desk time (a vendor statement)" | Wrong speaker |
| §8 Gartner | "Sessions on" changed to "agenda lists ... among its topics" | The page lists topics, not named sessions |
| §9 Auditors/LLM objection | "Start in advisory mode" now cited to Opal; MSFT-GOVOPT supports override tracking only | Claim attributed to the wrong document |
| §9 Cost | The monthly compute-unit charge is Security Copilot's, not the agent's | Precision (the source: turning off the agent does not stop the billing) |
| §10 | Added URLs for all 16 module-only keys; corrected the SAVIYNT-IARA title and found its URL; OWASP dated 2026-06-01; PINDROP-DRI date labelled as sitemap last-modified with its fieldwork dates; IBM date provenance stated | The brief requires every source to have a URL and a date. None had a URL before |

Checked and confirmed without change in the module (sample): Palo Alto Networks figures (Figure 5 on p. 14, the 56% on p. 15, n=2,930,
fielded March-April 2026); SANS 68%/55%/85%/8%; Okta TI 87/58/36/22% and 88%/99.75% on ~6,000 events; Okta/Yubico 76%/52%/44%/43%/36%;
SailPoint Horizons 87%/43%/340; Pindrop DRI 37%/250; DHS 78%/85%/9% vs 20%; VoiceWukong 13.50%; passkeys 53 of 103; arXiv 50.3% vs 15.3%;
FBI IC3 ATO ~4,700/$359.7M and AI-related 22,364/$893M; NIST 800-63A thresholds (1:10,000, 1:100, 1:1,000, <0.07, 0.1, 25%);
NIST 800-63-4 §3.8; DORA Art. 20-21 (yearly, six-monthly); NIS2 points 11.2-11.7; AI Act Art. 5(1)(f) and the verification exclusion;
FinCEN alert; NYDFS letter; CISA AA23-320A mitigations; ISC2 41%; Forrester RSAC; Silverfort four to five minutes; Identy.io 18 vendors;
Saviynt 2026-06-15; FIDO dates; FIRST Datadog session (TLP:AMBER, abstract gives no metrics).

## 4. Sources that couldn't be reached

- **CISA (www.cisa.gov):** returned 403 to curl, and the mirror was also blocked.
  - `CISA-AA23-320A-2025`: verified through the FBI-hosted copy of the same 2025-07-29 joint advisory
    (https://www.ic3.gov/CSA/2025/250729.pdf). The help-desk social engineering, MFA transfer, SIM swap and FIDO/WebAuthn or PKI mitigation
    text all match.
  - `CISA-IR8587-2026` press release: **not verified.** No figure depends on it. `#14` now cites NIST IR 8587 (reachable, dated
    2026-09-15) for the problem statement. The module's mention stays alongside the NIST key.
- **Blocked directly but read another way:** Persona (Cloudflare challenge; read with the mirror's browser engine), Coinbase, Elastic,
  Okta and Cloudflare job postings (read through the Greenhouse API), NYDFS, DHS, EUR-Lex, Business Wire, Hacker News, GitHub (repository
  cloned), Gartner.
- **Not opened (paywalled or out of scope):** Gartner's 2026 IGA Market Guide (quoted only through Pathlock); the DHS RIVR results site
  behind the Identy.io claim (the entry already labels it a vendor press release); the full SANS ITDR report (landing page only, as the
  entry states); the Omada original behind the NHIMG summary.

## 5. Module targets

| Target | Status |
|---|---|
| 15-25 use cases | Met (24) |
| At least 50% graded A or B | **Not met:** 11 of 24 (46%). I found no unsupported downgrade to reverse, and no new deployment evidence strong enough to raise a C. The gap is real: workforce IAM AI features are mostly documented or announced, with no customer measurements |
| Every source dated | Met. Every YAML source has a URL and an ISO date, and the 16 module-only sources now have URLs. Four entries moved from a retrieval date or partial date to the page's real date (Google, Entra ID Protection, Nametag, European Parliament) |
| Ids unique, vocabulary values | Met (validator: 0 errors) |
| Quotations under 25 words | Met |

## 6. Error patterns to fix in the briefs

1. **A claim attributed to the wrong document when two similar sources sit side by side** (3 cases: NHIMG SailPoint vs Omada summaries;
   Microsoft governance vs lifecycle pages; Opal vs Omada on hand-curated roles). Briefs should require the locator to name the exact
   sentence's page, and synthesis should re-check citations after merging angle entries.
2. **Vendor narration attributed to the customer.** Customer stories mix a customer's quotes with the vendor's own claims (Persona/Cisco).
   Briefs should say: attribute to the customer only what sits inside the customer's quotation marks.
3. **Embellished causes and qualifiers** ("without tripping endpoint tools", "legitimate", "more rarely", "rather than relying on
   judgement alone", "routing access requests", "later open-sourced"). Small words, each one unsupported. Add a check: every adjective or
   adverb describing a source's claim must appear in the source.
4. **A recommendation reported as its opposite** (FBI on recognising cloned voices). Paraphrases of advice should be checked against the
   source's recommendation list, not memory.
5. **Unsourced connective claims in `role_evolution` and `problem`** (Instacart, VEC, the behavioural-biometrics problem). These remain
   the most common slip. Briefs should forbid "moves from X to Y" sentences unless the source states both X and Y.
6. **Pages treated as undated or under-read.** Several pages labelled "undated" carried a date (Google "Last updated", Nametag byline,
   `ms.date` on Microsoft Learn, the EP release stamp). Two entries said a figure's basis or count was "not stated" when the page gave
   it (VEC $560K/$840K; MSUFCU October 2024 volumes). Briefs should list where to look (`ms.date`, "Last updated" footers, on-page
   datelines) and require a full read before writing "not stated".
7. **Search-only marked too early.** Two "search-only" sources opened through the text mirror or directly. Try the mirror before
   downgrading access.
8. **Module-only sources without URLs.** §10 listed 16 keys with no URL. The module template should require a URL on every §10 line.
9. **Quotation marks around paraphrase** ("three-to-four-hour"). Quotation marks should only surround the source's exact words.
10. **Ref-key year mismatches (not changed):** MSFT-GOVOPT-2026, MSFT-LIFECYCLE-2026 and MSFT-RISKYUSER-2026 are dated 2025-09-23, and
    REALDEFENDER-BANK-2025 duplicates REALITYDEFENDER-BANK-2026 at a second URL. I left the keys as they are because the same keys are
    used in other files. A cross-file key clean-up should align them.
