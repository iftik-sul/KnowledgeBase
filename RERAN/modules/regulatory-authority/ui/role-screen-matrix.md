---
project: RERAN
module: regulatory-authority
type: ui-rbac-matrix
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/roles-and-responsibilities.md"
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/service-flows/"
tags:
  - regulatory-authority
  - ui-spec
  - rbac
  - navigation
---

# Group A — Role × Screen Matrix (RBAC backbone)

This is where RBAC lives at the UI level. It states, for each of the eight Group A
roles, **which screens the role can reach**. It is the navigation spec for the back-office
app. On-screen actions are owned by the individual screen specs (see §2).

**The principle (do not build per-role screens).** There is one screen per piece of
work. This matrix does not create screen copies; it controls access to the shared
screens and the actions available on them. Where a cell says a role can reach a screen,
it opens the *same* screen every other permitted role opens — its permissions differ,
not its layout.

## 1. Navigation matrix — which role reaches which screen

`●` = in this role's sidebar / reachable · blank = not reachable.

| Screen | C&E Auditor | Licensing Officer | Dispute Officer | Super Admin | Revenue & Finance | DG/Registrar | Inspection & Enf. | State Liaison |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Dashboard | ● | ● | ● | ● | ● | ● | ● | ● |
| Work Queue — transaction | ● | | | | | | | |
| Work Queue — escrow | ● | | | | | | | |
| Work Queue — licensing | | ● | | | | | | |
| Application Review | ● | ● | | | | | | |
| Case Queue / Case Workspace | | | ● | | | | | |
| National Practitioner Register | | ● | | | | | | |
| Admin Console (staff / roles / permissions) | | | | ● | | | | |
| Fee Schedule Editor | | | | | ● | | | |
| Reconciliation / Remittance | | | | | ● | | | |
| Audit Trail view | ● | ● | ● | ● | ● | ● | ● | ● |
| Inspection screens *(latent)* | | | | | | | ● | |
| Enforcement screens *(latent)* | | | | | | ● | ● | |
| Harmonisation screens *(latent)* | | | | | | | | ● |
| Sign-off screens *(latent)* | | | | | | ● | | |

> **Proposed.** The DG/Registrar, Inspection & Enforcement, and State Liaison rows map
> to latent screens (open-questions A5); their navigation is defined for RBAC
> completeness but the screens are deferred. Super Admin sees the Admin Console only —
> not every other role's work screens — following least-privilege; a "break-glass"
> override, if wanted, is a separate decision. **Needs client confirmation.**

## 2. On-screen actions live in the screen specs, not here

This matrix governs **navigation only** — which screens a role can reach. What a role can
*do* on a reachable screen (view vs decide, which panels/controls are enabled, which
columns show) is defined once, per screen, in that screen spec's **Role Variations /
Permissions** section. This file deliberately does not restate on-screen actions, so the
two never drift: navigation is owned here, actions are owned by the screens.

Reaching a screen (a ● above) never by itself implies permission to act on it — the
screen spec decides that.

## 3. Cross-cutting rules

- **MFA is required** for every role before any screen can be acted on (per A-6).
- **A role with no functional screens built yet** (DG, Inspection, State Liaison in the
  first build) still exists in the permission model and can be assigned; it simply has
  little or nothing in its sidebar until its screens are built.
- **One person can hold more than one role**; their sidebar is the union of their roles'
  reachable screens, and their actions the union of their roles' permissions.

> **Proposed** — the exact per-screen permission refinements are first-pass and need
> confirmation against RERA's actual separation-of-duties rules (e.g. whether the same
> officer who requests info can also later approve the same item).
