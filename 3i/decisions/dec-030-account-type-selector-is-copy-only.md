---
project: 3i
type: decision
status: current
updated: 2026-08-24
id: 3I-DEC-030
tags: [decision, ux, registration]
---

# Account Type Selector Is Copy-Only, Not a New Account Type

## Context

Registration currently has one path: a single form, one account type, evaluated by date of birth ([3I-DEC-023](dec-023-no-standalone-accounts-under-18.md)). A request surfaced to show two cards at the "Create Account" entry point — one framed for someone signing up to study themselves, one framed for a parent signing up to add children or teens — so the product feels like it understood what the person came to do.

The risk this decision closes off: building this as two genuinely different registration paths would reopen exactly the branching complexity DEC-023 spent effort collapsing away.

## Decision

**[Account Type Selector](/3i/modules/identity-and-access/ui/screens/account-type-selector.md) is a new screen sitting in front of [Registration — Adult](/3i/modules/identity-and-access/ui/screens/registration-adult.md), with two cards ("For myself" / "For my family"). It changes copy only.**

Both cards lead to the identical registration form — same fields, same single adult account type, same date-of-birth gate — differing only in the headline and subtext shown ("Create your account" vs. "Start your family's learning journey"). No data is written or branched based on which card was clicked; nothing about the choice is persisted past the next screen's copy.

**No post-verification behaviour differs either.** Both paths reach [Email Verification](/3i/modules/identity-and-access/ui/screens/email-verification.md) and then the same first-login destination. A "nudge" variant — routing the Family card straight into "add your first child" after verification — was considered and explicitly declined, to keep the distinction purely presentational rather than adding a second onboarding path to maintain.

**The age gate carries no exemption from either card.** Someone who selects "For myself" and enters a date of birth under 18 is redirected to [Registration blocked — under 18](/3i/modules/identity-and-access/ui/screens/registration-blocked-under-18.md), identical to any other path.

**[Social login — DOB capture](/3i/modules/identity-and-access/ui/screens/social-login-dob-capture.md) stays neutral.** The copy variant does not carry through to it — a deliberate simplification, since it is a single field and the extra design variant was judged not worth the payoff.

## Consequences

- One data model, one account type, unchanged from DEC-023 — this decision touches presentation only.
- `registration-adult.md` now documents two copy variants sharing one field layout, kept in the same file specifically so they cannot drift apart from each other over time.
- Two extra copy strings (Variant A / Variant B headline + subtext) enter translation, but neither is a safeguarding-exempt string under DEC-019 — ordinary AI-translation pipeline applies.

## Cost

One additional screen in the registration funnel, and a small amount of ongoing discipline required to keep two copy variants of one form in sync — mitigated by documenting both in a single file rather than two.
