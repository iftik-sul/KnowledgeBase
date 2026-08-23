---
project: 3i
module: platform
type: data-model
status: current
updated: 2026-08-23
id: 3I-PLT-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - platform
---

# Platform — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## AuditLog

| Field | Notes |
| :---- | :---- |
| Account | FK to the Account that performed the action. Nullable only for a genuinely system-triggered event (e.g. an automatic WWCC-expiry course suspension, `instructors`) rather than an admin's own action |
| Action | A short, stable identifier for what happened — e.g. `instructor_application_rejected`, `certificate_revoked`, `waiver_approved`, `profile_dob_corrected` |
| Resource type, resource ID | What the action was taken against — e.g. `InstructorApplication`, `Certificate`, `LearnerProfile` — and its specific record |
| Details | Structured data specific to the action — a rejection reason, a revocation reason, the before/after of a corrected field. Never sensitive raw content (a WWCC number, a waiver's evidence file) — those stay in their own private-bucket-protected records; this table references them by ID, never duplicates their contents |
| IP address | Where available |
| Created at | |

**Every administrative and financial action writes one of these rows, without exception** (NFR-09) — this is a floor, not a suggestion. A module that already has its own richer action-specific log (`communication`'s `ModerationAction`, `commerce`'s `WebhookEvent`) doesn't need to *also* write a parallel `AuditLog` row for the same event — see [README.md](README.md#auditlog-resolves-an-implicit-dependency) for which modules already have that richer alternative and which rely on this table directly.

**Append-only, never edited or deleted.** An audit record that could be altered after the fact isn't an audit record — this is the same principle the decisions register applies to itself (a decision is never edited, only superseded), extended here to operational actions rather than project-level decisions.

---

## Forward References

None. This module reads from nothing — every other module writes to `AuditLog`, not the reverse.

---

## Referenced By

Every module with an admin-facing consequential action writes to this table. Not exhaustively listed per-module here since the relationship is uniform — see [data-model.md](#auditlog)'s own description of what qualifies.

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Account | `identity-and-access` | The actor behind every logged action |