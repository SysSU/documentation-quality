# Test plans

A test plan communicates a risk-based strategy for obtaining confidence. It is not merely a long inventory of test cases.

## Adapt this structure

1. **Objective and quality risks** — what confidence is needed and what failure would matter most.
2. **Scope and exclusions** — included behavior, integrations, platforms, and explicit gaps.
3. **Assumptions and dependencies** — build state, services, access, tooling, and upstream readiness.
4. **Environments and configurations** — relevant versions, devices, topology, feature flags, and production differences.
5. **Test data** — sources, privacy, reset/repeatability, boundary values, and destructive-data controls.
6. **Coverage strategy** — functional, integration, negative, edge, regression, performance, security, accessibility, compatibility, migration, or resilience as risk requires.
7. **Observability and oracles** — how results are judged; logs, metrics, traces, events, and expected invariants.
8. **Execution and ownership** — responsibilities, sequence, tooling, triage, and result reporting.
9. **Entry and exit criteria** — evidence-based thresholds, accepted residual risk, and waiver authority.
10. **Known gaps and contingencies** — what remains untested, why, impact, and follow-up.

## Select depth by risk

Map important risks to test approaches and evidence. Cover happy paths, invalid input, unavailable dependencies, partial failure, permissions, retries, idempotency, concurrency, boundaries, recovery, and regression where applicable. Do not add every test category mechanically.

## Keep plan and cases distinct

Link detailed cases or automation suites when they exist. The plan should explain why the selected coverage is sufficient, how environments and data support it, and what evidence permits release.

## Quality checks

- Does scope align with requirements and changed behavior?
- Can each high-impact risk be traced to coverage and an oracle?
- Are environment gaps and production-only risks visible?
- Are exit criteria decisions rather than slogans such as “all tests pass”?
- Is ownership clear for execution, defects, waivers, and final sign-off?
