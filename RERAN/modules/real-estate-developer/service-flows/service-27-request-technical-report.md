---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - service-flow
  - title-deed-data-services
---

# Service #27 – Requesting a Technical Report for the Project

**Service Category:** Title Deed Data Services

## 1. Service Overview

The **Requesting a Technical Report for the Project** service allows a developer to request an official RERA technical report on a project, involving a field visit and delivered by registered mail and the developers portal.

> **UI mismatch — flagged, not resolved.** `ui/screens/reports.md` is a self-service analytics and export feature (Generate Reports, Export Reports, Schedule Reports) the developer runs against its own data. This service is a regulatory request *to RERA* that triggers a field visit and produces an official report delivered by registered mail — a fundamentally different kind of "report." No screen in the 19-screen set represents this service; `reports.md` is not treated as a match.

## 2. Purpose

Obtain an official, RERA-conducted technical assessment of a project — for example for due diligence, dispute support, or regulatory compliance purposes — distinct from the developer's own self-service reporting.

## 3. Description

The developer submits the request electronically. RERA receives and reviews the application, schedules a site visit, conducts the field visit and data collection, prepares and approves the technical report, and delivers it via registered mail and the developers portal.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Project Registration Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing registered project (Service #13) the report will cover.
* Reason for requesting the technical report.

## 6. Required Information

* Project Reference Number
* Purpose of the Technical Report
* Preferred Site Visit Window (if applicable)

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Written Justification for the Request
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule. Where charged, paid through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Not specified in the source** — this service's workflow contains no payment step, so neither the fee's existence nor its timing is sourced. **Proposed**: a fee applies, paid per transaction through the shared platform payment gateway at the point of submission, consistent with the other document-issuance services whose payment step *is* sourced; needs client confirmation. Flagged rather than assumed, since neighbouring services in this category differ on timing.

## 10. Processing Authority

**Compliance & Escrow Auditor** (review); a RERA field team conducts the site visit.

## 11. Expected Processing Time

**5 business days**

## 12. Processing Workflow

Submit Application Electronically
↓
Receipt and Review of Application
↓
Set Appointment to Visit Site
↓
Field Visit and Data Collection
↓
Preparation and Approval of the Report
↓
Receipt of Report via Registered Mail and Developers Portal

## 13. Application Status Flow

Submitted
↓
Under Review
↓
Site Visit Scheduled
↓
Field Visit Completed
↓
Report in Preparation
↓
Approved
↓
Delivered

### Additional Statuses

* Information Requested
* Rejected

## 14. Possible Outcomes

* Technical Report Successfully Delivered
* Additional Information Requested
* Application Rejected

## 15. Output

* Electronic Technical Report (e-technical report), delivered via registered mail and the developers portal

## 16. Related Services

* Service #13 – Registration of Real Estate Project
* Service #24 – Registration/Amendment of Real Estate Project Details

## 17. UI Screens

Not currently represented in the 19-screen UI set. `reports.md` is not a match — see the mismatch note in Section 1. **Proposed** minimum surface: a "Request Technical Report" flow with site-visit scheduling, distinct from the self-service Reports screen.

## 18. API Requirements

* Submit Technical Report Request
* Schedule Site Visit
* Record Field Visit Data
* Retrieve Application Status
* Generate Electronic Technical Report
* Send Notifications
* Deliver Report (registered mail integration and portal)

## 19. Database Entities

* Developer Company
* Project
* Technical Report Request
* Site Visit
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can submit a technical report request against a registered project.
* System schedules a site visit as part of the workflow.
* Approved requests generate a technical report delivered by registered mail and the portal.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a registered project may be the subject of a technical report request.
2. A field visit is a required step in every request under this service; there is no desk-only path in the source.
3. All submissions, site visits, approvals, and deliveries must be permanently recorded in the audit trail.
4. **No UI screen exists for this service, and `reports.md` is not a substitute** — flagged for the client rather than force-fit to the self-service Reports screen.
