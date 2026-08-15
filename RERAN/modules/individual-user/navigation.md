---
project: RERAN
module: individual-user
type: navigation
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/individual-user/roles-and-responsibilities.md"
  - "RERAN/modules/individual-user/services-overview.md"
  - "RERAN/modules/individual-user/open-questions.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
tags:
  - individual-user
  - navigation
  - permissions
---

# Individual User — Navigation & Access

## Why This Module's Access Model Differs From Group C's

Group C's navigation is unified precisely because its four roles are provisioned staff positions on a corporate account — a Mortgage Officer and an Auditing Bureau Officer are different *employees*, and the client decided role should be audit-trail attribution only, not a permission gate.

Individual User is structurally different at the root: **one person holds one account, and the same person can hold several of the module's six roles at once, or acquire a new one at any time simply by taking an action.** `roles-and-responsibilities.md` says this directly — "an individual may perform multiple roles over time using the same account. The platform grants access to services based on the user's current activities." Ahmed is a Property Owner/Seller because he owns a registered property; the same Ahmed becomes a Landlord the moment he registers a lease against that property; nothing was provisioned, invited, or approved to make that happen.

So this module doesn't need Group C's "is role a permission gate or an audit-trail attribution?" question at all — **role here is neither.** It's a *derived state*, computed from what a person has already done or registered, not a static credential.

## The Sidebar

One menu, identical in structure for every Individual User, organized by the eight service categories `services-overview.md` already defines — not by role:

