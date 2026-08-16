---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/services-catalog.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/service-details.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/submit-application.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - application-management
---

# Feature #1 – Service Requests

**Feature Category:** Shared Platform Features – Application Lifecycle

> **Restructured 2026-08-16.** Previously drafted as "Submit Application," copied from individual-user's four-feature Application Management framing. Rebuilt against this module's actual built screens rather than that framing: `ui/screens-unified/` groups **Services Catalog**, **Service Details**, and **Submit Application** as one flow — the module's own README calls Submit Application "the module's one canonical eighteen-service form." Browsing the catalog and completing the form were previously going to be split into two separate top-level features ("Services Catalog" as a general feature, "Submit Application" as an application-management feature); the sourced screen grouping says they're one. `contains_proposals: true` remains — the module-wide adoption question (`services-overview.md` To Confirm item 2) is still open.

## 1. Feature Overview

The **Service Requests** feature is the beginning of the application lifecycle for any of the 18 Group C services: browsing the catalog, viewing a service's requirements, and completing and submitting the canonical application form. It covers validation, payment where the service's own model requires it before lodging, application-reference generation, and routing — either to internal certification (Services #3–#11) or directly to RERA's Transaction Audit queue (Services #1, #2, #12–#18).

## 2. Purpose

Provide institution users with a single entry point — browse, understand, complete, submit — for starting any Group C service request, ensuring consistency and traceability across the eighteen services.

## 3. Description

The user opens **Service Requests**, browses or searches the 18-service catalog, and opens a service's details to see its requirements before starting. The canonical submission form (`submit-application.md`) adapts its fields to the selected service — documented per-service as Pattern A (flat fields), Pattern B (repeatable groups), or Pattern C (field-selection/conditional pairs) in the module's UI package. The user completes the required information, uploads documents, and — where the selected service's payment model places payment before lodging — pays via the shared platform gateway, then submits. Any of the institution's four Group C roles may do this; role is recorded as audit-trail attribution only, per [navigation.md](../navigation.md).

Once submitted, the application moves to the **Applications** feature for all subsequent tracking and action — Service Requests does not re-appear after submission.

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

* User is logged into a verified institution account, with current (non-expired) institutional approval — an expired approval blocks submission specifically, not access to the rest of the platform (`navigation.md` Access Rule 3, B8).
* User has selected a service from the catalog.
* All mandatory information has been completed.
* Required documents have been uploaded.
* Payment has been completed via the shared platform gateway, where the selected service's payment model requires it before lodging.

## 6. Required Information

* Service Type (selected from catalog)
* Institution Information
* Borrower / Counterparty Information (where applicable)
* Property or Title Information (where applicable)
* Service-specific data, following the service's own field pattern (A/B/C)
* Uploaded Documents
* Payment Confirmation (where applicable)

## 7. Required Documents

Documents depend on the selected service. Examples include:

* Mortgage Agreement / Deed of Mortgage
* Loan Offer Letter / Property Valuation Report
* Title Deed / Certificate of Title
* Institution Identification and Registration Documents
* Other service-specific documents

## 8. Service Fee

No separate fee for the feature itself.

Uses the fee defined by the selected service, which may be zero (Service #2 carries no fee at all, confirmed by `open-questions.md` B11).

## 9. Payment Required

**Yes, where the selected service's payment model requires it — timing and payer vary by service, per [payments.md](../payments.md).**

Two models: **Upfront Gateway Payment** (institution pays, before lodging — Services #1, #3–#11) and **Customer Payment at Counter** (customer pays, at the point of service, before RERA's decision — Services #12–#18). This feature enforces whichever timing the selected service specifies.

**Corrected 2026-08-16** — this section previously described Services #12 and #18 as a confirmed exception paying *after* RERA's decision. The client has since normalized both to pay before RERA's decision, the same as #13–#17; the two payment models are now clean, without exception.

## 10. Processing Authority

**RERA — Compliance & Escrow Auditor**, reached either directly or via the institution's own Internal Certifier gate, depending on the service.

## 11. Expected Processing Time

Browsing and form completion are immediate. Submission processing depends on the selected service.

## 12. Processing Workflow

Open Services Catalog
↓
Browse or Search Services
↓
Open Service Details
↓
Review Requirements
↓
Start Service Request
↓
Complete Service-Specific Form (Pattern A / B / C)
↓
Upload Required Documents
↓
Review Application
↓
Complete Payment via Shared Platform Gateway (if the service's model requires it before lodging)
↓
Submit Application
↓
System Validates Application
↓
Generate Application Reference Number
↓
Record Audit Log
↓
**If Services #3–#11:** Route to Internal Certification Queue
**If Services #1, #2, #12–#18:** Route Directly to RERA Transaction Audit Queue
↓
Application Now Tracked Under **Applications**

## 13. Application Status Flow

Draft
↓
Payment Pending *(where applicable, and where payment precedes lodging)*
↓
Payment Successful *(where applicable)*
↓
Pending Internal Certification *(Services #3–#11 only)*
↓
Submitted

Once `Submitted`, the application belongs to the **Applications** feature's status flow, not this one.

Possible exception statuses (within this feature only)

* Validation Failed
* Payment Failed
* Submission Failed
* Cancelled

## 14. Possible Outcomes

* Application Successfully Submitted
* Validation Failed
* Missing Information
* Missing Documents
* Payment Failed
* Submission Failed

## 15. Output

Upon successful submission, the system generates:

* Application Reference Number
* Submission Confirmation
* Submission Timestamp
* Digital Acknowledgement Receipt
* Payment Receipt (where payment preceded lodging)

## 16. Related Features

* Applications *(where the application lives from `Submitted` onward)*
* Internal Certification Queue *(Services #3–#11 only)*
* Documents
* Notifications

## 17. UI Screens

* Services Catalog
* Service Details
* Submit Application
* Payment Confirmation (where applicable)

## 18. API Requirements

* Retrieve Services Catalog
* Retrieve Service Details
* Validate Application
* Validate Required Documents
* Validate Payment (where applicable)
* Generate Application Reference Number
* Submit Application
* Submit for Internal Certification (Services #3–#11 only)
* Assign Processing Authority
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Institution
* Institution Staff
* User
* Service
* Application
* Application Status
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can browse the catalog and submit a completed application.
* Service Details accurately reflects the selected service's requirements before the user commits to starting.
* All mandatory information is validated before submission.
* Required documents are successfully uploaded.
* Payment is verified before lodging only where the selected service requires it there.
* The system generates a unique application reference number.
* Services #3–#11 route to Internal Certification before RERA; all other services route directly to RERA.
* The application becomes available under **Applications** immediately after submission.
* All submission activities are recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Only authenticated users of a verified institution account, with current institutional approval, may submit applications.
2. All mandatory information must be completed before submission.
3. All required supporting documents must be uploaded before submission.
4. Where the selected service's payment model requires payment before lodging, it must be completed via the shared platform gateway before the application can be lodged.
5. Services #3–#11 must pass internal certification before routing to RERA. Services #1, #2, and #12–#18 do not carry this gate.
6. Every submitted application receives a unique application reference number.
7. Once submitted, the application is managed exclusively through the **Applications** feature — Service Requests does not track post-submission state.
8. Submission generates an acknowledgement receipt and user notification.
9. Every submission event must be permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. `services-overview.md` To Confirm item 2 ("Do the four Application Management features apply to Group C as they do to individual users?") is answered in a restructured form by this document's existence — the underlying "should this layer exist, and is it correctly described" question remains open, not the original four-feature framing.
2. Should individual service-flow files (Services #1–#18) be updated to cross-reference this feature document?
