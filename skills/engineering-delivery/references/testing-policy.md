# Testing and Verification Policy

## Test design

For each behavior change, identify:

- Primary success-path behavior.
- Invalid input and boundary values.
- Authorization denial and isolation failures.
- Retry, duplicate delivery, idempotency, and replay behavior.
- Concurrency and transaction behavior.
- Timeout, cancellation, process crash, dependency outage, and recovery.
- Backward compatibility and migration behavior where applicable.

Use the smallest deterministic test that proves the behavior, then run broader suites as time permits.

## Test quality

- Prefer observable outcomes and contract-level assertions.
- Avoid tests that merely mirror private implementation details.
- Where a defect is security-sensitive or concurrency-related, consider mutation testing or a counterfactual check: demonstrate that the test fails when the protection is removed.
- Do not weaken assertions, skip failing tests, or change expected behavior solely to obtain green CI.
- Record skipped tests, flaky tests, unavailable dependencies, and environment limitations.

## Verification record

For every check, capture:

- Exact command or CI workflow/run identifier.
- Commit SHA tested.
- Exit status and pass/fail/skip counts when available.
- Relevant failure output.
- Whether the result is local, CI, staging, or production evidence.

A green result on an old commit does not verify the current head. A passing suite does not prove untested properties.
