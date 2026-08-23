---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-005
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - mobile
  - app-store-compliance
---

# Screen: Subscription Status (Mobile)

Satisfies: FR-BILL-02, NFR-18

---

## Purpose

**The only billing-related screen that exists on mobile.** Shown when an account has no active subscription — never sells, never links, never prices. See [app-store-compliance.md](/3i/app-store-compliance.md), which this screen is the concrete implementation of.

## Access Gate

Mobile (Flutter) only. Shown in place of course/learning content when `Subscription.status` is anything other than active — no active subscription, suspended, or cancelled. The apps do not distinguish between these states in what they show (see app-store-compliance.md §3) — all three get identical neutral treatment.

## Contents

- A neutral status sentence — no price, no urgency language, no call to action beyond the one below. Draft copy example: *"Your account doesn't currently have an active subscription."* Final copy needs the human-translation consideration flagged in [app-store-compliance.md §7](/3i/app-store-compliance.md#7-open) before being finalised in all five languages.
- **One action: a support email address**, opening the device's native mail client with a pre-filled subject line. Not a web view, not a deep link to any web page — see app-store-compliance.md §3 on why a web view is itself a risk here.

## Explicitly Absent

No price. No "Subscribe" button. No link to the website, checkout, or the billing portal. No mention of what a subscription costs or how to get one. This is the one screen in the whole platform where "what's missing" is the actual specification — see [app-store-compliance.md §6](/3i/app-store-compliance.md#6-what-would-break-this) for the specific mistakes to avoid when implementing this.

## Role Variations

None — a Member is the only role that reaches mobile course content, so this screen has no variation by role.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
