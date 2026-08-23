---
project: 3i
module: certification
type: requirements
status: current
updated: 2026-08-23
id: 3I-CRT-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - certification
---

# Certificates

Baseline §13. Nine requirements. Three decisions apply — [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md), [3I-DEC-011](/3i/decisions/dec-011-attendance-certificate-without-exam.md), [3I-DEC-028](/3i/decisions/dec-028-session-delivery-floor-attendance-eligibility.md).

---

## Types and Thresholds

| ID | Requirement |
| :---- | :---- |
| **FR-CERT-01** | Two types: **attendance** and **completion** |
| **FR-CERT-02** | Attendance certificate thresholds: batch courses ≥ 70% of sessions attended; regular courses ≥ 70% of published materials completed |
| **FR-CERT-03** | Material completion definitions (video ≥90% watched, audio ≥90% played, document ≥30s viewed, quiz/exam submitted) |

FR-CERT-02's two-branch statement (batch vs. regular) is extended by [3I-DEC-028](/3i/decisions/dec-028-session-delivery-floor-attendance-eligibility.md) to cover the `Mixed` case the baseline leaves silent, and adds the batch-level delivery floor the original text doesn't mention at all. FR-CERT-03's per-type completion definitions are `materials`' concern, not restated here — see [3I-MTL-DM-001](/3i/modules/materials/data-model.md#materialprogress).

---

## Completion Certificate

| ID | Requirement |
| :---- | :---- |
| **FR-CERT-04** | The completion certificate is issued after the final exam is passed |

**Where a course has no final exam, this path never applies** — [3I-DEC-011](/3i/decisions/dec-011-attendance-certificate-without-exam.md): only the attendance certificate is ever available for such a course, not a permanently-unmet completion requirement.

---

## Language

| ID | Requirement |
| :---- | :---- |
| **FR-CERT-05** | Certificates are **English only**, regardless of user locale |

No exception for the attendance-vs-completion distinction or for course language — a certificate for an Arabic-taught course is still issued in English.

---

## Certificate Content and Verification

| ID | Requirement |
| :---- | :---- |
| **FR-CERT-06** | Each certificate carries a unique verification code, a QR code, the institute seal, and a digital signature image |
| **FR-CERT-07** | A **public verification page** resolves a verification code to learner name, course title, type, and issue date. No authentication required |

The QR code encodes a link to the verification page for that certificate's code — scanning it and looking up the code manually produce the same result. **FR-CERT-06's visual assets (seal, signature image) are blocked on an outstanding client dependency** — see [README.md](../README.md#open-against-this-module), §22.2 item 5. The verification page itself (FR-CERT-07) is not blocked by this — it's a data lookup, not a rendering of the certificate artwork.

---

## Permanence

| ID | Requirement |
| :---- | :---- |
| **FR-CERT-08** | Learner name and course title are **snapshotted at issue**. Certificates remain valid and verifiable after profile deletion, account deletion, or course archival |

Full mechanism in [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md) — not restated here. The requirement-level summary: a certificate never re-derives its own content from live records, by design, not as an optimisation.

---

## Revocation

| ID | Requirement |
| :---- | :---- |
| **FR-CERT-09** | Admin may revoke a certificate with a recorded reason. Revoked certificates show as revoked on the verification page |

**Correcting an error is a reissuance, not an edit** — revoke the original (with `revokeReason = "Correction — reissued"`), issue a corrected new one, link them. See [data-model.md](../data-model.md#reissuance) for the full mechanism, which is this module's own reasonable implementation of [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)'s principle rather than a separately baseline-mandated flow.

---

## Acceptance Criteria

1. A learner at 69% attendance (or material completion) cannot obtain a certificate; at 70% they can.
2. A batch cancelled at 60% of scheduled sessions delivered produces no attendance certificates for anyone in it, regardless of individual attendance.
3. A `Mixed`-course learner who completed 100% of materials but whose batch's session-delivery floor failed receives no attendance certificate.
4. A `Mixed`-course learner in a batch that cleared the floor, who completed all materials and attended zero delivered sessions, receives an attendance certificate if the pooled percentage still clears 70%.
5. The QR code on a generated certificate resolves to the correct verification page.
6. Verification still works after the learner profile is deleted.
7. Certificates render Arabic and Bengali learner names correctly within an English-only certificate.
8. A course with no final exam never produces a completion certificate, and never shows one as "pending" — the option simply doesn't exist for it.
9. Revoking a certificate for correction produces two independently verifiable records: the original, showing revoked with reason, and the reissued replacement, showing current.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-CRT-DM-001](../data-model.md) |
| Denormalisation | [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md) |
| No-exam courses | [3I-DEC-011](/3i/decisions/dec-011-attendance-certificate-without-exam.md) |
| Session-delivery floor, Mixed-course pooling | [3I-DEC-028](/3i/decisions/dec-028-session-delivery-floor-attendance-eligibility.md) |