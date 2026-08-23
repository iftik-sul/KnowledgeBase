---
project: 3i
module: reporting
type: data-model
status: current
updated: 2026-08-23
id: 3I-RPT-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - reporting
---

# Reporting — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## ReportExportJob

| Field | Notes |
| :---- | :---- |
| Report type | One of the eleven fixed values — see [README.md](README.md#eleven-fixed-report-types-not-a-report-builder). No code path produces a twelfth |
| Requested by | FK to Admin Account. Nullable — null when the job was produced by a `ScheduledReport` run rather than an on-demand request |
| Format | `excel`, `csv`, or `pdf` (FR-REP-02) |
| Filters | Report-type-specific parameters — date range at minimum, plus type-appropriate scoping (e.g. a specific course for course performance, a specific instructor for instructor activity). Stored as structured data, not free text, so a job's exact parameters remain inspectable after the fact |
| Status | `queued`, `running`, `completed`, or `failed` (FR-REP-04) |
| Result file | Reference to the generated export, private bucket, signed-URL access — same sensitive-file discipline as waiver evidence and instructor CVs (NFR-10) |
| Created at, completed at | |

**Runs as a background job, always** (FR-REP-04) — there is no synchronous "generate and return immediately" path for any report type, including small ones, since consistency here matters more than optimising the common case: an admin shouldn't need to know in advance whether a given export will be fast enough to wait for.

---

## ScheduledReport

| Field | Notes |
| :---- | :---- |
| Report type | Same fixed eleven |
| Recipients | Plain email addresses, **not necessarily FK to Account** — a nominated recipient (FR-REP-03) may be entirely outside the platform, an external accountant or board member with no login of their own |
| Schedule | Recurrence (daily/weekly/monthly) plus the specific day/time it runs |
| Format | `excel`, `csv`, or `pdf` |
| Filters | Same structured-parameter shape as `ReportExportJob` |
| Created by | FK to Admin Account |
| Active | Boolean — a schedule can be paused without deleting its configuration |

**Each scheduled run creates its own `ReportExportJob`** (with `requestedBy = null`, since no admin is actively waiting on it) and, on completion, **emails the file directly to every recipient** — not through `communication`'s Notification system, per [README.md](README.md#on-demand-exports-and-scheduled-reports-are-different-delivery-paths).

---

## Report Type → Source Mapping

Not a stored field — the actual query logic behind each of the eleven fixed types, documented here so the full cross-module reach of this module is visible in one place rather than inferred:

| Report type | Reads from |
| :---- | :---- |
| Learner activity | `identity-and-access` (Learner), `materials` (MaterialProgress), `learning-delivery` (Enrolment) |
| Course performance | `catalogue` (Course, Review), `learning-delivery` (Enrolment) |
| Enrolment | `learning-delivery` (Enrolment) |
| Attendance | `learning-delivery` (Session, AttendanceRecord) |
| Exam results | `assessment` (ExamAttempt) |
| Certificates issued | `certification` (Certificate) |
| Revenue (gross) | `commerce` (Subscription, invoices) — **GST separated**, per FR-REP-05, reading the GST breakout `commerce` already records on every invoice specifically for this purpose (FR-BILL-08) |
| Subscription and churn | `commerce` (Subscription) |
| Waivers granted | `commerce` (Waiver) |
| Moderation and reports handled | `communication` (ChatMessageReport, ModerationAction) |
| Instructor activity | `instructors` (InstructorProfile), `catalogue` (Course), `learning-delivery` (Batch) |

---

## Forward References

None. Every source module above already exists.

---

## Referenced By

No other module reads from this one — `reporting` is a leaf, the same shape as `public-site`: it reads outward from nine other modules but nothing in the platform's operational flow depends on this module's own data existing.

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Learner, Account | `identity-and-access` | Learner activity report |
| Course, Review | `catalogue` | Course performance report |
| MaterialProgress | `materials` | Learner activity report |
| Session, AttendanceRecord, Enrolment | `learning-delivery` | Attendance, enrolment, course performance, learner activity, instructor activity reports |
| ExamAttempt | `assessment` | Exam results report |
| Certificate | `certification` | Certificates issued report |
| Subscription, Waiver | `commerce` | Revenue, subscription/churn, waivers-granted reports |
| ChatMessageReport, ModerationAction | `communication` | Moderation report |
| InstructorProfile | `instructors` | Instructor activity report |