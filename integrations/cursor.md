# Cursor

Cursor's documented portable integration is `AGENTS.md` or project rules. It does not need to ingest every reference on every request.

For a repository using Cursor:

1. Add the core behavior from this repository's `AGENTS.md` to the target repository's root `AGENTS.md`.
2. Make the cloned `documentation-quality` directory available in the workspace.
3. Add a focused `.cursor/rules/documentation-quality.mdc` rule that tells the agent to read `documentation-quality/SKILL.md` for substantial documentation or persistent-knowledge work.

Example rule:

```md
---
description: Apply when creating, reviewing, or maintaining substantial documentation or persistent knowledge.
alwaysApply: false
---

Read @documentation-quality/SKILL.md and load only the references it routes for this task.
Search existing documentation before creating a new file.
```

Adjust the relative path to the installation. If rules cannot reference files outside the workspace, copy the skill into the repository or invoke it manually with `@` file context.

Official reference: [Cursor rules](https://docs.cursor.com/context/rules-for-ai).
