---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/ui/screens/applications.md"
  - "RERAN/modules/real-estate-developer/ui/screens/projects.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registrations.md"
  - "RERAN/modules/real-estate-developer/ui/screens/sales-and-disclosures.md"
  - "RERAN/modules/real-estate-developer/ui/screens/escrow-management.md"
  - "RERAN/modules/real-estate-developer/ui/screens/escrow-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/documents.md"
  - "RERAN/modules/real-estate-developer/ui/screens/document-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/help-and-support.md"
  - "RERAN/modules/real-estate-developer/ui/screens/notifications.md"
  - "RERAN/modules/real-estate-developer/ui/screens/reports.md"
  - "RERAN/modules/real-estate-developer/service-flows/feature-04-escrow-management.md"
  - "RERAN/modules/real-estate-developer/service-flows/feature-05-fund-release-request.md"
tags:
  - real-estate-developer
  - ui-spec
  - status
---

# Status Badges

The status vocabulary for this module.

**No colour coding survived migration.** The source material never specifies actual colours or hex values for any status badge — every screen only says something like "use the shared status badge component," "badge colours follow the existing RERA design system," or "use the platform's standard status badges." There is nothing to consolidate on the colour side; only the state *labels* are consolidated below.

**Status badges vs. workflow stages.** This file covers the *status badge* shown on a record in a table or header (e.g. "Approved," "Rejected"). It does **not** cover the stage names used by the horizontal Progress Tracker component on form/detail screens, which describe a fixed pipeline of steps rather than a badge vocabulary.

> **Corrected 2026-08-15, second pass.** This file previously reported six of eight categories below as unresolved "⚠ Conflict" between role variants, carried over unchanged from before the screen rebuild — even though every screen this file is `derived_from` had already been rebuilt into a single unified screen, several of which (`sales-and-disclosures.md`, `escrow-management.md`) explicitly link back here as the authoritative source for a resolved vocabulary this file wasn't actually providing. Only Project Status and Property Registration Status had been properly resolved. The other six are resolved below, using the rebuilt screens' own filter lists and row-action vocabularies where a screen stated one directly, and the same union-and-reconcile method used for Project Status where it didn't. Document Status remains genuinely unresolved — see that section — because the rebuilt `documents.md` explicitly says so, not because it was missed.

