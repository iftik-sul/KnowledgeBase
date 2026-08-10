---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - institution-profile
---

# Screen: Institution Profile

**Roles:** Institution Relationship Manager (`admin`) · all other roles (read)

The institution's own standing, staff and settlement preferences. Where registration Flow 5's provisioning becomes visible after the fact — every permission scope a staff member holds was granted here.

## Purpose

Let the Institution Relationship Manager maintain the institution's approved standing, provision and scope staff, and set the settlement preferences that other screens depend on (the low-balance threshold shown on [settlement-account.md](settlement-account.md) and the Institution Context Header). Give every other role read visibility into the same information, since approval expiry and staff scoping affect what they can do elsewhere in the module.

## Layout

```
Top Bar
↓
Institution Standing
↓
Tabs: Staff & Scopes | Settlement Preferences | Approval History
```

The Institution Context Header is suppressed here — this screen's own Institution Standing section is that same information, shown as the page's subject rather than a strip above it (consistent with [settlement-account.md](settlement-account.md)).

## Sections

### Section 1 — Institution Standing

* Institution legal name, type (Account Trustee / Auditing Company standing, where applicable), registration reference.
* Approval status badge — see [status-badges.md](../status-badges.md#institutional-approval-status).
* **Expiry countdown**, per answer B8's two-year validity term: neutral beyond 60 days, warning inside 60, error inside 14. Matches the Institution Context Header's own threshold, defined once here rather than twice.
* **Renew** action (routes to Service #1) shown inside the 60-day window; always visible, not conditionally hidden, so the IRM can renew early.
* **Cancel Approval** action (Service #2) and **Cancel Contract** (Service #18), both requiring confirmation.

### Section 2 — Staff & Scopes Tab

| Column | Description |
| :---- | :---- |
| Name | Staff member |
| Email | Contact |
| Scopes Held | `file`, `certify`, `escrow`, `audit`, `settlement`, `admin` — chips, per [validation-rules.md](../validation-rules.md#permission-scope) |
| Status | Invited · Active · Revoked |
| Added | Date provisioned |
| Action | Edit Scopes · Revoke |

**Row action — Edit Scopes** opens a scope-assignment panel: checkboxes for each of the six scopes, per registration Flow 5's requirement that the authorised representative confirm each staff member's scope before activation.

* **Provisioning validation:** assigning `audit` to a user who already holds `escrow` or `certify` is blocked with an explanation, and the reverse — assigning `escrow` or `certify` to a user who holds `audit` — is equally blocked. This is answer A1/D2's maker-checker mechanism combined with the audit-exclusivity rule proposed in PR #26, enforced at the point scopes are granted rather than left to institutional discretion.
* Scope changes take effect at the affected user's next sign-in and are written to the audit timeline (see [validation-rules.md](../validation-rules.md#permission-scope)).

**Page action:** Invite Staff Member — email, initial scope assignment, same provisioning validation as above.

### Section 3 — Settlement Preferences Tab

* **Low-Balance Threshold** — the amount below which the Settlement Account's Balance Card and the Institution Context Header switch to a warning treatment. Editable by `admin`, with a sensible platform default pre-filled. This is the setting [settlement-account.md](settlement-account.md) and [components.md](../components.md#balance-card) both reference as "the configured threshold" without defining where it is set — this screen is that definition.
* **Funding Authorisers** — which staff (beyond the IRM) may initiate a top-up, where the institution wants to delegate that beyond the `settlement` scope holder of record.

### Section 4 — Approval History Tab

| Column | Description |
| :---- | :---- |
| Date | Action date |
| Action | Approval Granted · Renewed · Cancelled · Contract Cancelled |
| Reference | Linked Service #1/#2/#18 application |
| Decision By | RERAN officer, where shown |

Read-only audit trail of the institution's own standing, separate from the Audit Timeline on individual applications.

## Empty State

Not applicable to Institution Standing (always populated once the institution exists). Applies to the Staff & Scopes tab before any delegated staff are invited:

**Message**

> No staff have been provisioned yet. The Institution Relationship Manager's own account is active by default; invite staff to delegate filing, certification, escrow, audit or settlement work.

**Primary Button:** Invite Staff Member

## Reused Components

See [components.md](../components.md). Uses Top Bar, Status Badge, Data Table, Audit Timeline, Buttons. Does **not** use the Institution Context Header — see Layout.

## Validation

See [validation-rules.md](../validation-rules.md#institutional-standing). Specific to this screen:

1. Only `admin` may edit scopes, invite staff, revoke access or change settlement preferences. All other roles see this screen fully but with no editable controls — a read view, not a disabled one.
2. The audit-exclusivity rule (`audit` vs. `escrow`/`certify`) is enforced at assignment time here, and cannot be bypassed by assigning scopes in a different order.
3. Revoking a scope does not retroactively invalidate that user's past certifications — the audit timeline on affected records is immutable.
4. An institution cannot revoke its own only `admin` holder without first designating a replacement, to avoid an institution locking itself out of provisioning.

## Role Variations

### Institution Relationship Manager

Full operation, as described.

### All other roles (Mortgage Officer, Account Trustee, Auditing Bureau Officer, any `certify` holder)

Read-only. See approval standing, the staff roster and scopes (relevant to understanding who else can act on what), and settlement preferences, but no edit controls anywhere on the screen. This matters most for a `certify` holder confirming they are not also barred from a scope combination, and for anyone checking whether the institution's approval is current before relying on it.

## User Flow

```
Dashboard
↓
Institution Profile
├─ Renew → Service Request (#1)
├─ Cancel Approval → Service Request (#2)
├─ Cancel Contract → Service Request (#18)
├─ Invite Staff Member → Scope Assignment → Staff & Scopes (Invited)
├─ Edit Scopes → Scope Assignment → Staff & Scopes (updated)
└─ Edit Low-Balance Threshold → Settlement Preferences (saved)
```

## Notes

* **The low-balance threshold now has a home.** Both the exemplar screens reference "the configured threshold" without saying where it is configured; this screen is the answer, and [validation-rules.md](../validation-rules.md) has been updated to point here — see the PR description for what changed and why.
* **B8's two-year validity is proposed, not sourced** — the structure (approvals expire and are renewed) is sourced from Service #1 being named "approval / renewal"; the specific duration is this module's own proposal.
* The audit-exclusivity rule remains unsourced (flagged in PR #26 as constraining institutional staffing without a source citation) — enforcing it in the UI does not resolve that; it makes the proposal concrete enough to evaluate.
* Staff provisioning itself (the invitation and identity-verification flow under registration Flow 5) is out of this module's scope per the module's own scope note; this screen covers only scope *assignment* after a staff member is already provisioned.
