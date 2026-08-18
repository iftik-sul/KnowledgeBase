---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - registration
  - safeguarding
---

# Screen: Registration — 13–17 Standalone

Satisfies: FR-AUTH-05

---

## Purpose

Reached when date of birth on [Registration — Adult](registration-adult.md) resolves to 13–17. Captures the same base fields plus guardian name and guardian email.

## Fields

All fields from [Registration — Adult](registration-adult.md), plus: guardian name, guardian email (FR-AUTH-05). Neither guardian field is validated against an existing account — the guardian named here need not have a 3i account at all.

## Behaviour

On submit, an automatic notification is sent to the guardian email, naming the institute and linking to the privacy policy (FR-AUTH-05). The event is logged with timestamp and address — required by the module's acceptance criteria, not optional instrumentation.

After submission, shows the [Guardian Notification Banner](../components.md#guardian-notification-banner) confirming the notification was sent, with the guardian email partially masked.

This screen does not gate the teenager's own registration on the guardian's response — the notification is informational, not a consent gate requiring guardian action before the account activates. (The baseline does not specify a consent-gate requirement here; confirm this reading if it matters commercially.)

## Role Variations

None — public only.

## Contrast and RTL

As [Registration — Adult](registration-adult.md). The [Guardian Notification Banner](../components.md#guardian-notification-banner) text is a safeguarding-adjacent string but is not itself in the exempt set defined in [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) — only the notification's own content, sent to the guardian, is exempt.
