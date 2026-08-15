# Example: Consolidating deployment knowledge

## Incoming information

> Production deployments now start automatically after a merge to `main`. An on-call engineer must still approve promotion after staging checks.

## Search

Search terms: `deployment`, `production`, `release`, `main`, `merge`, `automatic`, `manual`, `approval`, `promotion`.

Results in this fictional knowledge base:

| Document | Existing claim | Authority signal |
| --- | --- | --- |
| `systems/delivery.md` | “Production promotion is manually started.” | Named system owner; linked from system index |
| `runbooks/release.md` | Procedure begins with “click Start deployment” | Current operator procedure |
| `projects/automation-plan.md` | Automatic start is a planned milestone | Dated project plan |
| `onboarding.md` | “Releases are manual.” | Unsourced summary |
| `decisions/004-auto-start.md` | Accepted decision to automate start | Accepted, effective next release |

## Assessment

The new statement contradicts the current system and runbook text, but the accepted decision and supplied change show that it is a lifecycle transition, not four equally authoritative opinions.

Authoritative homes by claim:

- Current delivery behavior: `systems/delivery.md`
- Operator procedure: `runbooks/release.md`
- Rationale/history: `decisions/004-auto-start.md`
- Temporary execution tracking: `projects/automation-plan.md`

## Recommended update

1. Verify the change is live; if not, keep current behavior and add the effective condition to the decision/plan.
2. Update `systems/delivery.md` to distinguish automatic deployment start from manual production promotion.
3. Replace the runbook's start step with how to observe staging checks and approve or reject promotion.
4. Mark the project milestone complete or link its status to the delivery source.
5. Replace the onboarding summary with a link: “See Delivery lifecycle,” avoiding another volatile copy.
6. Search incoming links to the old runbook section and repair them.

## Resulting authoritative statement

```md
## Production delivery

Merging to `main` starts a deployment and runs staging checks automatically.
Production promotion remains paused until the on-call engineer reviews the
checks and approves it using the [release runbook](../runbooks/release.md).

This behavior implements [Decision 004](../decisions/004-auto-start.md).
```

No new document is created.
