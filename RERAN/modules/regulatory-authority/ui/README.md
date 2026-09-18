---
project: RERAN
module: regulatory-authority
type: ui-readme
status: draft
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/service-flows/"
tags:
  - regulatory-authority
  - ui-spec
  - back-office
---

# Regulatory Authority — UI (Back-Office App)

The Regulatory Authority's UI is the **back-office / staff app**, distinct from the
applicant-facing portals every other module documents. Per the monorepo decision it is a
separate app. Its screens are queues, review screens, and admin consoles — not
submission wizards.

## The two things that make the Regulatory Authority's UI different

1. **RBAC is real here.** Everywhere else a role is audit attribution only and gates
   nothing. In the back-office app, the role decides **which screens a user can reach**
   (navigation) and **what they can do on a screen** (actions). See
   [role-screen-matrix.md](role-screen-matrix.md) — the RBAC backbone the screens hang
   off — and the "Role Variations / Permissions" section in every screen spec.
2. **Screens are defined by the work, not by the role.** There is **one screen per piece
   of work**, shared across the roles that do that work; the role controls access and
   actions on top. We do **not** build a separate screen per role — that would multiply
   the build and create drift. If two roles work the same queue, they use the same
   screen with different permissions.

## Screen inventory

Consolidated from the 10 service-flows (most name the same patterns). A screen is built
where an active service routes or escalates work into it; the rest are deferred
(open-questions A5).

| Screen | Serves | Status |
| :-- | :-- | :-- |
| Back-office shell (sidebar + top bar) | all | Active (chrome) |
| [Dashboard](screens/dashboard.md) | all | Active |
| [**Work Queue**](screens/work-queue.md) (transaction / escrow / licensing views) | A-1, A-2 | **Active — build first** |
| [**Application Review**](screens/application-review.md) (+ decision panel) | A-1, A-2 | **Active — build first** |
| [Notifications](screens/notifications.md) | all | Active |
| [Audit Trail](screens/audit-trail.md) | all | Active |
| [Case Queue](screens/case-queue.md) · [Case Workspace](screens/case-workspace.md) | A-3 | Active (session + judgment are sections of the workspace) |
| [National Practitioner Register](screens/practitioner-register.md) | A-2 | Active |
| [Admin Console](screens/admin-console.md): Staff Directory · Account Editor · Role & Permission Editor | A-6 | Active |
| [Fee Schedule Editor](screens/fee-schedule-editor.md) | A-4 | Active |
| [Reconciliation Dashboard](screens/reconciliation.md) · Remittance (tab) | A-5 | Active |
| Inspection queue · on-site capture · inspection report | A-7 | **In scope — not yet specced** (mobile/tablet) |
| Sign-off queue · sign-off detail | A-10 | **In scope — not yet specced** |
| Enforcement screens | A-8 | Deferred |
| Harmonisation screens | A-9 | Deferred |

## Folder structure

- [`role-screen-matrix.md`](role-screen-matrix.md) — which role reaches which screen (the RBAC/navigation
  backbone). On-screen actions are owned by the screen specs.
- [`screen-archetypes.md`](screen-archetypes.md) — the five layout archetypes every screen spec declares.
- `screens/` (linked in the inventory above) — the screen specs (this layer; derived from service-flows).
- [`modals.md`](modals.md) — every modal, confirmation, and alert, by ID. Screens reference a modal
  by its ID; they never restate its wording, fields, or rules.
- [`components.md`](components.md), [`status-badges.md`](status-badges.md), [`validation-rules.md`](validation-rules.md) — supporting docs. Status
  wording is owned by status-badges; guard rules by validation-rules.
- [`flows/`](flows/compliance-escrow-auditor.md) — end-to-end user journeys, one per role. Where the matrix says what a role
  can reach and the screen specs say what a screen contains, a flow says what happens
  in what order and what the user sees between screens.

## Derivation

service-flows → **screen specs (here)**. The specs are the source of truth for behaviour.
Figma build prompts are **not kept in the KnowledgeBase** for this module — they proved to
drift from the specs they claimed to derive from, and design work happens in Figma itself.
