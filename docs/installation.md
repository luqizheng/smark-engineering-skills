# Installing Skills

The canonical, agent-neutral source of truth is `skills/<skill-name>/`. Keep the skill content independent of a specific model, vendor, IDE, or orchestration runtime.

## Codex

For a repository-local Codex installation, copy or link the selected skill directory into the repository's `.agents/skills/` directory:

```text
.agents/skills/engineering-delivery/
```

For a user-wide installation, use the user-level skills directory supported by the installed Codex version. Confirm the current Codex documentation for the exact path and discovery behavior.

## Claude Code

For a repository-local Claude Code installation, copy or link the selected skill directory into:

```text
.claude/skills/engineering-delivery/
```

## Other Agent Skills-compatible tools

Use the tool's documented skill discovery directory. Copy the complete skill directory, preserving `SKILL.md`, `references/`, and `templates/`.

## Version pinning

For reproducible use, pin this repository to a reviewed Git commit or release tag. Avoid silently tracking a moving default branch in production or security-sensitive workflows.

## Safety

Installing a skill does not grant repository, shell, network, cloud, or production permissions. The agent's actual tool permissions and the user's approvals remain the authority boundary.
