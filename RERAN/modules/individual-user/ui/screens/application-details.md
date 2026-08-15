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

One application in full: what was submitted, its documents, current status, and any action the account needs to take — including responding to an information request (Feature #3), resubmitting a returned application (Feature #4), or paying, where payment falls after RERAN's decision rather than inside the wizard.

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
* **Approved — Awaiting Payment** → **Pay Now**, shown only for the services `payments.md` confirms use this timing (#28, and the counter-channel path of #5, #9–#16, #23, #24, #26, #27 where applicable). This is the one action area this screen must get right that a naive build easily wouldn't — the module's entire payment-timing documentation defect was exactly this kind of "payment step shown/hidden at the wrong point" error, now corrected in the source files this screen reads from.
* **Recipient/Purchaser/Beneficiary Confirmation Pending** (Pattern C) → shows the counterparty's own confirmation status, not an action for the primary applicant.
* **Completed** → Download Output Document.

## Empty State

Not applicable — this screen only renders for an application that exists.

## Reused Components

Status Badge, Document Upload (for the Information Request response step), Payment Step, Buttons.

## Validation

The Action Area must match the current status exactly — a Pay Now button must never appear for a service that's confirmed no-fee or for a status other than Approved — Awaiting Payment, and an Information Request response option must never appear for any other status.

## Access

No role variation.

## User Flow

```
Applications → Application Details →
  [Respond to Info Request] or [Resubmit] or [Pay Now] or [Download]
```

## Notes

* For Pattern C applications, this screen is what the counterparty opens from their notification — the same screen, same reference number, but the Action Area shows their confirmation step instead of the primary applicant's.
