---
project: RERAN
module: regulatory-authority
type: ui-readme
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/service-flows/"
tags:
  - regulatory-authority
  - ui-spec
  - back-office
---

# Group A — UI (Back-Office App)

Group A's UI is the **back-office / staff app**, distinct from the applicant-facing
portals every other module documents. Per the monorepo decision it is a separate app.
Its screens are queues, review screens, and admin consoles — not submission wizards.

## The two things that make Group A's UI different

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

Consolidated from the 10 service-flows (most name the same patterns). Active screens are
built now; latent screens are deferred with their latent service-flows (open-questions A5).

| Screen | Serves | Status |
| :-- | :-- | :-- |
| Back-office shell (sidebar + top bar) | all | Active (chrome) |
| Dashboard | all | Active |
| **Work Queue** (transaction / escrow / licensing views) | A-1, A-2 | **Active — build first** |
| **Application Review** (+ decision panel) | A-1, A-2 | **Active — build first** |
| Audit Trail view | all | Active |
| Case Queue · Case Workspace · Session view · Judgment record | A-3 | Active |
| National Practitioner Register | A-2 | Active |
| Admin Console: Staff Directory · Account Editor · Role & Permission Editor | A-6 | Active |
| Fee Schedule Editor | A-4 | Active |
| Reconciliation Dashboard · Remittance | A-5 | Active |
| Inspection · Enforcement · Harmonisation · Sign-off screens | A-7–A-10 | Latent (deferred) |

## Folder structure

- `role-screen-matrix.md` — which role reaches which screen (the RBAC/navigation
  backbone). On-screen actions are owned by the screen specs.
- `screen-archetypes.md` — the five layout archetypes every screen spec declares.
- `screens/` — the screen specs (this layer; derived from service-flows).
- `modals.md` — every modal, confirmation, and alert, by ID. Screens reference a modal
  by its ID; they never restate its wording, fields, or rules.
- `components.md`, `status-badges.md`, `validation-rules.md` — supporting docs. Status
  wording is owned by status-badges; guard rules by validation-rules.
- `figma-prompts/` — the Figma AI prompts, derived from the finished specs. Built last,
  never before the specs.

## Derivation

service-flows → **screen specs (here)** → figma-prompts. Specs are the source of truth
for behaviour; figma-prompts reference the existing Figma component library generically.
