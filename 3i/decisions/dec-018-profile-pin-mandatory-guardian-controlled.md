---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-018
tags: [decision, identity, safeguarding]
---

# Profile PIN Is Mandatory and Guardian-Controlled

## Context

FR-FAM-03 makes the 4-digit profile PIN **optional**. Removing the feature entirely was considered on 2026-08-18 and rejected.

The reason it cannot be optional: chat access is derived per-profile from age (FR-FAM-08). Under-13 profiles have none; 13–17 profiles may. Without a PIN, the profile picker is the only thing standing between a nine-year-old and their fifteen-year-old sibling's chat access — and the picker is one tap. Profile separation would be honour-system, in the one place where it is a safeguarding boundary rather than a convenience.

## Decision

Taken 2026-08-18:

1. **The PIN is mandatory, not optional.** Switching from one profile to another requires it.
2. **The guardian sets it.** Not the learner. A child choosing their own PIN defeats the purpose, since the point is to stop a sibling entering a profile that is not theirs.
3. **The guardian resets it from the dashboard.** There is no learner-facing reset, no email recovery — a profile has no email address (FR-FAM-03).
4. **It applies to every profile, including the account holder's own.** They have already authenticated with a password, but exempting one profile would mean the picker sometimes challenges and sometimes does not, and an inconsistent control is one users learn to expect to fail.

## Scope

FR-FAM-03 says optional. Making it mandatory is a change requiring sign-off under §21.3.

## Consequences

- The guardian dashboard (FR-FAM-09) gains PIN management per profile — set on creation, reset on demand.
- Profile creation cannot complete without a PIN, so the creation flow gains a required step.
- A forgotten PIN is a guardian problem, resolved from a session that is already authenticated. No support path is needed.
- PINs are hashed at rest like any other credential. A 4-digit PIN has ten thousand possibilities, so the picker needs rate limiting — FR-AUTH-09's five-attempts-then-lockout is the natural pattern to reuse.

## Cost

Every profile switch now costs four digits. On a family tablet where children switch often, that is real friction, and it is the price of the boundary being real rather than nominal.

The PIN protects against a sibling, not against a determined adult with the account password. It is not trying to.
