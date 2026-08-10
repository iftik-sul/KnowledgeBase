---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - financial-trust-institutions
  - index
---

# Financial & Trust Institutions Module

RERAN user Group C — banks, mortgage institutions, account trustees and auditing bureaux that finance, secure and audit real-estate transactions.

**Scope:** post-login functionality only. Registration and onboarding are out of scope for this project.

## Contents

| Section | Count |
| :---- | :---: |
| Roles | 4 |
| Business Services | 18 |
| Shared Platform Features | 17 |

* [roles-and-responsibilities.md](roles-and-responsibilities.md) — Mortgage Officer, Institution Relationship Manager, Account Trustee, Auditing Bureau Officer.
* [services-overview.md](services-overview.md) — the 18 services, category breakdown, status vocabulary, and channels.

## Service Flows

18 service-flow documents are available, each using the 21-section individual-user template.

## UI Specifications

> Not yet written. Follows the service flows, per the project's derivation chain.

## The Defining Pattern: Two Gates

Every Group C action passes through an internal certification gate inside the institution and then an external audit gate at RERA. No Group C role completes a regulated action unilaterally. This shapes every service flow, every status, and every screen in the module.

## Platform Sub-systems

The source names three for this group:

* Online Mortgage System
* Trust-Account Approval & Renewal
* Transaction Audit Queue

## Proposed Content

This module contains proposed content marked with `contains_proposals: true` in frontmatter and inline `> **Proposed**` blocks. The source material is incomplete for this group — in particular, two of the four roles have no documented post-login behaviour at all.

**Client-data and proposed implementation details remain clearly marked.** They are listed in the To Confirm section of each document:

* [roles-and-responsibilities.md](roles-and-responsibilities.md#to-confirm--summary) — 7 items
* [services-overview.md](services-overview.md#to-confirm) — remaining category, scope and status-vocabulary confirmations

When an item is confirmed, remove its `> **Proposed**` block and bump `updated`. When every proposal in a file is resolved, remove `contains_proposals` from its frontmatter.

## Known Source Gaps

* **Account Trustee and Auditing Bureau Officer own no numbered services.** Both have substantial described functions but appear in the service table only as participants in Group B's escrow workflow. Their Group C interface is reconstructed, not sourced.
* **Internal certification is implemented as a maker-checker permission scope, not a fifth role.** **Proposed**
* **No status vocabulary exists anywhere in the source**, for any user group.
* **Services #1 and #2 have a role-assignment inconsistency** between the service table and the role descriptions.
