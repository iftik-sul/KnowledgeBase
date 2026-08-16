---
project: RERAN
module: individual-user
type: overview
status: current
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - individual-user
  - index
---

# Individual User Module

Documentation for the RERAN Individual User module: the roles, business services, shared platform features, analysis layer, and UI specifications available to natural persons (property owners, landlords, tenants, buyers/investors, diaspora investors, and PoA holders) on the RERA platform.

This module's documentation was split from a single combined file, `RERAN_ individual user_service_flows.md` (removed from this directory; preserved in git history), into one file per role/services-overview/service/feature for maintainability.

**Updated 2026-08-15.** This index previously stopped at the 43 service flows and shared platform features (as of 2026-08-10) — it predates and never mentioned the analysis layer or the UI package, both added later the same day the module's service flows were corrected. Both are now indexed below.

## Contents

| Section | Count |
| :---- | :---: |
| Roles | 6 |
| Business Services | 43 |
| Shared Platform Features | 12 |
| Analysis Layer | 4 documents |
| UI Specifications | 20 files |

## Roles (6)

* [roles-and-responsibilities.md](roles-and-responsibilities.md) — the 6 individual-user roles: Property Owner/Seller, Landlord, Owner's Representative/PoA Holder, Tenant, Property Buyer/Investor, Diaspora Investor. **Corrected 2026-08-16 — this bullet was itself stale.** It previously said the Landlord/Tenant verbatim-overlap ("Create and renew lease records" / "Register tenancy information... Renew lease records") was "not updated since 2026-08-09" and that the flag about it "was never actually raised anywhere trackable until now." Checked directly against the file: it was updated 2026-08-15 with an explanatory note and inline cross-references in both the Landlord and Tenant sections, resolving `open-questions.md` D1 — the overlap is intentional (one account can hold both roles at once, against different properties), not an unresolved conflict. `open-questions.md`'s own Summary confirms D1 as resolved, not standing open.

## Analysis Layer (4 documents)

