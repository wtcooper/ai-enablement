# Security consistency pass: report

Date: 2026-10-17. Scope: the 11 module files (`modules/*.md`) and 11 use-case files (`use-cases/*.yaml`) under
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/`. I did not touch the
archetype-level files (ARCHETYPE.md and the rest) or the archetypes index. I did not change what any source says,
changed no evidence grade, ladder or maturity, and deleted no entry. A script compared every entry with commit 9320596
(before this pass): all 245 entries are present with the same id, grade, ladder and maturity, and every entry cites
the same documents as before (old keys mapped to the new ones).

Result: `python3 scripts/validate.py` reports 0 errors. The 18 warnings are all the existing evidence-target warnings
(3 of them security: cloud-infrastructure, data-privacy, identity-access). Module lengths: ai-security 294,
application-security 289, cloud-infrastructure 300, data-privacy 276, governance-risk 285, human-risk 256,
identity-access 274, incident-response 298, operations 292, threat-intelligence 285, vulnerability-exposure 275. All
have a table of contents. Every YAML file loads.

Note on commits: snapshot commits (d8e54ca and earlier) picked up some in-progress edits to ai-security.yaml,
cloud-infrastructure.yaml, identity-access.yaml and threat-intelligence.yaml. The working tree holds the final state.

## 1. Build-process references removed

**YAML file headers** rewritten for all 11 files to a short scope line, "Sources checked 2026-10-17", the evidence
caveat, key notes where two similar keys name different documents (for example FINCEN alert PDF versus news release,
FLASHPOINT blog report versus press release, SANS press release versus landing page) and overlaps by full id.
Removed: "Synthesised/Merged from ... deep dives", `research/runs/...` paths, "landscape scan", "angle files",
"candidates in, N out", grade-change history ("regraded at synthesis", "Verified ... wave-4 verifier"), lists of old
keys each input file used, and "final ids not yet published" or "research-file ids, may be renumbered" (the
vulnerability-exposure header now names `security-application-security-02`, `-04`, `-07` and `-11`).

**YAML notes, automated pass (110 entries).** Removed the leading "Merged from P10, D08 and G06", "From practice-NN",
"From deep-dive NN" or "From discourse 07" sentence in cloud-infrastructure (7), governance-risk (21), human-risk (14),
identity-access (15), incident-response (21), operations (22) and threat-intelligence (10). Where that sentence held a
fact, the fact was kept in plain words (cloud-infrastructure-09 split reason; governance-risk-04 idea label;
incident-response-09 AIDA location, -18 BSides playbook, -20 NIST practice 5.5; operations-08, -22; threat-intelligence-
10, -11, -21).

**YAML notes and fields fixed by hand** (about 190 sentences across all 11 files):
- ai-security: "Merged: threats-redteam-NN, agent-identity-containment-NN, governance-assurance-NN" and "Source: ..."
  in 25 notes became "Covers ..." or were dropped; "the two deep dives name the harness differently" became "sources
  name ..."; "the landscape file dates" became "Axios reported".
- application-security, vulnerability-exposure: "Merged from all three angles", "Also in application-security
  research (practice UC 06, governance UC 06)", "the vulnerability-exposure synthesis dropped its copy" removed or
  replaced by full ids of the entries that hold the item.
- Grade history became the decision and its reason: "Downgraded from A to B in verification" became "Graded B, not
  A" (application-security-08, vulnerability-exposure-06, human-risk-10, data-privacy-14); "lowered from B to C"
  became "Graded C, not B" (application-security-09, governance-risk-04, -11); "raised from C to B at verification"
  became "Graded B, not C" (operations-22); "Graded B under the 2026-10-17 rule" became "Graded B, not A" (all files);
  "The discourse file graded this A" and "P and D said augment" were rewritten as the grade or ladder and its reason.
  No grade changed.
- "Verifier 2026-10-17 opened ...", "previously cited", "an earlier draft attributed", "synthesis cited the DHS
  inventory" became plain facts (incident-response-04, -16, -20, -21; threat-intelligence-08, -09, -12, -13, -23).
- Locators: "(routed from the ... dive)", "(as routed by the ... file)", "(read by the research angle; cisa.gov blocked
  the verifier ...)", "(read via text mirror by the practice researcher)" removed or reworded (ai-security, application-
  security, human-risk, incident-response, operations, threat-intelligence, vulnerability-exposure).
- governance-risk notes pointed to `research/runs/wave4/security-x-*.md`; they now point to the archetype's
  guardrails and workforce files.
- threat-intelligence-24 said "this file was compiled by an Anthropic model"; it now says Anthropic also makes the model
  behind this advisor (the conflict disclosure is kept).

**Modules:** all 11 stamps normalised to "Sources checked 2026-10-17" (human-risk said "Last reviewed and source-
verified"). Removed: incident-response header link to the verification report and "(opened by the research angles;
reopened by the verifier)"; ai-security "(routed from vulnerability-exposure)" (2) and "verified 2026-10-17";
application-security "(all opened by the research angles)"; data-privacy "This module had one combined deep dive";
governance-risk `research/runs/...` paths (now `../guardrails.md` and `../workforce.md`, which exist) and "the
landscape scan asked to add"; human-risk and identity-access "the landscape scan"; operations "(checked at
verification)" and "CAUCHY-IRNB-2026 in the operations inputs". Kept as ordinary usage: "research-synthesis" (work
type), "verification" as a control, "researchers" meaning outside or academic researchers, "routed" meaning work sent
to a person, NIST "practice 4.1" numbers, "patch wave" (NCSC).

## 2. Source keys

Before the pass, 859 distinct keys were used across the 11 YAML files; now 842. Each document has one key, and every
record of a key has the same title, publisher, type, URL and date (a script finds no key with differing metadata and no
URL under two keys, comparing EUR-Lex documents by CELEX number). Source lines in the flow-style files were re-emitted
with every free-text value double-quoted; two arXiv publisher values with unquoted commas in identity-access had been
silently parsed as extra keys and are now fixed.

**Same document, two or three keys (merged), new key first:**
NISTCISA-IRKEY-2026 (from NIST-KEYPRACTICES-2026 and CISA-KEYPRACTICES-2026; URL is the NIST document itself, type
standard-setter, publisher "NIST CAISSI, NSA and CISA"); TOB-AUDIT-2026 (TOB-MIDEN-2026); SECURITYWEEK-SAFE-2026
(SECWEEK-SAFE-2026); OPENAI-HFREVIEW-2026 (OPENAI-HFUPDATES-2026); OPENAI-HFINC-2026 (OPENAI-HF-2026);
HELPNET-GARTNER-2026 (HNS-GARTNER-2026); DATABRICKS-JOB-IR-2026 (DATABRICKS-JOB-2026); CURL-STENBERG-2026
(STENBERG-MYTHOS-2026); ANTHROPIC-GLASSWINGUPDATE-2026 (ANTHROPIC-GWUPDATE-2026); NYDFS-AIGUIDE-2024
(NYDFS-AIIL-2024); EU-AIACT-ART73-2024 (FLI-AIACT73-2024); HF-DISCLOSURE-2026 (HUGGINGFACE-INCIDENT-2026);
NIST-IR8596-2025 (NIST-CYBERAI-2025); EURLEX-NIS2-2022 (EUR-LEX-NIS2-2022, EUR-NIS2-2022); DEFCON-34-SPEAKERS-2026
(DEFCON-34-2026); CLOUDFLARE-JOB-CMDC-2026 (CLOUDFLARE-JOB-2026). Module-only duplicates: DORA-RTS-2024
(EURLEX-DORA-RTS-2024), EUR-DORATLPT-2025 (EURLEX-DORATLPT-2025), EC-CRAREPORT-2026 (EC-CRA-REPORTING-2026),
NIST-80061R3-2025 (NIST-SP80061R3-2025), VULNCHECK-1H-2026 (VULNCHECK-1H2026).

**One key, two documents (split):** RISKYBIZ-2026 means the "Srsly Risky Biz" post (incident-response); the podcast
feed cited in data-privacy is now RISKYBIZ-FEED-2026.

**Kept separate (different publications):** ARXIV-2607.14493 (preprint) and USENIX-LOGINJECT-2026 (proceedings);
ARXIV-2512.09882 and ICLR-ARTEMIS-2026; TOB-AINATIVE-2026 and TLDRSEC-TOBAINATIVE-2026; CSD-ISACAI-2026 and
HISAC-AIISAC-2026; the two Reality Defender case-study pages; FINCEN-DEEPFAKE-2024 and FINCEN-DEEPFAKE-NR-2024.

**Metadata choices:** the most common value, or the fuller one. Per-citation detail that had been put in titles
(talk names under BSIDESLV-2026, FIRST-CON-2026, USENIX-SEC-2026, DEFCON-34-SPEAKERS-2026; "PDF v1.0"; "blog
summary"; "NCSC-NZ copy") moved to the locator. Choices worth knowing: CISA-AGENTIC-2026 uses the cyber.gov.au PDF
(6 of 10 records); CSA-MYTHOSREADY-2026 the landing page; ENISA-ETL-2026 the PDF, dated 2026-09-22; EC-AIACT-2026
dated 2026-10-17 (undated page, retrieval date); EURLEX-NIS2-2022 and EU-AIACT-ART73-2024 dated by adoption
(2022-12-14, 2024-06-13); OKTA-AIAGENTS-2026 2026-05-27 (the more specific date, from data-privacy); WIZ-AISAST-2026
titled with the article heading (checked with one request). Types: OpenAI, Anthropic and Hugging Face accounts of their
own incidents are vendor, METR academic, SANS-SOC-2026 survey, MANDIANT-MTRENDS-2026 vendor.

**Module source lists:** every bracketed key in each module resolves to its own YAML or its own Sources list (script
check, all 11). Module entries for keys that are in a YAML now match that YAML's title, URL and date (17 entries fixed,
including DORA-RTS-2024 and EURLEX-NIS2-2022 URLs, CISA-AGENTIC-2026 URL, EC-AIACT-2026, FINRA-ROR-2026,
WIZ-AISAST-2026, SIFMA-SEC-2026, GTIG-AITRACKER-2026 and Splunk titles).

## 3. Cross-module references

All references use full ids (`security-<module>-NN`); governance-risk YAML and module used bare `ai-security-21` and
`operations-19/20/21` forms, now expanded. A script finds every `security-<module>-NN` reference in modules and YAML
resolves (the one non-match is a URL slug), and I read all 262 cross-module references against the target titles.

Wrong or stale ids fixed:
- ai-security-13 and -14 cited `security-application-security-21` (does not exist): now `-14` (screening inbound
  code, packages and skills).
- operations-23 cited `security-incident-response-25` (does not exist): now `-22` (responders as builders).
- operations: containment playbooks pointed to `security-incident-response-14` (summaries) in the YAML and module:
  now `-11`; AIDA and log hardening pointed to `-11`: now `-09`; SherAgent pointed to `-08`: now `-07`; module "case
  notebooks and timelines are -07 and -04; provenance-graph agents are -08" now reads timelines `-04`, provenance-graph
  `-07`; the CAUCHY notebooks note no longer claims a use case. operations-21 named "scenario scorecards" in
  `security-incident-response-12` (a digital-twin idea): that clause was removed.
- identity-access: per-action authority `security-operations-21` now `-20`; MDR shift `-23` now `-22`; tuning loop
  `-18` now `-17` (YAML and module); "provisional id" removed from `security-governance-risk-07`.
- governance-risk-13: "identity-access (agent identity)" now `security-ai-security-06`; unnamed application-security
  pointers now `security-application-security-02` and `-17`.
- human-risk said Datadog's fake-applicant session "is held in full as security-threat-intelligence-21"; that entry is
  Grow Therapy's hunting. The session is in `security-human-risk-12`; human-risk header, note, solution and module, and
  the threat-intelligence module, now say so.
- vulnerability-exposure said the Mandiant harness's IR use is `security-incident-response-10`; the incident-response
  file places it in `security-vulnerability-exposure-04`, so the note and header now say entry 04 covers it.

**Overlaps:** no exact duplicates, so nothing was deleted. Where two entries describe the same change, the thinner one
names the fuller one, and I added reverse links where only one side had one: incident-response-17 to ai-security-19,
operations-12 to incident-response-03 (duplicate sentence removed), ai-security-21, -22 and -24 to governance-risk-04,
-17 and -18, -03; application-security-14 to ai-security-14; vulnerability-exposure-06, -09, -19 to
application-security-09, -11; vulnerability-exposure-17 and -22 to ai-security-10 and -08; vulnerability-exposure-21 to
cloud-infrastructure-06.

## 4. ISACA 2026

Every module and YAML entry uses the global figures (8% run AI-related incident exercises regularly, 64% none;
ISACA-SOC-2026, ISACA-SOCINFO-2026). The European figures (5% regularly, 71% none, 60% in AI-use policy; 494
respondents) appear only in governance-risk (module §6 and entries 17 and 18) and are labelled European with
ISACA-SOCEU-2026. ISACA-AIPULSE-EU-2026 (incident-response module) is labelled European. governance-risk-17 no longer
says the European figures were "read by the cross-cutting regulation file".

## 5. "Super Intelligence" wording

Titles are cited as issued (NISTCISA-IRKEY-2026 keeps "Super Intelligence" in its title). Advisor prose says AI:
incident-response-17's solution now reads "NIST, NSA and CISA published" instead of "NIST CAISSI, NSA and CISA".
One short note per file: ai-security YAML header (with the 2026-09-29 Executive Order and "search both terms"; the
duplicate in ai-security-22 removed), incident-response-17, operations-20 and operations module §6. Source-record
notes on retrieved page titles (CISA-PLAYBOOK-2026, NIST-CAISI pages, ServiceNow) are metadata and were kept.

## 6. Wording

- "Measured" removed for entries graded B or lower: application-security-05, -06, -08, -16; cloud-infrastructure-02,
  -03; data-privacy-01, -14, -15; governance-risk-02; incident-response-08; operations-10 (title now "tested in
  controlled studies"); data-privacy module §3 (an idea entry). Remaining uses are A entries, negations ("no measured
  outcome") or interview questions.
- Terms of art explained at first use where they were not: OSINT, TLP, IOC, SIEM (threat-intelligence); IR, CIRCIA
  (incident-response); IAM, WAF, MCP, KEV, SAST (cloud-infrastructure); PSIRT, SBOM (application-security); PSIRT,
  NVD, AISI (vulnerability-exposure); IGA, OTP (identity-access); GPAI, SSO, MAS (ai-security); NYDFS (human-risk).
- Module headers now all say "other modules' ids are in full".
- Attacker detail: no change needed; entries already omit exploit steps.

## 7. Files changed

Modules: all 11. Use cases: all 11. human-risk `last_reviewed` values were quoted for consistency.
