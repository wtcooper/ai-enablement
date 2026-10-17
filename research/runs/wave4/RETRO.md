# Wave 4 retro: security archetype

Date: 2026-10-17 · Feeds: the plan's waves and costs, the brief templates, professional services (wave 3)

## Result

**Security archetype (pillar 2).** Added at the owner's request during wave 2. Eleven verified modules and 11
archetype-level files. Security is listed as available in `archetypes/index.md`.

The landscape scan read 139 sources and confirmed the 11 proposed modules against NIST CSF 2.0 and the CISSP domains.
With the owner's sign-off: fraud folded into human risk and identity; security architecture treated as a lens, not a
module; AI security run as three subtopic dives (threats and red teaming; agent identity and containment; governance
and assurance); one combined dive each for data security and privacy and for human risk. Module ids drop the
`security-` prefix (`operations`, `governance-risk`, ...).

| Module | Use cases | A/B | Evidence | Entries fixed by verifier |
|---|---|---|---|---|
| application-security | 17 | 88% | strong | 11 / 17 |
| operations | 24 | 83% | strong | 18 / 24 |
| ai-security | 25 | 80% | strong | 20 / 25 |
| vulnerability-exposure | 25 | 64% | strong | 13 / 25 |
| threat-intelligence | 24 | 58% | strong | 18 / 24 |
| incident-response | 22 | 55% | strong | 18 / 22 |
| governance-risk | 21 | 52% | strong | 17 / 21 |
| human-risk | 18 | 50% | strong | 14 / 18 |
| identity-access | 24 | 46% | moderate | 15 / 24 |
| data-privacy | 21 | 38% | moderate | 12 / 21 |
| cloud-infrastructure | 24 | 21% | thin | 14 / 24 |

**No entry was rejected.** 170 of 245 entries (69%) were corrected, slightly below waves 1 and 2.

**Archetype-level verification:** see `security-archetype-verification-A-report.md` and `-B-report.md`.

## What the evidence says

Security has much more named, measured practice than tax, but nearly all of it is self-reported or vendor-published.
The strongest themes: AI triage and investigation in the SOC (with the caution that the only independent benchmark found
every tested triage design missing at least 40% of attack alerts); AI finding vulnerabilities faster than teams can
verify and fix them; and agent containment, where 2026's incidents were read as ordinary cloud failures. Regulation
does not ban defensive AI; human judgment is tied to the decisions that start reporting clocks (SEC, NIS2, DORA, CRA).

## Cost and time

| Work | Agents | Model | Tokens (approx.) |
|---|---|---|---|
| Landscape scan | 1 | Sonnet | 0.3M |
| 29 module dives and 4 cross-cutting topics | 33 | Sonnet | 11.5M |
| Module synthesis | 11 | Opus | 4.0M |
| Module verification | 11 | Opus | 4.0M |
| Archetype-level synthesis and consistency pass | 2 | Opus | about 0.9M |
| Archetype-level verification | 2 | Opus | about 0.8M |
| **Total** | **60** | | **about 21.5M** |

Within the plan's 25-28M estimate for 11 modules.

## What went wrong, and what changed

| # | Problem | Change |
|---|---|---|
| 1 | Overlapping modules (application security and vulnerability exposure; operations, incident response and threat intelligence) were synthesized in parallel | Later syntheses were told to read finished modules and cross-reference by id; several dropped duplicates. Verification found off-by-one cross-references, fixed in the consistency pass. For future waves, synthesize the most overlapping modules in sequence |
| 2 | Conflicting ISACA figures (8% vs 71%) | Two ISACA releases from the same survey: global and European. The verifier settled it from the sources; product files use the global figures, European ones only when labelled |
| 3 | US agency pages print "Super Intelligence (SI)" where earlier documents say "AI" | Confirmed on the live NIST page by two fetch routes (and absent on unrelated sites), so it is real published wording. Titles are cited as issued; the advisor's prose says AI |
| 4 | Conference abstracts for talks not yet held were used as evidence | Verifiers relabelled them "scheduled" and excluded them from grade support. Add to the module-angle brief: an abstract of a future talk cannot support A or B |
| 5 | Two container restarts and the 20-agent limit | As in wave 2: queue file, commit after every completion, recover from disk |
| 6 | The strict grade A rule changed many candidates | Applied from synthesis on: A only where the named organization reports a measured figure; most vendor case-study numbers became B |
