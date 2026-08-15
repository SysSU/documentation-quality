# Example PRD: Passwordless sign-in recovery

> Fictional example. Assumptions and open questions are intentionally visible.

**Status:** Draft<br>
**Audience:** Product, design, security, support, and engineering<br>
**Reader outcome:** Decide whether the team has enough evidence and scope clarity to design and estimate the feature.

## Problem

Customers who lose access to their password cannot regain access without a support-assisted reset. Support tickets describe delays and identity-verification friction.

**Evidence:** A real PRD would link the ticket analysis and interview notes here. No source data was supplied for this example, so volume and severity are unknown.

## Goals and success criteria

- Eligible customers can regain access without support while meeting the approved account-recovery assurance level.
- Measure recovery completion, abandonment, support contacts after a recovery attempt, and confirmed account-takeover incidents.
- Targets are **TBD** until baseline data and security thresholds are supplied.

## Non-goals

- Replacing normal password sign-in.
- Recovering accounts that have no verified recovery factor.
- Changing organization-admin recovery policy.

## Users and use cases

- A returning customer has access to a verified recovery factor but not the password.
- A customer starts recovery on one device and completes verification on another.
- Support needs to identify a failed self-service attempt without seeing secret verification data.

## Requirements

1. The experience must disclose eligibility without exposing whether an arbitrary account exists.
2. Recovery must use a security-approved verified factor.
3. Verification attempts must be rate-limited and auditable.
4. Success must invalidate active recovery challenges and follow the approved session policy.
5. Users must receive an account-change notification through an independent available channel when policy requires it.
6. The flow must support keyboard and screen-reader operation.

## Constraints and dependencies

- **Dependency:** Security must define the required assurance level and abuse controls.
- **Dependency:** Identity service must expose challenge state and invalidation behavior.
- **Assumption:** At least one verified factor is available for the target population.
- **Unknown:** Regional notification and retention requirements.

## Experience notes

Design must cover ineligible accounts, expired challenges, rate limits, unavailable factors, cross-device completion, cancellation, and post-recovery sign-in. Detailed interaction design belongs in the linked design artifact, not this PRD.

## Risks

| Risk | Mitigation direction |
| --- | --- |
| Account enumeration | Consistent external responses and abuse monitoring |
| Recovery-factor compromise | Assurance-level review, notifications, session controls |
| Support confusion | Expose safe attempt status and documented escalation |
| Accessibility regression | Include assistive-technology checks in acceptance and test strategy |

## Rollout considerations

Begin with internal accounts, then a small eligible cohort with monitoring and a kill switch. Expansion criteria and rollback thresholds are open pending baselines.

## Open questions

- Which factors satisfy the required assurance level? **Owner: Security**
- What is the baseline support-contact rate? **Owner: Support analytics**
- Which session invalidation policy applies? **Owner: Identity product**
- Which markets have notification constraints? **Owner: Legal/privacy**
