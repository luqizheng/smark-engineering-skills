#!/usr/bin/env python3
"""Dependency-free structural validation for repository skills."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors: list[str] = []

if not SKILLS.is_dir():
    errors.append("missing skills/ directory")

for skill_file in sorted(SKILLS.glob("*/SKILL.md")) if SKILLS.exists() else []:
    skill_dir = skill_file.parent
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{skill_file.relative_to(ROOT)}: missing YAML frontmatter")
        continue
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{skill_file.relative_to(ROOT)}: unterminated frontmatter")
        continue
    frontmatter = text[4:end]
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.M)
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
    if not name:
        errors.append(f"{skill_file.relative_to(ROOT)}: missing/invalid name")
    elif name.group(1) != skill_dir.name:
        errors.append(f"{skill_file.relative_to(ROOT)}: name must match directory")
    if not description or len(description.group(1).strip()) < 20:
        errors.append(f"{skill_file.relative_to(ROOT)}: description missing or too short")
    if len(frontmatter) > 5000:
        errors.append(f"{skill_file.relative_to(ROOT)}: frontmatter exceeds 5000 characters")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("https://", "http://", "#", "mailto:")):
            continue
        resolved = (skill_file.parent / target.split("#", 1)[0]).resolve()
        if not resolved.exists():
            errors.append(f"{skill_file.relative_to(ROOT)}: broken local link {target}")

if not list(SKILLS.glob("*/SKILL.md")) if SKILLS.exists() else True:
    errors.append("no skills/*/SKILL.md files found")

if errors:
    print("Skill validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Skill validation passed.")
