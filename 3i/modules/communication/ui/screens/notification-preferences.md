---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CMN-UI-006
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - notifications
---

# Screen: Notification Preferences

Satisfies: FR-NOT-01, FR-NOT-03

---

## Purpose

Per-category push/email opt-out.

## Access Gate

Any authenticated role, managing their own preferences only.

## Contents

Four rows — Learning Updates, Billing, Chat \& Moderation, Instructor (shown only to accounts that have an instructor application on file, current or past; irrelevant otherwise and not shown as a dead toggle) — each with independent push and email switches (FR-NOT-01's two channels).

**Account verification does not appear on this screen at all** — not a toggle set to permanently-on, genuinely absent, since it isn't part of the category system (see [README.md](/3i/modules/communication/README.md#notification-categories--confirmed-grouping)). A Member should never wonder why one toggle can't be turned off; the cleaner answer is that it was never a toggle.

**Chat \& Moderation carries no special copy or warning distinguishing it from the other three** — confirmed no safety exemption, so the screen doesn't editorialise about it being a more consequential category to opt out of than Billing.

## Behaviour

Changes apply immediately, affecting only notifications sent from that point forward — nothing already in the [Notification Centre](notification-centre.md) is affected retroactively.

## Role Variations

Identical across roles, differing only in whether the Instructor row is shown.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): toggle switches mirror their on/off visual direction along with the rest of the layout.