# Execution Policy

## Evidence hierarchy

Prefer evidence in this order, while recognizing that different evidence answers different questions:

1. Current source code and executable configuration.
2. Reproducible tests and command output.
3. Git history and reviewed diffs.
4. Authoritative CI and deployment records.
5. Architecture/contract documents that match the current implementation.
6. Issues, plans, prior reports, and conversation summaries.

A document may define intended behavior, but it does not prove the implementation enforces it. A passing test proves only the behavior covered by that test.

## Work classification

For every work item, record:

- Expected outcome and acceptance evidence.
- Files/components likely affected.
- Dependencies and blockers.
- Risk: low, medium, high, or critical.
- Whether explicit approval is required.
- Verification method.

## Default execution policy

| Action | Default |
|---|---|
| Read repository files, history, issues, PRs, CI | Allowed when access is available |
| Edit local working branch, add tests/docs | Allowed within requested scope |
| Create topic branch | Allowed when needed and supported |
| Push branch / create Draft PR | Allowed when user requested execution and repository permissions permit |
| Change public API or persisted schema | Implement only within clear scope; document compatibility and migration |
| Modify sibling/upstream/downstream repositories | Not allowed unless explicitly in scope |
| Merge PR, publish release, deploy production | Explicit approval required |
| Destructive migration, data deletion, force push | Explicit approval required |
| Rotate/revoke credentials or change identity trust roots | Credential/authority owner approval required |
| Expand permissions, disable controls, fail open | Prohibited as a workaround |

## Session efficiency

- Prefer one coherent PR per work package; do not create many tiny PRs without a review or ownership reason.
- Parallelize independent read-only inspections and tests when safe.
- Serialize writes to the same branch/file to avoid races.
- Do not retry a failed mutation blindly. Inspect current remote state first.
- Preserve user work and report any environmental limitation precisely.
