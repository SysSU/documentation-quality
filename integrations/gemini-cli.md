# Gemini CLI

Gemini CLI discovers workspace skills in `.gemini/skills` or `.agents/skills`, and user skills in `~/.gemini/skills` or `~/.agents/skills`.

Link a local clone:

```sh
gemini skills link /absolute/path/to/documentation-quality
```

Or install from GitHub:

```sh
gemini skills install https://github.com/SysSU/documentation-quality
```

Use `/skills list` to confirm discovery and `/skills reload` after changes. Workspace skills require a trusted workspace. The skill can activate from a matching request; use the CLI's skills controls to enable or disable it.

Official references: [Agent Skills](https://geminicli.com/docs/cli/skills/) and [managing skills](https://geminicli.com/docs/cli/using-agent-skills/).
