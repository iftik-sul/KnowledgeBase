---
project: RERAN
module: regulatory-authority
type: ui-archetypes
status: draft
contains_proposals: true
updated: 2026-09-18
derived_from:
  - "RERAN/modules/regulatory-authority/ui/screens/work-queue.md"
  - "RERAN/modules/regulatory-authority/ui/screens/application-review.md"
  - "RERAN/modules/regulatory-authority/service-flows/"
tags:
  - regulatory-authority
  - ui-spec
  - archetypes
---

# Regulatory Authority — Screen Archetypes

The Regulatory Authority's ~16 active back-office UI surfaces reduce to **five
archetypes**. They are delivered as **10 screen specs** in `screens/` — some specs
bundle related surfaces (the Admin Console spec covers staff directory, account editor,
and role/permission editor; the dispute pair of Case Queue + Case Workspace covers the
queue, session, and judgment surfaces; Reconciliation covers reconciliation and
remittance). Every screen spec declares which archetype it follows, so section shapes
stay consistent and we don't reinvent layout per screen.

> **Note.** These archetypes are defined against the specs. Their concrete section shapes
> and component choices are reconciled to the real Figma component library during design
> work; treat the component names here as generic.

## Archetype 1 — Queue

A worklist the reviewer triages from. Row click opens a Detail/Decision screen.

**Section shape:** Summary Cards (KPIs, click-to-filter) → Filters & Search → Table →
Pagination. No decision is taken on the queue itself.
**Empty state (required):** every Queue screen states what an empty list means — "you
are clear" is different from "a filter hides everything" and from "nothing has arrived
yet". A blank table is never acceptable.
**Used by:** Work Queue (A-1, A-2); Case Queue (A-3); the Inspection queue (A-7) and
Sign-off queue (A-10), both in scope but not yet specced; Enforcement queues (A-8,
deferred).

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
**Used by:** Case Workspace (A-3) only. It is deliberately its own archetype because it
is the one Regulatory Authority screen that is not an approve/reject.

## Quick map

| Screen | Archetype |
| :-- | :-- |
| Work Queue, Case Queue | 1 Queue |
| Application Review | 2 Detail / Decision |
| Fee Schedule Editor, Admin Console, Practitioner Register (write) | 3 Editor / Config |
| Dashboard, Reconciliation Dashboard | 4 Dashboard / Monitor |
| Case Workspace | 5 Case Workspace |
| Audit Trail view | 1 Queue (read-only, no decision) |
