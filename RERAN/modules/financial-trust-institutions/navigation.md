---
project: RERAN
module: financial-trust-institutions
type: navigation
status: current
updated: 2026-08-14
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

Group C now works the same way Group B does: one sidebar, identical for every user of a verified institution account, whatever their role. What still differs from Group B is not the access model — that's now identical in kind — but the *reason* roles are documented at all here. Group B roles determine access; Group C roles exist purely as an audit-trail attribution field, recording who performed an action and what role they held at the time. See [roles-and-responsibilities.md](roles-and-responsibilities.md) for the role descriptions and how they feed the audit trail.

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
* Settlement Account
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

Every role lands on Dashboard, with identical access to its content. Only the suggested primary call to action differs, as a convenience default rather than an access restriction:

| Role | Primary call to action |
| :---- | :---- |
| Mortgage Officer | New Service Request |
| Institution Relationship Manager | Whichever of approval renewal or settlement shortfall is more urgent; otherwise institution overview |
| Account Trustee | Oldest escrow request awaiting assessment |
| Auditing Bureau Officer | Nearest reporting obligation |

**Kept, reworded.** These CTAs describe what each role *typically* does first — not what they are limited to. Any user can act on any queue from the Dashboard regardless of which CTA is shown for their role. Whether a unified dashboard should instead show one shared CTA for everyone is a design question this issue doesn't decide; flagging it here rather than resolving it unilaterally. The certification queue count on the Dashboard — previously described as visible "regardless of role" because of the `certify` scope — is now simply the institution-wide count, visible to everyone, since certification is not scope-gated at all.

---

## External Access

**Trustee Centre operators (Group G)** reach Group C services through [ui/screens/assisted-service-terminal.md](ui/screens/assisted-service-terminal.md), operating on a walk-in customer's behalf under answer C2. They are not Group C users, do not hold Group C roles, and do not appear in the sidebar above. Their per-operator transaction permissions are provisioned under registration Flow 7 and belong to Group G's navigation when those interfaces are written. **Unaffected by this change** — Group G's access model is outside issue #38's scope and is not addressed by the client decision above.

---

## Superseded By This Document

Until 2026-08-14, this document described a role × permission-scope matrix: six permission scopes (`file`, `certify`, `escrow`, `audit`, `settlement`, `admin`), each provisioned per staff member under registration Flow 5, gating which menu items a given user could see; a maker ≠ checker access rule; and an `audit`-exclusivity rule barring a user from holding `audit` alongside `escrow` or `certify`. All of that is **retired**, not demoted to optional detail, per the client decision above. See [roles-and-responsibilities.md](roles-and-responsibilities.md#how-they-work-together) for how certification now works as an unrestricted action, attributed by role in the audit trail rather than gated by scope.

**Not yet reconciled.** `ui/screens/*.md` (13 files), `ui/validation-rules.md`, and `ui/components.md` still describe the retired role/scope model and cross-reference this document's previous framing. Reconciling them against the unified model is explicitly out of scope for issue #38 and is tracked as a separate, later pass — those files are left exactly as they were.
