# Security Policy

CHNAI LAB builds several private product repositories, including education,
agriculture, SME operations, cybersecurity, and trading tools. Security issues
are handled conservatively because many projects are future startup assets.

## Public Reporting Boundary

Do not publish exploit details, credentials, tokens, private user data, or
production infrastructure information in public issues, pull requests, comments,
screenshots, or prompts.

For public repositories, use GitHub's private vulnerability reporting when the
repository exposes that option. Otherwise contact a CHNAI LAB owner through a
verified private channel. Never open a public issue containing exploit details.
For private repositories, report the issue in the team's private channel and
link the affected repository, commit, route, screen, or workflow.

## What To Include

- Affected repository and area.
- Reproduction steps.
- Expected impact.
- Logs or screenshots with secrets removed.
- Suggested fix if known.

## Internal Handling

1. Confirm the report privately.
2. Open a private tracking issue.
3. Patch on a branch.
4. Verify with tests, manual reproduction, or both.
5. Merge through pull request review.
6. Rotate any exposed secret and document follow-up work.

Access, secret rotation, production changes, repository visibility, and other
privileged incident actions are R3. An agent may prepare the procedure but must
stop before the action until the organization owner explicitly authorizes it.

## Account Baseline

- Every person uses an individual GitHub and email account.
- Two-factor authentication is required before private product access.
- Recovery codes stay private and outside repositories, issues, prompts, and
  chat.
- Shared default passwords are prohibited.
- Product access is granted through the smallest relevant GitHub team and is
  removed when no longer needed.

## Agent Safety

AI agents may help investigate and patch security issues, but they must not be
given raw secrets, private customer data, or production credentials. Share
redacted logs, synthetic fixtures, and minimal reproduction context instead.
Agents do not approve their own security work or claim a human performed a
manual check.
