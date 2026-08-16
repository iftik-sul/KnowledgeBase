---
project: 3i
type: decision
status: current
updated: 2026-08-16
id: 3I-DEC-005
tags: [decision, data-model, certification]
---

# Certificates Are Denormalised at Issuance

## Context

A certificate is a statement about a moment: this learner, this course, this result, this date. Normalised against live records, it stops being that. Rename the course and every historical certificate silently rewrites itself. Delete the learner profile and the certificate loses its subject.

Profile deletion is not hypothetical here. A guardian may remove a learner profile, and privacy law may require that removal to be honoured.

## Decision

**A certificate carries its own copy of everything it asserts** — learner name, course title, result, issue date, issuing authority — captured at issuance. It does not resolve these from live records at render time.

## Consequences

- A certificate issued in 2026 still reads correctly in 2030 after the curriculum has been restructured twice.
- Certificate verification survives profile deletion. The certificate remains verifiable as a historical fact without retaining the profile it was issued to.
- Correcting a genuine error — a misspelled name — requires reissuing rather than editing upstream. This is the correct behaviour for a credential and should be presented to the client as such.

## Cost

Denormalisation here is deliberate and must not be "fixed" by a later reviewer who sees duplicated course titles and reaches for a foreign key. Any schema review that flags this should be pointed at this document.
