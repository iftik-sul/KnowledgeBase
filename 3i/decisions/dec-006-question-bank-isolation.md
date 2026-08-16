---
project: 3i
type: decision
status: current
updated: 2026-08-16
id: 3I-DEC-006
tags: [decision, assessment, security]
---

# Question Bank Isolation Is Enforced at the Query Layer

## Context

Question banks must not leak across their boundary. Schema structure — a foreign key from question to bank, from bank to course — describes the relationship but does not enforce it. A query that omits the filter returns everything the schema permits, which is every question in the system.

This is a quiet failure. It produces a working feature with a leak in it, and nothing in testing fails.

## Decision

**Isolation is enforced at the query layer**, explicitly, on every read path that touches questions. The schema expresses the relationship; it is not treated as the control.

## Consequences

- Every question read carries its scope filter as a requirement, not as an optimisation.
- Review of assessment code checks the filter's presence specifically. Its absence is a defect regardless of whether the feature behaves correctly in testing.
- Bulk operations, exports, and reporting paths are in scope. These are where the filter is most often forgotten, because they are written against a different mental model than the learner-facing paths.

## Cost

Enforcement that lives in application code can be bypassed by application code. This decision accepts that in exchange for explicitness, on the basis that a filter visible in every query is more reviewable than one hidden in a schema constraint.

Should the isolation boundary later need to be defensible against a hostile actor rather than against developer error, this decision should be revisited — likely toward row-level security — rather than patched.
