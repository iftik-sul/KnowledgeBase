---
project: RERAN
module: financial-trust-institutions
type: navigation
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - index
---

# Financial & Trust Institutions — UI Specifications

**Proposed.** The source material gives workflows, channels, output documents and SLAs, but no screen designs. This package applies the UI-spec format established in the Real Estate Developer module.

**Derivation note.** These screens are derived from the roles document, the services overview and the answered open questions — not from the service-flow files, which are currently thin (see issue #23). Fourteen of the eighteen service flows will gain detail when that issue lands; the screens that will need re-checking against them are marked in the table below.

---

## Role × Screen Matrix

This is the index that makes a missing screen visible. Every role must be able to discharge every responsibility in `roles-and-responsibilities.md` through a screen listed here.

| Screen | Mortgage Officer | Institution Relationship Manager | Account Trustee | Auditing Bureau Officer | Certifier scope |
| :---- | :---: | :---: | :---: | :---: | :---: |
| [dashboard](screens/dashboard.md) | ● | ● | ● | ● | ● |
| [service-request](screens/service-request.md) | ● | #1, #2, #18 | — | — | — |
| [applications](screens/applications.md) | Own | Institution-wide | — | Read | Own |
| [application-details](screens/application-details.md) | ● | ● | — | Read | ● |
| [internal-certification-queue](screens/internal-certification-queue.md) | — | Configure | — | — | ● |
| [escrow-request-queue](screens/escrow-request-queue.md) | — | Read | ● | Read | — |
| [escrow-request-details](screens/escrow-request-details.md) | — | Read | ● | Read | — |
| [trust-accounts](screens/trust-accounts.md) | — | Read | ● | ● | — |
| [compliance-reports](screens/compliance-reports.md) | — | Read | — | ● | — |
| [settlement-account](screens/settlement-account.md) | Read | ● | — | Read | — |
| [institution-profile](screens/institution-profile.md) | Read | ● | Read | Read | Read |
| [documents](screens/documents.md) | ● | ● | ● | ● | ● |
| [notifications](screens/notifications.md) | ● | ● | ● | ● | ● |
| [assisted-service-terminal](screens/assisted-service-terminal.md) | — | — | — | — | — |

● = operates the screen · Read = read-only · — = no access

**Assisted Service Terminal** is operated by a Trustee Centre operator (Group G), not by a Group C role. It is documented here because it executes Group C services on a walk-in customer's behalf under answer C2. When Group G's interfaces are written, this screen moves there and is linked from here.

---

## Service × Form Matrix

All eighteen services use one configurable form (`service-request.md`) rather than eighteen form specs. The form's field groups, document set and routing vary by service; the shell does not.

| Services | Owner (per answer A4) | Assisted mode | Internal certification | Escrow-routed |
| :---- | :---- | :---: | :---: | :---: |
| #1–#2 institutional approval | Institution Relationship Manager | — | Optional | — |
| #3–#7 mortgage lifecycle | Mortgage Officer | Where source names centre | Yes when configured | — |
| #8–#11 finance lease lifecycle | Mortgage Officer | Yes | Yes when configured | — |
| #12 fund company registration | Mortgage Officer | Yes | Yes when configured | — |
| #13–#17 title and ownership | Mortgage Officer, or Group G operator | Yes | Yes when configured | — |
| #18 contract cancellation | Institution Relationship Manager | Yes | Yes when configured | — |
| Group B escrow requests | Account Trustee (inbound) | — | — | Yes |

Group B escrow requests are not among the eighteen. They arrive from the developer module and are worked in the escrow queue — see answer A2, which confirms from source rows 8–12 that the Account Trustee acts inside the platform rather than recording an outcome reached elsewhere.

---

## Screens

| Screen | Purpose |
| :---- | :---- |
| [dashboard](screens/dashboard.md) | Role-specific entry point: work in hand, approvals, settlement and expiry warnings |
| [service-request](screens/service-request.md) | The configurable form behind all eighteen services |
| [applications](screens/applications.md) | Search, filter and act on submitted requests |
| [application-details](screens/application-details.md) | One request: particulars, documents, workflow position, audit trail |
| [internal-certification-queue](screens/internal-certification-queue.md) | Maker-checker gate before RERAN submission |
| [escrow-request-queue](screens/escrow-request-queue.md) | Developer escrow requests awaiting trustee certification |
| [escrow-request-details](screens/escrow-request-details.md) | One escrow request: solvency, milestone evidence, decision |
| [trust-accounts](screens/trust-accounts.md) | Register of trust accounts under the institution's trusteeship |
| [compliance-reports](screens/compliance-reports.md) | Independent compliance reports and escrow audit findings |
| [settlement-account](screens/settlement-account.md) | Standing pre-funded account: balance, funding, ledger, awaiting settlement |
| [institution-profile](screens/institution-profile.md) | Approval standing, expiry tracking, staff and permission scopes |
| [documents](screens/documents.md) | Institution document repository |
| [notifications](screens/notifications.md) | Operational, approval, expiry and low-balance alerts |
| [assisted-service-terminal](screens/assisted-service-terminal.md) | Group C services operated for a walk-in customer |

---

## Shared Documentation

Shared logic is defined once in these files and linked from screens. Screens must not restate it.

* [components.md](components.md) — component library, including the sidebar definition
* [validation-rules.md](validation-rules.md) — validation patterns and permission-scope rules
* [status-badges.md](status-badges.md) — status vocabularies and their treatments

---

## Screen File Template

Every screen file uses, in order: **Purpose, Layout, Sections, Empty State, Reused Components, Validation, Role Variations, User Flow, Notes.**

Where a section is identical for all roles, state it once at screen level. Where it differs, state it under Role Variations and leave a pointer at screen level. Do not restate shared component or validation definitions — link to the shared files.

---

## Structural Characteristic

Every Group C action passes two gates: internal certification inside the institution, then external audit at RERAN. No Group C role completes a regulated action unilaterally. Every screen that submits, certifies or approves must show which gate the record currently sits at and who holds it.

The internal gate is a **permission scope**, not a role (answer A1). Any delegated staff member may hold a certifier scope; the screen serving that gate is filtered by scope, not by job title.
