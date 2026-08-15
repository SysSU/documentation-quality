# Design decisions

## 001 — Treat documentation as a knowledge-system change

**Status:** Accepted

Every substantial task evaluates local document quality and global knowledge quality. This prevents a polished new page from silently competing with an existing source of truth.

## 002 — Search before creating

**Status:** Accepted

The default in an existing collection is `SEARCH → READ → UNDERSTAND → MODIFY`. New files require a distinct reader task, authority, lifecycle, or scope that cannot be served coherently by an existing document.

## 003 — Keep the skill entry point as a router

**Status:** Accepted

`SKILL.md` contains mode selection and invariants. Document-type and maintenance detail lives in directly linked resources. This follows progressive disclosure and avoids charging every documentation task for every template.

## 004 — Use adaptive structures, not mandatory templates

**Status:** Accepted

References provide section sets and quality questions, not fixed empty headings. Audience and reader outcome control structure. This avoids turning PRDs, test plans, and designs into the same generic Markdown shape.

## 005 — Prefer instruction-only core behavior

**Status:** Accepted

No runtime, indexer, embedding store, linter dependency, or Git workflow is required. Agents use the search and edit capabilities already available in their host. Add automation only after an environment demonstrates a repeatable need.

## 006 — Recommend structural deletion before performing it

**Status:** Accepted

Knowledge-base audits report evidence, proposed authority, links affected, and confidence before bulk merges, moves, archives, or deletion. Structural changes can destroy history and retrieval paths even when the proposed taxonomy looks cleaner.

## 007 — Preserve decision history

**Status:** Accepted

Accepted decisions are superseded or annotated rather than silently rewritten. Current operational and architecture pages may change, while decision records retain why an earlier choice was made.

## 008 — Keep hooks optional and advisory

**Status:** Accepted

The included Claude Code hook only reminds the agent to apply the impact checklist after document edits. It neither blocks work nor attempts automated semantic judgment. Platform hooks are incomplete substitutes for the skill and are not portable across knowledge environments.

## 009 — Layer customization instead of forking the skill

**Status:** Accepted

User, organization, project, and knowledge-base profiles apply as scoped layers over the built-in guidance. Profiles stay with the environment they govern so skill updates do not overwrite them. Strict custom rules become review criteria, but cannot weaken accuracy, source integrity, safety, privacy, accessibility, or destructive-change safeguards.
