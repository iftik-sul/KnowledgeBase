---
project: OstadLagbo
type: test-plan
status: current
updated: 2026-09-26
id: OL-TST-001
derived_from: /OstadLagbo/governance/build-sequence.md
owner: Iftikher
---

# Test and Acceptance Plan

How a slice is proved done. NFR-14 requires automated tests covering *"every acceptance criterion of Slices 0–3 before soft launch"* — which leaves Slices 4 and 5 uncovered, and leaves the bilingual UI (CL-016) with no review process at all despite Bangla being half the product. This closes both.

The specification is unusually well suited to testing: nearly every requirement already ends in an **Acceptance** line. Those lines are the test cases. Nothing new needs inventing — it needs executing.

## The layers

| Layer | Covers | Runs |
|---|---|---|
| **Unit** | Pure logic: predicates, validators, date and distance maths, the fuzzy matcher | Every push (CI) |
| **Integration** | The API against a real Postgres and a real Supabase project — policy layer, RLS as second line, transactions, **the ADR-005 signing key against Realtime and Storage** | Every push (CI) |
| **End-to-end** | The critical paths below, on a real device | Before each slice gate |
| **Manual / UAT** | Everything judgement-based: Bangla copy, review queue ergonomics, real-device feel on a mid-range phone | Before each slice gate |

**Why integration tests hit a real Supabase project:** the platform's auth depends on Supabase accepting tokens the API minted (ADR-005), and a July 2025 PostgREST upgrade broke exactly that pattern for projects until they re-imported their key. A mocked Supabase would have passed. This test is the early-warning system for a second such change.

## Critical paths — these must never break

Each is one end-to-end test, run before every gate from the slice that introduces it onward:

1. **Register → verify OTP → account exists** (both roles, both locales)
2. **Ostad onboarding → submit → admin approves → pin appears on the map**
3. **Guest finds an Ostad** by map, by Bangla search, by filter — on a fresh install, with no account
4. **Offer → accept → contact revealed → chat with text and a voice note** ← the success unit; if only one test survived, this is it
5. **Block → the thread freezes, discovery severs, and no notification reaches the blocked party** (the opacity guarantee, RNT-08)
6. **Report → admin suspends → the suspended user reaches the appeal and nothing else**
7. **Delete account → immediate deactivation → login within 30 days recovers it**
8. **Rate an Ostad → the aggregate updates → the Ostad replies once**

## Per-slice acceptance

A slice is done when its gate (OL-BLD-001) passes **and** the items below hold. Nothing is accepted "in production."

**Slice 0** — auth and the audit log under test; an analytics event lands; the fuzzy-match test set (OL-SKC-001) passes; **both locale files complete for every shipped string**; ADR-005's three verification items closed.

**Slice 1** — paths 1–2 automated; identity upload tested with a **real device camera**, not a simulator; the review queue walked manually by the person who will actually staff it; the Slice-1 user-facing delete (CL-034) tested.

**Slice 2** — path 3 automated; map tested on a **mid-range Android phone on real 4G in Dhaka**, not on wifi on a flagship (NFR-02's reference device); zero-result and GPS-denied states exercised; the tile-provider bake-off decided (CL-035).

**Slice 3** — paths 4–6 automated; push delivery verified on **both platforms, on a fresh install and after a reinstall** (CL-038 — this is precisely what B4 got wrong); voice notes on a slow connection; the offer expiry job verified against the clock.

**Slice 4** — paths 7–8 automated; **the retention purge verified in staging** (gate); **a full restore rehearsal — database *and* Storage** (NFR-07, OL-OPS-001); legal hold set and released end-to-end (CL-041); incident Playbooks 1–3 walked through on paper with the actual tooling open.

**Slice 5** — the store-release checklist (OL-STR-001) passed; analytics reconciled against OL-MET-001's targets; **OSP-12's insight counts checked against ADM-12 for the same account and period** (the requirement's own acceptance line); the support queue exercised.

## Bilingual acceptance — the process CL-016 never got

Bangla is half the product and none of it is machine-checkable. The rule: **a screen is not done until both languages are done.**

- **Automated:** no hard-coded user-facing strings; every key present in **both** locale files (a CI check — a missing key is a build failure, not a runtime surprise); no layout breaks at the longest Bangla string; OTP codes and phone numbers render in Latin digits in both locales (NFR-11).
- **Manual, by a native Bangla speaker — the founder or a named reviewer:** every string read in context on a device, not in a spreadsheet. Register terms matter: *Ostad* and *Shagred* carry meaning that a literal translation loses. Error and empty states get read too — they are where machine-translated copy is most obviously machine-translated, and they arrive when the user is already frustrated.
- **Bangla copy is authored, not translated.** English is the source language for specifications; the Bangla is written by the founder (baseline v1.2). A reviewed Bangla string is the deliverable, not a translated one.
- **Outstanding:** Bangla versions of the Privacy Policy and Terms are **required at launch** (CL-029) and are not written. Founder-authored; needs a date.

## What is deliberately not automated

Honest scoping — a solo builder automating everything ships nothing:

- Admin dashboard UI beyond authentication and the policy layer behind it. The queues are manually exercised; the *permissions* are integration-tested, because that is where the identity vault is.
- Push **delivery** end to end (device notification trays resist automation). Token registration and dispatch are tested; the tray is checked by hand, on both platforms, per the Slice 3 item above.
- Store listing and review flows.
- Visual regression.

## Entry to soft launch

Soft launch (Slice 4 gate) requires, in addition to that gate: critical paths 1–8 green; the restore rehearsal done with a recorded RTO; both locales reviewed by a native speaker; the threat model's Slice-0 verification items closed (OL-THR-001 — especially Cloudflare's rate-limit capacity); and no open High from the audit.
