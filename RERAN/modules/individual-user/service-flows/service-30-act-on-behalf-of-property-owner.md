---
project: RERAN
module: individual-user
type: service-flow
status: current
source_type: extrapolated
updated: 2026-08-09
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - individual-user
  - service-flow
  - power-of-attorney
---

# Service #30 – Act on Behalf of Property Owner

**Service Category:** Power of Attorney Services

## 1. Service Overview

The **Act on Behalf of Property Owner** service enables an individual with a registered and valid Power of Attorney to perform authorized property-related transactions on behalf of a property owner through the RERAN platform. The service verifies the authority granted under the registered Power of Attorney before allowing the representative to access and perform eligible services.

## 2. Purpose

Enable an authorized representative to carry out approved property-related services on behalf of a property owner within the scope of a registered Power of Attorney.

## 3. Description

The service allows an authorized representative to select a registered property owner they represent and perform eligible property-related transactions within the permissions granted by the registered Power of Attorney. Before any transaction is initiated, the system validates the authorization, confirms that the Power of Attorney is active, and verifies that the requested service falls within the approved scope of authority.

## 4. Who Can Apply

* Registered Attorney under an approved Power of Attorney  
* Legally Authorized Representative with an active RERAN-registered Power of Attorney

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* A valid and active Power of Attorney has been registered with RERAN.  
* The representative has been granted authority to perform the requested service.  
* The Power of Attorney has not expired, been revoked, or suspended.

## 6. Required Information

### Property Owner Information

* Property Owner Name  
* Power of Attorney Reference Number

### Representative Information

* Representative Name  
* National Identification Number (NIN)

### Property Information

* Property Registration Number  
* Property Address

### Service Information

* Requested Service  
* Purpose of Request  
* Additional Remarks (Optional)

## 7. Required Documents

Depending on the requested service:

* Registered Power of Attorney  
* Government-issued Identification  
* Supporting Legal Documents  
* Other supporting documents required for the selected service

## 8. Service Fee

Applicable according to the RERAN fee schedule for the selected service.

## 9. Payment Required

**Yes**

Payment must be completed before the requested service is submitted, where applicable.

## 10. Processing Authority

**RERAN**

The requested service is processed by the appropriate RERAN department according to the applicable business process.

## 11. Expected Processing Time

Depends on the selected service and RERAN's regulatory service standards.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Act on Behalf of Property Owner"  
↓  
Select Registered Property Owner  
↓  
System Validates Power of Attorney  
↓  
Select Property  
↓  
Select Authorized Service  
↓  
Enter Required Information  
↓  
Upload Supporting Documents (if required)  
↓  
Review Application  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Application  
↓  
Application Validation  
↓  
RERAN Review  
↓  
Application Approved  
↓  
Requested Service Completed  
↓  
Download Confirmation

## 13. Application Status Flow

Draft  
↓  
Authorization Validation  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Validation  
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

* Authorization Failed  
* Returned  
* Rejected  
* Withdrawn  
* Cancelled

## 14. Possible Outcomes

* Service Successfully Completed  
* Authorization Validated  
* Authorization Rejected  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Service Confirmation  
* Updated Property Record (where applicable)  
* Application Reference Number  
* Transaction Receipt  
* Payment Receipt

## 16. Related Services

* Service \#29 – Register Power of Attorney  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale  
* Service \#23 – Register Lease  
* Service \#24 – Renew Lease  
* Service \#25 – Manage Lease

## 17. UI Screens

* Services  
* Act on Behalf of Property Owner  
* Select Property Owner  
* Authorization Validation  
* Select Property  
* Select Service  
* Service Details  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Service Confirmation

## 18. API Requirements

* Retrieve Registered Powers of Attorney  
* Validate Power of Attorney  
* Retrieve Authorized Properties  
* Retrieve Available Services  
* Validate Service Permission  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Service Application  
* Retrieve Application Status  
* Generate Service Confirmation

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Power of Attorney  
* Authorized Representative  
* Service Request  
* Application  
* Document  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* System validates the representative's authorization before allowing access.  
* Representative can only access properties covered by the registered Power of Attorney.  
* Representative can perform only services permitted by the registered authorization.  
* Required information is validated before submission.  
* Supporting documents are uploaded successfully.  
* Payment is completed where applicable.  
* Application receives a unique reference number.  
* User can monitor the application status.  
* Approved requests complete the selected service.  
* Payment receipt is generated after successful payment.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only representatives with an active, approved Power of Attorney may act on behalf of a property owner.  
2. The requested service must fall within the scope of authority granted by the registered Power of Attorney.  
3. The system must validate the authorization before allowing any transaction.  
4. Representatives cannot perform services outside the approved scope of authority.  
5. Expired, revoked, or suspended Powers of Attorney cannot be used to access services.  
6. Payment must be completed before submission where the selected service requires payment.  
7. Every transaction performed by a representative must be linked to both the property owner and the authorized representative.  
8. All activities performed under a Power of Attorney must be permanently recorded in the audit trail, including the representative's identity, the property owner, the service performed, and the date and time of the transaction.  
9. Any service completed by an authorized representative has the same legal effect as if it were performed directly by the property owner, provided it is within the registered scope of authority.
