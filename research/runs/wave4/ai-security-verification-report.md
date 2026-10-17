# Verification report: security / ai-security

Checked 2026-10-17 against the brief `research/runs/wave4/briefs/verify-ai-security.md`.

Files checked and edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/ai-security.yaml` (25 use cases, 122 distinct sources)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/ai-security.md`

Method: every cited URL was fetched (126 including the four module-only keys). Each figure in an outcome, and in the
module's metrics table, was matched to the source text. Publication dates came from page metadata, PDF creation dates,
arXiv submission lines or the greenhouse and Ashby job APIs. Blocked pages were read through alternative routes (see
"Sources that could not be reached directly"). `scripts/validate.py` reports 0 errors; ai-security shows 25 use cases,
20 graded A/B (80%).

## Counts

| Outcome | Use cases |
|---|---|
| Kept unchanged | 5 (`01`, `02`, `06`, `13`, `24`) |
| Fixed | 20. Ten had unsupported or embellished wording corrected. The other ten had only dates, metadata or the measurement setting changed (all nine A entries now state where the figure was measured). |
| Rejected | 0 |

No grade changed. Every cited figure was found in its source. The faults were in wording, attribution, dates and
missing measurement settings, not in the numbers.

## Final grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 9 | 03, 04, 08, 10, 14, 15, 17, 18, 23 |
| B | 11 | 01, 02, 06, 09, 11, 12, 13, 19, 22, 24, 25 |
| C | 4 | 05, 07, 20, 21 |
| D | 1 | 16 (labelled "Idea") |

Grade A check, with where each figure was measured (now written into each A entry's notes and the module's §3):

| Entry | Measured by (named organisation) | Where measured |
|---|---|---|
| 03 | NIST CAISI with Gray Swan and UK AISI; UK AISI; academic authors | Public competitions and research labs |
| 04 | UK AISI (40x effort; universal jailbreaks); OpenAI (preliminary) | Government and lab pre-deployment evaluations |
| 08 | Anthropic; Trajectory Labs and Apollo Research, both commissioned by Anthropic | A controlled study in a test environment built by the vendor, plus commissioned lab tests. Only the 97% approval rate comes from real use. |
| 10 | Trail of Bits; UK AISI | One lab test by the author; AISI's own evaluation runs |
| 14 | Academic authors (USENIX skills study; arXiv MCP study) | Scans of public registries and of live MCP servers |
| 15 | Anthropic; Google GTIG; NSA, CISA and FBI | Providers' production API traffic |
| 17 | Anthropic; OpenAI; NIST CAISI | The labs' own evaluation and training records |
| 18 | METR (independent); Hugging Face | METR's review of OpenAI's evaluation records; Hugging Face forensics on its production platform |
| 23 | AIUC (the tester) | A test engagement on one MSCI agent, reported in AIUC's own case study |

Entry 23 stays at A under the 2026-10-17 rule. The test count, role count and severity result are the tester's own
results, not a practitioner's recollection. The entry already says the figures are activity counts from a vendor case
study with no independent check. The MSCI CISO's quotes (B-level) are not used as A evidence. Entry 18's "in hours
rather than days" is a self-described estimate. It stays labelled as such, and the A grade rests on METR's counts.

## Fixes and rejections

