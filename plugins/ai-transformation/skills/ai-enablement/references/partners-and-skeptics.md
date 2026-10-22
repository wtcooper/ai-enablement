# Bring partners and skeptics along (step 6)

Read this on entering step 6, and whenever a partner, senior expert or skeptic pushes back. In a partnership the
people whose behaviour must change co-own the firm, so the program leads by influence more than authority.

**The method lives in the core skill.** Read `../../transformation-advisor/references/method/leading-partners.md` now:
partner economics (§2), the stakeholder map and its columns (§3), the partner briefing (§4), objections with
graded answers (§5), leader expectations (§6), more questions (§8) and traps (§9), with their sources (§12). This
file says how step 6 applies it to an enablement program and what it writes. Source keys in brackets are in §5.

## 1. Goal and exit criteria

**Goal.** The people others watch use AI on real work, state what they expect, and have their real concerns answered
with evidence or a test.

**Exit when all of these are true:** a stakeholder map by role and group (formal power, informal influence, economic
exposure, stance and its basis, the ADKAR gap, who they listen to, the ask); an objection log (§3); a partner briefing
outline for each partner segment; a senior modelling plan (which senior roles will use the tools visibly, on what, in
which forum); leader expectations in writing, with only the consequences the firm will actually apply; role
communication in the firm's own terms, consistent with step 2's statement on time saved.

## 2. How to run it

Core questions, one at a time: "Who else has to say yes, and who can say no without being asked?" (by role). "What
exactly does the skeptic worry about: accuracy, confidentiality, clients, craft, status, job security?" "Which tasks
would they gladly hand off?" "What result would change their mind?" "What will the most senior leaders state publicly,
and will they demonstrate it?"

1. **Map the constellation, not the org chart**, and segment partners by exposure and horizon (leading-partners §3).
2. **Collect objections** in the user's words and log each (§3).
3. **Answer with evidence or a test.** Open the matched archetype's `objections.md` and quote its figures with who
   measured them, and grades exactly as recorded.
4. **Draft the briefing** around a workflow from this firm with a baseline (leading-partners §4), using step 1's
   segments and step 7's measures where they exist.
5. **Write expectations and the modelling plan** with the user, and check them against step 2.
6. **Play back and save.** If the user fears for their own role, switch to
   `../../transformation-advisor/references/method/people-and-change.md` §8 first.

**Rule 11 in practice.** If the user names a partner, keep the name out of the file and do not recommend actions about
that person; offer the group-level move ("for skeptical audit partners who doubt accuracy: an expert-graded test on
their own files") and let the user decide how to apply it.

## 3. The objection log

Columns: objection | type | honest answer and evidence (grade or provenance) | test | owner | result. Objections files:
`../../transformation-advisor/references/archetypes/professional-services/objections.md`, and the same file under
`assurance/`, `tax/` and `security/`.

| Type | Example | What usually answers it |
|---|---|---|
| Risk | "It makes things up" | Concede the documented failure, then show the control and an expert-graded test (leading-partners §5) |
| Time | "I have no hours for this" | The credit rule from step 2; private, short practice |
| Identity | "This is not how good work is done" | Their judgment as the scarce input; ask which tasks they would hand off |
| Incentive | "This kills our billings" | The four variables and three scenarios (leading-partners §2); change the incentive or say it will not change |
| Trust | "Leadership will use this to cut us" | Honest role communication (`people-and-change.md` §7); never false reassurance |

Treat each objection as a hypothesis about a missing condition (time, trust, proof, incentive). Agree before the test
what result would change the skeptic's mind, and record the result.

## 4. What is specific to enablement

- **Ask which tasks they would hand off, not whether they like AI.** Workers were positive about AI agent automation
  for 46.1% of tasks in a Stanford study of 1,500 US workers across 104 occupations [STANFORD-WORKBANK-2025].
- **Offer an expert-graded evaluation before asking for use** on high-judgment work: Morgan Stanley describes advisors
  grading AI summaries for accuracy (vendor-published) [OPENAI-MSTANLEY-ND]. It gives skeptics a say.
- **Combine peer demonstration with a stated expectation.** Firms report using one or the other
  [HARVEY-CHAMPIONS-2026; CPAPA-PWC-2026]; no source compares them (working rule).
- **Resolve shared objections once:** if three or more groups raise the same one, settle it at firm level (incentive,
  policy or client position) (working rule).
- **Check that incentives do not reward visible use over quality:** 40% of 1,150 US desk workers had received
  AI-generated "workslop" in the past month, about two hours to resolve each [BETTERUP-2025].
- **Route senior people into step 4's forums** that suit them: private office hours, a peer pairing, or a showcase
  where juniors present to partners.

*Illustrative (invented).* Audit partners, mapped by group: the senior pair (supportive, rarely use it); two practice
heads (one open, one skeptical on accuracy); leverage-dependent partners (worried about junior hours). Answers: the
assurance objections file; a test on six closed engagement files graded by the skeptical practice head. When the user
asks about one named partner, the skill keeps it at group level and offers the private-session format.

**Output:** `program.md` section 6 (stakeholder map, objection log, briefing outlines, modelling plan, written
expectations, role communication); a measure in `measures.yaml` if an objection needs a measured answer (for example,
the error rate the checkpoint finds on a sample); frontmatter `step_completed: 6`, `next_step: 7`, `updated`.

## 5. Sources

- `BETTERUP-2025`: *Workslop: The Hidden Cost of AI-Generated Busywork*, BetterUp Labs with Stanford Social Media Lab, September 2025. https://www.betterup.com/workslop
- `CPAPA-PWC-2026`: *PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'*, CPA Practice Advisor citing the Financial Times, 2026-03-25. https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
- `HARVEY-CHAMPIONS-2026`: *Harvey Power Users: The Champions Network*, Harvey blog, vendor-published, 2026-06-02. https://www.harvey.ai/blog/harvey-power-users-the-champions-network
- `OPENAI-MSTANLEY-ND`: *Morgan Stanley uses AI evals to shape the future of financial services*, OpenAI, vendor case study, undated. https://openai.com/index/morgan-stanley/
- `STANFORD-WORKBANK-2025`: *Future of Work with AI Agents*, Shao et al., arXiv 2506.06576, June 2025. https://arxiv.org/pdf/2506.06576
