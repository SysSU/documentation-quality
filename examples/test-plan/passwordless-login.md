# Example test plan: Passwordless sign-in recovery

> Fictional example paired with the example PRD. It demonstrates strategy, not a complete case inventory.

**Objective:** Establish release confidence that eligible users can recover access without creating unacceptable account-takeover, privacy, or operational risk.

## Quality risks

| Priority | Risk | Evidence needed |
| --- | --- | --- |
| Critical | Attacker recovers or enumerates another user's account | Abuse, rate-limit, identity, and response-equivalence results |
| High | Valid user becomes locked out or loops indefinitely | State-transition and recovery-path results across supported factors |
| High | Recovery leaves old challenges or sessions active contrary to policy | Challenge/session invalidation assertions and audit events |
| Medium | Support cannot diagnose failures safely | Observability and support-workflow review |
| Medium | Flow is unusable with keyboard or screen reader | Accessibility checks on every user-visible state |

## Scope

In scope: eligibility response, challenge lifecycle, supported recovery factors, cross-device completion, expiry, cancellation, rate limits, notifications, audit trail, session policy, accessibility, and regression of normal sign-in.

Out of scope: organization-admin recovery and factors not approved for initial rollout. Penetration testing execution is owned by Security but its result is an exit dependency.

## Assumptions and dependencies

- **Assumption:** The approved assurance level and session policy are available before final execution.
- Identity, notification, audit, and abuse-control test environments must be reachable.
- Product supplies the supported-browser and assistive-technology matrix.
- Legal/privacy confirms test-data and notification constraints.

## Environments and data

Use an integration environment with production-equivalent identity state transitions and isolated notification sinks. Cover accounts with zero, one, and multiple verified factors; locked, disabled, and deleted accounts; expired and reused challenges; regional profiles; and boundary attempt counts. Use synthetic identities only. Reset challenge and rate-limit state between tests.

Known environment gap: production delivery latency and provider throttling are not faithfully reproduced; monitor both during staged rollout.

## Coverage strategy

- **Contract and component:** eligibility response invariants, challenge creation/expiry/single use, rate-limit boundaries, audit schema.
- **Integration:** identity, notification, session invalidation, abuse scoring, and support-safe status.
- **End-to-end:** eligible and ineligible paths, cross-device completion, cancellation, retry after expiry, unavailable dependency, and degraded notification delivery.
- **Negative and abuse:** account enumeration comparisons, replay, guessed identifiers, concurrent challenges, factor changes during recovery, and repeated failures across identifiers and networks.
- **Regression:** normal sign-in, password reset, account lock, and support-assisted recovery.
- **Accessibility:** keyboard order, focus restoration, error association, status announcements, time-limit accommodation, and contrast for every state.
- **Operational:** logs omit secrets, metrics distinguish causes, alerts fire on abuse and failure-rate thresholds, kill switch and rollback are rehearsed.

Detailed cases live in the test-management system; this plan controls selection and release evidence.

## Observability and oracles

Judge user-visible outcomes against approved requirements and identity state against service invariants. Correlate audit events without storing challenge secrets. Dashboards must expose attempt, completion, abandonment, error, notification, rate-limit, support-contact, and suspected-abuse rates by rollout cohort.

## Entry criteria

- PRD requirements and security policies are approved.
- Supported factors and matrices are fixed for the candidate.
- Critical integrations, synthetic data, monitoring, kill switch, and rollback path are ready.

## Exit criteria

- No open critical or high defects; any exception requires named product and security acceptance.
- Every critical/high risk has reviewed evidence from the planned coverage.
- Security assessment, accessibility review, observability check, and rollback rehearsal are complete.
- Known environment gaps have staged-rollout monitors and owners.

## Ownership

QA owns plan coordination and evidence reporting; engineering owns component/integration automation and defect fixes; Security owns abuse assessment and risk acceptance; Product owns requirement acceptance and rollout decision; Operations owns dashboards and rollback readiness.
