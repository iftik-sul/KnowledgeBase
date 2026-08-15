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
  - "RERAN/modules/financial-trust-institutions/payments.md"
  - "RERAN/modules/individual-user/service-flows/feature-01-submit-application.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - application-management
---

# Feature #1 – Submit Application

**Feature Category:** Shared Platform Features – Application Management

> **Proposed** — named and rationalized in [services-overview.md](../services-overview.md#shared-platform-features) ("the source defines a standard six-stage pipeline... Group C services run the same pipeline and therefore require the same capabilities") but not previously written as a standalone document. This file fills that gap. `services-overview.md`'s own To Confirm item 2 ("Do the four Application Management features apply to Group C as they do to individual users?") remains open — needs client confirmation.

## 1. Feature Overview

The **Submit Application** feature provides a standardized mechanism for institution-account users to submit requests for any of the 18 Group C services. It is the final submission stage of every service workflow: validating the application, confirming payment where the service's own payment model requires it before lodging, generating a unique application reference number, and routing the application either to internal certification (Services #3–#11) or directly to RERA's Transaction Audit queue (Services #1, #2, #12–#18).

## 2. Purpose

Provide a common application submission process shared across all 18 Group C business services, ensuring consistency, traceability, and regulatory compliance.

## 3. Description

After completing the required service-specific information, uploading supporting documents, and — where the applicable payment model requires it before lodging — paying the fee via the shared platform gateway, the user submits the application. The platform validates the application, assigns a unique reference number, records the submission, and routes it according to that service's own lifecycle: to internal certification first for the mortgage and finance-lease lifecycle (Services #3–#11), or directly to RERA for the remainder. Any of the institution's four Group C roles may submit; role is recorded as audit-trail attribution only, per [navigation.md](../navigation.md).

This feature is reused by every Group C service that requires an official application to RERA.

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
* Contract Cancellation

## 5. Prerequisites

* User is logged into a verified institution account, with current (non-expired) institutional approval — an expired approval blocks submission specifically, not access to the rest of the platform (`navigation.md` Access Rule 3, B8).
* User has selected a Group C service.
* All mandatory information has been completed.
* Required documents have been uploaded.
* Payment has been completed via the shared platform gateway, where the selected service's payment model requires it before lodging.

## 6. Required Information

The feature receives information from the selected business service.

Typical information includes:

* Service Type
* Institution Information
* Borrower / Counterparty Information (where applicable)
* Property or Title Information (where applicable)
* Service-specific Data
* Uploaded Documents
* Payment Confirmation (where applicable)
* Additional Remarks (Optional)

## 7. Required Documents

Documents depend on the selected service.

Examples include:

* Mortgage Agreement / Deed of Mortgage
* Loan Offer Letter / Property Valuation Report
* Title Deed / Certificate of Title
* Institution Identification and Registration Documents
* Other service-specific documents

## 8. Service Fee

No separate fee.

The feature uses the fee defined by the selected business service — which may be zero. Service #2 (Cancellation of Account Trustee & Auditing Company) carries no fee at all, confirmed by `open-questions.md` B11.

## 9. Payment Required

**Yes, where the selected service's payment model requires it — timing and payer vary by service, per [payments.md](../payments.md).**

Group C runs two payer/timing models, not one: **Upfront Gateway Payment**, paid by the institution before the application is lodged (Services #1, #3–#11), and **Customer Payment at Counter**, paid by the customer at the point of service (Services #13–#17, sourced). Within the second model, Services #12 and #18 are a documented exception: payment happens *after* RERA's decision, not before submission. This feature enforces whichever timing the selected service specifies — it does not impose a single order.

## 10. Processing Authority

**RERA — Compliance & Escrow Auditor**, reached either directly or via the institution's own Internal Certifier gate, depending on the service. See Section 12.

## 11. Expected Processing Time

Application submission is immediate.

Subsequent processing depends on the selected business service, and on whether it carries the internal certification gate.

## 12. Processing Workflow

User Completes Service Form
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
**If Services #3–#11:** Route to Internal Certification Queue (any of the institution's four Group C users may certify or return, including the filer)
**If Services #1, #2, #12–#18:** Route Directly to RERA Transaction Audit Queue
↓
Application Successfully Submitted

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

Possible exception statuses

* Validation Failed
* Payment Failed
* Returned by Certifier *(Services #3–#11 only — loops back to Draft, not the same as a RERA return)*
* Submission Failed
* Cancelled

## 14. Possible Outcomes

* Application Successfully Submitted
* Validation Failed
* Missing Information
* Missing Documents
* Payment Failed
* Returned by Internal Certifier *(Services #3–#11 only)*
* Submission Failed

## 15. Output

Upon successful submission, the system generates:

* Application Reference Number
* Submission Confirmation
* Submission Timestamp
* Digital Acknowledgement Receipt
* Payment Receipt (where payment preceded lodging)

## 16. Related Features

* Track Application Status
* Respond to Information Request
* Resubmit Returned Application
* Internal Certification Queue *(Feature #5, Services #3–#11 only — the institution-internal gate, distinct from this feature and from RERA-side review)*
* Documents
* Notifications

## 17. UI Screens

* Application Review
* Payment Confirmation (where applicable)
* Internal Certification Queue (Services #3–#11 only)
* Application Submitted
* Application Details

## 18. API Requirements

* Validate Application
* Validate Required Documents
* Validate Payment (where applicable)
* Generate Application Reference Number
* Submit Application
* Submit for Internal Certification (Services #3–#11 only)
* Assign Processing Authority
* Send Notifications
* Create Audit Log
* Retrieve Application Details

## 19. Database Entities

* Institution
* Institution Staff
* User
* Application
* Application Status
* Certification Record *(Services #3–#11 only)*
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can submit a completed application on behalf of the institution.
* All mandatory information is validated before submission.
* Required documents are successfully uploaded.
* Payment is verified before lodging only where the selected service's payment model requires it there.
* The system generates a unique application reference number.
* Services #3–#11 route to Internal Certification before RERA; all other services route directly to RERA.
* The user receives a submission confirmation.
* A digital acknowledgement receipt is generated.
* The application becomes available under **Applications** for status tracking.
* Notifications are sent to the user.
* All submission activities are recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Only authenticated users of a verified institution account, with current institutional approval, may submit applications.
2. All mandatory information must be completed before submission.
3. All required supporting documents must be uploaded before submission.
4. Where the selected service's payment model requires payment before lodging, it must be completed via the shared platform gateway before the application can be lodged.
5. Services #3–#11 must pass internal certification — an unrestricted action any of the institution's four Group C users may perform, including the filer — before routing to RERA. Services #1, #2, and #12–#18 do not carry this gate.
6. Every submitted application receives a unique application reference number.
7. Applications cannot be modified after submission unless additional information is requested or the application is returned.
8. Submission generates an acknowledgement receipt and user notification.
9. Every submission event must be permanently recorded in the audit trail, including the acting user's role.
10. The submitted application becomes available immediately under **Applications** for status tracking.

## Open Questions

1. `services-overview.md` To Confirm item 2 ("Do the four Application Management features apply to Group C as they do to individual users?") is answered by this document's existence, but remains a proposed answer ("yes, unchanged") pending client confirmation — not a closed item.
2. Should individual service-flow files (Services #1–#18) be updated to cross-reference this feature document, or should it remain a pure reference layer, as individual-user's does?
