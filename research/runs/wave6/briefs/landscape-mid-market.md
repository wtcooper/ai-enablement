**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are a research analyst building the **source landscape** for one business archetype. Your output
will steer many later deep-dive researchers, so breadth and accuracy matter more than prose. Today is
2026-10-20.

**Archetype:** mid-market extensions to the existing **assurance** and **tax** archetypes. The current archetypes lean toward large firms and public companies. Research how AI changes assurance and tax work at accounting firms serving private, middle-market companies, owners and families: smaller-entity audits, reviews and compilations, employee benefit plan audits, nonprofit and single audits, pass-through and owner taxation, trusts and estates, and state and local tax for multi-state private companies. Read the existing module lists first: `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/ARCHETYPE.md` and `.../tax/ARCHETYPE.md`. The goal is to add a few new modules (or widen existing ones) without duplicating them.
**Proposed modules:** assurance: private-company-audit (smaller-entity audits under AICPA standards, risk assessment and documentation at small scale, peer review findings) · reviews-compilations (SSARS engagements, preparation of financial statements) · benefit-plan-audits (ERISA employee benefit plan audits, DOL focus) · nonprofit-government (nonprofit audits, single audits under Uniform Guidance, Yellow Book). Tax: pass-through-owners (S corporations, partnerships, owner compensation and basis, entity choice for private companies) · trusts-estates-gifts (fiduciary returns, gift and estate planning compliance) · nonprofit-tax (Form 990, unrelated business income) · multistate-private (state and local income, sales and payroll nexus for growing private companies). Check against how practitioners divide the work (AICPA PCPS, the AICPA Employee Benefit Plan Audit Quality Center, the Governmental Audit Quality Center, peer review results, NSA, NATP, state CPA societies, INSIDE Public Accounting and Accounting Today service-line data) and say which deserve modules, which merge, and which existing modules already cover them.

## What to find

Use web search, and open the pages themselves (see the access note below); don't rely on search
snippets alone. The pilot's scan ran on snippets only and needed corrections.

**Access:** the web-fetch tool can fail on DNS in this environment. Use
`curl -sSL --max-time 30 -A "Mozilla/5.0" <url>` through Bash, and `pdftotext` for PDFs.

Use web search and fetch extensively. Aim to read **at least 40 distinct sources** across at least
**6 source types**. Prefer material from the last 12–18 months. For each item, record its name, the
organizer or publisher, a URL, the date or edition, and one line on why it matters for AI in this
field.

1. **Conferences and events (most important).** The main conferences, symposia and summits in this
   field, plus relevant technology-in-the-field events.
   - Cover the 2025 and 2026 editions.
   - Record AI-related **sessions, tracks, keynotes and panels**: titles, and the organizations of the
     speakers where available.
   - Include proceedings, slide decks, session recordings and recaps if they are public.
2. **Regulators and standard-setters:** statements, staff guidance, spotlights, inspection
   observations, consultations and standard changes that touch technology or AI.
3. **Professional bodies:** guidance, toolkits, surveys and reports on AI.
4. **Academic work:** the main journals and research centers, and notable papers and working papers on
   AI in this field from 2024–2026.
5. **Firms:** large and mid-tier firms' public AI platforms, announcements, reports and case studies.
   Include in-house teams where relevant.
6. **Vendors:** the main technology vendors and recent AI product launches for this field.
7. **Trade press, newsletters, podcasts and practitioner communities.**
8. **Surveys and benchmarks** of AI adoption in this field.

## Also produce

- **Evidence density per module:** high, medium or low, judged by how much specific public material
  exists. Low-density modules get one combined deep dive instead of three.
- **Source keys.** Give every source a ref in the form `PUBLISHER-SHORT-YYYY`. Later researchers reuse
  these refs.
- **Module check.** Is the proposed module list right for how practitioners divide the work? Propose
  changes, with reasons.
- **Journey-stage markers.** For this field, what does each stage look like in practice: Curious,
  Experimenting, Adopting, Scaling, AI-native? Give two or three observable markers per stage.
- **Ten or more frontier signals.** Dated, sourced signals of where AI in this field is heading in the
  next 12–36 months: agentic uses, regulatory moves, business-model shifts.
- **Research leads per module.** For each module, the five or more most promising sources or search
  directions for later deep dives.
- **Gaps.** What you couldn't reach (blocked or paywalled) and what seems under-documented.

## Rules

- Do not invent sources, sessions, speakers or dates. If you can't confirm something, mark it
  `(unverified)` or leave it out.
- Summarize in your own words. Quotations must be under 25 words.
- Public sources only.

## Output

Write a markdown file to `/home/user/ai-enablement/research/runs/wave6/landscape-mid-market.md` with these sections:

1. Summary
2. Conferences & events
3. Regulators & standard-setters
4. Professional bodies
5. Academic
6. Firms
7. Vendors
8. Press, podcasts & communities
9. Surveys & benchmarks
10. Module check
11. Journey-stage markers
12. Frontier signals
13. Research leads per module
14. Gaps
15. Source count by type

Then reply with a summary of **no more than 200 words**: the source count by type, the three most
valuable finds, and the main gaps.


## Notes for this field

- Conferences to cover include: AICPA ENGAGE (A&A, tax and firm tracks), AICPA Employee Benefit Plans Conference, AICPA Governmental and Not-for-Profit conferences, AICPA Peer Review conference, state CPA society tax and A&A conferences, NATP and NSA events, Thomson Reuters SYNERGY, CCH and Intuit ProConnect partner events, Accounting Today Growth & Profitability.
- Firms to cover: top-100 and regional firms with large private-company, benefit-plan, nonprofit and tax practices; PE-backed platforms; vendors serving small and mid-sized firms (engagement, audit, tax prep and workflow tools) and AI-native entrants.
- Regulators and standard-setters: AICPA ASB and ARSC, AICPA peer review (including findings on AI), DOL EBSA, GAO Yellow Book, IRS (including Circular 230 and section 7216), state boards.
- Public sources only; no client-confidential information.
