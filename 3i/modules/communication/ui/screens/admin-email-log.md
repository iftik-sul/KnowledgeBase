---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CMN-UI-007
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - notifications
  - admin
---

# Screen: Admin Email Log

Satisfies: FR-NOT-07, FR-NOT-08

---

## Purpose

Admin visibility into email delivery, bounce, and complaint events.

## Access Gate

Admin only.

## Contents

Searchable list of `NotificationDeliveryLog` rows for the `email` channel — recipient, notification category/trigger, status (`sent`/`bounced`/`complained`), timestamp. Push-channel delivery logs are out of scope for this specific screen's SES-focused framing (FR-NOT-07 names SES specifically for email); push delivery status, if tracked, belongs to a general delivery-log view rather than this SES-specific one.

## Behaviour

This screen is read-only — diagnostic visibility, not an action surface. A high bounce rate against one domain is the kind of thing this screen exists to surface, though no automated alerting on it is specified in the baseline.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).