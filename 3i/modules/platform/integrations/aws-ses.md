---
project: 3i
module: platform
type: integration
status: current
updated: 2026-08-23
id: 3I-PLT-INT-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - integration
  - aws-ses
---

# Integration: AWS SES

Contract with AWS SES (Sydney region), the platform's email delivery provider (FR-NOT-07). Consumed primarily by `communication`, with `reporting`'s scheduled-report delivery reusing the same infrastructure directly. Documented here per the same `integration` document-type convention as [Stripe](stripe.md) and [Bunny Stream](bunny-stream.md).

---

## What 3i Uses

- **Transactional and notification email** — every `communication` trigger with email enabled reaching a recipient goes through SES.
- **Domain authentication** — SPF, DKIM, and DMARC configured on the institute's own domain (FR-NOT-07), not a shared/generic sending domain — this matters for deliverability and for the domain's own reputation being the institute's to manage, not a third party's.
- **Delivery/bounce/complaint webhooks** — what populates `communication`'s `NotificationDeliveryLog` (FR-NOT-08).

## Two Consumers, One Infrastructure

`communication` routes every category-based notification through this same SES connection, checking `NotificationPreference` first. `reporting`'s scheduled-report emails **also** go through SES directly, but **bypass** `communication`'s category/preference system entirely — a scheduled report's recipient may not hold a platform Account at all, so there's no preference record to check ([reporting's README](/3i/modules/reporting/README.md#on-demand-exports-and-scheduled-reports-are-different-delivery-paths) already states this). Both consumers hit the same SES connection and the same domain authentication; only `communication`'s path is preference-gated.

## Related

| | |
| :---- | :---- |
| Primary owning module | `communication` |
| Secondary consumer | `reporting` (scheduled reports, bypasses category preferences) |
| Delivery/bounce logging | `communication`'s `NotificationDeliveryLog` |