---
project: RERAN
module: individual-user
type: service-flow
status: current
updated: 2026-08-15
source_type: sourced
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - individual-user
  - service-flow
  - property-ownership-transaction
---

# Service #41 – Register Company

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Register Company** service allows a Property Owner to register a company with RERAN in connection with their property holdings or transactions. The source material groups this alongside other Real Estate Transaction Services for Individual Users, distinct from Group D's brokerage/service-company licensing services.

## 2. Purpose

Enable an individual to register a company with RERAN as part of managing property transactions — for example, holding or transacting property through a corporate entity rather than as a natural person.

## 3. Description

The applicant visits a Real Estate Registration Trustee Centre, submits the required documents, and RERA staff enter and audit the transaction in-system. After payment, the applicant receives an email confirming successful registration along with the company's reference number and a digital payment receipt, issued by the Trustee Centre.

**Open question:** the source does not explain the relationship between this service and a company's general corporate registration (with whatever body handles that in Nigeria) — whether this is RERA registering a company from scratch, or recording an already-incorporated company's details for property-transaction purposes. Documented as-is from the source; needs client clarification before implementation.

## 4. Who Can Apply

* Property Owner / Seller

## 5. Prerequisites

* Registered RERAN Individual User account.
* Required supporting documents for the company (not itemized in source).

## 6. Required Information

Not itemized field-by-field in the source material. The workflow implies at minimum company name and ownership/representative details, but this is inferred from the general shape of the process, not stated explicitly.

## 7. Required Documents

Not specified in the source material beyond "submit docs."

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**25–30 minutes**

## 12. Processing Workflow

Visit Real Estate Registration Trustee Centre
↓
Submit Documents
↓
RERA Staff Enter Transaction Data
↓
RERA Staff Audit
↓
Pay Fees
↓
Receive Email with Company Reference Number and Digital Payment Receipt

**Note:** the source specifies this as a Trustee Centre (in-person) service only — no online/self-service channel is described, unlike most other services in this category. Payment is taken and receipted at the Trustee Centre counter itself, not through any financial-institution channel — this remains a RERAN service point throughout, matching every other Trustee-Centre service in this module.

## 13. Application Status Flow

Submitted
↓
Under Review
↓
Approved
↓
Registered

### Additional Statuses

* Rejected (implied by the audit step)

## 14. Possible Outcomes

* Company successfully registered, reference number issued
* Application rejected

## 15. Output

* Email confirming registration, including the company's reference number
* Payment Receipt (digital, issued by the Trustee Centre)

**Confirmed 2026-08-15.** This section previously flagged the missing Payment Receipt as a genuine ambiguity rather than asserting it, since the source's own description was terse ("receives an email confirming successful registration") and #41 lacked the close sibling comparables that made #43's equivalent gap a clear fix. Confirmed directly: the Trustee Centre counter issues the digital receipt as part of that same email — the applicant never leaves without one, matching the standard shared payment-gateway/receipt pattern used across the rest of the module (`payments.md`'s Payment Artefacts section). No separate Fee Balance or other payment artefact exists here, consistent with `open-questions.md` C2.

## 16. Related Services

* Service #4 – Register Property Ownership
* Service #6 – Register Property Sale

## 17. UI Screens

**Corrected 2026-08-15** — this previously said "Not yet designed — this module has no UI documentation yet," which predates the module's UI package (added and merged the same day this correction was made). This service is documented under Pattern B in [submit-application.md](../ui/screens-unified/submit-application.md), which correctly notes its fields are documented for reference but that #41 "has no online submission path at all" — matching Section 12's own note above that this is a Trustee-Centre-only service. No in-app wizard flow was built for it beyond the field documentation, consistent with there being no online channel to build a wizard for.

## 18. API Requirements

Not specified in the source material.

## 19. Database Entities

* Property Owner
* Company
* Company Registration
* Payment
* Payment Transaction

## 20. Acceptance Criteria

* Applicant can submit a company registration request at a Trustee Centre.
* RERA staff can enter, audit, and approve or reject the submission.
* Approved registrations generate a unique company reference number delivered by email.
* A digital payment receipt is issued by the Trustee Centre alongside the registration confirmation. *(Confirmed 2026-08-15 — see Section 15.)*

## 21. Business Rules

1. This service is documented in the source as Trustee-Centre-only; no in-app self-service path is described. **Flagged**, not resolved — whether an online path should be added is a scope decision.
2. The relationship between this RERA company registration and any broader corporate/business registration process is unclear from the source and needs client clarification.
3. Payment is taken and receipted at the Trustee Centre, not by any financial institution — the applicant receives a digital Payment Receipt from the RERAN counter itself. *(Confirmed 2026-08-15 — see Section 3/15.)*
