# Verification report: security / application-security

Checked 2026-10-17 against the cited sources. Files edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/application-security.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/application-security.md`

All 80 URLs cited in the YAML were opened. So were the module §10 sources (NIST PDFs included) and the NCSC PDF. Most
were read with curl. OpenAI's pages, the Coinbase and MongoDB postings, CISA, BSIMM and gov.ie were blocked to curl
and read through `r.jina.ai` or the Greenhouse job-board API. Every figure in the YAML outcomes and in module §5 was
checked against the source text. `scripts/validate.py` reports 0 errors (17 use cases, 15 graded A/B, 88%).

## Counts

| Action | Entries | Ids |
|---|---|---|
| Kept | 6 | 04, 05, 06, 11, 13, 14 |
| Fixed | 11 | 01, 02, 03, 07, 08, 09, 10, 12, 15, 16, 17 |
| Rejected | 0 | none |

## Final grade mix

| Grade | Count | Ids |
|---|---|---|
| A | 4 | 04, 07, 10, 11 |
| B | 11 | 01, 03, 05, 06, 08, 12, 13, 14, 15, 16, 17 |
| C | 2 | 02, 09 |
| D | 0 | none (merged ideas are labelled grade D in notes) |

Before verification: A 5, B 11, C 1. Two entries were downgraded: #08 (A to B) and #09 (B to C).

## The two borderline A entries

- **#07 Google pre-submit scanning: kept A, with caveats.** The post says the triage agent "gets over 92% precision".
  Google states this as a metric for a named production deployment, which meets the letter of the A rule. It is
  precision without recall: a triage agent that rejects most findings can still score high precision. No method,
  sample or period is given. The grade now rests on that single figure. "Hundreds of vulnerabilities per month" and
  "3% false positives in some cases" are labelled as approximate claims that would not support A. Module §3 and §5
  now say the 92% is the precision of reachability verdicts and that no recall is published.
- **#08 AI code scanning: downgraded A to B.** The A rested only on "24 Android vulnerabilities". That is one GitHub
  Security Lab researcher's tally from vulnerability research on third-party apps, which is an adjacent process, not
  pipeline scanning beside SAST. It was published by the tool's own developer, with no false-positive rate or
  baseline. B rests on named real use without published measurements: NETGEAR (customer quote on OpenAI's page, found
  in the HTML) and vLLM use Codex Security, and GitHub Security Lab uses the taskflows.

## Abstracts of talks not yet given

[un]prompted 2026 (agenda read 2026-10-17; Day 1 = 27 Oct, Day 2 = 28 Oct) is the source for Stripe (#01, 28 Oct),
Google Mantis (#07, 27 Oct), AISLE (#08, 28 Oct), Rubrik (#09, 27 Oct) and Meta (#12, 27 Oct). None of these talks
has happened yet. Every such claim now says "scheduled" and is excluded from grade support:

- #01 stays B on Anthropic's present-tense description, the Mandiant threat-model gate and Cloudflare's spec reviewer.
- #09 drops to C. Its closure loop is known only from the Rubrik abstract.
- #12 stays B on Google's bug-fix agent and Copilot Autofix. The Meta "over 40%" figure is labelled as unpresented.

## Fixes and rejections

| Id / section | Change | Reason |
|---|---|---|
| #01 | Stripe material recast as a talk scheduled for 2026-10-28; outcome marked "does not support the grade"; notes give the actual basis for B; Anthropic's "judgement layer" added to role_evolution | The talk has not happened; the tense said it had |
| #02 | Problem sentence "assistants default to insecure patterns unless security requirements are stated" replaced with the two measured prompt effects (about 4 points; up to 45%) | Embellished cause; the sources show instructions help only partly |
| #02 | NCSC "accepts full vibe coding" changed to "accepts sliding towards full vibe coding" | NCSC frames it as positions on a spectrum |
| #02 | VERACODE-GENAI-2026 type survey changed to vendor | It is a vendor's own test, typed as vendor for the 2025 edition |
| #03 | Reproducer rule reworded: an AI assistant that finds a non-trivial bug must attempt a reproducer, write and test a fix, and say explicitly when it could not | The kernel page does not require that reports "include" a reproducer |
| #07 | Problem sentence "checking every finding for exploitability burns reviewer time" replaced with the post's latency point | Not in the source (unsourced connective claim) |
| #07 | Precision outcome now says recall, sample and period are missing; "hundreds" labelled approximate; Mantis talk tense now "scheduled"; notes explain why A is kept | Precision without recall; future talk |
| #08 | Grade A to B; notes rewritten | Adjacent process and one researcher's tally (see above) |
| #08 | "AISLE argues the harness (scan, detect, triage, patch) matters more than the model" changed to AISLE's quoted line that discovery is "a systems problem, not a single model call" | The AISLE post does not say this; the wording was embellished |
| #08 | Semgrep IDOR measures now say Mythos was graded by an LLM judge while the other runs used deterministic matching | The source states this caveat, and the entry left it out |
| #08 | Semgrep "3.5 times more true positives" attributed to its AI-powered detection versus Opus 4.8 alone | The source gives the figure for that comparison, not for Agentic Workflows |
| #08 | AISLE 25,000-trial risk marked as an abstract of a talk scheduled for 2026-10-28 | Future talk |
| #09 | Grade B to C; solution, risks, checkpoint and role text now say "scheduled"; checkpoint "an accountable owner signs formal risk acceptance" changed to "can end in formal risk acceptance" | Future-talk abstract cannot support B; "accountable owner signs" is not in the abstract |
| #10 | Note corrected: the CodeMender link-up is in the primary post, not only in search-only press | Wrong attribution of a detail |
| #12 | Meta tense now "scheduled" and excluded from grade; ARXIV-2609.29172 risk labelled as code-quality (not security) remediation | Future talk; adjacent process presented as security evidence |
| #15 | "Internal goals not met despite the AI-assisted tooling" changed to "the post does not separate the tooling's effect" | Embellished connective |
| #15 | "Throughput, not data quality, was the failing point: CVE assignment rate 91-94%" reworded | The assignment rate measures incoming requests, not GitHub's advisory quality (a statistic reported as something it doesn't measure) |
| #16 | AWS paraphrase changed to its own words: its controls "reduce contamination rather than eliminate it" | The old wording read like a quotation the source does not contain |
| #17 | Problem statement now attributes the chat-licence point to Trail of Bits' view of most companies and gives the 95% figure | Was presented as Trail of Bits' own experience |
| Module header | Added a caveat that [un]prompted claims are unpresented abstracts | Tense rule |
| Module §2, §3, §4, §5, §8, §9 | Stripe, Rubrik, Meta and AISLE claims say "scheduled" with dates; §8 [un]prompted line corrected to 27-28 Oct with the speaker split | Future talks; the old text implied the talks had been given |
| Module §3, §5 | #07 figure now "precision of its reachability verdicts"; table notes "no recall published" | Precision is not detection accuracy |
| Module §5 | "283 of 2,265 developers' first fixes" changed to "first fixes for 283 of 2,265 vulnerabilities across 236 assessments" | The figure counts vulnerabilities, not developers |
| Module §6 | NCSC "manual coding for..." changed to "slide towards manual coding for..." | Embellished |
| Module §7 | Reviewer load "doubled" changed to "roughly doubled" | Matches the abstract |
| Module §8, §9 | PortSwigger "new attack class" changed to "what he treats as evidence of a new desync class" | Embellished qualifier |
| Module §8, §10 | OWASP Global AppSec USA item and OWASP-APPSEC-2026 removed | Search-only, no URL (format rule) |
| Module §9 | AWS quote corrected to "reduce contamination rather than eliminate it"; AI-remediation study labelled code-quality; AISLE and Meta labelled as scheduled-talk abstracts | Misquotation; adjacent process; future talks |

## Sources that could not be reached

None was unreachable. These needed another route:

- **openai.com** (Codex Security and Aardvark): 403 to curl; read through r.jina.ai. The NETGEAR quote came from the HTML return.
- **Coinbase and MongoDB postings**: read through the Greenhouse job-board API, which also gave the posting dates for Anthropic, Reddit, GitLab, Cloudflare, Okta, Stripe, Datadog and Samsara.
- **CISA Secure by Design, BSIMM16 and gov.ie**: 403 to curl; read through r.jina.ai.
- **OWASP-APPSEC-2026**: it never had a URL, so it was removed.

## Targets

- **Use cases:** 17, within 15–25. Met.
- **Graded A or B:** 15 of 17 (88%), above the 50% minimum. Met.
- **Every source dated:** every YAML source has a URL and an ISO date. Met.
  - Undated pages (OpenAI docs, GitHub application card) carry the retrieval date and say so in the title.
  - The Linux kernel docs carry the year only.
  - In the module, every §10 key has a URL and a date now that OWASP is removed.

## Known error patterns: results

- **A statistic reported as something it doesn't measure:** #15 (CVE assignment rate read as data quality) and the
  #07 precision figure, now explicitly not detection accuracy.
- **A claim attributed to the wrong document or speaker:**
  - #08's AISLE harness line is not in the cited post.
  - #10's CodeMender detail is in the primary post, not only in press.
  - #17's licence point is Trail of Bits' view of other companies.
- **Embellished qualifiers or causes:**
  - #02 "default to insecure patterns unless..."
  - #03 "include a reproducer"
  - #09 "an accountable owner signs"
  - #15 "despite"
  - module "manual coding", "new attack class" and "doubled"
- **Unsourced connective claims:** #07's problem sentence on exploitability checks.
- **Wrong or missing dates and tense:**
  - Five [un]prompted claims were written in the past or present tense for talks scheduled for 27-28 October.
  - The module put the conference at "10-27 to 10-29"; the talks fall on 27-28 October.
- **Grade inflated by an adjacent process:**
  - #08 (vulnerability research on third-party apps used as evidence for pipeline scanning).
  - #12 and module §9 (code-quality remediation study used as evidence on security fixes).
  - #05 and #06 were already correctly capped at B for this reason.
- **Search-only figure in an A or B entry:** none found in the YAML. The module's only search-only item (OWASP) is
  removed.

## Patterns to fix in the briefs

1. **Conference abstracts.** Briefs should require the talk date and the words "scheduled" or "not yet presented"
   for any abstract of a future talk. They should also bar such abstracts from supporting A or B, even as
   corroboration for the problem statement.
2. **Precision without recall.** A precision or false-positive figure should name what it is the precision of. It
   should state that recall is unpublished.
3. **Counts from adjacent work.** A count of vulnerabilities found by a vendor's own researcher doing discovery
   research should not grade a pipeline or tooling use case A.
4. **Paraphrase in quotation marks.** Several "quotes" were paraphrases (AWS, AISLE). Briefs should require verbatim
   text for anything in quotation marks.
5. **Adjacent studies.** Label any study whose remediation, review or benchmark subject is not security
   (code-quality fixes, general bug-fix benchmarks, general code review) at the point of use, not only in notes.
