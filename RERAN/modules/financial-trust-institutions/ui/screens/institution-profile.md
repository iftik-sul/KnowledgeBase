---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-19
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

**Access:** Any of the institution's four Group C roles — unified access, not scope-gated (`navigation.md`, confirmed 2026-08-14). Typically administered by the Institution Relationship Manager in practice.

The institution's own standing and staff roster.

> **Corrected 2026-08-15.** This screen previously gated every edit control behind an `admin` permission scope, and its Staff tab assigned and revoked six permission scopes (`file`, `certify`, `escrow`, `audit`, `settlement`, `admin`) per staff member, enforcing an audit-exclusivity rule at assignment time. All of that is retired. Every institution user has identical access; the Staff tab is now a roster for audit-trail attribution only, with no scopes to assign. The Settlement Preferences tab is removed entirely — there is no standing account, and so no low-balance threshold, left to configure. See [payment-history.md](payment-history.md) (formerly `settlement-account.md`) for the per-transaction payment record this institution now relies on instead.
>
> **Corrected 2026-08-19.** This file was dated 2026-08-15 and was never revisited on the 16th. It still described Services #12 and #18 as paying *after* RERA's decision, calling them "the two exceptions to the module's general pattern" — in Section 1 and again in the Notes. The client normalized both services to pay before RERA's decision on 2026-08-16, and `payments.md`, `payment-history.md`, `notifications.md`, `services-catalog.md`, `applications.md`, `status-badges.md` and `assisted-service-terminal.md` were all corrected at the time; this file was missed entirely. Both statements are corrected below, along with a link to `assisted-service-terminal.md#section-3a--payment-at-counter`, an anchor that ceased to exist when that file renamed Section 3a to Section 4 during the same correction.

## Purpose

Let any institution user maintain the institution's approved standing and staff roster. Every role sees and can edit the same information — role is attribution only, not a gate on who may administer the institution's profile.

## Layout

```
Top Bar
↓
Institution Standing
↓
Tabs: Staff Records | Approval History
```

**Corrected 2026-08-15** — the Settlement Preferences tab is removed. Two tabs remain, not three.

The Institution Context Header is suppressed here — this screen's own Institution Standing section is that same information, shown as the page's subject rather than a strip above it.

## Sections

### Section 1 — Institution Standing

