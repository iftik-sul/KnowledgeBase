---
project: OstadLagbo
type: baseline
status: current
updated: 2026-08-30
version: "1.1"
approval: written
approved: 2026-08-30
id: OL-BAS-001
supersedes: /OstadLagbo/reference/baseline/mvp-scope-v1.0.md
owner: Iftikher
---

# MVP Scope Baseline — v1.1

## Purpose and standing

This document defines the agreed scope of the Ostad Lagbo MVP and is the instrument change requests are measured against. Version 1.1 consolidates the founder-approved scope extensions made during the module requirements sessions of 2026-08-28 → 2026-08-30 (recorded in the [change log](/OstadLagbo/governance/change-log.md)) and the revised address model. It supersedes v1.0 in full.

## 1. Registration and verification

One account holds one role — Ostad or Shagred — chosen at registration and permanent. Registration requires a phone number verified by OTP and a password; login is phone + password, with OTP for password reset. Email is optional and verified if provided; an email address can be linked to only one account. All account holders must be 18 or older, enforced by date of birth at registration; guardians register and act on behalf of minor learners.

Shagred verification is phone-only in the MVP; Shagred onboarding collects display name and address, then opens the map. Ostad onboarding proceeds in fixed stages — personal information, identity verification, address, map location, professional details — ending in submission for admin review, with progress saved at every stage. An Ostad is discoverable only after admin approval.

Identity verification accepts NID or passport: ID number, front image, back image (NID only), and a selfie.

## 2. Profiles and the address model

**Address (both roles):** a manual street-address text line plus **Thana, District, Division, and Postal Code, each selected from dropdown lists** built on a Bangladesh administrative dataset. Ostads additionally set a **map pin** (GPS or manual placement) as their public discovery location; Shagreds never have a pin or stored coordinates.

**Ostad profile:** full legal name in English and Bangla (matching the NID), display name, photo, date of birth (internal), gender. Identity documents and selfie are internal-only; the public sees the verified badge. Contact details are never shown before an accepted offer. Professional information (headline, about, occupation, years of experience, languages), skills (admin-managed fixed categories + free-text skill names, with fuzzy category matching), structured education history (SSC → PhD and certifications; level, degree name, institution, passing year per entry), experience (work, teaching, certifications, awards), and portfolio — images, **one natively stored intro video of at most 45 seconds**, documents, and external links. Statistics: rating, review count, joined date, last active. Trust signals: profile completion, verification status, verified badge.

**Shagred profile:** deliberately minimal — display name, optional photo, date of birth (internal), optional gender, the address above, joined date, and a **private, immutable Ostad history** (accepted connections) visible only to the Shagred. A Shagred profile is never browsable, searchable, or mapped; it is visible only to an Ostad holding that Shagred's offer, lapsing on decline/expiry and persisting after acceptance.

## 3. Map discovery

The map shows approved Ostads at their **exact stored pin location**; location capture must state the pin is publicly visible and that it may be placed at any teaching location rather than a residence. **The map, search, filters, and full Ostad profiles are browsable by guests without an account; any contact action requires registration.** Discovery works by map browsing (pins only), a skill-category filter, a **gender filter**, and keyword search over category and skill names with fuzzy matching, under a user-adjustable radius measured from map center. Registered users can **favorite** Ostads (strictly private) and every profile has a **shareable deep link**. Only admin-approved Ostads ever appear.

## 4. Contact and offers

A registered Shagred sends a free-text offer (one pending per pair; five pending globally). The Ostad takes or declines; pending offers expire after 7 days; the Shagred may withdraw a pending offer and may re-offer after any terminal state. On acceptance, an in-app chat opens — **text messages and voice notes only** — and phone numbers are revealed mutually. Teaching location, schedule, and price are arranged between the parties; the platform manages none of them. Contact details are never exposed before acceptance; block is the termination instrument.

## 5. Admin panel

Admin review covers identity documents and full profile content; approval requires a passed identity check, so every live Ostad holds the verified badge. Verdicts: approve / request changes / reject (reasons mandatory); resubmissions unlimited; key-field edits (legal names, identity documents, skills) trigger re-review while the last approved version stays live. **The admin panel is a full web control panel:** review and report queues, user directories and account detail, suspension and warnings, skill-category management, full analytics with charts and time-series (connections, funnels, growth, retention, demand intelligence, quality), segment push broadcasts, an append-only audit log, identity-data retention tooling, and an SMS/OTP monitor.

## 6. Ratings and trust

Only a Shagred with an accepted offer may rate that Ostad — one rating per pair, unlocked immediately on connection, editable by its author: 1–5 stars plus a required written review. **The Ostad may post one public reply per review.** Reviews persist through blocks and survive reviewer account deletion in anonymized form. Both roles can report profiles, messages, reviews, and replies, and can block users; blocking freezes chat, severs visibility, prevents new offers between the pair, and removes each party from the other's discovery surfaces.

## 7. Platform-wide rules

Flutter for Android and iOS; English UI (Bangla post-MVP; Bangla data stored from day one); separate web admin dashboard. Push notifications cover offers, offer outcomes, chat messages, and approval-status changes, plus admin broadcasts. Identity documents and selfies are stored encrypted, admin-review-only, never public. Account deletion is self-service. Analytics events for the admin panel's metrics are instrumented from first release.

## Out of scope

| Excluded from the MVP | Notes |
|---|---|
| Payments, banking, payouts | Post-MVP; trust layer comes first |
| Platform-set or stored pricing | Agreed directly between participants |
| Availability calendars and bookings | Arranged in direct communication |
| Platform-managed teaching location after discovery | Participants decide together |
| Preference matching | Proximity + search are the only discovery signals |
| Bangla UI | Planned post-MVP; English-first ships |
| Accounts under 18 | Guardians register and act on behalf of minor learners |
| Images, documents, or video in chat | Text + voice notes only |

## MVP acceptance

The MVP is accepted when, in production: an Ostad registers, completes the full profile including address and pin, submits identity documents, and — after approval via the web panel — appears on the map with a verified badge; a guest can browse the map and open that profile without an account; a registered Shagred finds the Ostad by map, category, gender filter, keyword, and radius, favorites them, shares their link, and sends an offer; the Ostad receives a push, accepts, both chat by text and voice with numbers revealed; the Shagred rates and reviews, and the Ostad replies once; reporting, blocking, self-service deletion, and the admin panel's queues, directories, analytics, broadcast, and audit log all function. No out-of-scope item is present.

## Change control

This baseline is revised only by issuing v1.2 (or higher) with this file set to `status: superseded`, and a corresponding change-log entry. It is never edited in place.
