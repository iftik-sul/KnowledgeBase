---
project: RERAN
module: real-estate-service-companies
type: overview
status: draft
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-service-companies/roles-and-responsibilities.md"
tags:
  - real-estate-service-companies
  - services-overview
---

# Real Estate Service Companies Services Overview

> **Unified access, from the start.** No service listed below is restricted to a particular role. Any of the company's four Group D roles — Brokerage Principal, Owners'-Association Manager, Property Management Officer, Company Dispute Filing Officer — may act on any of the 26 services, with role recorded as audit-trail attribution only. See [roles-and-responsibilities.md](roles-and-responsibilities.md).

## Business Services

### 1. Jointly Owned Property Services

These services support the administration of jointly-owned (strata / JOP) properties: registering the managing company and the owners' association, managing the property's escrow account, and appointing auditors.

* Service #1 – Register Company for JOP Administrative Supervision
* Service #2 – Approve Service Fees & Utilization Fees
* Service #3 – Register JOP-Competent Employees
* Service #4 – Register Owners Association
* Service #5 – Transfer JOP Escrow Account
* Service #6 – Request No-Objection Letter to Close Escrow Account
* Service #7 – Accredit Escrow Account Signatories
* Service #8 – Appoint Financial Auditor
* Service #9 – Appoint Audit Office for JOP Financial Accounts
* Service #10 – Appoint Audit Office for JOP Budget Audit
* Service #11 – Approval / Renewal of Financial Auditing Company

### 2. Real Estate Licensing Services

These services cover the firm's own licence, permits, professional practice cards for agents, and training-entity accreditation.

* Service #12 – Real Estate Licensing Application
* Service #13 – Real Estate Permit Application
* Service #14 – Issue Professional Practice Card
* Service #15 – Renew Professional Practice Card
* Service #16 – Cancel Professional Practice Card
* Service #17 – Amend Professional Practice Card
* Service #18 – Register Real Estate Evaluation Details Certificate
* Service #19 – Accreditation of Training Entities

### 3. Real Estate Rental Services

These services support registration and renewal of the firm's property management contracts and its tenancy-system users.

* Service #20 – Register/Renew Management Contract
* Service #21 – Cancel Management Contract
* Service #22 – Register Tenancy System User

### 4. Real Estate Transaction Services

These services cover public-auction sales conducted by the firm.

* Service #23 – Permit to Sell by Public Auction
* Service #24 – Register Property Sold by Auction

### 5. Real Estate Dispute Services

These services cover formal dispute proceedings the firm files on behalf of managed or jointly-owned properties.

* Service #25 – Primary Suit (Joint Property)
* Service #26 – Execution Case (Joint Ownership)

## Business Services Summary

| Category | Number of Services |
| :---- | :---: |
| Jointly Owned Property Services | 11 |
| Real Estate Licensing Services | 8 |
| Real Estate Rental Services | 3 |
| Real Estate Transaction Services | 2 |
| Real Estate Dispute Services | 2 |
| **Total Business Services** | **26** |

## Service Provenance

Every service file's frontmatter will carry a `source_type` field, per the house convention established in Individual User and carried through Financial & Trust Institutions:

| Value | Meaning | Count |
| :---- | :---- | :---: |
| `sourced` | Traces to an explicit row in `RERAN_service_flows_v2.md`'s master Service Workflows table | 26 |
| `extrapolated` | Derived from role descriptions rather than an explicit row | 0 |

**Group D is the cleanest reconciliation of any module documented so far: 26 source rows (46–71, minus none) map 1:1 to 26 documented services, with no consolidation and no split.** Contrast Individual User (41 rows → 43 files, ten rows consolidated into one service, one row split into two) and Financial & Trust Institutions (41 rows including two transposed against file order). No such adjustment is needed here — see the row-to-service mapping below.

### Row-to-Service Mapping

| Service # | Source Row | Category |
| :---: | :---: | :---- |
| 1 | 46 | Jointly Owned Property |
| 2 | 47 | Jointly Owned Property |
| 3 | 48 | Jointly Owned Property |
| 4 | 49 | Jointly Owned Property |
| 5 | 50 | Jointly Owned Property |
| 6 | 51 | Jointly Owned Property |
| 7 | 52 | Jointly Owned Property |
| 8 | 53 | Jointly Owned Property |
| 9 | 54 | Jointly Owned Property |
| 10 | 55 | Jointly Owned Property |
| 11 | 56 | Jointly Owned Property |
| 12 | 59 | Real Estate Licensing |
| 13 | 60 | Real Estate Licensing |
| 14 | 61 | Real Estate Licensing |
| 15 | 62 | Real Estate Licensing |
| 16 | 63 | Real Estate Licensing |
| 17 | 64 | Real Estate Licensing |
| 18 | 65 | Real Estate Licensing *(provenance flagged — see below)* |
| 19 | 66 | Real Estate Licensing |
| 20 | 67 | Real Estate Rental |
| 21 | 68 | Real Estate Rental |
| 22 | 69 | Real Estate Rental |
| 23 | 70 | Real Estate Transaction |
| 24 | 71 | Real Estate Transaction |
| 25 | 57 | Real Estate Dispute |
| 26 | 58 | Real Estate Dispute |

**Row 65 provenance flag, carried from `roles-and-responsibilities.md`.** This row's own workflow text ("sign up and login via evaluation company option... make real estate evaluation") reads as a Valuer-facing service (Group G — Allied Professionals & Service Trustees), not a Brokerage service. It is provisionally kept in Group D's catalogue, matching the source table's own group assignment (D), but flagged for confirmation in `open-questions.md` before treating that assignment as settled. If reassigned to Group G, this module's total would drop to 25 and Real Estate Licensing Services to 7 — noted here so the count is traceable either way.

**Row 60 (Real Estate Permit Application) may bundle multiple permit sub-types.** Its channel column lists "Electronic, classified, billboard, and SMS advertisement permits" as distinct permit types under one row. Whether this should split into separate services the way Individual User's lease-registration row split into two, or stay as one service with a permit-type field, is checked in `open-questions.md` rather than assumed here.

## Shared Platform Features

**Deliberately not populated yet.** Per the module build playbook (`RERAN/module-build-playbook.md`, Phase 5), the shared-features layer is derived bottom-up from the actual built UI screens, not proposed by analogy to another module's feature list. Both Group B's original 17-feature guess and Group C's proposed feature set had to be substantially corrected once checked against real screens. This section is filled in after Phase 4 (UI Screens), not before.

## The Difference

### Business Services

Business Services represent the regulatory services RERAN provides to Group D companies. Each has its own business process, eligibility requirements, required documents, service fees, approval workflow, and regulatory outcome.

**Examples:**

* Service #4 – Register Owners Association
* Service #12 – Real Estate Licensing Application
* Service #25 – Primary Suit (Joint Property)

### Shared Platform Features

Shared Platform Features are reusable platform capabilities that support one or more Business Services. They do not represent standalone regulatory services but provide common functionality across the platform. Populated in Phase 5, once the UI screens they're derived from exist.
