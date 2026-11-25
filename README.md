# smark-engineering-skills

Reusable, repository-independent engineering skills for AI coding agents.

This repository starts with **Engineering Delivery**: a disciplined workflow for maximizing useful engineering output in a bounded session without weakening correctness, security, or human-approval boundaries.

## Status

The repository is being initialized. The first deliverable is tracked in [WP-SKILL-01](https://github.com/luqizheng/smark-engineering-skills).

## Design principles

- Inspect the actual repository state and source code before trusting plans or reports.
- Prefer verified implementation over advice-only output.
- Batch related work and minimize status chatter, especially in time- or token-constrained sessions.
- Continue safe, independent work when one item is blocked.
- Treat tests, CI, design review, security review, and human approval as distinct evidence.
- Never cross authorization boundaries or perform destructive/production actions without explicit authorization.

## Layout

The portable skill source lives under `skills/`. Agent-specific installation locations are generated or documented separately; the skill itself must not depend on a particular agent runtime.

## Contributing

Changes should be made on a topic branch and reviewed through a pull request. Do not merge a pull request merely because CI is green.
