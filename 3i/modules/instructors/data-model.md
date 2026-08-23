---
project: 3i
module: instructors
type: data-model
status: current
updated: 2026-08-23
id: 3I-INS-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - instructors
---

# Instructors — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## InstructorApplication

| Field | Notes |
| :---- | :---- |
| Account | FK to `identity-and-access` Account — the applicant |
| Bio | FR-INST-01 |
| Area of expertise | FR-INST-01 |
| CV | File upload, private bucket (NFR-10 — same sensitive-upload discipline as waiver evidence and WWCC data) |
| WWCC number, issuing state, expiry date | FR-INST-03, captured at application |
| Status | `pending`, `approved`, `rejected` |
| Reviewed by | FK to an Admin Account, nullable until reviewed |
| Reviewed at | Nullable |
| Rejection reason | Nullable, required when `status = rejected` (FR-INST-02) |
| Submitted at | |

**Append-only history, one row per attempt.** A rejected applicant may re-apply (FR-INST-02) — that's a new `InstructorApplication` row, not an edit to the rejected one, so the full history of attempts against one Account remains visible rather than being overwritten.

**Approval is what creates the `InstructorProfile` below** (or reactivates an existing one — see Re-approval). The application itself never grants the Instructor role directly; that's a consequence of approval, handled the same way [3I-DEC-007](/3i/decisions/dec-007-rbac-without-hardcoded-roles.md) treats every role assignment — as data, not a special-cased code path.

---

## InstructorProfile

| Field | Notes |
| :---- | :---- |
| Account | **Primary key is the Account's own id** — not a separate generated id. See [README.md](README.md#instructor-is-a-role-held-by-an-account-not-a-separate-identity) for why |
| WWCC number, issuing state | Current values — may differ from the originating application if renewed since (see WWCC Renewal below) |
| WWCC expiry date | **The field [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md)'s scheduling guard and FR-INST-04's teaching block both read.** Real, queryable, kept current — not a one-time snapshot from the application |
| WWCC expiry alert sent at | Nullable. Set when the 60-day alert (FR-INST-03) fires, so the same instructor's imminent expiry doesn't re-alert admin daily. Cleared on renewal |
| Storage quota | Bytes. Default 50 GB (FR-INST-05), admin-adjustable per instructor |
| Storage used | Computed, not stored — sum of upload sizes across every Material this instructor owns in `materials`, read live rather than kept as a running counter that could drift |
| Suspended at, suspension reason | Nullable. Set by admin action (FR-INST-07) or, distinctly, by automatic WWCC-expiry enforcement (FR-INST-04) — both use the same fields, but the two triggers are logged differently; see FR-INST-04 Enforcement below |

**Created once, on first approval.** Subsequent approvals after a suspension (see Re-approval) update this same row rather than creating a second one — there is exactly one `InstructorProfile` per Account, ever, matching the one-Account-one-identity principle this module is built around.

### WWCC Renewal

Not specified in the baseline who updates an expiring WWCC. Modelled as **instructor-initiated** — the instructor submits new WWCC details (number, state, expiry) directly against their own `InstructorProfile`, no fresh `InstructorApplication` required, since this is credential upkeep, not a new bid to become an instructor. A renewal clears `wwccExpiryAlertSentAt` and, where FR-INST-04 had auto-suspended courses for expiry, is the trigger that would let an admin reinstate them (not automatic — see FR-INST-04 Enforcement).

### FR-INST-04 Enforcement — What "Cannot Continue Teaching" Actually Does

Two distinct moments, both reading `wwccExpiryDate`:

1. **At course creation/publish**, for any course tagged with a minimum age under 18: refused if the instructor's WWCC is already expired. This is a `catalogue`-side check reading this module's data, not something `catalogue`'s own spec needed to change — it's an additional validation against a field that now exists.
2. **At the moment expiry actually passes** (today ≥ `wwccExpiryDate`, no renewal in between): every currently-`published` course this instructor owns with a minimum age under 18 is automatically moved to `suspended`, using the exact status transition `catalogue` already defines (see [3I-CAT-DM-001](/3i/modules/catalogue/data-model.md#publish-gate)) — this module doesn't invent a new course state, it just triggers a transition catalogue's own data model already supports. This is distinct from admin-initiated suspension (FR-INST-07): same mechanism, different trigger, and worth distinguishing in the audit trail (`suspensionReason` states which).

---

## Re-approval After Suspension

The baseline doesn't describe reinstating a suspended instructor explicitly, but FR-INST-02's approval flow is the natural mechanism: admin re-approves, which for an Account that already has an `InstructorProfile` clears `suspendedAt`/`suspensionReason` rather than creating a new profile. Courses suspended by that admin action are **not** automatically republished — each needs its own review, since whatever caused the suspension (WWCC lapse, conduct issue, anything else) may have implications beyond just "the instructor is active again." Reasonable default, not baseline-specified.

---

## Forward References

None. Every field this module needs — Account, Course, Batch — is already built.

---

## Referenced By

| Module | Reads |
| :---- | :---- |
| `catalogue` | InstructorProfile — `Course.instructorId` resolves here; FR-CRS-07's instructor-name search; FR-INST-04's course-creation-time check |
| `learning-delivery` | InstructorProfile — `Batch.instructorId`; `wwccExpiryDate` for the scheduling guard ([3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md)) |
| `materials` | InstructorProfile — `storageQuotaBytes`, for upload-time enforcement (see [README.md](README.md#open-against-this-module) — not yet added to `materials`' own validation rules) |
| `reporting` | InstructorApplication, InstructorProfile — instructor activity reports (FR-REP-01) |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Account | `identity-and-access` | The identity every InstructorApplication and InstructorProfile is keyed to |
| Course | `catalogue` | Target of the age-tag check at creation, and of automatic suspension on WWCC expiry |
| Material | `materials` | Summed for `storageUsed`'s live computation |