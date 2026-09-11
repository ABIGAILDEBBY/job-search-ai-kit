"""Contract tests for the prompt and ignore-rule changes in PR #23."""

import re
import subprocess
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_repo_file(relative_path: str) -> str:
    """Return a repository file as UTF-8 text."""
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def section_between(text: str, start: str, end: str) -> str:
    """Extract a prompt section without relying on line numbers."""
    _, separator, remainder = text.partition(start)
    if not separator:
        raise AssertionError(f"Missing section start: {start!r}")

    section, separator, _ = remainder.partition(end)
    if not separator:
        raise AssertionError(f"Missing section end: {end!r}")
    return section


GHOST_JOB_SECTIONS = {
    "vet-job command": section_between(
        read_repo_file(".claude/commands/vet-job.md"),
        "## Step 2: Ghost job check",
        "## Step 3: Remote legitimacy check",
    ),
    "research-company command": section_between(
        read_repo_file(".claude/commands/research-company.md"),
        "## Check 1: Is the role actually real?",
        "## Check 2: Financial health",
    ),
    "plain-text vet-job prompt": section_between(
        read_repo_file("prompts/README.md"),
        "STEP 2: Ghost job check",
        "STEP 3: Remote legitimacy check",
    ),
}


SIGNAL_PATTERNS = {
    "posting age": r"30 days",
    "repeated reposting": (
        r"repost(?:ed|ing)?[^\n]*(?:multiple times|prior versions)"
    ),
    "role specificity": r"specific tools",
    "generic responsibilities": r"(?:generic|vague)[^\n]*any company",
    "organizational context": (
        r"(?:reports? to|team [^\n]*sits in)"
    ),
    "headcount and hiring mismatch": (
        r"(?:headcount[^\n]*shrinking|shrinking headcount)[^\n]*post"
    ),
    "recent hires": r"(?:recent hires|hired into this function recently)",
}


class GhostJobPromptTests(unittest.TestCase):
    """Verify the ghost-job contract across all three user entry points."""

    def test_checks_cover_all_seven_signal_categories(self):
        """Every user entry point should retain all seven evidence categories."""
        for name, section in GHOST_JOB_SECTIONS.items():
            for category, pattern in SIGNAL_PATTERNS.items():
                with self.subTest(source=name, category=category):
                    self.assertRegex(
                        section,
                        re.compile(pattern, re.IGNORECASE),
                        f"{name} is missing the {category!r} ghost-job signal",
                    )

    def test_checks_list_exactly_seven_signals(self):
        """Prevent accidental additions from changing the documented signal count."""
        for name, section in GHOST_JOB_SECTIONS.items():
            with self.subTest(source=name):
                signal_lines = re.findall(
                    r"^- (?:\*\*)?[^\n]+", section, re.MULTILINE
                )
                self.assertEqual(
                    len(signal_lines),
                    7,
                    f"{name} defines {len(signal_lines)} signal bullets",
                )

    def test_posting_age_signal_uses_the_30_day_boundary(self):
        """A 31-day-old inactive post must not fall through a legacy threshold."""
        for name, section in GHOST_JOB_SECTIONS.items():
            with self.subTest(source=name):
                self.assertRegex(
                    section,
                    re.compile(
                        r"(?:(?:older|more) than|over) 30 days", re.IGNORECASE
                    ),
                )
                self.assertRegex(
                    section, re.compile(r"no (?:repost|activity)", re.IGNORECASE)
                )
                self.assertNotRegex(
                    section,
                    re.compile(r"(?:60 days|6 weeks)", re.IGNORECASE),
                    f"{name} still contains a legacy age threshold",
                )

    def test_weak_indicators_are_not_counted_as_ghost_job_signals(self):
        """Missing salary or a named contact alone must not create a false positive."""
        weak_indicators = (
            r"no salary",
            r"no named (?:contact|hiring manager|recruiter)",
        )
        for name, section in GHOST_JOB_SECTIONS.items():
            for pattern in weak_indicators:
                with self.subTest(source=name, weak_indicator=pattern):
                    self.assertNotRegex(
                        section,
                        re.compile(pattern, re.IGNORECASE),
                        f"{name} reintroduced weak indicator {pattern!r}",
                    )

    def test_checks_define_positive_and_negative_results(self):
        """Prompts should produce an explicit count or an explicit clean result."""
        for name, section in GHOST_JOB_SECTIONS.items():
            with self.subTest(source=name):
                self.assertRegex(
                    section,
                    r'This (?:posting|role) shows \[X\] ghost job signals',
                    f"{name} is missing the counted-result format",
                )
                self.assertIn("No ghost job signals detected.", section)
                self.assertRegex(
                    section,
                    re.compile(
                        r"(?:explain|name).*signal.*triggered.*why.*matters",
                        re.IGNORECASE,
                    ),
                    f"{name} does not require an explanation for triggered signals",
                )


class GeneratedWritingRuleTests(unittest.TestCase):
    """Verify punctuation requirements in the changed writing commands."""

    def test_generated_writing_explicitly_disallows_em_dashes(self):
        """Both writing commands should state the same safe punctuation fallback."""
        commands = (
            (".claude/commands/cold-email.md", "output"),
            (".claude/commands/tailor-resume.md", "resume"),
        )
        for relative_path, output_scope in commands:
            with self.subTest(command=relative_path):
                text = read_repo_file(relative_path)
                expected_rule = (
                    f"Never use em dashes (— or --) anywhere in the {output_scope}. "
                    "Replace with commas, parentheses, or restructure the sentence"
                )
                self.assertIn(expected_rule, text)


def is_ignored(relative_path: str) -> bool:
    """Ask Git to evaluate a path using the repository's real ignore semantics."""
    result = subprocess.run(
        ["git", "check-ignore", "--no-index", "--quiet", "--", relative_path],
        cwd=REPO_ROOT,
        check=False,
    )
    if result.returncode not in (0, 1):
        raise AssertionError(
            f"git check-ignore failed for {relative_path!r} "
            f"with {result.returncode}"
        )
    return result.returncode == 0


class GitIgnoreContractTests(unittest.TestCase):
    """Verify the user-data protections added to .gitignore."""

    def test_personal_and_generated_files_are_ignored(self):
        """Files likely to contain a job seeker's private data must stay untracked."""
        protected_paths = (
            "CLAUDE.md",
            "CLAUDE.md.backup",
            "build_resume_candidate.py",
            "resume/tailored/acme-data-engineer.docx",
            "jobs/acme-data-engineer.md",
            ".claude/projects/local-session.json",
            "assets/headshot.png",
        )
        for relative_path in protected_paths:
            with self.subTest(path=relative_path):
                self.assertTrue(is_ignored(relative_path))

    def test_ignore_rules_do_not_hide_nearby_repository_files(self):
        """Nearby source and placeholder files must stay visible."""
        visible_paths = (
            "build_resume.py",
            "resume/base-resume.md",
            ".claude/commands/vet-job.md",
            "applications/tracker.md",
            "reports/.gitkeep",
        )
        for relative_path in visible_paths:
            with self.subTest(path=relative_path):
                self.assertFalse(is_ignored(relative_path))


if __name__ == "__main__":
    unittest.main()
