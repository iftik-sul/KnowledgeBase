---
project: 3i
module: reporting
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-RPT-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
---

# Screen: Admin Scheduled Reports

Satisfies: FR-REP-03

---

## Purpose

Admin creates and manages recurring report schedules, each emailing its output directly to nominated recipients.

## Access Gate

Admin only.

## Contents

A list of every `ScheduledReport`, each showing type, recurrence, recipients, format, and active/paused state. **New Schedule** opens the same [Report Type Selector](../components.md#report-type-selector) and filter set as [Admin Report Generator](admin-report-generator.md), plus recurrence (daily/weekly/monthly, with day/time) and a recipient list (see [validation-rules.md](../validation-rules.md#schedule-recipient-validation) — plain email addresses, not required to be platform Accounts).

## Behaviour

**Pausing a schedule** (toggling `active`) stops future runs without deleting the configuration — an admin can re-enable it later without re-entering everything. **Each run is independent**: a paused-then-resumed schedule doesn't attempt to "catch up" on missed runs, it simply resumes its normal cadence from whenever it's reactivated.

**Delivery bypasses `communication`'s Notification system entirely** — the completed export is emailed directly to every recipient (see [README.md](/3i/modules/reporting/README.md#on-demand-exports-and-scheduled-reports-are-different-delivery-paths)), since recipients may not hold accounts to route preferences against.

## Role Variations

Admin only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).