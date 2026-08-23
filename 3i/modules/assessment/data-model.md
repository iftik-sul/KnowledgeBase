---
project: 3i
module: assessment
type: data-model
status: current
updated: 2026-08-23
id: 3I-ASM-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - assessment
---

# Assessment — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## Question

| Field | Notes |
| :---- | :---- |
| Scope | `admin` or `instructor` (FR-QB-01) |
| Owner | FK to `identity-and-access` Account — the admin or instructor who created (or holds the independent copy of) this question |
| Type | `mcq`, `multi_select`, `true_false`, `short_answer`, or `essay` (FR-QB-05) |
| Question text | |
| Options | List, up to 6. Used for `mcq`/`multi_select` only |
| Correct answer | Type-dependent — see below |
| Marks | Required |
| Negative marks | Optional, default 0. **Capped at the question's own marks value** — not baseline-stated, a reasonable default (see [README.md](README.md#open-against-this-module)) |
| Partial credit | Boolean, meaningful only for `multi_select` |
| Difficulty | `easy` / `medium` / `hard` |
| Explanation | Optional |
| Course | Optional FK to `catalogue` Course — a question may be tagged to a course or left general |
| Copied from | Nullable self-reference. Set when this row originated as a copy of an admin question (FR-QB-02). **Provenance only** — the copy is fully independent and editable; this field is never used to constrain what can be edited, only to answer "where did this come from" if ever asked |

**Correct-answer shape by type:**

| Type | Correct answer |
| :---- | :---- |
| `mcq` | One option |
| `multi_select` | A set of options |
| `true_false` | `true` or `false` |
| `short_answer` | Optional model answer, shown to the grading instructor as a reference — **not authoritative**. Grading stays manual regardless (FR-EX-05) |
| `essay` | None. Always manually graded |

**Isolation is enforced at the query layer on every read path** ([3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md)) — an `instructor`-scope question is returned only to its owner; every other requester, including admin, gets the same not-found response a nonexistent question would produce. This applies uniformly: the question-bank screens, bulk import's row-level lookups, exam assembly, reporting, and exports all carry the same filter. There is no code path exempted from it.

---

## Exam

| Field | Notes |
| :---- | :---- |
| Course | FK to `catalogue` Course |
| Title | |
| Type | `practice` or `final`. **At most one `final` exam per course** (§12.2 context) |
| Duration | Minutes |
| Pass mark | |
| Max attempts | Default 3 (FR-EX-03) |
| Cooldown | **Default 24 hours for `practice`, 7 days (168 hours) for `final`** — the two types have different baseline defaults, not a shared one |
| Open date, close date | Optional |
| Randomise questions, randomise options | Booleans (FR-EX-02) |
| Reveal-answers policy | `standard`, `always`, or `never` — see below |
| Questions | List of Question references, each with an optional marks override for this exam specifically |

**Total marks is computed, not stored** — the sum of each assigned question's marks (or its per-exam override where set), read live rather than kept as a separately-maintained field that could drift if a question's marks changed after assembly.

### Reveal-Answers Policy (FR-EX-06)

The baseline's default rule is a single combined condition, not a menu: **correct answers and explanations are revealed once the learner has either passed or exhausted every attempt** — whichever comes first. That combined rule is what `standard` means here. An instructor may override **per exam** to `always` (reveal immediately after each submission, whether passed or not) or `never` (reveal is never shown, regardless of outcome). Every exam has exactly one of these three values; there is no fourth "partially" state.

---

## ExamAttempt

| Field | Notes |
| :---- | :---- |
| Exam | FK |
| Learner | FK to `identity-and-access` Learner — attempts are per learner, never per account |
| Attempt number | Sequential per (Exam, Learner) |
| Status | `in_progress`, `submitted`, or `forfeited` — see below |
| Started at | |
| Expires at | `startedAt` + `Exam.duration`. Server-computed and server-authoritative — never trusted from the client |
| Submitted at | Nullable |
| Answers | Autosaved progressively during `in_progress`, finalised at submission |
| Score | Nullable until every question in the attempt is graded (auto and/or manual) |
| Passed | Nullable until fully graded |
| Awaiting manual grading | Boolean — true while any `short_answer`/`essay` question in the attempt hasn't been graded yet |
| Graded by, graded at | Set on manual grading completion |

**"Highest score retained" (FR-EX-03) is computed at read time** across every `submitted` attempt for a (Exam, Learner) pair — not a separately stored "best score" field, for the same drift-avoidance reason total marks isn't stored on Exam.

### The Timer and Disconnect Detection

FR-EX-04 states two distinct outcomes and this model needs to support telling them apart:

1. **Timer expiry → auto-submission.** The attempt is graded using whatever answers were last autosaved. This is a real, scored attempt.
2. **Disconnection mid-attempt → forfeiture.** The attempt is consumed (counts toward `maxAttempts`) but produces no score and is not retried automatically.

The baseline states these outcomes but not the detection mechanism. Modelled here as: the client autosaves answers periodically while `in_progress`; a `lastHeartbeatAt` timestamp updates with each autosave. If `expiresAt` is reached while still `in_progress`, the attempt auto-submits using the last saved answers — outcome 1. If `lastHeartbeatAt` goes stale beyond a grace window **before** `expiresAt` is reached, the attempt is marked `forfeited` — outcome 2. The exact grace-window length isn't specified in the baseline; treat it as an implementation parameter, not a fixed requirement.

---

## Forward References — Resolved (2026-08-23)

This module was originally scaffolded before `certification` existed. `certification`'s `Certificate` now reads `ExamAttempt`'s pass/fail and submission state directly — this module is the producer of that fact, `certification` the consumer.

---

## Referenced By

| Module | Reads |
| :---- | :---- |
| `certification` | ExamAttempt — completion certificate eligibility depends on the final exam having been passed |
| `learning-delivery` | ExamAttempt — course-level progress aggregation includes exam completion alongside `materials`' `MaterialProgress` |
| `reporting` | Question, Exam, ExamAttempt — exam results and instructor activity reports (FR-REP-01) |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Course | `catalogue` | Owner of Exam; optional tag on Question |
| Learner | `identity-and-access` | Subject of ExamAttempt |
| Account | `identity-and-access` | Owner of Question (admin or instructor) |