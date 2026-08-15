---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - real-estate-developer
  - ui-spec
---

# Screen: Escrow Details

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described two designs that disagreed on **page structure itself**, not merely on content: the Developer Principal / Director variant was a linear ten-section page, and the Escrow Liaison variant was a five-tab workspace with a persistent summary card and a right-hand alerts sidebar. Both are **retired**. This is one screen, and the structural conflict is resolved explicitly in [Notes](#notes) rather than by picking a side silently.

> **The balances on this screen are the project escrow account's, not a RERA-fee account.** See [escrow-management.md](escrow-management.md) for the full distinction. RERA service fees are paid per transaction through the shared platform payment gateway (issue #58) and have no bearing on anything here.

## Purpose

The detail view of a single project escrow account, opened from [Escrow Management](escrow-management.md). Covers the account, its financial institution, the construction milestone schedule, fund release history and requests, escrow documents, regulatory correspondence and the full activity log — with the controls to request releases, upload evidence and coordinate with the Account Trustee. Any user may do any of it.

## Layout

**Tabbed, with a persistent header and summary card above the tabs.**

```
Top Bar
↓
Escrow Header
↓
Escrow Summary Card + Quick Actions
↓
┌─ Tabs ────────────────────────────────────────────────┐
│ Overview · Fund Releases · Milestones · Documents ·    │
│ Regulatory History · Activity Log                     │
└───────────────────────────────────────────────────────┘
                                    ↕
                          Right Sidebar — Alerts & Reminders
```

## Sections

### Escrow Header

Escrow ID, project, financial institution, escrow status badge, release status badge.

**Actions:** **Request Fund Release** · **Upload Documents** · **Download Escrow Summary** · **View Applications**

**Reconciled 2026-08-15:** the linear variant's header offered view actions only. The full action set now applies to every user, subject to the account's own state.

### Escrow Summary Card + Quick Actions

Persistent above the tabs, from the tabbed variant: escrow account number, current balance, current milestone, last release, next scheduled milestone — with the Quick Actions row.

**Absorbed:** the linear variant's *Escrow Summary Cards* section covered the same figures as a card row. Merged into this one persistent card so the numbers stay visible while moving between tabs.

### Tab 1 — Overview

* **Project Information** — project, registration number, developer, unit counts, construction status.
* **Escrow Account Information** — account number, registration date, status, terms.
* **Financial Institution Information** — bank, branch, Account Trustee contact, agreement reference.
* **Financial Summary** — total deposited, total released, current balance, pending release value.
* **Responsible Parties** — named contacts against the account. *(Descriptive attribution, not access assignment.)*

**Absorbed 2026-08-15:** the linear variant's Sections 3, 4 and 5 (*Escrow Account Information*, *Project Information*, *Financial Institution Information*, plus *Responsible Parties*) and the tabbed variant's Overview groups. The linear variant carried more detail on the financial institution; the tabbed variant carried the Financial Summary. Both kept.

### Tab 2 — Fund Releases

Table of release requests: reference, milestone, requested amount, approved amount, request date, decision date, status, action.

**Actions** — governed by release status: Continue Draft · Edit · Submit · Respond to Query · View Details · Download Approval.

**Absorbed 2026-08-15:** the linear variant's *Fund Release History* (a read-only record) and the tabbed variant's *Fund Releases* tab (the same record plus request controls). The tabbed version is the superset.

Links to [fund-release-request.md](fund-release-request.md) and [fund-release-request-details.md](fund-release-request-details.md).

### Tab 3 — Milestones

Construction milestone schedule: milestone, planned date, actual date, release amount, verification status, evidence, action.

**Absorbed 2026-08-15:** the linear variant's *Milestone & Fund Release Timeline* was a combined stage tracker covering both milestones and releases. Splitting it follows the tabbed variant, since the two have different cardinality — a milestone may carry no release, and a release may be returned and resubmitted against the same milestone. The timeline *view* survives as the ordering of this tab.

### Tab 4 — Documents

Escrow documents by category — Escrow Agreement, Bank Confirmation Letter, Engineer Progress Certificate, Quantity Surveyor Report, Construction Progress Report, Site Inspection Report, Fund Release Documents, Financial Statements, Compliance Documents, Supporting Documents, Other.

Table with Upload / Replace / Preview / Resubmit actions governed by document status.

**Absorbed 2026-08-15:** the linear variant's *Escrow Documents* section (view/download only) and the tabbed variant's *Documents* tab (categories plus upload controls). The tabbed version is the superset.

### Tab 5 — Regulatory History

RERA review history against this escrow account: review round, reviewer, decision, date, remarks — together with any open queries and their response actions.

**Absorbed 2026-08-15** from the linear variant's *RERA Review History*, which the tabbed variant had no equivalent for. **This was the tabbed variant's one real omission**, and it is restored here as its own tab rather than folded into the Activity Log, where a decision record would be hard to find among routine events.

### Tab 6 — Activity Log

Chronological record of everything that has happened to this escrow account. Each entry shows who acted and what role they held at the time ([navigation.md](../../navigation.md#audit-trail-principle)).

**Absorbed** from the linear variant's *Activity Timeline* and the tabbed variant's *Activity Log* — the same section under two names.

### Right Sidebar — Alerts & Reminders

Milestone dates approaching, releases awaiting bank action, documents expiring, queries with due dates.

**Absorbed 2026-08-15** from the tabbed variant, the only one to define it. Backed by the **Alerts Sidebar** component recorded in [components.md](../components.md), which notes this as the component's single usage in the module. Retained — it is real content, and dropping it would have orphaned that component.

## Empty State

> This escrow account has no fund release requests yet. Request a release once a construction milestone is verified.

**Primary Button** — Request Fund Release

Applies to the Fund Releases tab. The Overview tab always renders, since account and institution details exist from registration onward.

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen — including the Alerts Sidebar, used only here.

## Validation

1. No tab, section, field or action on this screen is role-gated. What a user can do depends on the escrow account's and the release's state, never on who they are.
2. Users cannot modify approved or released fund requests; those records are read-only. A lifecycle rule, applying to every user equally.
3. The escrow account's status and each release's status are separate values and must not be conflated.
4. Balances and release figures come from the escrow system of record and must match [escrow-management.md](escrow-management.md) exactly.

## User Flow

```
Escrow Management
↓
Escrow Details
├─ Request Fund Release → Fund Release Request
├─ Fund Releases row → Fund Release Request Details
├─ Documents row → Document Details
├─ Regulatory History query → response flow
└─ Project link → Project Details
```

## Notes

* **The structural conflict, and how it was resolved.** The two variants did not merely differ in content — they were different page architectures. The Principal's was ten stacked sections; the Escrow Liaison's was five tabs plus a sidebar. Neither is a subset of the other, and no merge could preserve both.

  **Resolved in favour of the tabbed layout**, for reasons specific to this screen rather than a general preference:
  * The merged content runs to six substantial groupings. As a linear page that is a long scroll in which the Fund Releases table — the thing users come here to act on — sits below three information blocks.
  * The escrow record is genuinely multi-dimensional: account, milestones, releases and documents are related but separately navigable, which is what tabs are for.
  * The persistent summary card keeps the balance and current milestone visible from every tab, which the linear layout could not do at all.

  **What the linear layout contributed and kept:** its richer Financial Institution detail, its Responsible Parties block, and its RERA Review History — the last being content the tabbed variant lacked entirely, now restored as Tab 5. The linear ordering itself is gone.

  **Flagged:** this is a design decision made in the course of a documentation merge. If the client prefers the linear layout, the content mapping above is reversible — every tab corresponds to a former section — but the reverse move loses the persistent summary card.

* **Reconciliation — milestones and releases were one section, now two.** The linear variant combined them into a single *Milestone & Fund Release Timeline*. They have different cardinality (a milestone may have no release; a release may be resubmitted against one milestone), so combining them cannot represent the real relationship. Split, following the tabbed variant.

* **The Alerts & Reminders sidebar was single-sourced and is kept.** Same reasoning as "Suspended" in the project-status merge: single-sourced is not the same as redundant.

* **What was dropped, and why.** Only the linear page ordering, the view-only header actions, and the linear variant's note that "all operational escrow activities remain the responsibility of the Escrow Liaison" — a permission claim, already corrected once and now removed with the variant. Every information group, table, column and action from both variants is present above.
