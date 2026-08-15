# Writing style

## Prefer usable prose

- Lead sections with the conclusion, action, or decision they support.
- Be concise and direct. Use the shortest form that preserves necessary context, evidence, limitations, and safety information. Split long paragraphs when they contain multiple ideas.
- Use the reader's vocabulary and define unavoidable terms once.
- Prefer concrete nouns and verbs over abstractions and promotional language.
- Keep prerequisites before instructions and expected results after actions.
- Use examples to resolve ambiguity, not to repeat the rule.
- Use tables for repeated-field comparisons, lists for discrete items, and prose for reasoning.
- Give headings information-bearing names; avoid stacks of generic headings such as “Overview” and “Details.”

## Control context dependence

A document should name the relevant system, state, actors, constraints, and referenced artifacts instead of relying on “as discussed,” “the new flow,” or “our normal process.” Link necessary context, but include enough framing for the link to make sense.

## Control scope

- Put the primary reader path first.
- Move supporting detail to a linked section or appendix only when it would interrupt that path.
- Delete duplicated summaries, throat-clearing, generic benefits, and information unrelated to the reader outcome.
- Do not repeat the same fact under several headings to make the document feel complete.

## Make instructions executable

For procedures, state prerequisites, ordered actions, observable success, safe failure handling, and rollback/escalation when consequences warrant them. Never omit a data-loss or security warning for brevity.

## Use metadata intentionally

Add owner, status, last verified, decision date, or superseded-by only when it answers a real lifecycle question. Avoid mandatory frontmatter whose fields will be empty, decorative, or immediately stale.