* Institution legal name, type (Account Trustee / Auditing Company standing, where applicable), registration reference.
* Approval status badge — see [status-badges.md](../status-badges.md#institutional-approval-status).
* **Expiry countdown**, per answer B8 (confirmed 2026-08-15, client decision — renewing, per-approval-term structure; two-year validity remains a proposal): neutral beyond 60 days, warning inside 60, error inside 14. Matches the Institution Context Header's own threshold, defined once here rather than twice.
* **Renew** action (routes to Submit Application, pre-populated with Service #1) shown inside the 60-day window; always visible, not conditionally hidden, so renewal can happen early. **Corrected 2026-08-15** — Service #1 now pays upfront (`open-questions.md` B11); Renew routes into the same checkout-before-lodging flow as any other service request.
* **Cancel Approval** action (Service #2 — confirmed 2026-08-15 to carry no fee at all) and **Cancel Contract** (Service #18 — pays before RERA's decision, at the counter, the same as every other counter-paid service; see `payments.md`), both requiring confirmation.

**Corrected 2026-08-19** — the Cancel Contract bullet previously described Service #18 as paying "after RERA's decision, at the counter, one of the two exceptions to the module's general pattern." That exception was retired by client decision on 2026-08-16; #18 and #12 both pay before RERA's decision now, and no Group C service pays after one. See the banner note above.

### Section 2 — Staff Records Tab

| Column | Description |
| :---- | :---- |
| Name | Staff member |
| Email | Contact |
| Status | Invited · Active · Removed |
| Added | Date provisioned |
| Action | Remove |

**Corrected 2026-08-15** — this tab previously read "Staff & Scopes," with a Scopes Held column (six scope chips) and an Edit Scopes row action opening a scope-assignment panel. All of that is removed. Every staff member has identical system access from the moment they're added — this tab is now purely who is on the institution's staff list, for audit-trail attribution (`navigation.md#audit-trail-principle`), not about granting capability.

**Page action:** Invite Staff Member — email only. No scope assignment, since there is nothing to assign.

### Section 3 — Approval History Tab

| Column | Description |
| :---- | :---- |
| Date | Action date |
| Action | Approval Granted · Renewed · Cancelled · Contract Cancelled |
| Reference | Linked Service #1/#2/#18 application |
| Decision By | RERAN officer, where shown |

Read-only audit trail of the institution's own standing, separate from the Audit Timeline on individual applications. **Corrected 2026-08-15** — renumbered from Section 4 to Section 3, since the Settlement Preferences tab that previously sat between this and Staff Records is removed.

## Empty State

Not applicable to Institution Standing (always populated once the institution exists). Applies to the Staff Records tab before any delegated staff are invited:

**Message**

> No staff have been provisioned yet. The Institution Relationship Manager's own account is active by default; invite staff to add them to the institution's roster.

**Primary Button:** Invite Staff Member

**Corrected 2026-08-15** — previously referenced delegating "filing, certification, escrow, audit or settlement work" by scope. There is nothing to delegate by scope any more; every staff member gets full access on being added.

## Reused Components

See [components.md](../components.md). Uses Top Bar, Status Badge, Data Table, Audit Timeline, Buttons. Does **not** use the Institution Context Header — see Layout.

## Validation

See [validation-rules.md](../validation-rules.md#institutional-standing). Specific to this screen:

1. **Corrected 2026-08-15** — previously restricted editing to the `admin` scope, with every other role seeing a read view. Every institution user now has full edit access — invite staff, remove staff, renew or cancel approval, cancel contract.
2. **Removed 2026-08-15.** The audit-exclusivity rule (`audit` vs. `escrow`/`certify`) is retired along with the scopes it constrained.
3. Removing a staff member does not retroactively invalidate that user's past certifications — the audit timeline on affected records is immutable.
4. **Removed 2026-08-15.** The "an institution cannot revoke its own only `admin` holder" rule no longer applies — there is no `admin` scope, and every staff member has identical standing.

## Role Variations

**Corrected 2026-08-15 — this section is removed.** Every institution user has full access to every section of this screen. There is no per-role or per-scope variation left to describe.

## User Flow

```
Dashboard
↓
Institution Profile
├─ Renew → Submit Application (#1)
├─ Cancel Approval → Submit Application (#2)
├─ Cancel Contract → Submit Application (#18)
└─ Invite Staff Member → Staff Records (Invited)
```

**Corrected 2026-08-15, second pass** — previously named "Service Request" as the destination screen, deleted in favour of Submit Application (issue #50).

## Notes

* **B8's renewing structure is confirmed; the two-year duration specifically remains a proposal** (`open-questions.md` B8, confirmed 2026-08-15). The structure — approvals expire and are renewed — is sourced from Service #1 being named "approval / renewal"; the specific duration is this module's own proposal.
* **The Settlement Preferences tab is gone, not relocated.** There is no low-balance threshold, funding authoriser list, or any other standing-account setting left to configure anywhere in this module — see [payments.md](../../payments.md) and `open-questions.md` B1.
* **Cancel Contract (#18) pays before RERA's decision, at the counter, like every other counter-paid Group C service.** Confirming the cancellation here doesn't collect payment — the customer pays at the counter as part of lodging, before RERA reviews the application, per [payments.md](../../payments.md) and [assisted-service-terminal.md](assisted-service-terminal.md#section-4--payment-at-counter). **Corrected 2026-08-19** — this bullet previously read "one of two Group C services (with #12) that pays after RERA's decision, not before," and linked to a `#section-3a--payment-at-counter` anchor that no longer exists. Both were left behind by the 2026-08-16 normalization; see the banner note at the top of this file.
* Staff provisioning itself (the invitation and identity-verification flow under registration Flow 5) is out of this module's scope per the module's own scope note; this screen covers only who is on the roster, not the invitation/verification mechanics.
