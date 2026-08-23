---
project: 3i
type: overview
status: current
updated: 2026-08-23
tags:
  - open-questions
  - cross-cutting
---

# Open Questions

Unresolved items. Each blocks something specific. Resolved items move to [decisions/](decisions/README.md).

---

## Open

None against `identity-and-access`, `commerce`, `catalogue`, `materials`, `learning-delivery`, `assessment`, or `certification`. See each module's own "Open Against This Module" section for smaller flagged items (implementation defaults, external client dependencies) that don't rise to project-wide open questions.

---

## Resolved

| Was | Now |
| :---- | :---- |
| **OQ-01** Module partition | Thirteen modules, [project-standards.md](project-standards.md#modules) |
| **OQ-02** What a seat is | [3I-DEC-009](decisions/dec-009-seats-as-account-pool.md) — permanent, non-transferable enrolment grant |
| **OQ-03** Devices versus seats | [3I-DEC-015](decisions/dec-015-device-allowance-scales-with-seats.md) — seats plus two, floor of three |
| **OQ-04** Attendance after dismissal | [3I-DEC-021](decisions/dec-021-attendance-measured-against-sessions-delivered.md) — measured on sessions delivered, plus a WWCC scheduling guard |
| **OQ-06** Chat history on deletion | [3I-DEC-016](decisions/dec-016-deletion-removes-content-retains-record.md) — content removed, moderation record retained |
| **OQ-07** Per-seat price quotable | [3I-DEC-024](decisions/dec-024-two-tier-age-based-seat-pricing.md) — two tiers: adult $9.99/mo, $99.99/yr; under-18 $5.99/mo, $49.99/yr |
| **OQ-08** Inactive profiles and the cap | [3I-DEC-014](decisions/dec-014-cap-counts-active-profiles-only.md) — cap counts active and never-activated only |
| **OQ-09** `app-store-compliance.md` not yet written | [app-store-compliance.md](app-store-compliance.md) — written, consolidating FR-BILL-02, FR-NOT-06, and NFR-15–21 |
| **OQ-10** PIN attempt rate limiting | [3I-DEC-022](decisions/dec-022-pin-lockout-and-dob-correction-notification.md) — matches FR-AUTH-09 exactly |
| **OQ-11** Minimum sessions before an attendance certificate | **Resolved 2026-08-23** — [3I-DEC-028](decisions/dec-028-session-delivery-floor-attendance-eligibility.md): a batch-level floor (≥70% of scheduled sessions delivered) gates attendance-certificate eligibility entirely, fails closed, and extends to gate the whole course for `Mixed` courses too |

**Seven modules are now fully specified**: `identity-and-access`, `commerce`, `catalogue`, `materials`, `learning-delivery`, `assessment`, `certification`. No project-wide open questions remain unresolved.

---

## Client Dependencies (§22.2)

| # | Item | Needed by | Note |
| :---: | :---- | :---- | :---- |
| ~~1~~ | ~~Per-seat price~~ | ~~Commerce~~ | **Received 2026-08-20** — [3I-DEC-024](decisions/dec-024-two-tier-age-based-seat-pricing.md) |
| 2 | GST treatment for overseas learners | Commerce | From their accountant |
| 3 | Privacy policy, terms, refund policy | Launch | From their lawyer |
| 4 | WWCC position | Instructor onboarding | From their lawyer |
| 5 | Certificate design assets | Certification | Template, seal, signature — blocks certificate PDF rendering, not this module's specification |
| 6 | Cloud, Bunny, Stripe, SES accounts | Foundation | **Open now** — no cost to sit idle |
| 7 | Apple and Google developer accounts | Mobile | **Open now** — store review is the least predictable item |
| 8 | Live-class tool choice | Learning | See below |

**A ninth dependency exists.** [3I-DEC-019](decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) requires named human sign-off on the safeguarding strings, in each of five languages, before launch. The institute has native speakers; this is an afternoon of their time, not a translation budget. But it is a launch gate, and it is on them.

### On item 8

The baseline already requires "confirmation its terms permit the intended learner ages". Most video conferencing services set a minimum age in their own terms — commonly 13 or 16. The platform teaches from age five.

It is entirely possible the tool the institute chooses does not permit the students they intend to teach on it, and that is not fixable in the platform. Worth resolving before the Learning phase rather than during it.

---

## Change Request Backlog

Eleven decisions now change the baseline rather than interpret it — the original eight, plus [3I-DEC-024](decisions/dec-024-two-tier-age-based-seat-pricing.md), [3I-DEC-025](decisions/dec-025-waiver-single-profile-cap.md), and [3I-DEC-028](decisions/dec-028-session-delivery-floor-attendance-eligibility.md). Listed in [decisions/README.md](decisions/README.md#scope-changes-against-srd-v20) — that table has not yet been updated to include 024/025/028 explicitly; worth a follow-up pass. [3I-DEC-023](decisions/dec-023-no-standalone-accounts-under-18.md) remains the largest single item and should still be raised distinctly from the rest.

---

## Baseline Approval

SRD v2.0 is **verbally approved only**, recorded as `approval: verbal` in its frontmatter. §21.3 measures change requests against an approved baseline; with eleven changes now queued, that matters more than it did.

Raised and noted. No action requested.