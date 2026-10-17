# Wave 2 retro: tax archetype

Date: 2026-10-17 · Feeds: the plan's waves and costs, the brief templates, wave 4 (security)

## Result

**Tax archetype (pillar 2).** Eight verified modules and 11 archetype-level files. Tax is listed as available in
`archetypes/index.md`.

The landscape scan read 160 sources (105 opened) and changed the module list. With the owner's agreement:
- compliance split into individual and small-business returns, and corporate compliance (with credits);
- provision combined with Pillar Two;
- controversy widened to include tax-authority AI;
- professional responsibility researched once, as a cross-cutting topic, with `guardrails.md` as its home.

| Module | Use cases | A/B | Evidence | Entries fixed by verifier |
|---|---|---|---|---|
| research-advisory | 25 | 44% | moderate | 22 / 25 |
| compliance-individual-business | 25 | 40% | moderate | 16 / 25 |
| controversy | 25 | 40% | moderate | 17 / 25 |
| data-technology | 24 | 33% | moderate | 18 / 24 |
| indirect-tax | 22 | 18% | thin | 16 / 22 |
| transfer-pricing | 22 | 14% | thin | 16 / 22 |
| compliance-corporate | 24 | 12% | thin | 18 / 24 |
| provision-pillar-two | 16 | 0% | thin | 12 / 16 |

**No entry was rejected** in any module. 135 of 183 entries (74%) were corrected, close to wave 1 (about 72%).

**Archetype-level verification:** see the two reports `tax-archetype-verification-A-report.md` and `-B-report.md`.

## What the evidence says

Tax has far less measured evidence than assurance. Across every module the pattern is the same: plenty of rules,
vendor launches and conference talk; almost no published error rates, override rates or parallel runs. Controversy's
strongest evidence is about tax authorities (TIGTA, GAO, ANAO), not practitioners. Conduct regulators in the US, UK,
Australia and Germany all say existing duties apply to AI; no tax practitioner sanction was found.

## Cost and time

| Work | Agents | Model | Tokens (approx.) |
|---|---|---|---|
| Landscape scan | 1 | Sonnet | 0.4M |
| 22 module deep dives and 4 cross-cutting topics | 26 | Sonnet | 8.6M |
| Module synthesis | 8 | Opus | 2.6M |
| Module verification | 8 | Opus | 2.7M |
| Grade A re-check (assurance and tax) | 1 | Opus | 0.15M |
| Archetype-level synthesis and consistency pass | 2 | Opus | 1.0M |
| Archetype-level verification | 2 | Opus | about 0.8M |
| **Total** | **48** | | **about 16M** |

Under the plan's 20-25M estimate: fewer modules than assurance, and the low-evidence modules finished faster.

## What went wrong, and what changed

| # | Problem | Change |
|---|---|---|
| 1 | Web searches ran out at about 15 per agent; several agents got only 2-7 | Briefs already say to follow leads with `curl`; the landscape's leads per module carried most dives. Keep the landscape first and rich in leads |
| 2 | Only 20 subagents can run at once; 6 of 26 research agents had to queue | Queue file in the scratchpad; launch as slots free, highest-evidence modules first |
| 3 | Two container restarts interrupted the queue | All outputs survived on disk; recover by checking files and committing. Commit after every completion |
| 4 | Grade A was applied inconsistently: a recollection quoted in a vendor case study was A in wave 1 and B in a wave 2 verification | **Owner decision: strict rule.** A needs a figure the named organization reports as measured; recollections and rough estimates are B. Applied to vocabulary, schema, docs and briefs; 15 existing A entries re-checked, 3 moved to B |
| 5 | Module ids that repeat the archetype name produce ids like `tax-tax-data-technology-01` | Rename before research (`data-technology`); security ids drop the `security-` prefix |
| 6 | Synthesis of overlapping modules ran in parallel and could duplicate entries | Tell the later synthesis to read the finished module and cross-reference by id (done for application-security vs vulnerability-exposure in wave 4) |
| 7 | Verification corrected about three-quarters of entries again | No change: verification stays mandatory. The common fixes are the same as wave 1 (attribution, dates, statistics described as something else, scheduled events reported as held) |
