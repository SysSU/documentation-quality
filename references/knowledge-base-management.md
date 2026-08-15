# Knowledge-base and AI-brain management

Persistent knowledge is a retrieval system, not an append-only transcript. Its write path must decide what deserves persistence, where it belongs, and what existing knowledge it changes.

## Ingest new information

1. Identify the durable claim, its source, confidence, scope, and time sensitivity. Exclude conversational filler and temporary reasoning unless future work needs it.
2. Classify it conceptually: fact, decision, policy, process, project, person, system, research, plan, reference, working note, or history. Do not force this classification into folders.
3. Search for the entities, topic, likely synonyms, old terminology, and the claim's opposite.
4. Read candidate authoritative pages and their links.
5. Choose one action: update, append a dated event, link, merge recommendation, new page, or do not persist.
6. Check contradictions, duplication, navigation, and stale downstream summaries.

## Detect degradation

- **Duplicate knowledge:** substantially equivalent claims maintained in multiple places.
- **Conflicting facts:** incompatible claims without scope, date, or supersession explaining the difference.
- **Fragmentation:** one topic spread across tiny notes that no reader can discover as a whole.
- **Overloaded pages:** unrelated reader tasks or lifecycles combined in one file.
- **Weak authority:** readers cannot tell which statement controls.
- **Staleness:** temporary or future-tense language outlives its validity.
- **Poor discovery:** weak names, missing indexes, isolated pages, or absent links.
- **Repeated summaries:** secondary pages slowly become competing sources.
- **Link rot:** targets moved, deleted, or inaccessible.

## Resolve contradictions

Search the new claim's important nouns, verbs, and opposites. For “production deploys automatically after merge to main,” also search `deployment`, `release`, `production`, `main`, `manual`, `approval`, and old branch names.

Compare source authority, recency, scope, and observed behavior. If one source wins, update the authoritative page and repair or remove conflicting secondary text. If authority is unclear, surface the conflict with both sources and the decision needed; do not merge the statements into false certainty.

## Manage time

Pay attention to “currently,” “temporary,” “planned,” “starting next month,” version names, changing roles, and provisional architecture. Where useful, record status, effective date, decision date, owner, last verified date, or superseded-by. Do not attach every field to every note.

## Reorganize safely

Audit and recommend before bulk moves, merges, splits, or deletion. A recommendation should list proposed authoritative homes, content to merge, links to repair, history to preserve, and uncertain cases. Perform destructive changes only with authorization and an available recovery path.

## Environment notes

In an Obsidian vault, use the vault's established wikilink or Markdown-link style, inspect backlinks/unlinked mentions when available, and preserve aliases/properties used for retrieval. In wikis or agent memory stores, use their native search, identifiers, permissions, and revision history. The principles do not depend on Markdown or Git.
