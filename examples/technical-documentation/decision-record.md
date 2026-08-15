# Example decision: Keep one authoritative deployment lifecycle

**Status:** Accepted<br>
**Date:** 2026-08-15

## Context

The fictional knowledge base described production delivery in architecture, onboarding, setup, and runbook pages. Each copy used different language and changed on a different schedule, so readers could not determine current behavior.

## Decision

Make `systems/delivery.md` authoritative for lifecycle behavior. Keep executable operator steps in `runbooks/release.md` and rationale in decision records. Other pages link to the relevant section and may include only stable framing needed by their audience.

## Alternatives

- **Synchronize every copy:** rejected because manual synchronization is the failure mode.
- **Put behavior and procedures in one page:** rejected because system explanation and incident-time operation have different reader tasks and update patterns.
- **Generate every page from shared fragments:** deferred because current scale does not justify a generation pipeline.

## Consequences

Readers have a clear current source and a separate operational path. Changes may require updates to both lifecycle and runbook pages when behavior and procedure change together, but duplicated explanatory text is removed. Existing incoming links must be repaired during consolidation.
