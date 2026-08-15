---
name: documentation-quality
description: Create, review, and maintain trustworthy documentation across software repositories, AI brains, Obsidian vaults, wikis, plans, research, product artifacts, runbooks, and other knowledge systems. Use when an agent is asked to write or revise a substantial document, apply a custom style guide or documentation profile, document a change, add persistent knowledge, resolve conflicting or duplicate documentation, audit documentation health, or run a fresh-reader review.
---

# Documentation Quality

Optimize both the document in front of you and the knowledge system around it. Never assume that creating a new file is the right answer.

## Route the task

1. Read [references/core-principles.md](references/core-principles.md) for every substantial task.
2. Identify any user, organization, project, or knowledge-base documentation profile supplied in the request or available in scoped instructions. When one exists, or the user requests stricter custom rules, read [references/customization.md](references/customization.md) and load the applicable guide.
3. Choose one primary mode:
   - **Create or substantially rewrite a document:** follow **Creation mode**.
   - **Store or change persistent knowledge:** follow **Maintenance mode**.
   - **Review without editing:** follow **Review mode**.
4. Load only the task-specific references listed below.

### Creation mode

1. Establish the purpose, audience, reader task or decision, and available evidence.
2. Inspect related documents and sources before drafting.
3. Decide whether to update an authoritative document instead of creating a new one. Read [references/information-architecture.md](references/information-architecture.md) when a documentation collection already exists.
4. Load the relevant document-type guide:
   - PRD: [references/prd.md](references/prd.md)
   - Test plan: [references/test-plan.md](references/test-plan.md)
   - Technical design or architecture: [references/architecture.md](references/architecture.md)
   - Decision record: [references/decision-record.md](references/decision-record.md)
   - Project or implementation plan: [references/plans.md](references/plans.md)
   - Research: [references/research.md](references/research.md)
   - Runbook or operating procedure: [references/runbook.md](references/runbook.md)
   - README, API, tutorial, how-to, reference, or other software documentation: [references/software-documentation.md](references/software-documentation.md)
5. Draft with facts, assumptions, recommendations, decisions, hypotheses, and unknowns clearly distinguished. Load [references/writing-style.md](references/writing-style.md) when prose, structure, or procedures are material to the task, then apply the applicable custom profile as the stricter scoped layer.
6. Apply [checklists/document-review.md](checklists/document-review.md). For important or high-impact work, also apply [checklists/fresh-reader-review.md](checklists/fresh-reader-review.md).

### Maintenance mode

1. Read [references/knowledge-base-management.md](references/knowledge-base-management.md), [references/information-architecture.md](references/information-architecture.md), and [references/source-of-truth.md](references/source-of-truth.md).
2. Follow `SEARCH → READ → UNDERSTAND → MODIFY`:
   - Search filenames, headings, aliases, links, and likely synonyms.
   - Read candidate sources deeply enough to identify authority and lifecycle.
   - Compare new information with existing facts, decisions, and policies.
   - Update the authoritative home; link from secondary documents instead of copying.
3. Surface contradictions before choosing a winner. Record uncertainty when authority cannot be resolved.
4. Check affected links, navigation, duplicates, stale statements, and superseded material with [checklists/documentation-impact.md](checklists/documentation-impact.md).
5. Recommend merges, splits, moves, or deletions before destructive reorganization.

### Review mode

1. State the document's intended audience and outcome. If absent, mark that as a finding instead of inventing it.
2. Apply [checklists/document-review.md](checklists/document-review.md), including any applicable custom profile's required rules.
3. For collection-wide review, load [checklists/knowledge-base-health.md](checklists/knowledge-base-health.md) and the maintenance references.
4. For an independent usability pass, apply [checklists/fresh-reader-review.md](checklists/fresh-reader-review.md).
5. Rank findings by impact. Separate verified errors from risks, suggestions, and unanswered questions.

## Operating rules

- Gather available context before asking for information that can be discovered.
- Never fabricate missing details. Label `Unknown`, `Assumption`, `Open question`, or `TBD`.
- Apply scoped custom documentation rules over the built-in defaults, but never let style override accuracy, source integrity, safety, accessibility, or explicit user instructions.
- Prefer one authoritative home per important claim.
- Do not add metadata mechanically. Use status, owner, decision date, last verified date, or supersession only when lifecycle matters.
- Preserve decision history: supersede decisions rather than silently rewriting why they were made.
- Do not run a fresh-reader review with the author's hidden reasoning. Give the reviewer only the finished document, necessary source material, audience, and goal.
- Do not treat Git, Markdown, or any vendor feature as required. Use native search, links, metadata, and hooks only when the environment supports them.

## Output expectations

When creating or editing, return the artifact plus a compact note of evidence gaps, conflicts, and affected authoritative sources. When reviewing, return prioritized findings and recommended changes; do not reorganize or delete material unless the user asked for implementation.
