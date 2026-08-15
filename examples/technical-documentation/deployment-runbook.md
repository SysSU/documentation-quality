# Example runbook: Pause production promotion

> Fictional example. Replace systems, commands, thresholds, and escalation contacts with verified local sources before use.

## When to use

Use when an automatically started deployment has reached staging checks but production promotion must not proceed because a release check failed or evidence is inconclusive.

Do not use after production promotion has begun; follow the rollback runbook instead.

## Prerequisites

- You are the assigned on-call release approver.
- You have access to the delivery dashboard and incident channel.
- You have the deployment ID from the release event.

## Safety

Pausing is safe and leaves the current production version serving traffic. Do not cancel or delete the deployment: cancellation may discard evidence needed for diagnosis.

## Procedure

1. Open the deployment in the delivery dashboard using its ID.
2. Confirm the state is `AWAITING_PRODUCTION_APPROVAL`.
   - If promotion already started, stop and use the rollback runbook.
   - If the state differs for another reason, stop and escalate to Delivery Operations.
3. Select **Pause promotion** and record the failing check or uncertainty in the reason field.
4. Confirm the dashboard shows `PROMOTION_PAUSED` and the production version is unchanged.
5. Post the deployment ID, failed check, pause time, and investigation owner in the release incident channel. Do not paste secrets or customer data.

## Recovery

After the failing check is resolved, rerun the required staging checks. Approve production promotion only when every required check passes and the investigation owner has cleared the pause. If the deployment expires, start a new release; do not bypass expiry.

## Escalation

Escalate immediately if production version changes while paused, audit events are missing, or the dashboard state conflicts with observed traffic. Use the current Delivery Operations contact in the service directory rather than copying a person's name here.

## Verification record

This example intentionally has no “last verified” date because it is fictional. A real high-risk runbook should name its owner and last successful exercise or verification.
