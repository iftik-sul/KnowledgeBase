---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/role-workflows.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - dashboard
---

# Screen: Dashboard

**Roles:** Mortgage Officer · Institution Relationship Manager (`admin`/`settlement`) · Account Trustee (`escrow`) · Auditing Bureau Officer (`audit`) · any user holding `certify`

The landing screen for every Group C user. What it shows is not a smaller version of one design — the four roles do different jobs and the dashboard reflects that, not a shared shell with four label swaps.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations). In one sentence each: the Mortgage Officer needs to see work in hand; the Institution Relationship Manager needs to see institutional exposure; the Account Trustee needs to see queue state; the Auditing Bureau Officer needs to see reporting obligations coming due.

## Layout

Layout differs by role — see [Role Variations](#role-variations). Only the Top Bar and the certifier-scope overlay (below) are common to all four.

## Sections

Section content is entirely role-specific — see [Role Variations](#role-variations). Two things sit outside the per-role sections:

### Certifier Scope Overlay

Any user holding the `certify` scope — regardless of role — sees a **Certification Queue** count badge in the same position on their dashboard, linking to [internal-certification-queue.md](internal-certification-queue.md). This is a scope-driven addition to whichever role dashboard the user has, not a fifth dashboard (answer A1: certification is a permission scope, not a role).

### Institution Context Header

Shown to every role except where a role's own dashboard already leads with the same information (Institution Relationship Manager — see below). Carries approval standing and settlement position; see [components.md](../components.md#institution-context-header).

## Empty State

Empty state differs by role — see [Role Variations](#role-variations). There is no shared "no data" message: what "nothing to do" means is different for each role and each says so.

## Reused Components

See [components.md](../components.md). Common across all four: Top Bar, Institution Context Header (where shown), KPI Summary Cards, Status Badge, Buttons. Role-specific components are listed under each variation.

## Validation

See [validation-rules.md](../validation-rules.md#permission-scope). The dashboard itself performs no actions; every card and list item routes to a screen that enforces its own scope check. A card is not rendered if the user holds no scope that would let them act on what it shows, except where the card is explicitly read-only oversight (Institution Relationship Manager's Trustee Workload and Compliance summaries).

## Role Variations

### Mortgage Officer

**Purpose:** Surface work in hand — what needs filing, what is waiting on certification, what RERAN has queried, and what is about to settle.

**Layout**

```
Top Bar
↓
Institution Context Header
↓
Work Summary Cards
↓
My Applications (filtered)
↓
Settlement Watch
```

**Sections**

1. **Work Summary Cards** — Draft, Pending Internal Certification, Submitted, Information Requested, Approved — Awaiting Payment, Completed This Month. Selecting a card filters the list below.
2. **My Applications** — the officer's own filings only (not institution-wide), reusing the Applications table columns from [applications.md](applications.md), capped at ten rows with a link to the full list.
3. **Settlement Watch** — read-only: which of the officer's own approved transactions are awaiting settlement, and their expiry countdown. No Fund Account or Settle action here — see [settlement-account.md](settlement-account.md#role-variations).

**Empty State**

> No applications yet. Start a service request to register a mortgage, finance lease, or title transaction.

**Primary Button:** New Service Request

**Reused Components:** KPI Summary Cards, Data Table (own rows only), Status Badge, Buttons.

**Primary call to action:** New Service Request (per [navigation.md](../../navigation.md#landing-after-login)).

### Institution Relationship Manager

**Purpose:** Give institution-wide oversight of the two things that block everyone else's work — approval standing and settlement position — plus staff activity and volume.

**Layout**

```
Top Bar
↓
Institution Standing & Settlement (replaces Institution Context Header — this role's dashboard leads with it)
↓
Institution-Wide Volume
↓
Staff Activity
↓
Renewal & Settlement Actions
```

**Sections**

1. **Institution Standing & Settlement** — approval status and expiry countdown (see [status-badges.md](../status-badges.md#institutional-approval-status)), and the Settlement Account Balance Card (see [components.md](../components.md#balance-card)). This replaces the generic Institution Context Header because for this role the header's content *is* the dashboard's subject, not a strip above it.
2. **Institution-Wide Volume** — applications by status across every Mortgage Officer at the institution, not filtered to any one filer.
3. **Staff Activity** — roster size, active permission scopes, staff invited but not yet activated. Links to [institution-profile.md](institution-profile.md).
4. **Renewal & Settlement Actions** — surfaces whichever is more urgent: approval renewal (Service #1) or a settlement shortfall against committed fees, per [navigation.md](../../navigation.md#landing-after-login). Where neither is urgent, this section shows the institution overview instead.

**Empty State**

> No institution activity yet. Once staff begin filing service requests, institution-wide volume and settlement activity will appear here.

**Primary Button:** varies — Renew Approval, or Fund Settlement Account, or (where neither is urgent) View Institution Profile.

**Reused Components:** Balance Card, KPI Summary Cards, Data Table (institution-wide), Status Badge, Buttons.

### Account Trustee

**Purpose:** Show queue state for developer escrow requests — this role owns none of the eighteen Group C services and its dashboard reflects that; there is no "my applications" section at all.

**Layout**

```
Top Bar
↓
Institution Context Header
↓
Escrow Queue Summary Cards
↓
Oldest Awaiting Assessment
↓
Trust Accounts Summary
```

**Sections**

1. **Escrow Queue Summary Cards** — a condensed version of the six KPI cards on [escrow-request-queue.md](escrow-request-queue.md#section-1--queue-summary-cards): Awaiting Assessment, Under Assessment, Breaching SLA. The full six live on the queue screen; the dashboard shows only the three that indicate work outstanding.
2. **Oldest Awaiting Assessment** — the single request that has waited longest, shown as a call-to-action card rather than a table row, because the queue's failure mode is a request aging quietly.
3. **Trust Accounts Summary** — count of accounts under management, count with an overdue statement, count Flagged. Links to [trust-accounts.md](trust-accounts.md).

**Empty State**

> No escrow requests are awaiting assessment. Requests routed from developers will appear in the Escrow Requests queue.

**Primary Button:** Open Escrow Request Queue

**Reused Components:** KPI Summary Cards, Status Badge, Buttons.

**Primary call to action:** Oldest escrow request awaiting assessment (per [navigation.md](../../navigation.md#landing-after-login)) — where none is outstanding, the button falls back to Open Escrow Request Queue.

### Auditing Bureau Officer

**Purpose:** Show reporting obligations coming due — this role's work is periodic and deadline-driven, not inbound-queue-driven, so the dashboard is organized around dates rather than a work queue.

**Layout**

```
Top Bar
↓
Institution Context Header
↓
Reporting Obligations
↓
Open Findings
↓
Trust Account Audit Flags
```

**Sections**

1. **Reporting Obligations** — the same banded card set as [compliance-reports.md](compliance-reports.md#section-1--reporting-obligations): Reports Due, Overdue, Accounts Statement Overdue. The dashboard shows these because they are what the role's day is organized around.
2. **Open Findings** — count and nearest-severity summary of unresolved findings raised against trust accounts.
3. **Trust Account Audit Flags** — accounts currently Flagged, read-only. Links to [trust-accounts.md](trust-accounts.md).

**Empty State**

> No reporting obligations are currently due. Reports and findings will appear here as trust accounts under this institution's trusteeship generate them.

**Primary Button:** Open Compliance Reports

**Reused Components:** KPI Summary Cards, Status Badge, Buttons.

**Primary call to action:** Nearest reporting obligation (per [navigation.md](../../navigation.md#landing-after-login)) — routes directly to that obligation's Report Composer or Finding Detail.

## User Flow

```
Login
↓
Dashboard (role-specific — see above)
├─ Mortgage Officer: → Service Request / Applications / Settlement Account (read)
├─ Institution Relationship Manager: → Institution Profile / Settlement Account / Applications (institution-wide)
├─ Account Trustee: → Escrow Request Queue / Escrow Request Details / Trust Accounts
├─ Auditing Bureau Officer: → Compliance Reports / Trust Accounts (read)
└─ Any role holding `certify`: → Internal Certification Queue
```

## Notes

* **Four dashboards, not one dashboard with four labels.** This was the explicit defect in the previous version — Role Variations there read identically across every screen in the module, including this one. The differences above are structural (different Layout diagrams, different sections, different empty states), not cosmetic.
* The Certifier Scope Overlay is additive to whichever of the four role dashboards a `certify`-holding user has; it does not create a fifth variant.
* Exact card thresholds (what counts as "nearest," how many rows a summary table shows before linking out) are **Proposed** — reasonable defaults, not sourced.
* Institution Relationship Manager's landing action logic ("whichever is more urgent") needs a concrete urgency rule before build — this document does not propose one, since it depends on the approval-expiry and settlement-expiry windows both being client-configurable (answers B3, B8).
