---
project: RERAN
module: individual-user
type: service-flow
status: current
updated: 2026-08-10
source_type: sourced
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - individual-user
  - service-flow
  - power-of-attorney
---

# Service #42 – Cancel Power of Attorney

**Service Category:** Power of Attorney Services

## 1. Service Overview

The **Cancel Power of Attorney** service allows a Property Owner to cancel and notarize the cancellation of a previously registered Power of Attorney (see Service #29 – Register Power of Attorney). This is the counterpart cancellation service to registration; without it, a registered PoA has no documented way to be revoked through the platform.

## 2. Purpose

Enable a property owner to formally revoke a Power of Attorney they previously granted, with the cancellation notarized and recorded by RERA.

## 3. Description

**This service has the thinnest source specification of any service in this module.** The master service table describes only: the applicant moves to the Customer Centre at the Land Department, submits required documents to an employee, and the employee enters, audits, and approves the request — and then the source's own workflow description ends with the note **"(Not fully specified in document)."** That gap is in the client's own source material, not something omitted during documentation.

Everything below that is standard, unspecified, or genuinely unknown is marked as such rather than invented.

## 4. Who Can Apply

* Property Owner / Seller (the original grantor of the Power of Attorney)

## 5. Prerequisites

* An existing, registered Power of Attorney to cancel (see Service #29).
* Registered RERAN Individual User account.

## 6. Required Information

Not specified in the source material.

## 7. Required Documents

"Required documents" are referenced generically in the source but not itemized. Given the parallel with Service #29 (Register Power of Attorney), a notarized cancellation instrument and the original PoA reference are plausible requirements — but this is inference, not a sourced requirement, and should be confirmed with the client before being treated as final.

## 8. Service Fee

Not specified in the source material.

## 9. Payment Required

Not specified in the source material — the workflow described has no payment step, unlike most other services in this module.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**20 minutes**

## 12. Processing Workflow

Visit Customer Centre at Land Department
↓
Submit Required Documents to Employee
↓
Employee Enters, Audits, and Approves
↓
*(source ends here — "Not fully specified in document")*

## 13. Application Status Flow

Not specified in the source material.

## 14. Possible Outcomes

Not specified in the source material.

## 15. Output

Not specified in the source material. Given the service name ("cancellation **notarization**"), a notarized cancellation certificate or letter is a plausible output, matching the pattern of Service #29's registration certificate — but this is not confirmed by source and is flagged rather than assumed.

## 16. Related Services

* Service #29 – Register Power of Attorney
* Service #30 – Act on Behalf of Property Owner

## 17. UI Screens

Not yet designed — this module has no UI documentation yet.

## 18. API Requirements

Not specified in the source material.

## 19. Database Entities

* Property Owner
* Power of Attorney
* PoA Cancellation Record

## 20. Acceptance Criteria

Not specified in the source material — cannot be derived without inventing process detail the source doesn't provide.

## 21. Business Rules

1. **This service's business rules are not specified in the source material beyond the three steps above.** Rather than fill this gap with plausible-sounding rules (which the project's own AI Guidelines caution against), it is recorded here as an open item: the output document, fee, payment step, status flow, and completion criteria for PoA cancellation all need client input before this service can be implemented.
