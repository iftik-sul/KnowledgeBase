---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-24
id: 3I-IDA-UI-017
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - account
figma: null
---

# Screen: Account Settings

---

## Purpose

The hub between the [Account Menu](../components.md#account-menu) and every account-level area of the platform. Introduced by [3I-DEC-032](/3i/decisions/dec-032-account-settings-hub.md) to resolve four destinations that had either no route to them, or an under-specified one.

## Content

A simple list of four sections, each a large tappable row with an icon, a title, and a one-line description:

| Section | Description | Routes to |
| :---- | :---- | :---- |
| Family & profiles | Manage learner profiles, PINs, and seats | [Guardian dashboard](guardian-dashboard.md) |
| Devices | See and remove devices signed into your account | [Device management](device-management.md) |
| Subscription & billing | View your plan, payment method, and invoices | [Seat Management](/3i/modules/commerce/ui/screens/seat-management.md) |
| Login & security | Update your email and password | [Login & security](login-security.md) |

## Role Variations

**Family & profiles** and **Subscription & billing** are Member-only — an Instructor or Admin account holds no learner profiles or seats. **Devices** and **Login & security** are shown to any authenticated role (Member, Instructor, Admin), matching [Device management](device-management.md)'s existing availability to all three.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): row order and icon direction mirror in Arabic and Urdu.
