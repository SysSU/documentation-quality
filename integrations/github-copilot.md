# GitHub Copilot

GitHub Copilot supports Agent Skills in `.github/skills/<name>`, `.claude/skills/<name>`, or `.agents/skills/<name>` for project scope, and `~/.copilot/skills/<name>` or `~/.agents/skills/<name>` for personal scope.

```sh
mkdir -p ~/.copilot/skills
ln -s /absolute/path/to/documentation-quality ~/.copilot/skills/documentation-quality
```

For a repository, copy or link to `.github/skills/documentation-quality`. `AGENTS.md` is also supported by Copilot CLI for short always-on instructions; keep the detailed workflow in the skill so it loads only for relevant work.

Restart or start a new active session when instruction changes are not detected. Use Copilot's instruction inspection features to confirm what loaded.

Official references: [customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) and [Copilot CLI custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions).
