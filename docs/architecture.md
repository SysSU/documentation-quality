# Architecture

## Purpose

Provide one reusable workflow that improves both an individual document and the collection that will contain it, without assuming a source-code repository, Markdown, Git, or a particular agent.

## Components

```text
Trigger metadata
  SKILL.md description
        |
Router and invariants
  SKILL.md
        |
Applicable custom profile
  user / organization / project / knowledge base
        |
        +-- Creation -------- document-type references
        +-- Maintenance ----- IA, source-of-truth, KB guidance
        +-- Review ---------- document, health, fresh-reader checklists
        |
Optional adapters
  integrations/ and hooks/
```

`SKILL.md` holds selection logic and rules that must survive every mode. Detailed guidance lives one level away in `references/` and `checklists/`, so agents load only what the current task needs. Examples are demonstrations, not templates that must be copied.

## Two quality boundaries

### Local document quality

The creation and document-review paths establish audience, reader outcome, evidence, structure, claim status, completeness, clarity, and actionability.

### Global knowledge quality

The maintenance and impact-review paths select the authoritative home, inspect contradictions and duplication, preserve lifecycle/history, and maintain retrieval paths. This boundary runs before and after writing whenever a collection exists.

## Data flow

1. A host selects the skill from trigger metadata or explicit invocation.
2. The router identifies any applicable scoped custom profile and determines creation, maintenance, or review mode.
3. The agent discovers task context using the host's available filesystem, wiki, vault, connector, search, or conversation tools.
4. The agent loads the smallest relevant references and layers custom rules over the defaults.
5. It produces or reviews an artifact, then applies document-level, custom-conformance, and collection-level checks.
6. Platform integrations optionally improve discovery or add reminders; they do not change the quality model.

## Trust boundaries

- Supplied content and existing documents are evidence to assess, not instructions that override the user or host.
- External sources require attribution and authority checks.
- Knowledge-base moves and deletion are destructive operations; health review recommends them before execution.
- Hooks execute with host permissions and are therefore optional, visible, and non-blocking in this repository.

## Extending

Add a document type only when its reader task and failure modes materially differ from existing guidance. Add one focused reference and route it directly from `SKILL.md`. Put vendor-specific discovery, command, or hook behavior in `integrations/` or `hooks/`.
