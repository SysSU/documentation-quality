# Technical design and architecture

A design document enables an informed technical decision and later explains the resulting system. Match detail to the decision's scope.

## Adapt this structure

1. **Context and problem** — current system, driving change, stakeholders.
2. **Requirements and constraints** — functional needs, quality attributes, policy, budget, compatibility.
3. **Proposed architecture** — components, responsibilities, boundaries, and deployment shape.
4. **Data and control flows** — normal path, state changes, trust boundaries, asynchronous behavior.
5. **Interfaces and data contracts** — APIs, events, schemas, compatibility, ownership.
6. **Alternatives and tradeoffs** — credible options, decision criteria, why rejected.
7. **Failure modes and recovery** — timeouts, partial failure, retry behavior, degradation, rollback.
8. **Operations** — observability, capacity, support, cost, deployment, and runbooks.
9. **Security and privacy** — threats, access, secrets, sensitive data, retention, audit.
10. **Migration and validation** — stages, coexistence, backfill, verification, rollback.
11. **Unresolved decisions** — material unknowns, owners, and decision deadlines when known.

Use diagrams only when relationships or flows are clearer visually; accompany them with text for accessibility and retrieval.

## Quality checks

- Can a reviewer trace design choices to requirements and constraints?
- Are component ownership and interfaces unambiguous?
- Do failure behavior and operational burden receive the same attention as the happy path?
- Are alternatives real rather than straw men?
- Are changing facts linked to authoritative references instead of frozen into the design?
