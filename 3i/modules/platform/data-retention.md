---
project: 3i
module: platform
type: standard
status: current
updated: 2026-08-23
id: 3I-PLT-RET-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - privacy
  - retention
---

# Data Retention Periods

What [NFR-26](requirements/plt-non-functional-requirements.md#privacy-and-compliance-207) asks for: a documented retention period for every category of personal data the platform stores. Compiled here, once, across every module — not scattered as a per-module afterthought, since the whole point of NFR-26 is that someone can answer "how long do you keep X" without hunting through thirteen modules' worth of documents.

Three honesty levels below, marked explicitly rather than blended together: **baseline-specified** (the SRD or an existing decision states the period), **reasonable default** (this document proposes one, flagged as unconfirmed), and **genuinely unspecified** (no period exists anywhere yet, flagged as needing real input rather than a silently invented number).

---

## Baseline-Specified

| Category | Module | Retention | Basis |
| :---- | :---- | :---- | :---- |
| Waiver evidence files | `commerce` | **12 months from the decision date** | FR-WAV-08 |
| Backups | `platform` | **30 days**, point-in-time recovery within that window | NFR-02 |
| Learner progress, enrolments, exam results | `identity-and-access` | **Deleted immediately** on profile deletion | FR-FAM-10 |
| Issued certificates | `certification` | **Permanent** — survives profile deletion, account deletion, course archival, and refunds | [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md), FR-REF-04 |
| Chat message content | `communication` | Retained indefinitely; **removed** (tombstoned) on profile deletion, **kept** on account deletion | FR-CHAT-05, [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md), FR-CHAT-14 — see [communication's README](/3i/modules/communication/README.md#two-deletion-rules-that-look-similar-and-arent) for why these two differ |
| Chat moderation records, reports | `communication` | **Permanent**, survives message tombstoning | [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md) |
| Waiver audit trail (requester, decision, tier — not the evidence file itself) | `commerce` | **Permanent**, outlives the 12-month evidence-file deletion | FR-WAV-09 |

---

## Reasonable Default — Proposed Here, Not Confirmed

| Category | Module | Proposed retention | Reasoning |
| :---- | :---- | :---- | :---- |
| Blocked registration attempt (hashed session identifier) | `identity-and-access` | **90 days** | Long enough to catch a retry with an amended birth year (its entire purpose, FR-AUTH-04); a hash with no personal data attached carries little reason to keep it indefinitely |
| `AuditLog` rows | `platform` | **Permanent** | An audit record that expires defeats much of its own purpose — NFR-09 doesn't specify a period, and "keep it" is the safer default for something whose entire value is being available later, including much later |
| Notification `NotificationDeliveryLog` rows (bounce/complaint events) | `communication` | **12 months** | Operationally useful for diagnosing deliverability issues; no ongoing value once well past a year, and no safeguarding or legal reason to keep it longer |
| Report export files (the generated Excel/CSV/PDF itself, not the job record) | `reporting` | **30 days** | The signed URL already expires quickly; the underlying file has no reason to persist much beyond a period generous enough to cover "I meant to download that last week" |

---

## Genuinely Unspecified — Needs Real Input, Not a Default

| Category | Module | Why this one shouldn't get a silently invented number |
| :---- | :---- | :---- |
| **Payment and invoice records** | `commerce` | Australian tax law typically imposes a real minimum retention period (commonly around five years) that this project has no authority to guess at. Tied to the same **§22.2 item 3** legal dependency already tracked in [open-questions.md](/3i/open-questions.md) — this is a legal question, not a product one |
| **WWCC number, issuing state, expiry date** | `instructors` | Retention after an instructor leaves the platform (resignation, suspension, rejection) is a child-safety record with its own legal weight. Tied to **§22.2 item 4**, the outstanding WWCC legal-position dependency — the same lawyer input that clarifies what WWCC means for interstate/overseas instructors should also settle this |
| **Instructor CVs** | `instructors` | No baseline guidance and no obvious legal floor the way WWCC or payment records have. Lower stakes than the two above, but still not something to default without at least a product decision |

---

## What This Document Doesn't Cover

CMS content (`public-site`'s Pages and BlogPosts) is institute-authored, not personal data, and is out of scope for NFR-26 entirely. Course, material, and exam-question content is likewise not personal data in itself (the instructor's *authorship* of it is tracked via `AuditLog`/ownership fields, which are covered above).

## Related

| | |
| :---- | :---- |
| The requirement this document satisfies | [NFR-26](requirements/plt-non-functional-requirements.md#privacy-and-compliance-207) |
| Payment records dependency | [open-questions.md](/3i/open-questions.md), §22.2 item 3 |
| WWCC dependency | [open-questions.md](/3i/open-questions.md), §22.2 item 4 |