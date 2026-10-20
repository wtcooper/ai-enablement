# Partner materials verification report

Date: 2026-10-20. Brief: `briefs/verify-partner-materials.md`. Files checked:
`plugins/ai-transformation/skills/transformation-advisor/references/method/leading-partners.md` and its pointers in
`method/index.md`, `method/people-and-change.md` and `SKILL.md`. Inputs: `topic-partners.md`,
`partner-materials-authoring-report.md`, spec `spec/2026-10-20-skill-suite.md`.

## Summary

| | Count |
|---|---|
| Research-backed claims checked (figures, quotes, attributions, named examples, rules, internal cross-references) | 69 |
| Kept as written | 44 |
| Fixed | 24 |
| Removed | 1 (one source cited as support for a claim it does not make) |
| Source entries checked (existence, URL, date) | 33 of 33; all dates correct |

All 33 sources were reached in some form (direct, the r.jina.ai mirror, or Crossref metadata). No figure was
wrong. The errors were the known patterns: survey figures with no population or survey owner (6), embellished
or drifted attributions (7), a statistic read as a change over time when it is a comparison (1), a wrong
provenance note (1), unlabelled synthesis (3), and an output target that does not exist in the plan template.

## Fixes and removals

| # | Where | Was | Now | Reason |
|---|---|---|---|---|
| 1 | §1 Diffusion | "essentially a social process" as Gawande's words | Rogers' phrase, quoted in Gawande's essay | Attribution drift: the quote is Rogers', cited by Gawande |
| 2 | §1 Success stories | Chair "gave the program to respected senior people rather than technologists" | Chair asked top business leaders, not technologists, to run it as a business problem | Embellished: the transcript says "most talented people… not tech people" were asked to build "the business side"; the tech team stayed |
| 3 | §2 intro | Profit depends on hours, rates, leverage and realization (no source) | Labelled "(advisor framing)" | Unsourced connective claim |
| 4 | §2 Client pressure | Outside counsel guidelines claim unattributed; survey "vendor co-run, secondary" | Attributed to a Gartner analyst quoted by Bloomberg Law; survey named: ACC and Everlaw, about 650 in-house counsel and legal operations staff | Attribution; survey population and owner |
| 5 | §2 Conflicting instructions | 40% "(vendor-affiliated survey)" | Thomson Reuters Institute survey of 1,500+ respondents in legal, tax, accounting, corporate and government work, 27 countries | Population and survey owner required |
| 6 | §2 Learning time | Chair "refuses billing credit for AI training" | Refuses associates billable-hour credit | The transcript's refusal is about associates; the file uses it in a partner context |
| 7 | §2 Leverage and pipeline | 179 vs 276 "(trade press, no named data origin)"; "Empson notes firms struggle to forecast partner income streams" | UK Big Four; "citing Financial Times analysis"; Empson reported as saying firms struggle to forecast potential partners' income under generative AI | Wrong provenance note: the article names FT analysis. Scope: UK firms. Empson's point is about potential partners, as reported |
| 8 | §2 Compensation | MANDS opinion presented as about AI | "on technology adoption generally" | The article is about practice-management software, not AI |
| 9 | §2 Greenwood | Partnership gives knowledge workers strong incentives "under particular conditions" | Partnerships have superior incentive systems for professionals, within limiting conditions | Abstract (via Crossref) argues superior incentives generally and names limiting conditions |
| 10 | §3 Segmentation | "two opinion sources make similar distinctions [BGOV-ODOWD-2026; MANDS-2026]" | One source [BGOV-ODOWD-2026] | **Removal:** MANDS-2026 contrasts partners with associates but does not segment partners |
| 11 | §4 step 2 | "18% of respondents" | 18% of TRI respondents (population in §2) | Population required |
| 12 | §5 "It makes things up" | "17% to 33% of answers… (independent)" | "between 17% and 33% of the time" (abstract's words); 2024 tool versions; independent academics | Abstract wording; tools dated |
| 13 | §5 "I tried it" | Routing failures to a test team attributed to Polsinelli | Polsinelli: "we'll get back to you"; routing labelled inference | The transcript does not mention routing |
| 14 | §5 Savings inflated | 56% "(vendor survey)" | LexisNexis survey of management consultants, sample not stated | Population and survey owner |
| 15 | §5 after table | Risk versus identity split and peer pairing | Both labelled advisor synthesis | Unsourced connective claim |
| 16 | §6 Leaders | ICAEW 47% and 53% "(independent survey)" | Ipsos for Chartered Accountants Worldwide; 2,718 chartered accountants, 48 countries, 2024 | Population and owner. The survey was commissioned by a network of professional bodies and run by Ipsos, so "independent" alone was loose |
| 17 | §6 Leaders | "Employees feeling positive about GenAI rose from 15% to 55% with strong leadership support" | 55% with strong support against 15% without, in BCG's survey of 10,600+ employees in 11 countries and regions | Misread statistic: a comparison between groups, not a change over time. Population added |
| 18 | §6 Visible use | "private skill-building… for seniors" attributed to LexisNexis | LexisNexis: specialist office hours and a safe place to ask questions; private sessions for seniors labelled inference | The source says nothing about seniors or private sessions |
| 19 | §6 Visible use | Edmondson cited without context | Psychological safety goes with team learning, from teams in one manufacturer | The scope of the evidence |
| 20 | §6 Write it down | Regular use higher "with at least five hours of training" | Plus in-person coaching; labelled an association | BCG pairs the five hours with in-person training and coaching; the figure is correlational |
| 21 | §6 Steer | Steering group of "senior legal and business-services leaders" | Employees and senior leaders from legal and business functions | CIPD names employees too |
| 22 | §6 Usage | 40% from 22% | Years (2026, 2025) and survey named | Dates and population |
| 23 | §7 Demand | MIT NANDA ">90%" "(weak, non-random sample)" | 52 organizations interviewed, 153 senior leaders surveyed; non-random, directional only | Population and survey owner |
| 24 | §9 Traps | One firm's no-cut commitment "worked in its own circumstances" | The firm's statement that AI would not cut support roles "lowered anxiety there" | Embellished: the case study reports lower anxiety, not general success |

Kept after checking (selection): Empson's "nebulous and fragile" quote and the leadership constellation; Perlin's
four variables; ABA 512 on fees and supervision (Rules 5.1/5.3); the Law Society saying AI "does not absolve you
of legal responsibility"; the SRA's 2026 warning as summarised by VinciWorks; the Magesh preregistration; the
Dell'Acqua figures (758 workers, 19%); the Deloitte A$440,000 final-instalment repayment; the A&O Shearman plan to
sell agents and share revenue (kept as a plan); PwC's alternatives to hourly billing and "no place" remark (kept as
FT-reported); KPMG's 2026 AI objectives and "not for policing"; Baker McKenzie's "phased out… evolve" with
consultation; A&O's "limited and localized headcount reductions"; Paperjam's "Absolutely not" and "two to three
hours a week" (recollections); Polsinelli's "90%" (verbal); Law360's champions, newsletter and service-desk
mapping; Kotter's short-term wins; the ADKAR elements; `assurance-controls-testing-07` recorded as grade B; and the
worked example's cross-references (`business-case.md` §7 range 180–1,190, checklist F1, `plan-and-control.md` §7
monthly practice leadership review, §8 leadership summary).

