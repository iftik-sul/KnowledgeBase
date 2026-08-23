---
project: 3i
module: platform
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-PLT-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
---

# Screen: Admin Audit Log

Satisfies: NFR-09

---

## Purpose

Admin reviews the append-only record of every administrative and financial action taken on the platform.

## Access Gate

Admin only.

## Contents

A searchable, filterable list of `AuditLog` rows — by acting Account, action type, resource type, and date range. Each row shows the actor, the action, the target resource, and its structured details (a rejection reason, a revocation reason, whatever the specific action recorded).

**This screen surfaces `AuditLog` rows only** — it does not also pull in `communication`'s `ModerationAction` or `commerce`'s `WebhookEvent` history, which are richer, domain-specific logs viewed from their own modules' admin screens ([Admin Moderation Queue](/3i/modules/communication/ui/screens/admin-moderation-queue.md)'s audit tab, for instance). This is the general-purpose log, not a unified view across every kind of system record.

## Behaviour

**Read-only, absolutely** — see [validation-rules.md](../validation-rules.md#audit-log-immutability). No action on this screen ever modifies a row; the only actions available are search and filter.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).