# Independent Code and Architecture Audit Checklist

## Repository and change integrity
- Confirm repository identity, branch, base/head SHAs, clean/dirty state, and changed-file list.
- Inspect the complete diff and relevant surrounding code.
- Check for unrelated changes, generated files, accidental secrets, and dependency drift.
- Compare implementation with current contracts and repository-specific instructions.

## Architecture and contracts
- Identify ownership boundaries and authoritative data stores.
- Trace the full request/event path from entry point to persistence and side effects.
- Check tenant/project/resource scoping and cross-boundary calls.
- Check compatibility, versioning, error semantics, idempotency, retries, timeouts, and cancellation.
- Review schema changes, indexes, constraints, migration ordering, rollback, and data backfill.
- Identify hidden coupling, duplicated sources of truth, and undocumented assumptions.

## Correctness and lifecycle
- Check state transitions, invalid transitions, terminal states, and recovery.
- Check concurrency, races, locking, transaction boundaries, and lost updates.
- Check process/task cancellation, shutdown, disposal, orphan cleanup, and crash recovery.
- Check resource limits, backpressure, timeouts, and failure propagation.
- Check observability and whether logs/metrics allow diagnosis without leaking sensitive data.

## Security
- Apply [security-boundaries.md](security-boundaries.md).
- Inspect actual enforcement points, not just DTOs or middleware declarations.
- Attempt negative paths and boundary conditions.
- Verify least privilege and fail-closed behavior.

## Tests and evidence
- Determine whether tests assert externally observable outcomes or only implementation details.
- Look for missing negative, boundary, concurrency, isolation, and failure-path tests.
- Check whether tests can pass when the defect remains (mutation-oriented reasoning).
- Re-run relevant tests and inspect the exact output and exit code.
- Verify CI refers to the current PR head, not an earlier commit.

## Audit result
For each finding include: ID, severity, file/symbol/line, evidence, impact, reproduction/precondition, required fix, and regression test. Distinguish confirmed defects from risks and unanswered questions.
