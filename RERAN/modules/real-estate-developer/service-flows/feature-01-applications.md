---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/applications.md"
  - "RERAN/modules/real-estate-developer/ui/screens/application-details.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - shared-feature
  - application-management
---

# Feature #1 – Applications

**Feature Category:** Shared Platform Features – Application Lifecycle

> **Restructured 2026-08-16.** Previously drafted as three separate documents — Track Application Status, Respond to Information Request, Resubmit Returned Application — copied from individual-user's four-feature framing, mirroring the same restructure applied to financial-trust-institutions the same day. Rebuilt against this module's actual built screens: `applications.md` and `application-details.md` are the **only** screens covering anything post-submission — there is no dedicated screen for "tracking" as distinct from "the application record," and none for "responding" or "resubmitting" as distinct from acting on that same record. All three of the original documents described actions on the same object; they are sections of this one feature now, not three. `contains_proposals: true` remains — this whole shared-features layer is unsourced and needs client confirmation.

## 1. Feature Overview

The **Applications** feature is the single cross-cutting workspace for everything that happens to a Group B application after it leaves whichever domain workspace originated it — Projects, Property Registrations, Sales & Disclosures, Escrow Management, or Fund Release Request. It covers viewing status and history, responding to RERA's information requests, resubmitting after a return, and downloading issued outputs. It is where any of the four Group B roles goes to find and act on any application filed under the developer account, including ones they didn't personally submit.

## 2. Purpose

Provide one workspace for the full post-submission lifecycle — tracking, information-request response, resubmission — rather than splitting it across separate features that would describe the same two screens repeatedly.

## 3. Description

The feature lets users search and filter applications across all five domain workspaces, open an application's full detail record, view current status and processing history, see RERA's comments, respond to information requests, resubmit after a return, and download outputs once complete. Group B is not gated by role ([navigation.md](../navigation.md)), so any of the four roles can view and act on any application, whichever domain it originated from.

### 3a. Tracking

Users view an application's current status, timeline, processing history, and available documents, in real time, regardless of which domain workspace (Projects, Property Registrations, Sales & Disclosures, Escrow Management, Fund Release Request) it came from.

### 3b. Responding to an Information Request

When RERA raises a query (status `Information Requested`), the user reviews the request, updates information, uploads additional documents, and submits a response. This does not create a new application.

### 3c. Resubmitting a Returned Application

When RERA returns an application for correction (status `Returned`), the user reviews the return comments, corrects the application, uploads revised documents, and resubmits. The original application reference number is retained.

## 4. Used By

Applications originating from any of the module's domain workspaces, across all 27 Group B services, including:

* Register Initial Sale (via Property Registrations)
* Registration of Real Estate Project (via Projects)
* Escrow Account Activation (via Escrow Management)
* Project Profit Withdrawal (via Fund Release Request)
* Record Property Sale / Create Sales Disclosure (via Sales & Disclosures)

## 5. Prerequisites

* User is logged into a registered developer company account.
* At least one application has been submitted, from any domain workspace (for tracking).
* For responding: RERA has issued an Information Request and the application status is **Information Requested**.
* For resubmitting: RERA has returned the application and the application status is **Returned**.

## 6. Required Information

**For search/tracking:**

* Application Reference Number
* Originating Domain (Project / Property Registration / Sales & Disclosure / Escrow / Fund Release)
* Service Type
* Application Date
* Current Status

**For responding or resubmitting**, depending on the request or return reason:

* Response / Correction Comments
* Updated Application Information

## 7. Required Documents

No upload required for tracking.

For responding or resubmitting: missing or corrected supporting documents, as requested by RERA.

Approved certificates and documents become available for download once the application reaches the appropriate status.

## 8. Service Fee

No additional fee for tracking, responding, or resubmitting — all form part of the original submitted application. (The original application's own fee, and whether it applies at all, is set by its originating service — see the relevant domain workspace or numbered service.)

## 9. Payment Required

**No**, for tracking, responding, or resubmitting.

This module's payment timing is genuinely not uniform across services (confirmed variance: pay-before for Service #1, pay-after-decision for Service #13, no fee at all for Service #8) — but that variance belongs to the originating domain workspace, not to this feature, since none of tracking, responding, or resubmitting requires payment regardless of the underlying service's own model.

## 10. Processing Authority

**RERA — Compliance & Escrow Auditor**, or the Registrar / Account Trustee for specific services, per the originating domain. Responses and resubmissions route back to whichever authority is currently reviewing the application.

## 11. Expected Processing Time

Tracking retrieval is immediate. Response and resubmission processing follow the originating service's own review timeline.

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
Returned → Resubmitted → Under Review *(loop, via 3c)*
↓
Approved / Rejected / Registered / Completed

**Not every service uses this exact vocabulary** — e.g. Service #13 (Register Real Estate Project) sources a longer, service-specific status chain. This feature displays whatever status vocabulary the underlying service defines; it does not impose its own.

## 14. Possible Outcomes

* Application Found / Not Found
* Application Under Review
* Response Successfully Submitted / Returned to Review
* Application Successfully Resubmitted / Returned Again
* Application Approved / Rejected / Registered / Completed

## 15. Output

The system displays or generates, depending on the action:

* Application Reference Number, Service Name, Status, Timeline, Status History, RERA Comments
* Response Confirmation and Timestamp (3b)
* Resubmission Confirmation and Timestamp (3c)
* Available Certificates or Documents for download (on Completion)

## 16. Related Features

* Projects, Property Registrations, Sales & Disclosures, Escrow Management, Fund Release Request *(the domain workspaces applications originate from — see [shared-platform-features.md](../shared-platform-features.md))*
* Documents
* Notifications

## 17. UI Screens

* Applications
* Application Details

## 18. API Requirements

* Retrieve Developer Applications / Search Applications / Retrieve Application Details
* Retrieve Application Timeline / Status History / Comments
* Retrieve Information Request / Submit Response
* Retrieve Return Comments / Update Application / Resubmit Application
* Update Application Status / Send Notifications / Retrieve Available Documents / Download Documents

## 19. Database Entities

* Developer Company, User
* Application, Application Status, Application Timeline
* Information Request, Response
* Return Reason, Application Revision
* Document, Notification, Audit Log

## 20. Acceptance Criteria

* Any of the four Group B roles can view, search, and act on any application under the developer account, regardless of which domain workspace it originated from.
* Current status and complete history are displayed correctly, using the vocabulary the underlying service defines.
* Users can respond to information requests and resubmit returned applications without creating a new application record.
* Original application reference numbers are retained through both actions.
* Approved documents are available for download once the application reaches the appropriate status.
* All access, response, and resubmission activities are recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Only authenticated users of the developer company account may view or act on its applications; any of the four Group B roles may do so, including ones they did not personally submit.
2. Responses can only be submitted when status is **Information Requested**; resubmissions only when status is **Returned**.
3. Neither action creates a new application.
4. Status changes automatically on response or resubmission, per the originating service's own status flow.
5. RERA may issue a request or return again if the response/correction is insufficient.
6. Approved certificates and documents become available for download only once the application reaches the appropriate status.
7. Every action receives a timestamp and is permanently linked to the original application in its timeline.
8. All viewing, response, resubmission, and status-change activities must be permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. Should this feature (and the domain workspaces named in [shared-platform-features.md](../shared-platform-features.md)) be formally adopted for Group B? Needs client confirmation.
2. Should individual service-flow files be updated to cross-reference this feature document?
