---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/service-flows/"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - status-vocabulary
---

# Individual User — Status Badges

Three separate status vocabularies exist in this module — they must not be collapsed into one, since they track genuinely different lifecycles.

## Application Status (Patterns A, B, C, D, E, H, I, J)

The vocabulary most service-flow files' own Application Status Flow sections already define, reconciled here into one shared badge set:

| Status | Meaning | Badge treatment |
| :---- | :---- | :---- |
| Draft | Started, not submitted | Neutral / grey |
| Payment Pending | Upfront-payment services only, checkout in progress | Neutral |
| Payment Successful | Payment confirmed (upfront services) | Neutral |
| Submitted | Lodged, awaiting review | Info / blue |
| Booking Pending / Purchaser Response Pending / Recipient Confirmation Pending / Beneficiary Confirmation Pending | Pattern C only — awaiting the counterparty's action, not RERAN's | Warning / amber |
| Under Review | With RERAN | Info / blue |
| Information Requested | RERAN needs more from the applicant | Warning / amber |
| Resubmitted | Applicant has responded, back with RERAN | Info / blue |
| **Audited — Awaiting Payment** | The Trustee Centre / Service Center channel has audited the transaction but not yet approved it; payment is the next step, before approval — applies only to the counter-channel path of #9–#16, #23, #24, #26 (see `payments.md` Category 3, and each file's own Section 13, corrected in a later audit pass) | Warning / amber |
| **Approved — Awaiting Payment** | RERAN has fully decided the application; payment is the last step before the output is released — applies only to #28, whose single (online) workflow sources payment strictly after approval (see `payments.md` Category 2) | Warning / amber |
| Approved | Decision made, fully settled where a fee applies | Success / green |
| Completed | Output document issued | Success / green |
| Returned | Sent back for correction | Warning / amber |
| Rejected | Refused with reason | Error / red |
| Withdrawn | Applicant cancelled | Neutral / grey |
| Cancelled | System or applicant cancelled before submission | Neutral / grey |

**These are two distinct statuses, not one — corrected 2026-08-15 in a later audit pass.** This section previously collapsed both into a single "Approved — Awaiting Payment" label and applied it uniformly to #28 and the counter-channel path of #9–#16, #23, #24, #26, #27. That was wrong on inspection against the actual files: #28's own Section 13 genuinely says "Approved — Awaiting Payment" (RERAN's full decision precedes payment), but #9–#16, #23, #24, and #26 use "Audited — Awaiting Payment" instead, because their counter-channel sequence pays *before* formal approval, right after the audit step — audit and approval are not the same checkpoint in those files, and using "Approved" for a state that precedes approval would misrepresent what the file itself documents. **#27 needs neither status** — its own Section 13 just repositions the standard Payment Pending / Payment Successful pair after Information Requested rather than introducing a distinct named intermediate state, and that's already correct as written; nothing further should be added there.

**Both statuses are genuinely conditional, not universal** — the same lesson Group C's `payments.md` learned about its own #12/#18. They appear only on the specific services and channels where the source or the client-confirmed correction places payment after some or all of RERAN's decision. Every other service either pays upfront (neither status ever appears) or carries no fee at all (both are meaningless for it).

## Complaint / Dispute Status (Patterns G, K)

Distinct vocabulary — a complaint or dispute is not an "application" in the registration sense, and #26 in particular carries category-specific outcomes (Judgment, Settlement Agreement, Performance Order, etc.) that don't map onto the Application Status list above.

| Status | Meaning |
| :---- | :---- |
| Draft | Started, not submitted |
| Payment Pending / Successful | #38 only (fee confirmed by client, `open-questions.md` A7); #26's counter-channel timing is handled the same way as Application Status above (its own "Audited — Awaiting Payment" state, not a Complaint/Dispute-specific one) |
| Submitted | Lodged |
| Assigned | Routed to the correct dispute category / department (#26) or investigation queue (#38) |
| Under Review / Investigation | Being worked |
| Conciliation / Hearing | #26 only, where the sub-type requires a session |
| Information Requested | Additional evidence needed |
| Decision Issued / Resolved | Outcome reached — the specific document (Judgment, Settlement Agreement, Resolution Report) is named on [application-details.md](screens/application-details.md), the status badge itself just says "Resolved" |
| Closed | Complaint concluded (#38/#39 only) |
| Returned / Rejected / Withdrawn / Cancelled | Same meaning as Application Status |

**Tracking a complaint is free** (`open-questions.md` A6) — #39's own status badge never gates on payment, unlike some Application Status paths.

## Power of Attorney Status (Pattern H)

| Status | Meaning |
| :---- | :---- |
| Draft | Started, not submitted (#29) |
| Submitted / Under Review | Registration or cancellation in progress |
| Active | Registered PoA (#29), currently valid and usable for #30 |
| Expired | Past its defined validity period, if one was set |
| Revoked | Cancelled via #42 |
| **Unknown** | #42's own completion status is genuinely unspecified in source — see its service-flow file. This status is a placeholder pending client confirmation, not a designed state. |

## Property / Lease Record Status

Not an application status — these describe the underlying record, shown on My Properties and My Leases rather than on any application:

**Property:** Registered, Under Mortgage, Under Lease-to-Own, Under Usufruct.
**Lease:** Active, Expiring Soon (within 30 days of end date — **Proposed** threshold, not sourced), Expired, Cancelled, In Dispute (a #26 case is open against it).

## Shared Rule

No status badge in this module is filtered or reshaped by the viewing account's role, matching the Access Model in `ui/README.md`. A landlord and a tenant looking at the same lease's status see the identical badge.
