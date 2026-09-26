---
project: OstadLagbo
type: build-plan
status: current
updated: 2026-09-26
id: OL-BLD-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.2.md
owner: Iftikher
---

# MVP Build Sequence

Sequences the approved MVP scope into six **slices**, each ending in something usable and testable. **Nothing is cut** — every requirement is placed. A few requirements with distinct sub-parts are **phased across two slices**, each part named where it lands: **REG-02** (registration in Slice 0; deletion-window recovery routing in Slice 4), **REG-12** (user-facing account deletion in Slice 1; the automated purge machinery in Slice 4 — CL-034) and **ADM-18** (draft retention in Slice 1; full retention purges in Slice 4). The purpose is to convert an all-or-nothing build into a staircase, so the product becomes real early (risk R-06), supply seeding can start before the build finishes (risk R-01), and a solo builder always has a working system to stand on (risk R-05). Bilingual UI (CL-016) ships with every slice from the first, because i18n is architecture, not a feature. *(Revised 2026-09-14: termination (CL-019), language preference (REG-14), push-token registration, and the public website (CL-020) placed. Revised 2026-09-26: slice lists de-duplicated and the four instrumentation/cross-ref requirements (OFR-06, OFR-08, RNT-09, RNT-10) placed explicitly.)*

## Slice 0 — Foundation *(nothing visible; everything depends on it)*

Backend and hosting per ADR-001 (Supabase, Render, Vercel, Cloudflare, FCM; free tiers throughout development); localization architecture with both locale files live and **language selection with stored preference (REG-14)**; `user_account` and auth (REG-01…05, REG-13 consent capture; REG-06 password change and REG-07 phone change land in Slice 4); the append-only audit log (ADM-17) and admin authentication with TOTP (ADM-20); the analytics event pipeline (events are emitted from slice 1 onward — never retrofitted); encrypted object storage for the identity vault; the `skill_category` and `admin_area` seed migrations (OL-SKC-001; ADM-DM); ADR-001's Slice 0 open items (Dhaka latency test, **Alpha SMS gateway integration and Resend email** — both selected, CL-036, leaving only the masked-sender-ID application outstanding — Bangla fuzzy-match verification, coordinate log scrubbing, API framework and RLS baseline); **ADR-005's three verification items** — confirm whether a legacy JWT secret exists on the new project at all, prove the imported ES256 key works against **Realtime and Storage** and not just the Data API, and establish local-versus-hosted signing parity; **the map tile provider bake-off (CL-035)** — one launch-area viewport rendered in MapTiler, Stadia, and Google, compared for Bangla labels and Dhaka density, decided **before any MAP screen is built in Slice 2**, because the `flutter_map`-or-Google half of that choice is a rewrite rather than a config change once screens exist.

**Gate:** register both roles, log in, log out on Android and iOS in both languages; an audit entry writes; an analytics event lands; the fuzzy-match test set (OL-SKC-001) passes.

## Slice 1 — Supply *(the first real Ostad)*

Ostad onboarding wizard with identity capture (REG-09, REG-10 incl. live selfie holding ID, REG-11); the full Ostad profile with approved/pending revisions (OSP-01…10); skill categories with Bangla aliases (ADM-11); the review queue, identity gate with duplicate-ID flag, verdicts, resubmission, key-field re-review (ADM-02…06); minimal overview (ADM-01 review counts); retention tooling for drafts (part of ADM-18); **user-facing account deletion (part of REG-12, CL-034)** — the Settings "Delete account" item and `DELETE /v1/me`: immediate deactivation, sessions and push tokens revoked. **Real identity documents are collected from this slice, so the erasure right must exist from this slice.** The automated 30-day purge and retention sweeps land in Slice 4; until then the founder performs the erasure manually within the 30-day window (a handful of hand-recruited seed Ostads makes this tractable).

**Gate:** a real Ostad completes onboarding, is reviewed in the dashboard, approved, and holds the verified badge. **The paid tiers switch on here** (ADR-001 phased cost model).
**Unlock:** hand-recruitment of seed Ostads can **begin here** — weeks before discovery exists — in a private-beta posture, in the launch-focus categories (OL-SKC-001), concentrated in the launch area — **Dhanmondi** (OL-MET-001, CL-037). This is the earliest possible attack on R-01.

