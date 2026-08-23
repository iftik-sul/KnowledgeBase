---
project: 3i
module: commerce
type: requirements
status: current
updated: 2026-08-20
id: 3I-CMR-REQ-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - refunds
---

# Refunds

Baseline §14.4. Five requirements, none amended by decision.

The shortest requirement set in this module, and deliberately narrow: one self-service window, everything after it is discretionary.

---

## The Window

| ID | Requirement |
| :---- | :---- |
| **FR-REF-01** | **14-day full refund** on a **first subscription payment**, requested self-service |
| **FR-REF-02** | **Renewal payments are refundable at admin discretion only** |

The distinction is on payment sequence, not on time since account creation. A first payment refunded and re-subscribed later starts a new "first payment" for refund purposes — this module does not need to track a lifetime one-refund-ever limit unless the client asks for one, which the baseline does not.

---

## Consequences

| ID | Requirement |
| :---- | :---- |
| **FR-REF-03** | Access is **revoked immediately** on refund |
| **FR-REF-04** | **Certificates already issued remain valid** |

FR-REF-03 is immediate, unlike a normal cancellation which typically runs to the end of a paid period — a refund means the payment itself is undone, so continued access would be inconsistent with that. FR-REF-04 needs no special handling: certificate validity was never conditional on subscription status to begin with, the same snapshotting that survives profile deletion ([3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)) covers this automatically. See [3I-CMR-DM-001](../data-model.md#refund).

---

## Policy Disclosure

| ID | Requirement |
| :---- | :---- |
| **FR-REF-05** | The published policy acknowledges that **Australian Consumer Law guarantees apply regardless of policy terms** |

This is CMS copy on the public refund-policy page (part of the fixed page set, FR-CMS-01), not a data field this module stores or enforces programmatically.

---

## Acceptance Criteria

1. A refund requested on day 13 of a first subscription succeeds self-service with no admin involvement; day 15 requires an admin action.
2. Access is revoked at the moment of refund, not at the end of the current billing period.
3. A certificate issued before a refund still resolves correctly on the public verification page afterward.
4. The refund-policy page states the Australian Consumer Law disclaimer verbatim from client-supplied legal copy (§22.2 dependency #3), not paraphrased by this team.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-CMR-DM-001](../data-model.md) |
| Certificate snapshotting | [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md) |
| Refund policy copy — client dependency | §22.2 item 3, [open-questions.md](/3i/open-questions.md#client-dependencies-222) |
| Subscriptions and billing | [3I-CMR-REQ-001](bill-subscriptions-and-billing.md) |
| Waivers | [3I-CMR-REQ-002](wav-waivers.md) |