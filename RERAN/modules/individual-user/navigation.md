---
project: RERAN
module: individual-user
type: navigation
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/roles-and-responsibilities.md"
  - "RERAN/modules/individual-user/services-overview.md"
  - "RERAN/modules/individual-user/shared-platform-features.md"
  - "RERAN/modules/individual-user/open-questions.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
tags:
  - individual-user
  - navigation
  - permissions
---

# Individual User — Navigation & Access

This module has no UI documented yet (`module-roadmap.md`'s "mirror-image gap" of Real Estate Developer), so unlike Group C's `navigation.md` — which corrects a previously-documented access model — this is a first pass, written to inform the UI work this module still needs, not a correction of anything existing.

## Why This Module's Access Model Is Different From Groups B and C

Groups B and C are **corporate accounts**: a company holds one account, and multiple staff members with different roles operate inside it. Group C's `navigation.md` resolved a real question there — whether role gates access — because a bank's Mortgage Officer and Auditing Bureau Officer are different people sharing one institutional login surface.

Individual User is **not** a corporate account model. `roles-and-responsibilities.md` states this directly: *"Unlike organizational users, an individual may perform multiple roles over time using the same account."* Ahmed is a Property Owner/Seller when he sells his flat and nothing stops him from also being a Landlord for a different property, or a Property Buyer/Investor when he's shopping for his next purchase. There is one person, one account, and the "role" isn't a provisioned permission — it's a description of what the person is currently doing.

This means the Group C question ("does role X gate access to screen Y") doesn't translate directly. The equivalent question for Individual User is: **does the platform show every service to every logged-in user regardless of what they currently own or hold, or does it surface only the services relevant to what's actually in their account?**

## Proposed Access Model: Activity-Scoped, Not Role-Gated

**Proposed** (no source or client decision settles this yet — flagged for confirmation): every authenticated Individual User can *see* the full Services Catalog (all 43 services, all 8 categories), consistent with the platform-wide principle that verification and informational services (#1–#3) are explicitly open to "All registered Individual Users" regardless of what they own. But several services are only *actionable* once a precondition is met:

- **Register/Renew/Manage/Cancel Lease (#23–#27)** require the user to hold a registered property (as landlord) or a registered tenancy (as tenant) — see B1 in `open-questions.md` for the open question on which of those two the platform should support as primary.
- **Transfer, Sell, Amend, or otherwise act on a property (#5–#22, #35, #41, #43)** require the user to be the registered owner (or hold an active Power of Attorney over a registered owner — see #30) of the specific property selected.
- **Act on Behalf of Property Owner (#30)** requires an active, RERAN-approved Power of Attorney (#29) before the service does anything beyond showing a "no active authorization" state — this is already how #30's own file describes it (`Authorization Validation` as the first real status in its Application Status Flow), so this module has already implicitly designed for activity-scoped access at the single-service level; it just hasn't been stated as a platform-wide navigation principle until now.
- **Remote Identity Verification / Remote Property Transactions (#36–#37)** — #37 explicitly requires #36 to be completed first (`Prerequisites: Remote Identity Verification has been successfully completed`), a second example of one service gating another, already present in the sourced/extrapolated files without being generalised into a navigation rule.

**What this is not:** it is not a role-selection screen where a user picks "I am a Landlord today" before logging in. Every logged-in user sees one dashboard and one Services Catalog; which actions are live depends on what's already in their account (properties owned, leases registered, PoAs granted or held), not on a role they declare.

## Proposed Sidebar

Based on `shared-platform-features.md`'s 8 general platform features and `services-overview.md`'s 8 business-service categories:

* Dashboard
* My Properties *(new — not named as a standalone platform feature in the source, but implied by nearly every service's "Select Registered Property" step; without a properties list, a user can't act on #5–#22, #35, #41, #43 at all)*
* My Leases *(same reasoning, for #23–#28, #40)*
* Services Catalog (all 43, organized by the 8 categories in `services-overview.md`)
* My Applications *(Feature #2's home — free to use, per `payments.md` A6)*
* My Complaints *(#38/#39 — pending the fee resolution in `open-questions.md` A6/A7)*
* Power of Attorney *(registered PoAs granted and PoAs held — #29, #30, #42)*
* Documents
* Payments *(payment history, receipts — see `payments.md` for what's still unsettled about the Wallet Account question, C1)*
* Notifications
* Profile & KYC *(where Remote Identity Verification, #36, lives for diaspora users)*
* Help & Support

**Diaspora-specific note:** #36/#37 don't need a separate sidebar section under this model — a Diaspora Investor is still an Individual User acting through the same Services Catalog and My Properties surfaces as anyone else; #36's identity verification is a Profile & KYC action, and #37 is a mode of interacting with the same underlying services (#5, #6, etc.) once verified, not a parallel catalog. This matches how #37's own file describes it: *"Select Transaction Type"* from within Remote Property Transactions routes into the same transaction types documented elsewhere in the module.

## Landing After Login

**Proposed:** a single Dashboard, same for every user, showing:

- Properties owned / leases held (empty state for a new user with neither)
- Applications in progress (via Feature #2)
- Notifications requiring action (Information Requested, Returned applications — Features #3/#4)
- Quick actions: Register Property Ownership (#4), Verify a Property/Developer/Project (#1–#3), Submit Complaint (#38)

No per-role landing default is proposed, for the same reason no role-selection step is proposed above — the same person may need different quick actions on different days, and the account itself (not a role) is what's logged in.

## What Still Needs a Client Decision

1. **Whether My Properties / My Leases should exist as first-class sidebar sections**, or whether property/lease selection should instead happen inline within each service's own flow (as most service-flow files currently describe it — "Select Registered Property" as step 2 of the workflow, not a standalone screen visited first).
2. **B1's Landlord-vs-Tenant question** for #23/#24 directly affects whether "My Leases" needs to support both a landlord's and a tenant's view of the same lease record, or just one.
3. Whether **Diaspora Investor** status should surface anywhere in navigation at all (a badge, a distinct onboarding path) given #36/#37's design already routes diaspora users through the same catalog as everyone else once verified.

## Superseded By This Document

Nothing — this is the first `navigation.md` this module has had. Once UI work begins (per `module-roadmap.md`'s Proposed Sequence item 4), the actual screen inventory in `ui/screens/` should be checked against the proposed sidebar above the same way Group C's UI reconciliation (issue #50) checked its screens against its navigation model, rather than letting the two drift independently from the start.
