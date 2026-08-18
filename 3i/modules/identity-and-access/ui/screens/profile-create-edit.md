---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-009
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - profiles
  - safeguarding
---

# Screen: Profile Create / Edit

Satisfies: FR-FAM-01, FR-FAM-02, FR-FAM-03, FR-FAM-05, FR-FAM-07

---

## Purpose

Create a new learner profile, or edit an existing one within the limits of what remains editable.

## Access Gate

Only reachable by a Member whose own date of birth indicates 18+ (FR-FAM-01). A 13–17 standalone account never sees the entry point — the "Add profile" affordance is **absent**, not disabled, per [validation-rules.md](../validation-rules.md#guardian-age-gate-for-profile-creation).

## Fields — Create

Display name, date of birth, optional avatar, **mandatory 4-digit PIN set by the guardian** ([3I-DEC-018](/3i/decisions/dec-018-profile-pin-mandatory-guardian-controlled.md)) using the [PIN Pad](../components.md#pin-pad) component with confirmation entry.

Creation is free and does not touch a seat (FR-BILL-04 is a separate, later prompt). It is **not** rate-limited under FR-FAM-06 — that limit now applies only to activation and cancellation.

**Cap check on submit:** refused if the account already has 6 profiles counting active and never-activated ([3I-DEC-014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md)). The refusal message should distinguish this from a seat-availability message — they are different constraints and a Member conflating them will contact support about the wrong thing.

## Fields — Edit

Display name (until locked), avatar. **Date of birth has no edit control at all once set** — not disabled, absent (FR-FAM-07). **PIN can be reset** from here or from [Guardian dashboard](guardian-dashboard.md), guardian-only, no learner-facing path.

**Display name locks permanently once a certificate has been issued to the profile** (FR-FAM-05). Once locked, the name field either disappears or shows disabled with an explanatory message naming the reason, per [validation-rules.md](../validation-rules.md#profile-display-name). Admin may unlock on request with a reason recorded — that flow lives in `admin`, referenced but not detailed here.

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
