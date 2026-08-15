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
  - power-of-attorney
---

# Service #30 – Act on Behalf of Property Owner

**Service Category:** Power of Attorney Services

## 1. Service Overview

The **Act on Behalf of Property Owner** service enables an individual with a registered and valid Power of Attorney to perform authorized property-related transactions on behalf of a property owner through the RERAN platform. The service verifies the authority granted under the registered Power of Attorney before allowing the representative to access and perform eligible services.

## 2. Purpose

Enable an authorized representative to carry out approved property-related services on behalf of a property owner within the scope of a registered Power of Attorney.

## 3. Description

The service allows an authorized representative to select a registered property owner they represent and perform eligible property-related transactions within the permissions granted by the registered Power of Attorney. Before any transaction is initiated, the system validates the authorization, confirms that the Power of Attorney is active, and verifies that the requested service falls within the approved scope of authority. **This is a routing service, not an independent transaction type** — corrected 2026-08-15. Once authorization and scope are validated, the representative performs whichever underlying service they've selected (#4–#35), and that service's own fields, documents, fee status, and payment timing apply exactly as they would for the property owner acting directly. #30 doesn't have its own fee schedule or payment rule; it inherits the selected service's.

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

**The fields above cover only the routing step** (which owner, which property, which service). Once a service is selected, its own Required Information section applies in full — this section does not duplicate all 41 possible field sets.

## 7. Required Documents

* Registered Power of Attorney (required for every use of this service, regardless of which underlying service is selected)
* Government-issued Identification
* **Plus the selected service's own Required Documents list in full** — this section previously said only "supporting legal documents... depending on the requested service," which understated how directly the underlying service's own document list applies.

## 8. Service Fee

**Determined entirely by the selected service — #30 itself has no independent fee.** Corrected 2026-08-15: this section previously said "applicable according to the RERAN fee schedule for the selected service," which was directionally right but not reflected anywhere else in this file. See `payments.md` for the full per-service fee and timing table; #30 must show whichever entry applies to the service actually selected, including the five confirmed no-fee services (#17, #18, #33, #7's Owner/Entity-Amendment path) and #40/#42's unspecified status.

## 9. Payment Required

**Depends entirely on the selected service — not a fixed "yes."**

Corrected 2026-08-15 — this section, along with Sections 12 and 13 below, previously described a single fixed sequence ("Review Service Fee → Complete Payment → Submit Application," always present) that didn't actually match this file's own Section 8 or Business Rule 6, both of which already hedged with "where applicable" / "where the selected service requires payment." The diagram and status flow are now brought into line with the qualifier the text already had:

* If the selected service is upfront-paying (most of #4–#35), payment happens before submission, same as it would for the property owner acting directly.
* If the selected service pays after some or all of RERAN's decision (#28, and the counter-channel path of #9–#16/#23/#24/#26), the wizard shows no payment step at all here either — the representative sees "Pay Now" on Application Details once the same status the property owner would see is reached.
* If the selected service carries no fee (#17, #18, #33, #7's Owner/Entity-Amendment path), no payment step appears anywhere in this flow.

## 10. Processing Authority

**RERAN**

The requested service is processed by the appropriate RERAN department according to the applicable business process — the same department that would process it if the property owner submitted it directly.

## 11. Expected Processing Time

Depends on the selected service and RERAN's regulatory service standards — the same processing time the selected service's own file states, not a #30-specific figure.

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
**[Wizard re-opens at the selected service's own field pattern and payment rule — see that service's own Processing Workflow section]**  
↓  
Download Confirmation

*(Corrected 2026-08-15 — this previously continued with a single fixed "Enter Required Information → Upload Documents → Review Application → Review Service Fee → Complete Payment → Submit Application" sequence applied uniformly regardless of which service was selected in the step above. That's inconsistent with treating "Select Authorized Service" as a genuine branch point: a representative acting on #17 (Grant Registration, no fee) should never see a "Review Service Fee" step, and one acting on #28 (Request Rental Valuation) should see payment appear only after RERAN's approval, not here at all. The fixed downstream sequence has been replaced with an explicit hand-off to the selected service's own pattern.)*

## 13. Application Status Flow

Draft  
↓  
Authorization Validation  
↓  
**[Status flow from this point follows the selected service's own Application Status Flow exactly — see that service's own Section 13]**

### Statuses Specific to This Routing Step

* Authorization Failed
* Authorization Validated

*(Corrected 2026-08-15 — this previously listed one fixed status sequence, including "Payment Pending → Payment Successful" unconditionally positioned right after Authorization Validation, which assumes every selected service pays upfront. It doesn't: see Section 9 above. Only the two authorization-specific statuses genuinely belong to #30 itself; everything after Authorization Validation belongs to whichever service was selected.)*

## 14. Possible Outcomes

* Authorization Validated
* Authorization Rejected
* **Whatever outcome the selected service itself defines** — see that service's own Possible Outcomes section.

## 15. Output

* Authorization confirmation (from this routing step)
* **The selected service's own Output** — see that service's own Output section. #30 does not generate its own separate output document beyond what the underlying service produces.

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
* *(from here, the selected service's own UI screens — see that service's own file)*

## 18. API Requirements

* Retrieve Registered Powers of Attorney  
* Validate Power of Attorney  
* Retrieve Authorized Properties  
* Retrieve Available Services  
* Validate Service Permission  
* *(plus whichever API calls the selected service itself requires — see that service's own file)*

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Power of Attorney  
* Authorized Representative  
* Service Request  
* Application  
* Audit Log  
* Notification  
* *(plus whichever entities the selected service itself requires)*

## 20. Acceptance Criteria

* System validates the representative's authorization before allowing access.  
* Representative can only access properties covered by the registered Power of Attorney.  
* Representative can perform only services permitted by the registered authorization.  
* Once authorization is validated, the selected service's own acceptance criteria apply in full — including its own fee, payment timing, and required-field rules. *(Corrected 2026-08-15 — this previously said "payment is completed where applicable" as a standalone criterion, which is now folded into "the selected service's own... rules apply" rather than stated as a separate, potentially-conflicting rule.)*
* Application receives a unique reference number.  
* User can monitor the application status.  
* Approved requests complete the selected service.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only representatives with an active, approved Power of Attorney may act on behalf of a property owner.  
2. The requested service must fall within the scope of authority granted by the registered Power of Attorney.  
3. The system must validate the authorization before allowing any transaction.  
4. Representatives cannot perform services outside the approved scope of authority.  
5. Expired, revoked, or suspended Powers of Attorney cannot be used to access services.  
6. **Once authorization is validated, the selected service's own business rules govern the transaction in full — including its own fee status and payment timing.** #30 imposes no independent payment rule of its own. *(Corrected 2026-08-15 — this previously said "payment must be completed before submission where the selected service requires payment," which still implied an upfront-only default; the selected service's own rule, whatever it is, now governs without a #30-specific default layered on top.)*
7. Every transaction performed by a representative must be linked to both the property owner and the authorized representative.  
8. All activities performed under a Power of Attorney must be permanently recorded in the audit trail, including the representative's identity, the property owner, the service performed, and the date and time of the transaction.  
9. Any service completed by an authorized representative has the same legal effect as if it were performed directly by the property owner, provided it is within the registered scope of authority.
