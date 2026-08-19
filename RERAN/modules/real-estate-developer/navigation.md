---
project: RERAN
module: real-estate-developer
type: navigation
status: current
updated: 2026-08-19
derived_from:
  - "RERAN/modules/real-estate-developer/roles-and-responsibilities.md"
  - "RERAN/modules/real-estate-developer/ui/README.md"
tags:
  - real-estate-developer
  - navigation
  - permissions
---

# Real Estate Developer Navigation & Access

**Confirmed 2026-08-15.** Client decision: Group B does not gate access by role or permission scope. The sidebar and access rules below reflect a single unified model — every role sees and can act on everything; role is recorded as audit-trail attribution only. This supersedes the Role Permission Matrix this document previously described — see [Superseded By This Document](#superseded-by-this-document) at the bottom.

> **Added 2026-08-19.** A **Payment History** item is added to the sidebar, between Applications and Documents. RED previously had no consolidated payment view — payment data existed only scattered across `application-details.md` (per-application fee status), `notifications.md` (a payment-confirmation notification type) and `reports.md` (Financial Reports). This mirrors Group C's `payment-history.md`, built for the same per-transaction, no-standing-account payment model, adapted to RED's own fee-timing categories. See [ui/screens/payment-history.md](ui/screens/payment-history.md).

The shared navigation structure and access rules for the module. Screen files reference this document rather than repeating the sidebar in every file.

## Organizational Structure

Real Estate Developer

├── Developer Principal / Director  
│  
├── Project Registration Officer  
│  
├── Sales & Disclosure Officer  
│  
└── Escrow Liaison

## Audit-Trail Principle

Every action in this module is logged with the acting user and the role they held at the time:

```
Action: Project Registration Submitted
Performed by: Adaeze Nwosu
Role at time of action: Project Registration Officer

Action: Sales Disclosure Filed
Performed by: Adaeze Nwosu
Role at time of action: Project Registration Officer
```

Role is **attribution only**. It does not filter which menu items are visible, which actions are enabled, or who may act on which record. Any of the four roles — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison — may perform any action described in this module, including acting on a record they themselves filed.

## Left Sidebar Navigation

One sidebar, identical for every user of a registered developer account, regardless of role. Every item below is visible and actionable to all four roles.

| Menu | Description |
| ----- | ----- |
| Dashboard | Personalized operational dashboard |
| Projects | Manage development projects |
| Property Registrations | Register and manage property registrations |
| Sales & Disclosures | Manage sales information and disclosures |
| Escrow Management | Monitor escrow activities |
| Applications | View submitted service applications |
| Payment History | View payment history and receipts across all services *(added 2026-08-19)* |
| Documents | Upload and manage documents |
| Reports | Generate operational reports |
| Company Profile | View company information |
| Notifications | View alerts and system messages |
| Help & Support | Contact RERA support |

## Access Rules

1. **Every menu item is reachable by every role.** All four roles have full access to every feature listed above — there is no rendering distinction between roles, no `View`-only variant, and no feature withheld from any role.
2. **No maker ≠ checker restriction.** A user may review, certify, or act on a record they themselves filed. Role is not a basis for excluding anyone from a record's next step.
3. **No role has a read-only variant of any screen.** Every user sees full detail and full action controls on every record in the module.
4. **Reports are not scoped by role.** The full report set — registration, sales, escrow, and organizational — is available to every role. This replaces the previous per-role report scoping (`Registration` / `Sales` / `Escrow`).
5. **Payment History is unscoped the same way.** Every payment made under the developer account, across every service and every domain workspace, is visible to every role — see [ui/screens/payment-history.md](ui/screens/payment-history.md).

## Dashboard

Every role lands on the same [Dashboard](ui/screens/dashboard.md), with identical content and no per-role default view.

The four focus areas the dashboard covers — executive/project overview, registrations and applications, sales and disclosures, and escrow activity — are the same for everyone. They previously appeared as four separate per-role dashboard definitions; they are now sections of one shared screen, since any role may act on any of them.

## Superseded By This Document

Until 2026-08-15, this document described a **Role Permission Matrix** granting each of the four roles `Full`, `View`, or `❌` per feature: Property Registrations barred outright for the Escrow Liaison, Escrow Management barred for the Project Registration Officer, Company Profile editable only by the Principal / Director, and Reports scoped to each role's own domain. It also stated under Left Sidebar Navigation that "visibility depends on assigned role," and defined a separate **Dashboard Overview by Role** table assigning each role a different dashboard focus.

All of that is **retired**, not demoted to optional detail, per the client decision above. Role descriptions remain in [roles-and-responsibilities.md](roles-and-responsibilities.md) and the typical-practice notes in [role-workflows.md](role-workflows.md), but they describe what each role usually does, not what it is permitted to do.