## Slice 2 — Discovery *(a guest finds that Ostad)*

Map with exact pins, radius, category and gender filters, cross-script fuzzy search, clustering, empty states, self-preview (MAP-01…06, MAP-09…11); guest browsing with guest-reachable legal docs (MAP-03); Shagred onboarding and profile (REG-08, SGP-01/02/04/06); **the public website's guest legal pages (CL-020)**.

**Gate:** a guest on a fresh install finds the seeded Ostad by map, Bangla search, and filter, and reads the full profile.

## Slice 3 — Connection *(the product's success unit works end to end)* → **MVP-core**

Offer lifecycle, inboxes, acceptance effects with contact reveal, thread ending/freezing, and offer instrumentation (OFR-01…04, OFR-06, OFR-08, OFR-09); chat with text and voice notes, **push-token registration and locale-rendered notifications** (OFR-03, OFR-05; REG-DM `device_push_token`); Shagred-profile visibility lifecycle and Ostad history (SGP-03, SGP-05); blocks and reports with the reports queue, warnings, suspension, **and termination with the 30-day appeal window** (RNT-07, RNT-08, ADM-07, ADM-08 incl. CL-019); chat-context access for reports (OFR-07); the suspension-notice screen.

**Gate:** offer → accept → chat → phone reveal → block/report all function on real devices; a terminated test account can appeal and do nothing else. **The product is usable.** Friends-and-family testing starts; seed Ostads can receive real offers.

## Slice 4 — Trust *(soft-launch readiness)*

Ratings, replies, aggregation, review moderation, trust signals, and rating/block instrumentation (RNT-01…06, RNT-09, RNT-10); visibility pause (OSP-11); favorites and shareable deep links (MAP-07, MAP-08); **automated** deletion machinery — the 30-day recovery window and retention purges on both deletion paths (rest of REG-12, ADM-18 complete; the user-facing delete shipped in Slice 1, CL-034), replacing the interim manual purge; pending-deletion recovery routing (REG-02); phone change and password change (REG-06, REG-07).

**Gate:** the incident-response standing preparations are complete and **Playbooks 1–3 are operable** (Playbook 4's dashboard-dependent steps run manually until Slice 5 — CL-034), legal review of the privacy policy and ToS is done (the PDPA data-residency position is CL-025: Singapore accepted through development, compliance required before public launch), and the retention purge has been verified in staging. **Soft launch** with seeded supply in the launch area — **Dhanmondi**, against the supply targets in OL-MET-001 (40 approved Ostads, all six launch-focus categories covered).

## Slice 5 — Operate & grow *(public-launch readiness)* → **MVP-complete**

Support tickets and the support queue (SUP-01…03, SUP-05, SUP-06, ADM-22 — SUP-04 appeals shipped in Slice 3, principle 6); analytics charts and business intelligence (ADM-12…15); Ostad insights (OSP-12); bilingual broadcasts (ADM-16); SMS/OTP monitor (ADM-19); block overview and full directories (ADM-09, ADM-10); read-only settings (ADM-21); **the public website's marketing pages (CL-020)**.

**Gate:** app-store compliance checklist passed; funnel metrics from soft launch reviewed against **the targets in OL-MET-001** (CL-037) — the success unit being offer→acceptance ≥35% and zero-result searches under 20%. **Public launch.**

## Principles

1. **Slice order is a dependency order, not a priority ranking** — slice 5 features are not "less important," they simply need a running marketplace to be meaningful.
2. **Every slice ends usable.** If the build must pause at any gate, what exists is coherent.
3. **Seeding starts at slice 1, not at launch.** Supply is recruited while demand features are built.
4. **Scope freeze at v1.2:** during the build, new ideas are logged as change requests for v1.3 unless they block a gate.
5. Slice durations and dates belong to the schedule document, which sizes each slice against the architecture decision's cost and capacity model.
6. **Appeal tickets (SUP-04) are placed in Slice 3 with termination, ahead of the rest of the support module in Slice 5** — an appeal path must exist from the first day termination does.
