---
project: 3i
module: localisation
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-LCL-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Localisation — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## Locale Switcher

Used globally, across every module's public and authenticated screens — not owned by any one screen in this module.

A simple five-option selector (FR-LOC-01), always available in the platform's global chrome. Selecting a locale sets the visitor's session locale (and, for an authenticated Account, updates `Account.locale`, read by `communication` for FR-LOC-05's notification routing). Selecting `ur` or `ar` triggers the full RTL layout switch (FR-LOC-04) — this component is the single trigger point for that switch, even though the mirroring behaviour itself is implemented per-screen across every module.

## Translation Status Indicator

Used on: [Admin Translation Management](screens/admin-translation-management.md), [Exempt String Sign-Off](screens/exempt-string-signoff.md).

For an ordinary string: AI-generated (default) or admin-corrected — two states, both equally "live." For an exempt string: no sign-off yet (falls back to English), or signed off (live in that language) — these are not the same two-state system as ordinary strings and the indicator renders them visibly differently, since one pair describes translation quality and the other describes whether the string is even showing at all in that locale.