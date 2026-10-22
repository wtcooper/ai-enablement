# Brief: enterprise AI tool landscape (research)

Placeholders: `{scope}`, `{products}`, `{output_path}`. Today is 2026-10-22.

**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are researching the **tool landscape** for an AI transformation plugin. The plugin helps leaders at
professional-services firms (audit, tax, advisory, legal, consulting) decide which kind of AI tool fits which job.
The result becomes a shared reference file, `library/tool-landscape.md`, that maps jobs to tool types (runtime
classes) and lists current products of each type as dated, sourced examples. These are never endorsements.

- **Scope:** {scope}
- **Products and claims to check:** {products}

Before you search, read:
- `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/library/index.md`.
  Note its runtime classes: personal-assistant, shared-team-skills, workflow-automation, background-agent and
  managed-agent-runtime.
- The access and precision rules in `/home/user/ai-enablement/research/briefs/templates/module-angle.md`
  (sections **Access** and **Precision rules**).

## What to establish for each product

The leads above come from an unverified secondary summary. **Treat every one of them as a claim to check, not a
fact.** For each product, find the vendor's own page, documentation, release notes or official blog post, and record:

1. **What it is** in one plain sentence, in the vendor's terms.
2. **The job it serves**, for example: ask questions of documents; produce an Office deliverable; delegate a
   multi-step task; an always-on agent that acts while the user is away; a departmental bot on business systems; a
   coding agent working locally or in the cloud; a production agent on private data; a gateway or tool-access control.
3. **Runtime class**, from the five above, or say none fits and why.
4. **The three deciding boundaries:**
   - **Identity:** does it act as the user, or with its own service identity?
   - **Data:** where must the data live, for example Microsoft 365 / Google Workspace content, uploaded files,
     code repositories, or a private cloud network?
   - **Persistence:** in-session, or asynchronous and always-on?
5. **Status and date:** generally available, public preview, private preview, beta or announced, with the date of the
   source that says so.
6. **Enterprise controls that matter to a firm handling confidential client data:** admin enablement, data
   retention and training terms, audit logs. Report only what the source states.
7. **Pricing model** only if the vendor states it (per user, consumption or credits). No figures from third parties.

Then mark each lead **confirmed**, **partly confirmed** (say what differs), **not found** or **contradicted**, with
the source. Do not repeat an unconfirmed claim as fact anywhere in your output. Rule of thumb: a product name, a
rename, a launch date or a feature can go into the final file only if a vendor page or a reputable named outlet states
it.

## Rules

- **Public sources only.** Prefer vendor documentation and official announcements. Then use reputable trade press
  (The Verge, TechCrunch, Ars Technica, ZDNet, InfoWorld, The Register) with named authors and dates.
- **Keep the source's modal verbs and tense** ("announced", "in preview", "generally available").
- **Quotations under 25 words.**
- **No recommendations.** Describe, don't rank. Note where vendors overlap.
- **Web search is rationed and shared.** Go straight to vendor docs and blogs with `curl`, and use the `r.jina.ai`
  mirror for pages that need JavaScript.

## Output

Write `{output_path}` with these sections:

1. **Summary:** 5-8 bullets.
2. **Products:** one block per product with fields 1-7 and source refs.
3. **Lead check:** a table of each claim, verdict, source and note.
4. **How a firm would choose:** the questions that separate the products in your scope, and the job each one wins,
   with sources. Include when work should graduate from a personal or coding tool to a shared or production platform.
5. **Gaps:** what you couldn't reach or confirm.
6. **Sources:** ref (`VENDOR-SHORT-YYYY`), title, publisher, type, URL, date, access.

Reply with no more than 120 words: the counts of leads confirmed, partly confirmed, not found and contradicted, and
the two most important findings.
