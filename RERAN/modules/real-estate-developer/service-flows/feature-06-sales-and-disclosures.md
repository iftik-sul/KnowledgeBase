---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: extrapolated
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/sales-and-disclosures.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - shared-feature
  - compliance
---

# Feature #6 – Sales & Disclosures

**Feature Category:** Shared Platform Features – Compliance

> **Resolved 2026-08-16 — not a domain workspace.** The prior version of [shared-platform-features.md](../shared-platform-features.md) flagged this screen's relationship to the numbered service catalogue as genuinely unresolved. Checked directly this session: Service #1 (Register Initial Sale) and Service #6 (Register Sale Associated with an Initial Mortgage) both cite **Property Registrations**, not this screen, in their own `derived_from`. This screen's own frontmatter, in turn, cites only the master source files directly — not any specific numbered service. Read together, this screen is not where a sale is *registered* with RERA (that's Property Registrations, Feature #3); it's a **sales-performance and disclosure-compliance tracking layer** running parallel to it — recording sales and filing a separate disclosure obligation against each, similar in kind to financial-trust-institutions' Compliance Reports feature, which likewise doesn't map to a numbered service.

## 1. Feature Overview

**Sales & Disclosures** lists the organization's recorded property sales alongside their regulatory disclosure status, and provides both a monitoring view of sales performance/disclosure compliance and the operational controls to record sales, prepare disclosures, upload buyer documents, and submit to RERA.

## 2. Purpose

Track two related but separate lifecycles per sale — the sale's own record and its disclosure obligation to RERA — and surface sales-performance and disclosure-compliance analytics not captured anywhere else in the module.

## 3. Description

Merged 2026-08-15 from two prior role-based variants (an executive monitoring screen and an operational workspace) into one, absorbing the Sales Analytics that only the monitoring view carried. Two page actions exist: **Record Property Sale** and **Create Sales Disclosure** — genuinely separate operations, not two names for one action. A sale can be recorded and sit **Awaiting Disclosure** before its disclosure is even started; the sale's own status and the disclosure's status are tracked as two separate columns and two separate badge vocabularies, never conflated, the same pattern used on Escrow Management for account status vs. fund release status.

## 4. Used By

**Not sourced against any specific numbered service.** Functions alongside Property Registrations (Feature #3) rather than feeding into it — a sale registered there may separately need a disclosure recorded and filed here. Whether every Feature #3 sale requires a Feature #6 disclosure, or only some, is not established by any source document.

## 5. Prerequisites

* User is logged into a registered developer company account.

## 6. Required Information

Not itemized in source beyond the table's own columns: Property, Project, Buyer, Sale Date, Sale Value. Search/filter: Property/Buyer, project, property type, sales status, disclosure status, date range.

## 7. Required Documents

Buyer documents, uploaded via the "Upload Buyer Documents" action once a sale is recorded and Disclosure Pending. Not itemized further in source.

## 8. Service Fee

Not addressed in source.

## 9. Payment Required

**Not addressed in source.** Unlike every numbered service in this module, no payment step is described anywhere in this screen's spec.

## 10. Processing Authority

**RERA**, for the disclosure filing itself. Any of the developer's four Group B roles may record a sale or prepare/submit a disclosure — not role-gated, per the screen's own explicit statement that "no card, column, filter, row action or section on this screen is role-gated."

## 11. Expected Processing Time

Not sourced.

## 12. Processing Workflow

Dashboard
↓
Open Sales & Disclosures
↓
Record Property Sale *(creates a sale record, independent of disclosure)*
↓
Sale Status: Draft → *(finalized)*
↓
Create Sales Disclosure *(separate action, against a recorded sale)*
↓
Upload Buyer Documents → Validate → Submit to RERA
↓
RERA Reviews Disclosure
↓
*(if queried)* Respond to Query → Upload Additional Documents → Resubmit
↓
Disclosure Approved

## 13. Application Status Flow

**Sale Status** (own lifecycle): Draft → *(finalized/active)*

**Disclosure Status** (separate lifecycle): Disclosure Pending → Draft Disclosure → Submitted → Under Review → Information Requested / Returned → Approved

These two vocabularies are never conflated in filters, badges, or counts — the same discipline applied to Escrow Management's Escrow Status vs. Fund Release Status.

## 14. Possible Outcomes

* Sale Recorded
* Disclosure Submitted / Approved
* Disclosure Returned / Information Requested

## 15. Output

* Disclosure Record, downloadable once approved

## 16. Related Features

* Property Registrations *(Feature #3 — where the underlying sale is actually registered with RERA; this feature tracks the sale and its disclosure obligation alongside, not instead of, that registration)*
* Reports *(Sales Analytics links out to the full report set)*

## 17. UI Screens

* Sales & Disclosures
* Sales & Disclosure Details

## 18. API Requirements

* Retrieve Organization Sales & Disclosures / Search / Filter
* Record Property Sale
* Create / Submit Sales Disclosure
* Upload Buyer Documents
* Retrieve Sales Analytics
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Developer Company, User
* Property Sale, Sale Status
* Sales Disclosure, Disclosure Status
* Document
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can record a sale and independently prepare/submit its disclosure.
* Sale Status and Disclosure Status are tracked and displayed as separate values, never conflated.
* Summary card figures match the table's own filtered counts exactly.
* All sale-recording and disclosure activity is recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Recording a sale and creating its disclosure are two separate actions with two separate lifecycles.
2. Any of the developer's four Group B roles may perform either action — no role restriction.
3. Row actions depend on the sale's or disclosure's own status, never on who is viewing.
4. Sale Status and Disclosure Status must not be conflated in filters, badges, or counts.
5. All sale and disclosure activity is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. **Central and unresolved**: is a disclosure required for every sale recorded via Property Registrations, or only some? No source document establishes this relationship. Needs client confirmation before this feature's true dependency on Feature #3 can be documented precisely.
2. No payment step is described anywhere in this feature's spec, unlike every numbered service in the module — confirm whether this is intentional (a non-fee-bearing compliance obligation) or a gap.
3. Same adoption question as Feature #1 — needs client confirmation.
