# Runbooks and operating procedures

A runbook enables a qualified operator to act safely under real conditions. Optimize for scanning, verification, and recovery.

## Adapt this structure

1. **Purpose and trigger** — when to use and when not to use it.
2. **Prerequisites and permissions** — access, tools, approvals, system state.
3. **Risk and safety notes** — data loss, customer impact, security, irreversible steps.
4. **Procedure** — ordered actions with concrete inputs.
5. **Verification** — observable result after important steps and at completion.
6. **Failure handling** — stop conditions, rollback, retry constraints, escalation.
7. **Communication** — affected parties, status updates, incident linkage when needed.
8. **Ownership and lifecycle** — maintainer and last verification when operational drift is likely.

Do not hide prerequisites inside steps or rely on screenshots alone. Prefer commands that are safe to copy, but never include live secrets. Separate routine operation from incident diagnosis when their reader states differ.

## Quality checks

- Can an operator identify the correct starting condition quickly?
- Are destructive steps unmistakable and recoverable where possible?
- Does every critical action have a success or failure signal?
- Is escalation possible without undocumented personal knowledge?
- Has the procedure been verified against the actual environment recently enough for its risk?
