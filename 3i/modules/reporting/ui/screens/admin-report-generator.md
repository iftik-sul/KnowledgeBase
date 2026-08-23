---
project: 3i
module: reporting
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-RPT-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
---

# Screen: Admin Report Generator

Satisfies: FR-REP-01, FR-REP-02, FR-REP-04

---

## Purpose

Admin generates an on-demand export of any of the eleven fixed report types, and tracks/downloads completed jobs.

## Access Gate

Admin only.

## Contents

[Report Type Selector](../components.md#report-type-selector), filters (date range required — see [validation-rules.md](../validation-rules.md#filter-requirements-per-report-type), plus type-specific optional narrowing), format choice (Excel/CSV/PDF), and a **Generate** action. Below it, a history list of this admin's own past `ReportExportJob`s (and, since this is admin tooling rather than a per-user personal list, arguably every admin's — not specified in the baseline, reasonable default: shared visibility across admins, since reports are institutional artifacts, not personal ones), each with an [Export Job Status Badge](../components.md#export-job-status-badge).

## Behaviour

**Generate always queues a background job** (FR-REP-04) — there is no synchronous path, even for a report an admin expects to be small. The admin can navigate away immediately; the job list (and, reasonably, an in-app notification on completion — though this module doesn't specify routing that through `communication`'s category system, since it's operational feedback to the requesting admin, not one of `communication`'s own defined trigger categories) reflects progress without requiring the screen to stay open.

**A completed job's download link is a signed URL**, same private-bucket discipline as every other sensitive export in this project (NFR-10) — never a permanent public link.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).