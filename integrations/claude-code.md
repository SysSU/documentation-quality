# Claude Code

Claude Code supports Agent Skills at project, user, and plugin scope. Link the cloned repository into one supported skills directory:

```sh
mkdir -p ~/.claude/skills
ln -s /absolute/path/to/documentation-quality ~/.claude/skills/documentation-quality
```

For one project, use `.claude/skills/documentation-quality` instead. Invoke with `/documentation-quality` or ask for a matching documentation task; Claude can select it from the frontmatter description.

The skill remains useful without hooks. To add a non-blocking reminder after Markdown edits, follow [`../hooks/claude-code/README.md`](../hooks/claude-code/README.md). Review any hook before enabling it because hooks execute with the user's permissions.

Official references: [Agent Skills](https://code.claude.com/docs/en/skills) and [hooks](https://code.claude.com/docs/en/hooks).
