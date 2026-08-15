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

# Screen: Sales & Disclosure Details

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described two designs — a sales monitoring view (Developer Principal / Director) and a disclosure preparation workspace (Sales & Disclosure Officer) — with different information groupings and a Validation Summary present in only one. Both are **retired**; this is one screen absorbing the load-bearing content of each.

## Purpose

The detail view of a single property sale and its regulatory disclosure, opened from [Sales & Disclosures](sales-and-disclosures.md). Covers the sale record, the buyer record, the property, the disclosure's progress with RERA, supporting documents and regulatory correspondence — with the controls to edit, validate, submit and correct the disclosure. Any user may do any of it.

## Layout

```
Top Bar
↓
Sale Header
↓
Sales Summary Cards
↓
Disclosure Progress
↓
Sale Information
↓
Buyer Information
↓
Property Information
↓
Supporting Documents
↓
Validation Summary
↓
RERA Queries & Review History
↓
Communication History / Activity Timeline
```

## Sections

### Section 1 — Sale Header

**Left**

* Sale Reference
* Property / Unit and Project
* Buyer Name
* Sale Status badge · Disclosure Status badge

**Right**

* **Edit Sale** · **Create / Continue Disclosure** · **Submit to RERA** · **Download Record**

**Reconciled 2026-08-15:** the monitoring variant's header carried view actions only; the workspace variant's carried the edit/submit set. The full set now applies to every user, subject to sale and disclosure status.

**Both status badges appear here.** A sale and its disclosure have separate lifecycles — see [status-badges.md](../status-badges.md#sales--disclosure-status).

### Section 2 — Sales Summary Cards

Absorbed from the monitoring variant, the only one to define them: sale value, disclosure position, document completeness and days since sale.

### Section 3 — Disclosure Progress

Stage tracker for the disclosure's regulatory journey. Present in **both** variants; the workspace variant's stage list is more granular and is the one kept.

### Section 4 — Sale Information

**Sale Details** — sale reference, sale date, agreed value, payment plan, sale type.

**Transaction Details** *(workspace variant only)* — payment schedule, amounts received, outstanding balance, instrument details.

**Reconciled 2026-08-15:** the monitoring variant had a single *Sales Information* group; the workspace variant split it into *Sale Details* and *Transaction Details*. The two-group structure is kept — Transaction Details is real content the monitoring variant omitted.

### Section 5 — Buyer Information

**Primary Buyer** — name, identification, contact details, nationality.

**Buyer Classification** *(workspace variant only)* — individual / corporate / joint, and the documentation each implies.

**Additional Purchasers** *(workspace variant only, "when applicable")* — for joint purchases.

**Reconciled 2026-08-15:** the monitoring variant defined only *Buyer Details*, a flat field list covering the primary buyer. The workspace variant's three-group structure is the superset and is kept. Joint-purchase handling exists only there and would have been lost by picking the monitoring variant.

### Section 6 — Property Information

Property details — unit, type, size, project, registration reference.

**Reconciled 2026-08-15:** the workspace variant marked this group *(Read-only)*. That marking is **kept**, because it is a data-integrity rule rather than a permission: property attributes are owned by the property registration record and are edited there, not on the sale. It applies to every user, and always did.

### Section 7 — Supporting Documents

Required-document checklist and table, with Upload / Replace / Preview / Resubmit actions governed by document status.

**Reconciled 2026-08-15:** the monitoring variant's *Submitted Documents* section listed what had been filed with view/download actions; the workspace variant's *Supporting Documents* added the required-document checklist and upload controls. The workspace version is the superset and is kept.

### Section 8 — Validation Summary

Automatic pre-submission checks, displayed as Passed / Warning / Error, with the submit action disabled until all mandatory checks pass.

**Reconciled 2026-08-15 — this section now applies to every user.** It existed only in the workspace variant; the monitoring variant had none, because that variant could not submit. That was an access restriction, not a property of the screen. See [validation-rules.md](../validation-rules.md).

### Section 9 — RERA Queries & Review History

**Absorbed 2026-08-15** by combining two sections the variants held separately:

* **RERA Queries** *(workspace variant)* — open queries with Respond and Upload actions.
* **RERA Review History** *(monitoring variant)* — the closed record of review rounds, decisions, reviewers and dates.

These are the same correspondence at two points in its life, and were split only because one variant could act on it and the other could only read it. Presented as one section: open queries first, resolved history below.

### Section 10 — Communication History / Activity Timeline

Chronological record of everything that has happened to this sale and disclosure. Each entry shows who acted and what role they held at the time ([navigation.md](../../navigation.md#audit-trail-principle)).

**Reconciled 2026-08-15:** the monitoring variant called this *Activity Timeline*; the workspace variant called it *Communication History* and scoped it to correspondence. Kept as the full activity timeline, which contains the correspondence entries as a subset.

## Empty State

> No disclosure has been prepared for this sale yet. Create the disclosure to begin.

**Primary Button** — Create Sales Disclosure

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

1. No section, field, action or card on this screen is role-gated. What a user can do depends on the sale's and disclosure's status, never on who they are.
2. Property Information is read-only for everyone — it is owned by the property registration record.
3. Fields become read-only after submission unless RERA returns the disclosure.
4. Validation Summary checks are defined in [validation-rules.md](../validation-rules.md).
5. The sale's status and the disclosure's status are separate values and must not be conflated.

## User Flow

```
Sales & Disclosures
↓
Sales & Disclosure Details
├─ Edit / Create Disclosure / Submit → disclosure flow
├─ Document row → Document Details
├─ RERA Query → response flow
└─ Property link → Property Registration Details
```

## Notes

* **This absorbs, rather than references, both retired variants.** Their headers, progress trackers, information groupings, document tables, correspondence and timelines are now one screen.

* **The Validation Summary asymmetry** was resolved the same way as on [project-details.md](project-details.md): it is a property of submitting, and every user can now submit.

* **A read-only marking was kept, deliberately.** Property Information stays read-only for everyone. Distinguishing this from the role-based read-only claims that were removed is the point: this one is about which record owns the data, not about who is looking.

* **What was dropped, and why.** Only the view-only header actions and the monitoring framing. Nothing representing distinct work was discarded — the monitoring variant's Sales Summary Cards and RERA Review History are carried forward, and the workspace variant's Transaction Details, Buyer Classification, Additional Purchasers, required-document checklist and Validation Summary are all kept.