## Usability fixes

- **`SKILL.md` phase 6:** the Read now line again lists only the two phase files. The partner condition is now a
  separate instruction ("also read `leading-partners.md` and add a stakeholder map by role and one partner briefing
  per audience"), and the exit criteria name those outputs.
- **`SKILL.md` phase 7:** the partner file serves Plan (per `index.md`), but phase 7 had no pointer. Added one line:
  when partners must adopt the change, set written expectations (§6) and the learning-time credit rule (§2).
  `SKILL.md` is now 232 lines.
- **`leading-partners.md` §11 Output:** this section put the stakeholder map "under People and change", but the plan
  template has no such section. The map and briefings now go under Make the case and are carried into the people
  and change plan under Plan. Added "save after each, as for any phase."
- **`people-and-change.md` §7:** the pointer now also names leader expectations.
- **Core rules:** the file holds to them. People are named only as cited authors or quoted by role; role mapping
  only, and the advisor declines to rank people in the worked example; the worked example uses ranges; grade B is
  as recorded; no calendar deadlines (events only, such as "before the next methodology update"); no claims to
  build or run.
- **Formats:** these files contain no YAML schema examples. The only ids are `ct-07` and
  `assurance-controls-testing-07`, both existing ids; no new vocabulary ids.
- **Structure:** `scripts/validate.py` reports no ERROR. `leading-partners.md` is 299 lines (limit 300), and its
  contents list holds. Every backtick path resolves, including the four archetype `objections.md` files, each
  with a "How to respond well" section.

## Sources not reached directly

- Reached through the r.jina.ai mirror only (the direct fetch failed or was blocked): Accountancy Age, BCG AI at Work, Kotter, the Law Society
  (direct 403), and the HBS working-paper page (direct error).
- doi.org was blocked by the mirror. The abstracts for Greenwood and Empson (2003) and Edmondson (1999) were read through
  the Crossref API.
- Primaries not read (as in the research): Empson's 2013 report, Perlin's paper, ABA Formal Opinion 512, the SRA
  warning notice, the FT interview with PwC and the FT partner data, the full TRI 2026 report, the ACC/Everlaw
  report, the LexisNexis Future of Work report, and the full texts of the Magesh and Dell'Acqua papers.

## Open questions for the owner

1. **Sibling handoffs.** The spec gives `ai-enablement` "bringing partners and skeptics along" and champions,
   which overlaps §6 and §7 here. No sibling `SKILL.md` exists yet, so I added no handoff or description change.
   When siblings land: should `ai-enablement` read `../transformation-advisor/references/method/leading-partners.md`?
   Should the advisor's description and phase 7 hand champions and office hours to `ai-enablement` with the
   file-read fallback?
2. **One Read now per step.** Phase 6 still reads two files (`business-case.md` and `people-and-change.md`). That
   predates this work, so I left it.
3. **No room left.** `leading-partners.md` is at 299 of 300 lines. Any addition needs a cut, or the question bank
   (§8) could move into a companion file.
4. **Polsinelli in a partner context.** The no-credit rule applies to associates. It is still the only public
   example of a credit decision. Keep it, or find a partner-level example?
5. **MANDS-2026** concerns practice-management software, not AI. It is now labelled as such. Keep it, or drop it?
