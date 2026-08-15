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
  - real-estate-development-services
---

# Service #7 – Transfer Registration Fees Between Properties

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Transfer Registration Fees Between Properties** service allows a developer to apply previously paid registration fees from one property/unit application to another, rather than paying the fee again — for example when a sale falls through on one unit and is redirected to a different unit for the same purchaser.

> **UI gap — flagged, not resolved.** No screen in `ui/screens/property-registrations.md` or `property-registration-details.md` (or elsewhere in the 19-screen set) exposes a fee-transfer action between two property applications. The UI Screens list below is a **proposed** minimum surface, not a documented existing one. See the PR description for the full list of source rows with no matching screen.

## 2. Purpose

Avoid double-charging developers for registration fees already paid, when a registration application is redirected from one property to another under the same overall transaction.

## 3. Description

The developer identifies the source application whose fee was paid, the destination property/unit, and the reason for the transfer, and submits the request. RERA reviews and, on approval, applies the existing fee credit to the destination application and issues a Provisional Registration Contract reflecting the transferred fee.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Sales & Disclosure Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

> **Corrected 2026-08-15, second pass — the attribution was backwards.** This section previously said "typically filed by the Project Registration Officer," inherited from historical UI-screen sidebar scoping rather than checked against what the work actually is. This service manages a fee credit between two sale/unit applications — a Sales & Disclosure matter, not project registration. The master service table's Responsible Role column agrees: "Sales & Disclosure Officer / Admin Officer" for this row. Checked systematically across all eight sale/lease/usufruct-registration services this applies to (#1–#7, #19). This has no access consequence: any of the four Group B roles may file this application regardless of which is "typical."

## 5. Prerequisites

* A prior registration application with a paid, transferable fee.
* Destination property/unit identified.
* Reason for the transfer.

## 6. Required Information

* Source Application Reference Number
* Destination Property/Unit Identifier
* Reason for Transfer

## 7. Required Documents

> **Proposed** — the source row names only the output document, not required inputs. Needs client confirmation.

* Written Justification for the Transfer
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule — subject to the fee credit being transferred, per the service's purpose. Any balance payable is charged through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Conditional — before RERA's decision where payable.** The source places payment selection at submission, ahead of review, as with the other initial-procedures services. No new payment where the transferred credit fully covers the destination application; a shortfall is charged per transaction through the shared platform payment gateway. The shortfall handling is not specified in the source; **proposed**, needs client confirmation.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**6 business days**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Select "Transfer Registration Fees"
↓
Identify Source Application and Destination Property
↓
Provide Reason for Transfer
↓
Submit Application Online
↓
RERA Reviews Application
↓
Fee Credit Applied to Destination Application
↓
Provisional Registration Contract Issued

## 13. Application Status Flow

Draft
↓
Submitted
↓
Under Review
↓
Approved
↓
Fee Transferred

### Additional Statuses

* Information Requested
* Returned
* Rejected
* Cancelled

## 14. Possible Outcomes

* Fee Successfully Transferred
* Additional Information Requested
* Application Returned
* Application Rejected

## 15. Output

* Provisional Registration Contract

## 16. Related Services

* Service #1 – Register Initial Sale
* Service #4 – Amend Initial Procedures Data

## 17. UI Screens

Not currently represented in the 19-screen UI set. **Proposed** minimum surface: a "Transfer Fee" action from Property Registration Details, following the pattern of the module's other in-context detail actions.

## 18. API Requirements

* Retrieve Source Application Fee Status
* Validate Destination Property
* Submit Fee Transfer Application
* Apply Fee Credit
* Retrieve Application Status
* Generate Provisional Registration Contract
* Send Notifications

## 19. Database Entities

* Developer Company
* Property Unit
* Application
* Fee Transfer
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request that a paid registration fee be applied to a different property/unit application.
* System validates the source application's fee is eligible for transfer.
* Reason for the transfer is required.
* Approved transfers generate a Provisional Registration Contract.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a fee already paid on an eligible source application may be transferred.
2. A reason for the transfer is required for every submission.
3. Every application receives a unique application reference number.
4. All submissions, approvals, and fee-credit movements must be permanently recorded in the audit trail.
5. **No UI screen currently exists for this service** — flagged for the client rather than force-fit to an existing screen.
