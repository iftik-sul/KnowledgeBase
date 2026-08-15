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

# Screen: Document Details

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described four designs: a master viewer (Developer Principal / Director) and three operational workspaces (Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison) for managing a document through verification. All four are **retired**; this is one screen absorbing the load-bearing content of each.

## Purpose

The detail view of a single document, opened from [Documents](documents.md). Covers the document itself, its metadata, the records it is linked to, its verification state, its version history and its regulatory correspondence — with the controls to replace it, upload revised versions and respond to queries. Any user may do any of it.

## Layout

```
Top Bar
↓
Document Header
↓
Document Summary Cards
↓
Verification Progress
↓
Document Preview
↓
Document Information
↓
Linked Records
↓
Verification Summary
↓
Version History
↓
RERA Queries & Review History
↓
Activity Timeline
```

## Sections

### Section 1 — Document Header

Document name, category, verification status badge, upload date, expiry date.

**Actions:** **Replace Document** · **Upload Revised Version** · **Preview** · **Download** · **Resubmit** · **Respond to Query**

Governed by document status. **Reconciled 2026-08-15:** the master viewer's header offered Preview and Download only — an access restriction, now retired.

### Section 2 — Document Summary Cards

Absorbed from the master viewer, the only variant to define them: version count, days since upload, days to expiry, and linked-record count.

### Section 3 — Verification Progress

Stage tracker for the document's verification journey.

**Absorbed 2026-08-15** from the three operational variants. The master viewer had no equivalent — it showed verification state as a static field rather than a tracker. Kept as the tracker.

### Section 4 — Document Preview

Embedded viewer with zoom, rotate, page navigation, full screen and download.

Present in **all four** variants with an identical feature list. **Reconciled:** the master viewer's Reused Components list called this "Document Viewer" and the operational variants' called it "Embedded Document Viewer" — [components.md](../components.md) recorded that naming divergence as probably-but-not-confirmed the same component. The identical feature lists confirm it. Kept as **Embedded Document Viewer**, and `components.md` is updated accordingly.

### Section 5 — Document Information

**Basic Information** — name, category, file type, size, upload date, uploaded by and the role held at the time.

**Administrative Information** — expiry, retention, confidentiality, source reference.

**File Information (Read-only)** — technical file attributes. **Kept read-only for everyone**: these are properties of the stored file, not editable fields. A data-integrity rule, not a permission.

### Section 6 — Linked Records

The records this document is filed against — project, property registration, application, sale or disclosure, escrow account or fund release — with reference, type and status.

**Absorbed 2026-08-15:** each variant scoped this table to its own domain. One table now covers all record types, rendered by what the document is actually linked to.

### Section 7 — Verification Summary

**Automatic Validation** — the six file-integrity checks, resolved from the three variants' differing lists. See [validation-rules.md](../validation-rules.md#document-upload-rules) for the resolution and the one flagged question.

**Regulatory Verification** — RERA's own verification outcome, reviewer and remarks.

**Reconciled 2026-08-15:** the master viewer had a *Verification Details* section carrying the regulatory outcome only, with no automatic-validation checks, because it could not upload. Both parts are present for every user.

### Section 8 — Version History

Table of versions — version number, uploaded date, uploaded by and role, file size, status, remarks — with Preview, Download and Restore actions where the document's status permits.

**Reconciled 2026-08-15:** the master viewer offered Preview and Download only. **Reconciled naming:** it called the component "Version History Component", the operational variants "Version History Table"; [components.md](../components.md) flagged the divergence and it is resolved to **Version History Table**.

### Section 9 — RERA Queries & Review History

**Absorbed 2026-08-15** by combining the operational variants' *RERA Queries* (open, with response actions) and the master viewer's *Review History* (the closed record of verification rounds). Open queries first, resolved history below — the same pattern used on [application-details.md](application-details.md).

### Section 10 — Activity Timeline

Everything that has happened to this document. Each entry shows who acted and what role they held at the time ([navigation.md](../../navigation.md#audit-trail-principle)).

## Empty State

> This document has no linked records yet. Link it to a project, registration, sale or escrow account so it counts toward that record's required documents.

## Reused Components

See [components.md](../components.md) — Embedded Document Viewer, Version History Table, Status Badges, Activity Timeline, File Upload Component, Buttons.

## Validation

1. No section, field, action or card on this screen is role-gated. What a user can do depends on the document's status, never on who they are.
2. File Information is read-only for everyone — it describes the stored file.
3. Automatic Validation checks are defined in [validation-rules.md](../validation-rules.md#document-upload-rules).
4. A verified document cannot be replaced without creating a new version — a lifecycle rule applying to everyone.

## User Flow

```
Documents
↓
Document Details
├─ Replace / Upload Revised Version → upload flow
├─ Respond to Query → response flow
├─ Linked Record → that record's detail screen
└─ Version row → previous version preview
```

## Notes

* **This absorbs, rather than references, all four retired variants.**

* **The three operational variants were one design scoped three ways** — same sections, same verification mechanism, differing only in their Linked Records domain and, unexpectedly, in their automatic-validation check lists. That check-list difference was the one real divergence and is resolved in [validation-rules.md](../validation-rules.md#document-upload-rules) rather than here.

* **Two component naming divergences are resolved.** [components.md](../components.md) had flagged "Document Viewer" vs "Embedded Document Viewer" and "Version History Component" vs "Version History Table" as probably-the-same-thing, inferred rather than confirmed. With one screen, one name is required for each; the identical feature lists confirm the inference, and both are resolved to the operational variants' names.

* **What was dropped, and why.** Only the master viewer's view-only action sets, its static rendering of verification state, and the per-domain scoping of Linked Records. Nothing representing distinct work was discarded — its Document Summary Cards, Administrative Information and Review History all survive.
