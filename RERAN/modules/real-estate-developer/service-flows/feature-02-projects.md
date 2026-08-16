---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/projects.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - shared-feature
  - domain-workspace
---

# Feature #2 – Projects

**Feature Category:** Shared Platform Features – Domain Workspace

## 1. Feature Overview

**Projects** is the domain workspace for the project-registration lifecycle: registering a new development project, tracking it through RERA review, and monitoring the organization's portfolio. It is one of five domain workspaces this module uses instead of a single generic submission form — see [shared-platform-features.md](../shared-platform-features.md).

## 2. Purpose

List the organization's development projects and provide both the monitoring view of the portfolio and the operational controls to create, edit, submit, and correct project registrations — any user may do either.

## 3. Description

The screen was previously two designs (an executive portfolio view and an operational workspace); both are retired and merged into one, since access is not gated by role. Row actions depend on project status, not who is looking — a submitted project cannot be edited by anyone, approved or not. Portfolio Insights (distribution by stage/type, progress summary, quarterly performance) is carried forward from the monitoring variant as real content, not a role's framing of shared content, and links out to Reports.

## 4. Used By

Services #13–#19, confirmed via service-13's `derived_from`:

* Registration of Real Estate Project
* Real Estate Project Cancellation
* Real Estate Project Sub-division
* Changing the Name of a Real Estate Project
* Project Re-registration
* Settlements Application
* Request Termination of Initial Registration

## 5. Prerequisites

* User is logged into a registered developer company account.

## 6. Required Information

Varies by which of Services #13–#19 is selected — see each service's own Section 6. Search/filter on this screen: Project name, status, development type, location, registration stage, date range.

## 7. Required Documents

Varies by service — see each service's own Section 7.

## 8. Service Fee

Set by the selected service — not uniform across #13–#19. See Feature #1's note on this module's genuine payment-timing variance.

## 9. Payment Required

**Depends on the selected service.** Confirmed variance within this cluster alone: Service #13 (Registration of Real Estate Project) pays *after* an intermediate audit/accept step, not before submission — unlike the simpler pay-before pattern elsewhere in the module. This feature does not assume a single timing; consult the selected service's own Section 9.

## 10. Processing Authority

**RERA — Compliance & Escrow Auditor**, or the Registrar for specific services. Any of the developer's four Group B roles may act on this screen — role is audit-trail attribution only.

## 11. Expected Processing Time

Set by the selected service — see its own Section 11.

## 12. Processing Workflow

Dashboard
↓
Open Projects
↓
Register New Project *(or select an existing project)*
↓
Complete Project-Specific Form (per selected service)
↓
Upload Required Documents
↓
Submit
↓
RERA Reviews *(routing and steps vary by service — see Service #13's own longer chain: License → Apply → Audit → Upload Units → Registrar Account → Pay → Certificate)*
↓
Application Tracked Under **Applications** *(Feature #1)*

## 13. Application Status Flow

Draft → Submitted → Under Review → Information Requested / Returned → Approved → Active / Suspended / Completed

**Reconciled 2026-08-15** into a nine-state union after the screen's two prior variants genuinely conflicted (not a clean subset): Draft, Submitted, Under Review, Information Requested, Returned, Approved, Rejected, Suspended, Completed. "Pending Review" was dropped as a duplicate label for Under Review; "Suspended" was kept as a real, otherwise-unrepresentable state.

## 14. Possible Outcomes

* Project Approved and Active
* Information Requested
* Returned for Correction
* Rejected
* Suspended
* Completed

## 15. Output

Set by the selected service — typically a registration certificate or equivalent regulatory output. See the service's own Section 15.

## 16. Related Features

* Applications *(Feature #1 — where post-submission tracking, response, and resubmission actually happen)*
* Reports *(Portfolio Insights links out to the full report set)*

## 17. UI Screens

* Projects
* Project Details

## 18. API Requirements

* Retrieve Organization Projects / Search / Filter
* Retrieve Project Details
* Submit Project Registration (per selected service)
* Retrieve Portfolio Insights
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Developer Company, User
* Project, Project Status
* Document, Application *(cross-referenced with Feature #1)*
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can view, create, and act on any project.
* Row actions are governed by project status, never by who is viewing.
* Portfolio Insights figures match the table's own filtered counts exactly.
* All project activity is recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Any of the developer's four Group B roles may register, edit, or act on any project — no per-user assignment scoping.
2. Row actions depend on project status: Draft is editable, Submitted/Under Review is view-only, Approved allows registering properties.
3. Status vocabulary is the nine-state union described above — not a subset specific to any one prior role-based variant.
4. Portfolio Insights figures must match the table's own filtered counts exactly; no independent aggregation logic.
5. All project activity is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. Same adoption question as Feature #1 (Applications) — needs client confirmation.
