# CHNAI LAB Agent Guide

This is the default operating standard for AI agents working inside CHNAI LAB
repositories. If a repo has its own `AGENTS.md`, follow that repo guide first
when it is stricter than this org guide.

## Read Order

Every agent session starts by reading:

1. This file.
2. `docs/AI_AGENT_WORKFLOW.md`.
3. The target repo's `AGENTS.md` or `CLAUDE.md`, if present.
4. The target repo's `README.md`.
5. The issue, task, or pull request being worked on.
6. The relevant source files before editing.

If any of those files are missing, say so in the handoff and continue with the
available context.

## Agent Role

Agents help with research, implementation, refactoring, tests, documentation,
debugging, and review. They do not replace human ownership. A human teammate is
responsible for product judgment, security, verification, and merge decisions.

The default relationship is:

- Human: owns product intent, access, secrets, final review, and merge.
- Agent: proposes changes, edits files, runs checks, explains uncertainty.
- Reviewer: verifies behavior and risk, not only whether the diff looks clean.

## Required Workflow

1. Start from a fresh branch created from `main`.
2. Restate the task and the product boundary before editing.
3. Inspect current files and Git state.
4. Make one focused change.
5. Run the repo's documented checks.
6. Record what changed, how it was verified, and what remains uncertain.
7. Open or update a pull request with AI involvement clearly stated.

## Hard Rules

- Do not commit secrets, tokens, API keys, customer data, private chats, or
  internal strategy.
- Do not invent traction, customers, revenue, compliance, certifications, or
  security claims.
- Do not expose private product code in public repositories.
- Do not rewrite unrelated files to make a diff look cleaner.
- Do not bypass tests, lint, type checks, or build failures without documenting
  the reason.
- Do not push directly to `main`.
- Do not change repo visibility, access, billing, secrets, or production
  settings without explicit human instruction.

## Standard Agent Prompt

When a teammate starts an agent in a CHNAI LAB repo, they can paste:

```text
You are working in a CHNAI LAB repository. First read AGENTS.md, CONTRIBUTING.md,
SECURITY.md, README.md, and any CLAUDE.md file. Then inspect package scripts,
Git status, and the issue/task. Before editing, summarize the product boundary,
the files you will touch, the checks you will run, and any risks. Do not use or
ask for secrets. Keep the change small, run verification, and prepare a PR
summary with AI involvement and human verification notes.
```

## Handoff Format

At the end of an agent session, report:

- Branch and commit, if created.
- Files changed.
- Verification commands and results.
- Behavior manually checked.
- Risks, assumptions, and remaining work.
- Whether any sensitive context was used. The expected answer is "none".

## Verification Standard

"The agent said it works" is not verification. A mergeable pull request should
include commands run, screenshots when UI changed, and a human note explaining
what was personally checked.
