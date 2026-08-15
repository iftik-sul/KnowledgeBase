---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-15
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - real-estate-developer
  - ui-spec
---

# Screen: Project Details

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described two designs — an executive project overview (Developer Principal / Director) and an operational registration workspace (Project Registration Officer) — with different sections, different information groupings and, critically, a Validation Summary present in only one of them. Both are **retired**; this is one screen absorbing the load-bearing content of each.

## Purpose

The detail view of a single development project, opened from [Projects](projects.md). Covers the project's registration progress, its full information record, its documents, its regulatory correspondence, and the sales, escrow and compliance position that sits against it — with the controls to edit, validate, submit and correct the registration. Any user may do any of it.

## Layout

```
Top Bar
↓
Project Header
↓
Project Summary Cards
↓
Registration Progress
↓
Project Information
↓
Required Documents
↓
Validation Summary
↓
RERA Queries
↓
Linked Position (Sales · Escrow · Compliance)
↓
Activity Timeline
```

## Sections

### Section 1 — Project Header

**Left**

* Project Name
* Project ID / Registration Number
* Location
* Current Status badge
* Development Stage

**Right**

* **Edit Project** · **Submit to RERA** · **Register Properties** · **Download Summary**

**Reconciled 2026-08-15:** the overview variant's header carried navigation actions only; the workspace variant's carried the edit/submit set. The full action set now applies to every user, subject to project status — a submitted project still cannot be edited by anyone.

### Section 2 — Project Summary Cards

Absorbed from the overview variant, which was the only one to define them: unit counts, registered properties, sales position, escrow position and outstanding compliance items for this project.

### Section 3 — Registration Progress

Stage tracker for the project's regulatory journey — present in **both** variants, and the one section they broadly agreed on. The workspace variant's stage list is the more granular of the two and is the one kept; the overview variant's stages map onto it without loss.

### Section 4 — Project Information

**General / Basic Information**

Project name, reference, type, location, land details, plot size, approvals, registration date.

**Development Information** *(workspace variant only)*

Number of phases, unit counts by type, construction start and expected completion, survey company.

**Responsible Personnel / Contacts**

Named contacts against the project.

**Reconciled 2026-08-15:** the overview variant grouped this as *General Information* + *Responsible Personnel*; the workspace variant as *Basic Information* + *Development Information* + *Responsible Contacts*. The three-group structure is kept, since *Development Information* is real content the overview variant simply omitted. The role labels inside Responsible Personnel are **descriptive attribution** — who is named against the project — not access assignments.

### Section 5 — Required Documents

Document checklist and table, with Upload / Replace / Preview / Resubmit actions per row, governed by document status.

**Reconciled 2026-08-15:** the overview variant had a *Documents* section listing submitted documents with view-only actions; the workspace variant had *Required Documents* with a checklist of what is mandatory plus upload controls. The workspace version is the superset — it shows the same submitted documents *and* what is still missing — so it is the one kept, with the overview variant's columns folded in.

### Section 6 — Validation Summary

Automatic pre-submission checks, displayed as Passed / Warning / Error, with the primary submit action disabled until all mandatory checks pass.

**Reconciled 2026-08-15 — this section now applies to every user.** It existed only in the workspace variant; the overview variant had none, because that variant could not submit. That was an access restriction, not a property of the screen. See [validation-rules.md](../validation-rules.md).

### Section 7 — RERA Queries

Table of regulatory queries against this project — query, raised date, due date, status, response — with Respond and Upload actions.

Absorbed from the workspace variant. The overview variant carried the same information as read-only *Compliance* content; consolidated here.

### Section 8 — Linked Position

**Absorbed 2026-08-15** from the overview variant's *Sales Overview*, *Escrow Overview* and *Compliance* sections — the monitoring content the workspace variant lacked entirely. Retained as condensed summary cards, each linking out rather than duplicating detail.

* **Sales** — units sold, active listings, pending disclosures against this project. Links to [sales-and-disclosures.md](sales-and-disclosures.md).
* **Escrow** — the project's escrow account, balance, current milestone and pending releases. Links to [escrow-management.md](escrow-management.md). *(Project escrow account figures — not RERA fees.)*
* **Compliance** — outstanding regulatory items and their severity.

### Section 9 — Activity Timeline

Chronological record of everything that has happened to this project. Organization-wide, not filtered to the viewer — each entry shows who acted and what role they held at the time ([navigation.md](../../navigation.md#audit-trail-principle)).

**Reconciled 2026-08-15:** the overview variant called this *Recent Activity* and showed the latest few; the workspace variant called it *Activity Timeline* and showed the full history. Kept as the full timeline, which contains the other.

## Empty State

Applies to a newly created project with no documents, queries or linked records yet.

> This project has no submitted documents yet. Upload the required documents to move the registration forward.

**Primary Button** — Upload Documents

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

1. No section, field, action or card on this screen is role-gated. What a user can do depends on the project's status, never on who they are.
2. Fields become read-only after submission unless RERA returns the project — a lifecycle rule that applies to every user equally.
3. Validation Summary checks are defined in [validation-rules.md](../validation-rules.md) and are not restated here.
4. Linked Position figures must match their source screens exactly; this screen computes nothing independently.

## User Flow

```
Projects
↓
Project Details
├─ Edit / Submit → registration flow
├─ Register Properties → Property Registrations
├─ Document row → Document Details
├─ RERA Query → response flow
└─ Linked Position link → Sales / Escrow / Reports
```

## Notes

* **This absorbs, rather than references, both retired variants.** Their headers, progress trackers, information groupings, document tables, query tables, monitoring summaries and timelines are now one screen.

* **The Validation Summary asymmetry was the substantive merge decision.** [validation-rules.md](../validation-rules.md) recorded that the overview variant had no Validation Summary "because those screens are read-only for that role." That reasoning does not survive unified access — the section is a property of submitting a project, and every user can now submit. It applies to everyone.

* **What was dropped, and why.** Only the navigation-only header actions and the read-only framing. Nothing representing distinct work was discarded — the overview variant's Project Summary Cards, Sales Overview, Escrow Overview and Compliance sections are all carried forward as Sections 2 and 8, and the workspace variant's Development Information, Required Documents checklist, Validation Summary and RERA Queries are all kept.