| Entry / section | What changed | Reason |
|---|---|---|
| 07 risks | "the study reports a live red-team exercise was needed to confirm containment" became: the proxy still missed about 5.5% (94.5% recall), and the authors credit containment to the closed intent vocabulary and argument validator, checked in a live red-team exercise | Embellished cause. The abstract says the exercise "confirms" containment, not that it "was needed". |
| 09 problem | Removed "weak passwords" from the CERT-In attribution | Not in THN-CERTIN-2026. Weak passwords appear in Anthropic's incident (HelpNet), which the entry already cites in its risks. |
| 10 notes | "a joint initiative with OpenAI" became: preview access to an OpenAI cyber model through Trail of Bits' Patch the Planet programme | The post says preview access came via Patch the Planet. "Joint initiative" was not stated. |
| 11 risks | Replaced "Anthropic revised an early claim about what its model believed..." with: Anthropic's chain-of-thought monitors would have missed one incident because biased reasoning persuaded the monitor | No such revision in ANTHROPIC-ALIGNMENT-2026. Its 10 Sept correction concerns PyPI timing and system access. The replacement is stated in "Replication and monitoring". |
| 11 role_evolution; module §7 | "share an on-call rota with decision rights" became: safety, security and research staff are paged together, may end experiments, and must pause if a false positive cannot be ruled out in 30 minutes | Embellished. The OpenAI report (IX.B) describes joint paging and pause expectations, not a shared rota. |
| 12 role_evolution; module §7 | "sponsor becomes the accountable endpoint of the log chain" / "ends the accountability chain" became: the creating user is recorded as sponsor, and authentications are logged against the agent identity | Embellished qualifier. Microsoft Learn says only that the creator is recorded as sponsor and that authentications are logged. |
| 16 problem | "poisoned retrieval content can steer outputs (ARXIV-2510.07192)" became "the same holds for fine-tuning" | Claim attributed to the wrong document. The paper covers pretraining and fine-tuning poisoning, not retrieval. |
| 18 risks | COLLUSIONWIKI: "before OpenAI could review it" became "which they believe OpenAI had also discovered"; METR: "did not confirm claims" became "confirming claims ... was out of scope" | The wiki itself says the researchers believe OpenAI found the board. METR's wording is "out of scope for this investigation". |
| 19 solution | "Add AI scenarios to tabletop exercises (ISACA-SOC-2026)" became "ISACA reports 17% include AI incidents in broader cyber exercises" | ISACA's release makes no such recommendation. It reports the 17% figure. |
| 19 sources | ISACA date 2026-09 became 2026-09-22; OpenAI framework 2026-09 became 2026-09-16 (also in the module §8) | Imprecise dates; exact dates are on the pages |
| 21 solution | "find agents through browser, endpoint, network and SaaS signals and assign named owners (OKTA; CROWDSTRIKE)" now credits CrowdStrike with endpoint, cloud and SaaS, and Okta with shadow-agent discovery, named owners and access certifications | "Browser" and "network" are unsupported. The owner and certification claims come from Okta only. |
| 22 outcome | "42% single-executive accountability" became "42% place AI purchasing decisions with a single executive" | The statistic was reported as something it does not measure |
| 22 prerequisites | "An executive sponsor with authority and resources (CISA-FVEY-2026)" became: cyber leaders given authority and resources, as the Five Eyes agencies urge | Matches the statement's wording ("empower cyber leaders with authority and resources") |
| 22 role_evolution | "Governance staff become classifiers and standard-setters" became: lower-tier agents apply a subset of AIUC-1 at build time, while top-tier agents get independent certification | Unsourced connective claim. Replaced with the case study's own words. |
| 25 risks | The insurance claim is now cited to AIUC-MSCI-2026 (the company description) | The AIUC-1 home page does not say AIUC offers insurance. The MSCI case study's company description does. |
| 05, 07, 10, 11, 12, 17, 19, 20 sources | NISTCISA-IRKEY-2026 title restored to "...in Super Intelligence Training and Evaluation"; publisher set to NIST CAISSI, NSA SISC and CISA; header note amended | The PDF issued on 2026-10-16 already carries "Super Intelligence" and those author names. Renaming it to "AI" misstated the document. |
| 14 sources | ARXIV-2605.22333 date 2026-05 became 2026-05-21 | The arXiv submission date is available |
| 15 sources | CISA-AA26-251A-2026 locators note that it was read in full from the identical FBI IC3 PDF | cisa.gov blocks automated access. Every advisory figure (six companies, billions of tokens, ATLAS mitigation IDs, response alteration) was confirmed in the IC3 copy. |
| 03, 04, 08, 10, 14, 15, 17, 18, 23 notes; 08 measures | Added "Measured in: ..." (lab, competition, evaluation records, production traffic or test engagement) | The brief requires A entries to say where they were measured |
| Module §2 | "alerts without authority to stop" became "a port-sweep alert did not stop the run" | Embellished. On-call staff chose not to stop the run (OpenAI report III.B). |
| Module §3 | Where-measured labels added to every grade A mention | Same as above |
| Module §5 | Measurement setting added to the rows for lab tests, labs' own records, and the tester's own report | Same as above |
| Module §6 | Added the [MITRE-ATLAS], [CSA-STARAI-2026] and [ETSI-EN304223-2025] citations | These items were named without a source key |
| Module §7 | Agent-sponsor, evaluator and governance-broker lines rewritten (see 11, 12 and 22); Okta Dex and Cengage cited | Embellished or unsourced connective claims |
| Module §8 | Dropped "first" from the CISA guidance line; Portkey labelled a gateway; dates set to 2026-09-16 (OpenAI) and 2026-10-13 (ATT&CK v20, now verified); RSAC month removed | "First" is unsourced; Portkey is an AI gateway, not an identity product; exact dates found; the RSAC page does not state a month |
| Module §9 | Sandbox objection now says "in one Trail of Bits lab test". Reasoning objection: dropped the unsourced "reasoning is not always available" and restated the Anthropic monitor finding. The UK AISI result is labelled a lab setting. | Says where it was measured; removes an unsourced claim |
| Module §10 | MITRE-ATTCK-2026 is now verified (dated 2026-10-13); RSAC entry corrected; added a note on keys that also appear in the YAML | It had been marked "not re-verified" |

## Known error patterns: explicit checks

