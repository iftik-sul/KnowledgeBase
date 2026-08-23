---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-INS-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Instructors — Validation Rules

Field-level validation shared across two or more instructor screens.

---

## WWCC Field Validation

On [Instructor Application](screens/instructor-application.md) and [WWCC Renewal](screens/wwcc-renewal.md): WWCC number, issuing state, and expiry date are all required together — there's no partial-WWCC state (FR-INST-03). Expiry date must be a real future date at time of submission; a WWCC already expired at the moment of application or renewal is refused outright, since accepting one would immediately trigger [FR-INST-04's enforcement](/3i/modules/instructors/data-model.md#fr-inst-04-enforcement--what-cannot-continue-teaching-actually-does) on data that was never valid to begin with.

## Rejection Reason Required

On [Admin Application Review](screens/admin-application-review.md): rejecting an application requires a reason, non-empty (FR-INST-02) — same principle as [certification's revocation-reason rule](/3i/modules/certification/ui/validation-rules.md#revocation-reason-required): a consequential negative action against a real person's application isn't silent.