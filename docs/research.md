# Research

**Research date:** 2026-08-15<br>
**Question:** Which established documentation, knowledge-management, and agent-extension practices should shape a cross-agent documentation-quality system?

## Method

Primary specifications, official product documentation, established framework sites, maintainers' repositories, and research papers were preferred. Sources were used for principles, not copied as a single methodology. Product-specific details were kept in integrations; the core includes only behavior that remains useful across tools and non-code knowledge systems.

## Findings

### Skills should disclose detail progressively

The [Agent Skills specification](https://agentskills.io/specification) defines a minimal `SKILL.md` plus optional references and scripts, and explicitly describes progressive disclosure. [Anthropic's Agent Skills repository](https://github.com/anthropics/skills) uses the same resource pattern. The design implication is a short trigger/router and task-specific references, not a monolithic prompt.

Anthropic's [doc-coauthoring skill](https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md) contributes three useful ideas: gather context before drafting, refine structure and content iteratively, and test with a fresh reader who lacks the author's conversational context. This project generalizes those ideas beyond coauthoring and adds collection-wide authority, contradiction, duplication, and lifecycle checks.

### Agent instructions and document guidance are different scopes

The [AGENTS.md specification](https://agents.md/) positions `AGENTS.md` as a predictable place for repository instructions, supports nested scope, and gives closer instructions precedence. Current [Codex skill guidance](https://developers.openai.com/codex/skills/) likewise separates on-demand skills from persistent repository guidance. Therefore `AGENTS.md` in this project stays small, while the reusable documentation workflow lives in the skill.

### Document type must follow reader need

[Diátaxis](https://diataxis.fr/start-here/) distinguishes tutorials, how-to guides, reference, and explanation by whether readers are studying or working and whether they need action or cognition. The useful general principle is not to force the four-folder taxonomy everywhere; it is to stop mixing incompatible reader tasks in one document.

The [Write the Docs docs-as-code guide](https://www.writethedocs.org/guide/docs-as-code/) advocates issue tracking, version control, plain text, review, and automated tests where appropriate. Its [writing guide](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/) also warns that FAQs tend to become stale, unrelated, and hard to search. The extracted principle is workflow integration and maintainability, while keeping Git optional for wikis, shared documents, and AI brains.

Google's [developer documentation style guide](https://developers.google.com/style) prioritizes project-specific rules, clarity, consistency, and reader needs over rigid adherence. This supports adaptive structures and a local style hierarchy rather than a universal prose template.

### PRDs and test plans are decision artifacts, not content dumps

Atlassian's [PRD guidance](https://www.atlassian.com/agile/product-management/requirements) emphasizes shared customer understanding, goals, assumptions, user stories, questions, and explicit out-of-scope work without over-specifying implementation. This project strengthens the separation between problem, requirement, solution, and implementation and requires evidence and visible unknowns.

Microsoft's [architecture strategies for testing](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/testing) distinguishes a durable high-level strategy from a release-specific plan and ties both to objectives, scope, risk, roles, environments, and entry/exit criteria. Its [test-plan guidance](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/testing-strategy-planning) adds business-process scope, positive and negative scenarios, versioned environments, results, and ownership. The project therefore treats a test plan as a risk and evidence strategy, with test cases linked separately.

### Decisions need history and supersession

The maintained [Architecture Decision Record collection](https://github.com/joelparkerhenderson/architecture-decision-record) defines ADRs around context and consequences and recommends specificity, rationale, timestamps, and explicit consideration of when a record is unnecessary. The extracted principle applies beyond architecture: preserve the context and consequences of material decisions, then supersede them rather than rewriting history.

### Knowledge bases need managed write paths

Obsidian's official guidance treats [internal links](https://obsidian.md/help/links) as a network between notes and provides [properties](https://obsidian.md/help/properties) for small, machine-readable metadata. These are useful primitives, but they do not by themselves prevent duplicated or stale notes. An AI-assisted vault workflow must search links, headings, aliases, and contrary terms before writing, and must add metadata only when it supports retrieval or lifecycle.

Agent-memory research reinforces that storage alone is insufficient. The survey [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) organizes memory around design and evaluation rather than treating recall as simple accumulation. A newer survey, [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564), distinguishes memory forms, functions, and dynamics—how memory is formed, evolved, and retrieved. The practical implication here is a managed `write → reconcile → retrieve` lifecycle with filtering, contradiction handling, consolidation, and forgetting/supersession.

### Linting is useful but cannot judge authority

[Vale](https://github.com/errata-ai/vale) demonstrates extensible automated prose linting, while docs-as-code practices support link checking and tests. These tools can catch syntax, style, and broken-link defects. They cannot decide whether a claim is authoritative, whether two scoped statements truly conflict, or whether a new page improves a knowledge system. Automated checks remain optional supplements to semantic review.

### Cross-agent support is converging but not identical

Claude Code documents [project and user Agent Skills](https://code.claude.com/docs/en/skills) and lifecycle [hooks](https://code.claude.com/docs/en/hooks). GitHub Copilot documents skill locations in its [customization reference](https://docs.github.com/en/copilot/reference/customization-cheat-sheet). Gemini CLI documents [skill discovery, installation, linking, and reload](https://geminicli.com/docs/cli/using-agent-skills/). Cursor documents [`AGENTS.md` and scoped project rules](https://docs.cursor.com/context/rules-for-ai). A standard `SKILL.md` core is therefore broadly reusable, but installation, automatic discovery, invocation syntax, and hooks belong in per-platform adapters.

## Synthesis adopted by this project

1. Start from audience, purpose, reader task, evidence, and lifecycle.
2. Use document-type guidance selectively rather than applying one template.
3. Search the surrounding knowledge system before creating or changing a page.
4. Give consequential knowledge one authoritative home and link from secondary views.
5. Label facts, assumptions, decisions, recommendations, hypotheses, and unknowns.
6. Treat contradiction, duplication, staleness, navigation, and orphaning as quality defects.
7. Preserve history through dated status and supersession only where lifecycle needs it.
8. Use fresh-reader review to expose hidden context.
9. Use linting and hooks as optional signals, not semantic authorities.

## Research limits

- “AI knowledge management” and “AI-assisted Obsidian” have rapidly changing, vendor- and workflow-specific practices; this project relies on durable knowledge-lifecycle principles and official platform primitives instead of endorsing a plugin stack.
- No universal quantitative thresholds define an oversized document, excessive fragmentation, or acceptable duplication. Reviews use audience, authority, lifecycle, and retrieval evidence.
- Agent skill discovery and installation behavior changes over time. Integration pages link their current official sources and should be reverified when platforms update.
