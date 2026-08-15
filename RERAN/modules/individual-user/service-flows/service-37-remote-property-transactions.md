---
project: RERAN
module: individual-user
type: service-flow
status: current
source_type: extrapolated
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - individual-user
  - service-flow
  - diaspora
---

# Service #37 – Remote Property Transactions

**Service Category:** Diaspora Services

## 1. Service Overview

The **Remote Property Transactions** service enables eligible users to complete property-related transactions through the RERAN platform without being physically present in Nigeria. The service supports secure digital processing of property transactions, allowing verified users to submit applications, upload documents, complete payments, and receive regulatory approvals remotely.

## 2. Purpose

Enable eligible users to securely complete property-related transactions remotely while ensuring compliance with RERAN regulations.

## 3. Description

The service allows users who have successfully completed identity verification to initiate and manage eligible property transactions through the RERAN platform. **This is a routing service, not an independent transaction type** — corrected 2026-08-15. Once identity verification is confirmed, the user selects which underlying transaction they actually want (#4–#35, wherever the transaction is eligible to be conducted remotely), and that transaction's own fields, documents, fee status, and payment timing apply exactly as they would for a user physically present in Nigeria. #37 doesn't have its own fee schedule or payment rule; it inherits the selected transaction's.

## 4. Who Can Apply

* Diaspora Investor  
* Nigerian Citizen Living Abroad  
* Property Owner Living Abroad  
* Property Buyer Living Abroad  
* Authorized Representative acting on behalf of a verified user

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Remote Identity Verification (#36) has been successfully completed.  
* User is eligible for the selected property transaction.  
* Required supporting documents are available.

## 6. Required Information

### Applicant Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information  
* Country of Residence

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Transaction Information

* Transaction Type  
* Additional Remarks (Optional)

**The fields above cover only the routing step** (applicant, property, which transaction type). Once a transaction type is selected, that transaction's own Required Information section applies in full — this section does not duplicate all 41 possible field sets. *(Corrected 2026-08-15 — "Property Owner Information" and "Purchaser Information" removed from this section; those belong to the selected transaction's own field set, e.g. #6's counterparty fields, not to this routing step.)*

## 7. Required Documents

* Verified Identity Documents (required for every use of this service, regardless of which transaction is selected — confirms #36 was completed)
* **Plus the selected transaction's own Required Documents list in full** — this section previously listed several transaction-type-specific documents (Sale Agreement, Lease Agreement, Power of Attorney) directly here; those belong to the selected transaction's own file, not duplicated in this routing service's list.

## 8. Service Fee

**Determined entirely by the selected transaction — #37 itself has no independent fee.** Corrected 2026-08-15: this section previously said "applicable according to the RERAN fee schedule for the selected transaction," which was directionally right but not reflected anywhere else in this file. See `payments.md` for the full per-service fee and timing table; #37 must show whichever entry applies to the transaction actually selected, including the five confirmed no-fee services (#17, #18, #33, #7's Owner/Entity-Amendment path) and #40/#42's unspecified status, wherever those happen to be conductable remotely.

## 9. Payment Required

**Depends entirely on the selected transaction — not a fixed "yes."**

Corrected 2026-08-15 — this section previously stated flatly that "payment must be completed before the transaction application is submitted," with no conditional language at all. That directly contradicted this file's own Business Rule 4 ("Each transaction is processed according to the business rules governing the selected service"), which already implied variable rules per transaction — Section 9 and Business Rule 4 disagreed with each other within the same file. Section 9 is now brought into line with Rule 4's own acknowledgment:

* If the selected transaction is upfront-paying (most of #4–#35), payment happens before submission, same as it would in person.
* If the selected transaction pays after some or all of RERAN's decision (#28, and the counter-channel path of #9–#16/#23/#24/#26, where remotely conductable), the wizard shows no payment step at all here either — the user sees "Pay Now" on Application Details once the same status they'd see in person is reached.
* If the selected transaction carries no fee (#17, #18, #33, #7's Owner/Entity-Amendment path), no payment step appears anywhere in this flow.

## 10. Processing Authority

**RERAN**

The application is processed by the appropriate RERAN department based on the selected transaction — the same department that would process it for a user physically present in Nigeria.

## 11. Expected Processing Time

Depends on the selected transaction and RERAN's regulatory service standards — the same processing time the selected transaction's own file states, not a #37-specific figure.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Remote Property Transactions"  
↓  
Complete Identity Verification Check (confirms #36 was completed)  
↓  
Select Transaction Type  
↓  
**[Wizard re-opens at the selected transaction's own field pattern and payment rule — see that service's own Processing Workflow section]**  
↓  
Download Transaction Documents

*(Corrected 2026-08-15 — this previously continued with a single fixed "Select Property → Enter Transaction Information → Upload Supporting Documents → Review Application → Review Service Fee → Complete Payment → Submit Application" sequence applied uniformly regardless of which transaction was selected. That's inconsistent with treating "Select Transaction Type" as a genuine branch point: a user conducting #17 (Grant Registration, no fee) should never see a "Review Service Fee" step, and one conducting #28 (Request Rental Valuation) should see payment appear only after RERAN's approval, not here at all. The fixed downstream sequence has been replaced with an explicit hand-off to the selected transaction's own pattern.)*

## 13. Application Status Flow

Draft  
↓  
Identity Verification Pending  
↓  
**[Status flow from this point follows the selected transaction's own Application Status Flow exactly — see that service's own Section 13]**

### Statuses Specific to This Routing Step

* Identity Verification Failed
* Identity Verification Confirmed

*(Corrected 2026-08-15 — this previously listed one fixed status sequence, including "Payment Pending → Payment Successful" unconditionally positioned right after Identity Verification Pending, which assumes every selected transaction pays upfront. It doesn't: see Section 9 above, and this file's own Business Rule 4. Only the two identity-verification-specific statuses genuinely belong to #37 itself; everything after Identity Verification Confirmed belongs to whichever transaction was selected.)*

## 14. Possible Outcomes

* Identity Verification Confirmed
* Identity Verification Failed
* **Whatever outcome the selected transaction itself defines** — see that service's own Possible Outcomes section.

## 15. Output

* Identity verification confirmation (from this routing step)
* **The selected transaction's own Output** — see that service's own Output section. #37 does not generate its own separate output document beyond what the underlying transaction produces.

## 16. Related Services

* Service \#36 – Remote Identity Verification  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale  
* Service \#23 – Register Lease  
* Service \#29 – Register Power of Attorney

## 17. UI Screens

* Services  
* Remote Property Transactions  
* Transaction Type Selection  
* *(from here, the selected transaction's own UI screens — see that service's own file)*

## 18. API Requirements

* Validate Identity Verification Status  
* Retrieve Available Transaction Types  
* *(plus whichever API calls the selected transaction itself requires — see that service's own file)*

## 19. Database Entities

* User  
* Identity Verification  
* Audit Log  
* Notification  
* *(plus whichever entities the selected transaction itself requires)*

## 20. Acceptance Criteria

* User has a verified identity (#36) before initiating a remote transaction.  
* User can select an eligible property transaction.  
* Once identity is confirmed, the selected transaction's own acceptance criteria apply in full — including its own fee, payment timing, and required-field rules. *(Corrected 2026-08-15 — this previously said "payment is completed before submission" as a standalone, unconditional criterion, contradicting Business Rule 4 in the same file. Now folded into "the selected transaction's own... rules apply.")*
* Application receives a unique reference number.  
* User can monitor the application throughout the review process.  
* Approved applications complete the requested transaction.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only users with a successfully verified identity may access remote property transaction services.  
2. The requested transaction must comply with all applicable RERAN regulations.  
3. **Once identity is verified, the selected transaction's own business rules govern the transaction in full — including its own fee status and payment timing.** #37 imposes no independent payment rule of its own. *(Corrected 2026-08-15 — this previously said flatly "payment must be completed before the application is submitted," directly contradicting the very next rule, which already said transactions follow their own selected-service rules. That contradiction is why this file needed correcting.)*
4. Each transaction is processed according to the business rules governing the selected service.  
5. Supporting documents must be submitted and validated before review.  
6. Additional information may be requested during the review process.  
7. Approved transactions update the relevant property records where applicable.  
8. Every remote transaction is assigned a unique transaction reference number.  
9. All applications, approvals, payments, document submissions, and completed transactions must be permanently recorded in the audit trail.
