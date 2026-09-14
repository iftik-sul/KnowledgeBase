---
project: RERAN
module: regulatory-authority
type: service-flow
status: draft
contains_proposals: true
source_type: derived
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/roles-and-responsibilities.md"
  - "RERAN/modules/regulatory-authority/roles-and-actions-analysis.md"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - rbac
  - platform
---

# Group A Service A-6 — Provision & Manage Access (RBAC)

> **Back-office platform service — the foundation for every other Group A service.**
> No external service routes to it, but A-1, A-2, and A-3 cannot be used until it
> exists: it is the service that creates staff accounts and enforces the role
> permissions those services depend on. This service *is* RBAC.

## 1. Service Overview

**Provision & Manage Access** is how RERA administers who its staff are and what each is
allowed to do inside Group A. It creates and manages staff accounts, assigns the eight
Group A roles, configures the permissions attached to them, enrols MFA, and owns the
audit trail. It is the one place in RERAN where real access control is administered —
everywhere else a role is audit attribution only.

## 2. Purpose

Make Group A's access model real and safe: every staff member has exactly the
permissions their role requires, protected by MFA, with every access change recorded —
so the RBAC that A-1/A-2/A-3 rely on is actually enforced and auditable.

## 3. Description

A System Super Administrator creates a staff account, assigns one or more of the eight
Group A roles, configures or adjusts the permissions on those roles, and enrols the
user in MFA. The administrator can also suspend or deactivate accounts and review the
audit trail. All of these are themselves recorded.

## 4. Who Can Act

**System Super Administrator** (Group A), under RBAC + MFA. This role administers the
permission model itself, so it is the most sensitive access surface on the platform.

## 5. Trigger *(replaces "Entry Conditions")*

Internal — staff onboarding, a role change, an offboarding, or a permission adjustment.
No queue and no applicant submission.

## 6. What the Administrator Works With

- The staff directory (existing accounts and their roles).
- The eight Group A roles and their permission sets.
- The MFA enrolment state of each account.
- The access audit trail.

## 7. Task Checklist *(replaces "Review Checklist")*

- The account maps to a real staff member.
- The assigned role(s) match the person's function.
- Permissions follow least-privilege for the role.
- MFA is enrolled before the account can act.

## 8. Service Fee / 9. Payment Required

**N/A.**

## 10. Authority & Access Control

- **Role:** System Super Administrator (Group A).
- **Access control:** RBAC-gated + MFA (self-referential — this service administers the
  very controls it is protected by).
- **Sub-system:** Admin & Configuration Console.

## 11. Expected Processing Time

N/A — an administrative action, not a timed application.

## 12. Processing Workflow

```
Administrator opens Admin Console  (RBAC + MFA)
        ↓
Create / select staff account
        ↓
Assign role(s) from the eight Group A roles
        ↓
Configure permissions  (least-privilege)
        ↓
Enrol MFA
        ↓
Activate  (or suspend / deactivate on offboarding)
        ↓
Write every access change + actor to the audit trail
```

## 13. Status *(not the shared decision vocabulary)*

An account is **Invited**, **Active**, **Suspended**, or **Deactivated**.

## 14. Possible Outcomes

- **Provisioned / Updated** — the account and its access are set.
- **Suspended / Deactivated** — access is withdrawn.

## 15. RBAC scope note *(back-office-specific)*

Per the module analysis and open-questions A5, all **eight** roles are defined here so
the permission model and MFA are complete, even though only some have functional
screens in the first build. Defining a role and granting it functional screens are
separate steps: this service can define and assign a role (e.g. State Liaison) before
that role's own service surfaces are built.

## 16. Cross-Module Dependencies

1. **Every other Group A service depends on this one.** A-1/A-2/A-3's "RBAC + MFA" gate
   is enforced by the roles and permissions this service administers. It must be built
   first (see the analysis's proposed build order).
2. **The audit trail** this service owns underpins the accountability claims of every
   other Group A service.

## 17. Related Services

- **A-1, A-2, A-3** — all gated by the access this service administers.
- All other Group A services (their actors are provisioned here).

## 18. UI Screens

- **Staff directory** — accounts, roles, and MFA state.
- **Account editor** — create/edit an account, assign roles, enrol MFA, suspend/deactivate.
- **Role & permission editor** — the eight roles and their permission sets.
- **Access audit view** — the record of access changes.

## 19. API Requirements

- Create / edit / suspend / deactivate staff account
- Assign / revoke roles
- Configure role permissions
- Enrol / reset MFA
- Fetch access audit trail
- Write audit-log entry

## 20. Database Entities

- Staff User *(account)*
- Role *(the eight Group A roles)*
- Permission *(attached to roles)*
- MFA Enrolment
- Audit Log *(owned here)*

## 21. Acceptance Criteria

- Only a System Super Administrator with MFA can administer accounts, roles, or
  permissions.
- An account cannot act on any Group A service until it has a role and enrolled MFA.
- All eight roles are definable and assignable, whether or not their functional screens
  are built.
- Suspending or deactivating an account immediately withdraws its access.
- Every access change, with its actor, is written to the audit trail.

## 22. Business Rules

1. This service administers the RBAC + MFA that every other Group A service enforces;
   it must exist before they can be used.
2. Permissions follow least-privilege per role.
3. MFA enrolment is mandatory before an account can act.
4. All access changes are permanently recorded in the audit trail with the acting
   administrator.
