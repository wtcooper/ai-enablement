# Platforms and infrastructure: production-agent platforms, AI/MCP gateways, MCP, Agent Skills, SaaS-embedded agents

Research date: 2026-10-22. Public sources only. Every product name, rename, date and feature below is stated by the cited vendor page or named outlet. Pages marked "undated" showed no publication date; they are recorded with the access date 2026-10-22. These are dated, sourced examples, not endorsements.

## 1. Summary

- Two of the three hyperscaler names in the brief have changed. "Azure AI Foundry" is now **Microsoft Foundry** (Microsoft's docs list the old names as "previous"). "Vertex AI Agent Builder" now sits inside the **Gemini Enterprise Agent Platform**, which Google described as an evolution of Vertex AI and The Register reported on 2026-04-22. Product names in the library should use the current names and note the old ones.
- All three hyperscaler platforms (Microsoft Foundry Agent Service, Gemini Enterprise Agent Platform, Amazon Bedrock AgentCore) offer the same building blocks: a managed agent runtime, a per-agent identity, a tool gateway with MCP, a registry, and evaluation and tracing. They differ on where identity comes from (Entra, Google IAM/SPIFFE, AWS plus any IdP) and where data sits (your Azure, Google Cloud or AWS tenant).
- The "Elastic Runtime" lead is only partly right. AWS published "The new AgentCore runtime: Elastic, optimized, and consistently fast starts" on 2026-09-18, but the post does not name a product "Elastic Runtime". It describes a new AgentCore runtime with on-demand memory and consumption billing.
- The Agent Skills lead is wrong on the year. Anthropic's own page says it published Agent Skills as an open standard on **2025-12-18**, not 2026. A skill is a folder with a `SKILL.md` of instructions; MCP is a protocol that connects an AI application to tools and data. They do different jobs and are used together.
- An MCP server is a program that provides context (tools, resources, prompts) to an MCP client. A registry is a catalog of such servers. The official MCP Registry is a public catalog in preview and does not take private servers. Several vendors sell private registries inside their gateways (TrueFoundry, Kong in tech preview, Glean, AgentCore Registry, Google Agent Registry).
- AI and MCP gateways (LiteLLM, TrueFoundry, Bifrost, Kong, Portkey inside Palo Alto Networks Prisma AIRS) sit between agents and models or tools. They are infrastructure controls, not a runtime class. LiteLLM Lens launched on 2026-10-01 and its docs label it early access. Palo Alto Networks announced the Portkey deal on 2026-04-30 and completed it on 2026-05-29.
- SaaS-embedded agents (Salesforce Agentforce, ServiceNow AI Agents, Glean) run inside the vendor's system of record and inherit its permission model. Both Salesforce and ServiceNow document a choice between acting as the invoking user and acting as a dedicated agent user.
- For professional services: EY (2026-04-07) and KPMG (2025-06-18) named Microsoft Foundry or Azure AI Foundry as the base of their audit and firm-wide agent platforms. I found no verifiable public example of a law, tax or accounting firm building on Bedrock or Vertex/Gemini Enterprise Agent Platform, and none for a law firm on any of the three.

## 2. Products

Runtime classes follow `library/index.md`: personal-assistant, shared-team-skills, workflow-automation, background-agent, managed-agent-runtime.

### 2.1 Microsoft Foundry (formerly Azure AI Foundry)

**Foundry Agent Service**
1. **What it is:** "A managed platform for building, deploying, and scaling AI agents" with prompt agents, voice-based prompt agents and hosted (code-based) agents (MSFT-FOUNDRY-AGENTS-2026).
2. **Job:** a production agent on private data; hosted agents suit an agent that calls the firm's own code; prompt agents suit internal tools without custom orchestration.
3. **Runtime class:** managed-agent-runtime.
4. **Boundaries:**
   - Identity: each hosted agent gets "a dedicated Microsoft Entra identity"; prompt agents also show an Entra agent identity. Calling the Responses API supports On-Behalf-Of authentication, so an agent can act as the user (MSFT-FOUNDRY-AGENTS-2026).
   - Data: bring your own Azure resources (storage, Azure AI Search, Cosmos DB), virtual network isolation and data-residency controls. Stored agent data sits in the Azure OpenAI resource in the customer's tenant, in the same geography (MSFT-FOUNDRY-PRIVACY-2025).
   - Persistence: hosted agents have "session-level state persistence" and run as managed containers; ephemeral agents can be defined in your own code via the Responses API (MSFT-FOUNDRY-AGENTS-2026).
5. **Status and date:** the overview page (updated 2026-10-15; `ms.date` 2026-09-25) does not label the service as a whole as preview. It flags as preview: voice-based agents and related monitoring/evaluation capabilities, and the agent optimizer. It says A2A v1.0 is generally available and v0.3 remains in preview (MSFT-FOUNDRY-AGENTS-2026). Toolbox features such as skills and tool search are labelled preview (MSFT-FOUNDRY-TOOLBOX-2026).
6. **Enterprise controls:** Microsoft states prompts and completions "are NOT available to other customers" and are not used to improve OpenAI, Meta, Cohere or Mistral models; stored data can be encrypted with a customer-managed key, "except preview features may not support customer managed keys" (MSFT-FOUNDRY-PRIVACY-2025, page dated 2025-11-19). Guardrails include cross-prompt injection (XPIA) mitigation. I did not find an audit-log statement on these pages beyond tracing and Application Insights.
7. **Pricing model:** per-call inference and tool usage; hosted agents add container compute; voice uses Voice Live and model usage (MSFT-FOUNDRY-AGENTS-2026).

**Entra Agent ID**
1. **What it is:** "Identity accounts within Microsoft Entra ID" that give AI agents unique identification and authentication (MSFT-ENTRA-AGENTID-2026).
2. **Job:** a gateway or tool-access control, specifically agent identity.
3. **Runtime class:** none fits; it is an identity layer that any of the runtimes can use.
4. **Boundaries:** Identity: both modes are documented. Autonomous access uses rights given to the agent identity; delegated access acts "on behalf of human users" with rights the user controls. Data and persistence: not applicable.
5. **Status:** the page (`updated_at` 2026-06-15) says Agent ID "is available for all Microsoft Entra customers" without a preview label (MSFT-ENTRA-AGENTID-2026).
6. **Controls:** the page says extending Entra security features to agents requires Microsoft Agent 365, included in Microsoft 365 E7 and an add-on to some other plans.
7. **Pricing model:** Agent 365 "requires a Microsoft Agent 365 license for each user" (per user), per the same page.

**Connectors (tools and MCP)**
1. **What it is:** Toolbox: a curated set of tools defined once and exposed through "a single MCP-compatible endpoint" with central credentials, governance and versioning (MSFT-FOUNDRY-TOOLBOX-2026, `ms.date` 2026-07-28). Agents can also add remote MCP servers using a project connection and can require approval of tool calls (MSFT-FOUNDRY-MCP-2026, `ms.date` 2026-08-26). Data sources named for Agent Service include Bing Search, SharePoint, Fabric and Azure Blob storage; actions include Logic Apps, Functions and OpenAPI tools (MSFT-FOUNDRY-PRIVACY-2025).
2. to 7. As for Agent Service. Skills and tool search in Toolbox are preview.

**Evaluation tools**
1. **What it is:** Evaluation of quality, safety and reliability: built-in evaluators (coherence, fluency, groundedness, relevance, safety), evaluation of production traces, simulation, and CI/CD quality gates (MSFT-FOUNDRY-OBS-2026, `ms.date` 2026-10-15). The overview adds an agent optimizer (preview).
2. **Job:** test and monitor a production agent.
3. **Runtime class:** none fits; a quality layer for managed-agent-runtime.

**Rename (lead check):** the "What is Foundry" page (`ms.date` 2026-08-13) lists "Azure AI Studio / Azure AI Foundry" as the previous brand and "Microsoft Foundry" as current; "Azure AI Services" became "Foundry Tools" (MSFT-FOUNDRY-WHAT-2026).

### 2.2 Google: Gemini Enterprise Agent Platform (formerly Vertex AI Agent Builder)

1. **What it is:** "A unified platform to build, deploy, govern, and optimize enterprise-grade AI agents", described as "an evolution of Vertex AI" (GOOG-AGENTPLATFORM-2026, page updated 2026-10-21). The Register reported on 2026-04-22 that Google was rebranding and expanding Vertex AI into the Gemini Enterprise Agent Platform at Cloud Next (REG-GOOGLE-2026). The overview is organised as Build, Scale, Govern and Optimize.
2. **Job:** a production agent on private data (RAG Engine and Vector Search for private data), with a governance layer.
3. **Runtime class:** managed-agent-runtime.

**Agent Runtime (the former Agent Engine)**
- The current overview names "Agent Runtime" and describes sub-second cold starts and long-running agents, plus Sessions and Memory Bank for state across sessions (GOOG-AGENTPLATFORM-2026, GOOG-SCALE-2026). I did not find the string "Agent Engine" on the current Google pages I read, so the rename rests on the absence of the old name and on the ADK docs, which now say "Agent Runtime". Treat the exact rename and its date as not confirmed from a Google source.
- Data: agents run in your Google Cloud project. Persistence: stateful sessions, persistent memory, background and long-running agents.

**Agent Development Kit (ADK)**
- "The open-source agent development framework" for building, debugging and deploying agents, available in Python, TypeScript, Go, Java and Kotlin (GOOG-ADK-2026). The docs banner says ADK TypeScript 2.0 is generally available. It supports non-Google models and deployment to Agent Runtime, Cloud Run or GKE.
- Runtime class: not a runtime. It is a build framework; the agent it produces runs on a runtime.

**Agent Identity and Agent Gateway**
- Agent Identity: a per-agent identity based on SPIFFE, credentials bound by mTLS through Context-Aware Access, described as "a more secure principal than service accounts". For user-delegated flows, logs show both the user and the agent identity (GOOG-AGENTID-2026, updated 2026-10-21). Sandboxes access is labelled Preview on that page; the page does not label the feature itself.
- Agent Gateway: the "governance and security enforcement layer" for agent traffic to tools, MCP servers and other agents; by default all connections are blocked until an IAM policy allows them. It works with Agent Registry, which catalogs approved agents, tools and MCP servers. It is currently available for agents running on the Gemini Enterprise Agent Platform; GKE, Cloud Run and cross-cloud support is described as coming through an early preview (GOOG-GATEWAY-2026, updated 2026-10-21).
- Status: Google's pages do not label the gateway itself generally available.

**Model Armor**
- Runtime screening of prompts, responses and agent interactions for prompt injection, sensitive data leaks and harmful content; the product page says it offers a free tier (GOOG-MODELARMOR-2026, undated; a Security Summit banner dates the page near Nov 2026 events). Attached to Agent Gateway as a content filter (GOOG-GATEWAY-2026).

**Controls and pricing (all Google items):** audit logging through Cloud Logging and identity-labelled logs is stated; I did not find a Google statement on training terms in the pages read. Pricing model: not read from a vendor page (Model Armor free tier only).

### 2.3 Amazon Bedrock AgentCore and Strands Agents

**AgentCore**
1. **What it is:** "An agentic platform for building, deploying, and operating highly effective agents securely at scale using any framework and foundation model" (AWS-AGENTCORE-DOCS-2026). Services: Harness, Runtime, Memory, Gateway, Identity, Code Interpreter, Browser, Observability, Payments, Evaluations, Optimization, Policy and Registry.
2. **Job:** a production agent on private data; Gateway turns APIs and Lambda functions into MCP tools; Registry catalogs agents, MCP servers, tools and skills.
3. **Runtime class:** managed-agent-runtime.
4. **Boundaries:**
   - Identity: AgentCore Identity works with existing identity providers (Cognito, Okta, Entra ID, Auth0). AWS's 2026-09-18 post lists "scoped identity for unattended agents" as coming soon.
   - Data: agents run in the customer's AWS account; Runtime offers "true session isolation". The data-protection page applies the AWS shared-responsibility model and recommends CloudTrail logging.
   - Persistence: Runtime has "extended runtime support for asynchronous agents"; Memory holds short-term and long-term memory.
5. **Status and date:** generally available since 2025-10-13 (AWS blog by Swami Sivasubramanian, AWS-AGENTCORE-GA-2025). The AWS docs overview carries no preview labels for the services listed.
6. **Controls:** CloudTrail logging recommended; Policy intercepts every tool call before execution, using Cedar-compatible rules. I did not read a training-terms statement for AgentCore.
7. **Pricing model:** "You pay only for what you consume": consumption-based, scaling to zero (AWS-AGENTCORE-RUNTIME-2026).

**The "new AgentCore runtime" (lead check)**
- AWS ML blog, 2026-09-18, authors Evandro Franco and five others: "The new AgentCore runtime: Elastic, optimized, and consistently fast starts." It announces better memory management (reclaiming memory as a session releases it) and consistent cold starts; the post reports a P75 cold start of about 2 seconds in its own client-side test (5,000 cold invocations per agent). It lists committed baseline discounts, larger compute and storage, x86 support and scoped identity for unattended agents as coming soon (AWS-AGENTCORE-RUNTIME-2026).
- "Elastic Runtime" appears as an adjective in the title, not as a product name.

**Strands Agents**
- "The open source toolkit for production AI agents", in TypeScript and Python, with a harness, SDK, evals and sandbox projects. It has guides for deploying to AgentCore, Lambda, Fargate, EKS and other targets (STRANDS-HOME-2026, undated). AgentCore's docs list Strands among supported frameworks. Not a runtime; a framework.

### 2.4 Claude Managed Agents (platform comparison only)

A sibling agent covers the product. The comparison points below come from Anthropic's overview page (ANTHROPIC-CMA-2026, undated; beta header `managed-agents-2026-04-01`).
- It is a "pre-configured agent harness that runs in managed infrastructure", built from Agent, Environment, Session and Events. It targets long-running, asynchronous work and offers cron-style scheduled deployments.
- Where it differs from the hyperscaler platforms: it is model-specific (Claude) and offers an Anthropic-managed cloud sandbox or a self-hosted sandbox on the customer's infrastructure. The hyperscaler platforms offer many models and run in the customer's own cloud account.
- Status and controls: beta. Because sessions are stateful, Anthropic states Managed Agents is "not currently eligible" for Zero Data Retention or HIPAA BAA coverage; sessions and files can be deleted through the API.
- Runtime class: managed-agent-runtime.

### 2.5 Model Context Protocol (MCP)

1. **What it is:** "An open-source standard for connecting AI applications to external systems" (MCP-INTRO-2026; the docs show spec version 2026-07-28 as latest).
2. **What a server is:** "A program that provides context to MCP clients". A host (the AI application) runs one client per server connection. Servers can run locally over STDIO or remotely over Streamable HTTP; the spec's primitives are tools, resources and prompts (MCP-ARCH-2026).
3. **What a registry is:** the official MCP Registry is "the official centralized metadata repository for publicly accessible MCP servers", in preview, backed by Anthropic, GitHub, PulseMCP and Microsoft. It stores `server.json` metadata that points to packages or remote URLs. It "does not support private servers"; the docs advise hosting a private registry for those (MCP-REGISTRY-2026). Gateways and platforms above sell private registries.
4. **Runtime class:** none; a protocol. Identity, data and persistence depend on the host and the server.
5. **Governance note:** Simon Willison wrote on 2025-12-19 that the AAIF is "recently the new home of the MCP specification". This is a blogger's statement; I did not confirm it from the AAIF.

### 2.6 Agent Skills

1. **What it is:** "A lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows"; a skill is a folder containing a `SKILL.md` with `name` and `description` metadata plus instructions, and optionally scripts, references and assets (SKILLS-OVERVIEW-2026, SKILLS-SPEC-2026). The site states the format was "originally developed by Anthropic" and released as an open standard.
2. **Date:** Anthropic's skills announcement (originally 2025-10-16) carries an update dated 2025-12-18 saying it "published Agent Skills as an open standard for cross-platform portability" (ANTHROPIC-SKILLS-2025). Simon Willison covered it on 2025-12-19 (WILLISON-SKILLS-2025).
3. **How skills differ from MCP:** MCP connects an AI application to systems, data and tools through a client-server protocol. A skill is a set of instructions and resources the agent loads when relevant. The MCP docs themselves ship MCP-building guidance as skills (MCP-SKILLS-2026), and Claude Managed Agents, Foundry Toolbox and Glean all list skills next to MCP tools. A skill can tell an agent how to use an MCP server; it does not give the agent access.
4. **Runtime class:** shared-team-skills (packaged skills used the same way across a team).
5. **Controls:** none defined by the standard. The spec marks `allowed-tools` as experimental. Controls come from the client.

### 2.7 AI and MCP gateways

**LiteLLM**
1. **What it is:** the LiteLLM Proxy "provides an MCP Gateway that allows you to use a fixed endpoint for all MCP tools and control MCP access by Key, Team" (LITELLM-MCP-2026). The docs also list an Agent Gateway for A2A agents, and show "SOC 2 Type II" and "MIT license" in the footer.
2. **Job:** a gateway or tool-access control.
3. **Runtime class:** none fits; an infrastructure control layer.
4. **Boundaries:** Identity: permissions by key, team and organization; the docs list OAuth and on-behalf-of authentication pages. Data: self-hosted proxy in your environment (deployment docs); I did not read where logs are stored. Persistence: not a runtime.
5. **Status:** MCP Gateway documented as current (docs undated). Enterprise features (SSO/SAML, audit logs, spend tracking, guardrails) are described on the Enterprise page (LITELLM-ENT-2026).
6. **Pricing model:** not read.

**LiteLLM Lens**
- "Uses AI agents to analyze your agent traces and find recurring problems" and links each finding to the original traces; docs label it "Early access" (LITELLM-LENS-2026). The launch post, dated 2026-10-01, says "Today we're launching LiteLLM Lens" (LITELLM-LENS-LAUNCH-2026). A follow-up post on 2026-10-05 describes how it finds repeated failures; the v1.106.0 release notes dated 2026-10-18 mention a Rust Lens service (LITELLM-RELEASE-2026). Lens is observability for agent traces, not an agent runtime.

**TrueFoundry**
1. **What it is:** "Centralized MCP gateway for enterprise AI agents" with unified access, OAuth, observability and guardrails for MCP servers; also an AI gateway and a registry (TF-MCP-DOCS-2026, TF-MCP-2026; both undated).
2. **Job:** gateway or tool-access control.
3. **Runtime class:** none fits.
4. **Boundaries:** Identity: federates with Okta, Azure AD or any IdP and uses OAuth flows; role-based access with approval flows for MCP servers. Data: the homepage says "VPC | On-Prem | Air-Gapped" deployment. Persistence: not a runtime.
5. **Status:** not labelled; the MCP page shows a free start tier and a waitlist form.
6. **Controls:** "Full Audit Trail" and tracing of requests are stated.
7. **Pricing model:** the MCP page lists a free start tier with 30k tool calls a month; no other pricing read.

**Bifrost (Maxim AI)**
1. **What it is:** "A high-performance AI gateway" with one OpenAI-compatible API over 23+ providers; its MCP Gateway acts as an MCP client and optionally an MCP server (BIFROST-README-2026, BIFROST-MCP-2026). The repository's licence file is Apache 2.0.
2. **Job:** gateway or tool-access control.
3. **Runtime class:** none fits.
4. **Boundaries:** Identity: virtual keys; per-user OAuth and token exchange for MCP servers. Data: self-hosted; enterprise offers in-VPC deployment. Persistence: stateless by design.
5. **Status:** the docs show "Enterprise" features separately (OIDC/SCIM provisioning, audit logs, guardrails, virtual MCPs, in-VPC deployment). The README lists "MCP gateway" among enterprise capabilities while the open docs document MCP; I could not tell from the sources which edition holds which MCP features.
6. **Controls:** by default Bifrost does "NOT automatically execute tool calls"; auto-execution is opt-in (BIFROST-MCP-2026). Audit logs are an enterprise feature (BIFROST-ENT-2026).
7. **Pricing model:** not read.

**Kong AI Gateway**
1. **What it is:** "A high-performance control plane that secures, governs, and observes AI-native systems end to end" for LLM, MCP and A2A traffic (KONG-AIGW-2026).
2. **Job:** gateway or tool-access control.
3. **Runtime class:** none fits.
4. **Boundaries:** Identity: consumer and consumer-group ACLs for MCP tools, an AI MCP OAuth2 plugin. Data: gateway data plane runs where you deploy it (hybrid, db-less, Konnect-hosted options). Persistence: not a runtime.
5. **Status:** the AI MCP Proxy plugin is "only available as part of our AI Gateway Enterprise offering" and needs Kong Gateway 3.12; the MCP Registry in Konnect is labelled "tech preview" (KONG-MCPPLUGIN-2026, KONG-MCP-2026).
6. **Controls:** AI MCP audit logs and access controls for MCP tools are documented.
7. **Pricing model:** not read.

**Palo Alto Networks Prisma AIRS and Portkey**
1. **What it is:** Palo Alto Networks "closed the acquisition of Portkey, a pioneer in AI Gateways", and says Portkey is the core AI Gateway for Prisma AIRS, its AI security platform (PANW-CLOSE-2026).
2. **Job:** runtime inspection and governance of AI and agent traffic.
3. **Runtime class:** none fits.
4. **Boundaries:** the release says the combined offer will include agent identity security through Idira and observability through Chronosphere, worded as "will be able to deliver". Data and persistence: not stated.
5. **Status and date:** intent to acquire announced 2026-04-30 (PANW-ANNOUNCE-2026); completed 2026-05-29 (PANW-CLOSE-2026). The integration is described in future tense in both releases.
6. **Controls:** the April release mentions "audit logs" and centralized artifact management for models, agents and MCP servers.
7. **Pricing model:** not stated.

### 2.8 SaaS-embedded agents

**Glean (enterprise search with an MCP endpoint)**
1. **What it is:** Glean's docs describe a "Glean MCP server" that exposes Glean search, chat, document read, people and agents as tools to AI hosts, and a "Glean MCP Gateway" that proxies custom tools, connector tools and third-party MCP servers (GLEAN-MCP-2026, GLEAN-GATEWAY-2026; both updated around 2026-10).
2. **Job:** ask questions of company content; a governed tool endpoint for coding and chat hosts.
3. **Runtime class:** none fits cleanly. The search and MCP endpoint is a tool-access layer; Glean Agents sit nearer managed-agent-runtime inside Glean.
4. **Boundaries:** Identity: results are described as "permission-enforced"; access can be limited by department, role or data-sensitivity tier. Data: content stays in source systems, reached through 250+ connectors (the nav says "more than 250 connectors"). Persistence: in-session requests from hosts; agents are separate.
5. **Status:** documented as current; no preview label on the pages read.
6. **Controls:** Glean Protect+ policies apply to external MCP tool calls; an Insights dashboard shows who calls which tool. I did not read retention or training terms.
7. **Pricing model:** not stated on pages read.

**Salesforce Agentforce**
1. **What it is:** "The AI Agent Platform" from Salesforce (SF-AGENTFORCE-2026).
2. **Job:** a departmental agent on CRM and service data (service, sales, employee agents).
3. **Runtime class:** managed-agent-runtime, built into a business system.
4. **Boundaries:** Identity: a web search against Salesforce's help site returned text saying employee agents run as the logged-in user and customer-facing agents run as a dedicated agent user. I could not load the help page itself (search-only). Data: Salesforce data, with the Einstein Trust Layer between the org and LLMs.
5. **Status:** the product page is current; no preview label seen.
6. **Controls:** Salesforce's Agentforce privacy FAQ (June 2025) says "zero data retention" applies, so third-party LLM providers do not retain customer data or train on it (SF-PRIVACY-2025).
7. **Pricing model:** the pricing page says "consumption-based pricing, with Flex Credits or Conversations, or per-user licensing" (SF-PRICING-2026). The page's navigation lists an "Accounting, Tax, and Audit" and a "Legal" solution under Professional Services.

**ServiceNow AI Agents**
1. **What it is:** the product page says "Take action with autonomous AI agents that work for you"; the platform page frames an "Autonomous Workforce" of AI specialists "assigned to roles, with business context and permissions" (SN-AIAGENTS-2026). The Knowledge 2026 press release (event 2026-05-05 to 05-07) introduces ServiceNow Otto and a unified AI governance story (SN-K26-2026).
2. **Job:** a departmental agent on IT, HR, customer and security workflows in ServiceNow.
3. **Runtime class:** managed-agent-runtime, built into a business system.
4. **Boundaries:** Identity: a ServiceNow community article dated 2026-07-28 (author is a community member, not a vendor release) describes two modes: a Dynamic User that inherits the invoking user's permissions, and an AI User, "a dedicated, standalone machine identity" (SN-COMMUNITY-ID-2026). Treat as secondary. Data: ServiceNow instance data and ACLs. Persistence: workflow-driven.
5. **Status:** the product pages are current; I did not find a dated vendor release note giving general availability for each feature.
6. **Controls and pricing:** not read from a vendor page.

## 3. Lead check

| Claim | Verdict | Source | Note |
|---|---|---|---|
| "Azure AI Foundry" with Foundry Agent Service, Entra Agent ID, connectors, evaluation tools | Partly confirmed | MSFT-FOUNDRY-WHAT-2026, MSFT-FOUNDRY-AGENTS-2026, MSFT-ENTRA-AGENTID-2026 | All four components exist. The platform is now called Microsoft Foundry; "Azure AI Foundry" is listed as the previous brand. |
| "Vertex AI Agent Builder": Agent Engine, ADK, Agent Identity, Agent Gateway, Model Armor | Partly confirmed | GOOG-AGENTPLATFORM-2026, REG-GOOGLE-2026, GOOG-ADK-2026, GOOG-AGENTID-2026, GOOG-GATEWAY-2026, GOOG-MODELARMOR-2026 | Platform now called Gemini Enterprise Agent Platform (reported 2026-04-22). Current docs say "Agent Runtime"; Agent Engine not found on current Google pages. Agent Gateway is available for agents on the platform, with other environments in early preview. |
| AgentCore "Elastic Runtime" dated 2026-09-18 | Partly confirmed | AWS-AGENTCORE-RUNTIME-2026 | Date matches an AWS post titled "The new AgentCore runtime: Elastic, optimized..."; no product named "Elastic Runtime". |
| Strands Agents framework (AWS) | Confirmed | STRANDS-HOME-2026, AWS-AGENTCORE-DOCS-2026 | Open-source toolkit; supported by AgentCore. |
| agentskills.io published SKILL.md as an open standard in 2026 | Contradicted | ANTHROPIC-SKILLS-2025, WILLISON-SKILLS-2025 | Anthropic's update is dated 2025-12-18; the standard is not a 2026 publication. |
| LiteLLM is an MCP gateway | Confirmed | LITELLM-MCP-2026 | Fixed endpoint, access by key, team and organization. |
| "LiteLLM Lens" in early access from 2026-10-01 | Confirmed | LITELLM-LENS-2026, LITELLM-LENS-LAUNCH-2026 | Launch post dated 2026-10-01; docs label "Early access". |
| TrueFoundry offers an MCP gateway | Confirmed | TF-MCP-DOCS-2026 | Undated vendor docs. |
| Bifrost offers an MCP gateway | Confirmed | BIFROST-MCP-2026 | Open docs; enterprise edition split unclear. |
| Kong offers an MCP gateway | Confirmed | KONG-MCP-2026, KONG-MCPPLUGIN-2026 | AI MCP Proxy plugin is AI Gateway Enterprise only; MCP Registry is tech preview. |
| Prisma AIRS acquired Portkey in May 2026 | Confirmed | PANW-CLOSE-2026, PANW-ANNOUNCE-2026 | Announced 2026-04-30; completed 2026-05-29. |
| Glean as enterprise search with an MCP endpoint | Confirmed | GLEAN-MCP-2026, GLEAN-GATEWAY-2026 | Also an MCP gateway. |
| Public examples of accounting/tax firms on Microsoft Foundry | Confirmed | EY-AUDIT-2026, KPMG-WORKBENCH-2025 | EY (2026-04-07) and KPMG (2025-06-18). Details in section 6. |
| Examples of accounting/tax/legal firms on Bedrock | Not found | none | A search snippet pointed to a PwC AgentCore page, which returned 404 when fetched; I did not use it. |
| Examples of accounting/tax/legal firms on Vertex or Gemini Enterprise Agent Platform | Not found | none | Only a partner listing mentioning Deloitte appeared in search results; no detail. |
| Examples of law firms on any of the three platforms | Not found | none | Only an AWS reference architecture and platform comparisons. |

Counts: 9 confirmed, 3 partly confirmed, 3 not found, 1 contradicted (15 rows; vendor-product descriptions for Agentforce, ServiceNow and Managed Agents carried no specific claim to check).

## 4. How a firm would choose

Questions that separate the products in this scope, with the sources that describe the difference:

1. **Where must client data stay?** Microsoft Foundry stores agent data in the customer's Azure OpenAI resource, in the same geography (MSFT-FOUNDRY-PRIVACY-2025). Google's and AWS's agents run in the customer's Google Cloud project or AWS account. Claude Managed Agents offers an Anthropic-managed sandbox or a self-hosted one (ANTHROPIC-CMA-2026). SaaS-embedded agents keep data in the vendor's system of record. Gateways can be self-hosted (LiteLLM MIT, Bifrost Apache 2.0; TrueFoundry lists VPC, on-prem and air-gapped).
2. **Does the agent act as the user or as itself?** Entra Agent ID, Google Agent Identity and ServiceNow/Salesforce all document both modes (delegated or dynamic user, versus autonomous or dedicated agent identity). AWS lists scoped identity for unattended agents as coming soon. A firm should ask which mode a given job needs and who owns the agent's permissions.
3. **Does the work continue when nobody is present?** AgentCore Runtime supports extended runtime for asynchronous agents; Google Agent Runtime supports long-running agents and Memory Bank; Foundry hosted agents keep session state; Managed Agents supports scheduled deployments. These match the background-agent and managed-agent-runtime classes.
4. **What controls tool access?** If the problem is "which agents may call which tools, and who is logging it", the answer sits in the gateway layer: Foundry Toolbox, Google Agent Gateway with Agent Registry, AgentCore Gateway and Policy, or a standalone gateway (LiteLLM, TrueFoundry, Bifrost, Kong, Portkey in Prisma AIRS, Glean MCP Gateway). Gateways differ on where they run and on which edition holds MCP features (Kong's MCP plugin is enterprise only; Bifrost's split is unclear).
5. **Which model and cloud is the firm already tied to?** Foundry offers catalog models including Anthropic; Google's platform lists 200+ models; AgentCore works with Claude, OpenAI, Gemini and open models; Managed Agents is Claude only. Frameworks (ADK, Strands, Microsoft Agent Framework, LangGraph) run on more than one platform.
6. **Is the work inside a system the firm already licenses?** If the job lives in CRM, IT service or enterprise search, the vendor's embedded agent inherits the existing permission model (Agentforce, ServiceNow, Glean). Overlap: all three also expose or consume MCP.

**When work should move from a personal or coding tool to a shared or production platform** (descriptive, from what the sources say each platform adds):
- The job must run without a person present, or for hours: the platforms above document asynchronous, scheduled or long-running execution, which personal assistants in a chat session do not.
- The agent needs its own identity and audit trail rather than a person's login: Entra Agent ID, Google Agent Identity and AgentCore Identity exist for this; Google logs both the user and the agent for delegated flows.
- The agent reads or writes private client data that must stay in a private network or tenant: Foundry virtual network isolation and bring-your-own resources, AgentCore session isolation, Managed Agents self-hosted sandboxes.
- Many agents or many tool connections need one policy point: gateways and registries.
- Quality must be measured over time: Foundry evaluations, Google Agent evaluation, AgentCore Evaluations and LiteLLM Lens (early access) analyse traces.
- Packaged instructions that several people reuse (skills) can start in a personal or team tool and are portable across clients that support the standard; they need a gateway or platform only when they call tools with real access.

## 5. Gaps

- **Dates on gateway pages:** the LiteLLM MCP docs, TrueFoundry, Bifrost, Kong, Glean and Strands pages were undated; I recorded access dates only.
- **Google Agent Engine to Agent Runtime rename:** not confirmed from a Google statement; Google release notes did not surface it in my fetch. Agent Gateway and Agent Identity general-availability status is not stated on the pages read. Google training/retention terms not read.
- **Salesforce identity model:** from a search snippet of a help article that did not load; the privacy FAQ PDF was read directly.
- **ServiceNow:** official AI Agents docs are behind JavaScript or authentication; identity details rest on a community article. No dated vendor page giving feature-level general availability was read.
- **Glean:** retention and training terms, and pricing, not read. Foundry audit-log specifics not read.
- **MCP governance:** the AAIF statement is from a blogger.
- **Professional services:** the PwC/AgentCore page cited in search results returned 404, so it is not used. No legal-firm example was found on any of the three platforms. No quality or override-rate evidence from any firm was found.
- **Pricing:** third-party price comparisons were seen in search results and deliberately not used.

## 6. Professional-services specifics

Do accounting, legal and tax firms use these platforms? Public, dated evidence found:

- **EY (accounting/assurance), 2026-04-07:** EY announced a global roll-out of enterprise-scale agentic AI in Assurance. It is "directly embedding a new multi-agent framework, integrated with Microsoft Azure, Microsoft Foundry and Microsoft Fabric" into EY Canvas, which EY says covers 130,000 Assurance professionals across 160,000 audit engagements (EY-AUDIT-2026). Self-reported by EY. This is an announced roll-out; the release does not say which Foundry services are used.
- **KPMG (accounting/tax/advisory), 2025-06-18:** KPMG International launched KPMG Workbench, "built on Microsoft Azure AI Foundry Services", which brings in agents from partners such as Oracle, Salesforce, ServiceNow and Workday (KPMG-WORKBENCH-2025). Self-reported; the release is from before the Foundry rename.
- **Bedrock:** nothing verified. **Vertex / Gemini Enterprise Agent Platform:** nothing verified. **Law firms:** nothing verified on any of the three platforms.
- **Adjacent evidence, not platform use:** Thomson Reuters launched agentic CoCounsel for tax, audit and accounting professionals in 2025 (seen only in search results from legaltechnology.com; not fetched, so search-only), which is a vendor product, not a firm building on a cloud platform. It is not counted above.

Professional-services firms that appear are large firms building their own platforms. Evidence for mid-size firms building on these platforms was not found.

## 7. Sources

Access for all rows: full unless noted. Access date 2026-10-22.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| MSFT-FOUNDRY-AGENTS-2026 | What is Microsoft Foundry Agent Service? | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview | ms.date 2026-09-25; updated 2026-10-15 | full |
| MSFT-ENTRA-AGENTID-2026 | What are agent identities? | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id | updated 2026-06-15 | full |
| MSFT-FOUNDRY-TOOLBOX-2026 | What is Toolbox in Microsoft Foundry? | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/tool-catalog | 2026-07-28 | full |
| MSFT-FOUNDRY-MCP-2026 | Connect agents to MCP server endpoints | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/model-context-protocol | 2026-08-26 | full |
| MSFT-FOUNDRY-OBS-2026 | Observability in Generative AI | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability | 2026-10-15 | full |
| MSFT-FOUNDRY-PRIVACY-2025 | Data, privacy, and security for Foundry Agent Service | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/agents/data-privacy-security | 2025-11-19 | full |
| MSFT-FOUNDRY-WHAT-2026 | What is Microsoft Foundry? | Microsoft Learn | Vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-foundry | 2026-08-13 | full |
| GOOG-AGENTPLATFORM-2026 | Agent Platform overview | Google Cloud docs | Vendor docs | https://cloud.google.com/agent-builder/overview (redirects to Gemini Enterprise Agent Platform) | updated 2026-10-21 | full |
| GOOG-SCALE-2026 | Scale your agents | Google Cloud docs | Vendor docs | https://cloud.google.com/agent-builder/agent-engine/overview | undated | full |
| GOOG-AGENTID-2026 | Use Agent Identity with Agent Runtime | Google Cloud docs | Vendor docs | https://cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity | updated 2026-10-21 | full |
| GOOG-GATEWAY-2026 | Agent Gateway overview | Google Cloud docs | Vendor docs | https://cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview | updated 2026-10-21 | full |
| GOOG-MODELARMOR-2026 | Model Armor | Google Cloud | Vendor product page | https://cloud.google.com/security/products/model-armor | undated | full |
| GOOG-ADK-2026 | Agent Development Kit | Google (ADK docs) | Vendor docs | https://google.github.io/adk-docs/ | undated | full |
| REG-GOOGLE-2026 | Google claims to have all the answers for enterprise AI agent sprawl | The Register (O'Ryan Johnson) | Trade press | https://www.theregister.com/2026/04/22/google_enterprise/ | 2026-04-22 | full |
| AWS-AGENTCORE-DOCS-2026 | What is Amazon Bedrock AgentCore? | AWS docs | Vendor docs | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html | undated | full |
| AWS-AGENTCORE-GA-2025 | Make agents a reality with Amazon Bedrock AgentCore: Now generally available | AWS ML Blog (Swami Sivasubramanian) | Vendor blog | https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-is-now-generally-available/ | 2025-10-13 | full |
| AWS-AGENTCORE-RUNTIME-2026 | The new AgentCore runtime: Elastic, optimized, and consistently fast starts | AWS ML Blog (Franco et al.) | Vendor blog | https://aws.amazon.com/blogs/machine-learning/the-new-agentcore-runtime-elastic-optimized-and-consistently-fast-starts/ | 2026-09-18 | full |
| STRANDS-HOME-2026 | Strands Agents | strandsagents.com | Vendor docs | https://strandsagents.com/latest/ | undated | full |
| ANTHROPIC-CMA-2026 | Claude Managed Agents overview | Anthropic | Vendor docs | https://platform.claude.com/docs/en/managed-agents/overview | undated (beta header 2026-04-01) | full (text mirror) |
| MCP-INTRO-2026 | What is the Model Context Protocol? | modelcontextprotocol.io | Standard docs | https://modelcontextprotocol.io/introduction | spec version 2026-07-28 | full |
| MCP-ARCH-2026 | MCP architecture | modelcontextprotocol.io | Standard docs | https://modelcontextprotocol.io/docs/learn/architecture | undated | full |
| MCP-REGISTRY-2026 | The MCP Registry | modelcontextprotocol.io | Standard docs | https://modelcontextprotocol.io/registry/about | undated | full |
| MCP-SKILLS-2026 | Build with Agent Skills | modelcontextprotocol.io | Standard docs | https://modelcontextprotocol.io/docs/develop/build-with-agent-skills | undated | full |
| SKILLS-OVERVIEW-2026 | Agent Skills overview | agentskills.io | Standard docs | https://agentskills.io/home | undated | full |
| SKILLS-SPEC-2026 | Agent Skills specification | agentskills.io | Standard docs | https://agentskills.io/specification | undated | full |
| ANTHROPIC-SKILLS-2025 | Introducing Agent Skills (with 2025-12-18 update) | Anthropic | Vendor announcement | https://www.anthropic.com/news/skills | 2025-10-16; update 2025-12-18 | full (text mirror) |
| WILLISON-SKILLS-2025 | Agent Skills | Simon Willison's Weblog | Named blog | https://simonwillison.net/2025/dec/19/agent-skills/ | 2025-12-19 | full |
| LITELLM-MCP-2026 | MCP Overview | LiteLLM docs | Vendor docs | https://docs.litellm.ai/docs/mcp | undated | full |
| LITELLM-LENS-2026 | LiteLLM Lens | LiteLLM docs | Vendor docs | https://docs.litellm.ai/docs/proxy/lens | undated | full |
| LITELLM-LENS-LAUNCH-2026 | LiteLLM Lens launch post | LiteLLM blog (Ishaan Jaffer et al.) | Vendor blog | https://docs.litellm.ai/blog/litellm-lens-launch | 2026-10-01 | full |
| LITELLM-RELEASE-2026 | LiteLLM release notes (v1.106.0, 2026-10-18) | LiteLLM docs | Vendor release notes | https://docs.litellm.ai/release_notes | 2026-10-18 | full |
| LITELLM-ENT-2026 | LiteLLM Enterprise | LiteLLM docs | Vendor docs | https://docs.litellm.ai/docs/enterprise | undated | partial (nav and summary) |
| TF-MCP-2026 | MCP Gateway | TrueFoundry | Vendor product page | https://www.truefoundry.com/mcp-gateway | undated | full |
| TF-MCP-DOCS-2026 | TrueFoundry MCP Gateway | TrueFoundry docs | Vendor docs | https://docs.truefoundry.com/gateway/mcp-overview | undated | full |
| BIFROST-MCP-2026 | MCP Gateway overview | Bifrost docs | Vendor docs | https://docs.getbifrost.ai/mcp/overview | undated | full |
| BIFROST-README-2026 | Bifrost AI Gateway README | Maxim AI (GitHub raw) | Vendor repo | https://raw.githubusercontent.com/maximhq/bifrost/main/README.md | undated | full |
| BIFROST-ENT-2026 | Bifrost enterprise overview | Bifrost docs | Vendor docs | https://docs.getbifrost.ai/enterprise/overview | undated | partial (nav) |
| KONG-AIGW-2026 | Kong AI Gateway | Kong Docs | Vendor docs | https://developer.konghq.com/ai-gateway/ | undated | full |
| KONG-MCP-2026 | MCP Traffic Gateway | Kong Docs | Vendor docs | https://developer.konghq.com/mcp/ | undated | full |
| KONG-MCPPLUGIN-2026 | AI MCP Proxy plugin | Kong Docs | Vendor docs | https://developer.konghq.com/plugins/ai-mcp-proxy/ | undated | full |
| PANW-ANNOUNCE-2026 | Palo Alto Networks to Acquire Portkey to Secure the Rise of AI Agents | Palo Alto Networks | Press release | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-to-acquire-portkey-to-secure-the-rise-of-ai-agents | 2026-04-30 | full |
| PANW-CLOSE-2026 | Palo Alto Networks Completes Acquisition of Portkey to Secure AI Agents | Palo Alto Networks | Press release | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents | 2026-05-29 | full |
| GLEAN-MCP-2026 | About Glean MCP server | Glean docs | Vendor docs | https://docs.glean.com/administration/platform/mcp/about | updated Oct 2026 (day not captured) | full |
| GLEAN-GATEWAY-2026 | Glean MCP Gateway | Glean docs | Vendor docs | https://docs.glean.com/administration/platform/mcp/mcp-gateway | undated | full |
| SF-AGENTFORCE-2026 | Agentforce: The AI Agent Platform | Salesforce | Vendor product page | https://www.salesforce.com/agentforce/ | undated | partial (JS-heavy) |
| SF-PRICING-2026 | Agentforce Pricing | Salesforce | Vendor product page | https://www.salesforce.com/agentforce/pricing/ | undated | full |
| SF-PRIVACY-2025 | Salesforce's Agentforce Privacy FAQ | Salesforce | Vendor PDF | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Privacy/agentforce-privacy-FAQ.pdf | June 2025 | full |
| SN-AIAGENTS-2026 | AI Agents | ServiceNow | Vendor product page | https://www.servicenow.com/products/ai-agents.html | undated | partial (text mirror) |
| SN-K26-2026 | ServiceNow turns enterprise AI chaos into control with the platform for governed, autonomous work | ServiceNow Newsroom | Press release | https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-turns-enterprise-AI-chaos-into-control-with-the-platform-for-governed-autonomous-work/default.aspx | Knowledge 2026 (May 5-7, 2026); exact day not captured | full (text mirror) |
| SN-COMMUNITY-ID-2026 | Technical Article: Securing AI Agent Identities in Now Assist | ServiceNow Community (member post) | Community post | https://www.servicenow.com/community/servicenow-otto-for-creator/technical-article-securing-ai-agent-identities-in-now-assist/m-p/3580391 | 2026-07-28 | full |
| EY-AUDIT-2026 | EY launches enterprise-scale agentic AI to redefine the audit experience for the AI era | EY | Press release | https://www.ey.com/en_us/newsroom/2026/04/ey-launches-enterprise-scale-agentic-ai-to-redefine-the-audit-experience-for-the-ai-era | 2026-04-07 | full |
| KPMG-WORKBENCH-2025 | KPMG Launches KPMG Workbench: A Multi-Agent AI Platform | KPMG International (via Newsfile Corp) | Press release | https://www.newsfilecorp.com/release/255985/KPMG-Launches-KPMG-Workbench-A-MultiAgent-AI-Platform-Transforming-Client-Delivery-and-Ways-of-Working-Across-the-Global-Organization | 2025-06-18 | full (text mirror) |
