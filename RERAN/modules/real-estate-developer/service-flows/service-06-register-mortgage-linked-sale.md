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

The **Register Sale Associated with an Initial Mortgage** service allows a developer to register the provisional sale of a unit where the purchaser is financing the purchase through a mortgage. The application captures the mortgage institution, reference number, and amount, and — **by client decision, 2026-08-16** — validates that reference against financial-trust-institutions' Mortgage Registration records before the application can proceed to RERA's audit.

> **Corrected 2026-08-16, twice.** First pass found that the previously-asserted "coordinating... linking" relationship to financial-trust-institutions' Service #3 was an unconfirmed inference, not a sourced fact — the raw workflow just captures mortgage data as reference fields, with no validation described. That correction surfaced a genuine open question: should this service actually validate the mortgage, or stay independent? **Decided 2026-08-16: validated.** This service now performs that validation, modelled on the platform's own standard pipeline (`RERAN_service_flows_v2.md`'s Workflow Stages: *"2 Validate — System checks completeness, statutory windows, and pre-conditions (e.g. active escrow)"*) — treating "mortgage genuinely registered with the cited institution" as a pre-condition of the same kind the platform already validates elsewhere (e.g. active escrow). This is a documented product decision extending beyond what source specifies, not itself sourced — flagged accordingly throughout.

## 2. Purpose

Provide a regulated, provisional record of a mortgage-financed unit sale, validated against the actual mortgage registration held by the financing institution, under a single project unit.

## 3. Description

The developer selects the property, records the purchaser and mortgage-institution details, attaches supporting documents, selects a payment method, and submits online. The system validates the cited mortgage reference against financial-trust-institutions' Mortgage Registration records before the application proceeds to RERA's review. RERA reviews and issues a Mortgage Provisional Registration Certificate and an Electronic Map.

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
* **Added 2026-08-16, by client decision, not sourced.** The cited mortgage must exist as a record in financial-trust-institutions' Mortgage Registration system — see Section 12 and Open Questions for exactly what stage of that record's own lifecycle is required, which is not yet settled.

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
* Mortgage Reference Number *(validated against financial-trust-institutions' Mortgage Registration records — see Section 12)*
* Mortgage Amount *(checked for consistency against the matched record, where found)*

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

**6 business days**

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
**System Validates Mortgage Reference Against Financial & Trust Institutions' Mortgage Registration Records** *(added 2026-08-16, by client decision)*
↓
*If Not Found or Mismatched:* Application Automatically Returned to Developer *(see Section 13)*
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
Validating Mortgage Reference *(added 2026-08-16 — automatic, system-side; not a developer-facing waiting state expected to take meaningful time under normal conditions)*
↓
Under Review
↓
Approved
↓
Registered

### Additional Statuses

* Information Requested
* Returned *(now includes automatic system-generated returns for a mortgage reference not found or mismatched against financial-trust-institutions' records, in addition to RERA's own manual returns — the application's own return reason should distinguish the two, per Open Questions)*
* Rejected
* Cancelled

## 14. Possible Outcomes

* Mortgage-Linked Sale Successfully Registered
* Additional Information Requested
* Application Returned *(RERA decision, or automatic mortgage-validation failure)*
* Application Rejected
* Payment Failed

## 15. Output

* Mortgage Provisional Registration Certificate
* Electronic Map

## 16. Related Services

* Service #1 – Register Initial Sale
* Service #4 – Amend Initial Procedures Data
* Service #5 – Complete Initial Procedures Data
* Financial & Trust Institutions Service #3 – Mortgage Registration *(cross-module dependency, confirmed by client decision 2026-08-16: this service now validates its mortgage reference against FTI Service #3's records before proceeding to RERA's audit — see Section 12. This is a product decision, not a sourced requirement; the master source table and FTI Service #3's own file do not describe this coordination. FTI Service #3's own Related Services still does not cite this service back — worth adding once the validation mechanism itself is confirmed, see Open Questions.)*

## 17. UI Screens

* Property Registrations
* Property Registration Details
* Document Upload
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Project Units
* Validate Unit Availability
* **Validate Mortgage Registration** *(added 2026-08-16 — cross-module call to Financial & Trust Institutions' Mortgage Registration records; checks the cited Mortgage Reference Number exists and its institution/amount are consistent)*
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
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can initiate a mortgage-linked sale registration for a unit within a registered project.
* System validates the unit belongs to a registered project and is available.
* **Mortgage reference is validated against financial-trust-institutions' Mortgage Registration records before the application proceeds to RERA's review** *(added 2026-08-16)*.
* An application whose mortgage reference cannot be validated is automatically returned to the developer, with a reason distinguishing it from a RERA-issued return.
* Required documents are uploaded before submission.
* Payment is completed before the application proceeds for review.
* Approved applications generate a Mortgage Provisional Registration Certificate and Electronic Map.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a unit belonging to a registered real estate project may be sold under this service.
2. A mortgage institution must be identified for the application to proceed.
3. **Added 2026-08-16, by client decision, not sourced.** The cited mortgage must be validated against financial-trust-institutions' Mortgage Registration records before the application proceeds to RERA's review. An application that fails this check is automatically returned to the developer.
4. Payment must be completed before the application proceeds for regulatory review.
5. Every application receives a unique application reference number.
6. All submissions, approvals, payments, and notifications must be permanently recorded in the audit trail.

## Open Questions

1. ~~Should this service coordinate with financial-trust-institutions' Service #3?~~ **Decided 2026-08-16 — validated.**
2. **New 2026-08-16, unresolved.** What stage of the FTI mortgage record's own lifecycle satisfies this validation? FTI's Mortgage Registration (Service #3) has its own two-gate process (internal certification, then RERA audit) before reaching `Completed`. Given this service's name — "Register Sale Associated with an *Initial* Mortgage" — the mortgage may well be filed on FTI's side around the same time as this sale, not pre-existing and already complete. Requiring a fully `Completed` FTI record could create a chicken-and-egg ordering problem between the two modules. Whether validation should accept any existing FTI record regardless of its own status, or require it to have reached a specific stage, is not settled here.
3. **New 2026-08-16, unresolved.** Is this a real-time synchronous API call at submission, or a batch/asynchronous check before RERA's audit stage? The workflow above assumes synchronous for simplicity; not confirmed.
4. **New 2026-08-16, unresolved.** Should financial-trust-institutions' Service #3 cite this service back in its own Related Services, and does it need a corresponding "expose mortgage lookup" API requirement on its own side? Not yet added there — see that file.
