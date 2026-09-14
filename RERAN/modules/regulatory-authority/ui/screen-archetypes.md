---
project: RERAN
module: regulatory-authority
type: ui-archetypes
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/ui/screens/work-queue.md"
  - "RERAN/modules/regulatory-authority/ui/screens/application-review.md"
  - "RERAN/modules/regulatory-authority/service-flows/"
tags:
  - regulatory-authority
  - ui-spec
  - archetypes
---

# Group A — Screen Archetypes

Group A's ~16 active back-office screens reduce to **five archetypes**. Every screen spec
declares which archetype it follows, so section shapes stay consistent and we don't
reinvent layout per screen. This is the back-office analogue of a design pattern library
at the spec level.

> **Note.** These archetypes are defined against the specs. Their concrete section shapes
> and component choices will be reconciled to the actual Figma component library in the
> Figma thread; treat the component names here as generic until then.

## Archetype 1 — Queue

A worklist the reviewer triages from. Row click opens a Detail/Decision screen.

**Section shape:** Summary Cards (KPIs, click-to-filter) → Filters & Search → Table →
Pagination. No decision is taken on the queue itself.
**Used by:** Work Queue (A-1, A-2); Case Queue (A-3); Inspection/Enforcement/Sign-off
queues (A-7/A-8/A-10, latent).

## Archetype 2 — Detail / Decision

Open one item; see everything needed to decide; record an outcome.

**Section shape:** Item Header → context panels (application, documents, live checks) →
Decision Panel (mutually exclusive outcomes + mandatory reason where required) →
collapsible Activity/Audit. The Decision Panel is enabled only for the item's primary
decision role.
**Used by:** Application Review (A-1, A-2). The Case Workspace (A-3) is a specialised
multi-session variant (Archetype 5).

## Archetype 3 — Editor / Config

Create, edit, and publish/commit records — CRUD with versioning, not a queue.

**Section shape:** Record List (or directory) → Record Editor (form) → Commit/Publish
action → Version/History. No SLA, no applicant, no four-outcome decision; the "outcome"
is saved/published.
**Used by:** Fee Schedule Editor (A-4); Admin Console (A-6); the writable parts of the
Practitioner Register (A-2).

## Archetype 4 — Dashboard / Monitor

A read-first landing or monitoring surface: at-a-glance state, drill into detail.

**Section shape:** Header → KPI/summary tiles → charts or grouped lists → drill-in links.
Little or no direct action; it routes the user to the screens that act.
**Used by:** Dashboard (all roles, role-scoped tiles); Reconciliation Dashboard (A-5).

## Archetype 5 — Case Workspace

A hub for a matter worked over multiple sessions across time — not a single decision.

**Section shape:** Case Header → Parties & Evidence → Session Timeline (schedule/conduct
sessions, request info between them) → Judgment/Resolution (recorded once, closes the
case). Its status is a case lifecycle, not the shared four-state decision vocabulary.
**Used by:** Case Workspace (A-3) only. It is deliberately its own archetype because it is
the one Group A screen that is not an approve/reject.

## Quick map

| Screen | Archetype |
| :-- | :-- |
| Work Queue, Case Queue | 1 Queue |
| Application Review | 2 Detail / Decision |
| Fee Schedule Editor, Admin Console, Practitioner Register (write) | 3 Editor / Config |
| Dashboard, Reconciliation Dashboard | 4 Dashboard / Monitor |
| Case Workspace | 5 Case Workspace |
| Audit Trail view | 1 Queue (read-only, no decision) |
