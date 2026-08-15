---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/payments.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - wizard
---

# Screen: Application Review

**Access:** Any authenticated Individual User, mid-wizard only — not a standalone navigable screen.

## Purpose

The final step inside [Submit Application](submit-application.md) before payment/submission — a read-only summary of everything entered, across whichever pattern is in play, so the user can catch mistakes before committing.

## Layout

```
Summary by Section (varies by pattern)
↓
Edit Links (per section)
↓
[Payment Step, if upfront] or [Submit directly, if no fee or after-decision]
```

## Sections

Mirrors whichever pattern's field groups were shown during the wizard — Property/Applicant details, Counterparty details (Pattern C), Transaction-specific fields, Uploaded documents (listed by filename and type, not re-uploaded), and — for Pattern D's repeatable groups (#19, #21) — the full list of heirs/partners entered with their shares.

Each section has an Edit link that returns to the relevant wizard step without discarding progress elsewhere.

## Empty State

Not applicable — this screen only renders once the wizard's prior steps are complete.

## Reused Components

Payment Step, Buttons.

## Validation

This screen must not allow submission if any required field from the pattern's own step sequence is missing — it is the last gate before an application is lodged, not just a display.

## Access

No role variation.

## User Flow

```
Submit Application (final wizard step) → Application Review →
  [Payment, where upfront] → Submit → Application Details
```

## Notes

* Where payment happens after RERAN's decision rather than here, this screen's final action reads "Submit Application" rather than "Pay & Submit" — the distinction matters enough (per `payments.md`'s entire audit) that the button label itself should never claim payment is happening when it isn't.
