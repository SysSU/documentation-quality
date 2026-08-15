# Codex

Codex discovers repository skills under `.agents/skills` from the working directory through the repository root, and user skills under `~/.agents/skills`.

```sh
mkdir -p ~/.agents/skills
ln -s /absolute/path/to/documentation-quality ~/.agents/skills/documentation-quality
```

For repository scope, link or copy it to `.agents/skills/documentation-quality`. Invoke it explicitly with `$documentation-quality`; matching tasks can also activate it implicitly. `agents/openai.yaml` supplies optional UI metadata.

Use `AGENTS.md` for short, always-on repository expectations and this skill for the longer workflow that should load on demand. Codex follows symlinked skill directories.

Official references: [Build skills](https://developers.openai.com/codex/skills/) and [AGENTS.md](https://developers.openai.com/codex/guides/agents-md/).