* Dashboard
* My Properties
* Verification *(#1–#3)*
* Ownership & Transactions *(#4–#16, #41, #43)*
* Title & Land Registration *(#17–#22)*
* Tenancy *(#23–#28, #40)*
* Power of Attorney *(#29–#30, #42)*
* Property Certificates *(#31–#35)*
* Diaspora Services *(#36–#37)*
* Complaints *(#38–#39)*
* Applications
* Documents
* Payments
* Notifications
* Profile & KYC
* Help & Support

**Every category is visible to every logged-in user, always.** There is no role-based menu filtering — not because a client decision retired one (as in Group C), but because there was never a role-gated menu to retire: a person's roles change constantly as a side effect of ordinary use, so gating the *menu* on current role would mean the sidebar changes shape every time someone registers a new property or files a new lease. That's a worse experience than showing everything and letting eligibility be enforced at the point of use (Section 5, "Prerequisites," in each service-flow file) rather than at the point of menu rendering.

**Confidence:** Medium-high — this is a reasoned design position, not confirmed by source (the source is silent on menu structure entirely), but follows directly from the "multiple roles, same account" principle `roles-and-responsibilities.md` already states.

## What Changes Per Role Is Content, Not Access

Inside a given category, what a person *sees* is scoped to what they actually have — a Landlord's Tenancy category shows the leases they've registered as landlord; a Tenant's shows the leases where they're the named tenant; someone who is both sees both, unmerged, since they're legally distinct relationships even when the underlying property is the same. This mirrors Service #6's already-documented seller/purchaser split (each party gets their own half of the same transaction) and extends it to every category where a person could plausibly sit on either side of a relationship (Tenancy, and — pending A1's resolution in `open-questions.md` — potentially Register/Renew Lease specifically).

**Where this needs a decision, not a default:** Service #38/#39 (Complaints) and the Power of Attorney category are the two places "what a person sees" isn't obviously self-scoping. A PoA holder acting under Service #30 sees the represented owner's properties, not their own — this is already handled at the service level (Section 6 of `service-30-act-on-behalf-of-property-owner.md` requires selecting "Registered Property Owner" first), so no navigation-level change is needed, but it's worth naming here since it's the one place in this module where "whose data am I looking at" genuinely isn't the logged-in user's own by default.

## Landing After Login

**Proposed:** a single Dashboard, not role-differentiated, showing:

* A summary of the user's active roles (computed, not selected) — e.g. "You are registered as: Property Owner (2 properties), Landlord (1 active lease)" — surfaced as information, not as a mode switch
* Applications in progress, across every service category, sorted by most-recent-activity
* Payment-pending items — see the note below on why this needs to be built carefully given `payments.md`'s findings
* Quick actions: the four most-used services platform-wide are unknown without usage data, so propose Verify Property, Register Property Sale, Submit Tenancy Dispute, and Request Detailed Real Estate Statement as placeholders pending real usage data, not a sourced or confirmed set

**Confidence:** Medium — no source material describes a dashboard for this module at all; this follows Group C's already-confirmed pattern (one shared dashboard, no per-role default) since the same "should a unified dashboard show one CTA per role" question Group C answered applies here for the same underlying reason: a person's roles aren't a fixed identity to design a CTA around.

**A caution specific to this module, not present in Group C's dashboard:** the Payment-pending summary cannot be built as a single "pay before you can proceed" queue the way Group C's could, because `payments.md` documents at least three different payment-timing models coexisting in this module (upfront, pay-after-audit-before-decision, pay-after-decision). A dashboard widget that shows every unpaid application as blocking, or every paid application as complete, will misrepresent Service #28 (which pays *after* approval — an item sitting in "Approved" with no payment yet is not stuck or overdue, it's exactly where it should be) and the Model B services (#23/#24/#26, where an application awaiting the post-audit payment step is mid-process, not abandoned). This needs `payments.md`'s corrected timing models to inform the dashboard's status logic, not the currently-published (and partly incorrect) Section 9 lines in the individual service files — see `open-questions.md` B2.

## External / Assisted Access — Trustee Centres

**Proposed, pending `open-questions.md` B4:** by analogy with Group C's confirmed C2 answer, the Real Estate Registration Trustee Centre channel — named as the only or an alternate channel on a large share of this module's sourced services (#5, #6, #9–#16, #19–#22, #23–#24, #26–#27, #31–#33, #35, #41, #43) — should be treated as an **assisted mode of the same service**, not a parallel paper process, consistent with the platform's stated goal of reducing in-person visits.

Trustee Centre operators are Group G users, not Individual User roles; they do not appear in this sidebar, and their own access model belongs in Group G's own navigation documentation once written (per `module-roadmap.md`'s Group G note). What belongs here is only the acknowledgment that an Individual User's application may be *filed on their behalf* through this channel, and that doing so changes the payment-timing sequence for the services listed in `payments.md`'s channel-split section — this is a genuine difference in the applicant's own experience (when they pay, relative to submission), not just a back-office detail.

**Confidence:** Medium — the C2 reasoning transfers well, but hasn't been independently confirmed for this module, and closing `open-questions.md` B4 first would raise this to High.

## Diaspora Access — A Genuine Difference From Group C

Unlike any Group C role, two of this module's six roles (Diaspora Investor, and Property Owner/Seller or Landlord roles held by someone living abroad) are explicitly designed around **not** being able to use the Trustee Centre channel at all. Services #36 (Remote Identity Verification) and #37 (Remote Property Transactions) exist specifically to substitute for in-person presence. This has one navigation consequence worth stating plainly: for a diaspora user, the sidebar's Verification category functions as a gate — Service #37 and several PoA-adjacent flows (Section 5 of `service-37-remote-property-transactions.md`) require Remote Identity Verification to have already succeeded, which is not true of any other role in this module. **Proposed:** surface identity-verification status prominently (e.g., in the Dashboard's role summary described above), since it is the one piece of account state that gates access to an entire category for this user type specifically, unlike every other role's Section 5 prerequisites, which are typically per-service rather than per-category.

**Confidence:** High that this gating exists (sourced, Section 5 of #37); Medium on the specific dashboard treatment proposed, which is a design judgement.

## Summary of What's Confirmed vs. Proposed

| Element | Status |
| :---- | :---- |
| One sidebar, no role-based menu filtering | Proposed — reasoned from `roles-and-responsibilities.md`'s multi-role principle, not source-confirmed |
| Content within a category scoped to the user's actual relationships (not role) | Proposed, following Service #6's already-documented pattern |
| Unified dashboard, no per-role CTA | Proposed, by analogy with Group C's confirmed answer |
| Dashboard payment-status logic must reflect `payments.md`'s multiple timing models | High-confidence requirement, not yet built — flagged as a dependency on `open-questions.md` B2 being resolved first |
| Trustee Centre as assisted mode, not a separate system | Proposed, pending `open-questions.md` B4 |
| Diaspora identity-verification status as a prominent, category-gating dashboard element | Proposed, sourced gating + design judgement on treatment |
