---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-24
id: 3I-IDA-UI-016
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - registration
figma: null
---

# Screen: Account Type Selector

Satisfies: FR-AUTH-01 (entry point only — see [Registration — Adult](registration-adult.md) for the requirement's substance)

---

## Purpose

The first screen reached when someone clicks "Create Account," sitting in front of [Registration — Adult](registration-adult.md). Two cards, chosen once, that set which copy variant the registration form shows next — **not a second account type**. Every account created downstream is identical: same fields, same single adult account type, same date-of-birth gate. See [3I-DEC-030](/3i/decisions/dec-030-account-type-selector-is-copy-only.md) for the decision this screen implements.

## Content

Two cards, equal visual weight, side by side:

- **"For myself"** — for someone signing up to study themselves. Routes to [Registration — Adult](registration-adult.md), Variant A copy.
- **"For my family"** — for someone signing up to add children or teens as profiles. Routes to [Registration — Adult](registration-adult.md), Variant B copy. "Teens" is named explicitly so a parent of a 13–17-year-old does not wonder whether this applies to them — per [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md), it does, exactly as it would for a five-year-old.

Neither card should read as the default or primary option — same size, same icon weight, same treatment.

## Behaviour

**Copy-only fork.** Both paths land in exactly the same place afterward: the same registration form fields, the same date-of-birth evaluation, then [Email Verification](email-verification.md), then wherever first-time login normally goes. There is no post-verification nudge (e.g. "add your first child") tied to the Family card — that was considered and explicitly declined in favour of keeping the distinction copy-only.

**The age gate does not care which card was clicked.** Someone who selects "For myself" and then enters a date of birth under 18 is still redirected to [Registration blocked — under 18](registration-blocked-under-18.md), same as anyone else — the card choice carries no exemption of any kind.

**If "Continue with Google/Apple" is chosen instead of the manual form**, the person skips directly to [Social login — DOB capture](social-login-dob-capture.md), which stays **neutral** regardless of which card was picked on this screen — no Adult/Parent framing carries through to that screen, a deliberate simplification since it is a single field.

This screen is shown once, at entry. It is not revisited or stored as account state — nothing about which card was clicked is persisted beyond the copy shown on the very next screen.

## Role Variations

None — public only, entry point before any session exists.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): card order and icon direction mirror in Arabic and Urdu.
