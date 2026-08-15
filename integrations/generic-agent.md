# Generic agent integration

The core requires only a model that can read local resources and search the target documentation collection.

1. Make this directory available to the agent.
2. Register `SKILL.md` as an on-demand workflow if the platform supports skills. Use its `description` as the trigger metadata.
3. Otherwise, instruct the agent to read `SKILL.md` when creating, reviewing, or maintaining documentation.
4. Preserve relative paths so the router can load `references/` and `checklists/`.
5. Give the agent search and edit access only to knowledge sources the user placed in scope.

Suggested persistent instruction:

```text
For substantial documentation or persistent-knowledge tasks, read
<installation-path>/documentation-quality/SKILL.md and follow its routing.
Search existing knowledge before creating a file. Do not reorganize or delete
knowledge-base content without first recommending the change.
```

If the platform cannot load files progressively, include `SKILL.md` and only the task-specific references in the request. Hooks and Git are optional.
