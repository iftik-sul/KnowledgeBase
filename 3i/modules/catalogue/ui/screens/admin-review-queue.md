---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CAT-UI-004
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - catalogue
  - admin
---

# Screen: Admin Review Queue

Satisfies: FR-CRS-04

---

## Purpose

Admin approves or rejects courses tagged under 13, before they can go live.

## Access Gate

Admin only.

## Contents

A queue of every course in `pending_review` status, each showing the full course detail (same fields as [Course Detail](course-detail.md)) plus the instructor's identity, so the reviewer has everything needed to judge age-appropriateness without navigating away.

**Approve** moves the course to `published`. **Reject** moves it back to `draft` with a **required reason field**, recorded and shown to the instructor — same pattern as instructor application rejection (FR-INST-02), reused rather than inventing a second rejection-reason convention.

## Behaviour

No bulk actions — each course is reviewed individually, since the judgement being made (is this genuinely appropriate for the age tag it carries) is not one that scales safely to a batch "approve all" action.

Queue sorted oldest-submission-first by default, so nothing sits unreviewed indefinitely — not a baseline-specified requirement, standard practice for a review queue with safeguarding weight.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).