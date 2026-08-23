---
project: 3i
module: certification
type: overview
status: current
updated: 2026-08-23
id: 3I-CRT-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Certification

The module that turns "this learner did the work" into a permanent, verifiable credential — and, once issued, never lets that credential drift even if the course, the profile, or the institute's own records change underneath it.

**Module status: complete.** README, data model, requirements, and the full UI stage are written.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| CERT | Certificates | 9 |

Three decisions apply directly: [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md) (certificates snapshot everything at issuance, never resolve live), [3I-DEC-011](/3i/decisions/dec-011-attendance-certificate-without-exam.md) (no final exam → attendance certificates only), and the new [3I-DEC-028](/3i/decisions/dec-028-session-delivery-floor-attendance-eligibility.md) (a batch-level session-delivery floor gates attendance eligibility, resolving OQ-11 and settling `Mixed`-course behaviour the baseline never addressed).

## The First Module With No Forward References

Every producer this module reads from is already built: `materials` (MaterialProgress), `learning-delivery` (Session, AttendanceRecord), `assessment` (ExamAttempt), `catalogue` (Course), `identity-and-access` (Learner). This module is purely an aggregator and issuer — nothing here is flagged as waiting on a module that doesn't exist yet.

## Eligibility Is Computed, Never Pre-Checked Into a Field

Whether a learner currently *qualifies* for a certificate is a live computation over three other modules' data — it is not stored anywhere, the same principle already applied to course-level progress and derived age bands elsewhere in this project. The **Certificate** row itself is only created at the moment of actual issuance, and from that instant on it owns its own permanent copy of everything it asserts ([3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)) — eligibility computation and the issued record are two entirely different things, and the second never re-derives from the first after the fact.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-CRT-DM-001 | current |
| [requirements/cert-certificates.md](requirements/cert-certificates.md) | 3I-CRT-REQ-001 | current |
| [ui/README.md](ui/README.md) | 3I-CRT-UI-000 | current — 3 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| Denormalisation at issuance | [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md) |
| No final exam → attendance only | [3I-DEC-011](/3i/decisions/dec-011-attendance-certificate-without-exam.md) |
| Session-delivery floor, Mixed-course pooling | [3I-DEC-028](/3i/decisions/dec-028-session-delivery-floor-attendance-eligibility.md) |
| Individual attendance measured against sessions delivered | [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md) |

## Delivery

Phase 5, Assessment (§21.1) — question bank, exams, grading, certificates. This module is the certificate half; `assessment` (already built) is the question-bank/exam half.

## Open Against This Module

| Item | Note |
| :---- | :---- |
| Certificate design assets — template, institute seal, signature image | **Outstanding client dependency, §22.2 item 5.** This module is fully specified without it — the data model and eligibility logic don't need the actual artwork — but nothing can render a real certificate PDF until it arrives |
| Attendance-certificate wording for self-paced vs. batch courses | Raised in [3I-DEC-011](/3i/decisions/dec-011-attendance-certificate-without-exam.md)'s Cost section ("attendance" reads oddly with nothing to attend) — **confirmed the copy should not differ by course type**, so this is resolved as "one wording, no branching," not left open |

## Change Requests Owed to the Client

[3I-DEC-028](/3i/decisions/dec-028-session-delivery-floor-attendance-eligibility.md) is new logic the baseline doesn't state and needs §21.3 sign-off — the same tier as [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md), which it sits directly alongside. Not yet added to the consolidated change-request list in [decisions/README.md](/3i/decisions/README.md#scope-changes-against-srd-v20); worth folding in on the next pass over that document.