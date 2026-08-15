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
  - tenancy
---

# Service #24 – Renew Lease

**Service Category:** Tenancy Services

## 1. Service Overview

The **Renew Lease** service enables a landlord to renew an existing registered tenancy agreement through the RERAN platform. The service updates the tenancy record with the new lease period and revised lease information, ensuring the tenancy remains valid within the official RERAN registry.

## 2. Purpose

Enable landlords to officially renew an existing registered tenancy agreement while maintaining an accurate tenancy record in the RERAN registry.

## 3. Description

The service allows a landlord or an authorized representative to renew an existing lease by selecting a registered tenancy, updating the lease terms where applicable, uploading any revised supporting documents, and completing the applicable service fee. Following review by RERAN, the renewed tenancy is approved and an updated Electronic Contract Registration Certificate is issued.

## 4. Who Can Apply

* Registered Property Owner (Landlord) — **primary applicant**, per the platform's current registration model.  
* Authorized Property Representative.  
* Registered Tenant — **secondary applicant path**, for the same reasons documented in Service #23's Who Can Apply section: the master table (row 82) attributes this service to the Tenant role, and this module's role descriptions give both roles overlapping "renew lease" responsibilities. See `open-questions.md` B1.

*(Corrected 2026-08-15 — "Property Management Company acting on behalf of the owner" removed as a cross-module leak from Group D. See `open-questions.md` B3.)*

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* An active registered lease exists.  
* Applicant has authority to renew the lease (as landlord) or is a party to the tenancy agreement (as tenant).  
* Required supporting documents are available.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type  
* Unit Number (where applicable)

### Existing Lease Information

* Lease Registration Number  
* Current Lease Expiry Date

### Renewal Information

* New Lease Start Date  
* New Lease End Date  
* Lease Duration  
* Updated Annual Rent  
* Updated Payment Frequency  
* Updated Security Deposit (if applicable)  
* Revised Lease Terms (if applicable)  
* Additional Remarks (Optional)

## 7. Required Documents

* Updated Tenancy Agreement  
* Government-issued Identification (where required)  
* Proof of Property Ownership (if requested)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment timing differs by channel — see Processing Workflow.

**Real Estate Services Trustee (Option 1):** documents are submitted and updated lease information entered into the system first; payment is completed once the application is audited, immediately before approval.

**RERA App / Land Department Tenancy System (Option 2, Online):** payment is completed before the application is submitted.

*(Corrected 2026-08-15 — this file previously stated a single blanket "before submission" claim, which contradicted Option 1's own workflow below (already correctly ordered) and the sourced order in row 82. See `payments.md` Category 2.)*

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

* **Via Real Estate Services Trustee:** Approximately **7 minutes** (excluding customer waiting time)  
* **Via RERA App / Land Department Tenancy System:** Immediate

## 12. Processing Workflow

Option 1 – Service Center

Visit Real Estate Services Trustee Center  
↓  
Submit Updated Lease Documents  
↓  
Officer Reviews Documents  
↓  
Updated Lease Information Entered into System  
↓  
Application Audited  
↓  
Pay Service Fee  
↓  
Lease Renewal Approved  
↓  
Receive Updated Electronic Contract Registration Certificate

──────────────────────────────

Option 2 – Online

Login  
↓  
Open Services  
↓  
Select "Renew Lease"  
↓  
Select Registered Lease  
↓  
Update Lease Information  
↓  
Upload Revised Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application  
↓  
Application Reviewed  
↓  
Lease Renewal Approved  
↓  
Receive Updated Electronic Contract Registration Certificate via Email

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
Approved  
↓  
Completed

### Additional Statuses

* Returned  
* Rejected  
* Cancelled  
* Withdrawn  
* Audited — Awaiting Payment *(Real Estate Services Trustee channel only — the application is audited before payment is collected, unlike the online channel's upfront timing shown in the main flow above; see Section 9)*

## 14. Possible Outcomes

* Lease Successfully Renewed  
* Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Updated Electronic Contract Registration Certificate

## 16. Related Services

* Service \#23 – Register Lease  
* Service \#25 – Manage Lease  
* Service \#26 – Submit Tenancy Dispute  
* Service \#3 – Verify Property

## 17. UI Screens

* Services  
* Renew Lease  
* Select Registered Lease  
* Update Lease Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Updated Electronic Contract Registration Certificate

## 18. API Requirements

* Retrieve Registered Leases  
* Retrieve Lease Details  
* Validate Lease  
* Update Lease Information  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Lease Renewal Application  
* Retrieve Application Status  
* Generate Updated Electronic Contract Registration Certificate  
* Download Certificate

## 19. Database Entities

* User  
* Property  
* Lease  
* Lease Renewal  
* Landlord  
* Tenant  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* User can renew an eligible registered lease, as landlord or as tenant.  
* System validates that the applicant is authorized to renew the lease.  
* Updated lease information is validated before submission.  
* Required documents are uploaded successfully.  
* Payment is completed at the point required by the selected channel.  
* Application receives a unique reference number.  
* User can monitor the application status.  
* Approved applications update the registered lease.  
* An updated Electronic Contract Registration Certificate is generated upon approval.  
* Payment receipt is generated after successful payment.  
* All application activities are recorded in the audit log.

## 21. Business Rules

1. The registered property owner (landlord), an authorized representative, or the registered tenant may renew a tenancy agreement. *(Corrected 2026-08-15 — see Section 4 and `open-questions.md` B1.)*  
2. The lease must already be registered with RERAN.  
3. Payment must be completed at the point required by the selected channel — before submission online, or after the Trustee audits the application. *(Corrected 2026-08-15 — see Section 9.)*  
4. Renewal requests must be submitted with all mandatory updated lease information and supporting documents.  
5. Lease renewal becomes effective only after approval by the Compliance & Escrow Auditor.  
6. An updated Electronic Contract Registration Certificate is issued upon successful renewal.  
7. Every lease renewal application receives a unique application reference number.  
8. All submissions, approvals, payments, document uploads, and lease renewal activities must be permanently recorded in the audit trail.  
9. The renewed lease supersedes the previous lease period while preserving the historical lease record.
