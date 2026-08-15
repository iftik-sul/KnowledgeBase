---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/service-flows/feature-03-respond-to-information-request.md"
  - "RERAN/modules/individual-user/service-flows/feature-04-resubmit-returned-application.md"
  - "RERAN/modules/individual-user/payments.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - applications
---

# Screen: Application Details

**Access:** Any authenticated Individual User — own application only.

## Purpose

One application in full: what was submitted, its documents, current status, and any action the account needs to take — including responding to an information request (Feature #3), resubmitting a returned application (Feature #4), or paying, where payment falls after some or all of RERAN's decision rather than inside the wizard.

## Layout

```
Header (reference, service, status)
↓
Submitted Details (read-only)
↓
Documents
↓
Timeline
↓
Action Area (varies by status)
```

## Sections

### Section 1 — Header

Application reference number, service name, current status badge.

### Section 2 — Submitted Details

Read-only rendering of everything entered during the wizard — the same section groupings [Application Review](../screens-unified/application-review.md) showed before submission.

### Section 3 — Documents

Every uploaded document, downloadable, plus the issued output document once Completed (Certificate of Title, judgment, report, etc. — whichever the specific service's own Output section names).

### Section 4 — Timeline

Chronological status history — submission, review milestones, information requests, decisions.

### Section 5 — Action Area

Conditional on status:

* **Information Requested** → Respond to Information Request (Feature #3): upload additional documents / provide clarification, returns to Under Review.
* **Returned** → Resubmit (Feature #4): correct and resubmit without creating a new application.
* **Approved — Awaiting Payment** → **Pay Now**, shown only for #28, whose single (online) workflow sources payment strictly after RERAN's full decision (`payments.md` Category 2).
* **Audited — Awaiting Payment** → **Pay Now**, shown only for the counter-channel path of #9–#16, #23, #24, and #26, where the Trustee Centre / Service Center channel pays after the audit step but before formal approval — a different checkpoint from #28's, which is why it's a different status (`status-badges.md`, corrected in a later audit pass; `payments.md` Category 3).
* **Payment Pending**, wherever it appears in the sequence → **Pay Now**, same as any other upfront-payment service. This already covers #27, whose post-review payment step is deliberately just a repositioned `Payment Pending` rather than a distinctly-named status — no special-case handling needed here beyond what the generic Payment Pending status already triggers.
* **Recipient/Purchaser/Beneficiary Confirmation Pending** (Pattern C) → shows the counterparty's own confirmation status, not an action for the primary applicant.
* **Completed** → Download Output Document.

*(Corrected 2026-08-15, second audit pass — this section previously named a single "Approved — Awaiting Payment" status and listed #5, #9–#16, #23, #24, #26, and #27 as sharing it. That was wrong in two ways: #5 was never Category 3's after-decision case at all — its counter channel pays *before* the combined audit-and-approval step, confirmed directly against the file, so it never shows a Pay Now action here after Approved. And #9–#16/#23/#24/#26 use a different, earlier checkpoint than #28's — see `status-badges.md`'s corrected two-status split. #27 needs no special-case entry, since its post-review payment step already uses the generic Payment Pending status.)*

## Empty State

Not applicable — this screen only renders for an application that exists.

## Reused Components

Status Badge, Document Upload (for the Information Request response step), Payment Step, Buttons.

## Validation

The Action Area must match the current status exactly — a Pay Now button must never appear for a service that's confirmed no-fee, and must appear only for Payment Pending, Approved — Awaiting Payment, or Audited — Awaiting Payment; an Information Request response option must never appear for any other status.

## Access

No role variation.

## User Flow

```
Applications → Application Details →
  [Respond to Info Request] or [Resubmit] or [Pay Now] or [Download]
```

## Notes

* For Pattern C applications, this screen is what the counterparty opens from their notification — the same screen, same reference number, but the Action Area shows their confirmation step instead of the primary applicant's.
