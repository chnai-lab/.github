# AI Agent Workflow

CHNAI LAB works AI-native, but not AI-blind. Agents can move fast; humans keep
the product, security, and verification standards high.

## Team Model

- One issue owns one outcome.
- One branch owns one issue.
- One pull request owns one reviewable change.
- One human owns final verification.

Agents can create drafts, run checks, and explain tradeoffs. Humans decide what
ships.

## Access Model

Use org membership for teammates. Repo-only outside collaborator access is
temporary and should be converted to org membership when the person is part of
the team.

Recommended default:

- Org owner: administers org, repo settings, secrets, billing, and production.
- Member: receives write access only to assigned repos.
- Outside collaborator: short-term access for one repo only.

## Session Start Protocol

Before an agent edits, it must gather context:

1. Read org `AGENTS.md`.
2. Read repo `AGENTS.md` or `CLAUDE.md`.
3. Read repo `README.md`.
4. Inspect package scripts and available checks.
5. Inspect Git status.
6. Read the issue or task.
7. Inspect relevant files.

The agent should then report:

- Product boundary.
- Intended files.
- Planned checks.
- Risks or unknowns.

## Branch Protocol

Branch names:

- `feat/<issue>-short-name`
- `fix/<issue>-short-name`
- `docs/<issue>-short-name`
- `chore/<issue>-short-name`

Rules:

- Branch from fresh `main`.
- Do not mix unrelated changes.
- Push early if work will continue.
- Delete branch after merge.
- Use `--force-with-lease` only on your own PR branch.

## Pull Request Protocol

Every PR should include:

- Issue link.
- What changed and why.
- How it was verified.
- AI involvement.
- Human verification.
- Risk and rollback.
- Public/private boundary check.

For UI work, include screenshot or screen recording evidence when possible. For
backend or data work, include command output and affected route/function names.

## Review Protocol

Reviewers should ask:

- Does this solve the issue?
- Is the change scoped?
- Did the agent follow the repo guide?
- Are claims conservative and supported?
- Are secrets and private data absent?
- Did the human actually verify behavior?
- Is rollback clear?

## Product Claim Rules

Do not claim:

- Revenue, traction, customers, certifications, safety guarantees, compliance,
  or impact numbers unless verified and approved.
- That an AI model is trained, fine-tuned, or proprietary unless it is true.
- That a private repo feature is shipped publicly unless it is deployed and
  verified.

Prefer:

- "prototype"
- "demo"
- "private product repo"
- "validated by local check"
- "human-reviewed"
- "claim-safe"

## Security Rules

Never give agents:

- Tokens or API keys.
- Customer, buyer, farmer, student, or teammate private data.
- Production infrastructure credentials.
- Payment, trading, or financial secrets.

Use redacted logs and minimal reproduction steps.

## Handoff Template

Agents should end with:

```md
Branch:
Commit:
Changed:
Verified:
Manual check:
Risks:
Sensitive context used: none
Next step:
```

## When To Stop

Stop and ask a human before:

- Changing production settings.
- Changing repo visibility or access.
- Touching secrets.
- Making legal, security, finance, trading, or certification claims.
- Publishing private strategy or source code.
- Expanding scope beyond the issue.
