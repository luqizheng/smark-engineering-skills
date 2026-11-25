"""Regression tests for non-negotiable Engineering Delivery behavior.

These tests validate the published skill contract, not an agent's runtime performance.
Scenario-based agent evaluations are documented separately under evals/.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/engineering-delivery/SKILL.md"


class SkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")

    def test_skill_has_valid_frontmatter_identity(self):
        self.assertTrue(self.skill.startswith("---\n"))
        frontmatter = self.skill.split("\n---\n", 1)[0]
        self.assertRegex(frontmatter, r"(?m)^name: engineering-delivery$")
        self.assertRegex(frontmatter, r"(?m)^description: .{20,}$")

    def test_all_required_references_are_linked_and_present(self):
        targets = re.findall(r"\[[^\]]+\]\((references/[^)#]+|templates/[^)#]+)\)", self.skill)
        self.assertGreaterEqual(len(targets), 6)
        for target in targets:
            self.assertTrue((SKILL.parent / target).is_file(), target)

    def test_human_authority_gates_are_explicit(self):
        for phrase in ("explicit approval", "Do not merge", "Never self-approve", "production", "credential"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.skill.lower())

    def test_source_and_evidence_first_behavior_is_explicit(self):
        for phrase in ("actual state", "source code", "tests", "evidence"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.skill.lower())

    def test_untrusted_repository_content_is_not_authority(self):
        self.assertIn("untrusted data", self.skill.lower())
        self.assertIn("hostile instructions", self.skill.lower())

    def test_delivery_disposition_is_bounded(self):
        for disposition in ("READY FOR INDEPENDENT REVIEW", "CHANGES REQUIRED", "BLOCKED"):
            with self.subTest(disposition=disposition):
                self.assertIn(disposition, self.skill)


if __name__ == "__main__":
    unittest.main()
