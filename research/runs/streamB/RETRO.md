# Stream B retro: backbone library

Date: 2026-10-20 · Feeds: the plan, the library index, future refreshes

## Result

The shared library now has detailed files behind its working definitions:

- **11 pattern files** (`library/patterns/<id>.md`, 146-160 lines each): where each pattern fits, how it moves up
  the ladder, how it is built, prerequisites, failure modes and controls, metrics, governance, graded cross-industry
  examples, the strongest archetype use cases, and probes.
- **10 function cards** (`library/functions/<id>.md`, 148-191 lines each): processes, pain points, opportunities by
  Reimagine lens with graded examples, metrics, probes, guardrails and roles, with pointers to archetype entries.
- **Journey stages** (`library/journey-stages.md`, 250 lines): what moves a scope from one stage to the next, exit
  criteria, failure points, and how organizations are spread across stages. It complements `method/onboarding.md`
  §5 (diagnosis), which now links to it.

`library/index.md` links every pattern and function to its file. The validator reports 0 errors.

## Verification

| Files | Claims checked | Fixed | Removed | Main fixes |
|---|---|---|---|---|
| Patterns and index §3 | about 536 | about 42 | 4 | Figures sourced to the wrong document (evaluation report vs press release; a radio story instead of the VA inspector general); claims not in the source; misread denominators; one grade A to B; monitor-diagnose-act's usual ladder corrected to augment → automate |
| Function cards and journey stages | about 560 | 61 | 2 | Misread statistics (a variance read as disagreement; "less likely" turned into odds); independence overstated where authors had ties to the company studied; vendor papers typed as academic; 4 grades A to B |

The syntheses had already lowered 16 examples the research graded A (tool benchmarks, unnamed firms, time
estimates, a simulation) under the strict grade rule.

## What the evidence says

Across patterns and functions the pattern is the same as in the archetypes: speed and volume figures are common,
quality figures are rare. No production source reports override, escalation and error rates together for any
pattern. The best-measured examples are public-sector (UK government transparency records and trials, the VA
inspector general, DWP), and the clearest lessons come from failures (automated adverse decisions with no human
check or sampled control). No organization reaches grade A for document-to-decision, reconcile-exceptions or
end-to-end-case-agent.

## Cost

| Work | Agents | Model | Tokens (approx.) |
|---|---|---|---|
| Research (5 pattern groups, 4 function groups, journey stages) | 10 | Sonnet | 3.0M |
| Synthesis (patterns; functions and journey stages) | 2 | Opus | 0.7M |
| Verification | 2 | Opus | 1.0M |
| **Total** | **14** | | **about 4.7M** |

As planned (14 agents).

## Open items

| # | Item | Status |
|---|---|---|
| 1 | 227 archetype use cases are tagged `pattern: other`; the pattern synthesis proposes 18 re-tags (`patterns-synthesis-report.md` §4) | Not applied: it changes verified archetype files. Owner decision |
| 2 | Delegate-level evidence is thin in every function card | Recorded in the cards |
| 3 | ISO/IEC 42001 primary text not retrieved by any agent | Cited through secondary sources where used |
