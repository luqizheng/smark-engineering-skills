# smark-engineering-skills

Reusable, repository-independent engineering skills for AI coding agents.

The canonical skill source is agent-neutral and lives under `skills/`. The first skill is **Engineering Delivery**, a disciplined workflow for maximizing verified engineering output in a bounded session without weakening correctness, security, or human-approval boundaries.

## Included

- `skills/engineering-delivery/` — core skill entrypoint, references, and execution templates.
- `docs/installation.md` — install guidance for Codex, Claude Code, and other Agent Skills-compatible tools.
- `docs/validation-case-wp-lmms-delegation-01.md` — first real-world validation case.
- `scripts/validate_skill.py` — dependency-free structural and local-link validation.
- `.github/workflows/validate-skills.yml` — pull-request and main-branch validation.

## Design principles

- Inspect actual repository state and source code before trusting plans or reports.
- Prefer verified implementation over advice-only output.
- Batch related work and minimize status chatter in time- or token-constrained sessions.
- Continue safe, independent work when one item is blocked.
- Treat tests, CI, design review, security review, and human approval as distinct evidence.
- Never cross authorization boundaries or perform destructive/production actions without explicit authorization.

## Use

Read [the installation guide](docs/installation.md), then install the complete `skills/engineering-delivery/` directory in the agent's documented skill-discovery location.

Pin a reviewed commit or release tag for reproducible use. Installing a skill does not grant permissions.

## Development

Make changes on a topic branch and submit a pull request. The initial repository bootstrap commit is the only expected direct commit to `main` while the GitHub repository has no existing commit; substantive work belongs on topic branches.

Run:

```bash
python scripts/validate_skill.py
```

A passing structural check does not prove the skill's operational effectiveness or authorize a merge/release.
