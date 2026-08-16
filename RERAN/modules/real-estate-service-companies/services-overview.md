---
project: RERAN
module: real-estate-service-companies
type: overview
status: draft
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-service-companies/roles-and-responsibilities.md"
  - "RERAN/modules/real-estate-service-companies/shared-platform-features.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
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
* Service #18 – Register Real Estate Evaluation Details Certificate *(confirmed in Group D 2026-08-16 — see below; own screen not yet designed)*
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
| 18 | 65 | Real Estate Licensing *(confirmed 2026-08-16 — see below)* |
| 19 | 66 | Real Estate Licensing |
| 20 | 67 | Real Estate Rental |
| 21 | 68 | Real Estate Rental |
| 22 | 69 | Real Estate Rental |
| 23 | 70 | Real Estate Transaction |
| 24 | 71 | Real Estate Transaction |
| 25 | 57 | Real Estate Dispute |
| 26 | 58 | Real Estate Dispute |

**Row 65 provenance — resolved 2026-08-16 (client decision, `open-questions.md` A2).** This row's own workflow text ("sign up and login via evaluation company option... make real estate evaluation") still reads as a Valuer-facing service (Group G — Allied Professionals & Service Trustees), not a Brokerage service in its actual mechanics. **Ownership is now settled, not the underlying structural oddity**: the client has confirmed this stays in Group D, on the source table's own group assignment, rather than moving to an undocumented Group G module. The module's total remains 26; Real Estate Licensing Services remains 8.

**What changed as a result:** the Phase 4 UI package excluded Service #18 entirely (`navigation.md`, `ui/screens/services-catalog.md`, `ui/screens/dashboard.md` all carried explicit exclusion notes pending this decision). Those exclusions are being corrected in a follow-up pass; Service #18 itself still has no designed screen, since its own atypical workflow (the evaluation company decides, not RERA) doesn't fit the shared Submit Application wizard every other service uses — see `service-flows/service-18-register-evaluation-details-certificate.md`'s own Open Questions for what's still genuinely unresolved now that ownership is settled.

**Row 60 (Real Estate Permit Application) may bundle multiple permit sub-types.** Its channel column lists "Electronic, classified, billboard, and SMS advertisement permits" as distinct permit types under one row. Resolved provisionally in `open-questions.md` A4 as one service with a Permit Type field, and built that way in `ui/screens/submit-application.md` — Pattern A, not split into multiple services. Flagged as Medium confidence, reversible if wrong.

## Shared Platform Features

**Populated as of Phase 5, corrected 2026-08-16 for two client decisions.** Derived bottom-up from the module's 12 built UI screens, not proposed by analogy to another module — see [shared-platform-features.md](shared-platform-features.md) for the full derivation and reasoning.

**8 features**, fewer than Financial & Trust Institutions' 12 or Real Estate Developer's 13:

| Category | Features |
| :---- | :---- |
| Application Lifecycle | Service Requests, Applications |
| Company-Specific | Jointly Owned Property Register |
| General Platform | Dashboard, Documents, Notifications, Company Profile, Help & Support |

The lower count is a direct consequence of what Group D's own source material does and doesn't contain — no internal certification gate, no Trustee-mediated escrow mechanism, no sourced recurring compliance-reporting obligation — not an indication the module is smaller or simpler than it is (26 services is comparable in scale to Financial & Trust Institutions' 18).

**Payment timing for Services #12–15 (Real Estate Licensing Application, Permit, Issue Card, Renew Card) is normalized to pay-before-lodging, per `open-questions.md` B4 (client decision, 2026-08-16).** These four services now pay upfront, via the shared platform gateway, before RERA reviews the application — the same pattern used by most fee-bearing services across the project. See `payments.md` for the full model breakdown.

## The Difference

### Business Services

Business Services represent the regulatory services RERAN provides to Group D companies. Each has its own business process, eligibility requirements, required documents, service fees, approval workflow, and regulatory outcome.

**Examples:**

* Service #4 – Register Owners Association
* Service #12 – Real Estate Licensing Application
* Service #25 – Primary Suit (Joint Property)

### Shared Platform Features

Shared Platform Features are reusable platform capabilities that support one or more Business Services. They do not represent standalone regulatory services but provide common functionality across the platform. See [shared-platform-features.md](shared-platform-features.md) for the full list.
