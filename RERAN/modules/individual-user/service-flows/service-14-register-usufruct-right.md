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

# Service #14 – Register Usufruct Right

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Register Usufruct Right** service enables a property owner to register a usufruct right over a property in accordance with applicable property laws and RERAN regulations. Upon successful registration, the usufruct right is officially recorded in the property registry, and the relevant registration documents are issued to the parties.

## 2. Purpose

Enable property owners to legally establish and register usufruct rights while maintaining accurate records within the official RERAN property registry.

## 3. Description

The service allows an eligible property owner to register a usufruct right by identifying the beneficiary, providing property details, submitting the required supporting documents, and paying the applicable service fee. Following review and approval, the usufruct right is recorded in the official registry and the appropriate registration documents are generated.

## 4. Who Can Apply

### Property Owner

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney

### Usufruct Beneficiary

* Registered Individual User  
* Registered Legal Entity (where applicable)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Applicant has legal authority over the property.  
* Usufruct beneficiary information is available.  
* Required supporting documents are available.

## 6. Required Information

### Property Owner Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Beneficiary Information

* Full Name / Organization Name  
* National Identification Number or Registration Number  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Usufruct Information

* Usufruct Start Date  
* Usufruct End Date  
* Duration  
* Scope of Rights  
* Conditions and Restrictions (if applicable)  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Certificate of Title  
* Government-issued Identification (Property Owner)  
* Government-issued Identification (Beneficiary)  
* Proof of Property Ownership  
* Usufruct Agreement  
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

**Maximum 30 minutes.**

## 12. Processing Workflow

Option 1 – Real Estate Registration Trustee Centre

Visit Real Estate Registration Trustee Centre  
↓  
Submit Required Documents  
↓  
Officer Enters Usufruct Registration into System  
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
Select "Register Usufruct Right"  
↓  
Select Registered Property  
↓  
Enter Beneficiary Information  
↓  
Enter Usufruct Details  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application

↓

Beneficiary

Receive Notification  
↓  
Login  
↓  
Review Usufruct Details  
↓  
Confirm Acceptance  
↓  
Confirm Identity

↓

RERAN

Review Application  
↓  
Verify Property Ownership  
↓  
Verify Supporting Documents  
↓  
Approve Usufruct Registration  
↓  
Update Property Registry  
↓  
Generate Registration Documents  
↓  
Notify Property Owner & Beneficiary

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Beneficiary Confirmation Pending *(Online only)*  
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
* Beneficiary Declined *(Online only)*

## 14. Possible Outcomes

* Usufruct Right Successfully Registered  
* Property Registry Successfully Updated  
* Beneficiary Accepted Registration *(Online only)*  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Electronic Usufruct Registration Certificate  
* Electronic Usufruct Title Deed  
* Updated Property Registry Record  
* Property Map  
* Payment Receipt

## 16. Related Services

* Service \#15 – Amend Usufruct Right  
* Service \#16 – Terminate Usufruct Right  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#7 – Update Property Ownership Information

## 17. UI Screens

* Services  
* Register Usufruct Right  
* Select Property  
* Beneficiary Information  
* Usufruct Details  
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
* Validate Beneficiary  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Usufruct Registration Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Registration Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Usufruct Right  
* Usufruct Beneficiary  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Property owner can register a usufruct right for an eligible property.  
* System validates ownership before submission.  
* Beneficiary successfully confirms participation *(Online channel)*.  
* Required information is validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed at the point required by the selected channel.  
* Application receives a unique application reference number.  
* Approved applications update the official property registry.  
* Registration documents are generated after successful approval.  
* Property owner and beneficiary receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the registered property owner or an authorized representative may register a usufruct right.  
2. The property must be registered in the official RERAN property registry.  
3. The beneficiary must be identified before the application is submitted.  
4. Payment must be completed at the point required by the selected channel — before submission online, or after the Trustee Centre audits the transaction. *(Corrected 2026-08-15 — see Section 9.)*  
5. The beneficiary may be required to confirm acceptance before registration is finalized, where applicable to the selected channel.  
6. The usufruct right becomes legally effective only after approval by RERAN and registration in the official property registry.  
7. An Electronic Usufruct Registration Certificate and related registration documents are issued upon successful registration.  
8. Every Register Usufruct Right application receives a unique application reference number.  
9. Any future amendment or termination of the registered usufruct right must be completed through the appropriate RERAN service.  
10. All applications, approvals, payments, registry updates, document submissions, beneficiary confirmations, and notifications must be permanently recorded in the audit trail.
