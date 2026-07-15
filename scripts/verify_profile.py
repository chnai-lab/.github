from pathlib import Path


REQUIRED_FILES = [
    "profile/README.md",
    "CONTRIBUTING.md",
    "PULL_REQUEST_TEMPLATE.md",
    "AGENTS.md",
    "SECURITY.md",
    "docs/AI_AGENT_WORKFLOW.md",
    "docs/MEMBER_ONBOARDING.md",
    "ISSUE_TEMPLATE/bug-report.yml",
    "ISSUE_TEMPLATE/feature.yml",
    "ISSUE_TEMPLATE/task.yml",
]

REQUIRED_PROFILE_TERMS = [
    "CHNAI LAB",
    "student-run product studio",
    "AI-native",
    "BayonHub",
    "Svaeng Yul",
    "Chomkar",
    "Sat Digital",
    "Vantrex",
    "PHSAROS",
    "private",
    "AI-Native Team Starter",
]

REQUIRED_AGENT_TERMS = [
    "secrets",
    "verification",
    "pull request",
    "main",
    "Standard Agent Prompt",
]

REQUIRED_WORKFLOW_TERMS = [
    "Session Start Protocol",
    "Pull Request Protocol",
    "Review Protocol",
    "Handoff Template",
    "Security Rules",
]

PLACEHOLDER_MARKERS = [
    "TODO",
    "FIXME",
    "TBD",
    "example.com",
    "your-org",
    "your-repo",
]


def read(path: str) -> str:
    file_path = Path(path)
    if not file_path.is_file():
        raise SystemExit(f"Missing required file: {path}")
    text = file_path.read_text(encoding="utf-8")
    if not text.strip():
        raise SystemExit(f"Required file is empty: {path}")
    return text


def ensure_terms(path: str, terms: list[str]) -> None:
    text = read(path)
    missing = [term for term in terms if term not in text]
    if missing:
        raise SystemExit(f"{path} is missing required terms: {', '.join(missing)}")


def ensure_no_placeholders() -> None:
    for path in REQUIRED_FILES:
        text = read(path)
        for marker in PLACEHOLDER_MARKERS:
            if marker in text:
                raise SystemExit(f"{path} contains unresolved marker: {marker}")


def main() -> None:
    for path in REQUIRED_FILES:
        read(path)
    ensure_terms("profile/README.md", REQUIRED_PROFILE_TERMS)
    ensure_terms("AGENTS.md", REQUIRED_AGENT_TERMS)
    ensure_terms("docs/AI_AGENT_WORKFLOW.md", REQUIRED_WORKFLOW_TERMS)
    ensure_no_placeholders()


if __name__ == "__main__":
    main()
