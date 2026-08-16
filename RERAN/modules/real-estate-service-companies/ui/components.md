---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/ui/screens/"
tags:
  - real-estate-service-companies
  - ui-spec
  - components
---

# Shared Component Library

UI components reused across screens in this module, gathered from every "Reused Components" list across all 12 screen files — not templated from another module in advance.

## Layout & Chrome

### Company Operations Sidebar

The persistent navigation sidebar shown on every operational screen. See `navigation.md` for the full menu structure and access rules. Identical for every user, regardless of role.

### Top Bar

Page header: title, subtitle, search, and page-specific actions. Used on all 12 screens.

### Company Context Header

Company licence status badge and expiry countdown. Used on Dashboard and Applications, mirroring Financial & Trust Institutions' Institution Context Header pattern, since Service #12 plays the same institutional-standing role that module's Service #1 does.

## Data Display

### KPI Summary Cards

Summary metric cards near the top of list screens. Used on Dashboard, Applications, Jointly Owned Property, and Documents.

### Data Table

Tabular list with sortable/filterable columns. Used on Applications, Jointly Owned Property, Documents, and Company Profile's staff roster.

### Information Cards

Read-only field display, used on Service Details, Submit Application, Application Review, and Application Details.

### Status Badge

Colour-coded status indicator. See `status-badges.md` for the full vocabulary set. Used on every screen that displays a record's state.

### Audit Timeline

Reverse-chronological event history: actor, role held at time of action, action, timestamp, reason where given. Used on Application Details.

### Empty State

Illustration, message, and primary/secondary actions. Message and actions defined per screen. Used on Applications, Jointly Owned Property, Documents, and Notifications.

## Progress & Workflow

### Progress Tracker

A horizontal stepper showing a record's position in its pipeline: `Draft → Submitted → RERA Review → Approved → Completed`. Used on Submit Application and Application Details.

**Corrected 2026-08-16, by client decision (`open-questions.md` B4).** This component previously carried an additional **Payment Pending** step between Approved and Completed, scoped to Services #12–15's then-sourced post-decision payment timing. That timing is normalized as of 2026-08-16 — these four services now pay upfront, before lodging, resolving payment before `Submitted` rather than after `Approved`. The tracker is now a single four-stage definition, used identically for every service in the module.

**This module needed no `Pending Internal Certification` step**, unlike Financial & Trust Institutions' equivalent component, since no Group D service sources an internal company-side certification gate (`open-questions.md` A5). **With both corrections, Group D's Progress Tracker is now the simplest of any module documented so far** — no internal-certification branch, and, as of 2026-08-16, no payment-timing branch either.

## Forms & Inputs

### Document Uploader

Drag-and-drop plus file picker, showing required vs. optional documents for the selected service. Used on Submit Application and Application Details.

### Repeatable Field Group

A block of sub-fields that can be added or removed as a unit. Used on Submit Application's Service-Specific Details step for **Pattern B**, currently only Service #7 (Accredit Escrow Signatories — one group per proposed signatory).

**Reused from Financial & Trust Institutions' equivalent component definition, not redefined from scratch** — the underlying interaction pattern (Add Another / Remove controls, independent per-group validation) is identical.

### Conditional Field Selector

A checklist of available attributes, where checking an item reveals a Current Value / Requested New Value input pair for that attribute only. Used on Submit Application's Service-Specific Details step for **Pattern C**, currently only Service #17 (Amend Professional Practice Card).

**Reused from Financial & Trust Institutions' equivalent component definition** (that module's own Service #15 uses the identical pattern), for the same reason as Repeatable Field Group above.

## Actions & Navigation

### Search Bar

Free-text search input. Used on Services Catalog.

### Filter Bar

Search field plus dropdown filters and a Reset action. Used on Applications, Jointly Owned Property, and Documents.

### Pagination

Rows per page, Previous, Next, page number, total records. Used on every table-based list screen.

### Quick Action Cards

Shortcut cards linking to common next actions. Used on Dashboard only.

### Buttons

Primary, secondary, destructive. Used on every screen.

## Screen-Specific, Single Occurrence

Included per the same "one definition per component, gathered from every mention" convention Real Estate Developer's `components.md` uses — a future screen needing the same pattern should reuse the definition here rather than re-describing it.

* **Property Detail Panel** — Jointly Owned Property's own per-property drill-down, showing a property's full JOP history across all applicable services.
* **Ticket List** — Help & Support's Support Tickets section.

## Not Yet Designed

**Service #18's own atypical screen.** Confirmed to stay in Group D (`open-questions.md` A2), but its sourced workflow — an evaluation company deciding on a customer's request, not a company filing an application RERA reviews — doesn't fit any component defined above. No new component is proposed here ahead of that screen's actual design, per this document's own opening principle: components are gathered from built screens, not templated in advance of them.
