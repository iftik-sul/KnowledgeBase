---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registrations.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-03-mortgage-registration.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
---

# Service #6 – Register Sale Associated with an Initial Mortgage

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Register Sale Associated with an Initial Mortgage** service allows a developer to register the provisional sale of a unit where the purchaser is financing the purchase through a mortgage. The application captures the mortgage institution, reference number, and amount, and — **by client decision, 2026-08-16** — validates that reference against financial-trust-institutions' Mortgage Registration records before the application can proceed to RERA's audit. **A second decision, same day: the matched FTI record must be `Completed`** — its mortgage registration must have already passed both of FTI's own gates (internal certification, then RERA's audit) before this sale can validate.

> **Corrected 2026-08-16, three times.** First pass found that the previously-asserted "coordinating... linking" relationship to financial-trust-institutions' Service #3 was an unconfirmed inference, not a sourced fact. Second pass decided the service should validate the mortgage after all. **Third: the FTI record must be `Completed` to count as valid** — resolving what the second pass had left open. This has a real consequence worth stating plainly, not just as a status-value footnote: **despite this service's name — "Initial Mortgage" — the two applications cannot be filed concurrently.** The institution's mortgage registration must fully complete, through both of its own gates, before the developer can successfully register this sale. A developer submitting this application while the matching FTI mortgage is still `Pending Internal Certification` or `Under Review` will have their sale automatically returned, not held pending — see Section 13. This is a documented product decision extending beyond what source specifies, not itself sourced.

## 2. Purpose

Provide a regulated, provisional record of a mortgage-financed unit sale, validated against a mortgage the financing institution has already fully registered, under a single project unit.

## 3. Description

The developer selects the property, records the purchaser and mortgage-institution details, attaches supporting documents, selects a payment method, and submits online. The system validates the cited mortgage reference against financial-trust-institutions' Mortgage Registration records, requiring that record to already be `Completed`, before the application proceeds to RERA's review. RERA reviews and issues a Mortgage Provisional Registration Certificate and an Electronic Map.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Sales & Disclosure Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

