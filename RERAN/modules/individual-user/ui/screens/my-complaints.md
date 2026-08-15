---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/service-flows/service-38-submit-complaint.md"
  - "RERAN/modules/individual-user/service-flows/service-39-track-complaint.md"
  - "RERAN/modules/individual-user/open-questions.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - complaints
---

# Screen: My Complaints

**Access:** Any authenticated Individual User — own complaints only.

## Purpose

Combines #38 (Submit Complaint) and #39 (Track Complaint) into one screen — a list of submitted complaints plus the entry point for filing a new one, matching how the two services are already grouped as Consumer Protection Services in `services-overview.md`.

## Layout

```
File New Complaint (button)
↓
Search / Filter
↓
Complaint List
↓
Complaint Detail (on selection)
```

## Sections

### Section 1 — File New Complaint

Opens [Submit Application](../screens-unified/submit-application.md) at Pattern K — category selection, free-text details, evidence upload, payment (confirmed required, `open-questions.md` A7).

### Section 2 — Complaint List

Reference number, category, date submitted, Complaint/Dispute Status badge (`status-badges.md` — distinct vocabulary from Application Status).

### Section 3 — Complaint Detail

Timeline, investigation updates, communications from RERAN, and the final resolution/decision letter once Closed. **No payment gate anywhere on this screen or its detail view** — tracking a complaint is confirmed free (`open-questions.md` A6), the module's clearest internal-consistency finding, and this is the screen where getting that wrong would be most visible to a user who already paid once to file.

## Empty State

**Message:**

> No complaints filed. If you have a concern about a developer, landlord, or practitioner, you can file one here.

## Reused Components

Status Badge, Document Upload (evidence), Payment Step (filing only, never tracking).

## Validation

Filing (#38) requires payment; tracking (#39) never does. This is the one payment rule in the whole module that isn't about *timing* (before vs. after decision) but about *which action* — submit vs. read — carries a fee at all. Must not be implemented as "complaints are chargeable," since that statement is only half true.

## Access

No role variation — any account may file a complaint about any RERAN-regulated matter; not restricted to property owners or tenants specifically.

## User Flow

```
Sidebar → My Complaints → File New Complaint → Submit Application (Pattern K) →
  My Complaints (list) → [select] → Complaint Detail
```

## Notes

* #26 (Submit Tenancy Dispute) is a different service with its own status vocabulary overlap risk — a tenancy dispute is reached from [my-leases.md](my-leases.md), not from here, even though both use category-conditional field patterns. Keeping them on separate screens avoids conflating a regulatory grievance (#38, this screen) with a formal adjudication/litigation process (#26).
