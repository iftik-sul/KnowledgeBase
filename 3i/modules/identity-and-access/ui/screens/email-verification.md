---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-IDA-UI-004
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - registration
figma: null
---

# Screen: Email Verification

Satisfies: FR-AUTH-06

---

## Purpose

Shown after registration and after any email change, until the address is confirmed. Blocks enrolment, checkout, and chat while pending (FR-AUTH-06).

## Behaviour

A verification link is emailed on account creation and on any subsequent email change. This screen shows pending state with a resend option (rate-limited — not specified in the baseline, default to one resend per 60 seconds pending client input).

**On an email change**, the account's prior verified state is preserved until the new address confirms — the account does not drop to a blocked state mid-change. This screen in that context reads as "confirm your new email" rather than "your account is unverified", since the two situations carry very different urgency.

**Destination after successful verification varies by context** — generally "wherever the person was headed before the block," with one named exception: **an Account whose registration also created a `pending` InstructorApplication** (the combined instructor-registration path, [3I-DEC-038](/3i/decisions/dec-038-instructor-registration-account-works-normally.md)) routes to [Instructor Application Confirmation](/3i/modules/instructors/ui/screens/instructor-application-confirmation.md) instead of the ordinary post-registration destination — [3I-DEC-040](/3i/decisions/dec-040-instructor-registration-confirmation-screen.md).

## Role Variations

Shown to any role — Member, Instructor, Admin — whenever their email is unverified. Content is otherwise identical across roles; only the destination after successful verification differs.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
