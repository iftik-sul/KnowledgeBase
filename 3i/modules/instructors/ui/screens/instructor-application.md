---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-INS-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - instructors
---

# Screen: Instructor Application

Satisfies: FR-INST-01, FR-INST-03

---

## Purpose

A Member applies to become an instructor — bio, expertise, CV, and WWCC details. Reached two ways, per [3I-DEC-038](/3i/decisions/dec-038-instructor-registration-account-works-normally.md):

1. **From a dedicated "Become an Instructor" landing-page button** (new) — for someone with no existing account. This variant combines core account-creation fields with the application fields below, in one form.
2. **From account settings**, for an already-registered Member deciding to apply later — the original path, application fields only, no account fields needed since the account already exists.

## Access Gate

Any Account not already holding the Instructor role — either just-created via path 1 above, or an existing Member via path 2.

## Fields

**Path 1 (new account) additionally includes:** first name, last name, email, password, date of birth — identical fields and identical DOB evaluation to [Registration — Adult](/3i/modules/identity-and-access/ui/screens/registration-adult.md). An applicant under 18 hits [Registration Blocked — Under 18](/3i/modules/identity-and-access/ui/screens/registration-blocked-under-18.md), no exception.

**Both paths:** bio (free text), area of expertise, CV upload, WWCC number, issuing state, WWCC expiry date — see [validation-rules.md](../validation-rules.md#wwcc-field-validation) for the all-or-nothing WWCC requirement and the not-already-expired check.

## Behaviour

Submission creates an [InstructorApplication](../../data-model.md#instructorapplication) with `status = pending` and notifies admin (see [Admin Application Review](admin-application-review.md)). **A Notification is also sent to the applicant** confirming their application is under review (`communication`, FR-NOT) — added per [3I-DEC-038](/3i/decisions/dec-038-instructor-registration-account-works-normally.md), previously undocumented.

**For Path 1 specifically, submission is followed by [Email Verification](/3i/modules/identity-and-access/ui/screens/email-verification.md), then [Instructor Application Confirmation](instructor-application-confirmation.md)** — a one-time screen confirming both the verified email and the pending application together — [3I-DEC-040](/3i/decisions/dec-040-instructor-registration-confirmation-screen.md). **Path 2 has no such confirmation screen** — the account already exists and is already verified, so only the application-submitted notification applies.

**No immediate role change, and critically — for path 1 — no account restriction either.** The account works exactly like any other Member's once email-verified: full login, full ordinary platform access. Only instructor-specific capability (the instructor dashboard, course-creation tools) stays locked until approval. This is a deliberate choice, not an oversight — [3I-DEC-038](/3i/decisions/dec-038-instructor-registration-account-works-normally.md) considered and rejected a fully-locked pending-account state.

**On approval:** [InstructorProfile](../../data-model.md#instructorprofile) is created, per the existing data model. **An email is sent with a link to log in** — since the account already works, this is a "you're approved, here's where to go" notification with a shortcut, not a first-time access grant.

If this Account has a prior `rejected` application, submitting a new one is simply another row — no special "reapplying" framing is needed structurally, though the screen may reasonably show the applicant their own prior rejection reason as context.

## Role Variations

Member only (either freshly created via path 1, or pre-existing via path 2).

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring (FR-LOC-04).
