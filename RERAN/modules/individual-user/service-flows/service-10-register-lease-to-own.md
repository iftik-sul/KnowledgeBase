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

# Service #10 – Register Lease-to-Own

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Register Lease-to-Own** service enables a property owner and an eligible purchaser to register a lease-to-own agreement with RERAN. The service records the agreement in the official property registry, allowing the purchaser to occupy or lease the property with the contractual right to acquire ownership upon satisfying the agreed lease-to-own terms.

## 2. Purpose

Enable property owners and purchasers to establish a legally recognized lease-to-own arrangement that is recorded and regulated by RERAN.

## 3. Description

The service allows the property owner to initiate a lease-to-own registration by submitting the agreement, identifying the purchaser, providing property details, uploading supporting documents, and paying the applicable service fee. Following review and approval by RERAN, the lease-to-own agreement is officially registered and the corresponding registration documents are issued.

## 4. Who Can Apply

### Property Owner

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney

### Lease-to-Own Purchaser

* Registered Individual User  
* Eligible Property Purchaser  
* Authorized Representative (where legally permitted)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Property owner has legal authority to enter into the lease-to-own agreement.  
* Purchaser information is available.  
* Lease-to-own agreement has been prepared.  
* Required supporting documents are available.

## 6. Required Information

### Property Owner Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Purchaser Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Lease-to-Own Information

* Agreement Date  
* Lease Start Date  
* Lease End Date  
* Purchase Option Date  
* Purchase Price  
* Lease Payment Amount  
* Payment Schedule  
* Additional Terms  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Certificate of Title  
* Lease-to-Own Agreement  
* Government-issued Identification (Property Owner)  
* Government-issued Identification (Purchaser)  
* Proof of Property Ownership  
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
Officer Enters Lease-to-Own Registration into System  
↓  
Transaction Audited  
↓  
Pay Service Fee  
↓  
Receive Registration Documents via Email

──────────────────────────

Option 2 – Online

Property Owner

Login  
↓  
Open Services  
↓  
Select "Register Lease-to-Own"  
↓  
Select Registered Property  
↓  
Enter Purchaser Information  
↓  
Enter Lease-to-Own Details  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application

↓

Purchaser

Receive Notification  
↓  
Login  
↓  
Review Lease-to-Own Agreement  
↓  
Review Property Details  
↓  
Accept Agreement  
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
Approve Lease-to-Own Registration  
↓  
Update Property Registry  
↓  
Generate Registration Documents  
↓  
Notify Property Owner & Purchaser

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Purchaser Confirmation Pending *(Online only)*  
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
* Purchaser Declined *(Online only)*

## 14. Possible Outcomes

* Lease-to-Own Successfully Registered  
* Agreement Successfully Recorded  
* Purchaser Accepted Agreement *(Online only)*  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Purchaser Declined Agreement *(Online only)*

## 15. Output

Upon successful completion, the system generates:

* Electronic Certificate of Title  
* Electronic Title Deed  
* Usufruct Title Deed (where applicable)  
* Statement Certificate  
* Provisional Sale Registration Certificate  
* Property Map  
* Fee Balance Information

## 16. Related Services

* Service \#11 – Transfer Lease-to-Own  
* Service \#12 – Release Lease-to-Own  
* Service \#13 – Amend Lease-to-Own  
* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale

## 17. UI Screens

* Services  
* Register Lease-to-Own  
* Select Property  
* Purchaser Information  
* Lease-to-Own Agreement  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Registration Confirmation

## 18. API Requirements

* Retrieve User Properties  
* Retrieve Property Details  
* Validate Property Ownership  
* Validate Purchaser  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Lease-to-Own Registration Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Registration Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Lease-to-Own Agreement  
* Lease-to-Own Registration  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Property owner can register a lease-to-own agreement for an eligible property.  
* System validates ownership before submission.  
* Purchaser successfully confirms participation *(Online channel)*.  
* Required information is validated before submission.  
* Required documents are uploaded successfully.  
* Payment is completed at the point required by the selected channel.  
* Application receives a unique application reference number.  
* Approved applications update the official property registry.  
* Registration documents are generated after successful approval.  
* Property owner and purchaser receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the registered property owner or an authorized representative may initiate a lease-to-own registration.  
2. The property must be registered in the official RERAN property registry.  
3. The lease-to-own agreement must identify both the property owner and the purchaser.  
4. Payment must be completed at the point required by the selected channel — before submission online, or after the Trustee Centre audits the transaction. *(Corrected 2026-08-15 — see Section 9.)*  
5. The purchaser must confirm participation before the application can be approved, where applicable to the selected channel.  
6. The lease-to-own arrangement becomes officially registered only after approval by RERAN.  
7. Registration documents are issued upon successful completion of the registration process.  
8. Every lease-to-own registration application receives a unique application reference number.  
9. Any future transfer, amendment, or release of the agreement must be processed through the corresponding Lease-to-Own services.  
10. All applications, approvals, payments, agreement details, document uploads, registry updates, and notifications must be permanently recorded in the audit trail.
