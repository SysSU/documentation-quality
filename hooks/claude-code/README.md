# Optional Claude Code hook

`documentation_impact.py` adds a non-blocking context reminder after Claude Code successfully edits a document. It does not review content, change files, or prevent completion.

To enable it in this repository, merge `settings.example.json` into `.claude/settings.json`. For another repository, copy the script there or replace the command with its absolute installed path. Claude Code merges hooks from its settings layers, so preserve existing entries.

Test the script before enabling it:

```sh
python3 hooks/claude-code/documentation_impact.py --self-test
printf '%s' '{"tool_input":{"file_path":"docs/plan.md"}}' \
  | python3 hooks/claude-code/documentation_impact.py
```

Review hooks before enabling them: command hooks execute automatically with the user's environment permissions. This hook uses only the Python standard library. See the official [Claude Code hooks reference](https://code.claude.com/docs/en/hooks).
