# Contributing At CHNAI LAB

CHNAI LAB is an AI-native product studio. We use agents to move faster while
keeping every meaningful change owned by a person, linked to a real outcome,
verified with evidence, and reviewed before it reaches `main`.

Read these before contributing:

- [`AGENTS.md`](AGENTS.md) - vendor-neutral agent contract.
- [`docs/AI_AGENT_WORKFLOW.md`](docs/AI_AGENT_WORKFLOW.md) - complete delivery loop.
- [`docs/REPOSITORY_STANDARD.md`](docs/REPOSITORY_STANDARD.md) - repository adoption contract.
- [`GOVERNANCE.md`](GOVERNANCE.md) - roles, access, and decision rights.
- [`SECURITY.md`](SECURITY.md) - reporting and sensitive-data boundary.

## The Working Agreement

1. Every change starts from an issue with an accountable human.
2. One issue maps to one branch and one focused pull request.
3. The issue states risk, evidence, scope, non-goals, verification, and done.
4. The agent reads the issue and repository contract before editing.
5. AI work and human judgment are disclosed separately.
6. A human personally verifies the behavior they claim to have checked.
7. `main` is kept reviewable and deployable through pull requests.

## Exact Path

```text
Choose product -> join product team -> ready issue -> issue branch -> agent
preflight -> focused implementation -> checks -> draft PR -> agent handoff ->
human verification -> CODEOWNER/domain review -> merge -> delete branch ->
follow-up issue
```

The default work-in-progress limit is one active implementation issue per
builder per product. If work is blocked, record the blocker before starting a
second item.

## 1. Choose Or Open A Ready Issue

Use the inherited feature, bug, task, or decision form. A ready issue contains:

- Accountable human.
- Problem or outcome.
- Evidence or clearly labeled assumption.
- Scope and non-goals.
- Definition of done.
- Verification plan.
- Risk tier R0, R1, R2, or R3.
- Safe public/private boundary.

Do not place private member information or startup-sensitive context in this
public `.github` repository. Open the issue in the affected private product
repository.

## 2. Create The Issue Branch

```bash
git switch main
git pull --rebase origin main
git switch -c feat/42-short-name
```

Use `fix/`, `docs/`, or `chore/` when appropriate. Do not push directly to
`main`. Never force-push a shared branch. On your own unreviewed PR branch, use
`--force-with-lease` only when necessary.

## 3. Start The Agent With Context

Give the agent the issue and ask it to read the local repository files in
`AGENTS.md`. Before editing, the agent must return:

- Outcome and product boundary.
- Risk tier.
- Files likely to change.
- Checks it will run.
- Assumptions and unknowns.
- Stop conditions.

Correct wrong assumptions before the agent produces a large diff. Do not paste
secrets, private chats, personal data, production credentials, or an unbounded
private knowledge dump into the prompt.

## 4. Build One Outcome

- Follow existing architecture and repository conventions.
- Keep unrelated cleanup out of the branch.
- Preserve human changes already in the worktree.
- Add tests proportional to behavior and risk.
- Push early when work will continue.
- Open a draft PR before the work becomes difficult to review.

An agent can implement and explain. The builder remains responsible for
understanding the change well enough to maintain and defend it.

## 5. Prove The Change

Run the repository's documented verification command plus relevant tests,
lint, type checks, build, security checks, and manual flows. Record exact
commands and results in the PR.

For visible UI changes, test the affected mobile and desktop flow and attach
evidence when useful. For backend, data, auth, security, payment, or trading
work, test failure paths and name the affected route, function, migration, or
boundary.

"The agent said it works" is not verification.

## 6. Complete The Pull Request

The PR template requires:

- `Closes #<issue>`.
- Accountable human and risk tier.
- Outcome, scope, and non-goals.
- Automated evidence and human manual verification.
- AI involvement and human decisions.
- Risks, rollback, and remaining uncertainty.
- Public/private and claim-safety confirmation.

Keep the PR in draft while required evidence is missing. Mark it ready only
when the builder has inspected the final diff and completed their human checks.

## 7. Review Behavior And Risk

Reviewers check the issue outcome, not only whether the diff looks plausible.
They verify scope, architecture, evidence, failure paths, security, data
boundaries, public claims, and maintainability.

R2 changes require the relevant domain reviewer. R3 actions stop before the
privileged or irreversible action until the organization owner explicitly
authorizes it.

Resolve conversations with code, evidence, or a clear scope decision. Silence
is not approval.

## 8. Merge And Learn

Use squash merge unless the repository documents another method. Delete the
branch after merge. Create a new issue for follow-up work instead of hiding it
inside the merged PR.

## Commits And Attribution

- Use Conventional Commit subjects: `feat:`, `fix:`, `docs:`, `chore:`,
  `refactor:`, `test:`, or `ci:`.
- Keep commits coherent and free of generated noise.
- Use `Co-authored-by` only for a human who materially contributed to the final
  change and approved the credit.
- Record AI assistance in the PR's **AI involvement** section. Do not use
  authorship metadata to simulate human collaboration or GitHub achievements.
- Never stage issues, reviews, reactions, merges, or co-authors for profile
  metrics.

## Access And Accounts

- Members receive product access through GitHub teams.
- Organization base repository access remains `none`.
- Two-factor authentication is required before product access.
- Each person uses their own account and credentials.
- Commit identity must be deliberate: use GitHub's account-provided no-reply
  address or an intentionally public professional address, never expose a
  personal mailbox by accident.
- Enable GitHub's **Keep my email addresses private** and **Block command line
  pushes that expose my email** settings before the first contribution.
- Shared passwords are prohibited for GitHub, email, internal systems, and
  production.
- Outside collaborators are temporary and limited to one repository.

CHNAI LAB currently uses GitHub Free. Private-repository branch protection is
therefore a policy rather than an enforced control. The organization will not
claim required approvals or checks are technically enforced until a GitHub Team
upgrade and live settings prove it.

## Reusable AI-Native Team Starter

The public
[`ai-native-team-starter`](https://github.com/kavatana/ai-native-team-starter)
packages a product-neutral version of this workflow. It contains no private
startup source, data, or strategy.

## Final Traceability Check

Before merge, a teammate should answer from the PR alone:

- What issue and human owner does this trace to?
- What changed and what stayed out of scope?
- What did the AI agent contribute?
- What did a human personally verify?
- Which checks passed?
- What could fail and how is it rolled back?
- Did the change preserve secrets, private data, strategy, and claim boundaries?