> **Corrected again 2026-08-16 — Escrow Status and Fund Release Status were themselves superseded, and this file never caught up.** The "Resolved" vocabularies below for both categories were taken directly from `escrow-management.md`'s own UI filter list — which is exactly the mistake this file's 2026-08-15 correction was written to fix everywhere else. A later, independent audit (checking all six escrow service files — #8, #9, #10, #12, #20, #21 — directly against source) found that filter list does **not** match what those service files actually source. The genuinely sourced vocabulary, now the one `feature-04-escrow-management.md` and `feature-05-fund-release-request.md` use, is: `Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → [service-specific terminal state]`, plus additional statuses `Information Requested / Returned / Rejected`. See both sections below for the corrected vocabulary and how the old filter-list terms map onto it.

## Project Status

Used on [projects.md](screens/projects.md).

**Resolved 2026-08-15 — nine states:**

`Draft` · `Submitted` · `Under Review` · `Information Requested` · `Returned` · `Approved` · `Rejected` · `Suspended` · `Completed`

> **How this was resolved.** Two former role variants of `projects.md` disagreed: Developer Principal / Director (6 states, including "Pending Review" and "Suspended") vs. Project Registration Officer (8 states, including "Submitted," "Under Review," "Information Requested," "Returned"). Union of both lists; "Pending Review" merged into "Under Review" as a duplicate label; "Suspended" kept though single-sourced, since it was the only way to represent a project on hold.

## Property Registration Status

Used on [property-registrations.md](screens/property-registrations.md) and referenced from [property-registration-details.md](screens/property-registration-details.md).

**Resolved 2026-08-15 — seven states:**

`Draft` · `Submitted` · `Under Review` · `Information Requested` · `Returned` · `Approved` · `Rejected`

> **How this was resolved.** A clean subset case: the Project Registration Officer variant's 7 states included everything the Principal variant's 6 had, plus "Returned." Resolved to the 7-state union.

## Application Status

Used on [applications.md](screens/applications.md).

**Resolved 2026-08-15, second pass — eight states:**

`Draft` · `Submitted` · `Under Review` · `Information Requested` · `Returned` · `Approved` · `Rejected` · `Withdrawn`

> **How this was resolved.** The former Developer Principal / Director variant (7 states) had a single "Pending Additional Information" state where the three operational variants (8 states, identical across all three) split this into "Information Requested" and "Returned" — two genuinely different situations (RERA has a question, vs. RERA sent the application back for correction) that the Principal's single state collapsed. Resolved to the fuller 8-state operational list, which `applications.md`'s own rebuilt Row Actions table confirms directly (Draft · Submitted/Under Review · Information Requested · Returned · Approved · Rejected). "Withdrawn" was present, unchanged, in every former variant and is retained even though the rebuilt screen's own Row Actions table doesn't give it a distinct action row — an application the developer withdrew has nothing further to action, which is why it has no listed action, not evidence the state was dropped.

## Sales & Disclosure Status

Used on [sales-and-disclosures.md](screens/sales-and-disclosures.md) and referenced from [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md). This module tracks **two separate statuses** per sale — the sale's own lifecycle, and the regulatory disclosure's lifecycle — documented separately in the source and kept separate here.

### Sales Status

**Resolved 2026-08-15, second pass — five states:**

`Draft` · `Reserved` · `Sold` · `Completed` · `Cancelled`

> **How this was resolved.** Clean subset: the former Sales & Disclosure Officer variant (5 states) added only "Draft" to the Developer Principal / Director variant's 4. The rebuilt `sales-and-disclosures.md` confirms "Draft Sale" is a real, actionable state in its own Row Actions table (Continue Sale Entry · Edit · Delete), so it is kept.

### Disclosure Status

**Resolved 2026-08-15, second pass — seven states:**

`Disclosure Pending` · `Draft` · `Submitted` · `Under Review` · `Information Requested` · `Returned` · `Approved` · `Rejected`

> **How this was resolved.** The former variants disagreed more sharply here than on any other category: Developer Principal / Director had 6 states including "Not Submitted"; Sales & Disclosure Officer had 8 including "Not Started," "Draft," and "Information Requested" as a state the Principal's variant had no equivalent for at all. `sales-and-disclosures.md`'s own rebuilt Row Actions table uses **"Disclosure Pending"** as the label for a sale with no disclosure yet started — this becomes the resolved name for the initial state, replacing both "Not Submitted" and "Not Started" rather than picking one of the two old labels. Every other state from the fuller 8-state variant is kept, since the rebuild's Row Actions table shows distinct handling for Draft, Submitted/Under Review, and Information Requested/Returned as separate real situations.

## Escrow Status

Used on [escrow-management.md](screens/escrow-management.md).

**Corrected 2026-08-16 — superseded the 2026-08-15 resolution below.** This category's actual, sourced status flow is the same one used across all six escrow services: `Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → Active` (the terminal state for escrow account activation specifically — see [service-08-activate-escrow-account.md](../service-flows/service-08-activate-escrow-account.md)), plus `Information Requested / Returned / Rejected`. This is what the **status badge** shown on an escrow account should reflect.

**`escrow-management.md`'s own Filters section (`Pending Registration · Active · Suspended · Closed`) is retained as-is, as UI filter options** — those remain useful ways to narrow the account list — **but are not the sourced status flow**, and should not be read as such. "Pending Registration" spans everything from Draft through RERA Escrow Audit; "Suspended" and "Closed" describe account-lifecycle states after activation that the six-service status flow doesn't itself define and that need their own source or client confirmation if they're to be more than filter labels.

> **Superseded 2026-08-15 pass, kept for the record.** That pass took the filter list itself (`Pending Registration · Active · Suspended · Closed`) as the resolved status badge vocabulary, reasoning that `escrow-management.md`'s own Filters section "states this list directly." That was the same mistake this file's earlier 2026-08-15 correction had just finished fixing elsewhere — treating a UI screen's own filter values as if they were the sourced status flow, rather than checking the underlying service files directly. See [feature-04-escrow-management.md](../service-flows/feature-04-escrow-management.md) for the full correction and source citation.

## Fund Release Status

Used on [escrow-management.md](screens/escrow-management.md) and [escrow-details.md](screens/escrow-details.md).

**Corrected 2026-08-16 — superseded the 2026-08-15 resolution below.** This category's actual, sourced status flow, checked directly against Services #10 and #12's own files, is: `Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → Released`, plus `Information Requested / Returned / Rejected`. This is what the **status badge** shown on a fund release request should reflect — and is also the vocabulary [feature-05-fund-release-request.md](../service-flows/feature-05-fund-release-request.md) and [feature-13-profit-withdrawal-request.md](../service-flows/feature-13-profit-withdrawal-request.md) now use.

**`escrow-management.md`'s own Filters section (`No Request · Pending Approval · Under Review · Approved · Released · Returned · Rejected`) is retained as-is, as UI filter options** — but is not the sourced status flow. Where the two vocabularies overlap (`Approved`, `Released`, `Returned`, `Rejected`), the terms happen to match; where they don't, the filter list's terms map onto the sourced flow as follows:

| Old filter term | Sourced status badge |
| :---- | :---- |
| No Request | *(not applicable — a request that doesn't yet exist has no status badge)* |
| Pending Approval | Draft / Submitted, depending on whether it has been sent for review yet |
| Under Review | Trustee Review or RERA Escrow Audit, depending on which stage the request has reached |

> **Superseded 2026-08-15 pass, kept for the record.** That pass resolved this category the same way as Escrow Status above — taking `escrow-management.md`'s own Filters section as the resolved vocabulary, on the reasoning that it was "the single canonical source both screens link to." Same underlying mistake: a UI filter list, not a check against the six escrow service files' own sourced status flows. `fund-release-request.md`'s detailed 9-stage progress tracker (`Draft → ... → Under Bank Review → Under RERA Review → Approved → Funds Released`) is the UI screen's own step-by-step view and maps onto this corrected vocabulary the same way — see that screen's own file for the mapping, once corrected there.

### Milestone Verification Status

Used on [escrow-details.md](screens/escrow-details.md) (Milestones tab). A third, distinct status axis from both of the above — a construction milestone can be "Verified" while its associated fund release is still "Under Review."

**Unaffected by this pass — five states:**

`Pending` · `In Progress` · `Submitted` · `Verified` · `Returned`

No conflict was ever recorded for this vocabulary; it was found as a single, consistent list during the original consolidation and needs no resolution.

## Document Status

Used on [documents.md](screens/documents.md) and [document-details.md](screens/document-details.md).

**Still genuinely unresolved — not a gap in this pass.** The rebuilt `documents.md` states directly: *"The source uses three different, unreconciled vocabularies for document status; that conflict is recorded there and is not resolved by this rebuild — it predates the role variants and survives the merge unchanged."* This is the one category where the screen rebuild deliberately left the underlying conflict in place, correctly, because it isn't a role-variant artifact the unification could resolve — it needs source clarification.

**Documents list screen — "Verification Status":** `Draft` · `Pending Verification` · `Verified` · `Information Requested` · `Returned` · `Rejected` · `Expired` (7 states, the fuller of two former variants — the shorter 5-state variant is a subset missing "Draft" and "Information Requested").

**Documents list screen — "Expiry Status"** (a separate, smaller vocabulary for proximity to expiry, not verification state): `Valid` · `Expiring Soon` · `Expired` (3 states).

**Document Details screen — "Regulatory Verification"** (a narrower, review-outcome-only vocabulary — no "Draft," "Expired," or "Returned"): `Pending Review` · `Information Requested` · `Verified` · `Rejected` (4 states).

Reported as three separate, unreconciled lists. Resolving this needs a client decision on which vocabulary — or whether a genuinely reconciled fourth one — is correct; it is not something this file can resolve on its own reasoning the way the other six categories were.

## Generic (not tied to a specific business entity)

### Ticket Status (Help & Support)

**Resolved 2026-08-15, second pass — seven states:**

`Draft` · `Open` · `In Progress` · `Waiting for Customer` · `Escalated` · `Resolved` · `Closed`

> **How this was resolved.** Three former variants disagreed: Developer Principal / Director (6 states, no "Draft"); Project Registration Officer / Sales & Disclosure Officer (7 states, identical, adds "Draft"); Escrow Liaison (5 states, no "Draft," no "Escalated," and "Waiting for User" instead of "Waiting for Customer"). `help-and-support.md`'s own rebuild does not enumerate ticket states explicitly, so this follows the same union method used for Project Status: "Waiting for User" merged into "Waiting for Customer" as a naming variant (3-of-3 role groups used the latter); "Draft" kept, since a ticket being drafted before creation is a real, distinct state the fuller two variants agree on; "Escalated" kept — its absence from only the Escrow Liaison variant matches this same screen's own documented pattern elsewhere ("the Escrow Liaison variant's omission reads as a gap, not a restriction," stated three separate times in `help-and-support.md`'s own Notes for other sections), not a considered exclusion.

### Notification Status

[notifications.md](screens/notifications.md) — a per-notification read state, consistent across all roles: `Unread` · `Read` · `Archived` (3 states). No conflict, unaffected by this pass.

### Company / RERA License Status

[company-profile.md](screens/company-profile.md) — the developer organization's own RERA license status, distinct from any project's or application's status: `Active` · `Pending Renewal` · `Expiring Soon` · `Suspended` · `Expired` (5 states). No conflict, unaffected by this pass.

### Report Generation Status

[reports.md](screens/reports.md) — the processing state of a generated report file: `Processing` · `Completed` · `Failed` · `Expired` (4 states). No conflict, unaffected by this pass.
