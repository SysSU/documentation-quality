# Software documentation

Software documentation is one specialization, not the boundary of this skill.

## Choose by reader need

Use the Diátaxis distinction when it helps:

- **Tutorial:** a safe learning experience for a learner.
- **How-to:** steps for a competent user pursuing a real goal.
- **Reference:** accurate, complete facts organized like the system described.
- **Explanation:** context, rationale, and connections that build understanding.

Avoid combining all four into one undifferentiated page.

## Common artifacts

### README

State what the project is, who it is for, the problem it solves, the shortest successful start, where deeper docs live, support/contribution paths, and license. Keep volatile architecture or deployment detail in authoritative linked pages.

### API and reference

Reflect actual interfaces and versions. Include inputs, outputs, errors, constraints, auth, examples, and compatibility where relevant. Generated reference should identify its source; handwritten explanation should not compete with it.

### Tutorials and how-tos

State prerequisites, give executable steps, show expected results, and verify the path. A tutorial prioritizes learning continuity; a how-to permits branching around a real task.

### Change documentation

Inspect the behavior, requirements, tests, existing docs, and previous decisions. Update the authoritative user, operator, or developer path as part of the change; do not merely append a changelog entry.

## Docs-as-code when available

Version control, review, issue tracking, plain text, link checking, and automated tests can improve traceability and freshness. They are means, not requirements: apply the same quality model in wikis, shared documents, and memory systems without Git.

## Quality checks

- Does documentation match actual supported behavior?
- Can the target user reach first success without undocumented context?
- Are version and compatibility boundaries visible?
- Are generated and handwritten sources clearly separated?
- Does navigation lead to the next likely task?
