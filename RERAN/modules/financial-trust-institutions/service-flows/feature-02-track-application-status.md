---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: extrapolated
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
  - "RERAN/modules/individual-user/service-flows/feature-02-track-application-status.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - application-management
---

# Feature #2 – Track Application Status

**Feature Category:** Shared Platform Features – Application Management

> **Proposed** — named in [services-overview.md](../services-overview.md#shared-platform-features), not previously written as a standalone document. Needs client confirmation.

## 1. Feature Overview

The **Track Application Status** feature enables institution-account users to monitor the progress of every application submitted for any of the 18 Group C services, via the **Applications** sidebar item. It provides visibility into the application's current status, processing history, assigned authority, outstanding actions, and final decision — including, for Services #3–#11, whether the application is currently inside the institution's own internal certification gate or has already been routed to RERA.

## 2. Purpose

Provide a centralized location to track the progress and current status of all submitted applications throughout their lifecycle, for any of the institution's four Group C roles.

## 3. Description

The feature allows users to view all submitted applications, search for specific applications, monitor status changes, review processing history, view comments or requests from RERA, and download approved documents once processing is complete. Because Group C is not gated by role ([navigation.md](../navigation.md)), any of the four roles can view and act on any application filed under the institution account, including ones they did not personally submit.

This feature displays whichever status vocabulary the underlying service uses — the platform-wide core statuses, plus the Group C extension (`Pending Internal Certification`, `Returned by Certifier`) for Services #3–#11 only. It does not include the certify-or-return action itself, which belongs to the separate **Internal Certification Queue** (Feature #5).

This feature is shared by every business service that submits an application to RERA.

## 4. Used By

The feature is shared by all 18 Group C business services, including:

* Mortgage Registration
* Mortgage Amendment
* Mortgage Transfer
* Mortgage Release
* Grant Property Mortgage
* Finance Lease Registration
* Registration of Real Estate Fund Companies
* Updating Title Deed Information
* Split Ownership
* Issuance of Title Deed

## 5. Prerequisites

* User is logged into a verified institution account.
* At least one application has been submitted under the institution account.

## 6. Required Information

The user may search using one or more of the following:

* Application Reference Number
* Service Type
* Institution Reference Number
* Property Registration Number / Title Reference (where applicable)
* Application Date
* Current Status

## 7. Required Documents

No document upload is required.

Approved documents and certificates become available for download when applicable.

## 8. Service Fee

No additional fee.

Application tracking is included as part of the submitted service.

## 9. Payment Required

**No**

Payment is not required to track an application that has already been submitted.

## 10. Processing Authority

**RERA**

Application status information is retrieved directly from the official application management system.

## 11. Expected Processing Time

Immediate (real-time retrieval).

## 12. Processing Workflow

Login
↓
Open Applications
↓
Search or Select Application
↓
Retrieve Application Details
↓
View Current Status
↓
View Timeline
↓
View Processing History
↓
Download Documents (when available)

## 13. Application Status Flow

Draft
↓
Pending Internal Certification *(Services #3–#11 only)*
↓
Submitted
↓
Under Review
↓
Information Requested (if applicable)
↓
Approved / Rejected
↓
Completed

Possible additional statuses

* Payment Pending / Payment Successful (where the service's model places payment before lodging)
* Returned by Certifier *(Services #3–#11 only)*
* Returned for Correction
* Approved — Awaiting Payment *(Services #12 and #18 only — the two services where payment sources after RERA's decision)*
* Withdrawn

**This module's status vocabulary genuinely differs by service**, unlike a fully uniform platform-wide set: only Services #3–#11 carry the internal-certification statuses, and only Services #12/#18 carry `Approved — Awaiting Payment`. This feature displays whatever the underlying service defines; see `services-overview.md`'s Application Status Vocabulary section and each service's own Section 13 for the authoritative per-service list.

## 14. Possible Outcomes

* Application Found
* Application Not Found
* Application Pending Internal Certification *(Services #3–#11 only)*
* Application Under Review
* Information Requested
* Application Approved
* Application Rejected
* Application Completed

## 15. Output

The system displays:

* Application Reference Number
* Service Name
* Submission Date
* Current Status
* Processing Timeline
* Assigned Authority (Internal Certifier and/or Compliance & Escrow Auditor, as applicable)
* Status History
* Comments from RERA (where applicable)
* Available Certificates or Documents
* Payment Information

## 16. Related Features

* Submit Application
* Respond to Information Request
* Resubmit Returned Application
* Internal Certification Queue *(Feature #5 — where the certify/return action itself is performed, for Services #3–#11)*
* Documents
* Notifications

## 17. UI Screens

* Applications
* Application Details
* Status History
* Download Documents

## 18. API Requirements

* Retrieve Institution Applications
* Search Applications
* Retrieve Application Details
* Retrieve Application Timeline
* Retrieve Status History
* Retrieve Comments
* Retrieve Available Documents
* Download Documents

## 19. Database Entities

* Institution
* Institution Staff
* User
* Application
* Application Status
* Certification Record *(Services #3–#11 only)*
* Application Timeline
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can view all applications submitted under the institution account.
* Users can search applications using supported search criteria.
* Current application status is displayed correctly, including internal-certification statuses where the service carries that gate.
* Complete status history is available.
* Processing timeline is displayed in chronological order.
* Users can view requests for additional information.
* Approved documents are available for download when applicable.
* All application access activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated users of the institution account may access its application status information.
2. Any of the four Group C roles may view or act on any application under the institution — there is no per-role restriction (per [navigation.md](../navigation.md)).
3. Application status is updated automatically as processing progresses.
4. Status history cannot be modified by users.
5. Approved certificates and documents become available for download only after the application reaches the appropriate status.
6. If RERA requests additional information, the application status changes to **Information Requested**, and the user must use the **Respond to Information Request** feature.
7. If an application is returned by RERA for correction, the user must use the **Resubmit Returned Application** feature. A **Returned by Certifier** status (Services #3–#11 only) is a separate, institution-internal loop handled by the Internal Certification Queue, not this feature.
8. Every status change is recorded with a timestamp in the application timeline, including the acting user's role.
9. All application viewing activities must be permanently recorded in the audit trail.
10. The feature displays whatever status vocabulary the underlying service defines, including whether it carries the internal-certification extension or the Services #12/#18 payment-after-approval status.

## Open Questions

1. Same adoption question as Feature #1 — needs client confirmation.
