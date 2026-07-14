# Member Onboarding

Use this checklist when a new teammate joins CHNAI LAB.

## Owner Checklist

- Invite the teammate to the `chnai-lab` GitHub organization.
- Assign only the product team or teams they need.
- Confirm they enabled GitHub two-factor authentication.
- Confirm they can clone the assigned repo.
- Point them to `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, and
  `docs/AI_AGENT_WORKFLOW.md`.
- Ask them to make a small first PR so the workflow is practiced early.

## Product Teams

- `@chnai-lab/chomkar-builders` - Chomkar
- `@chnai-lab/sat-digital-builders` - Sat Digital
- `@chnai-lab/phsaros-builders` - PHSAROS
- `@chnai-lab/svaeng-yul-builders` - Svaeng Yul

Team membership grants product write access and lets `CODEOWNERS` request the
right reviewers automatically. If a product has no team yet, an org owner
creates one before assigning a new builder.

## New Member Checklist

- Accept the org invite.
- Enable two-factor authentication.
- Confirm which product team or teams you joined.
- Clone the assigned repo.
- Read the org guide files.
- Read the repo's `README.md`, `AGENTS.md`, and `CLAUDE.md` if present.
- Start work from an issue and a branch.
- Use an AI agent only after it reads the same guides.
- Open a PR with verification and AI involvement notes.

## First Agent Prompt

```text
You are helping me work inside a CHNAI LAB repository. Read AGENTS.md,
CONTRIBUTING.md, SECURITY.md, README.md, docs/AI_AGENT_WORKFLOW.md, and CLAUDE.md
if present. Summarize the repo rules, product boundary, checks, and risks before
editing. Do not use secrets. Work on a branch. Keep the change small. Run the
repo checks and prepare a PR summary with AI involvement and human verification.
```

## First PR Ideas

- Improve one README section.
- Add one missing test or verification script.
- Fix one small bug.
- Improve one issue template.
- Add one screenshot or documented manual check.
