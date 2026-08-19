---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - registration
  - safeguarding
---

# Screen: Registration Blocked — Under 18

Satisfies: FR-AUTH-03, FR-AUTH-04, as extended by [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md)

**Renamed from "Under 13."** [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) removed the 13–17 standalone registration path entirely, so this screen's trigger widened from "under 13" to "under 18." The screen's content and behaviour are otherwise unchanged — the same redirect now simply catches a wider age range.

---

## Purpose

Reached when date of birth on [Registration — Adult](registration-adult.md) resolves to **any age under 18**, via any route including [Social login — DOB capture](social-login-dob-capture.md).

## Content

**The block message is in the exempt string set** — [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md). It bypasses AI translation and requires named human sign-off per language before launch.

The message must be **neutral and not disclose the age threshold in a way that invites retry** (FR-AUTH-03's principle, now applied at the 18 threshold as well). It should not say "you must be 18" or similar — that teaches the specific number to amend a birth year against. A general statement that the account cannot be created, with a pointer toward the family account model, is the target shape; exact wording is the sign-off owners' call per language, not fixed here.

**Wording should read naturally for a 17-year-old, not just a young child.** The original copy was written with a 6-to-12-year-old in mind. A near-adult being redirected to "ask your parent to make an account" needs a tone that doesn't read as condescending — this is worth explicit attention during the sign-off pass, since it's a new audience for this screen that didn't exist before DEC-023.

Offers a path toward [Registration — Adult](registration-adult.md) framed as "if you are a parent or guardian, you can create an account for your child" — this is the intended redirect, not an afterthought, since the family account model is now the **only** way anyone under 18 reaches the platform.

## Behaviour

On render, a hashed session identifier and timestamp are recorded server-side (FR-AUTH-04), regardless of what the person does next. This is silent — nothing on screen indicates that a record was made, since disclosing it would itself invite evasive behaviour.

A subsequent attempt from the same hashed session with an amended date of birth is identifiable as a retry. What happens on a detected retry (stricter block, flag for review, no visible change) is **not specified in the baseline** and is worth raising with the client rather than assumed.

## Role Variations

None — public only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04). Given the sign-off requirement above, this screen cannot ship in a given language until that language's sign-off is complete — it is a literal launch blocker per language, not just a translation nicety.
