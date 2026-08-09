---
project: RERAN
type: standard
status: current
updated: 2026-08-09
tags:
  - standard
  - meta
---

# RERAN Project Standards

This document declares RERAN's vocabulary under the repository-wide rules in [/documentation-standards.md](/documentation-standards.md). Where the two differ, the repository standards win; this document only fills in what they leave to each project.

---

## What a Module Means Here

RERAN is a regulatory platform serving distinct stakeholder groups. **A module is a user group** — the set of people who share a service surface, a portal, and a set of roles.

Modules follow the eight groups defined in the RERA Nigeria User Group Structure:

| Module folder | User group | Abbrev. | Status |
| :---- | :---- | :---: | :---- |
| `individual-user` | Property owners, landlords, tenants, buyers, diaspora investors, PoA holders | IU | Documented |
| `real-estate-developer` | Group B — Real Estate Developers | RED | In progress |
| `financial-trust-institutions` | Group C — Financial & Trust Institutions | FTI | Planned |
| `regulatory-authority` | Group A — Regulatory Authority & Governance | RA | Planned |
| `real-estate-service-companies` | Group D — Real Estate Service Companies | RESC | Planned |
| `allied-professionals` | Group G — Allied Professionals & Service Trustees | AP | Planned |
| `public-users` | Group H — Public & Informational Users | PU | Planned |

Groups E (Property Owners & Landlords) and F (Tenants & Consumers) are both natural persons and are documented together as `individual-user`.

Abbreviations are for document IDs (`RERAN-IU-FLOW-001`).

---

## Stage Folders

RERAN's derivation chain:

```
reference/source-of-truth/  →  service-flows/  →  ui/
```

```
modules/<module-name>/
├── README.md                    # module index
├── roles-and-responsibilities.md
├── services-overview.md         # where the module has business services
├── service-flows/
│   ├── service-01-<name>.md
│   └── feature-01-<name>.md
└── ui/
    ├── README.md                # role × screen matrix
    ├── components.md
    ├── validation-rules.md
    ├── status-badges.md
    └── screens/
        └── <screen-name>.md
```

A module is not required to have every stage. A module may be documented at the service-flow stage with no UI yet, or the reverse.

---

## The `ui/` Stage

Screens and services are **many-to-many**. A single service flow touches a dozen screens, and a screen such as Payment or Document Upload appears in most services. UI documentation is therefore organized by screen, not mirrored per service.

**Rules:**

1. **One file per distinct screen**, in `ui/screens/`. Never one file per role-screen pair.
2. **Role differences go inside the screen file**, under a `## Role Variations` section. A Dashboard that differs across four roles is one file with four variations, not four files.
3. **Shared logic is documented once** and linked, never repeated per screen:
   - `components.md` — the component library (data tables, alert cards, badges)
   - `validation-rules.md` — validation patterns referenced by form screens
   - `status-badges.md` — status vocabulary and colour coding
4. **`ui/README.md` carries the role × screen matrix** — which roles reach which screens. This is the index that makes a missing screen visible.
5. **Screens link back to the flows that use them**, and flows list the screens they touch. The matrix is maintained from both ends.
6. **`figma:` frontmatter** on a screen file records the design generated from it.

No `flows/` folder inside `ui/`. Journey-level content — the linear path a role takes through the system — lives at module level in `role-workflows.md`, because it describes the user's route, not the interface.

---

## Additional Document Types

Beyond the base types in the repository standards, RERAN uses:

| Type | Purpose |
| :---- | :---- |
| `service-flow` | A regulatory service: eligibility, documents, fees, workflow, statuses, outcomes |
| `registration-flow` | Onboarding and account registration sequences |
| `user-group` | Roles and responsibilities within a module |
| `navigation` | Sidebar structure, permission matrix, and access rules |

---

## File Naming

| Location | Pattern | Example |
| :---- | :---- | :---- |
| `service-flows/` | `service-NN-<name>.md` | `service-06-register-property-sale.md` |
| `service-flows/` | `feature-NN-<name>.md` | `feature-01-submit-application.md` |
| `ui/screens/` | `<screen-name>.md` | `application-details.md` |
| module root | `<document-name>.md` | `roles-and-responsibilities.md` |

Service numbers are stable once assigned and are not renumbered when a service is deprecated.

---

## Exceptions

None currently. Any exception to the repository standards is recorded here with its reason.