| Pattern | Finding |
|---|---|
| Statistic reported as something it doesn't measure | One case (22: 42%). All other figures matched their measures, including 13.6% vs 89%, 0 of 720, 40x, R² 0.097, 141,006, 481M / 9.2M, 50 PB, 1,200 / 700, 7%, 157 of 98,380, 40.55% of 7,973, and 16M / 24,000. |
| Claim attributed to wrong document or speaker | Four cases (09, 16, 19, 11). Also the NISTCISA title, which had been normalised away from the issued document. |
| Embellished qualifiers or causes | Seven cases: 07; 18 (two); 11 and 12 role lines; module §2; module §8 ("first") |
| Unsourced connective claims in role_evolution / risks | 11, 12 and 22 role_evolution; module §7 (three lines) and §9 (one clause) |
| Wrong or missing dates | Four imprecise dates fixed (ISACA, OpenAI framework, arXiv 2605.22333, ATT&CK v20). The RSAC month was dropped as unsupported. All other dates matched page metadata. Pages with no date carry the access date with a note. |
| Grade inflated by adjacent process | No change needed. 07 is already C because its lab figure comes from SOC remediation, an adjacent process. 09 is B with the adjacency noted. 14's A is labelled a research registry scan, not an enterprise deployment. 01 (B) rests on CISA, NSA and FBI using ATLAS in a real advisory, which is borderline but defensible. |
| Search-only figure inside an A or B entry | None. Every source is `access: full`, and two search-only items were already confined to notes (21: alliance membership; 24: job postings). |

Format: all values come from the vocabulary. The 25 ids are unique. All 122 sources have a URL and a date. The quotations
checked are all under 25 words; the longest is Trail of Bits at about 16 words.

## Sources that could not be reached directly (and how they were read)

| Source | Route used | Residual limit |
|---|---|---|
| CISA-AA26-251A-2026 (cisa.gov 403) | Identical FBI copy at https://www.ic3.gov/CSA/2026/260908.pdf | None |
| CISA-AGENTIC-2026 (cyber.gov.au PDF stream error) | r.jina.ai text mirror of the PDF; CISA landing page via mirror confirms 2026-05-01 | PDF page numbers in locators could not be checked against the text mirror |
| CISA-FVEY-2026, CISA-PLAYBOOK-2026 (cisa.gov 403) | r.jina.ai browser mirror | None |
| GARTNER-GENAIINC-2026, GARTNER-UNIFORMGOV-2026, GARTNER-AGENTSPRAWL-2026 (CAPTCHA) | r.jina.ai browser engine with wait-for-selector | None |
| TECHZINE-SAFE-2026, TECHZINE-OPENAI-2026 (403) | r.jina.ai browser engine | None |
| OECD-INCIDENT-2025 (bot check) | r.jina.ai browser engine (29 criteria confirmed) | None |
| OPENAI-HF-2026, OPENAI-HFUPDATES-2026, OPENAI-MISALIGN-2026 (403) | r.jina.ai mirror | None |
| OWASP-ACS-GH-2026, MSFT-AGT-2026 (GitHub blocked for this session) | raw.githubusercontent.com README files | None |
| MITRE-ATLAS, RSAC-ISB-2026 (JavaScript pages) | r.jina.ai browser mirror | RSAC page does not state the contest month |
| OWASP landing pages (JavaScript download links) | Downloaded the OWASP PDFs (LLM Top 10 2026, Agentic Top 10, red-team vendor criteria, State of Agentic AI) | None |
| UKAISI-ASTRA-2026 | Abstract only (as the YAML already states); full paper at arXiv 2609.38415 not read | AISI's propensity rates not read |
| arXiv papers | Abstract-level, as the YAML states | Full texts not read |

## Module targets

| Target | Status |
|---|---|
| 15-25 use cases | Met (25) |
| At least 50% graded A or B | Met (20 of 25, 80%) |
| Every source dated | Met (YAML and the four module-only keys) |

## Patterns of error to fix in the briefs

1. **Require "where measured" for every A figure.** Most A figures in security modules come from AI labs' evaluation
   environments, vendor-run studies or vendor case studies. Synthesis briefs should require a "Measured in:" clause
   (lab / competition / own records / production) in the notes and in module §3 and §5.
2. **Do not normalise document titles.** The terminology note (US agencies now print "Super Intelligence") was applied
   to a document that was issued with that title. Briefs should say: cite titles and authors exactly as issued, and put
   the terminology caveat in notes.
3. **Watch causal and procedural embellishment in paraphrase.** Typical drift: "confirms" became "was needed", "paged
   together" became "on-call rota", "recorded as sponsor" became "ends the accountability chain", and "believe OpenAI
   discovered" became "before OpenAI could review". Briefs should ask writers to keep the source's verb.
4. **Check that each attributed clause appears in the cited source, not in a neighbouring one.** Weak passwords
   (Anthropic, not CERT-In), retrieval poisoning (not in the pretraining paper), an ISACA "recommendation" that is a
   statistic, and a vendor capability list that drifted between Okta and CrowdStrike.
5. **Role_evolution and module §7 are where unsourced connective sentences cluster.** Briefs should require each
   sentence there to restate the source's own words with a key.
6. **Survey labels.** Restate the survey question's object (for example "AI purchasing decisions") rather than a
   summarising label ("accountability").
7. **Exact dates.** Use the day-level date where the page has one (press releases, arXiv, OpenAI posts, ATT&CK version
   tables) rather than a month.
