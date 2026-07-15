# Contributing at CHNAI LAB

This guide applies to every CHNAI LAB repository. We are an AI-native team:
everyone builds with AI agents (Claude Code, Copilot, etc.), so our workflow is
designed to keep agent-speed development **traceable, reviewable, and safe**.

For agent-specific rules, also read [`AGENTS.md`](AGENTS.md) and
[`docs/AI_AGENT_WORKFLOW.md`](docs/AI_AGENT_WORKFLOW.md). For sensitive work,
read [`SECURITY.md`](SECURITY.md) before you share context with any tool.

## Principles

1. **`main` is always deployable.** Nobody — human or agent — commits directly
   to `main`. All work lands through pull requests.
2. **Every change traces to an issue.** If it's worth doing, it's worth an
   issue. PRs link their issue with `Closes #N`.
3. **Small PRs win.** One PR = one concern. A reviewer (human or agent) should
   understand it in under 10 minutes.
4. **Agents are teammates, humans are owners.** An agent can write the code,
   but a human opens the PR, verifies the result, and is accountable for it.

## The loop

```
Issue → Branch → Build (with your agent) → PR → Review → Squash-merge → Delete branch
```

1. **Pick or open an issue** describing the problem/outcome (not the code).
2. **Branch from fresh `main`:**
   ```bash
   git checkout main && git pull --rebase origin main
   git checkout -b feat/42-lesson-progress
   ```
3. **Build.** Point your agent at the issue. Keep commits small and coherent.
4. **Open a PR early** (draft is fine). Fill in the template — especially
   *How it was verified* and *AI involvement*.
5. **Review.** At least one other human approves product-repo PRs. Review the
   *behavior and risk*, not just the diff — agents produce plausible-looking
   code; verify it actually runs.
6. **Squash-merge**, then delete the branch. The issue closes automatically.

## New Member Start

1. Accept the CHNAI LAB org invite.
2. Turn on GitHub two-factor authentication.
3. Confirm which product repos you can access.
4. Clone only the repo assigned to your task.
5. Ask your AI agent to read the org guide and the repo guide before editing.
6. Open a small first PR: docs, test, bug fix, or one isolated feature slice.

Use this first prompt for any agent:

```text
Read AGENTS.md, CONTRIBUTING.md, SECURITY.md, README.md, and CLAUDE.md if it
exists. Summarize the repo rules, product boundary, checks, and risk before
editing. Do not use secrets. Work on a branch. Keep the change small and prepare
a PR summary with verification.
```

## Branches & commits

- Branch names: `feat/<issue>-slug`, `fix/<issue>-slug`, `chore/…`, `docs/…`
  — e.g. `fix/17-pos-change-due`.
- Commits follow [Conventional Commits](https://www.conventionalcommits.org):
  `feat: …`, `fix: …`, `chore: …`, `docs: …`, `refactor: …`, `test: …`.
- Use `Co-authored-by` only for a human who materially contributed to the final
  change and approved the credit. Record AI assistance in the pull request's
  **AI involvement** section instead of using authorship metadata to simulate
  human collaboration or GitHub achievement activity.

## Working with AI agents

- **Agents work on branches, never on `main`.** Configure your agent's working
  directory on a feature branch before it starts editing.
- **Give agents context, not secrets.** Each repo keeps a `CLAUDE.md` /
  `AGENTS.md` with project context, commands, and conventions so any
  teammate's agent onboards instantly. Never paste tokens, customer data, or
  credentials into prompts, commits, or agent context files.
- **Verify before you push.** "The agent said it works" is not verification.
  Run the app / tests yourself and record what you did in the PR's
  *How it was verified* section.
- **One agent session ≈ one branch.** If your agent pivots to a different
  concern, open a new issue and branch instead of growing the PR.
- **Record AI involvement in the PR.** Say which agent helped, what it changed,
  what a human reviewed, and what commands or screens proved the result.
- **Keep contribution activity authentic.** Do not stage co-authors, reviews,
  issues, discussions, or merges for profile metrics or achievements.

## Push / pull hygiene

- Sync before you push: `git pull --rebase origin main` (rebase, don't merge,
  so history stays linear).
- Never `git push --force` a shared branch. On your own PR branch,
  `--force-with-lease` only.
- Push at least daily on active branches — unpushed work is invisible to the
  team and to reviewers.
- Delete branches after merge (GitHub offers the button; take it).
- Dependabot PRs: whoever owns the repo that week reviews/merges them; don't
  let them pile up.

## Roles & access

- **Org owners** (founders) administer repos, settings, and merges to `main`.
- **Members** get `write` through product teams on the repos they build; they
  work through PRs like everyone else.
- New teammates join the **chnai-lab org** (not personal-repo invites), so
  access is managed in one place.
- Outside collaborators are temporary. If someone is joining the team, invite
  them to the org and assign repo access through a product team.

## Review Standard

Reviewers check:

- The issue and PR match.
- The agent followed the repo guide.
- The change is small enough to review.
- The verification is real.
- Public/private boundaries are respected.
- Claims are supported and conservative.

## Traceability checklist

Before you merge, your PR should answer — from the PR page alone, without
asking you:

- [ ] What issue does this close?
- [ ] What changed, in one paragraph?
- [ ] How was it verified (commands run, screenshots, test output)?
- [ ] What did the AI agent do vs. what did the human check?
- [ ] Did the change avoid secrets, private user data, and overbroad public
      claims?