> **Corrected 2026-08-15, second pass — the attribution was backwards.** This section previously said "typically filed by the Project Registration Officer," inherited from `property-registrations.md`'s old role-gated sidebar scoping rather than checked against what the work actually is. This is a sale registration, the same object as Service #1, just financed by mortgage — `roles-and-responsibilities.md`'s Sales & Disclosure Officer worked example is the closer match, not the Project Registration Officer's, whose example describes creating a new project entirely. The master service table's Responsible Role column agrees: "Sales & Disclosure Officer / Admin Officer" for this row. Checked systematically across all eight sale/lease/usufruct-registration services this applies to (#1–#7, #19). This has no access consequence: any of the four Group B roles may file this application regardless of which is "typical."

## 5. Prerequisites

* Registered developer company account.
* Real estate project already registered with RERA.
* Property/unit exists within that project's approved unit list.
* Purchaser and mortgage institution identified.
* Required supporting documents available.
* **Added 2026-08-16, by client decision, not sourced. The cited mortgage must exist as a `Completed` record in financial-trust-institutions' Mortgage Registration system** — meaning the institution has already carried it through internal certification and RERA's own audit before this application can validate. A mortgage still awaiting either of those gates does not satisfy this prerequisite.

## 6. Required Information

### Property Information

* Project Reference Number
* Unit/Property Identifier

### Purchaser Information

* Full Name
* National Identification Number (NIN)
* Contact Information

### Mortgage Information

* Mortgage Institution
* Mortgage Reference Number *(validated against financial-trust-institutions' Mortgage Registration records — must match a `Completed` record; see Section 12)*
* Mortgage Amount *(checked for consistency against the matched record)*

## 7. Required Documents

> **Proposed** — not itemized in the source beyond "attach documents." Needs client confirmation.

* Provisional Sale Agreement
* Mortgage Offer Letter
* Purchaser Government-issued Identification
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule. Paid through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Yes — before RERA's decision.** The source workflow places payment at the point of submission, ahead of any review: the developer selects a payment method and sends the application in one step. Paid per transaction through the shared platform payment gateway.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**6 business days**, assuming the matching FTI mortgage record is already `Completed` at submission. Not adjusted here for the case where the developer submits before that record has finished FTI's own process — see Section 13 and Business Rules.

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Select "Register Sale Associated with an Initial Mortgage"
↓
Select Property (Unit)
↓
Enter Purchaser and Mortgage Information
↓
Attach Supporting Documents
↓
Select Payment Method
↓
Submit Application Online
↓
**System Validates Mortgage Reference Against Financial & Trust Institutions' Mortgage Registration Records — Requires a `Completed` Match** *(added/decided 2026-08-16)*
↓
*If Not Found, Mismatched, or Not Yet `Completed`:* Application Automatically Returned to Developer *(see Section 13)*
↓
*If Validated:* RERA Reviews Application
↓
Mortgage Provisional Registration Certificate Issued
↓
Electronic Map Issued

## 13. Application Status Flow

Draft
↓
Payment Pending
↓
Payment Successful
↓
Submitted
↓
Validating Mortgage Reference *(added 2026-08-16 — automatic, system-side; not a developer-facing waiting state expected to take meaningful time under normal conditions when the matching FTI record is already `Completed`)*
↓
Under Review
↓
Approved
↓
Registered

### Additional Statuses

* Information Requested
* Returned *(now includes automatic system-generated returns for a mortgage reference not found, mismatched, or not yet `Completed` on financial-trust-institutions' side, in addition to RERA's own manual returns — the application's own return reason should distinguish system-generated returns from RERA's, and should specifically say "mortgage not yet completed" when that is the cause, so the developer knows to wait rather than resubmit incorrect data)*
* Rejected
* Cancelled

## 14. Possible Outcomes

* Mortgage-Linked Sale Successfully Registered
* Additional Information Requested
* Application Returned *(RERA decision, or automatic mortgage-validation failure — including "not yet Completed")*
* Application Rejected
* Payment Failed

## 15. Output

* Mortgage Provisional Registration Certificate
* Electronic Map

## 16. Related Services

* Service #1 – Register Initial Sale
* Service #4 – Amend Initial Procedures Data
* Service #5 – Complete Initial Procedures Data
* Financial & Trust Institutions Service #3 – Mortgage Registration *(cross-module dependency, decided 2026-08-16: this service validates its mortgage reference against FTI Service #3's records, requiring a `Completed` match, before proceeding to RERA's audit — see Sections 5, 12, 13. **The practical sequencing this creates: the institution's mortgage registration must finish first.** This is a product decision, not a sourced requirement. FTI Service #3's own file now cites this service back and exposes a corresponding lookup capability.)*

## 17. UI Screens

* Property Registrations
* Property Registration Details
* Document Upload
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Project Units
* Validate Unit Availability
* **Validate Mortgage Registration** *(added 2026-08-16 — cross-module call to Financial & Trust Institutions' Mortgage Registration records; checks the cited Mortgage Reference Number exists, is `Completed`, and its institution/amount are consistent)*
* Upload Documents
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Submit Mortgage-Linked Sale Registration
* Retrieve Application Status
* Generate Mortgage Provisional Registration Certificate
* Generate Electronic Map
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Property Unit
* Purchaser
* Mortgage Institution
* Property Sale
* Mortgage
* Application
* Document
* Notification
* Payment
* Payment Transaction
* Audit Log

## 20. Acceptance Criteria

* Developer can initiate a mortgage-linked sale registration for a unit within a registered project.
* System validates the unit belongs to a registered project and is available.
* **Mortgage reference is validated against financial-trust-institutions' Mortgage Registration records, and must match a `Completed` record, before the application proceeds to RERA's review** *(decided 2026-08-16)*.
* An application whose mortgage reference cannot be validated — not found, mismatched, or not yet `Completed` — is automatically returned to the developer, with a reason distinguishing it from a RERA-issued return and specifically flagging "not yet completed" where that is the cause.
* Required documents are uploaded before submission.
* Payment is completed before the application proceeds for review.
* Approved applications generate a Mortgage Provisional Registration Certificate and Electronic Map.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a unit belonging to a registered real estate project may be sold under this service.
2. A mortgage institution must be identified for the application to proceed.
3. **Decided 2026-08-16, by client decision, not sourced.** The cited mortgage must be validated against financial-trust-institutions' Mortgage Registration records, and the matched record must have status `Completed`, before the application proceeds to RERA's review. An application that fails this check — including one whose mortgage is still mid-process on FTI's side — is automatically returned to the developer.
4. **Added 2026-08-16.** Because of Rule 3, a developer cannot successfully register a mortgage-linked sale until the financing institution has already carried the mortgage through both of its own gates (internal certification and RERA's audit) on financial-trust-institutions' side. The two applications are sequential, not concurrent, despite this service's "Initial Mortgage" name.
5. Payment must be completed before the application proceeds for regulatory review.
6. Every application receives a unique application reference number.
7. All submissions, approvals, payments, and notifications must be permanently recorded in the audit trail.

## Open Questions

1. ~~Should this service coordinate with financial-trust-institutions' Service #3?~~ **Decided 2026-08-16 — validated.**
2. ~~What stage of the FTI mortgage record's own lifecycle satisfies this validation?~~ **Decided 2026-08-16 — must be `Completed`.**
3. **Still unresolved.** Is this a real-time synchronous API call at submission, or a batch/asynchronous check before RERA's audit stage? The workflow above assumes synchronous for simplicity; not confirmed.
4. **New 2026-08-16.** Given Rule 4's sequencing consequence, should the developer-facing UI actively communicate this dependency before submission — e.g. warning the developer if the cited mortgage isn't yet `Completed`, rather than letting them submit, pay, and only then receive an automatic return? Not addressed in the source screen (`fund-release-request.md`-style guidance doesn't exist for this screen); a UX decision, not resolved here.
5. **New 2026-08-16.** Is there a reasonable maximum wait — should this application expire or require re-validation if the referenced mortgage still hasn't reached `Completed` after some period? Not addressed.
