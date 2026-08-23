---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CAT-UI-005
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - catalogue
  - admin
---

# Screen: Admin Course Management

Satisfies: FR-CRS-05

---

## Purpose

Admin oversight of every course on the platform — edit, suspend, or take down, regardless of status or owning instructor. Also where the flat Category list ([data-model.md](../data-model.md#category)) is managed.

## Access Gate

Admin only.

## Contents

A searchable, filterable list of **every** course — all statuses, not just `published` — with the same [Course Card](../components.md#course-card) summary plus current status. Selecting a course opens the same edit form as [Course Create / Edit](course-create-edit.md), with admin able to edit any field regardless of owning instructor.

**Suspend** and **Take down** are distinct actions with distinct meaning (see [requirements](../requirements/crs-course-catalogue-and-management.md#admin-review-and-moderation)): suspension is reversible and existing enrolled learners keep access to completed materials; take-down is the harder action, styled and worded accordingly.

**Category management** is a simple add/rename/deactivate list, reached from this screen rather than given its own screen — proportionate to how small the entity is ([data-model.md](../data-model.md#category)).

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).