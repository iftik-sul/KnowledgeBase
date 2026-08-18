---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-011
tags: [decision, certification]
---

# A Course With No Final Exam Yields Attendance Certificates Only

## Context

There are two certificate types, attendance and completion (FR-CERT-01). The completion certificate is issued after the final exam is passed (FR-CERT-04).

Nothing requires a course to have a final exam. A Regular self-paced course may consist entirely of materials, in which case FR-CERT-04 can never fire.

## Decision

**Where a course has no final exam, only the attendance certificate is available.** Taken in review, 2026-08-18.

## Consequences

- The completion certificate keeps its meaning. It certifies assessed achievement, and it is never issued without assessment.
- Attendance remains reachable for these courses through the materials route: ≥70% of published materials completed (FR-CERT-02), with completion defined per material type in FR-CERT-03.
- The course editor should state which certificates a course can produce, so an instructor building a materials-only course knows before publishing that completion is unavailable. Not currently a requirement.

## Cost

A learner finishing every material in a self-paced course receives a certificate that says attendance, which reads oddly for self-paced study — there is nothing to attend. The wording on the certificate itself may need to differ by course type, which touches the client's certificate template (§22.2 item 5) and is worth raising before that artwork is commissioned.
