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

# Service #26 – Submit Tenancy Dispute

**Service Category:** Tenancy Services

## 1. Service Overview

The **Submit Tenancy Dispute** service enables landlords and tenants to submit tenancy-related disputes to RERAN for review, conciliation, adjudication, and resolution. Based on the dispute type selected by the applicant, the system routes the application to the appropriate RERAN dispute process.

## 2. Purpose

Provide a single platform service through which landlords and tenants can initiate tenancy-related dispute proceedings under the appropriate RERAN dispute process.

## 3. Description

The service allows an applicant to select the appropriate dispute category, provide dispute details, upload supporting evidence, and complete the required payment. The application is then routed to the appropriate dispute workflow, where it may proceed through conciliation, adjudication, appeal, or execution depending on the nature of the dispute.

## 4. Who Can Apply

* Registered Tenant  
* Registered Landlord  
* Authorized Property Representative  
* Legal Representative (where legally permitted)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* A registered tenancy relationship exists or sufficient evidence of the tenancy is provided.  
* Supporting evidence is available.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address

### Applicant Information

* Applicant Name  
* Applicant Role (Tenant / Landlord)  
* Contact Information

### Dispute Information

* Dispute Category  
* Subject  
* Description of the Dispute  
* Date of Incident  
* Requested Resolution  
* Additional Remarks (Optional)

## 7. Required Documents

Depending on the dispute category:

* Tenancy Agreement  
* Proof of Payment  
* Communication Records  
* Photographs  
* Supporting Evidence  
* Government-issued Identification  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment timing differs by channel — see Processing Workflow.

**Service Center (Option 1):** documents are submitted and the application is entered and audited first; payment is completed at that point, before the dispute is assigned to a hearing or conciliation track.

**Online (Option 2):** payment is completed before the application is submitted.

*(Corrected 2026-08-15 — this file previously stated a single blanket "before submission" claim, which contradicted Option 1's own workflow below (already correctly ordered) and the sourced order across all ten consolidated dispute rows (72–81). See `payments.md` Category 2.)*

## 10. Processing Authority

**Dispute Adjudication Officer**

## 11. Expected Processing Time

Registration of the dispute application:

* **Approximately 10 minutes**

Service completion depends on the dispute category:

| Dispute Type | Expected Completion |
| ----- | ----- |
| Dispute Case (Amicable Settlement) | 7 Business Days |
| Preliminary Suit | 8 Business Days |
| Appeal Case | 13 Business Days |
| Grievance Case | 13 Business Days |
| Petition to Reconsider | 8 Business Days |
| Order on Petition | 1 Business Day |
| Offer & Deposit | 1 Business Day |
| Performance Order | 1 Business Day |
| Performance Order Grievance | 13 Business Days |
| Execution Case | 1 Business Day |

## 12. Processing Workflow

Option 1 – Service Center

Visit Real Estate Services Trustee Center  
↓  
Submit Required Documents  
↓  
Application Entered into System  
↓  
Application Audited  
↓  
Complete Payment  
↓  
Dispute Assigned  
↓  
Attend Conciliation / Hearing (where applicable)  
↓  
Decision Issued  
↓  
Receive Resolution / Judgment

──────────────────────────────

Option 2 – Online

Login  
↓  
Open Services  
↓  
Select "Submit Tenancy Dispute"  
↓  
Select Dispute Category  
↓  
Complete Dispute Details  
↓  
Upload Supporting Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application  
↓  
Application Assigned  
↓  
Attend Remote Litigation / Hearing (where applicable)  
↓  
Receive Agreement, Assignment or Judgment

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Assigned  
↓  
Under Review  
↓  
Conciliation / Hearing  
↓  
Information Requested  
↓  
Decision Issued  
↓  
Completed

### Additional Statuses

* Returned  
* Rejected  
* Withdrawn  
* Cancelled

## 14. Possible Outcomes

* Amicable Settlement Reached  
* Agreement Signed  
* Assignment Issued  
* Judgment Issued  
* Appeal Decision Issued  
* Petition Decision Issued  
* Performance Order Issued  
* Execution Approved  
* Additional Information Requested  
* Application Rejected

## 15. Output

Depending on the dispute category:

* Settlement Agreement  
* Assignment  
* First Instance Judgment  
* Appeal Judgment  
* Grievance Judgment  
* Petition to Reconsider Judgment  
* Judge's Resolution  
* Performance Order  
* Execution Order

## 16. Related Services

* Service \#23 – Register Lease  
* Service \#24 – Renew Lease  
* Service \#25 – Manage Lease  
* Feature \#2 – Track Application Status  
* Feature \#3 – Respond to Information Request

## 17. UI Screens

* Services  
* Submit Tenancy Dispute  
* Select Dispute Category  
* Dispute Details  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Dispute Details  
* Hearing Schedule (where applicable)  
* Resolution / Judgment

## 18. API Requirements

* Retrieve Registered Leases  
* Retrieve Dispute Categories  
* Validate Applicant  
* Upload Supporting Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Dispute Application  
* Assign Dispute Case  
* Retrieve Application Status  
* Retrieve Hearing Information  
* Generate Resolution Document  
* Download Judgment

## 19. Database Entities

* User  
* Property  
* Lease  
* Tenancy Dispute  
* Dispute Category  
* Hearing  
* Judgment  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* User can submit a tenancy dispute for an eligible tenancy.  
* System validates the applicant before submission.  
* User selects a dispute category.  
* Required documents are uploaded successfully.  
* Payment is completed at the point required by the selected channel.  
* Application receives a unique reference number.  
* System routes the application to the correct dispute process.  
* Hearing or conciliation sessions are scheduled where required.  
* Resolution or judgment is issued upon completion.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only authorized landlords, tenants, or their legal representatives may submit tenancy disputes.  
2. Payment must be completed at the point required by the selected channel — before submission online, or after the Service Center audits the application. *(Corrected 2026-08-15 — see Section 9.)*  
3. Every dispute must be assigned to one official dispute category.  
4. The dispute category determines the workflow, processing time, and expected outcome.  
5. RERAN may conduct conciliation sessions, hearings, or remote litigation depending on the selected dispute type.  
6. Additional information may be requested at any stage of the proceedings.  
7. Every dispute application receives a unique reference number.  
8. Resolution documents or judgments are issued according to the applicable dispute process.  
9. All applications, hearings, judgments, payments, supporting documents, and communications must be permanently recorded in the audit trail.
