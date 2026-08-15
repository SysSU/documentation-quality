# Documentation Quality

A vendor-neutral Agent Skill for creating useful documents and maintaining coherent knowledge systems.

Most documentation tooling asks, “Is this page well written?” This project also asks, “Does this page make the larger body of knowledge healthier?” It applies to software repositories, AI brains, Obsidian vaults, wikis, PRDs, test plans, architecture records, research, runbooks, project plans, internal knowledge bases, and handoff artifacts.

## What changes

Without this skill, “document this” often becomes another polished Markdown file. With it, an agent first establishes the reader's purpose, searches what already exists, resolves the authoritative location, writes from evidence, checks contradictions and staleness, and reviews the result as a fresh reader.

```text
                   Documentation Quality
                            Skill
                              |
          +-------------------+-------------------+
          |                   |                   |
      Document            Knowledge           Review
      creation            maintenance          / QA
          |                   |                   |
      PRD, test,          AI brain, wiki,    Fresh reader,
      design, plan        docs repository     health review
```

## Core behavior

### Create a document

```text
purpose → audience → reader task → evidence → structure
        → draft → completeness → clarity → claim check
        → fresh-reader review → revise
```

The structure is selected for the document's job. A PRD separates problem, requirements, and solution; a test plan explains risk and strategy rather than expanding into a case inventory.

### Maintain a knowledge base

```text
SEARCH → READ → UNDERSTAND → MODIFY
```

The agent searches first, updates the authoritative source when one exists, links instead of copying, checks contradictions and references, and recommends destructive reorganization before performing it.

### Review quality

The shared rubric covers correctness, completeness, relevance, clarity, structure, findability, authority, consistency, maintainability, and actionability. A separate health review detects duplication, conflicts, fragmentation, staleness, orphaned pages, weak navigation, and unclear ownership across a collection.

## Install

This repository is itself an [Agent Skill](https://agentskills.io/specification). Clone it, then link or copy the repository into the skill directory supported by your agent.

```sh
git clone https://github.com/SysSU/documentation-quality.git
```

Common locations:

| Agent | Project scope | User scope |
| --- | --- | --- |
| Claude Code | `.claude/skills/documentation-quality` | `~/.claude/skills/documentation-quality` |
| Codex | `.agents/skills/documentation-quality` | `~/.agents/skills/documentation-quality` |
| Gemini CLI | `.gemini/skills/documentation-quality` or `.agents/skills/documentation-quality` | `~/.gemini/skills/documentation-quality` |
| GitHub Copilot | `.github/skills/documentation-quality` or `.agents/skills/documentation-quality` | `~/.copilot/skills/documentation-quality` |

Cursor can use the repository's compact [`AGENTS.md`](AGENTS.md) as a project rule; see [`integrations/cursor.md`](integrations/cursor.md). Other agents can load `SKILL.md` directly or copy its routing instructions into their instruction mechanism.

Invoke it explicitly when supported:

```text
Use $documentation-quality to write a PRD from these notes.
Use $documentation-quality to add this information to my AI brain.
Use $documentation-quality to audit this vault for conflicting sources of truth.
```

See [`integrations/`](integrations/) for platform-specific setup and [`hooks/claude-code/`](hooks/claude-code/) for an optional, non-blocking edit reminder.

## Use your own documentation rules (optional)

The skill works without any setup. Its built-in guidance covers document structure, writing quality, and knowledge-base maintenance.

Add custom rules only when you want the agent to follow an existing style guide or remember documentation conventions for later tasks:

| Need | What to do |
| --- | --- |
| One document | Put the extra rules in your request. |
| One repository, vault, or wiki | Put short rules in its agent instructions, or keep a profile there and link to it. |
| All of your projects | Keep a user-level profile and reference it from your agent's user instructions. |

A profile is an ordinary document containing only the rules you want to add or make stricter. For example:

```md
# Documentation profile

## Required
- Use sentence-case headings.
- Link factual claims to their authoritative source.

## Preferred
- Write concise paragraphs in active voice.

## Terminology
- Use “workspace,” not “tenant.”
```

Store the profile with the content it governs—not inside this skill—so updating the skill cannot overwrite your rules. The filename is up to you; `DOCUMENTATION_STYLE.md` is one clear option.

For project-scoped rules, you can put a short style guide directly in `AGENTS.md` or `CLAUDE.md`. If it becomes long, keep it in a separate file and link to it from those instructions. `AGENTS.md` works across agents that support the convention; `CLAUDE.md` is specific to Claude Code. Some vault and wiki environments do not load either file automatically, so name the profile in your request when necessary.

Then name it when invoking the skill:

```text
Use $documentation-quality and follow ./DOCUMENTATION_STYLE.md to write this runbook.
Treat its Required rules as completion criteria.
```

The order is simple: your current request wins, then the closest applicable profile, then broader profiles, then this skill's built-in guidance. Custom style rules cannot override accuracy, source integrity, safety, privacy, or accessibility.

Users create or edit their own profile, such as `DOCUMENTATION_STYLE.md`. The agent—not the user—reads [`references/customization.md`](references/customization.md) for instructions on applying profile scopes, strictness, templates, and conflicts. Do not edit that reference to store personal or project rules.

## Repository map

- [`SKILL.md`](SKILL.md) — lightweight task router and invariant workflow.
- [`references/`](references/) — focused guidance loaded only when relevant.
- [`checklists/`](checklists/) — document, impact, fresh-reader, and knowledge-health reviews.
- [`examples/`](examples/) — PRD, test-plan, knowledge-base, and runbook examples.
- [`integrations/`](integrations/) — vendor-specific installation and invocation.
- [`docs/research.md`](docs/research.md) — research findings and sources.
- [`docs/architecture.md`](docs/architecture.md) and [`docs/design-decisions.md`](docs/design-decisions.md) — design and tradeoffs.

## Principles

- Optimize local document quality and global knowledge quality.
- Establish audience and reader outcome before selecting headings.
- Ground claims; label uncertainty and recommendations.
- Give important knowledge one authoritative home.
- Add lifecycle metadata only where it prevents staleness or preserves history.
- Prefer links and useful navigation over repeated summaries.
- Make health recommendations before merges, moves, or deletion.
- Keep the core useful without Git, hooks, plugins, or network access.

## Validation

Run:

```sh
python3 scripts/validate.py
```

The dependency-free validator checks skill frontmatter, routed local links, Markdown links, JSON examples, and the example hook's behavior. The project is licensed under the [MIT License](LICENSE).
