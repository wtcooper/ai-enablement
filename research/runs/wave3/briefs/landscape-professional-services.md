**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are a research analyst building the **source landscape** for one business archetype. Your output
will steer many later deep-dive researchers, so breadth and accuracy matter more than prose. Today is
2026-10-19.

**Archetype:** professional-services: Professional services: how advisory and professional firms run their business and deliver client work, across the client lifecycle. Covers management and strategy consulting, technology consulting and systems integrators, accounting and advisory firms (the firm-operations side, not audit or tax technical work), law firms and legal operations, and engineering, architecture and other project-based advisory firms, plus in-house shared-service teams that work like firms. This is the base archetype that assurance and tax extend, and the one consulting teams use. Focus on AI changing how firms win, price, staff, deliver, review, bill and reuse knowledge, and on how the business model (leverage pyramid, billable hour, utilization) responds.
**Proposed modules:** pursuit-proposals (business development, RFP responses, proposals, pitches) · acceptance-risk (client and engagement acceptance, conflicts, risk and ethics checks) · scoping-pricing (estimating, scoping, pricing models, fee proposals) · staffing-resourcing (matching people to work, capacity planning, utilization) · delivery-management (project management, status, client reporting, deliverable production) · quality-review (review of deliverables, quality and risk management, professional standards) · billing-collections (time capture, invoicing, write-offs, collections, realization) · knowledge-management (precedents, methods, expertise location, reuse). Check against how practitioners divide firm operations (Thomson Reuters, SPI Research, Source Global Research, ALM, the Legal Operations community CLOC, consulting associations) and say whether client relationship and account management, talent and learning, firm finance and performance, or consulting delivery itself deserve modules.

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

Write a markdown file to `/home/user/ai-enablement/research/runs/wave3/landscape-professional-services.md` with these sections:

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

- Conferences to cover include: Source Global Research and Consultancy.uk events, MCA and Management Consultancies Association, ACG and AMCF, Thomson Reuters Institute events (Legal Executive Institute, Tax and Accounting), CLOC Global Institute, Legalweek, ILTACON, Legal Geek, AICPA ENGAGE (firm management tracks), Accounting Today and CPA.com events, PMI Global Summit, Kantata and other PSA user conferences, Gartner and Forrester services events.
- Firms to cover: McKinsey (Lilli), BCG, Bain, Accenture, Deloitte, PwC, EY, KPMG, mid-tier consultancies, law firms (Allen & Overy Shearman / A&O Shearman, Clifford Chance, Latham), legal AI vendors (Harvey, Legora), PSA and proposal vendors (Kantata, Certinia, Loopio, Responsive), and AI-native consultancies.
- Public sources only; no client-confidential information.
