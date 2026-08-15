---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/applications.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/application-details.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/application-review.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - application-management
---

# Feature #2 – Applications

**Feature Category:** Shared Platform Features – Application Lifecycle

> **Restructured 2026-08-16.** Previously drafted as three separate documents — Track Application Status, Respond to Information Request, Resubmit Returned Application — copied from individual-user's four-feature framing. Rebuilt against this module's actual built screens: `applications.md`, `application-details.md`, and `application-review.md` are the **only** screens covering everything a submitted application does — there is no dedicated screen for "tracking" as distinct from "the application record," and no dedicated screen for "responding" or "resubmitting" as distinct from acting on that same record. All three of the original documents described actions on the same object; they are sections of this one feature now, not three features. `contains_proposals: true` remains — the module-wide adoption question is still open.

**Scope note, carried forward from the previous drafts and still important:** this feature covers only the **RERA-side** loop (`Information Requested` / `Returned for Correction`). The institution-internal certify-or-return loop (`Returned by Certifier`, Services #3–#11 only, looping back to Draft) belongs to the separate **Internal Certification Queue** feature, not this one.

## 1. Feature Overview

The **Applications** feature is the single workspace for everything that happens to a Group C application from the moment it's submitted: viewing its status and history, responding to RERA's information requests, resubmitting after a RERA return, and downloading issued outputs on completion. It is where any of the institution's four Group C roles goes to find, track, and act on any application filed under the institution — including ones they didn't personally submit.

## 2. Purpose

Provide a centralized workspace covering the full post-submission lifecycle of an application — tracking, information-request response, and resubmission — rather than splitting that lifecycle across separate features that would, in practice, describe the same screen three times.

## 3. Description

The feature allows users to search and filter applications, open an application's full detail record, view its current status and processing history, see RERA's comments or information requests, respond to those requests, resubmit after a return, and download issued outputs once complete. Because Group C is not gated by role ([navigation.md](../navigation.md)), any of the four roles can view and act on any application filed under the institution account.

This feature displays whichever status vocabulary the underlying service uses — the platform-wide core statuses, plus the Group C extension (`Pending Internal Certification`, `Returned by Certifier`) for Services #3–#11 only, shown here for visibility but acted on through the separate Internal Certification Queue.

### 3a. Tracking

Users view an application's current status, timeline, processing history, assigned authority, and available documents, in real time.

### 3b. Responding to an Information Request

When RERA's Compliance & Escrow Auditor raises a query (status `Information Requested`), the user reviews the request, updates information, uploads additional documents, and submits a response. This does not create a new application, and does not re-enter the institution's internal certification gate — it returns directly to RERA's queue.

### 3c. Resubmitting a Returned Application

When RERA returns an application for correction (status `Returned for Correction`), the user reviews the return comments, corrects the application, uploads revised documents, and resubmits. The original application reference number is retained; this is a correction of the existing application, not a new one.

## 4. Used By

All 18 Group C business services, including:

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
* At least one application has been submitted under the institution account (for tracking).
* For responding: RERA has issued an Information Request and the application status is **Information Requested**.
* For resubmitting: RERA has returned the application and the application status is **Returned for Correction**.

## 6. Required Information

**For search/tracking**, the user may search using:

* Application Reference Number
* Service Type
* Institution Reference Number
* Property Registration Number / Title Reference (where applicable)
* Application Date
* Current Status

**For responding or resubmitting**, depending on the request or return reason:

* Response / Correction Comments
* Updated Application Information
* Additional Remarks (Optional)

## 7. Required Documents

No upload required for tracking.

For responding or resubmitting, depending on the request:

* Missing or Corrected Supporting Documents
* Updated Mortgage / Lease / Title Documents
* Other documents requested by RERA

Approved certificates and documents become available for download once the application reaches the appropriate status.

## 8. Service Fee

No additional fee for any of tracking, responding, or resubmitting — all form part of the original submitted application.

## 9. Payment Required

**No**, for tracking, responding, or resubmitting. (Where the original application's payment model places payment after RERA's decision — Services #12, #18 — that timing is unaffected by activity in this feature.)

## 10. Processing Authority

**RERA — Compliance & Escrow Auditor**. Responses and resubmissions route back to RERA's review queue directly — never to the institution's internal certification gate.

## 11. Expected Processing Time

Tracking retrieval is immediate. Response and resubmission processing follow the original service's normal review timeline.

## 12. Processing Workflow

**Tracking**

Login → Open Applications → Search or Select Application → View Status, Timeline, History → View RERA Comments → Download Documents (when available)

**Responding**

User Receives Information Request → Open Application → Review Request → Update Information / Upload Documents → Submit Response → Returns to RERA Review

**Resubmitting**

User Receives Return Notification → Open Application → Review Return Comments → Correct Application / Upload Revised Documents → Resubmit → Returns to RERA Review

## 13. Application Status Flow

Submitted
↓
Under Review
↓
Information Requested → Response Submitted → Under Review *(loop, via 3b)*
↓
Returned for Correction → Resubmitted → Under Review *(loop, via 3c)*
↓
Approved / Rejected
↓
Approved — Awaiting Payment *(Services #12 and #18 only)*
↓
Completed

Possible additional statuses

* Pending Internal Certification / Returned by Certifier *(Services #3–#11 only — displayed here, acted on via Internal Certification Queue)*
* Withdrawn

**Status vocabulary genuinely differs by service** — only Services #3–#11 carry the internal-certification statuses, and only Services #12/#18 carry `Approved — Awaiting Payment`. See `services-overview.md`'s Application Status Vocabulary section and each service's own Section 13.

## 14. Possible Outcomes

* Application Found / Not Found
* Application Under Review
* Response Successfully Submitted / Returned to Review
* Application Successfully Resubmitted / Returned Again
* Application Approved / Rejected / Completed

## 15. Output

The system displays or generates, depending on the action:

* Application Reference Number, Service Name, Status, Timeline, Assigned Authority, Status History, RERA Comments, Payment Information
* Response Confirmation and Timestamp (3b)
* Resubmission Confirmation and Timestamp (3c)
* Available Certificates or Documents for download (on Completion)

## 16. Related Features

* Service Requests *(where the application originates)*
* Internal Certification Queue *(Services #3–#11 only — the certify/return action itself happens there, not here)*
* Documents
* Notifications

## 17. UI Screens

* Applications
* Application Details
* Application Review

## 18. API Requirements

* Retrieve Institution Applications / Search Applications / Retrieve Application Details
* Retrieve Application Timeline / Status History / Comments
* Retrieve Information Request / Submit Response
* Retrieve Return Comments / Update Application / Resubmit Application
* Update Application Status / Send Notifications / Retrieve Available Documents / Download Documents

## 19. Database Entities

* Institution, Institution Staff, User
* Application, Application Status, Application Timeline
* Information Request, Response
* Return Reason, Application Revision
* Document, Notification, Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can view, search, and act on any application under the institution.
* Current status and complete history are displayed correctly, using the vocabulary the underlying service defines.
* Users can respond to information requests and resubmit returned applications without creating a new application record.
* Both actions route back to RERA directly, never to internal certification.
* Original application reference numbers are retained through both actions.
* Approved documents are available for download once the application reaches the appropriate status.
* All access, response, and resubmission activities are recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Only authenticated users of the institution account may view or act on its applications; any of the four Group C roles may do so, including ones they did not personally submit.
2. Responses can only be submitted when status is **Information Requested**; resubmissions only when status is **Returned for Correction**.
3. Neither action creates a new application or re-enters internal certification.
4. Status changes automatically: `Information Requested` → `Under Review` on response; `Returned for Correction` → `Under Review` on resubmission.
5. RERA may issue a request or return again if the response/correction is insufficient.
6. Approved certificates and documents become available for download only once the application reaches the appropriate status.
7. Every action receives a timestamp and is permanently linked to the original application in its timeline.
8. A `Returned by Certifier` status (Services #3–#11 only) is a separate, institution-internal loop handled by the Internal Certification Queue, not this feature.
9. All viewing, response, resubmission, and status-change activities must be permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. `services-overview.md` To Confirm item 2 is answered in restructured form by this document's existence — the underlying adoption question remains open.
2. Should individual service-flow files (Services #1–#18) be updated to cross-reference this feature document?
