---
project: 3i
module: assessment
type: requirements
status: current
updated: 2026-08-23
id: 3I-ASM-REQ-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - examinations
---

# Examinations

Baseline §12.2. Eight requirements, none amended by decision.

---

## Types and Structure

| ID | Requirement |
| :---- | :---- |
| **FR-EX-01** | Exam types: **practice** and **final**. A course may have many practice exams and **one** final |

Enforced at creation — attempting to create a second `final`-type exam on a course that already has one is refused.

---

## Configuration

| ID | Requirement |
| :---- | :---- |
| **FR-EX-02** | Exam configuration: duration, pass mark, maximum attempts, cooldown, optional open and close dates, question and option randomisation |
| **FR-EX-03** | Defaults: **3 attempts with 24-hour cooldown for practice**; **3 attempts with 7-day cooldown for finals**. The highest score is retained |

The cooldown default genuinely differs by exam type — this is not "one default, occasionally overridden," it's two different baseline defaults depending on `type`, applied at creation. See [data-model.md](../data-model.md#exam). "Highest score retained" is computed across every submitted attempt, not stored as a separate field — see [data-model.md](../data-model.md#examattempt).

---

## Timing and Forfeiture

| ID | Requirement |
| :---- | :---- |
| **FR-EX-04** | Timer expiry triggers **auto-submission**. Disconnection mid-attempt results in **forfeiture** of that attempt |

Two distinct outcomes, not one — see [data-model.md](../data-model.md#the-timer-and-disconnect-detection) for how they're told apart. Both consume an attempt toward `maxAttempts`; only the auto-submitted one produces a score.

---

## Grading

| ID | Requirement |
| :---- | :---- |
| **FR-EX-05** | Objective questions are **auto-graded**. Written answers await **manual grading** by the course instructor, with no service-level commitment |

"No service-level commitment" means there's no baseline-mandated grading turnaround — unlike chat moderation's 24-hour target (FR-CHAT-10), a learner's essay answer has no promised grading window. An attempt containing any ungraded written answer stays `awaitingManualGrading = true` (see [data-model.md](../data-model.md#examattempt)) and its `score`/`passed` fields stay null until every written answer in it has been graded.

---

## Reveal Policy

| ID | Requirement |
| :---- | :---- |
| **FR-EX-06** | Correct answers and explanations are revealed **only after the learner passes or exhausts all attempts**. An instructor may override this per exam |

The baseline default is a single combined condition (pass **or** exhausted, whichever first), not two separate switches — see [data-model.md](../data-model.md#reveal-answers-policy-fr-ex-06) for the three-value policy (`standard`/`always`/`never`) this resolves to.

---

## Retakes

| ID | Requirement |
| :---- | :---- |
| **FR-EX-07** | A learner failing the final exam may retake it within the attempt limit |

No special handling beyond the ordinary attempt/cooldown mechanics already covering every exam — a failed final is not treated differently from a failed practice exam in terms of retry eligibility, only in terms of what it unlocks (a completion certificate, `certification`'s concern, not this module's).

---

## Explicitly Absent

| ID | Requirement |
| :---- | :---- |
| **FR-EX-08** | No proctoring, webcam monitoring, tab-switch detection, or IP checking |

A deliberate baseline exclusion, not a gap — nothing in this module's screens or data model should introduce any of these.

---

## Acceptance Criteria

1. An attempt left open past its duration is auto-submitted with whatever answers were last autosaved.
2. A learner who disconnects mid-attempt without submitting has that attempt marked `forfeited`, consuming one of their `maxAttempts`, with no score.
3. Under the `standard` reveal policy, answers are not shown after a failed first attempt when attempts remain; they are shown after the second failure if `maxAttempts = 2`.
4. A second `final`-type exam creation attempt on a course that already has one is refused.
5. A practice exam's cooldown defaults to 24 hours; a final exam's defaults to 168 hours (7 days), without either needing to be set explicitly.
6. An attempt containing one auto-graded MCQ and one ungraded essay answer shows `awaitingManualGrading = true` and a null `score` until the essay is graded.
7. The highest of three submitted attempts is what's reported as the learner's result for that exam.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-ASM-DM-001](../data-model.md) |
| Question bank | [3I-ASM-REQ-001](qb-question-bank.md) |
| Certificate eligibility (reads this module's output) | `certification` |