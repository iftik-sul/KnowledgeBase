---
project: RERAN
module: public-users
type: user-group
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - public-users
  - roles
---

# Public & Informational Users — Roles & Responsibilities

Two roles, distinguished by access tier rather than by function. Both consume the same underlying register; the difference is volume and interface.

## Role Summary

| Role | Player | Access | Services |
| :---- | :---- | :---- | :---: |
| General Public | Unregistered individual | Web, App, WhatsApp, Call Centre | 33 |
| Institutional Verifier | Bank, government body, researcher | API, bulk verification | 33 via API |

---

## 1. General Public

**Player:** Unregistered individual

### Purpose

Verifies property, practitioners and projects before transacting, and consumes awareness content. This is the platform's anti-fraud surface — the source names instant public verification as a direct counter to fake-developer and land-fraud schemes.

### Responsibilities

Not responsibilities in the regulatory sense — this role has no obligations. It performs:

* Property and project status inquiries
* Verification of titles, licences, permits and practitioner cards
* Lookups of accredited surveyors, valuers, trustees, auditors, brokers and management companies
* Rental and service-fee index inquiries
* Case tracking and judicial record lookups
* Fee receipt retrieval and refund requests

### Practical Example

A buyer is offered an off-plan apartment. Before paying a deposit, they open the RERA app, look up the developer to confirm the licence is active, check the project's registration status by project name, and verify the agent's practice card by card number. All three return immediately, without an account.

---

## 2. Institutional Verifier

**Player:** Bank, government agency, or researcher

### Purpose

Performs the same verifications at volume, through an API rather than a screen.

### Responsibilities

* Bulk or programmatic verification of titles, projects and practitioner standing
* Operating within an assigned access tier and usage quota
* Complying with data-use terms

> **Proposed** — the source describes API and bulk access as an access tier with scoped, rate-limited, revocable keys and a usage quota. No API surface, endpoint set, or quota model is described anywhere. If institutional API access is in scope, it needs its own specification. Needs client confirmation.

### Practical Example

A mortgage lender runs title verification as part of loan origination. Rather than staff performing individual lookups, the bank's system calls the verification API for each application and records the result against the file.

---

## Relationship to Other Modules

Group H's verification services appear inside other modules' workflows:

| Verification | Used by |
| :---- | :---- |
| Verify developer, verify project | Property buyers before purchase |
| Verify title / Certificate of Title | Banks before lending; buyers before sale |
| Verify practice card, licences and permits | Anyone engaging an agent or firm |
| Approved trustees and auditors | Developers selecting an escrow partner |

> **Proposed** — this mapping is ours, drawn from reading which verifications correspond to decisions taken in other modules. The source lists the services but never states who consumes them. Needs client confirmation.

**Implication:** these lookups should be built once as shared components and surfaced inside authenticated modules, not rebuilt per module.

## To Confirm

1. Is institutional API access in scope for this platform version?
2. Does the General Public role need any authenticated state at all, given registration is out of scope?
3. Should verification lookups be shared components consumed by other modules, or standalone public pages only?
