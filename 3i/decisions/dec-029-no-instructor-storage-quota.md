---
project: 3i
type: decision
status: current
updated: 2026-08-23
id: 3I-DEC-029
tags: [decision, instructors, scope-change]
---

# No Per-Instructor Storage Quota

## Context

FR-INST-05 specifies a 50 GB storage quota per instructor, admin-adjustable, with enforcement expected at material-upload time in `materials`. When `instructors` was scaffolded, the quota field (`InstructorProfile.storageQuotaBytes`) and a live-computed `storageUsed` were both specified, but enforcement itself was flagged as not yet added to `materials`' own upload validation — a genuine gap between the two modules.

Confirmed 2026-08-23: **there will be no storage quota for instructors.**

## Decision

**FR-INST-05 is dropped.** No per-instructor storage quota exists, in any form — no quota field, no usage tracking, no enforcement at upload time. Instructors upload material within the per-file size limits `materials` already enforces (FR-MAT-02: video 4 GB, audio 500 MB, document 100 MB, image 10 MB) and nothing further constrains their total storage across every course they own.

This closes the gap the flag identified — not by building the missing enforcement, but by confirming the requirement it would have enforced doesn't apply.

## Reasoning

Not recorded beyond the confirmation itself — this is a client/product decision to drop a requirement, not an interpretation of an ambiguity, and the reasoning behind it belongs to Saitama and the client rather than something this repository infers.

## Scope

**Reverses FR-INST-05 outright**, the same category of change as [3I-DEC-023](dec-023-no-standalone-accounts-under-18.md)'s removal of standalone accounts — requires §21.3 sign-off, added to the consolidated change-request list.

## Consequences

- **`InstructorProfile`** ([3I-INS-DM-001](/3i/modules/instructors/data-model.md)) drops `storageQuotaBytes` and `storageUsed` entirely — not set to unlimited, genuinely absent as fields.
- **`materials`' upload validation** needed no change, since the enforcement this decision removes the need for was never built there in the first place — the flagged gap is closed by removing what it was tracking, not by finishing it.
- **[Admin Instructor Management](/3i/modules/instructors/ui/screens/admin-instructor-management.md)** loses its storage-quota display and edit control; the [Storage Usage Bar](/3i/modules/instructors/ui/components.md#storage-usage-bar) component is removed.
- `reporting`'s instructor activity report (FR-REP-01) no longer has a storage dimension to report on — it never listed one explicitly, so no correction needed there.

## Cost

None identified. Removes a feature rather than adding one.

## Related

| | |
| :---- | :---- |
| Reverses | FR-INST-05 |
| Data model updated | [3I-INS-DM-001](/3i/modules/instructors/data-model.md) |
| Requirements updated | [3I-INS-REQ-001](/3i/modules/instructors/requirements/inst-instructor-onboarding.md) |