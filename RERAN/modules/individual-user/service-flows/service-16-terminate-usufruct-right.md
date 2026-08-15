---
project: RERAN
module: individual-user
type: service-flow
status: current
source_type: sourced
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - individual-user
  - service-flow
  - property-ownership-transaction
---

# Service #16 – Terminate Usufruct Right

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Terminate Usufruct Right** service enables authorized parties to legally terminate an existing registered usufruct right before or upon the completion of its validity period. Upon approval, the usufruct right is removed from the official property registry, the property records are updated, and the appropriate registration documents are issued.

## 2. Purpose

Enable the lawful termination of registered usufruct rights while maintaining accurate and up-to-date ownership records within the official RERAN property registry.

## 3. Description

The service allows eligible applicants to request the termination of an existing registered usufruct right. The applicant submits the required information, supporting documents, and applicable service fee. Following verification and approval, the usufruct registration is terminated, the property registry is updated, and revised registration documents are generated where applicable.

## 4. Who Can Apply

### Property Owner

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney

### Registered Usufruct Beneficiary

* Registered Individual User  
* Registered Legal Entity (where applicable)  
* Authorized Representative (where legally permitted)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* A registered usufruct right exists.  
* Applicant is authorized to request termination.  
* All contractual or legal obligations relating to the usufruct have been fulfilled.  
* Required supporting documents are available.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Existing Usufruct Information

* Usufruct Registration Number  
* Registration Date

### Termination Information

* Termination Date  
* Termination Reason  
* Mutual Consent Status (where applicable)  
* Court Order Reference (where applicable)  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Usufruct Registration Certificate  
* Existing Usufruct Agreement  
* Government-issued Identification  
* Proof of Property Ownership  
* Termination Agreement or Court Order (where applicable)  
* Proof of Payment  
* Power of Attorney (where applicable)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment timing differs by channel — see Processing Workflow.

**Real Estate Registration Trustee Centre:** documents are submitted and entered into the system first; payment is completed once the transaction is audited, immediately before the output is issued. Sourced by inheritance from row 86 ("same as sale registration"), per `services-overview.md`.

**Online:** payment is completed before the application is submitted.

*(Corrected 2026-08-15 — this file previously documented only the online path. See `payments.md` Category 3.)*

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**10–15 minutes.**

## 12. Processing Workflow

Option 1 – Real Estate Registration Trustee Centre

Visit Real Estate Registration Trustee Centre  
↓  
Submit Required Documents  
↓  
Officer Enters Usufruct Termination into System  
↓  
Transaction Audited  
↓  
Pay Service Fee  
↓  
Receive Termination Documents via Email

──────────────────────────

Option 2 – Online

Applicant

Login  
↓  
Open Services  
↓  
Select "Terminate Usufruct Right"  
↓  
Select Registered Usufruct Right  
↓  
Provide Termination Information  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application

↓

RERAN

Review Application  
↓  
Verify Existing Registration  
↓  
Verify Supporting Documents  
↓  
Confirm Termination Eligibility  
↓  
Approve Termination  
↓  
Update Property Registry  
↓  
Generate Updated Registration Documents  
↓  
Notify Applicant

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Under Review  
↓  
Information Requested  
↓  
Resubmitted  
↓  
Approved  
↓  
Completed

### Additional Statuses

* Returned  
* Rejected  
* Cancelled  
* Withdrawn  
* Audited — Awaiting Payment *(Trustee Centre channel only — the transaction is audited before payment is collected, unlike the online channel's upfront timing shown in the main flow above; see Section 9)*

## 14. Possible Outcomes

* Usufruct Right Successfully Terminated  
* Registry Successfully Updated  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Usufruct Termination Confirmation  
* Updated Electronic Certificate of Title (where applicable)  
* Updated Electronic Title Deed (where applicable)  
* Updated Property Registry Record  
* Payment Receipt

## 16. Related Services

* Service \#14 – Register Usufruct Right  
* Service \#15 – Amend Usufruct Right  
* Service \#5 – Transfer Property Ownership  
* Service \#7 – Update Property Ownership Information

## 17. UI Screens

* Services  
* Terminate Usufruct Right  
* Select Registered Usufruct Right  
* Termination Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Termination Confirmation

## 18. API Requirements

* Retrieve Registered Usufruct Rights  
* Retrieve Usufruct Details  
* Validate Registration Status  
* Validate Applicant  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Termination Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Termination Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Usufruct Right  
* Usufruct Termination  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit a termination request for an eligible registered usufruct right.  
* System validates that the usufruct right is active and eligible for termination.  
* Required information is validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed at the point required by the selected channel.  
* Application receives a unique application reference number.  
* Approved applications update the official property registry.  
* Updated registration documents are generated where applicable.  
* Applicant receives completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only authorized parties to a registered usufruct right or their authorized representatives may request termination.  
2. The usufruct right must be active and registered before a termination request can be submitted.  
3. Termination may require the consent of all relevant parties or a legally enforceable order, where applicable.  
4. Payment must be completed at the point required by the selected channel — before submission online, or after the Trustee Centre audits the transaction. *(Corrected 2026-08-15 — see Section 9.)*  
5. The usufruct right is considered terminated only after approval by RERAN.  
6. The official property registry is updated only after the termination has been approved.  
7. Updated registration documents are issued where the termination affects the registered property records.  
8. Every Terminate Usufruct Right application receives a unique application reference number.  
9. The terminated usufruct record must remain permanently available as part of the property's historical registration records.  
10. All applications, approvals, payments, registry updates, document submissions, termination records, and notifications must be permanently recorded in the audit trail.
