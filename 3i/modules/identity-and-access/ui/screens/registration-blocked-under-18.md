---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-24
id: 3I-IDA-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - registration
  - safeguarding
figma: null
---

# Screen: Registration Blocked — Under 18

Satisfies: FR-AUTH-03, FR-AUTH-04

---

## Purpose

Reached when date of birth on [Registration — Adult](registration-adult.md) resolves to any age under 18, via any route including [Account Type Selector](account-type-selector.md) → either copy variant, or [Social login — DOB capture](social-login-dob-capture.md).

## Content

**The block message is in the exempt string set** — [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md). It bypasses AI translation and requires named human sign-off per language before launch.

The message must be **neutral and not disclose the age threshold in a way that invites retry** (FR-AUTH-03). It should not say "you must be 18" or similar — that teaches the specific number to amend a birth year against. It must, however, still make clear that the date of birth entered is *why* the account can't be created directly — omitting the reason entirely was tried and rejected as under-explaining the block. The constraint is specifically about not disclosing the numeric threshold, not about hiding the cause.

**Wording must read naturally across the full age range this screen serves** — from a young child's guardian reading on their behalf, to a near-adult teenager reading it themselves. A tone that only suits a young child will read as condescending to a 17-year-old.

### Draft Copy — Pending Sign-Off

**This is a starting draft for the DEC-019 sign-off owners, not finalised copy.** It satisfies the constraints above (no numeric threshold, states the DOB-based reason, impersonal enough to suit the full age range) but still requires named human sign-off per language before it can ship in any locale.

> **Heading:** This account needs to be set up by a parent or guardian
>
> **Body:** Based on the date of birth entered, we're not able to create this account directly. A parent or guardian can create an account instead, and add you as a learner profile — with full access to courses, progress tracking, and certificates. If a parent or guardian is nearby, they can get started below.

Offers a path **directly to [Registration — Adult](registration-adult.md), Variant B ("For my family") copy** — not routed back through [Account Type Selector](account-type-selector.md) first. Whoever reaches this screen has already stated their situation by getting here; sending them through a selector whose only job is to establish what they've already established would be a redundant extra step.

## Behaviour

On render, a hashed session identifier and timestamp are recorded server-side (FR-AUTH-04), regardless of what the person does next. This is silent — nothing on screen indicates that a record was made, since disclosing it would itself invite evasive behaviour.

A subsequent attempt from the same hashed session with an amended date of birth is identifiable as a retry. What happens on a detected retry (stricter block, flag for review, no visible change) is **not specified in the baseline** and is worth raising with the client rather than assumed.

## Role Variations

None — public only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04). Given the sign-off requirement above, this screen cannot ship in a given language until that language's sign-off is complete — it is a literal launch blocker per language, not just a translation nicety.
