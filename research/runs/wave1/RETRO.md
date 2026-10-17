# Wave 1 retro: assurance archetype and stream M (method)

Date: 2026-10-17 · Feeds: the plan's waves and costs, spec revision 6, the brief templates

## Result

**Method (pillar 1).** Eleven phase and cross-cutting method files plus an index.

- They were built from 8 research topics, merged by two editors and checked by two verifiers.
- Verification: 337 claims checked, 75 fixed, 3 removed.
- Every reference to the build spec was removed, and the wording is consistent across files.
- Validator: 0 errors.

**Assurance archetype (pillar 2).** Ten verified modules and 11 archetype-level files: `ARCHETYPE.md` with evidence ratings, an interview guide, value chain, economics, state of AI, 29 frontier signals, guardrails, workforce, disruption, objections and sources.

| Module | Use cases | A/B | Evidence | Entries fixed by verifier |
|---|---|---|---|---|
| controls-testing (pilot, all research on Opus) | 25 | 64% | strong | 21 / 25 |
| substantive-testing | 25 | 52% | strong | 15 / 25 |
| soc-attestation | 16 | 56% | strong | 15 / 16 |
| planning-risk-assessment | 25 | 44% | moderate | 20 / 25 |
| quality-management | 25 | 40% | moderate | 17 / 25 |
| assurance-over-ai | 24 | 25% | thin | 17 / 24 |
| acceptance-independence | 21 | 19% | thin | 19 / 21 |
| completion-reporting | 18 | 17% | thin | 8 / 18 |
| specialists | 13 | 15% | thin | 12 / 13 |
| sustainability-assurance | 13 | 0% | thin | 6 / 13 |

**No entry was rejected** in any module. Every source behind the use cases was opened, and only a handful were unreachable.

## Cost and time

| Work | Agents | Model | Tokens (approx.) |
|---|---|---|---|
| Landscape rerun and 8 method topics | 9 | Sonnet | 2.7M |
| 23 module deep dives | 23 | Sonnet | 9.1M |
| 5 cross-cutting topics | 5 | Sonnet | 1.5M |
| Method synthesis and verification | 4 | Opus | 1.4M |
| Module synthesis | 9 | Opus | 3.1M |
| Module verification | 9 | Opus | 3.7M |
| Archetype synthesis, two verifiers, consistency pass | 4 | Opus | ~1.8M |
| **Wave 1** | **63** | | **~23M** |

- **Wall-clock time:** about 2 hours, with up to 20 agents at once.
- **Versus the estimate:** the plan estimated about 17M tokens for this wave. The overrun came mainly from the landscape recommending **10 modules instead of 8**, which added deep dives. Deep-dive agents averaged about 390k tokens on Sonnet, against the pilot's 380k on Opus. Sonnet saved money per token, not tokens.

## Sonnet research against the all-Opus pilot

- **Correction rate:** verifiers fixed 129 of 180 entries (72%) in wave 1. The pilot's rate was 84%.
- **Rejections:** zero in both.

Research on Sonnet, with synthesis and verification on Opus, is at least as accurate as all-Opus, and cheaper. **Keep it.**

Fixes concentrate in the same places as the pilot: attribution, overstated wording, dates, and figures reported as something they don't measure. Synthesis introduces most of this drift, so **verification stays mandatory.**

## What went wrong, and the fixes

| # | Issue | Fix |
|---|---|---|
| 1 | **The web-search quota is shared across agents and ran out mid-wave.** Later agents got 4–16 searches each | Briefs now say to follow the landscape's leads and known pages with `curl`, and to ration searches. For future waves, the landscape scan should run *first and alone*, and should list more leads per module |
| 2 | Sites blocking `curl` (McKinsey, BCG, Gartner, PCAOB pages) | The `r.jina.ai` text mirror worked. It is now in the briefs |
| 3 | **The shared scratch folder caused collisions.** Two agents overwrote each other's downloaded files | Every brief must tell agents to use a private working folder (`mktemp -d`) |
| 4 | Snapshot commits captured files mid-write | Harmless, since final versions were committed after. Commit by name where possible |
| 5 | Evidence-thin modules can't reach 50% A/B honestly | **Policy:** the A/B target applies where public evidence exists. Thin modules are rated "thin" in `ARCHETYPE.md`, and the advisor uses them for risk awareness and probes, not proof. Synthesizers and verifiers correctly refused to inflate grades |
| 6 | Module count changes after the landscape (8 became 10) | Planning should assume the landscape may add modules. Budget about 25% extra |
| 7 | The same document had different source keys across modules | Recorded, not yet unified. A later clean-up pass, or a shared key registry for each archetype |
| 8 | Method synthesis cited "the spec" | Removed in verification. Briefs for shipped files now say: no build references |

## Patterns in the evidence, useful for the product

- **Strong evidence** where AI is the tool doing the work: testing, document matching, SOC preparation.
- **Thin evidence** where the topic is governance, structure, or auditing AI itself.
- **No independent measure of AI quality** in any assurance module. Every outcome figure is self-reported or vendor-published. The advisor must say so when quoting one. The method files already instruct this.

## Decisions for waves 2 and 3

1. **Keep the recipe and the model split:** research on Sonnet, synthesis and verification on Opus.
2. **Revised estimate per archetype:** about 50–60 agents and about 20–25M tokens, allowing for module growth.
   - Remaining work: tax, professional services, stream B (about 15 agents, about 5M).
   - **That totals about 50M tokens.**
   - **Full build including the pilot and wave 1: about 75M tokens**, up from the earlier estimate of about 50M.
3. **Run the landscape scan alone first**, then the deep dives, so they don't compete for the search quota with every other agent.
4. **Assign private working folders** in every brief.
