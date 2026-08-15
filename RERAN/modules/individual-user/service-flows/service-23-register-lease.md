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

# Service #23 – Register Lease

**Service Category:** Tenancy Services

## 1. Service Overview

The **Register Lease** service enables a landlord to officially register a tenancy contract with RERAN. The service records the tenancy agreement in the official tenancy registry, validates the submitted lease information and supporting documents, and issues an Electronic Contract Registration Certificate upon successful approval.

## 2. Purpose

Enable landlords to officially register tenancy agreements with RERAN, creating a legally recognized tenancy record within the official registry.

## 3. Description

The service allows a landlord or an authorized representative to register a new tenancy agreement by providing the property details, tenant information, lease information, supporting documents, and completing the applicable service fee. Following review by RERAN, the tenancy contract is registered and an Electronic Contract Registration Certificate is issued.

## 4. Who Can Apply

* Registered Property Owner (Landlord) — **primary applicant**, per the platform's current registration model.  
* Authorized Property Representative.  
* Registered Tenant — **secondary applicant path.** The master service table (row 82) attributes this service to the Tenant role, and this module's role descriptions give Landlord and Tenant overlapping "register/renew lease" responsibilities. Rather than treat one attribution as simply wrong, both are documented: a tenant may initiate registration of a lease they have signed, in addition to a landlord registering a lease they are letting out. See `open-questions.md` B1 for the full reasoning and the conflict check performed before adopting this resolution. Detailed screen design for the tenant-initiated path is deferred to when this module's UI work begins.

*(Corrected 2026-08-15 — "Property Management Company acting on behalf of the owner" removed. That was Group D's Property Management Officer role, a cross-module leak into this list; it is not an Individual User concept. See `open-questions.md` B3.)*

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Applicant has authority to lease the property (as landlord) or is a party to the tenancy agreement (as tenant).  
* A tenancy agreement has been executed between the landlord and tenant.  
* Required supporting documents are available.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type  
* Unit Number (where applicable)

### Landlord Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Tenant Information

* Full Name  
* National Identification Number (where applicable)  
* Contact Number  
* Email Address

### Lease Information

* Lease Start Date  
* Lease End Date  
* Lease Duration  
* Annual Rent  
* Rent Payment Frequency  
* Security Deposit (if applicable)  
* Lease Purpose  
* Additional Terms (Optional)

## 7. Required Documents

* Signed Tenancy Agreement  
* Government-issued Identification (Landlord)  
* Government-issued Identification (Tenant)  
* Proof of Property Ownership  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment timing differs by channel — see Processing Workflow.

**Real Estate Services Trustee (Option 1):** documents are submitted and lease information entered into the system first; payment is completed once the application is audited, immediately before approval.

**RERA App / Land Department Tenancy System (Option 2, Online):** payment is completed before the application is submitted.

*(Corrected 2026-08-15 — this file previously stated a single blanket "before submission" claim in this section, which contradicted Option 1's own workflow below (already correctly ordered) and the sourced order in row 82. Only this section's wording was wrong. See `payments.md` Category 2.)*

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

* **Via Real Estate Services Trustee:** Approximately **7 minutes** (excluding customer waiting time)  
* **Via RERA App / Land Department Tenancy System:** Immediate

## 12. Processing Workflow

Option 1 – Service Center

Visit Real Estate Services Trustee Center  
↓  
Submit Required Documents  
↓  
Officer Reviews Documents  
↓  
Lease Information Entered into System  
↓  
Application Audited  
↓  
Pay Service Fee  
↓  
Lease Registration Approved  
↓  
Receive Electronic Contract Registration Certificate

──────────────────────────────

Option 2 – Online

Login  
↓  
Open Services  
↓  
Select "Register Lease"  
↓  
Enter Lease Information  
↓  
Attach Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application  
↓  
Application Reviewed  
↓  
Lease Registration Approved  
↓  
Receive Electronic Contract Registration Certificate via Email

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

* Lease Successfully Registered  
* Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Electronic Contract Registration Certificate

## 16. Related Services

* Service \#24 – Renew Lease  
* Service \#25 – Manage Lease  
* Service \#26 – Submit Tenancy Dispute  
* Service \#3 – Verify Property

## 17. UI Screens

* Services  
* Register Lease  
* Property Information  
* Tenant Information  
* Lease Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Electronic Contract Registration Certificate

## 18. API Requirements

* Retrieve User Properties  
* Validate Property Ownership  
* Validate Tenant Information  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Lease Registration Application  
* Retrieve Application Status  
* Generate Electronic Contract Registration Certificate  
* Download Certificate

## 19. Database Entities

* User  
* Property  
* Lease  
* Landlord  
* Tenant  
* Lease Registration  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* User can register a tenancy agreement for an eligible property, as landlord or as tenant.  
* System validates that the applicant is authorized to register the agreement.  
* Required information is successfully validated.  
* Required documents are uploaded successfully.  
* Payment is completed at the point required by the selected channel.  
* Application receives a unique reference number.  
* User can monitor the application status.  
* Approved applications generate an Electronic Contract Registration Certificate.  
* Payment receipt is generated after successful payment.  
* All application activities are recorded in the audit log.

## 21. Business Rules

1. The registered property owner (landlord), an authorized representative, or the registered tenant may register a tenancy agreement. *(Corrected 2026-08-15 — see Section 4 and `open-questions.md` B1.)*  
2. The property must already exist in the RERAN property registry.  
3. Payment must be completed at the point required by the selected channel — before submission online, or after the Trustee audits the application. *(Corrected 2026-08-15 — see Section 9.)*  
4. All mandatory tenancy information and supporting documents must be provided before review.  
5. Lease registration becomes effective only after approval by the Compliance & Escrow Auditor.  
6. An Electronic Contract Registration Certificate is issued upon successful registration.  
7. Every lease registration application receives a unique application reference number.  
8. All submissions, approvals, payments, document uploads, and tenancy registrations must be permanently recorded in the audit trail.  
9. Once registered, the lease may subsequently be renewed through the **Renew Lease** service or terminated through the appropriate tenancy service.
