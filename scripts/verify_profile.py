import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "profile/README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "PULL_REQUEST_TEMPLATE.md",
    "SECURITY.md",
    "docs/AI_AGENT_WORKFLOW.md",
    "docs/AI_CONCIERGE_STANDARD.md",
    "docs/MEMBER_ONBOARDING.md",
    "docs/REPOSITORY_STANDARD.md",
    ".github/CODEOWNERS",
    ".github/copilot-instructions.md",
    ".github/dependabot.yml",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/decision.yml",
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/ISSUE_TEMPLATE/task.yml",
    ".github/workflows/profile-checks.yml",
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
    "GOVERNANCE.md",
    "REPOSITORY_STANDARD.md",
]

REQUIRED_AGENT_TERMS = [
    "Human And Agent Contract",
    "Required Start",
    "Risk Stop Gate",
    "Communication Standard",
    "secrets",
    "verification",
    "pull request",
    "main",
    "Standard Agent Prompt",
]

REQUIRED_WORKFLOW_TERMS = [
    "Delivery Framework",
    "Traceability Chain",
    "Session Start Protocol",
    "Risk Gate",
    "Work State Machine",
    "Pull Request Protocol",
    "Evidence Standard",
    "Review Protocol",
    "Handoff Template",
    "Security Rules",
    "R0",
    "R1",
    "R2",
    "R3",
]

REQUIRED_GOVERNANCE_TERMS = [
    "System Of Record",
    "Access Lifecycle",
    "Product Team Map",
    "Decision Routing",
    "Merge Authority",
    "Current Enforcement Boundary",
    "GitHub Free",
    "audit-log API",
    "2FA",
]

REQUIRED_REPO_STANDARD_TERMS = [
    "Control Architecture",
    "Required Files",
    "Required Repository State",
    "Adoption States",
    "Context-ready",
    "Review-ready",
    "Enforced",
]

REQUIRED_CONCIERGE_TERMS = [
    "AI Concierge And Agent-City Standard",
    "Digital City Map",
    "Authority Matrix",
    "Release Levels",
    "Required Public Answer Contract",
    "Knowledge Classes",
    "Request Lifecycle",
    "Security And Privacy Gate",
    "Product Boundaries",
    "Agent Discovery And Interoperability",
    "External Channel Adapters",
    "Evaluation Gate",
    "Work And Audit State",
    "Model Context Protocol",
    "Agent2Agent",
    "OAuth",
    "LinkedIn",
    "X",
    "prompt injection",
    "44 by 44",
    "R2",
    "R3",
]

REQUIRED_PR_TERMS = [
    "Closes #",
    "Accountable human",
    "Risk tier",
    "Human manual verification",
    "AI Involvement",
    "Risk And Rollback",
    "Public And Private Boundary",
    "Ready-To-Merge Gate",
]

PLACEHOLDER_MARKERS = [
    "TODO",
    "FIXME",
    "TBD",
    "example.com",
    "your-org",
    "your-repo",
]

PINNED_ACTIONS = {
    "actions/checkout": "9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0",  # v7.0.0
    "actions/setup-python": "ece7cb06caefa5fff74198d8649806c4678c61a1",  # v6.3.0
}

ACTION_REFERENCE = re.compile(r"^\s*uses:\s*([^@\s]+)@([^\s#]+)", re.MULTILINE)
COMMIT_SHA = re.compile(r"^[0-9a-f]{40}$")
PERSONAL_EMAIL = re.compile(
    r"\b[A-Z0-9._%+-]+@(?:gmail|hotmail|outlook|yahoo)\.[A-Z]{2,}\b",
    re.IGNORECASE,
)
TEXT_SUFFIXES = {".json", ".md", ".py", ".txt", ".yml", ".yaml"}
SECRET_MARKERS = (
    "ghp" + "_",
    "github_pat" + "_",
    "sk_live" + "_",
    "sk_test" + "_",
    "sk-ant" + "-",
    "gsk" + "_",
    "xoxb" + "-",
    "-----BEGIN " + "PRIVATE KEY-----",
)


def read(path: str) -> str:
    file_path = ROOT / path
    if not file_path.is_file():
        raise SystemExit(f"Missing required file: {path}")
    text = file_path.read_text(encoding="utf-8")
    if not text.strip():
        raise SystemExit(f"Required file is empty: {path}")
    return text


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [path for path in result.stdout.decode().split("\0") if path]


def ensure_terms(path: str, terms: list[str]) -> None:
    text = read(path)
    missing = [term for term in terms if term not in text]
    if missing:
        raise SystemExit(f"{path} is missing required terms: {', '.join(missing)}")


def verify_no_placeholders_or_sensitive_content() -> None:
    for path in tracked_files():
        file_path = ROOT / path
        if not file_path.is_file() or file_path.suffix.lower() not in TEXT_SUFFIXES:
            continue

        text = file_path.read_text(encoding="utf-8", errors="ignore")
        if path in REQUIRED_FILES:
            for marker in PLACEHOLDER_MARKERS:
                if marker in text:
                    raise SystemExit(f"{path} contains unresolved marker: {marker}")

        if PERSONAL_EMAIL.search(text):
            raise SystemExit(f"Public repository contains a personal email address: {path}")

        for marker in SECRET_MARKERS:
            if marker in text:
                raise SystemExit(f"Potential secret marker {marker!r} in {path}")


