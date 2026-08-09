---
project: RERAN
module: allied-professionals
type: overview
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - allied-professionals
  - index
---

# Allied Professionals & Service Trustees Module

RERAN user Group G — accredited surveyors, valuers, conveyancers, and the Registration / Service Trustee Centres that transact on behalf of walk-in customers.

**Scope:** post-login functionality only.

## This Module Has No Services

Group G owns **zero** of the 145 services in the master table. This is not an omission in the source — it reflects what these roles are.

Group G actors are **participants inside other groups' workflows**, not applicants with their own catalogue. They appear throughout the service table as steps in someone else's service:

* "Developer designates a survey company"
* "Survey company prepares data and matches it to approved plans"
* "Visit Real Estate Registration Trustee Centres"
* "Move to service center, submit docs, employee enters system and audits"

They act; they do not apply.

> **Proposed** — this module should document **interfaces**, not services. Each Group G role needs a specification for the actions it performs inside other groups' flows: what it receives, what it does, what it returns. This is a different document shape from every other module in the project. Needs client confirmation.

## Contents

* [roles-and-responsibilities.md](roles-and-responsibilities.md)

## Why This Module Matters More Than Its Service Count Suggests

The **Registration / Service Trustee Centre** is named as a channel on a large share of the 145 services — across Groups C, E and F. For many services it is the *only* channel. A Trustee Centre operator is therefore one of the highest-volume users of the entire platform, performing transactions on behalf of customers who never log in themselves.

No source document describes the operator's interface.

## Open Questions

1. Is a Trustee Centre operator's interface in scope for this project? It may be the highest-volume interface in the platform.
2. When an operator transacts on a customer's behalf, whose account is the transaction recorded under — the customer's, the centre's, or both?
3. Do survey companies and valuers work inside the RERA platform, or in their own systems with outputs submitted to RERA?
4. Should this be a module at all, or a set of shared interface documents referenced from the modules that use them?
