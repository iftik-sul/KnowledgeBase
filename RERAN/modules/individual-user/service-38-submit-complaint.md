---
project: RERAN
module: individual-user
type: service-flow
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/individual-user/RERAN_ individual user_service_flows.md"
tags:
  - individual-user
  - service-flow
  - consumer-protection
---

# Service #38 – Submit Complaint

**Service Category:** Consumer Protection Services

## 1. Service Overview

The **Submit Complaint** service enables an Individual User to formally report complaints related to real estate activities, registered developers, real estate practitioners, property transactions, tenancy matters, or other services regulated by RERAN. The service provides a structured process for lodging complaints, submitting supporting evidence, and obtaining regulatory intervention where appropriate.

## 2. Purpose

Provide individuals with an official channel to report grievances and request regulatory intervention regarding real estate matters under RERAN's jurisdiction.

## 3. Description

The service allows users to submit complaints by selecting the complaint category, providing detailed information about the issue, identifying the parties involved, and uploading supporting evidence. RERAN reviews the complaint, may request additional information, investigates the matter where necessary, and communicates the outcome to the complainant.

## 4. Who Can Apply

* Property Owner  
* Property Buyer  
* Property Seller  
* Tenant  
* Landlord  
* Diaspora Investor  
* Authorized Representative  
* Any Registered Individual User with a complaint relating to RERAN-regulated services

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* The complaint relates to a matter within RERAN's regulatory jurisdiction.  
* Supporting evidence is available where applicable.

## 6. Required Information

### Complainant Information

* Full Name  
* Contact Number  
* Email Address

### Complaint Information

* Complaint Category  
* Subject  
* Description of Complaint  
* Date of Incident  
* Location  
* Parties Involved  
* Property Information (where applicable)  
* Application or Transaction Reference Number (where applicable)  
* Requested Resolution  
* Additional Remarks (Optional)

## 7. Required Documents

Depending on the complaint:

* Supporting Evidence  
* Sale Agreement  
* Lease Agreement  
* Property Documents  
* Communication Records  
* Photographs  
* Payment Receipts  
* Government-issued Identification (where required)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the complaint is submitted.

## 10. Processing Authority

**RERAN**

The complaint is reviewed and investigated by the appropriate RERAN department based on the complaint category.

## 11. Expected Processing Time

Subject to RERAN's complaint resolution service standards.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Submit Complaint"  
↓  
Select Complaint Category  
↓  
Enter Complaint Details  
↓  
Upload Supporting Documents  
↓  
Review Application  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Complaint  
↓  
Application Validation  
↓  
Complaint Assigned  
↓  
RERAN Review  
↓  
Investigation  
↓  
Additional Information Requested (if required)  
↓  
Final Decision  
↓  
Complaint Closed  
↓  
Receive Complaint Resolution

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Complaint Assigned  
↓  
Under Review  
↓  
Investigation  
↓  
Information Requested  
↓  
Resubmitted  
↓  
Resolved  
↓  
Closed

### Additional Statuses

* Returned  
* Rejected  
* Withdrawn  
* Cancelled

## 14. Possible Outcomes

* Complaint Successfully Resolved  
* Complaint Partially Resolved  
* Complaint Dismissed  
* Additional Information Requested  
* Complaint Returned  
* Complaint Rejected  
* Payment Failed  
* Complaint Withdrawn

## 15. Output

Upon completion, the system generates:

* Complaint Reference Number  
* Complaint Resolution Report  
* Official Decision Letter  
* Investigation Summary (where applicable)  
* Payment Receipt

## 16. Related Services

* Service \#39 – Track Complaint  
* Feature \#1 – Submit Application  
* Feature \#3 – Respond to Information Request  
* Service \#3 – Verify Property  
* Service \#26 – Submit Tenancy Dispute

## 17. UI Screens

* Services  
* Submit Complaint  
* Complaint Category  
* Complaint Details  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Complaint Submitted  
* Complaint Details  
* Complaint Resolution

## 18. API Requirements

* Retrieve Complaint Categories  
* Upload Supporting Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Complaint  
* Assign Complaint  
* Retrieve Complaint Status  
* Update Complaint  
* Generate Resolution Report  
* Download Decision Letter

## 19. Database Entities

* User  
* Complaint  
* Complaint Category  
* Property  
* Application  
* Service Request  
* Document  
* Evidence  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User can submit a complaint related to a RERAN-regulated matter.  
* Complaint information is validated before submission.  
* Supporting documents are uploaded successfully.  
* Payment is completed before submission.  
* Complaint receives a unique reference number.  
* Complaint is assigned to the appropriate RERAN department.  
* User can monitor the complaint status.  
* RERAN may request additional information during the investigation.  
* Complaint resolution is communicated to the complainant.  
* Payment receipt is generated after successful payment.  
* All complaint activities are recorded in the audit log.

## 21. Business Rules

1. Only registered Individual Users may submit complaints through the platform.  
2. The complaint must relate to a matter regulated by RERAN.  
3. Payment must be completed before the complaint is submitted.  
4. Each complaint receives a unique complaint reference number.  
5. RERAN may request additional information from the complainant during the investigation.  
6. Complaints are assigned to the appropriate department based on the complaint category.  
7. Supporting evidence submitted becomes part of the official complaint record.  
8. Only authorized users may access complaint details and investigation outcomes.  
9. All complaint submissions, investigations, communications, decisions, and supporting documents must be permanently recorded in the audit trail.
