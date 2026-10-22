# Synthesis report: tool landscape

Date: 2026-10-22. Output: `plugins/ai-transformation/skills/transformation-advisor/references/library/tool-landscape.md`
(300 lines, 66 sources) and one paragraph in `library/index.md` §4 pointing to it. No other files edited. Not
committed.

## 1. Leads excluded, and why

**Not found or contradicted (left out as claims; the corrected fact is used where the research states it):**
- "Copilot Agent Kit": not found. The "Copilot Studio Kit" result was search-only.
- Claude Managed Agents "launched September 2026": contradicted. The file uses the stated public-beta date,
  2026-04-08, and the current beta label.
- Agent Skills "published as an open standard in 2026": contradicted. The file uses 2025-12-18.
- Imagen 4: contradicted (shut down in the Gemini API). Image tools are out of scope for the file anyway.
- Professional-services firms on Bedrock or the Gemini Enterprise Agent Platform, and law firms on any platform:
  not found. The file says so instead of naming any.

**Partly confirmed or weakly sourced, left out:**
- Microsoft billing change "effective 2026-12-01": only two third-party reports, which disagree on the default cap.
  The file uses only Microsoft's stated split of per-user licence plus usage billing.
- Scout desktop identity: the Learn FAQ says it signs in with the user's credentials, while the blog says
  Autopilot has its own Entra identity. The file states the blog claim for Autopilot only.
- "Scout renamed on 2026-09-25": no effective date stated. The file says "previously Scout" only.
- Google Agent Engine renamed Agent Runtime: inferred from absence of the old name. The file uses "Agent Runtime"
  as the current name without claiming a rename.
- Salesforce Agentforce identity modes (search snippet only) and ServiceNow identity modes (community post).
  The file says only that embedded agents inherit the system's permissions.
- MCP governance moving to the AAIF: a blogger's statement.
- Thomson Reuters CoCounsel and a PwC AgentCore page: search-only or 404.
- Gemini model names (3.1 Flash, 3.5 Flash, 3.1 Pro), GPT-6.x and Claude model releases: model news, not tool
  types. They change fastest and were left out to keep the file about tool types.
- Work IQ APIs: GA was announced for 2026-06-16, but no confirmation that it happened was read.
- "Four-level permission ladder" for dots: partly confirmed, wording differs between sources. Left out for space.

**Confirmed but left out for length (300-line limit):** TrueFoundry and Bifrost gateways, ChatGPT Deep Research,
Google ADK and Strands as separate rows, Scout desktop admin controls, GitHub local sandboxing GA (2026-10-07) and
Copilot computer use preview (2026-10-01), Cursor privacy and residency details, vendor prices other than the
pricing model. All remain in the three research files.

## 2. Proposed vocabulary (not added to `vocabulary.yaml`)

1. **A tool-layer field beside `runtime_class`**, for things that are not runtimes:
   `tool_layer: [runtime, gateway, agent-identity, registry, protocol, skill-format, framework, app-hosting]`.
   Gateways, Agent 365, Entra Agent ID, MCP, Agent Skills, ADK and Copilot Managed Runtime currently map to "none"
   or to the nearest class in notes 4 and 5 of the file.
2. **An identity field**: `acts_as: [user, maker, agent-identity, service-account]`. Identity is the first
   deciding question and drives audit and approval design, but no controlled value records it today.
3. **Optionally, two runtime classes** if the suite wants finer mapping:
   - `delegated-task-agent`: a personal agent that runs asynchronously as the user (Copilot Cowork, ChatGPT Work,
     Claude Cowork). Today it sits between `personal-assistant` and `background-agent`.
   - `saas-embedded-agent`: an agent inside a vendor's system of record (Agentforce, ServiceNow AI Agents).
     Today it maps to `managed-agent-runtime`.
   Coding agents do not need a class of their own; local, cloud and shared-skill use map cleanly to existing
   classes.
4. The brief names a catalog field `use_for`. The current `tool-catalog/v1` schema has `approved_for` and no
   `use_for`. The landscape file refers to `use_for` as the owner decision states. ai-governance's schema needs
   the field added, or the landscape should say `approved_for`.

## 3. Gaps

- No independent quality evidence (error, override or parallel-run rates) exists for any product in the research.
  The file describes features and stated controls only.
- Several key pages are undated (most Microsoft Learn, OpenAI help, gateway and Anthropic product pages). Their
  statuses rest on the access date.
- Not read: Copilot Code admin and audit pages; current Cowork DLP status; Google Workspace audit, Vault and
  eDiscovery behaviour for Gemini; Google training terms for the Agent Platform; Foundry audit-log specifics;
  Claude Enterprise admin controls for Cowork and computer use on Enterprise; whether OpenAI's Compliance API
  covers dots, Work and Codex records; Glean retention and training terms.
- Pricing figures for Agent 365, Gemini Enterprise, Claude Enterprise seats, Cursor Enterprise and the gateways
  were not captured. The file gives pricing models only.
- Google has no equivalent named for "always-on agent" or "governed app hosting" in the sources read.
- Professional-services evidence is two self-reported Big Four announcements on Microsoft Foundry. No mid-size firm
  or law firm example was found.
- Independence questions in §6 of the file are marked *(guidance)*. No source in the research addresses
  independence for AI vendors directly; ai-governance's `professional-duties.md` should be the authority.
