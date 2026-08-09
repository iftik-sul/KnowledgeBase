---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - financial-trust-institutions
  - services-overview
---

# Financial & Trust Institutions — Services Overview

18 business services, verified against the master service table (rows 28–45). This total reconciles with the source workbook's own summary: Development 2 + Transaction 15 + Title-Deed Data 1 = 18.

All 18 are approved by the **Compliance & Escrow Auditor**, a Group A role. No Group C service is self-approving.

## Business Services

### 1. Institutional Approval Services (2)

Approval and cancellation of the institution's standing as an approved trustee or auditor.

* Service #1 — Approval / renewal of Account Trustee & Auditing company
* Service #2 — Cancellation of Account Trustee & Auditing company

### 2. Mortgage Services (5)

The core lending lifecycle against registered titles.

* Service #3 — Mortgage registration
* Service #4 — Mortgage amendment
* Service #5 — Mortgage transfer
* Service #6 — Mortgage release
* Service #7 — Grant property mortgage

### 3. Finance Lease Services (4)

The finance lease lifecycle, mirroring the mortgage services.

* Service #8 — Finance lease registration
* Service #9 — Finance lease amendment
* Service #10 — Finance lease transfer
* Service #11 — Finance lease release

### 4. Title & Ownership Transaction Services (6)

Title-deed transactions executed through the institution rather than by the owner directly.

* Service #12 — Registration of real estate fund companies in the register of privileges
* Service #13 — Sale procedure (heirs)
* Service #14 — Company shares sale
* Service #15 — Updating title deed information
* Service #16 — Split ownership
* Service #17 — Issuance of title deed

### 5. Contract Services (1)

* Service #18 — Contract cancellation

> **Proposed** — the five category names above are not in the source material. The source groups these 18 services under three internal admin categories (Development 2, Transaction 15, Title-Deed Data 1), which describe RERA's filing structure rather than what an institution user does. The regrouping is by user-facing task, matching the approach taken in the individual-user module. The underlying 18 services and their count are unchanged and fully sourced. Needs client confirmation.

## Business Services Summary

| Category | Services |
| :---- | :---: |
| Institutional Approval Services | 2 |
| Mortgage Services | 5 |
| Finance Lease Services | 4 |
| Title & Ownership Transaction Services | 6 |
| Contract Services | 1 |
| **Total Business Services** | **18** |

### Reconciliation to Source Categories

| Source category | Count | Maps to |
| :---- | :---: | :---- |
| Development | 2 | Institutional Approval Services |
| Transaction | 15 | Mortgage (5) + Finance Lease (4) + Title & Ownership (6) |
| Title-Deed Data | 1 | Contract Services |
| **Total** | **18** | |

## Service Ownership

| Role | Services |
| :---- | :---: |
| Mortgage Officer | 17 |
| Institution Relationship Manager | 1 (Service #18) |
| Account Trustee | 0 — acts within Group B escrow services |
| Auditing Bureau Officer | 0 — acts as internal certification gate |

> The source assigns Services #1 and #2 to the Account Trustee as responsible role, but both concern the institution's own approval status, which the Institution Relationship Manager is described as maintaining. This is a source inconsistency, recorded here rather than resolved. See To Confirm.

## Shared Platform Features

> **Proposed** — not in source material. Rationale: the source defines a standard six-stage pipeline (lodge → validate → audit → pay → issue → record) that every regulated service follows, and the individual-user module documents four shared application-management features serving that pipeline. Group C services run the same pipeline and therefore require the same capabilities. Needs client confirmation.

### Application Management (4)

* Feature #1 — Submit Application
* Feature #2 — Track Application Status
* Feature #3 — Respond to Information Request
* Feature #4 — Resubmit Returned Application

### Institution-Specific Features (3)

* Feature #5 — Internal Certification Queue — transactions awaiting the Auditing Bureau Officer's certification before routing to RERA
* Feature #6 — Escrow Request Queue — developer-originated requests awaiting Account Trustee action
* Feature #7 — Approval Expiry Tracking — trustee and auditor approval renewal windows

### General Platform Features (8)

* Dashboard
* Services Catalog
* Applications
* Documents
* Payments — note: Group C fees are deducted from the institution's account rather than paid per transaction by an individual
* Notifications
* Institution Profile
* Help & Support

## Platform Features Summary

| Category | Features |
| :---- | :---: |
| Application Management | 4 |
| Institution-Specific | 3 |
| General Platform | 8 |
| **Total Shared Platform Features** | **15** |

## Application Status Vocabulary

> **Proposed** — not in source material. Rationale: the source describes the audit stage as "approves, returns for correction, or rejects with reason" and references an audit queue, but never enumerates statuses for any group. Group C needs a status vocabulary for its two-gate flow. Needs client confirmation.

| Status | Meaning | Set by |
| :---- | :---- | :---- |
| Draft | Started, not submitted | Mortgage Officer |
| Pending Internal Certification | Awaiting the institution's own auditor | Mortgage Officer |
| Returned by Auditor | Sent back internally for correction | Auditing Bureau Officer |
| Submitted to RERA | In the Transaction Audit queue | Auditing Bureau Officer |
| Information Requested | RERA has raised a query | Compliance & Escrow Auditor |
| Approved | Passed audit, awaiting fee settlement | Compliance & Escrow Auditor |
| Rejected | Refused with documented reason | Compliance & Escrow Auditor |
| Completed | Fees settled, output document issued | Platform |

## Channels

Group C services run through two channels, per the source:

* **Online Mortgage System** — the institution's own portal access, used for mortgage and grant services
* **Real Estate Registration Trustee Centres** — walk-in processing, used for finance lease services and several title transactions

Several services list only the Trustee Centre channel in the source, implying no online path exists for them today. Whether the platform should add online equivalents is a scope question, not a documentation gap.

## To Confirm

1. Are the five proposed service categories acceptable, or should the source's Development / Transaction / Title-Deed Data grouping be retained?
2. Services #1 and #2 are assigned to the Account Trustee in the source but concern institution standing — should they belong to the Institution Relationship Manager?
3. Do the four Application Management features apply to Group C as they do to individual users?
4. Are the three proposed institution-specific features correct, and is anything missing?
5. Is the proposed status vocabulary acceptable, and should it be shared across all modules or defined per module?
6. Should services currently limited to Trustee Centre channels gain an online path in this platform?
7. Fee settlement: is deduction from the institution's account correct for all 18 services?
