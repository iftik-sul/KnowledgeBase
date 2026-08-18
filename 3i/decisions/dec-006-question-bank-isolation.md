---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-006
tags: [decision, assessment, security]
---

# Question Bank Isolation at the Query Layer, Returning 404

## Context

There are two bank scopes, admin and instructor (FR-QB-01). Instructors may copy admin questions into their own bank, where the copy becomes independent and editable (FR-QB-02).

Instructor questions are private to their owner and invisible to other instructors **and to admins** (FR-QB-03). That last part is unusual and deliberate: administrative reach stops at the question bank.

Schema structure describes the relationship but does not enforce it. A query that omits the filter returns everything the schema permits. It produces a working feature with a leak in it, and nothing in testing fails.

## Decision

**Isolation is enforced at the query layer, on every read path touching questions** (FR-QB-04).

**A request for another instructor's bank returns 404, not 403** (FR-QB-04). A 403 confirms the bank exists. A 404 does not.

## Consequences

- Every question read carries its scope filter as a requirement, not an optimisation.
- Admin tooling, reporting, and exports are in scope for the restriction. This is where the filter is most often forgotten, because those paths are written against a different mental model — and admin visibility is exactly what FR-QB-03 forbids.
- Bulk CSV import (FR-QB-07) writes into a scope and must validate the target scope belongs to the requester.

## Cost

Enforcement living in application code can be bypassed by application code. Accepted in exchange for explicitness: a filter visible in every query is more reviewable than a schema constraint nobody reads.

If the boundary later needs to hold against a hostile actor rather than developer error, this should be revisited toward row-level security rather than patched.

## Correction

An earlier version omitted that admins are also excluded, and did not specify 404 over 403. Both are explicit in FR-QB-03 and FR-QB-04.
