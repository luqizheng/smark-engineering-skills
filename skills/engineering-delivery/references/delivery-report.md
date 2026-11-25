# Delivery Report Format

## Disposition
One of:
- READY FOR INDEPENDENT REVIEW
- CHANGES REQUIRED
- BLOCKED

This is an engineering handoff status, not approval to merge or release.

## Repository state
- Repository:
- Base branch / base SHA:
- Working branch / head SHA:
- Working tree:
- PR:
- CI status and exact head SHA:

## Outcomes
| Work item | Status | Evidence |
|---|---|---|
| | Completed / Partial / Blocked / Not attempted | |

## Changes
Summarize behavior and contract changes, key files, migrations, and operational implications.

## Verification
| Check | Command / run | Result | Commit SHA |
|---|---|---|---|
| | | | |

## Findings and residual risks
List P0/P1/P2/P3 findings with evidence, impact, and next action. State explicitly when none were found within the inspected scope; do not imply a whole-system audit if only a subset was examined.

## Human decisions required
List only decisions that genuinely require the user's authority, with the exact choice and consequence.

## Next steps
Give the smallest actionable sequence. Identify any operation intentionally not performed due to approval or safety boundaries.
