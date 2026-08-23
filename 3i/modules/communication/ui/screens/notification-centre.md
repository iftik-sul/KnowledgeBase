---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CMN-UI-005
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - notifications
---

# Screen: Notification Centre

Satisfies: FR-NOT-02, FR-NOT-04

---

## Purpose

In-app history of every notification sent to this account, with read/unread state.

## Access Gate

Any authenticated role — Member, Instructor, Admin all have their own centre.

## Contents

Reverse-chronological [Notification Row](../components.md#notification-row)s. Notifications concerning a specific learner profile name that profile in the body (FR-NOT-04) — always addressed to the account holder viewing this screen, never requiring a profile-picker context to read, since notifications are account-level regardless of which profile they're about.

## Behaviour

Opening an individual row marks it read; the list itself never bulk-marks-read on scroll or on screen open. History persists regardless of later category opt-outs — turning off Billing notifications doesn't retroactively remove past billing notifications from this list, only stops future ones.

## Role Variations

Identical across roles — each sees only their own notifications.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).