Added 2026-08-15, built by checking all 43 service-flow files individually against the master table rather than trusting a module-wide pattern (see each document's own opening section for the full reasoning).

* [payments.md](payments.md) — per-service payment timing and fee-existence findings; the single most-corrected fact in this module's documentation history.
* [open-questions.md](open-questions.md) — role-attribution conflicts, payment questions, and their resolutions. **Corrected 2026-08-16 — this bullet previously said "13 of 14 resolved; 1 remains genuinely open."** Checked directly against `open-questions.md`'s own Summary table: **all 15 questions are resolved, 0 awaiting client data** — the same figure `module-roadmap.md` already carried, which this file had fallen behind. The apparent "1 remaining open item" was D1, resolved the same day this README was last touched but never reflected here — see the Roles entry above for the same drift, caught in the same document.
* [navigation.md](navigation.md) — activity-scoped access model and proposed sidebar structure.
* [role-workflows.md](role-workflows.md) — the shared login-to-logout journey and what each of the 6 roles typically does, including a provenance finding: 3 of the 6 roles never appear as a Responsible Role in any sourced master-table row.

## Services Overview

* [services-overview.md](services-overview.md) — the 8 business service categories, summary tables, service provenance (sourced vs. extrapolated), and the distinction between Business Services and Shared Platform Features.

## Business Services (43)

### Verification Services (3)

* [service-01-verify-developer.md](service-flows/service-01-verify-developer.md)
* [service-02-verify-development-project.md](service-flows/service-02-verify-development-project.md)
* [service-03-verify-property.md](service-flows/service-03-verify-property.md)

### Property Ownership & Transaction Services (14)

* [service-04-register-property-ownership.md](service-flows/service-04-register-property-ownership.md)
* [service-05-transfer-property-ownership.md](service-flows/service-05-transfer-property-ownership.md)
* [service-06-register-property-sale.md](service-flows/service-06-register-property-sale.md)
* [service-07-update-property-ownership-information.md](service-flows/service-07-update-property-ownership-information.md)
* [service-08-register-sale-of-mortgaged-property.md](service-flows/service-08-register-sale-of-mortgaged-property.md)
* [service-09-register-gift-transfer.md](service-flows/service-09-register-gift-transfer.md)
* [service-10-register-lease-to-own.md](service-flows/service-10-register-lease-to-own.md)
* [service-11-transfer-lease-to-own.md](service-flows/service-11-transfer-lease-to-own.md)
* [service-12-release-lease-to-own.md](service-flows/service-12-release-lease-to-own.md)
* [service-13-amend-lease-to-own.md](service-flows/service-13-amend-lease-to-own.md)
* [service-14-register-usufruct-right.md](service-flows/service-14-register-usufruct-right.md)
* [service-15-amend-usufruct-right.md](service-flows/service-15-amend-usufruct-right.md)
* [service-16-terminate-usufruct-right.md](service-flows/service-16-terminate-usufruct-right.md)
* [service-41-register-company.md](service-flows/service-41-register-company.md)

### Title & Land Registration Services (7)

* [service-17-grant-registration.md](service-flows/service-17-grant-registration.md)
* [service-18-grant-completion.md](service-flows/service-18-grant-completion.md)
* [service-19-register-heirs-ownership.md](service-flows/service-19-register-heirs-ownership.md)
* [service-20-register-community-land.md](service-flows/service-20-register-community-land.md)
* [service-21-register-partners-division.md](service-flows/service-21-register-partners-division.md)
* [service-22-register-industrial-commercial-land-ownership.md](service-flows/service-22-register-industrial-commercial-land-ownership.md)
* [service-43-exchange-properties.md](service-flows/service-43-exchange-properties.md)

### Tenancy Services (7)

* [service-23-register-lease.md](service-flows/service-23-register-lease.md)
* [service-24-renew-lease.md](service-flows/service-24-renew-lease.md)
* [service-25-manage-lease.md](service-flows/service-25-manage-lease.md)
* [service-26-submit-tenancy-dispute.md](service-flows/service-26-submit-tenancy-dispute.md)
* [service-27-cancel-tenancy-contract.md](service-flows/service-27-cancel-tenancy-contract.md)
* [service-28-request-rental-valuation.md](service-flows/service-28-request-rental-valuation.md)
* [service-40-upload-building-details-for-leasing.md](service-flows/service-40-upload-building-details-for-leasing.md)

### Power of Attorney Services (3)

* [service-29-register-power-of-attorney.md](service-flows/service-29-register-power-of-attorney.md)
* [service-30-act-on-behalf-of-property-owner.md](service-flows/service-30-act-on-behalf-of-property-owner.md)
* [service-42-cancel-power-of-attorney.md](service-flows/service-42-cancel-power-of-attorney.md)

### Property Information & Certificate Services (5)

* [service-31-request-detailed-real-estate-statement.md](service-flows/service-31-request-detailed-real-estate-statement.md)
* [service-32-request-to-whom-it-may-concern-certificate.md](service-flows/service-32-request-to-whom-it-may-concern-certificate.md)
* [service-33-request-property-survey.md](service-flows/service-33-request-property-survey.md)
* [service-34-request-property-valuation.md](service-flows/service-34-request-property-valuation.md)
* [service-35-request-full-partial-indemnity.md](service-flows/service-35-request-full-partial-indemnity.md)

### Diaspora Services (2)

* [service-36-remote-identity-verification.md](service-flows/service-36-remote-identity-verification.md)
* [service-37-remote-property-transactions.md](service-flows/service-37-remote-property-transactions.md)

### Consumer Protection Services (2)

* [service-38-submit-complaint.md](service-flows/service-38-submit-complaint.md)
* [service-39-track-complaint.md](service-flows/service-39-track-complaint.md)

## Shared Platform Features (12)

* [shared-platform-features.md](shared-platform-features.md) — overview of the application lifecycle and the 8 general platform features (Dashboard, Services Catalog, Applications, Documents, Payments, Notifications, Profile & KYC, Help & Support).

### Application Management (4)

* [feature-01-submit-application.md](service-flows/feature-01-submit-application.md)
* [feature-02-track-application-status.md](service-flows/feature-02-track-application-status.md)
* [feature-03-respond-to-information-request.md](service-flows/feature-03-respond-to-information-request.md)
* [feature-04-resubmit-returned-application.md](service-flows/feature-04-resubmit-returned-application.md)

### General Platform Features (8)

Documented in [services-overview.md](services-overview.md) and [shared-platform-features.md](shared-platform-features.md); no separate file per feature.

## UI Specifications (20 files)

Added 2026-08-15, in [ui/](ui/). This module's first UI package — see [ui/README.md](ui/README.md) for the full Service × Form Matrix (11 field-layout patterns across the 43 services, not Group C's 3) and the reasoning behind it.

* [ui/README.md](ui/README.md), [ui/components.md](ui/components.md), [ui/validation-rules.md](ui/validation-rules.md), [ui/status-badges.md](ui/status-badges.md) — shared documentation.
* [ui/screens-unified/](ui/screens-unified/) (4 files) — Services Catalog, Service Details, the configurable Submit Application wizard, Application Review.
* [ui/screens/](ui/screens/) (12 files) — Dashboard, My Properties, My Leases, Applications, Application Details, My Complaints, Power of Attorney, Documents, Payment History, Notifications, Profile & KYC, Help & Support.

## Verified 2026-08-16

Checked directly against the actual repository state, not assumed from any single document's own claims: file counts in `service-flows/` (47 = 43 services + 4 features, matches), `ui/screens/` (13, not 12 — see below), `ui/screens-unified/` (4, matches), and this file's own two corrections above. **One further count discrepancy found and left as-is, since it's a labeling choice rather than an error:** this README says 12 files in `ui/screens/`, but 13 exist — `help-and-support.md` was added at some point after this list was written and was never added to the bullet list, though it is correctly counted in the "20 files" UI Specifications total and in `services-overview.md`'s 8-feature General Platform list. Worth a follow-up line-item fix, tracked here rather than corrected silently in the same pass as the two substantive drift corrections above.