def verify_tracked_boundary() -> None:
    for path in tracked_files():
        if path.startswith("ISSUE_TEMPLATE/"):
            raise SystemExit(
                "Legacy ISSUE_TEMPLATE path is tracked; organization defaults must use "
                ".github/ISSUE_TEMPLATE/"
            )

        file_path = ROOT / path
        if file_path.is_file() and file_path.stat().st_size > 1024 * 1024:
            raise SystemExit(f"Public tracked file exceeds 1 MiB review boundary: {path}")


def verify_commit_identity() -> None:
    commit_ref = os.environ.get("CHNAI_COMMIT_SHA", "HEAD")
    if commit_ref != "HEAD" and not COMMIT_SHA.fullmatch(commit_ref):
        raise SystemExit("CHNAI_COMMIT_SHA must be an immutable commit SHA")

    result = subprocess.run(
        ["git", "show", "-s", "--format=%ae%n%ce", commit_ref],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    if PERSONAL_EMAIL.search(result.stdout):
        raise SystemExit(
            "Contributed commit exposes a personal email; use the account-provided "
            "GitHub no-reply address"
        )


def verify_mermaid_framework() -> None:
    required_diagrams = {
        "docs/AI_AGENT_WORKFLOW.md": 4,
        "docs/MEMBER_ONBOARDING.md": 1,
        "docs/REPOSITORY_STANDARD.md": 1,
        "docs/AI_CONCIERGE_STANDARD.md": 3,
        "GOVERNANCE.md": 1,
    }
    for path, minimum in required_diagrams.items():
        count = read(path).count("```mermaid")
        if count < minimum:
            raise SystemExit(f"{path} must contain at least {minimum} Mermaid diagrams")


def verify_issue_forms() -> None:
    forms = [
        ".github/ISSUE_TEMPLATE/bug-report.yml",
        ".github/ISSUE_TEMPLATE/decision.yml",
        ".github/ISSUE_TEMPLATE/feature.yml",
        ".github/ISSUE_TEMPLATE/task.yml",
    ]
    for path in forms:
        text = read(path)
        for term in ["Risk tier", "R0 -", "R1 -", "R2 -", "R3 -"]:
            if term not in text:
                raise SystemExit(f"{path} is missing issue contract term: {term}")
        if re.search(r"^labels:\s*", text, re.MULTILINE):
            raise SystemExit(
                f"{path} must not assume labels exist in every inheriting repository"
            )

    for path in [
        ".github/ISSUE_TEMPLATE/bug-report.yml",
        ".github/ISSUE_TEMPLATE/feature.yml",
        ".github/ISSUE_TEMPLATE/task.yml",
    ]:
        text = read(path)
        for term in ["Accountable human", "Definition of done", "Verification plan"]:
            if term not in text:
                raise SystemExit(f"{path} is missing issue contract term: {term}")

    config = read(".github/ISSUE_TEMPLATE/config.yml")
    if "blank_issues_enabled: false" not in config or "SECURITY.md" not in config:
        raise SystemExit("Issue config must disable blank issues and route security reports")


def verify_ci_policy() -> None:
    workflow = read(".github/workflows/profile-checks.yml")
    if "permissions:\n  contents: read" not in workflow:
        raise SystemExit("CI must declare least-privilege read-only contents access")
    if "timeout-minutes:" not in workflow:
        raise SystemExit("CI jobs must declare a timeout")
    if "python3 scripts/verify_profile.py" not in workflow:
        raise SystemExit("CI must run the repository verifier")
    if "CHNAI_COMMIT_SHA: ${{ github.event.pull_request.head.sha || github.sha }}" not in workflow:
        raise SystemExit("CI must verify the contributed commit rather than a merge ref")
    if "fetch-depth: 0" not in workflow:
        raise SystemExit("CI must fetch history before checking the branch diff")
    if 'git diff --check "$(git merge-base origin/main HEAD)" HEAD' not in workflow:
        raise SystemExit("CI must check whitespace across the branch diff")

    references = ACTION_REFERENCE.findall(workflow)
    if not references:
        raise SystemExit("CI must use pinned GitHub Actions")
    for action, revision in references:
        if not COMMIT_SHA.fullmatch(revision):
            raise SystemExit(f"CI action {action} must use an immutable commit SHA")
        expected = PINNED_ACTIONS.get(action)
        if expected and revision != expected:
            raise SystemExit(f"CI action {action} is not pinned to the reviewed revision")

    dependabot = read(".github/dependabot.yml")
    if 'package-ecosystem: "github-actions"' not in dependabot:
        raise SystemExit("Dependabot must monitor GitHub Actions")

    codeowners = read(".github/CODEOWNERS")
    if "* @kavatana" not in codeowners:
        raise SystemExit("CODEOWNERS must retain the organization-owner fallback")


def main() -> None:
    for path in REQUIRED_FILES:
        read(path)

    ensure_terms("profile/README.md", REQUIRED_PROFILE_TERMS)
    ensure_terms("AGENTS.md", REQUIRED_AGENT_TERMS)
    ensure_terms("docs/AI_AGENT_WORKFLOW.md", REQUIRED_WORKFLOW_TERMS)
    ensure_terms("GOVERNANCE.md", REQUIRED_GOVERNANCE_TERMS)
    ensure_terms("docs/REPOSITORY_STANDARD.md", REQUIRED_REPO_STANDARD_TERMS)
    ensure_terms("docs/AI_CONCIERGE_STANDARD.md", REQUIRED_CONCIERGE_TERMS)
    ensure_terms("PULL_REQUEST_TEMPLATE.md", REQUIRED_PR_TERMS)

    verify_tracked_boundary()
    verify_no_placeholders_or_sensitive_content()
    verify_commit_identity()
    verify_mermaid_framework()
    verify_issue_forms()
    verify_ci_policy()


if __name__ == "__main__":
    main()
