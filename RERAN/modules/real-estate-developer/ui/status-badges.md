---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-09
derived_from:
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
tags:
  - real-estate-developer
  - ui-spec
  - status
---

# Status Badges

The status vocabulary for this module.

**No colour coding survived migration.** The source material never specifies actual colours or hex values for any status badge — every screen only says something like "use the shared status badge component," "badge colours follow the existing RERA design system," or "use the platform's standard status badges." The one exception ([property-registrations.md](screens/property-registrations.md), Principal's version) says "Badge colors follow the existing RERA design system" — a pointer to a design system that isn't itself documented in this source. There is nothing to consolidate on the colour side; only the state *labels* are consolidated below.

**Conflicts are reported, not resolved**, per this batch's instructions. Where two screens (or two role variants of the same screen) list different states for what is nominally the same status, both lists are shown in full and the difference is called out — no state has been silently added, dropped, or renamed to make the lists agree.

**Status badges vs. workflow stages.** This file covers the *status badge* shown on a record in a table or header (e.g. "Approved," "Rejected"). It does **not** cover the stage names used by the horizontal Progress Tracker component on form/detail screens (e.g. "Initial Validation → Technical Review → Compliance Review → Final Approval"), which describe a fixed pipeline of steps rather than a badge vocabulary. Those stage lists are screen-specific and remain in each screen's own Layout/Sections content.

## Project Status

Used on [projects.md](screens/projects.md).

**⚠ Conflict — the Principal's and Registration Officer's lists disagree, not just in ordering:**

- **Developer Principal / Director:** Draft, Pending Review, Approved, Rejected, Suspended, Completed (6 states)
- **Project Registration Officer:** Draft, Submitted, Under Review, Information Requested, Returned, Approved, Rejected, Completed (8 states)

The Principal's list has no "Submitted," "Under Review," "Information Requested," or "Returned" states — it also has "Pending Review" and "Suspended," which the Registration Officer's list lacks entirely. These aren't reconcilable by assuming one is a subset of the other; "Pending Review" and "Suspended" appear nowhere in the Registration Officer's list, and "Suspended" in particular describes a state (a project put on hold) that isn't representable at all in the Registration Officer's vocabulary. Flagged as-is; not resolved here.

## Property Registration Status

Used on [property-registrations.md](screens/property-registrations.md) and referenced from [property-registration-details.md](screens/property-registration-details.md).

**⚠ Conflict — one state present only in the Registration Officer's list:**

- **Developer Principal / Director:** Draft, Submitted, Under Review, Information Requested, Approved, Rejected (6 states)
- **Project Registration Officer:** Draft, Submitted, Under Review, Information Requested, Returned, Approved, Rejected (7 states — adds "Returned")

The Principal's version notes "Badge colors follow the existing RERA design system" (see note above); the Registration Officer's version doesn't repeat that note but uses the same label set otherwise, plus "Returned."

## Sales & Disclosure Status

Used on [sales-and-disclosures.md](screens/sales-and-disclosures.md) and referenced from [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md). This module tracks **two separate statuses** per sale — the sale's own lifecycle, and the regulatory disclosure's lifecycle — documented separately in the source and kept separate here.

### Sales Status

**⚠ Conflict:**

- **Developer Principal / Director:** Reserved, Sold, Completed, Cancelled (4 states)
- **Sales & Disclosure Officer:** Draft, Reserved, Sold, Completed, Cancelled (5 states — adds "Draft")

### Disclosure Status

**⚠ Conflict — the two lists barely overlap in vocabulary:**

- **Developer Principal / Director:** Not Submitted, Submitted, Under Review, Approved, Returned, Rejected (6 states)
- **Sales & Disclosure Officer:** Not Started, Draft, Submitted, Under Review, Information Requested, Returned, Approved, Rejected (8 states)

The Principal's "Not Submitted" and the Officer's "Not Started" appear to describe the same initial state under different names — that's a naming conflict, not a state the other list lacks. The Officer's list additionally has "Draft" and "Information Requested," which the Principal's list has no equivalent for at all.

## Escrow Status

Used on [escrow-management.md](screens/escrow-management.md).

**⚠ Conflict:**

- **Developer Principal / Director:** Active, Pending, Milestone Under Review, Funds Released, Suspended, Closed (6 states)
- **Escrow Liaison:** Pending Registration, Active, Suspended, Closed (4 states)

The Escrow Liaison's list is shorter and uses "Pending Registration" where the Principal's uses plain "Pending"; the Principal's "Milestone Under Review" and "Funds Released" states have no equivalent in the Escrow Liaison's list at all — those two appear to describe escrow-level rollups of fund-release activity that the Escrow Liaison's screen tracks separately (see Fund Release Status below) rather than as an escrow-account-level state.

### Milestone Verification Status (additional vocabulary found during consolidation)

[escrow-details.md](screens/escrow-details.md) (Escrow Liaison's Tab 3 — Milestones) uses a **third, distinct** status vocabulary for the construction milestone itself, separate from both Escrow Status and Fund Release Status above: Pending, In Progress, Submitted, Verified, Returned (5 states). This wasn't in the original 7-category scaffold for this file; it's included here because it's a real, independently-tracked status axis (a milestone can be "Verified" while its associated fund release is still "Under Review"), not a duplicate of either status above.

## Fund Release Status

Used on [escrow-management.md](screens/escrow-management.md) and [escrow-details.md](screens/escrow-details.md) (Tab 2 — Fund Releases).

**⚠ Conflict:**

- **Developer Principal / Director** (escrow-management.md): Not Requested, Requested, Under Review, Approved, Released, Rejected (6 states)
- **Escrow Liaison** (escrow-management.md): No Request, Pending Approval, Under Review, Approved, Released, Returned, Rejected (7 states)
- **Escrow Liaison** (escrow-details.md, Tab 2 table): Draft, Submitted, Under Review, Approved, Released, Returned, Rejected (7 states)

All three describe the same concept but disagree on the initial-state name ("Not Requested" / "No Request" / "Draft" — three different labels for what appears to be the same starting point) and on whether "Returned" exists as a distinct state (present in both Escrow Liaison lists, absent from the Principal's). The Escrow Liaison's own two lists (escrow-management.md vs. escrow-details.md) also disagree with each other on the initial-state label ("No Request" vs. "Draft"), which suggests this wasn't just a Principal-vs-Liaison gap but an inconsistency within the same role's screens.

## Application Status

Used on [applications.md](screens/applications.md).

**⚠ Conflict:**

- **Developer Principal / Director:** Draft, Submitted, Under Review, Pending Additional Information, Approved, Rejected, Withdrawn (7 states)
- **Registration Officer / Sales & Disclosure Officer / Escrow Liaison** (identical across all three): Draft, Submitted, Under Review, Information Requested, Returned, Approved, Rejected, Withdrawn (8 states)

The three operational roles agree with each other exactly. Only the Principal's list differs, and only by one state: "Pending Additional Information" (Principal) vs. "Information Requested" + "Returned" (operational roles) — the Principal's single state maps to what the operational roles track as two separate states.

## Document Status

Used on [documents.md](screens/documents.md) and [document-details.md](screens/document-details.md). The source uses **three different vocabularies** for what is arguably the same underlying concept (a document's verification state), and they don't reduce to one list without dropping information:

**Documents list screen — "Verification Status":**

- **Developer Principal / Director:** Verified, Pending Review, Returned, Rejected, Expired (5 states)
- **Registration Officer / Escrow Liaison** (identical): Draft, Pending Verification, Verified, Information Requested, Returned, Rejected, Expired (7 states)

**Documents list screen — "Expiry Status"** (Principal's version only; a separate, smaller vocabulary for how close a document is to expiring, not its verification state): Valid, Expiring Soon, Expired (3 states).

**Document Details screen — "Regulatory Verification"** (Registration Officer / Sales & Disclosure Officer / Escrow Liaison, identical across all three): Pending Review, Information Requested, Verified, Rejected (4 states).

The Document Details variant is shorter than either Documents-list variant and uses "Regulatory Verification" as its heading rather than "Verification Status" — it isn't clearly the same list with items dropped; it reads as a narrower, review-outcome-only vocabulary (no "Draft," "Expired," or "Returned"). Reported as three separate, unreconciled lists rather than merged into one.

## Generic (not tied to a specific business entity)

These appeared in the source under a "Status" or similarly generic heading, scoped to a UI mechanism rather than a regulatory entity. Included for completeness since the issue asked for every legend found, not just the 7 named categories.

### Ticket Status (Help & Support)

**⚠ Conflict — no two of the four role versions agree exactly:**

- **Developer Principal / Director:** Open, In Progress, Waiting for Customer, Escalated, Resolved, Closed (6 states)
- **Registration Officer / Sales & Disclosure Officer** (identical): Draft, Open, In Progress, Waiting for Customer, Escalated, Resolved, Closed (7 states — adds "Draft")
- **Escrow Liaison:** Open, In Progress, Waiting for User, Resolved, Closed (5 states)

The Escrow Liaison's list is the odd one out twice over: it has no "Draft" or "Escalated" state, and uses "Waiting for User" where the other three roles all say "Waiting for Customer."

### Notification Status

[notifications.md](screens/notifications.md) — a per-notification read state, consistent across all roles (only documented once, under the Principal's version, but nothing in any other role's block contradicts it): Unread, Read, Archived (3 states). No conflict.

### Company / RERA License Status

[company-profile.md](screens/company-profile.md) (Principal only — this screen has no other role's version to compare against, so no conflict is possible): Active, Pending Renewal, Expiring Soon, Suspended, Expired (5 states), covering the developer organization's own RERA license, distinct from any project's or application's status. Found under a plain "Status badges:" prose lead-in rather than a heading, easy to miss on a first pass of the source — added here for completeness.

### Report Generation Status

[reports.md](screens/reports.md) — the processing state of a generated report file. **Identical across all four roles** — the one legend in this whole file with no conflict at all: Processing, Completed, Failed, Expired (4 states).
