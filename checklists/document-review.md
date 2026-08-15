# Document review

Start by stating the intended audience, reader outcome, document authority, evidence set, and applicable custom profile. Score only when comparison benefits from it; findings are more useful than a decorative total.

## Rubric

| Dimension | Review question | Failure signals |
| --- | --- | --- |
| Correctness | Are claims accurate and grounded? | unsupported certainty, behavior mismatch, incorrect links |
| Completeness | Can the reader fulfill the document's purpose? | missing prerequisites, constraints, decisions, failure paths |
| Relevance | Does each section help the reader's task? | generic filler, history in procedures, repeated context |
| Clarity | Can the intended audience understand it once? | undefined terms, vague pronouns, hidden assumptions |
| Structure | Is information ordered and grouped by reader need? | template-shaped content, mixed lifecycles, poor headings |
| Findability | Would someone know this exists and retrieve it later? | weak title, no navigation, missing synonyms or links |
| Authority | Is this the correct home for these claims? | duplicated policy, unclear owner, derived page presented as source |
| Consistency | Does it agree with relevant documentation? | conflicting procedures, terminology drift, unexplained scope differences |
| Maintainability | Can changes be made once and propagated safely? | volatile duplication, needless metadata, no lifecycle signal |
| Actionability | Can the reader act or decide with confidence? | no next step, no success criteria, unresolved ambiguity hidden as prose |
| Conformance | Does it satisfy applicable required custom rules? | wrong terminology, missing required structure, unreported exception |

## Review sequence

1. **Contract:** infer or identify audience, purpose, reader task, scope, and lifecycle.
2. **Custom rules:** identify applicable scope, separate required rules from preferences, and note conflicts or permitted exceptions.
3. **Evidence:** trace consequential claims to sources; label fact, assumption, decision, recommendation, hypothesis, and unknown correctly.
4. **Reader path:** follow the document in the order a target reader would use it.
5. **System impact:** search likely authoritative sources, contradictions, and duplication.
6. **Lifecycle:** inspect dates, status language, ownership, supersession, and volatile details.
7. **Economy:** remove content that does not support the reader outcome.

## Findings format

For each material finding, report:

```text
[severity] location — problem
Impact: what the intended reader or knowledge system cannot safely do
Evidence: source, contradiction, or observed gap
Recommendation: smallest change that resolves it
```

Use high severity for factual errors, unsafe instructions, controlling-source conflicts, or missing information that blocks the reader's core task. Separate verified defects from risks and optional improvements.
