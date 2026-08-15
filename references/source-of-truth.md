# Source of truth

## Rule

Every important piece of knowledge should ideally have one authoritative home. Other artifacts should point to that home or clearly state that they are derived snapshots.

Authority is claim-specific. A PRD may control product intent while an architecture document controls system design and a runbook controls the approved recovery procedure. “One source” does not mean “one giant document.”

## Identify authority

Evaluate:

1. explicit ownership or policy;
2. proximity to the system or decision it describes;
3. intended scope and audience;
4. verification against actual behavior;
5. recency and lifecycle status;
6. links from recognized indexes or governance pages.

Do not assume the newest, longest, or most polished page is authoritative.

## Handle secondary documents

Secondary pages may summarize context for a reader, but they should:

- link directly to the authoritative section;
- avoid copying volatile details;
- say when they are a point-in-time snapshot;
- name the scope of any intentional difference.

If duplication is necessary for offline use, access boundaries, compliance, or generated output, identify the source and update mechanism.

## Change authority deliberately

When moving the authoritative home:

1. update the new source;
2. mark the old source as moved, archived, or superseded rather than leaving a competing claim;
3. repair incoming links and navigation;
4. preserve history needed to explain past decisions;
5. record the ownership or policy change when material.
