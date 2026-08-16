---
project: RERAN
module: financial-trust-institutions
type: navigation
status: current
updated: 2026-08-16
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

**Confirmed 2026-08-14.** Client decision: Group C does not gate access by role or permission scope. Sidebar structure and access rules below reflect a single unified model — every role sees and can act on everything; role is recorded as audit-trail attribution only. This supersedes the role × scope matrix this document previously described — see [Superseded By This Document](#superseded-by-this-document) at the bottom.

## Why This Module No Longer Differs From The Others

Group C now works the same way Group B does: one sidebar, identical for every user of a verified institution account, whatever their role.

**Corrected 2026-08-15.** This section previously added that the two groups still differed in the *reason* roles are documented — "Group B roles determine access; Group C roles exist purely as an audit-trail attribution field." That distinction no longer holds. The same client decision has since been applied to Group B (issue #58): its four roles no longer gate access either, and are likewise retained as audit-trail attribution only. Roles in both modules now mean the same thing — a record of who performed an action and what role they held at the time, not a permission. See [roles-and-responsibilities.md](roles-and-responsibilities.md) for Group C's role descriptions and how they feed the audit trail, and [`../real-estate-developer/navigation.md`](../real-estate-developer/navigation.md) for Group B's.

---

## Audit-Trail Principle

Every action in this module is logged with the acting user and the role they held at the time:

```
Action: Application Submitted
Performed by: Amara Okafor
Role at time of action: Mortgage Officer

Action: Application Certified
Performed by: Musa Ibrahim
Role at time of action: Account Trustee
```

Role is **attribution only**. It does not filter which menu items are visible, which actions are enabled, or who may act on which record. Any of the four roles — Mortgage Officer, Institution Relationship Manager, Account Trustee, Auditing Bureau Officer — may perform any action described in this module, including certifying a record they themselves filed.

---

## Institution Operations Sidebar

One sidebar, identical for every user of a verified institution account, regardless of role:

* Dashboard
* Service Requests
* Applications
* Internal Certification
* Escrow Requests
* Trust Accounts
* Compliance Reports
* Payment History *(corrected 2026-08-14 — previously "Settlement Account"; no standing account exists to manage, see `open-questions.md` B1 and [payments.md](payments.md))*
* Documents
* Institution Profile
* Notifications
* Help & Support

Every item is visible and actionable to every role. There is no menu filtering, no scope-gated rendering, and no role-driven read-only variant of any screen.

**Count badges** appear on items carrying actionable work: Internal Certification, Escrow Requests, Applications and Notifications — the same counts for every user, since the underlying queues are institution-wide rather than role- or scope-scoped.

---

## Access Rules

1. **Every menu item is reachable by every role.** There is no rendering distinction between roles.
2. **No maker ≠ checker restriction.** A user may certify a record they themselves filed. This corrects the previous documentation, which enforced maker ≠ checker as an access rule tied to the retired `certify` scope.
3. **Expired institutional approval blocks submission, not access.** Every menu item remains reachable; Service Requests saves drafts but will not submit, and directs the user to Institution Profile. Per answer B8. *(Unaffected by the unified-access decision — this was never a role/scope rule.)*
4. **No role has a read-only variant of any screen.** Every user sees full detail and full action controls on every record in the module.

---

## Landing After Login

**Resolved 2026-08-15.** Every role lands on the same [Dashboard](ui/screens/dashboard.md), with identical content and no per-role primary call to action.

> **Superseded 2026-08-14 framing, replaced rather than extended.** This section previously proposed a different suggested CTA per role — New Service Request (Mortgage Officer), approaching approval renewal (Institution Relationship Manager), oldest escrow request (Account Trustee), nearest reporting obligation (Auditing Bureau Officer) — described as "a convenience default, not an access restriction," with the underlying design question ("should a unified dashboard show one shared CTA for everyone?") explicitly left open. That question is now answered: the reworked Dashboard (issue #50) shows the same Quick Actions row to every user — New Service Request, View Applications, Internal Certification Queue, Escrow Requests — plus Focus Area summaries covering what the four role-specific CTAs used to point at individually (applications, escrow & trust accounts, compliance, institution standing). There is no remaining per-role landing default to document.

---

## External Access

**Trustee Centre operators (Group G)** reach Group C services through [ui/screens/assisted-service-terminal.md](ui/screens/assisted-service-terminal.md), operating on a walk-in customer's behalf under answer C2. They are not Group C users, do not hold Group C roles, and do not appear in the sidebar above. Their per-operator transaction permissions are provisioned under registration Flow 7 and belong to Group G's navigation when those interfaces are written. **Unaffected by this change** — Group G's access model is outside issue #38's scope and is not addressed by the client decision above.

---

## Superseded By This Document

Until 2026-08-14, this document described a role × permission-scope matrix: six permission scopes (`file`, `certify`, `escrow`, `audit`, `settlement`, `admin`), each provisioned per staff member under registration Flow 5, gating which menu items a given user could see; a maker ≠ checker access rule; and an `audit`-exclusivity rule barring a user from holding `audit` alongside `escrow` or `certify`. All of that is **retired**, not demoted to optional detail, per the client decision above. See [roles-and-responsibilities.md](roles-and-responsibilities.md#how-they-work-together) for how certification now works as an unrestricted action, attributed by role in the audit trail rather than gated by scope.

**Fully reconciled as of 2026-08-16.** This section previously reported all 14 `ui/screens/*.md` files, plus `ui/screens-unified/`, `ui/validation-rules.md`, and `ui/components.md`, as "mostly reconciled" against the unified-access and corrected-payment models, with `service-request.md` named as the one file still carrying the retired scope model. That framing is now stale on both counts: `service-request.md` was deleted outright in favour of `screens-unified/submit-application.md` (issue #50) — it was never reconciled, because it stopped existing — and every file in the current 14-screen set (`ui/screens/`) and the four-screen `ui/screens-unified/` package, along with `ui/validation-rules.md` and `ui/components.md`, has since been checked directly against both the unified-access model and the corrected two-timing payment model (`payments.md`), including a further correction pass on 2026-08-16 following the normalization of Services #12 and #18's payment timing. Nothing in this module's UI package still describes the retired role/scope model or an outdated payment timing.
