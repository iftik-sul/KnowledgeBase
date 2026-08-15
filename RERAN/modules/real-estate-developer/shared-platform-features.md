---
project: RERAN
module: real-estate-developer
type: overview
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/individual-user/shared-platform-features.md"
  - "RERAN/modules/real-estate-developer/README.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-01-register-initial-sale.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-13-register-real-estate-project.md"
tags:
  - real-estate-developer
  - shared-feature
  - application-management
---

# Shared Platform Features – Application Management

> **Proposed** — this document and the four feature files it indexes are not sourced. `RERAN_service_flows_v2.md` describes each of the 27 Group B services as its own row; it does not name a shared application-management layer. This module is documented by the same six-stage pipeline (lodge → validate → audit → pay → issue → record) that the individual-user and financial-trust-institutions modules already carry, and the same generic submit/track/respond/resubmit shape recurs across all 27 service-flow files' own Section 12/13 (Processing Workflow / Application Status Flow) — most visibly the shared `Information Requested` and `Returned` statuses that appear as Additional Statuses in nearly every service. This document names that recurring shape once, following the pattern already established in [individual-user/shared-platform-features.md](../individual-user/shared-platform-features.md) and already proposed (not yet written) for financial-trust-institutions in `services-overview.md`. Needs client confirmation.

**Unlike individual-user, payment timing is not uniform across Group B.** Sampling this module's service-flow files found genuine variance: Service #1 (Register Initial Sale) pays before RERA's decision; Service #13 (Register Real Estate Project) pays after RERA's audit/accept step; Service #8 (Escrow Account Activation) carries no RERA fee at all. Feature #1 below documents the *mechanics* of submission — form, documents, payment where applicable — without asserting a single timing order; each service's own Section 8/9 remains the authority on its fee and payment timing.

## Feature #1 – Submit Application

Used by every service that requires an official submission to RERA.

Examples:

* Register Initial Sale
* Register Initial Rent-to-Own
* Register Real Estate Project
* Amend Initial Procedures Data
* Register Sale Associated with an Initial Mortgage
* Escrow Account Activation
* Real Estate Licensing Application
* Real Estate Project Sub-division
* Requesting a Technical Report for the Project

See [feature-01-submit-application.md](service-flows/feature-01-submit-application.md) for full detail.

## Feature #2 – Track Application Status

Allows users to monitor every submitted application from one place — the module's **Applications** sidebar item.

Examples:

* Project Registration
* Property (Unit) Sale Registration
* Escrow Account Activation / Transfer
* Real Estate Licensing Application
* Technical Report Request

See [feature-02-track-application-status.md](service-flows/feature-02-track-application-status.md) for full detail.

## Feature #3 – Respond to Information Request

Allows users to respond when RERA requests additional information, documents, or corrections.

Examples:

* Upload missing project or unit documents
* Correct sale or purchaser details
* Provide additional survey or licensing evidence
* Submit revised escrow assessment documents

See [feature-03-respond-to-information-request.md](service-flows/feature-03-respond-to-information-request.md) for full detail.

## Feature #4 – Resubmit Returned Application

Allows users to correct returned applications and resubmit them without creating a new application.

Examples:

* Incorrect project or unit details
* Missing documents
* Invalid survey data
* Incorrect payment evidence (where the service requires payment)

See [feature-04-resubmit-returned-application.md](service-flows/feature-04-resubmit-returned-application.md) for full detail.

## This order mirrors the lifecycle most Group B services follow:

Choose Service
        ↓
Complete Form
        ↓
Submit Application
        ↓
Track Application Status
        ↓
Information Requested? ── Yes ──► Respond to Information Request
        │
        No
        │
Returned? ─────────────── Yes ──► Resubmit Returned Application
        │
        No
        │
Approved / Registered / Rejected

**Not every service follows this exact shape.** Service #13 (Register Real Estate Project) runs a longer chain — License → Apply → Audit (accept/reject) → Upload Units → Registrar Account → Pay → Certificate — with payment gated behind an intermediate accept step rather than at the front. This diagram documents the common case, not every service's Section 12; consult each service-flow file directly where its own workflow diverges.
