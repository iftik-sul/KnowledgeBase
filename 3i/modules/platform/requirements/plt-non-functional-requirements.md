---
project: 3i
module: platform
type: requirements
status: current
updated: 2026-08-23
id: 3I-PLT-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - platform
  - nfr
---

# Non-Functional Requirements

Baseline §20. Thirty-one requirements (corrected from the project's previously-stated 32 — see [README.md](../README.md#scope)), organised into the same five subsections the baseline itself uses. App store compliance (§20.6, NFR-15–21) is fully covered in [app-store-compliance.md](/3i/app-store-compliance.md) and only linked here, not restated.

---

## Availability and Recovery (§20.3)

| ID | Requirement |
| :---- | :---- |
| **NFR-01** | Uptime target **99.5%**, excluding announced maintenance |
| **NFR-02** | Daily automated PostgreSQL backups, **30-day retention**, point-in-time recovery |
| **NFR-03** | **RPO 24 hours, RTO 8 hours** |
| **NFR-04** | Restore tested at handover and **quarterly thereafter** |
| **NFR-05** | Uptime monitoring, error tracking (Sentry), and alerting **from day one** |

NFR-04's quarterly restore test is an ongoing operational commitment, not a one-time handover checkbox — it should appear on whatever operational calendar or runbook the handover documentation (§21.4) produces.

---

## Security (§20.4)

| ID | Requirement |
| :---- | :---- |
| **NFR-06** | All data in transit over **TLS**. All data at rest **encrypted** |
| **NFR-07** | All data resident in **Sydney** |
| **NFR-08** | Rate limiting on **authentication, enrolment, and upload** endpoints |
| **NFR-09** | **Audit logging** of all administrative and financial actions |
| **NFR-10** | Sensitive uploads (waiver evidence, CVs, WWCC data) are **private-bucket only** |
| **NFR-11** | OWASP Top 10 addressed; dependency scanning in CI |

NFR-08's three named endpoint categories already have their own rate-limit specifics elsewhere — login lockout (FR-AUTH-09), PIN lockout ([3I-DEC-022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md)) — this requirement is the umbrella; those decisions are the actual numbers. NFR-09 is [data-model.md](../data-model.md#auditlog)'s `AuditLog`. NFR-10's private-bucket discipline is already applied consistently everywhere it's needed — waiver evidence (`commerce`), instructor CVs (`instructors`), report exports (`reporting`) — this is the umbrella statement, not new instruction to any of them.

---

## Accessibility and Compatibility (§20.5)

| ID | Requirement |
| :---- | :---- |
| **NFR-12** | **WCAG 2.2 Level AA** on public and learner-facing web: semantic HTML, keyboard navigation, visible focus, 4.5:1 contrast, labelled forms, alt text, captions on video, reduced-motion support |
| **NFR-13** | Browsers: current and previous major versions of Chrome, Edge, Safari, Firefox |
| **NFR-14** | **Android 8.0 (API 26)+**, **iOS 14+** |

NFR-12 is the requirement every single screen document across every module already cites ("Standard, 4.5:1 (NFR-12)") — this is the umbrella; individual screens don't need to be revisited, they already comply with the citation pattern. Video captions specifically are `materials`' FR-MAT-06.

---

## App Store Compliance (§20.6)

| ID | Requirement |
| :---- | :---- |
| **NFR-15–21** | Multiplatform services submission model, no purchase surface, web-first registration, neutral unsubscribed status, 13+ age rating, parent-addressed marketing, demo credentials for review |

**Fully specified in [app-store-compliance.md](/3i/app-store-compliance.md)** — not restated here. That document already resolved what was OQ-09 and is the authoritative statement of this whole cluster, cited from `commerce`, `communication`, and this module alike.

---

## Privacy and Compliance (§20.7)

| ID | Requirement |
| :---- | :---- |
| **NFR-22** | Australian Privacy Act 1988 and the APPs; **GDPR** where EU/UK learners enrol |
| **NFR-23** | Consent banner for analytics, **defaulting to off** for non-essential categories |
| **NFR-24** | Self-service **data export** and **account deletion** |
| **NFR-25** | Analytics: GA4, Firebase, Sentry — **Google Signals and all ads-personalisation disabled**, ad ID collection disabled, **no advertising SDKs** |
| **NFR-26** | Documented **retention periods** for every personal data category |
| **NFR-27** | A written **social media minimum age self-assessment**, reviewed by the client's lawyer, **re-run whenever social features change** |

NFR-24's account deletion is `identity-and-access`'s territory (profile/account deletion already fully specified there) — this requirement is the umbrella that module's existing behaviour already satisfies.

**NFR-26 is fully compiled in [data-retention.md](../data-retention.md)**, 2026-08-23 — not restated here. That document is honest about which periods come from the baseline, which are this project's own reasonable defaults, and which are genuinely unresolved pending legal input (payment records, WWCC data) rather than inventing numbers for categories with real legal weight.

---

## Performance (§20.8)

| ID | Requirement |
| :---- | :---- |
| **NFR-28** | Public pages: **LCP under 2.5s** on a median mobile connection |
| **NFR-29** | API p95 response **under 400ms**, excluding video and file transfer |
| **NFR-30** | Video start time **under 3s** on a 5 Mbps connection |
| **NFR-31** | Adaptive bitrate rendition switching without playback interruption |

NFR-28 applies to `public-site`'s server-rendered pages specifically (FR-CMS-04 already requires SSR/ISR for exactly this reason). NFR-30 and NFR-31 are `materials`' Bunny Stream integration — see [integrations/bunny-stream.md](../integrations/bunny-stream.md).

---

## Acceptance Criteria

1. A restore from backup completes within the 8-hour RTO in a scheduled quarterly test, with results recorded.
2. Every admin action that changes a record — a rejection, a revocation, a correction, a suspension — produces exactly one `AuditLog` row (or lands in a module's own richer log, per [README.md](../README.md#auditlog-resolves-an-implicit-dependency)), never zero, never a silent duplicate.
3. A waiver evidence file, an instructor CV, and a report export are all unreachable by direct URL — signed-URL access only, in every case.
4. The consent banner defaults to every non-essential category off; enabling analytics is an explicit opt-in action, not a default.
5. A public course page's Largest Contentful Paint stays under 2.5 seconds on a throttled mobile connection in testing.
6. A waiver evidence file is inaccessible (deleted) 12 months after its decision date, with the surrounding audit trail still intact.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-PLT-DM-001](../data-model.md) |
| App store compliance, fully specified elsewhere | [app-store-compliance.md](/3i/app-store-compliance.md) |
| Data retention periods (NFR-26) | [data-retention.md](../data-retention.md) |
| Integration contracts | [integrations/stripe.md](../integrations/stripe.md), [integrations/bunny-stream.md](../integrations/bunny-stream.md), [integrations/aws-ses.md](../integrations/aws-ses.md) |