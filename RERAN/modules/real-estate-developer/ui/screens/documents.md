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

# Screen: Documents

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described four designs: an organization-wide repository (Developer Principal / Director) and three operational workspaces (Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison), each with its own document category set, filters and empty state. All four are **retired**; this is one screen absorbing the load-bearing content of each — most importantly the **union of all four category taxonomies**, which is the thing a merge could most easily have lost.
>
> The Sales & Disclosure Officer variant had itself only just been recovered: it was left out of the original migration because including it would have contradicted the Role Permission Matrix, and was merged back in earlier under this issue. It is folded into this rebuild along with the other three.

## Purpose

List every document the organization has uploaded, across projects, property registrations, sales disclosures, escrow accounts and regulatory applications — with the controls to upload, replace, preview, resubmit and track verification. Any user may do any of it, for any document category.

## Layout

```
Top Bar
↓
Document Summary Cards
↓
Filters & Search
↓
Documents Table
↓
Pending Verification
↓
Document Analytics
↓
Recent Document Activity
↓
Pagination
```

**Top Bar**

* Title: Documents
* Subtitle: Upload, organize and manage every document the organization files with RERA.
* Search Bar: Search anything...
* Page Actions: **Upload Documents**

## Sections

### Section 1 — Document Summary Cards

| KPI | Description | Absorbed from |
| :---- | :---- | :---- |
| Total Documents | All documents, organization-wide | All four |
| Draft Documents | Uploaded but not submitted | The three operational variants |
| Pending Verification | Awaiting verification | All four |
| Verified Documents | Successfully verified | All four |
| Returned Documents | Require replacement or correction | The three operational variants |
| Rejected Documents | Verification failed | All four |
| Missing Required Documents | Mandatory documents not yet uploaded | The three operational variants |
| Expiring Soon | Documents nearing expiry | Principal · operational variants *(reconciled — see Notes)* |
| Expired Documents | Already expired | Principal |
| Recently Uploaded | Uploaded in the last 30 days | Principal |
| Document Categories | Count of categories in use | Principal |

Selecting a card filters the table.

### Section 2 — Filters

* Search Document
* **Category Filter**
* Project Filter
* Property Filter
* Application Filter / Application Type Filter
* Buyer Filter
* Disclosure Filter
* Escrow Account Filter
* Fund Release Filter
* Financial Institution Filter
* Verification Status Filter
* Expiry Status Filter
* Uploaded By Filter
* Upload Date Range
* Reset Filters

**Absorbed 2026-08-15:** the union of all four variants' filters. The domain filters that each operational variant carried alone — *Buyer* and *Disclosure* (sales), *Escrow Account*, *Fund Release* and *Financial Institution* (escrow), *Property* (registration) — are all retained, since each narrows a real relationship. The repository variant's *Uploaded By* and *Expiry Status* filters are likewise kept.

**Uploaded By** filters on who performed the upload, as recorded in the audit trail. It is attribution, not a permission scope — anyone may filter by anyone.

### Section 3 — Document Categories

**Absorbed 2026-08-15 — the union of all four taxonomies**, grouped by what the document attaches to. Each variant defined its own 10–11 category list, with substantial overlap at the general end and none at the domain end. Dropping any one list would have lost an entire domain's vocabulary.

**Organization**

* Company Documents
* Regulatory Certificates
* Licenses & Permits
* Legal Agreements
* Financial Documents
* Compliance Documents

**Project & Registration**

* Project Documents
* Property Registration Documents
* Technical Documents
* Survey Documents
* Building Approval Documents
* Environmental Documents

**Sales & Disclosure**

* Sales Agreements
* Buyer Identification
* Proof of Payment
* Mortgage Documents
* Corporate Buyer Documents
* Power of Attorney
* Disclosure Forms

**Escrow**

* Escrow Agreement
* Bank Confirmation Letter
* Engineer Progress Certificate
* Quantity Surveyor Report
* Construction Progress Report
* Site Inspection Report
* Fund Release Documents

**Other**

* Supporting Documents
* Other

### Section 4 — Documents Table

| Column | Description |
| :---- | :---- |
| Document Name | Uploaded document |
| Category | Document category |
| Linked Record | Project · Property · Application · Sale / Disclosure / Buyer · Escrow Account / Fund Release |
| Financial Institution | Associated bank *(escrow documents only)* |
| Uploaded By | Employee, and the role they held at the time |
| Upload Date | Date uploaded |
| Verification Status | Current status |
| Expiry Date | If applicable |
| Action | Available actions |

**Absorbed 2026-08-15:** the union of all four variants' columns. **Linked Record** is the reconciliation point — each variant defined it over its own domain ("Project / Property / Application", "Sale / Disclosure / Buyer", "Escrow Account / Fund Release / Application"). One column now covers all of them, showing the record type alongside the reference.

### Row Actions

Available actions depend on **document status**, not on who is looking.

