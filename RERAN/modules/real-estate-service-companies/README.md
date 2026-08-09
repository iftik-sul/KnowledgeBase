---
project: RERAN
module: real-estate-service-companies
type: overview
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - real-estate-service-companies
  - index
---

# Real Estate Service Companies Module

RERAN user Group D — brokerage, property-management and jointly-owned-property management firms operating under licence.

**Scope:** post-login functionality only.

## Contents

| Section | Count |
| :---- | :---: |
| Roles | 4 |
| Business Services | 26 |

* [roles-and-responsibilities.md](roles-and-responsibilities.md)
* [services-overview.md](services-overview.md)

## The Defining Characteristic: Four Sub-domains

Group D is the most internally varied module in the project. Its 26 services span four largely unrelated areas of business:

| Sub-domain | Services | Nature |
| :---- | :---: | :---- |
| Jointly Owned Property (JOP) | 11 | Owners' associations, service charges, JOP escrow accounts |
| Licensing | 8 | Firm licences, permits, practice cards, valuations |
| Rental | 3 | Management contracts, tenancy system users |
| Transaction | 2 | Auction permits and auction sale registration |
| Disputes | 2 | Primary suits and execution cases for managed property |

A brokerage firm and a jointly-owned-property manager share a module but barely share a workflow. This is worth confirming with the client before building — see Open Questions.

## Platform Sub-systems

* Owner / JOP System
* Tenancy Management System
* Brokerage Licensing & Listings
* Dispute Filing Portal

## Service Flows

> Not yet written.

## UI Specifications

> Not yet written.

## Open Questions

1. **Should JOP be its own module?** With 11 services, its own sub-system, its own escrow mechanics and its own role, it functions as a separate product that happens to be operated by service companies. Splitting it would give five RERAN modules rather than four.
2. **Do the four roles ever overlap?** A firm might be both a brokerage and a property manager. Does one company account carry multiple Group D roles simultaneously?
3. **JOP escrow vs developer escrow.** Several JOP services mirror Group B's escrow services — account transfer, authorised signatories, appointing auditors. Are these the same mechanism with different actors, or genuinely separate systems?
4. Does the two-gate pattern observed in Group C (internal certification, then RERA audit) apply here? Group D services show no internal certification step in the source.
