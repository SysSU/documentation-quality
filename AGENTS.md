# Repository instructions

This repository is a vendor-neutral documentation-quality Agent Skill.

- Follow `SKILL.md` when creating or changing documentation.
- Use `SEARCH → READ → UNDERSTAND → MODIFY`; do not create a new page until existing authoritative locations have been checked.
- Keep `SKILL.md` a concise router. Put detailed guidance in one-level-deep `references/` or `checklists/` files and link it directly from `SKILL.md`.
- Keep vendor-specific behavior in `integrations/` or `hooks/`.
- Do not make Git, a network connection, subagents, or hooks a requirement of the core workflow.
- Preserve one authoritative home for each rule. Link rather than repeating detailed instructions.
- Add sources to `docs/research.md` when research changes project guidance.
- Run `python3 scripts/validate.py` before finishing.
