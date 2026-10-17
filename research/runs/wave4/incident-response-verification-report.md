# Verification report: security / incident-response

Checked on 2026-10-17 against the cited sources. These files were edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/incident-response.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/incident-response.md`

Every cited source key was opened. That covers the 90 YAML keys and the 9 keys listed only in module §10. Most
pages were read directly with curl. The blocked pages were read through `r.jina.ai`: OpenAI (3), EUR-Lex (3), SEC,
Axios, SecurityWeek, Cyber Triage, Rubrik (2), N2WS and Block. These PDFs were read in full with `pdftotext`:

- NIST SP 800-61r3
- the NIST/NSA/CISA key practices (PP-26-4396)
- the CERT-In blueprint
- SIABench (arXiv 2603.06422)
- SherAgent (arXiv 2607.09176)
- the ASD ACSC copy of the agentic-AI guidance (through the mirror)

Greenhouse posting dates were checked against the boards API. The CIRCIA status was checked against the Federal
Register API. `scripts/validate.py` reports 0 errors for these files: 22 use cases, 12 graded A or B (55%). The
remaining errors are in the tax and cloud-infrastructure files.

Note: another agent's commit (`3aea8a9`, application-security verification) swept these in-progress edits into git.
The files on disk are the final verified versions.

## Counts

| Action | Entries | Ids |
|---|---|---|
| Kept | 4 | 01, 06, 07, 08 |
| Fixed | 18 | 02, 03, 04, 05, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 |
| Rejected | 0 | none |

## Final grade mix

| Grade | Count | Ids |
|---|---|---|
| A | 1 | 14 |
| B | 11 | 03, 04, 05, 08, 16, 17, 18, 19, 20, 21, 22 |
| C | 9 | 01, 02, 06, 07, 09, 10, 11, 13, 15 |
| D | 1 | 12 (labelled "Idea") |

**Grade A rule.** Only #14 meets the rule. Google reports a measured 51% time saving on 300 summaries, a 10% higher
rating in a blind test of 50 against 50 summaries, and a 53% saving on executive updates. #20 (OpenAI) was
downgraded to B. Its figures (about 50 PB, over 100 organisations notified, about 7,000 GPUs, 45 minutes to days per
case) count scale, cost and effort, and none measures an outcome of the AI stages. Other figures stay below A for
these reasons:

- SANS's 14-minute demo and 119-of-143 judge run (#05) are demonstrations.
- Meta's 42% (#08) is a reliability incident, so adjacent-process evidence caps the entry at B.
- SherAgent's verified 96% (#07) comes from an unnamed SOC.

## Fixes and rejections

| Id | Fix | Reason |
|---|---|---|
| #16 | Problem, solution, title, outcome and notes rewritten from the Cloudflare post. The reviewer is "mandatory" for high-severity incidents, and reports "are not considered complete until all findings have been addressed". The outcome changed from "none published" to "more than 200 incident reports assessed" since May 2026 (93% low-impact), labelled as usage, not effect. Adjacent-process note added | The earlier wording ("blocks closure of high-severity incidents") came from the tl;dr sec summary, not the post. The problem stated a motive the post does not give. The post does publish a usage count. Its postmortems cover engineering incidents generally |
| #20 | Grade A changed to B. "50 PB searched" changed to "under review (ongoing)" | Scale and cost counts are not a measured outcome. The review is one month in |
| #04 | role_evolution corrected | Hugging Face's "far beyond what an operator could sustain by hand" describes the attacker's pace, not how hard manual reconstruction was (misread) |
| #04, #14, #03, #05, #11, #12 and module | Cross-references to operations.yaml corrected: 13→12, 14→13, 20→19, 21→20, 22→21, 25→24. The phantom "DNB notebooks and Centene pipeline (security-operations-12)" was removed. The module now places Centene in #04 | operations.yaml has had this numbering since the incident-response synthesis. It has no Centene or DNB-notebook entry (claim attributed to the wrong document) |
| #17 | Prerequisite "inventory of AI systems… with an owner" replaced by what practices 2.1 and 2.3 say. "Logging of prompts, tool calls, identities, permissions (THN)" replaced by THN and CERT-In's "tamper-resistant log of agent actions". The "executive and legal participation (NIST Table 2)" checkpoint replaced by SP 800-61r3 §2 (leadership authority over shutdown). Wording softened: OpenAI "is strengthening" its plan, not "strengthened"; WIRED "days and weeks" | Unsourced connective claims. The THN wording actually comes from SAFE/Axios. NIST Table 2 does not mention executives or legal |
| #21 | The Techzine source was replaced by the primary SAFE RFC on GitHub (OSAA-SAFERFC-2026). It confirms the 72-hour customer notice, the 14-day advisory, the 4 business days, 30 days and 90 days. "Grown from 37 (Techzine)" was replaced by SiliconANGLE's "roughly two dozen founding members". The CERT-In problem was scoped to the evaluation cases. A no-safe-harbour risk was added (Axios). "Terms may change" was removed | Techzine returned a bot challenge to both routes, so its figures could not be confirmed. "Terms may change" was not in the cited sources |
| #09 | The CyCraft "inventory of every place an LLM ingests text" was reworded to the artifacts CyCraft names. NIST 4.1 was flagged as written for monitors of AI agents. "Detection-engineering work" was removed | Embellishment, and an adjacent source applied without saying so |
| #11 | Mandiant prerequisite rewritten to what the report says (machine-speed playbooks, read-only agent permissions) | "Playbooks stating which actions may run without approval, with each action logged" is not in the report |
| #10 | Risk "Not all incidents produce guided responses" replaced by the documented incident types. The checkpoint no longer says "execution is by the analyst" | Neither is stated on the Microsoft Learn page |
| #02 | "So many exercises stay generic" removed. role_evolution ("directing and curating") replaced by Immersive's actual claim | Embellished qualifier. The role-evolution claim was not in the post |
| #03 | The cost claim now cites DEW #164 (moved from #04, where it was unused). The leadership-decision checkpoint was re-attributed to DEW #165 ("up to your CSO"). "Lab leader" became "OpenAI's Dean Ball". Connective "alongside tooling and retainers" removed | The claim was attributed to the wrong document (HF does not mention leadership), and the connective claim was unsourced |
| #05 | Problem "intrusions complete in minutes… a day or more" changed to SANS's "consumes an analyst's day". BankInfoSec date "2026" changed to 2026-08-12 and title updated to the page title. Proskauer date changed to 2026-07-29. The SIABench 33.33% figure is now described as one hard scenario (15 questions) | Embellishment and incomplete dates |
| #13 | "Executes only what you approve" and approval of the recovery sequence re-cited to RUBRIK-AI-2026 | The wording is on the product page, not the press release |
| #14 | Problem changed to Google's "we estimate… nearly an hour" | The figure is an estimate, not a measured baseline |
| #15 | DORA Art. 5(2) late-classification case added. "Single reporting point managed by ENISA" changed to the Digital Omnibus proposal (ENISA is not named in Hunton). CIRCIA status extended: no final rule in the Federal Register through 2026-10-17. GOV.UK date changed to 2025-04-01 | Embellished qualifier, and a regulatory detail was missing |
| #18, #11, #17 | CISA-AGENTIC date changed from 2026-05-01 to 2026-05 | cisa.gov blocked both routes. The ACSC PDF path supports only the month |
| #19 | Anthropic title corrected ("Improving our alignment and security practices"). 19 July alert worded as in the source (Artifactory credentials). role_evolution no longer says "on-call duty" | Wrong title, and an inference that was not stated |
| #22 | "Without matching headcount" removed. Twilio "evidence triage" is no longer described as LLM-based. Cloudflare "autonomously" changed to "independently" (it describes the human) | Embellishment, and an ambiguous qualifier that could suggest AI autonomy |
| Module §2, §3, §5, §9 | Cloudflare row corrected. COTOOL-AGENTICSOC-2026 renamed UNSECURE-EVAL-2026 (the key operations.yaml uses). The page is by John Ao and Michel San on unsecure.sh and never names Cotool. "#14 only A" | Claim attributed to the wrong publisher. The same document must carry the same key |
| Module §6, §8, §9 | DORA intermediate and final deadlines made precise. EU Action Plan wording limited to the landing page (no JRC, no "incident response"). The Register objection reworded to what the podcast said (vendors privately called it partly marketing, and the FBI and Inglis called it real). "No independent measure exists yet" changed to "was found" | Embellished or overstated wording |

## Sources that couldn't be reached

- **Techzine** (TECHZINE-SAFE-2026): the bot challenge blocked curl and the mirror. The source was removed and its
  claims were replaced by the SAFE RFC and SiliconANGLE.
- **cisa.gov** (CISA-AGENTIC-2026, CISA-CIRCIA-2026): returned 403, and the mirror is blocked until 19:00 UTC.
  CISA-AGENTIC was confirmed through the ASD ACSC PDF. CISA-CIRCIA was not opened, but its claim is cross-checked
  against the Federal Register API.
- **Not opened** (gated or not retrievable): the OpenAI technical report PDF, full M-Trends 2026, the full Magnet
  2026 State of Enterprise DFIR report, the full ISACA report, the SANS 2026 AI Survey (a Swimlane summary only),
  Forrester's report (a PANW landing page only) and the CIS white paper PDF. Entries already label these as summary
  or landing-page reads.

## Targets

| Target | Result |
|---|---|
| 15–25 use cases | Met: 22 |
| At least 50% graded A or B | Met: 12 of 22 (55%), the same count as before; one A became a B |
| Every source dated | Met: every source has a URL and an ISO date. Year-only dates remain where the page gives no more: SANS-FINDEVIL, MANDIANT-MTRENDS-EXEC, SANS-SOC, EC-AIACT and SANS-AI, whose JSON-LD dates conflict (2026-05-18 and 2026-05-20, displayed 2026-08-17) |
| Ids unique, vocabulary values valid, quotations under 25 words | Met (validator plus a manual check) |

## Known error patterns: results

- **Statistic reported as something it doesn't measure.** Found in #20: counts of scale and cost were treated as
  measured outcomes. Also found in #16, where a code-review figure was correctly excluded, but a usage count had been
  missed. The SIABench 33.33% figure was clarified.
- **Wrong document or speaker.**
  - The operations cross-references were off by one, and one target did not exist.
  - "Cotool" was not named on the page.
  - THN was cited for a logging wording that comes from SAFE.
  - NIST Table 2 was cited for executive and legal roles it does not mention.
  - HF was cited for a leadership decision that comes from DEW.
  - The Cloudflare wording came from tl;dr sec.
- **Embellished qualifiers or causes.** Found in #02 ("stay generic"), #05, #15 (ENISA), #16 (motive), #22
  (headcount, "autonomously") and the module (JRC, "exists yet").
- **Unsourced connective claims** in role_evolution and risks_and_guardrails. Found in #02, #03, #09, #10, #17, #19
  and the #11 prerequisites.
- **Wrong or missing dates.** BankInfoSec (year only, now 2026-08-12), GOV.UK (now 2025-04-01), Proskauer (now
  2026-07-29), CISA-AGENTIC (day unverifiable, now 2026-05). All other dates matched the bylines or JSON-LD.
- **Grade inflated by adjacent-process evidence.** #08 is already capped at B. #16's postmortems are general
  engineering incidents (noted, still B). The NIST practices, written for AI-agent monitors, were applied to analyst
  tools in #09 (now flagged).
- **Search-only figure in an A or B entry.** None found. Every source in A and B entries was opened. The one claim that
  rested on an unreachable source (Techzine, #21) was replaced.

## Patterns of error to fix in the briefs

1. **Routed items must be re-read at the primary source.** #16 rested entirely on another module's reading and carried
   a newsletter's paraphrase. Require the synthesiser to open any routed source that supports wording in a B entry.
2. **Check cross-module ids against the current target file**, not against a research draft. The ids here were off by
   one, and one entry was phantom.
3. **Name a publisher only if the page names it.** Do not carry over attributions from search snippets or other
   research files.
4. **For prerequisites and checkpoints, cite the clause that says it.** Practice numbers and table numbers were often
   adjacent, not exact.
5. **Grade A needs an outcome measure**, a before-and-after or an accuracy figure. Volume, cost, notification counts
   and per-case effort ranges are B evidence even when reported as data.
6. **Watch for direction errors** in sentences about speed and difficulty. Hugging Face's "beyond what an operator
   could sustain" referred to the attacker.
7. **Record full ISO dates** from bylines or the Greenhouse API. Do not fall back to the year when the page carries a
   date.
