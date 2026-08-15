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

# Service #11 – Transfer Lease-to-Own

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Transfer Lease-to-Own** service enables the transfer of an existing registered lease-to-own agreement from the current purchaser to another eligible purchaser, subject to approval by RERAN and compliance with the terms of the original agreement. The service updates the official registry to reflect the new lease-to-own beneficiary while maintaining the integrity of the original property ownership records.

## 2. Purpose

Enable the lawful transfer of rights and obligations under a registered lease-to-own agreement while maintaining an accurate record within the official RERAN property registry.

## 3. Description

The service allows the current lease-to-own purchaser to transfer an existing registered lease-to-own agreement to another eligible purchaser. The application includes the details of the existing agreement, the incoming purchaser, supporting documents, and payment of the applicable service fee. Upon approval by RERAN, the lease-to-own registry is updated and revised registration documents are issued.

## 4. Who Can Apply

### Current Lease-to-Own Purchaser

* Registered Lease-to-Own Purchaser  
* Authorized Representative acting under a valid Power of Attorney

### Incoming Purchaser

* Registered Individual User  
* Eligible Property Purchaser

### Property Owner

* May be required to provide consent where applicable.

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* A valid lease-to-own agreement is already registered.  
* Applicant has legal authority to transfer the agreement.  
* Incoming purchaser information is available.  
* Required supporting documents are available.

## 6. Required Information

### Current Purchaser Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Incoming Purchaser Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Lease-to-Own Information

* Lease-to-Own Registration Number  
* Agreement Date  
* Transfer Date  
* Remaining Contract Period  
* Transfer Reason  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Lease-to-Own Registration Certificate  
* Lease-to-Own Agreement  
* Transfer Agreement  
* Government-issued Identification (Current Purchaser)  
* Government-issued Identification (Incoming Purchaser)  
* Property Owner Consent (where required)  
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

**Approximately 25 minutes.**

## 12. Processing Workflow

Option 1 – Real Estate Registration Trustee Centre

Visit Real Estate Registration Trustee Centre  
↓  
Submit Required Documents  
↓  
Officer Enters Lease-to-Own Transfer into System  
↓  
Transaction Audited  
↓  
Pay Service Fee  
↓  
Receive Updated Registration Documents via Email

──────────────────────────

Option 2 – Online

Current Lease-to-Own Purchaser

Login  
↓  
Open Services  
↓  
Select "Transfer Lease-to-Own"  
↓  
Select Registered Lease-to-Own Agreement  
↓  
Enter Incoming Purchaser Information  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application

↓

Incoming Purchaser

Receive Notification  
↓  
Login  
↓  
Review Lease-to-Own Transfer Details  
↓  
Review Property Information  
↓  
Accept Transfer  
↓  
Confirm Identity  
↓  
Confirm Participation

↓

RERAN

Review Application  
↓  
Verify Documents  
↓  
Verify Eligibility  
↓  
Approve Lease-to-Own Transfer  
↓  
Update Lease-to-Own Registry  
↓  
Generate Updated Registration Documents  
↓  
Notify All Parties

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Incoming Purchaser Confirmation Pending *(Online only)*  
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
* Incoming Purchaser Declined *(Online only)*  
* Audited — Awaiting Payment *(Trustee Centre channel only — the transaction is audited before payment is collected, unlike the online channel's upfront timing shown in the main flow above; see Section 9)*

## 14. Possible Outcomes

* Lease-to-Own Successfully Transferred  
* Transfer Successfully Registered  
* Incoming Purchaser Accepted Transfer *(Online only)*  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Incoming Purchaser Declined Transfer *(Online only)*

## 15. Output

Upon successful completion, the system generates:

* Updated Lease-to-Own Registration Certificate  
* Updated Electronic Certificate of Title (where applicable)  
* Updated Electronic Title Deed (where applicable)  
* Updated Property Registry Record  
* Property Map  
* Payment Receipt

## 16. Related Services

* Service \#10 – Register Lease-to-Own  
* Service \#12 – Release Lease-to-Own  
* Service \#13 – Amend Lease-to-Own  
* Service \#5 – Transfer Property Ownership

## 17. UI Screens

* Services  
* Transfer Lease-to-Own  
* Select Registered Agreement  
* Incoming Purchaser Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Transfer Confirmation

## 18. API Requirements

* Retrieve Registered Lease-to-Own Agreements  
* Retrieve Agreement Details  
* Validate Current Purchaser  
* Validate Incoming Purchaser  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Lease-to-Own Transfer Application  
* Retrieve Application Status  
* Update Lease-to-Own Registry  
* Generate Updated Registration Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Lease-to-Own Agreement  
* Lease-to-Own Transfer  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Current lease-to-own purchaser can initiate a transfer for an eligible agreement.  
* System validates that the agreement is active and transferable.  
* Incoming purchaser successfully confirms participation *(Online channel)*.  
* Required information is validated before submission.  
* Required documents are uploaded successfully.  
* Payment is completed at the point required by the selected channel.  
* Application receives a unique application reference number.  
* Approved applications update the official lease-to-own registry.  
* Updated registration documents are generated upon approval.  
* All involved parties receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the registered lease-to-own purchaser or an authorized representative may initiate a transfer.  
2. The lease-to-own agreement must already be registered with RERAN.  
3. The incoming purchaser must meet the eligibility requirements established by RERAN.  
4. Payment must be completed at the point required by the selected channel — before submission online, or after the Trustee Centre audits the transaction. *(Corrected 2026-08-15 — see Section 9.)*  
5. The incoming purchaser must confirm acceptance before the transfer can be approved, where applicable to the selected channel.  
6. Property owner consent shall be obtained where required by the terms of the lease-to-own agreement or applicable regulations.  
7. The transfer becomes legally effective only after approval by RERAN and the lease-to-own registry is updated.  
8. Updated registration documents are issued upon successful completion of the transfer.  
9. Every Lease-to-Own Transfer application receives a unique application reference number.  
10. All applications, approvals, payments, participant confirmations, registry updates, document submissions, and notifications must be permanently recorded in the audit trail.
