---
project: RERAN
module: financial-trust-institutions
type: navigation
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/"
tags:
  - financial-trust-institutions
  - navigation
  - permissions
---

# Financial & Trust Institutions — Navigation & Access

**Proposed.** Sidebar structure, permission matrix and access rules for Group C.

## Why This Module Differs From The Others

Group B has four roles and four clean sidebars: role determines access entirely.

Group C does not. Access here is governed by **role plus permission scope**. Scopes are provisioned by the Institution Relationship Manager under registration Flow 5, which has the authorised representative confirm each staff member's permission scope before activation. Answer A1 establishes that the internal certification gate *is* one of those scopes rather than a role.

The consequences for navigation:

* A Mortgage Officer who holds `certify` sees a menu item that another Mortgage Officer does not.
* The Internal Certification queue belongs to no role at all — it is reached by scope only.
* Two users with the same job title can have different sidebars.

So the matrix below is role × menu **crossed with** scope, not role × menu alone.

---

## Institution Operations Sidebar

One sidebar serves the whole module. Items are filtered per user — a user never sees a menu item they cannot open.

| Menu item | Mortgage Officer | Institution Relationship Manager | Account Trustee | Auditing Bureau Officer | Required scope |
| :---- | :---: | :---: | :---: | :---: | :---- |
| Dashboard | ● | ● | ● | ● | — |
| Service Requests | ● | ● | — | — | `file` |
| Applications | Own | Institution-wide | — | Read | `file` or `audit` |
| Internal Certification | Scope | Configure + Read | — | — | `certify` to act |
| Escrow Requests | — | Read | ● | Read | `escrow` to act |
| Trust Accounts | — | Read | ● | ● | `escrow` or `audit` |
| Compliance Reports | — | Read | — | ● | `audit` |
| Settlement Account | Read | ● | — | Read | `settlement` to act |
| Documents | Own-linked | Institution-wide | Escrow-linked | Institution-wide (read) | — |
| Institution Profile | Read | ● | Read | Read | `admin` to edit |
| Notifications | ● | ● | ● | ● | — |
| Help & Support | ● | ● | ● | ● | — |

● = full access · Read = read-only · Scope = visible only where the user holds the scope · — = not shown

**Count badges** appear on items carrying actionable work: Internal Certification, Escrow Requests, Applications and Notifications.

> **Two rows corrected against the finished screens (issue #27 verification pass).** Documents previously showed `●` for all four roles, which reads as institution-wide visibility for everyone; the finished screen scopes visibility to what each role is linked to (own filings, institution-wide, escrow work, or institution-wide read), and this table now says so instead of the flatter `●`. Internal Certification's Institution Relationship Manager cell was `Configure` alone, which conflated two different things — configuring who holds `certify` (on Institution Profile) and seeing the queue itself (on Internal Certification, now built with a read-only institution-wide view for this case) — corrected to `Configure + Read`.

---

## Permission Scopes

Defined in full in [ui/validation-rules.md](ui/validation-rules.md#permission-scope). Summary:

| Scope | Grants | Typically held by |
| :---- | :---- | :---- |
| `file` | Create and submit service requests | Mortgage Officer, IRM |
| `certify` | Act at the internal certification gate | Any delegated staff member |
| `escrow` | Act on developer escrow requests | Account Trustee |
| `audit` | Submit compliance reports, view escrow audit records | Auditing Bureau Officer |
| `settlement` | Fund the account, settle approved transactions | IRM |
| `admin` | Provision staff, manage scopes, renew approvals | IRM |

---

## Access Rules

1. **Menu items a user cannot open are not rendered** — not rendered-and-disabled. A greyed-out item advertises a capability the user cannot request.
2. **Maker ≠ checker.** A user cannot certify a record they filed, whatever scopes they hold. Holding both `file` and `certify` is permitted and normal; using both on the same record is not.
3. **`audit` is exclusive.** A user holding `audit` may not also hold `escrow` or `certify` at the same institution — the auditor cannot audit their own certifications. **Proposed**; see PR #26, this constrains how smaller institutions staff themselves and is not in any source.
4. **Expired institutional approval blocks submission, not access.** Every menu item remains reachable; Service Requests saves drafts but will not submit, and directs the user to Institution Profile. Per answer B8.
5. **Scope changes take effect at next sign-in** and are written to the audit timeline.
6. **Read-only is a filtered view, not a disabled one.** A read-only user sees the screen without its action controls, not the screen with everything greyed.

---

## Landing After Login

Every role lands on Dashboard. The dashboard is role-specific — see [ui/screens/dashboard.md](ui/screens/dashboard.md) — and its primary call to action differs:

| Role | Primary call to action |
| :---- | :---- |
| Mortgage Officer | New Service Request |
| Institution Relationship Manager | Whichever of approval renewal or settlement shortfall is more urgent; otherwise institution overview |
| Account Trustee | Oldest escrow request awaiting assessment |
| Auditing Bureau Officer | Nearest reporting obligation |

A user holding `certify` sees a certification queue count on the dashboard regardless of role.

---

## External Access

**Trustee Centre operators (Group G)** reach Group C services through [ui/screens/assisted-service-terminal.md](ui/screens/assisted-service-terminal.md), operating on a walk-in customer's behalf under answer C2. They are not Group C users, hold no Group C scopes, and do not appear in the matrix above. Their per-operator transaction scopes are provisioned under registration Flow 7 and belong to Group G's navigation when those interfaces are written.
