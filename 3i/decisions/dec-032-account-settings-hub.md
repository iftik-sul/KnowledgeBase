---
project: 3i
type: decision
status: current
updated: 2026-08-24
id: 3I-DEC-032
tags: [decision, navigation, ux, identity-and-access, commerce]
---

# Account Settings Hub Sits Between the Account Menu and Its Destinations

## Context

[3I-DEC-031](dec-031-persistent-account-menu-entry-to-guardian-dashboard.md) gave the Account Menu a single destination: "Manage account" → [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md). Designing the actual screens behind it surfaced that this is too narrow — "account settings" genuinely covers four different areas, only one of which is Guardian Dashboard's job:

1. **Family & profiles** — Guardian Dashboard's actual scope.
2. **Devices** — [Device Management](/3i/modules/identity-and-access/ui/screens/device-management.md) exists, satisfies FR-AUTH-11, but has never stated how a Member reaches it. Same shape of gap DEC-031 fixed for Guardian Dashboard, one screen over.
3. **Subscription & billing** — lives entirely in `commerce` ([Seat Management](/3i/modules/commerce/ui/screens/seat-management.md), [Billing Portal Redirect](/3i/modules/commerce/ui/screens/billing-portal-redirect.md)). [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md)'s own per-profile "Activate," "Reactivate," and "Cancel seat" buttons already reference "seat purchase (`commerce`)" without naming a screen — an unresolved link, not a deliberate simplification.
4. **Login & security** — email and password changes. Grounded in the requirements ("Email changes require re-verification," [`auth-registration-and-authentication.md`](/3i/modules/identity-and-access/requirements/auth-registration-and-authentication.md#email-changes-require-re-verification)) but **no screen has ever existed for this** — not a redirect gap like the other three, a genuinely missing screen.

## Decision

**A new screen, Account Settings, sits between the Account Menu and all four destinations.** The Account Menu's "Manage account" item now routes here, not directly to Guardian Dashboard.

Account Settings is a simple list of four sections, each routing onward:

| Section | Routes to | Status before this decision |
| :---- | :---- | :---- |
| Family & profiles | [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md) | Existed, was the Account Menu's sole destination |
| Devices | [Device Management](/3i/modules/identity-and-access/ui/screens/device-management.md) | Existed, unreachable — no "reached from" anywhere |
| Subscription & billing | [Seat Management](/3i/modules/commerce/ui/screens/seat-management.md) | Existed, referenced vaguely as "`commerce`" from Guardian Dashboard's buttons |
| Login & security | **New screen**, [`login-security.md`](/3i/modules/identity-and-access/ui/screens/login-security.md) | Did not exist |

**A second, smaller fix rides along with this:** [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md)'s "Activate," "Reactivate," and "Cancel seat" buttons now route specifically to [Seat Management](/3i/modules/commerce/ui/screens/seat-management.md), scoped to the profile clicked from, rather than a vague reference to the module. [Seat Management](/3i/modules/commerce/ui/screens/seat-management.md) already owns the cancellation confirmation copy and the add-seat path to [Pricing / Plan Selection](/3i/modules/commerce/ui/screens/pricing-plan-selection.md) — Guardian Dashboard's buttons hand off to it rather than duplicating that logic.

**Role scope:** Account Settings' Family & Profiles and Subscription & Billing sections are Member-only, matching what those destinations already require. Devices and Login & Security are shown to any authenticated role — Member, Instructor, Admin — consistent with [Device Management](/3i/modules/identity-and-access/ui/screens/device-management.md) already being available to all three.

## Consequences

- New screen: `account-settings.md` (`3I-IDA-UI-017`), the hub itself.
- New screen: `login-security.md` (`3I-IDA-UI-018`) — email change (triggers re-verification per the existing settled rule) and password change (FR-AUTH-08's policy, applied to a change as much as an initial set).
- [`components.md`](/3i/modules/identity-and-access/ui/components.md)'s Account Menu entry updated: "Manage account" routes to Account Settings, not Guardian Dashboard directly.
- [`guardian-dashboard.md`](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md)'s own "reached from" statement updated to name Account Settings' Family & Profiles section specifically, and its seat-related buttons now cite Seat Management by name.
- [`device-management.md`](/3i/modules/identity-and-access/ui/screens/device-management.md) gains the "reached from" statement it never had.
- `ui/README.md`'s matrix and `mobile-scope.md`'s totals both grow by two screens (15→17 module screens, 68→70 project-wide).

## Cost

One extra click between the Account Menu and Guardian Dashboard, for what was previously the single most common destination. Accepted deliberately: three more real destinations exist behind "manage account" than the menu currently admits, and folding them all into an ever-longer dropdown, or silently expanding Guardian Dashboard's own scope to cover billing and login credentials, would have been worse than one small hub screen.
