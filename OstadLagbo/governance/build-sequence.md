---
project: OstadLagbo
type: build-plan
status: current
updated: 2026-09-12
id: OL-BLD-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.1.md
owner: Iftikher
---

# MVP Build Sequence

Sequences the approved MVP scope into six **slices**, each ending in something usable and testable. **Nothing is cut** — every requirement in every module is placed in exactly one slice. The purpose is to convert an all-or-nothing build into a staircase, so the product becomes real early (risk R-06), supply seeding can start before the build finishes (risk R-01), and a solo builder always has a working system to stand on (risk R-05). Bilingual UI (CL-016) ships with every slice from the first, because i18n is architecture, not a feature.

## Slice 0 — Foundation *(nothing visible; everything depends on it)*

Backend and hosting per the architecture decision record; localization architecture with both locale files live; `user_account` and auth (REG-01…07, REG-13 consent capture); the append-only audit log (ADM-17) and admin authentication (ADM-20); the analytics event pipeline (events are emitted from slice 1 onward — never retrofitted); encrypted object storage for the identity vault.

**Gate:** register both roles, log in, log out on Android and iOS in both languages; an audit entry writes; an analytics event lands.

## Slice 1 — Supply *(the first real Ostad)*

Ostad onboarding wizard with identity capture (REG-09, REG-10 incl. live selfie holding ID, REG-11); the full Ostad profile with approved/pending revisions (OSP-01…10); skill categories with Bangla aliases (ADM-11); the review queue, identity gate with duplicate-ID flag, verdicts, resubmission, key-field re-review (ADM-02…06); minimal overview (ADM-01 review counts); retention tooling for drafts (part of ADM-18).

**Gate:** a real Ostad completes onboarding, is reviewed in the dashboard, approved, and holds the verified badge.
**Unlock:** hand-recruitment of seed Ostads can **begin here** — weeks before discovery exists — in a private-beta posture. This is the earliest possible attack on R-01.

## Slice 2 — Discovery *(a guest finds that Ostad)*

Map with exact pins, radius, category and gender filters, cross-script fuzzy search, clustering, empty states, self-preview (MAP-01…06, MAP-09…11); guest browsing with guest-reachable legal docs (MAP-03); Shagred onboarding and profile (REG-08, SGP-01/02/04/06).

**Gate:** a guest on a fresh install finds the seeded Ostad by map, Bangla search, and filter, and reads the full profile.

## Slice 3 — Connection *(the product's success unit works end to end)* → **MVP-core**

Offer lifecycle, inboxes, acceptance effects with contact reveal (OFR-01…04, OFR-09); chat with text and voice notes, notifications (OFR-03, OFR-05); Shagred-profile visibility lifecycle and Ostad history (SGP-03, SGP-05); blocks and reports with the reports queue, warnings, and suspension (RNT-07, RNT-08, ADM-07, ADM-08); chat-context access for reports (OFR-07); the suspension-notice screen.

**Gate:** offer → accept → chat → phone reveal → block/report all function on real devices. **The product is usable.** Friends-and-family testing starts; seed Ostads can receive real offers.

## Slice 4 — Trust *(soft-launch readiness)*

Ratings, replies, aggregation, review moderation (RNT-01…06); visibility pause (OSP-11); favorites and shareable deep links (MAP-07, MAP-08); full account deletion with the 30-day recovery window and retention purges (REG-12, ADM-18 complete); pending-deletion recovery routing (REG-02); phone change and password change (REG-06, REG-07).

**Gate:** the incident-response standing preparations are complete, legal review of the privacy policy and ToS is done, and the retention purge has been verified in staging. **Soft launch** with seeded supply in the launch area.

## Slice 5 — Operate & grow *(public-launch readiness)* → **MVP-complete**

Support tickets and the support queue with suspension appeals (SUP-01…06, ADM-22); analytics charts and business intelligence (ADM-12…15); Ostad insights (OSP-12); broadcasts (ADM-16); SMS/OTP monitor (ADM-19); block overview and full directories (ADM-09, ADM-10); read-only settings (ADM-21).

**Gate:** app-store compliance checklist passed; funnel metrics from soft launch reviewed against targets. **Public launch.**

## Principles

1. **Slice order is a dependency order, not a priority ranking** — slice 5 features are not "less important," they simply need a running marketplace to be meaningful.
2. **Every slice ends usable.** If the build must pause at any gate, what exists is coherent.
3. **Seeding starts at slice 1, not at launch.** Supply is recruited while demand features are built.
4. **Scope freeze at v1.2:** during the build, new ideas are logged as change requests for v1.3 unless they block a gate.
5. Slice durations and dates belong to the schedule document, which sizes each slice against the architecture decision's cost and capacity model.
