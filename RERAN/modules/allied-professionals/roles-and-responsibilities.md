---
project: RERAN
module: allied-professionals
type: user-group
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - allied-professionals
  - roles
---

# Allied Professionals & Service Trustees — Roles & Responsibilities

Four roles, none of which owns a service. Each performs actions inside other groups' workflows.

This document describes what each role does and where in other modules it appears. Post-login only.

## Role Summary

| Role | Player | Appears in | Own services |
| :---- | :---- | :---- | :---: |
| Registration / Service Trustee Centre | Accredited centre | C, E, F — extensively | 0 |
| Survey Company | ESVARBON-accredited | B, E | 0 |
| Valuer | Registered valuer | D, E, F | 0 |
| Conveyancer / Legal Practitioner | Property lawyer | — not named in any service row | 0 |

---

## 1. Registration / Service Trustee Centre

**Player:** Accredited centre with operator staff

### Purpose

Processes walk-in transactions, registrations and dispute filings on behalf of customers who do not transact online. The platform's counter channel.

### Where It Appears

Named as a channel across a large share of the 145 services, including:

* **Group C** — finance lease registration, amendment, transfer and release; fund company registration; heirs' sale; company share sale
* **Group E** — sale registration, mortgaged property sale, gift registration, lease-to-own services, usufruct services, heirs' ownership, statements and valuations
* **Group F** — dispute filing across most tenant dispute services; lease registration and renewal

The recurring workflow phrase is: customer moves to the centre, submits documents, the operator enters the transaction into the system and audits it, the customer pays, and outputs are delivered by email.

### Actions Performed

* Receive and verify customer documents at the counter
* Enter transaction data into the relevant RERA sub-system on the customer's behalf
* Perform first-line audit of submission completeness
* Take payment and issue receipts
* Deliver outputs to the customer

> **Proposed** — no source document describes the operator's interface, permissions, or how a transaction is attributed between operator, centre and customer. The actions above are inferred from the workflow steps that name the centre. Needs client confirmation.

### Practical Example

A landlord without internet access visits a Trustee Centre to register a lease. The operator checks the tenancy contract and identification, enters the lease details into the tenancy system under the landlord's record, takes payment, and the registration certificate is emailed to both parties.

---

## 2. Survey Company

**Player:** ESVARBON-accredited surveying firm

### Purpose

Prepares project and property survey data, matches it to approved plans, and submits it to the Survey Department.

### Where It Appears

* **Group B** — project registration, sub-division, project re-registration, and survey data registration/amendment. The developer designates the survey company, which then prepares and submits data.
* **Group E** — real estate survey application: site visit, measurement, preparation of survey data and charts, issue of final report.

### Actions Performed

* Accept designation by a developer or owner
* Prepare survey data and match it to approved plans
* Upload unit inventories for registered projects
* Submit packages to the Survey Department for review
* Correct and resubmit returned packages

### Practical Example

A developer registering a new project designates an accredited survey company. The company prepares the plot and unit data, matches it against the approved building plans, pays the approval fee, and submits to the Survey Department. The department verifies coordinates and approves; the project data is committed to the title-deed register.

---

## 3. Valuer

**Player:** Registered valuer

### Purpose

Submits valuations and professional reports supporting transactions, financing and disputes.

### Where It Appears

Valuation services exist in the service table but are owned by other groups — Group D holds evaluation certificate registration, Group E and F hold property and rental valuation applications. The valuer performs the underlying work.

### Actions Performed

* Receive valuation requests
* Conduct the valuation
* Submit valuation details, value and notes
* Issue the evaluation certificate

> **Proposed** — the Group D evaluation service describes a company signing in, viewing applications, preparing an application on a customer's behalf, accepting or rejecting it, performing the evaluation, and issuing a certificate through the app. That flow is filed under Group D but describes valuer behaviour. Whether the valuer is a Group D company user or a distinct Group G actor is unclear in the source. Needs client confirmation.

---

## 4. Conveyancer / Legal Practitioner

**Player:** Property lawyer

### Purpose

Conducts title verification, lodges documentation, and supports due diligence.

### Where It Appears

**Nowhere in the service table.** This role is defined in the user group structure but is not named in any of the 145 service rows, in any workflow step, or in any channel.

> **Proposed** — the conveyancer has a role definition and no documented platform behaviour whatsoever. Either they use the platform only through general public verification services, or their function was intended and never specified. This is the single largest unknown in Group G. Needs client confirmation.

---

## Cross-Cutting Question: Attribution

When a Trustee Centre operator submits a transaction for a customer, or a survey company submits data designated by a developer, the record must be attributed. The source never addresses this.

Unresolved for every Group G role:

* Whose account owns the resulting record?
* Who is liable for an error — the acting professional or the principal?
* Does the customer see the transaction in their own account afterwards?
* Is the acting professional's identity recorded on the output document?

> These questions apply to every service where a Group G actor participates — a large share of the platform. They are worth resolving before any module's service flows are written, not after.

## To Confirm

1. Is the Trustee Centre operator interface in scope? It may be the highest-volume interface in the platform.
2. Transaction attribution — operator, centre, customer, or all three?
3. Do survey companies and valuers work inside the RERA platform or their own systems?
4. Is the valuer a Group D company user, a Group G actor, or both?
5. What does a conveyancer do on this platform? No source material describes any behaviour.
6. Should Group G be a module, or shared interface documents referenced from the modules that use them?
