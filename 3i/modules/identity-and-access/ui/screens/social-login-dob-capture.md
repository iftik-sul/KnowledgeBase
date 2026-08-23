---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-IDA-UI-006
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - registration
  - authentication
figma: null
---

# Screen: Social Login — DOB Capture

Satisfies: FR-AUTH-07

---

## Purpose

Shown on the **first** login via Google or Apple, before any account record is created. The single highest-risk screen in the module for an age-gate leak, since the social provider supplies an already-verified identity and it is tempting to trust it wholesale.

## Fields

Date of birth only. Name and email are taken from the social provider and are not re-entered here, but date of birth is **always** captured on this screen regardless of what the provider does or does not supply — FR-AUTH-07 makes no exception.

## Behaviour

On submit, this screen routes through exactly the same age-branch logic as [Registration — Adult](registration-adult.md): 18+ proceeds to account creation and triggers [Email verification](email-verification.md); anything under 18 redirects to [Registration blocked — under 18](registration-blocked-under-18.md), the single path serving every under-18 age per [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md).

**This screen must exist and must block, with no bypass.** The acceptance criterion for FR-AUTH-03 is explicit: no one under 18 can produce an account by any route, including social login. A social provider returning an adult-verified identity does not exempt this step.

## Role Variations

None — public only, first-login-only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).