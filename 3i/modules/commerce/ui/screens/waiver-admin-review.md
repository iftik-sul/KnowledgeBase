---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-CMR-UI-007
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - waivers
  - admin
---

# Screen: Waiver Admin Review

> **⚠ Provisional — see [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md).** This screen's Figma design was completed and confirmed against the current learner-facing design system, but the admin/instructor portal will use a separate, not-yet-specified visual design. Do not treat the existing Figma work as final — it will need revisiting, not just extending, once that direction exists. The spec below is unaffected and remains current.

Satisfies: FR-WAV-02, FR-WAV-05, FR-WAV-07, FR-WAV-09

---

## Purpose

Admin reviews a pending waiver request, approves at one of four fixed tiers or rejects, and can later revoke an active waiver.

## Access Gate

Web only. Admin only.

## Contents

- The written explanation and any evidence files, accessed only via short-lived signed URLs — every access to an evidence file is logged (FR-WAV-07). No direct file link or CDN URL is ever rendered.
- **The covered profile**, with its [Tier Badge](../components.md#tier-badge), plus a count of how many other profiles are currently on the account and will be auto-deactivated if this request is approved. This count is the admin-side equivalent of the warning on the request form — the reviewer should see the consequence too, not just approve blind.
- **Tier selector** — one of the four fixed discount percentages, 25/50/75/100% (FR-WAV-02). No free-text or custom percentage field exists.
- **Approve / Reject** actions. Approving immediately (a) activates the waiver at the next renewal per FR-WAV-03, (b) auto-deactivates every other profile on the account in the same action ([3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md)) — no separate confirmation step, no pending-but-not-active state — and (c) records the full audit trail (FR-WAV-09): reviewer, decision, tier, and which profiles were auto-deactivated as a consequence.

## Revocation (Separate Action, Same Screen)

For an already-active waiver: a **Revoke** action with a required reason field. Triggers the account-holder notification by email and push (FR-WAV-05) and reverts full price at the account's **next billing date**, not immediately. Revocation does **not** restore any auto-deactivated profile — the account simply reverts to the normal six-profile cap, and re-adding profiles is the ordinary paid flow ([3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md)).

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
