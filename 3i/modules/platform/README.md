---
project: 3i
module: platform
type: overview
status: current
updated: 2026-08-23
id: 3I-PLT-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Platform

The module that holds what genuinely belongs to no functional area — the 31 non-functional requirements, and the integration contracts with Stripe, Bunny Stream, and AWS SES that every other module's third-party dependency ultimately rests on.

**Module status: complete.** README, data model, the NFR requirements document, a dedicated data-retention document, three integration contracts, and the UI stage are written. **This is the last of the thirteen modules — the project's module partition is now fully specified.**

## Scope

| Code | Area | Count |
| :---- | :---- | ----: |
| — (unprefixed NFR series) | Non-functional requirements | 31 |

**Correction against the project's own stated total, 2026-08-23:** both [3i/README.md](/3i/README.md#baseline) and [project-standards.md](/3i/project-standards.md#the-19-requirement-codes)'s module table say **32** non-functional requirements. A direct count against §20.3–20.8 gives NFR-01 through NFR-31 — **31**, not 32. Same kind of off-by-one already caught and corrected for `catalogue`'s FR count; fixed in both places in this same change, not left as a second unresolved discrepancy alongside the first.

## Not a Drawer for Anything Hard to Place

[project-standards.md](/3i/project-standards.md#platform) is explicit: this module holds the 32 (now corrected: 31) NFRs, deployment topology, the capacity baseline, and third-party integration contracts — nothing that could live in a real functional module belongs here instead. Tech stack and capacity baseline are already documented at project root ([3i/README.md](/3i/README.md#tech-stack), [3i/README.md](/3i/README.md#capacity-baseline)) and are not restated here.

## AuditLog Resolves an Implicit Dependency

NFR-09 ("audit logging of all administrative and financial actions") has been **cited by name** in already-written modules — `identity-and-access`'s [Admin — DOB Correction](/3i/modules/identity-and-access/ui/screens/admin-dob-correction.md) and [Admin — Profile Name Unlock](/3i/modules/identity-and-access/ui/screens/admin-name-unlock.md) both say a reason "should appear in the admin audit log (NFR-09)" — without `AuditLog` ever being a defined entity anywhere. This wasn't flagged as a forward reference at the time because `platform` hadn't been identified yet as where it would eventually live. It's real now — see [data-model.md](data-model.md#auditlog).

**AuditLog is the general-purpose mechanism, not a replacement for modules that already log their own actions more richly.** `communication`'s `ModerationAction` and `commerce`'s `WebhookEvent` are both already more specific and detailed than a generic audit row would be for their own domains — `AuditLog` exists for everything that doesn't already have a dedicated, richer log of its own (instructor application decisions, certificate revocation/reissuance, waiver decisions, admin course suspensions, DOB corrections, name unlocks).

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-PLT-DM-001 | current |
| [requirements/plt-non-functional-requirements.md](requirements/plt-non-functional-requirements.md) | 3I-PLT-REQ-001 | current |
| [data-retention.md](data-retention.md) | 3I-PLT-RET-001 | current — the full NFR-26 compilation, added 2026-08-23 |
| [integrations/stripe.md](integrations/stripe.md) | 3I-PLT-INT-001 | current |
| [integrations/bunny-stream.md](integrations/bunny-stream.md) | 3I-PLT-INT-002 | current |
| [integrations/aws-ses.md](integrations/aws-ses.md) | 3I-PLT-INT-003 | current |
| [ui/README.md](ui/README.md) | 3I-PLT-UI-000 | current — 1 screen, matrix, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| App store compliance (NFR-15–21) — fully written already | [app-store-compliance.md](/3i/app-store-compliance.md) |
| Tech stack, capacity baseline | [3i/README.md](/3i/README.md) |
| Sensitive-upload private-bucket discipline (NFR-10), already applied throughout | Every module handling waiver evidence, CVs, WWCC data, report exports |

## Delivery

Spans every phase in §21.1 — the NFRs and integration contracts aren't a phase of their own; they're cross-cutting concerns implemented alongside whichever functional module first needs them (Stripe alongside `commerce`, Bunny alongside `materials`, SES alongside `communication`). This module's job is to hold the contracts and requirements in one place, not to claim a delivery slot none of the others already used.

## Forward References

None. This is the last module; nothing remains for it to wait on.

## Open Against This Module

| Item | Note |
| :---- | :---- |
| Payment/invoice record retention period | [data-retention.md](data-retention.md) flags this as genuinely unspecified, tied to §22.2 item 3 (legal copy dependency) — Australian tax law likely sets a real minimum this project has no authority to guess at |
| WWCC data retention period | Same document, tied to §22.2 item 4 (WWCC legal position dependency) |

## Change Requests Owed to the Client

None. Nothing in this module amends or reverses the baseline.

## Project Status

**All thirteen modules in the partition are now specified**: `identity-and-access`, `commerce`, `catalogue`, `materials`, `learning-delivery`, `assessment`, `certification`, `instructors`, `communication`, `public-site`, `localisation`, `reporting`, `platform`. No forward references remain anywhere in the project.