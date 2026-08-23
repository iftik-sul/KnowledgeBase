---
project: 3i
module: certification
type: data-model
status: current
updated: 2026-08-23
id: 3I-CRT-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - certification
---

# Certification — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## Certificate

| Field | Notes |
| :---- | :---- |
| Type | `attendance` or `completion` (FR-CERT-01) |
| Learner name (snapshot) | Captured at issuance, never re-read from the live Learner record ([3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)) |
| Course title (snapshot) | Same — captured at issuance |
| Issued at | |
| Verification code | Unique. What the public verification page resolves (FR-CERT-06, FR-CERT-07) |
| Issuer name | Static — the institute, not a per-certificate field that varies |
| Language | Always `en` (FR-CERT-05, FR-LOC-06) — not a locale-dependent field, regardless of the learner's or account's own locale |
| Revoked at, revoke reason | Nullable. Set only by admin action (FR-CERT-09). A revoked certificate is never deleted — it remains resolvable on the verification page, shown as revoked |
| Reissued from | Nullable self-reference — set when this certificate supersedes an earlier one issued in error. See Reissuance below |
| Learner (reference) | Nullable FK to `identity-and-access` Learner — **internal cross-reference only.** Never read by the verification page, which resolves entirely from the snapshot fields above. Null after the learner profile is deleted; the certificate remains fully verifiable regardless (FR-FAM-10, [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)) |
| Course (reference) | Nullable FK to `catalogue` Course — same internal-only, non-authoritative role as the learner reference |

**The snapshot fields are the only thing verification ever reads.** The two FK references exist purely for internal tooling (an admin looking up "which certificates trace back to this course") and are allowed to go null or dangle without affecting a single already-issued certificate's correctness.

### Reissuance

[3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md) establishes that correcting an error (a misspelled name, for instance) means **reissuing, not editing** — this module's mechanism, confirmed 2026-08-23: **revoke the original certificate** (`revokedAt` set, `revokeReason = "Correction — reissued"`) and **issue a new one** with the corrected snapshot, its `reissuedFrom` field pointing at the original. Both remain independently resolvable on the verification page — the old one shows as revoked with a note explaining why, the new one shows as current. This is this module's own reasonable implementation of DEC-005's principle, not a separately baseline-mandated procedure.

---

## Eligibility — Computed, Not Stored

Whether a learner currently qualifies for a certificate is computed live, every time it's checked, from three other modules' records. Nothing below is a field on any entity — it's the logic that decides when a `Certificate` row gets created.

### Attendance Eligibility (FR-CERT-02, FR-CERT-03)

| Course type | Batch-level gate ([3I-DEC-028](/3i/decisions/dec-028-session-delivery-floor-attendance-eligibility.md)) | Individual learner threshold |
| :---- | :---- | :---- |
| `Regular` | None — no sessions exist | ≥ 70% of the course's materials completed (`materials`' MaterialProgress, per-type thresholds in [3I-MTL-DM-001](/3i/modules/materials/data-model.md#materialprogress)) |
| `Online Class` | Sessions delivered ≥ 70% of originally scheduled, per batch. **Fails closed** — if this doesn't clear, no attendance certificate issues to anyone in the batch | ≥ 70% of sessions **delivered** attended ([3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md)) |
| `Mixed` | Same floor as `Online Class`, gating the **whole course** — confirmed explicitly: a learner who completed 100% of materials still gets nothing if the session floor fails | Pooled: `(materials completed + sessions attended) ÷ (total materials + sessions delivered) ≥ 70%` |

Full reasoning and worked examples in [3I-DEC-028](/3i/decisions/dec-028-session-delivery-floor-attendance-eligibility.md) — not restated here.

### Completion Eligibility (FR-CERT-04)

The course's `final`-type Exam has an ExamAttempt with `passed = true` for this Learner (`assessment`'s ExamAttempt).

**If the course has no final exam at all, completion eligibility never exists** — not "not yet met," genuinely unreachable ([3I-DEC-011](/3i/decisions/dec-011-attendance-certificate-without-exam.md)). Only the attendance path applies to such a course.

### When Eligibility Is Checked

A check runs whenever an event could plausibly change the answer — an AttendanceRecord is marked, a MaterialProgress crosses its completion threshold, an ExamAttempt is graded as passed, or (for the batch-level floor) a Session is cancelled or a batch is otherwise concluded. On a newly-met eligibility, a Certificate is issued automatically — there is no learner-initiated "claim my certificate" action anywhere in the baseline, and this module doesn't invent one.

**A Certificate is issued at most once per (Learner, Course, Type)** — re-crossing an already-certified threshold (re-watching a completed video, for instance) never produces a duplicate.

---

## Forward References

None. See [README.md](README.md#the-first-module-with-no-forward-references).

---

## Referenced By

| Module | Reads |
| :---- | :---- |
| `identity-and-access` | Certificate — the guardian dashboard's per-profile certificate list, and the deleted-profile "surviving certificates only" view (both already referenced from that module's own screens) |
| `commerce` | Certificate — FR-REF-04, a refund does not affect already-issued certificates |
| `reporting` | Certificate — "certificates issued" report (FR-REP-01) |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Learner | `identity-and-access` | Name snapshot source at issuance; internal reference afterward |
| Course | `catalogue` | Title snapshot source at issuance; type (Regular/Online Class/Mixed) drives which eligibility branch applies |
| MaterialProgress | `materials` | Attendance eligibility (Regular, and the material half of Mixed) |
| Session, AttendanceRecord | `learning-delivery` | Attendance eligibility (Online Class, and the session half of Mixed), and the batch-level delivery floor |
| ExamAttempt | `assessment` | Completion eligibility |