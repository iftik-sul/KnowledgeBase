---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: extrapolated
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/shared-platform-features.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/individual-user/service-flows/feature-01-submit-application.md"
tags:
  - real-estate-developer
  - shared-feature
  - application-management
---

# Feature #1 – Submit Application

**Feature Category:** Shared Platform Features – Application Management

> **Proposed** — not sourced as a standalone feature; see [shared-platform-features.md](../shared-platform-features.md) for why this document exists and what it deliberately does not assert (a single payment-timing order). Needs client confirmation.

## 1. Feature Overview

The **Submit Application** feature provides a standardized mechanism for developer-account users to submit requests for any Group B service through the Real Estate Developers Portal. It is the final submission stage of every service workflow: validating the application, confirming payment where the service requires one, generating a unique application reference number, and routing the application to the appropriate RERA authority — Compliance & Escrow Auditor, Registrar, or Account Trustee, depending on the service.

## 2. Purpose

Provide a common application submission process shared across all Group B business services, ensuring consistency, traceability, and regulatory compliance across the development lifecycle.

## 3. Description

After completing the required service-specific information, uploading supporting documents, and — where the selected service requires it — paying the applicable service fee, the user submits the application from the Real Estate Developers Portal. The platform validates the application, assigns a unique reference number, records the submission, and routes it to the responsible authority. Any of the four Group B roles may submit on behalf of the developer account; role is recorded as audit-trail attribution only, per [navigation.md](../navigation.md).

This feature is reused by every business service that requires an official application to RERA.

## 4. Used By

The feature is shared by all applicable Group B business services, including:

* Register Initial Sale
* Register Initial Rent-to-Own
* Register Initial Usufruct
* Register Sale Associated with an Initial Mortgage
* Registration of Real Estate Project
* Escrow Account Activation
* Escrow Account Transfer
* Real Estate Licensing Application
* Real Estate Project Sub-division
* Requesting a Technical Report for the Project

## 5. Prerequisites

* User is logged into a registered developer company account.
* User has selected a Group B service.
* All mandatory information has been completed.
* Required documents have been uploaded.
* Payment has been successfully completed, where the selected service requires it.

## 6. Required Information

The feature receives information from the selected business service.

Typical information includes:

* Service Type
* Project / Unit Reference (where applicable)
* Purchaser or Counterparty Information (where applicable)
* Service-specific Data
* Uploaded Documents
* Payment Confirmation (where applicable)
* Additional Remarks (Optional)

## 7. Required Documents

Documents depend on the selected service.

Examples include:

* Provisional Sale / Lease / Usufruct Agreement
* Purchaser Identification
* Survey Reports
* Real Estate License
* Project Financial or Solvency Summary
* Other service-specific documents

## 8. Service Fee

No separate fee.

The feature uses the fee defined by the selected business service — which may be zero. Not every Group B service carries a RERA fee (Escrow Account Activation, Service #8, sources none).

## 9. Payment Required

**Yes, where the selected service requires it — timing varies by service.**

Unlike individual-user, Group B does not source a single "pay before submission" order. Confirmed variants found in this module: payment before RERA's decision (Service #1); payment after an intermediate audit/accept step (Service #13); no payment at all (Service #8). This feature enforces whatever timing the selected service's own Section 8/9 specifies — it does not impose an order of its own.

## 10. Processing Authority

**RERA**

The submitted application is automatically routed to the authority responsible for the selected service — typically the Compliance & Escrow Auditor, with the Registrar and Account Trustee as additional routing targets for specific services (project registration, escrow).

## 11. Expected Processing Time

Application submission is immediate.

Subsequent processing depends on the selected business service.

## 12. Processing Workflow

User Completes Service Form
↓
Upload Required Documents
↓
Review Application
↓
Complete Payment (if the service requires it, and if required before this step)
↓
Submit Application
↓
System Validates Application
↓
Generate Application Reference Number
↓
Record Audit Log
↓
Route Application to Responsible Authority
↓
Application Successfully Submitted

## 13. Application Status Flow

Draft
↓
Payment Pending *(where applicable, and where payment precedes submission)*
↓
Payment Successful *(where applicable)*
↓
Submitted

Possible exception statuses

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
* Payment Receipt (where applicable)

## 16. Related Features

* Track Application Status
* Respond to Information Request
* Resubmit Returned Application
* Documents
* Notifications

## 17. UI Screens

* Application Review
* Payment (where applicable)
* Payment Successful (where applicable)
* Application Submitted
* Application Details

## 18. API Requirements

* Validate Application
* Validate Required Documents
* Validate Payment (where applicable)
* Generate Application Reference Number
* Submit Application
* Assign Processing Authority
* Send Notifications
* Create Audit Log
* Retrieve Application Details

## 19. Database Entities

* Developer Company
* User
* Application
* Application Status
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the four Group B roles can submit a completed application on behalf of the developer account.
* All mandatory information is validated before submission.
* Required documents are successfully uploaded.
* Payment is verified before submission, only where the selected service requires it.
* The system generates a unique application reference number.
* The application is routed to the correct responsible authority for the selected service.
* The user receives a submission confirmation.
* A digital acknowledgement receipt is generated.
* The application becomes available under **Applications** for status tracking.
* Notifications are sent to the user.
* All submission activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated users of a registered developer company account may submit applications.
2. All mandatory information must be completed before submission.
3. All required supporting documents must be uploaded before submission.
4. Where the selected service requires payment, it must be completed at the point specified by that service's own workflow — not assumed to be before submission in every case.
5. Every submitted application receives a unique application reference number.
6. Applications cannot be modified after submission unless additional information is requested or the application is returned.
7. Every application is automatically routed to the correct responsible authority based on the selected service.
8. Submission generates an acknowledgement receipt and user notification.
9. Every submission event must be permanently recorded in the audit trail, including the acting user's role at the time.
10. The submitted application becomes available immediately under **Applications** for status tracking.

## Open Questions

1. Should this feature (and the three that follow it) be formally adopted for Group B, the way financial-trust-institutions has already proposed the same four features in `services-overview.md`? Needs client confirmation.
2. Should individual service-flow files be updated to cross-reference this feature document, or should it remain a pure reference layer (the current state in individual-user, which does not link back from its own service files either)?
