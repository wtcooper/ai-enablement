# Brief: write the tool landscape (synthesis)

Today is 2026-10-22. You are writing `library/tool-landscape.md` for the plugin at
`/home/user/ai-enablement/plugins/ai-transformation/`, under `skills/transformation-advisor/references/`.
Every skill in the suite reads it:
- the advisor, when it reimagines work and proposes a runtime class;
- ai-solution-delivery, at build or buy;
- ai-enablement, for a staff tool guide;
- ai-governance, for the approved-tool catalog.

## Owner decision (2026-10-22)

The knowledge of "which tool for which job" lives in two places:

1. **Shared and generic:** `library/tool-landscape.md`, the file you write. It maps jobs to tool types (runtime
   classes), gives the questions that decide between them and the path from prototype to production, and has a
   dated table of current products per type, sourced from public vendor pages. Products are examples, never
   endorsements.
2. **The firm's own:** `overlay/tool-catalog.yaml`, the tools the firm has approved, each with a `use_for` field.
   ai-governance writes it. When it exists, it always wins over the landscape.

Core rule 6 will read: "If `overlay/tool-catalog.yaml` exists, recommend tools from it and flag anything outside it.
Otherwise recommend a runtime class, and name current products only as dated examples from
`../transformation-advisor/references/library/tool-landscape.md`, never as endorsements."

## Read first

- `research/runs/tools/suites-microsoft-google.md`, `assistants-coding.md` and `platforms-infra.md`: the three
  research files. Use only their **confirmed** or **partly confirmed** findings, with the stated difference. Leave out
  anything marked not found or contradicted.
- `skills/transformation-advisor/references/library/index.md` (the runtime classes) and two pattern files in
  `library/patterns/`, for house style.
- `skills/transformation-advisor/references/schemas/vocabulary.yaml`.

## Contents of the file (at most 300 lines; contents list; plain, short sentences)

1. **How to use this file:** the overlay catalog wins, products are dated examples, and statuses change monthly, so
   check the vendor page before relying on one.
2. **Jobs to tool types.** A table with columns: job (in a practitioner's words, for example "ask questions of a
   team's documents", "produce an Office deliverable end to end", "delegate a multi-step task", "an agent that keeps
   working while you're away", "a departmental bot on business systems", "analyse a large document set", "write or
   change code", "a production agent on private data", "control which models and tools agents may use"), tool type,
   runtime class, and what to check. Use the existing five runtime classes. If a job needs a class that doesn't exist
   (for example coding agents, or SaaS-embedded agents), map it to the nearest class and add a note. Propose any new
   vocabulary in your report; don't add it to `vocabulary.yaml`.
3. **The deciding questions:**
   - Identity: does it act as the user or with its own identity?
   - Data: where does the data live?
   - Persistence: in-session or always-on?
   - Who builds and maintains it?
   - Which data classes may go in? Defer to the overlay policy.
   - Cost model: per user or consumption.

   For each question, give one line on what each answer implies.
4. **From prototype to production:** how work moves from a personal tool or coding agent, to a shared skill or
   department agent, to a production platform. What triggers each move (more users, own identity, private data,
   always-on, audit needs), and what ai-solution-delivery's readiness check needs at each step.
5. **Current products by type, as of October 2026.** Grouped by tool type: product, vendor, job it serves, status
   (GA, preview or beta) with date, and source ref. Keep the vendor's own names. Include the Office suites
   (Microsoft 365 Copilot family, Gemini for Workspace), standalone assistants (ChatGPT Enterprise, Claude
   Enterprise), coding agents, pro-code platforms, gateways and MCP/skills infrastructure, and SaaS-embedded agents.
6. **Notes for professional-services firms:**
   - client-data rules and the overlay policy;
   - independence and confidentiality questions to ask a vendor;
   - field-specific tools (audit, tax, legal) live in the archetypes' use cases, not here;
   - the public examples, if any, of firms building on these platforms (from the research).
7. **Refresh:** what to recheck and how often. Keep the date in the file's header.
8. **Sources:** `VENDOR-SHORT-YYYY` keys with title, publisher, type, URL, date and access.

## Also edit

- `library/index.md`: add one row or line pointing to `tool-landscape.md`, in the existing style.

Don't edit other files. Don't commit.

## Report

Write `research/runs/tools/synthesis-report.md` with:
- the leads you excluded, and why;
- any proposed vocabulary;
- the gaps.

Reply in no more than 100 words.