| Status | Actions |
| :---- | :---- |
| Draft | Edit Details · Replace · Preview · Delete |
| Pending Verification | Preview · View Details |
| Information Requested / Returned | Replace Document · Upload Revised Version · Preview · Resubmit |
| Verified | View · Download |
| Rejected | View Remarks · Replace Document |

**Reconciled 2026-08-15:** the repository variant offered *View Details* only, with the note "no editing or uploading is permitted from this screen" — an access restriction, now retired. The three operational variants defined the identical status-to-action mapping above, so no reconciliation was needed between them.

### Section 5 — Pending Verification

Documents requiring immediate attention, with columns **Document · Issue · Due Date · Priority · Action** and actions **Upload · Replace · Continue**. Items nearing their deadline sort first.

Example issues, absorbed across all three operational variants: missing mandatory documents, returned verification, expiring approvals, incorrect file format, low-quality scan, missing signature, missing buyer identification, sales agreement requires correction, proof of payment missing, missing Engineer Certificate, Quantity Surveyor report requires correction, bank confirmation pending, construction progress report returned, expiring escrow agreement, missing photographic evidence.

### Section 6 — Document Analytics

**Absorbed 2026-08-15** from the repository variant, the only one to carry analytics. Retained in full.

**Repository Overview**

* Total Storage Used
* Total Documents
* Average File Size
* Most Used Category

**Compliance Overview**

* Verification Rate
* Documents Expiring This Month
* Missing Required Documents
* Compliance Score

> The repository variant showed Document Analytics *instead of* Pending Verification, and the operational variants the reverse. **Both are kept**, as Sections 5 and 6 — they answer different questions, and the either/or was a consequence of one variant being unable to act.

### Section 7 — Recent Document Activity

Timeline of document events across the organization — uploaded, replaced, verification started, information requested, revised version uploaded, verified, rejected. Each entry shows who acted and what role they held at the time ([navigation.md](../../navigation.md#audit-trail-principle)). Selecting an entry opens the document.

### Verification Status

See [status-badges.md](../status-badges.md#document-status). The source uses three different, unreconciled vocabularies for document status; that conflict is recorded there and is **not** resolved by this rebuild — it predates the role variants and is not caused by them.

## Empty State

**Message**

> No documents uploaded yet. Upload the documents required to support your projects, registrations, sales disclosures and escrow activity.

**Primary Button** — Upload Documents
**Secondary Button** — View Projects

**Reconciled 2026-08-15:** the four variants each had an empty state addressed to their own domain ("No sales disclosure documents have been uploaded yet…", "No escrow documents…", and so on). One organization-wide message replaces them.

## Pagination

Rows per page · Previous · Next · Page Number · Total Records

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

1. No card, column, filter, category, row action or section on this screen is role-gated. What a user can do depends on the document's status, never on who they are.
2. Domain filters and the Financial Institution column apply to the document categories where they carry a value; they are never role-conditional.
3. Summary card figures must match the table's own filtered counts exactly.
4. Status vocabulary comes from [status-badges.md](../status-badges.md#document-status).

## User Flow

```
Dashboard
↓
Documents
├─ Upload Documents → upload flow
├─ Summary Card / Category Filter → filtered table
├─ Row → Document Details
└─ Pending Verification row → replace or resubmit flow
```

## Notes

* **This absorbs, rather than references, all four retired variants.**

* **The category taxonomies were the substantive merge.** Each variant defined its own list of 10–11 categories. They shared the general end (Company Documents, Compliance Documents, Supporting Documents, Other) and had **no overlap at all** at the domain end — sales agreements and buyer identification existed only in the sales variant; engineer progress certificates and quantity surveyor reports only in the escrow variant; survey, technical and environmental documents only in the registration variant. Picking one list would have deleted two entire domains' vocabulary. Unioned and grouped by what the document attaches to.

* **Reconciliation — "Expiring Soon" vs "Expiring Documents."** The repository variant used the former, the operational variants the latter; both defined as documents nearing expiry. Kept as **Expiring Soon**, which pairs with the repository variant's *Expired Documents* card that is also retained.

* **Reconciliation — Pending Verification vs Document Analytics was a false either/or.** The repository variant's layout substituted Analytics where the operational variants had a Pending Verification queue. That was a consequence of one variant having no actions to offer, not a judgement that the two are alternatives. Both are present.

* **A pre-existing conflict is deliberately left open.** [status-badges.md](../status-badges.md#document-status) records three unreconciled document-status vocabularies in the source. That conflict is not between role variants — it predates them and survives the merge unchanged. Resolving it needs source clarification, not a merge decision, so it stays flagged.

* **What was dropped, and why.** Only the view-only row-action list and its "no editing or uploading is permitted from this screen" note, the per-domain scoping of KPIs and empty-state text, and duplicate copies of the identical Recent Document Activity section. Nothing representing distinct work was discarded.
