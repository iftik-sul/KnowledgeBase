---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/navigation.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - components
---

# Individual User — Component Library

Shared component definitions. Screens reference these rather than restating them.

## Sidebar

Defined in `navigation.md`'s Proposed Sidebar. Identical for every authenticated user — no role-based variant:

* Dashboard
* My Properties
* My Leases
* Services Catalog
* My Applications
* My Complaints
* Power of Attorney
* Documents
* Payments
* Notifications
* Profile & KYC
* Help & Support

**Badge counts** appear on My Applications (count with Information Requested or Returned status), My Complaints (count Resolved but unread), Power of Attorney (count of incoming PoA requiring confirmation, if any), and Notifications (unread count). No count is role-filtered — every count reflects the logged-in account's own records only, never institution-wide, since there is no institution here.

## Top Bar

* Platform logo / home link
* Global search (searches properties, leases, applications, and complaints by reference number or address)
* Notification bell (links to Notifications, shows unread count)
* Profile menu (Profile & KYC, Help & Support, Log Out)

## Property Selector

Used by every Pattern B/C/D/E service that needs "select a registered property" as its first step. A searchable list of the account's own registered properties, each row showing address, property type, and registration number. Selecting a property carries its details forward into the wizard so the applicant doesn't re-enter them.

**Empty state:** if the account has no registered properties and the selected service requires one, the wizard cannot proceed — the empty state directs the user to Register Property Ownership (#4) first, rather than allowing an impossible submission.

## Lease Selector

Same pattern as Property Selector, for Pattern D/E/F services acting on an existing lease (#12, #13, #15, #16, #24, #25, #27). Shows both leases where the account is landlord and leases where the account is tenant, labelled accordingly, since B1's resolution means either role may need to act on the same lease record.

## Counterparty Confirmation Card

Used by every Pattern C service. Shown to the primary applicant after submission ("Awaiting [Purchaser/Recipient/Beneficiary] Confirmation") and to the counterparty when they open the notification. The counterparty's own screen shows: what they're being asked to confirm, the primary applicant's submitted details (read-only), an OTP verification step where sourced (#6 specifically), Accept / Decline actions, and a document-upload step where the counterparty must supply their own documents (varies by service — see each service's own Required Documents).

## Document Upload

Standard multi-file upload with per-document-type labelling, matching each service's own Required Documents list. Accepted formats and size limits are **Proposed**, not sourced — no service-flow file specifies them.

## Payment Step

Renders differently depending on which payment category the selected service falls into — see `payments.md` for the full per-service breakdown. Three renderings:

1. **Upfront** (most services): "Review Service Fee → Complete Payment" appears before the Submit action.
2. **After-decision** (#28, and the counter-channel path of #23, #24, #26, #27, #9–#16 where sourced): no payment step appears in the wizard at all; instead, [application-details.md](../screens/application-details.md) shows a "Pay Now" action once the application reaches Approved status.
3. **No fee** (#17, #18, #33, #40, #42, and the Owner/Entity-Amendment half of #7): the wizard skips the payment step entirely — no "Review Service Fee" screen renders.

Every fee-bearing service also shows the standard shared platform gateway (card, bank transfer, USSD per the PRD) as the payment method — see `payments.md`'s Settlement Mechanism section, which confirmed there is no separate Wallet Account mechanism anywhere in this module (resolved 2026-08-15, `open-questions.md` C1).

## Status Badge

See [status-badges.md](status-badges.md) for the full vocabulary. Rendered consistently across Applications, Application Details, My Complaints, My Leases, and Dashboard.

## Buttons

Primary (submit, pay, confirm), Secondary (save draft, cancel), Destructive (withdraw application, decline counterparty request) — standard three-tier treatment, no module-specific variants.

## KPI / Summary Cards

Used on Dashboard and list screens. Each card shows a count and, where relevant, links to the filtered list it summarizes.

## Empty States

Every list screen defines its own empty-state message — see each screen file. The Property Selector and Lease Selector components above are the two cases where an empty state can actually block a wizard step, not just show a friendly message on an otherwise-usable screen.
