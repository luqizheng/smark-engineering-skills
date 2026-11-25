# Validation Case: WP-LMMS-DELEGATION-01

## Purpose

Use the cross-service delegation work package as the first realistic validation case for the Engineering Delivery skill. This is a workflow validation record, not a claim that the underlying implementation or security design has passed review.

## What the skill must demonstrate

1. Inspect the original AI-PM, Artifact Service, and LMMS source before accepting inherited audit conclusions.
2. Trace token issuance, trust-root distribution, verification, tenant/project mapping, action authorization, request binding, replay handling, and audit behavior.
3. Distinguish contract defects from implementation defects and identify the owning repository for each.
4. Preserve hard security gates: no secret disclosure, no unauthorized credential rotation, no production migration, no enabling protected generation paths, and no cross-repository edits outside scope.
5. Produce concrete findings with severity, source evidence, impact, remediation, and regression-test expectations.
6. Keep implementation blocked where unresolved P0 authorization issues make implementation unsafe; continue safe documentation and test-planning work.
7. Prepare a second independent review rather than treating a green CI run or a completed draft as approval.

## Known review lessons to retain

- A tenant identifier's representation and mapping must be explicit across service boundaries; similarly named fields are not proof of compatible types.
- A short-lived bearer token is not inherently bound to one request. Define request/resource binding, atomic replay semantics, and safe retry behavior.
- JWKS transport and key distribution require an authenticated trust root; private network reachability alone is not sufficient.
- Time validation must define future-issued-at skew, maximum age/lifetime, expiry, not-before, and allowed signing algorithms.
- Resource headers may locate a resource or support consistency checks; they must not become authorization evidence by themselves.
- A security contract must match the actual domain model, including required identifiers and actor types.

## Acceptance

The skill is effective only if an agent can reproduce these checks from source, preserve the explicit scope/approval boundaries, and produce an evidence-based disposition. This document does not embed live credentials, authorize code changes in LMMS, or declare the work package complete.
