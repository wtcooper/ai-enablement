# Verification report: security / cloud-infrastructure

Checked on 2026-10-17 against the cited sources. These files were edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/cloud-infrastructure.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/cloud-infrastructure.md`

I opened every cited source key: the YAML keys plus the 22 keys listed only in module §10, 116 URLs in all. Most
were read directly with curl. The PDFs were read with `pdftotext`: CISA/NCSC-NZ, ENISA (2), CSA financial
services, the NIST IR 8596 draft, the OpenAI report and the DORA CTPP list. Dates come from `article:published_time`,
JSON-LD, arXiv submission history, pretalx schedules, PDF metadata or the Greenhouse boards API (`first_published`).
I checked every figure in the YAML outcomes and in module §5 against the source text. `scripts/validate.py` reports
0 errors. The module stays at 300 lines, table of contents included.

## Counts

| Action | Entries | Ids |
|---|---|---|
| Kept | 10 | 04, 08, 09, 11, 12, 14, 17, 19, 21, 23 |
| Fixed | 14 | 01, 02, 03, 05, 06, 07, 10, 13, 15, 16, 18, 20, 22, 24 |
| Rejected | 0 | none |

## Final grade mix

| Grade | Count | Ids |
|---|---|---|
| A | 0 | none |
| B | 5 | 02, 03, 06, 16, 22 |
| C | 14 | 01, 04, 05, 07, 08, 09, 10, 11, 13, 14, 15, 18, 21, 23 |
| D | 5 | 12, 17, 19, 20, 24 (all labelled "Idea") |

**#02 decision (grade A rule): B.** The only A figure was ZS's "around 95.17%" agreement between the Blue Agent and
analysts over a three-month parallel run, and it does not meet the rule:

- ZS has not published the figure itself. It appears only on an undated Wiz customer page, as the Director of
  Information Security's spoken quote, hedged with "around".
- The description of the method ("built an internal framework", "self-validated") is Wiz's narration, not ZS's.
- The page gives no case count, no definition of accuracy, no dates for the period and no account of how
  disagreements were handled.

The rule puts a practitioner's figure quoted in a vendor case study at grade B. The operations verification set the
same precedent: customer figures in vendor case studies stay B. Redis's 85.7% over 431 cases has the same weakness,
because Wiz relays it. The figure stays in the entry, labelled as a customer quote on a vendor page.

## Fixes

| Id / section | Change | Reason |
|---|---|---|
| #01 | Checkpoint changed from "engineers confirm exploitability and accept or reject the ticket" to "findings reach engineering only after a validation pipeline confirms exploitability". The unsourced opening clause of role_evolution was removed. "Cost of not acting" changed to "impact of not acting". The risk line no longer claims the filter hides future exploitable findings | CSA says only that pipelines require confirmed exploitability (embellished). The role clause had no source (unsourced connective). Microsoft says "impact". The Wiz blog does not make that claim |
| #02 | Grade changed from A to B. Notes rewritten. COTOOL-AGENTICSOC-2026 renamed UNSECURE-EVAL-2026, with publisher unsecure.sh | Grade A rule, see above. The scenario page is by John Ao and Michel San on unsecure.sh and never names Cotool (wrong publisher). The key now matches operations.yaml |
| #03 | HN risk rewritten. One commenter said the permissions are "not read-only", and the founders replied that destructive changes go through IaC | "Some practitioners preferred IaC PRs" is wrong: that was the vendor's own reply (wrong speaker) |
| #05 | Changed "4 failures in about a year" to "more than a year of operation". role_evolution now gives the speaker's lesson, without "on-call engineers" | The abstract says "over a year". On-call engineers are not mentioned (embellished) |
| #06 | Ownership sources (service catalog, tags, cloud event logs, CODEOWNERS, git blame) re-cited to WIZ-PILLAR2-2026. Prerequisite re-cited to PILLAR2 and Workflows. Checkpoint changed from "review pull requests before merge" to "choose to open a PR or send the fix to a coding agent" | The ownership list is in the Pillar 2 post, not the Green Agent or operating-model posts (wrong document). Review before merge is not stated (embellished) |
| #07 | "A fix that breaks production is why remediation stalls" changed to "fear of breaking production is the main reason". "One of five buckets" changed to "one of several". PatchWeaver changed from "single author" to "two authors at Dawn Computing" | Tamnoon's words. Its illustration describes four buckets. The USENIX page lists Rui Li and Shuang Cao |
| #10 | The generic "testers build harnesses" role claim was replaced with what the speaker did | Unsourced connective claim |
| #13 | Lightwell changed from "plans same-day protection" to "protections can be deployed the same day". The unsourced "WAF engineer's work shifts to reviewing rules" was removed | Source wording. The role shift is not in the abstract |
| #15 | role_evolution changed from "engineers move from writing rules to specifying intent" to FwChange's actual argument: vendor AI fits drafting, but the impact statement and verification need an independent check | FwChange does not say this (unsourced connective) |
| #16 | Changed "Coding agents run with the developer's own permissions" to "act on privileged developer endpoints". role_evolution now cites what Perplexity's team does | Perplexity says "privileged endpoints", not the developer's permissions. The first role clause had no source |
| #18 | Wiz posting date changed from 2026-08-19 to 2025-06-08, and the key renamed WIZ-JOB-CLOUDDET-2025 (used only in this file). The title notes that the version read was updated 2026-08-19 | Greenhouse API: first_published 2025-06-08. The old date was the update date (wrong date) |
| #20 | role_evolution changed from "detection engineers add deception scoring" to "no source describes a role change", plus what the abstract argues | Unsourced connective claim |
| #22 | "CrowdStrike quotes a customer analyst" changed to "cites an unnamed analyst's comparison" | CrowdStrike says only "one analyst" (embellished qualifier) |
| #24 | Measures changed from "SACR states the named vendors are not claimed to deliver the full model" to "category definition only; landscape 'not as a ranking'". role_evolution rewritten to SACR's actual framing | Neither statement is on the SACR page. The full report is gated behind a Palo Alto form |
| #06, #18, #22 (sources) | Locators for PILLAR2, Pinterest and Block now note how each source was read | Pinterest returned 403 and Block timed out. Both were read through the Greenhouse boards API; content and dates confirmed |
| Module header, §3 | Changed from "one A (#02)" to "5 graded B, none A". #02 now reads "Grade B: method unpublished" | Follows the #02 regrade |
| Module §1, §9 | CERT-In wording narrowed to the incidents it reported and the controls it asks organisations to apply. Dropped "the 2026 agent incidents" and "controls sit in cloud infrastructure" | The broad framing and the infrastructure claim are synthesis, not CERT-In's (unsourced connective) |
| Module §2 | Endpoint row changed to "act on privileged endpoints, approvals often skipped" | Same as #16 |
| Module §5 | ZS row relabelled. ENISA row changed from "misconfiguration 20.7% where a vector was identified" to "misconfiguration or accidental exposure, 20.7% of unauthorised-access incidents with an identified vector (5.2% had one)" | The ENISA figure combines two causes, covers one incident class, and rests on a small base (a statistic reported as something it doesn't measure) |
| Module §7 | Owkin credits Wiz's agents. La Centrale credits graph context and developer ownership, no longer "AI-assisted triage" | La Centrale's results come from graph context and developer ownership; its AI use is a proof of concept (embellished) |
| Module §8 | "Audited 37-CVE benchmark" changed to "its own 37-CVE benchmark (33 exploited)" | The audit is AWS's own per-sample check; "audited" implied a third party |
| Module §9 | TerraProbe figures qualified "for the primary model" | The abstract gives them for the primary model only |
| Module §10 | IEEESP-LLMSOC-2026 renamed ARXIV-2508.18947 and relabelled as an arXiv preprint "under review". EBA URL: stray `%5C` removed, and a note added that the 19 names are in the linked PDF. OpenAI URL corrected (the old one returned 404) | arXiv lists the paper as under review, and no IEEE S&P venue could be confirmed (wrong attribution). The CTPP list PDF names the 19 providers. The correct OpenAI URL matches ai-security.yaml |

## Sources that couldn't be reached directly

- **Pinterest (403) and Block (timeout) careers pages.** Both read in full through the Greenhouse boards API.
- **OpenAI incident report, module URL (404).** The corrected URL opened, and the report supports "narrower egress".
- **CISA BOD 26-04.** The cisa.gov page could not be found. Details rest on CrowdStrike's summary, which the YAML and
  module already label as such.
- **SACR full ACSP report.** Gated behind a Palo Alto form. Only the substack summary was read.
- **Unit 42 report PDF.** Gated, but the landing page carries Table 1 (cloud in 20% of incidents) and the over-90% figure.
- **Undated pages.** The Wiz customer stories (ZS, Owkin, Cohere, project44, La Centrale) carry no date in the HTML.
  The sitemap `lastmod` is a site-wide build stamp. The dates stay "2026".

## Targets

- **Use cases:** 24. Meets the 15–25 range.
- **Graded A or B:** 5 of 24 (21%). Below the 50% target. Most entries rest on vendor announcements, conference
  abstracts or research prototypes, and no cloud-security AI deployment with a published, organisation-measured figure
  was found.
- **Every source has a URL and an ISO date:** yes. Some dates are coarse by necessity:
  - five Wiz customer stories carry year-only dates because the pages are undated;
  - the EC AI Act page is undated and is cited with its retrieval date;
  - the Unit 42 month is inferred.
- **Quotations under 25 words:** yes. **Ids unique:** yes. **Vocabulary values:** valid per `validate.py`.

## Error patterns to fix in the briefs

1. **Wrong-document citation within one vendor's blog family.** Wiz says similar things across 10+ posts. Cite the post
   that actually contains the detail (here, ownership sources were in Pillar 2, not the Green Agent launch).
2. **Unsourced role_evolution openers.** Generic sentences such as "X teams move from A to B", placed before a real
   citation, recurred in #01, #10, #15, #16 and #20. The brief should require that a role claim be the source's own
   statement, or say "no source describes a role change".
3. **Vendor replies reported as practitioner views** (#03), and "customer" or "five" added to vague source wording
   (#07, #22).
4. **Claims from gated full reports cited to the free summary** (SACR #24). Cite only what the opened page says.
5. **Posting dates taken from "updated" rather than first_published** (Wiz job). Use the Greenhouse API.
6. **Statistics stripped of scope** (ENISA 20.7%): keep the population and the base rate with the figure.
7. **Venue claims for preprints** (IEEE S&P): check arXiv comments and journal-ref before naming a venue.
8. **Grade A from a customer quote on a vendor page** (#02). The 2026-10-17 rule should state plainly that "self-validated",
   as narrated by the vendor, is not organisation-reported measurement.
