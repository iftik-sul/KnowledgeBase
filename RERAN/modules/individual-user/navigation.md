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

**Corrected 2026-08-15, found in an audit pass.** This document previously opened by saying the module "has no UI documented yet" and closed by saying its own proposals should be checked "once UI work begins" — both true when this file was first written, both stale since: the UI package (20 files) was built directly against this document, merged (PR #61), and has since been checked against it repeatedly across multiple audit passes. This document is no longer a forward-looking proposal awaiting UI work; it's the access-model reference the UI package was actually built from. Where a proposal below was adopted as-is, that's noted inline rather than left as an open question.

## Why This Module's Access Model Is Different From Groups B and C

Groups B and C are **corporate accounts**: a company holds one account, and multiple staff members with different roles operate inside it. Group C's `navigation.md` resolved a real question there — whether role gates access — because a bank's Mortgage Officer and Auditing Bureau Officer are different people sharing one institutional login surface.

Individual User is **not** a corporate account model. `roles-and-responsibilities.md` states this directly: *"Unlike organizational users, an individual may perform multiple roles over time using the same account."* Ahmed is a Property Owner/Seller when he sells his flat and nothing stops him from also being a Landlord for a different property, or a Property Buyer/Investor when he's shopping for his next purchase. There is one person, one account, and the "role" isn't a provisioned permission — it's a description of what the person is currently doing.

This means the Group C question ("does role X gate access to screen Y") doesn't translate directly. The equivalent question for Individual User is: **does the platform show every service to every logged-in user regardless of what they currently own or hold, or does it surface only the services relevant to what's actually in their account?**

## Access Model: Activity-Scoped, Not Role-Gated

**Adopted as designed — the UI package's own Access Model section confirms this exact framing was built.** Every authenticated Individual User can *see* the full Services Catalog (all 43 services, all 8 categories), consistent with the platform-wide principle that verification and informational services (#1–#3) are explicitly open to "All registered Individual Users" regardless of what they own. Several services are only *actionable* once a precondition is met:

- **Register/Renew/Manage/Cancel Lease (#23–#27)** require the user to hold a registered property (as landlord) or a registered tenancy (as tenant) — see B1 in `open-questions.md`, resolved: Landlord is the primary applicant, with Tenant added as a documented secondary path.
- **Transfer, Sell, Amend, or otherwise act on a property (#5–#22, #35, #41, #43)** require the user to be the registered owner (or hold an active Power of Attorney over a registered owner — see #30) of the specific property selected.
- **Act on Behalf of Property Owner (#30)** requires an active, RERAN-approved Power of Attorney (#29) before the service does anything beyond showing a "no active authorization" state — this is already how #30's own file describes it (`Authorization Validation` as the first real status in its Application Status Flow), so this module has already implicitly designed for activity-scoped access at the single-service level; it just hasn't been stated as a platform-wide navigation principle until now.
- **Remote Identity Verification / Remote Property Transactions (#36–#37)** — #37 explicitly requires #36 to be completed first (`Prerequisites: Remote Identity Verification has been successfully completed`), a second example of one service gating another, already present in the sourced/extrapolated files without being generalised into a navigation rule.

**What this is not:** it is not a role-selection screen where a user picks "I am a Landlord today" before logging in. Every logged-in user sees one dashboard and one Services Catalog; which actions are live depends on what's already in their account (properties owned, leases registered, PoAs granted or held), not on a role they declare.

## Sidebar

**Built exactly as proposed** — every item below matches `components.md`'s Sidebar definition in the shipped UI package, verified against it directly:

* Dashboard
* My Properties *(built as a first-class screen — see "What Was a Client Decision" below)*
* My Leases *(same)*
* Services Catalog (all 43, organized by the 8 categories in `services-overview.md`)
* My Applications *(Feature #2's home — free to use, per `payments.md` A6)*
* My Complaints *(#38 charges a fee, #39 does not — resolved in `open-questions.md` A6/A7)*
* Power of Attorney *(registered PoAs granted and PoAs held — #29, #30, #42)*
* Documents
* Payments *(payment history, receipts — via the standard shared gateway throughout; see `payments.md` C1, resolved — there is no separate Wallet Account mechanism)*
* Notifications
* Profile & KYC *(where Remote Identity Verification, #36, lives for diaspora users)*
* Help & Support

**Diaspora-specific note:** #36/#37 don't need a separate sidebar section under this model — a Diaspora Investor is still an Individual User acting through the same Services Catalog and My Properties surfaces as anyone else; #36's identity verification is a Profile & KYC action, and #37 is a mode of interacting with the same underlying services (#5, #6, etc.) once verified, not a parallel catalog. This matches how #37's own file describes it: *"Select Transaction Type"* from within Remote Property Transactions routes into the same transaction types documented elsewhere in the module. **Confirmed as-built** — `profile-kyc.md` implements exactly this, with no separate diaspora section anywhere in the shipped sidebar.

## Landing After Login

**Adopted as designed.** A single Dashboard, same for every user, showing:

- Properties owned / leases held (empty state for a new user with neither)
- Applications in progress (via Feature #2)
- Notifications requiring action (Information Requested, Returned applications — Features #3/#4)
- Quick actions: Register Property Ownership (#4), Verify a Property/Developer/Project (#1–#3), Submit Complaint (#38)

No per-role landing default was built, for the same reason no role-selection step was proposed above — `dashboard.md`'s own Notes section confirms this explicitly: "No per-role landing default, matching `navigation.md`'s explicit reasoning: the account, not a declared role, is what's logged in."

## What Was a Client Decision, Now Resolved

1. **Whether My Properties / My Leases should exist as first-class sidebar sections, or property/lease selection should happen inline within each service's own flow** — resolved by design choice when the UI package was built: both were built as first-class screens (`ui/README.md`'s Open Item 3 records this explicitly as "the richer option," and notes it's reversible if the client prefers inline-only). Not confirmed by the client directly, but a design decision made and shipped, not still an open question sitting only in this document.
2. **B1 is resolved** (Landlord primary, Tenant secondary applicant — see `open-questions.md` B1), which settles that "My Leases" needs to support both a landlord's and a tenant's view of the same lease record, not just one. `my-leases.md` implements exactly this — two tabs, "As Landlord" and "As Tenant."
3. **Whether Diaspora Investor status should surface anywhere in navigation** — resolved by design choice: it doesn't. `dashboard.md`'s own Notes section states this directly: "`navigation.md` leaves open whether it should surface as a badge anywhere; this dashboard doesn't currently show one" — so the *building* of the dashboard treated this as still-open even though the design direction (no distinct diaspora surface, per the Sidebar section above) was already set. Genuinely the one item on this list that's still soft — a badge could be added later without contradicting anything already built, unlike items 1 and 2 which are now load-bearing design decisions the shipped screens depend on.

## Relationship to the UI Package

This document predates the UI package (`ui/`) and was the access-model reference it was built against — not superseded by it, but consumed by it. `ui/README.md`'s own Access Model section restates this document's activity-scoped framing directly, and every screen file's own Access section traces back to the reasoning here. Where this document and a shipped screen file appear to disagree, the screen file's Access section should be checked first — it may reflect a design decision made during the UI build that was never carried back into this document (see item 1 above, which is exactly that situation, now corrected).
