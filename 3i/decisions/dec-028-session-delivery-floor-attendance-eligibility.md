---
project: 3i
type: decision
status: current
updated: 2026-08-23
id: 3I-DEC-028
tags: [decision, certification, scope-change]
---

# A Session-Delivery Floor Gates Attendance-Certificate Eligibility (Resolves OQ-11)

## Context

[3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) measures an individual learner's attendance against sessions **delivered**, not scheduled — correct on its own terms, but it left a gap recorded as [OQ-11](../open-questions.md#resolved): a batch cancelled after 1 of 10 planned sessions still lets a learner who attended that one session receive a certificate, since 70% of one is one.

Separately, `Mixed` courses (materials **and** sessions) raised a question the baseline never addresses at all: FR-CERT-02 only defines attendance eligibility for "batch courses" (sessions) and "regular courses" (materials) — it's silent on a course with both.

Both resolved together, 2026-08-23, since the second question turned on the first.

## Decision

**1. A batch-level delivery floor, separate from and prior to DEC-021's individual-learner rule:** for any batch (Online Class or the session portion of Mixed), **at least 70% of originally scheduled sessions must actually be delivered** before **any** attendance certificate can issue to **anyone** in that batch. This is evaluated once per batch, not per learner — DEC-021's individual ≥70%-of-delivered rule only ever applies *after* this floor is cleared. A batch that never clears it produces zero attendance certificates, regardless of any individual's attendance record.

**2. For `Mixed` courses, the floor gates the whole course, not just the session component.** If the session floor fails, **no attendance certificate issues to anyone in that batch — even a learner who completed 100% of the course's materials.** This was a genuine fork (fail the whole course vs. fall back to materials-only eligibility) and the former was chosen deliberately: the floor exists to stop a near-empty course from certifying, and letting materials completion alone route around it would undermine the reason the floor exists.

**3. Once the floor clears, `Mixed` eligibility pools materials and sessions into one combined measure**, not two separate thresholds: `(materials completed + sessions attended) ÷ (total materials + sessions delivered) ≥ 70%`. The denominator uses sessions **delivered**, not originally scheduled, consistent with DEC-021's own reasoning — once the floor confirms the batch wasn't abandoned early, a learner shouldn't be penalised further for sessions the institute itself didn't hold.

**4. `Regular` (materials-only) courses are entirely unaffected** — there is no session floor concept where there are no sessions.

### Worked Examples

| Scenario | Sessions scheduled | Sessions delivered | Floor | Outcome |
| :---- | :---: | :---: | :---- | :---- |
| Online Class, cancelled early | 10 | 6 | 60% < 70% — **fails** | No attendance certificate for anyone in the batch |
| Online Class, completed | 10 | 10 | 100% ≥ 70% — clears | DEC-021 applies per learner as before |
| Mixed: 7 materials + 3 sessions, 1 of 3 sessions delivered | 3 | 1 | 33% < 70% — **fails** | No attendance certificate for anyone — **even a learner who completed all 7 materials** |
| Mixed: 7 materials + 3 sessions, all 3 delivered, learner completes all 7 materials, attends 0 sessions | 3 | 3 | 100% ≥ 70% — clears | Pooled: (7 + 0) ÷ (7 + 3) = 70% ≥ 70% — **certificate issues** |

The third and fourth rows are the same course shape with a different delivery outcome — the floor, not the pooling, is what separates them.

## Reasoning

The floor and DEC-021's rule answer two different questions that the original decision conflated into one: *was this batch delivered enough to mean anything* (the floor) versus *did this particular learner show up enough, given what was actually delivered* (DEC-021). Keeping them as two separate checks, in that order, is what makes both the OQ-11 gap and the Mixed-course silence resolvable with one consistent rule rather than two overlapping ones.

70% was chosen to match the number already established everywhere else in this area — FR-CERT-02's own attendance threshold and DEC-021's delivered-sessions rule both use it. Using a different number for the new floor would introduce a second unexplained threshold into the same feature.

## Scope

This is new logic the baseline doesn't state — requires §21.3 sign-off, same tier as DEC-021, which this decision sits directly alongside.

## Consequences

- [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md)'s own "Cost" section, which named the OQ-11 gap as an accepted trade-off, is superseded on that specific point — the gap it flagged is now closed. DEC-021 itself is not edited (per this project's append-only convention); this decision is the resolution referenced from OQ-11.
- `certification`'s eligibility computation reads `learning-delivery`'s Session/AttendanceRecord data twice, at two different scopes: once per-batch (the floor) and once per-learner (DEC-021, then the pooled measure for Mixed). Both are computed at read time, never stored — consistent with how this module treats eligibility generally.
- A `Mixed` course's instructor-facing tooling should be able to show, before a batch is even cancelled, how close it is to the 70% floor — not a requirement, but the natural implication of the floor existing at all.

## Cost

A learner who did everything right — completed every material in a Mixed course — can still end up with no certificate if the institute cancels the batch early enough. This is the accepted trade-off: the alternative (materials alone routing around the floor) was considered and rejected in favour of the floor meaning what it says.

## Related

| | |
| :---- | :---- |
| Resolves | [OQ-11](/3i/open-questions.md#resolved) |
| Sits alongside | [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) |
| Data model | [3I-CRT-DM-001](/3i/modules/certification/data-model.md) |
| Requirements | [3I-CRT-REQ-001](/3i/modules/certification/requirements/cert-certificates.md) |