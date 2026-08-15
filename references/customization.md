# Custom documentation profiles

This is agent-facing guidance bundled with the skill. Users should not edit this file to configure their documentation rules. Read the user's separate style guide or profile instead.

Layer user, team, organization, project, or knowledge-base rules over this skill without editing the skill itself. A profile may define voice, terminology, mechanics, templates, citations, naming, metadata, lifecycle rules, or review gates.

## Find the applicable profile

Use a guide explicitly supplied or named by the user first. Otherwise inspect documentation instructions already in scope, such as an AI brain's schema, repository instructions, a linked editorial guide, or a host-provided user profile. Do not search outside the user's authorized knowledge sources.

Keep custom profiles in the system they govern, not inside an installed copy of this skill. This prevents skill updates from overwriting local policy. No filename is required; `DOCUMENTATION_STYLE.md` is a reasonable choice when the environment has no convention.

## Resolve precedence

Follow the host's instruction hierarchy. Within documentation guidance, use this order:

1. explicit constraints in the current user request;
2. the most narrowly scoped applicable custom profile;
3. broader project, organization, or user profiles;
4. the relevant document-type reference;
5. the built-in writing style.

Accuracy, evidence labeling, source integrity, security, privacy, accessibility, and destructive-change safeguards remain mandatory. Surface a conflict instead of following a style rule that would weaken them.

## Interpret strictness

- Treat `must`, `must not`, and rules under **Required** as acceptance criteria.
- Treat `should`, **Preferred**, and examples as guidance unless the profile says otherwise.
- Apply scope conditions such as audience, document type, folder, publication channel, or lifecycle before enforcing a rule.
- Ask only when unresolved rules would materially change the artifact. Otherwise follow the higher-precedence or narrower rule and note the choice.

For a strict profile, make a short applicable-rules checklist before drafting, check every required rule during review, and report any deliberate exception with its reason. Do not alter facts or omit necessary warnings merely to satisfy tone or length limits.

## Suggested profile shape

Use only the sections that carry real rules:

```md
# Documentation profile

Scope: Published product documentation
Strictness: Required rules block completion

## Required
- Use sentence-case headings.
- Define an abbreviation on first use.
- Keep procedures in numbered steps with an observable result.

## Preferred
- Use second person and active voice.
- Keep paragraphs under five sentences when clarity permits.

## Terminology
- Use “workspace,” not “tenant.”
- Use “select” for UI controls; reserve “click” for mouse-specific actions.

## Structure
- Every how-to must include prerequisites, procedure, verification, and recovery.

## Citations
- Link external factual claims to a primary source.

## Exceptions
- Legal text supplied by counsel is reproduced unchanged.

## Verification
- Report required-rule exceptions before completion.
```

## Apply templates carefully

Treat required template sections as required. For optional sections, omit those that do not support the reader's task rather than leaving empty headings. Link to authoritative facts instead of copying them into every template-generated document.
