---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - question-bank
  - admin
---

# Screen: Admin Question Bank

Satisfies: FR-QB-01, FR-QB-05, FR-QB-06

---

## Purpose

The shared, admin-authored question bank that instructors can browse and copy from.

## Access Gate

Admin only for creating/editing/deleting. **Admin has no visibility into any instructor's private bank from here or anywhere else** ([3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md)) — this screen only ever shows `admin`-scope questions, never a cross-instructor view.

## Contents

Same [Question Card](../components.md#question-card) grid and Add/Edit/Delete pattern as [Question Bank Manage](question-bank-manage.md), scoped to `admin`. No "browse instructor banks" tab exists — there is nothing for it to show.

## Role Variations

Admin only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).