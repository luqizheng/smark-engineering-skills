# Security and Authorization Boundaries

This skill does not confer authority. It must operate within the user's explicit request, repository policy, tool permissions, and applicable organizational controls.

## Hard stops requiring explicit human authorization

Stop the affected action (but continue unrelated safe work) before:

- Production deployment, production migration, or destructive data change.
- Deleting or rewriting shared history, force-pushing, or merging a PR.
- Creating, exposing, rotating, or revoking credentials, keys, certificates, or trust roots.
- Expanding a service account, token scope, role, permission, network boundary, or data access.
- Disabling authentication, authorization, validation, audit, isolation, or fail-closed behavior.
- Approving requirements, designs, security exceptions, compliance attestations, or release gates.
- Accessing data or systems outside the explicitly authorized project/scope.

## Secrets and sensitive data

- Never print, copy into documentation, commit, or paste secrets into issue/PR comments.
- If a credential is found in tracked history, do not assume deleting the current file is sufficient. Record the exposure location without reproducing the value; notify the credential owner and recommend rotation/revocation and history remediation.
- Do not perform rotation or revocation unless explicitly authorized by the credential owner.
- Use placeholders in tests and examples. Ensure logs redact tokens, authorization headers, private keys, and sensitive identifiers.

## Authorization review checklist

For delegated or cross-service operations, verify from implementation and tests:

- Issuer, audience, subject, tenant, project, actor type, action, and expiry are validated as intended.
- Identifier types and mappings are consistent across services.
- Request/resource binding prevents a valid credential from being replayed against a different operation.
- Replay prevention is atomic under concurrency and defines safe retry semantics.
- Key discovery and trust-root distribution are authenticated and fail closed.
- Algorithms and key IDs are explicitly constrained; unknown keys and unavailable trust material fail closed.
- Time validation covers expiry, not-before, issued-at future skew, maximum age, and maximum lifetime.
- Authorization decisions are enforced at the resource boundary, not inferred from caller-supplied headers.
- Audit records are useful without leaking secrets.
- Negative, cross-tenant, cross-project, and concurrency tests exercise the actual enforcement path.

Do not mark a security issue resolved because a design document describes the intended control. Verify the code path and tests.

## Findings severity

Use the repository's severity convention where defined. Otherwise:

- **P0 / Critical**: exploitable authorization bypass, cross-tenant access, credential compromise, destructive data loss, or equivalent release blocker.
- **P1 / High**: material security/correctness defect with bounded exploitability or significant operational impact.
- **P2 / Moderate**: meaningful weakness, missing defense/test, or reliability issue without immediate critical impact.
- **P3 / Low**: minor hardening, clarity, or maintainability concern.

Explain evidence, impact, preconditions, and remediation. Do not inflate or downgrade severity for convenience.
