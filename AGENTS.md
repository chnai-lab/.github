# CHNAI LAB Agent Guide

This file defines the default operating standard for AI agents working inside
CHNAI LAB repositories.

## Agent Role

Agents help with research, implementation, refactoring, tests, documentation,
debugging, and review. They do not replace human ownership. A human teammate is
responsible for final product judgment, verification, security, and merge
decisions.

## Required Workflow

1. Start from a fresh branch created from `main`.
2. Read the issue, README, local project guide, and relevant source before
   editing.
3. Keep changes scoped to the issue or task.
4. Run the repo's documented checks before handing work back.
5. Record what changed, how it was verified, and what remains uncertain.
6. Open or update a pull request with AI involvement clearly stated.

## Hard Rules

- Do not commit secrets, tokens, API keys, customer data, private chats, or
  internal strategy.
- Do not invent traction, customers, revenue, compliance, or security claims.
- Do not rewrite unrelated files to make a diff look cleaner.
- Do not bypass tests, lint, type checks, or build failures without documenting
  the reason.
- Do not push directly to `main`.
- Do not expose private product code in public repositories.

## Context To Provide Agents

Useful context:

- Issue or task objective.
- Product audience and user workflow.
- Relevant files and existing patterns.
- Commands for lint, type-check, test, and build.
- Screenshots or logs with secrets removed.

Unsafe context:

- Credentials.
- Private user data.
- Payment, financial, or trading secrets.
- Unannounced strategy.
- Production infrastructure details.

## Verification Standard

"The agent said it works" is not verification. A mergeable PR should include
commands run, screenshots when UI changed, and a short human note explaining
what was personally checked.
