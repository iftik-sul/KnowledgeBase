---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/service-flows/service-12-real-estate-licensing-application.md"
  - "RERAN/modules/real-estate-service-companies/service-flows/service-14-issue-professional-practice-card.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - company-profile
---

# Screen: Company Profile

**Access:** Any of the company's four Group D roles — identical screen for every user.

## Purpose

The company's own standing (licence status, corporate information) and staff roster — not gated by role, matching Financial & Trust Institutions' and Real Estate Developer's equivalent screens.

## Layout

```
Top Bar
↓
Company Standing
↓
Agent Roster & Practice Cards
↓
Staff Records
↓
Corporate Information
```

## Sections

### Section 1 — Company Standing

Licence status badge, licence reference, renewal action (routes into Service #12). **Proposed**, pending client confirmation of the actual renewal mechanics — unlike Financial & Trust Institutions' Service #1, Group D's Service #12 is not sourced with an explicit "renewal" framing the way that service is ("approval **/ renewal**"); row 59's own text describes only a first-time application shape. Whether this service also handles renewal, or a separate renewal service exists that source didn't capture, is flagged here rather than assumed.

### Section 2 — Agent Roster & Practice Cards

Every agent holding a practice card under the company, with card status (Active · Expiring · Cancelled), and actions routing into Services #15–#17 (Renew, Cancel, Amend) per agent.

### Section 3 — Staff Records

A roster — name, email, role, status, date added — for audit-trail attribution only. No permission scopes to assign, matching the unified-access model from the start.

### Section 4 — Corporate Information

Company legal name, registration reference, contact details, editable by any user.

## Empty State

Not applicable — every registered company has a profile.

## Reused Components

Company Operations Sidebar, Top Bar, Status Badge, Data Table, Buttons.

## Validation

1. Any of the company's four Group D roles can view and edit every section.
2. Removing a staff member does not retroactively invalidate that user's past actions in the audit trail.

## Access

Identical for all four roles.

## User Flow

```
Dashboard
↓
Company Profile
├─ Renew Licence → Submit Application (Service #12)
├─ Agent Row → Renew / Cancel / Amend Card (Services #15–#17)
└─ Add / Remove Staff → Staff Records updated
```

## Notes

* **Whether Service #12 genuinely covers renewal, or only first-time licensing, is an open item this screen's own Section 1 flags** — not resolved elsewhere in this module's documentation. Worth checking directly against source before this screen's renewal action is built against an assumption.
