---
project: OstadLagbo
type: baseline
status: current
updated: 2026-08-28
version: "1.0"
approval: written
approved: 2026-08-28
id: OL-BAS-001
owner: Iftikher
---

# MVP Scope Baseline — v1.0

## Purpose and standing

This document defines the agreed scope of the Ostad Lagbo MVP. It is the instrument change requests are measured against. It governs **what** is in scope and what acceptance means; **how** the system is built is governed by `modules/` documents derived from it. Decisions here were made section by section by the founder on 2026-08-28.

## 1. Registration and verification

One account holds one role — Ostad or Shagred — chosen at registration and permanent. Registration requires a phone number verified by OTP and a password; login is phone + password, with OTP for password reset. Email is optional and verified if provided. All account holders must be 18 or older, enforced by date of birth at registration.

Shagred verification is phone-only in the MVP. Ostad onboarding proceeds in stages — personal information, identity verification, address, map location, professional details — ending in submission for admin review, with progress saved at every stage so onboarding can stop and resume without loss. An Ostad is discoverable only after admin approval.

Identity verification accepts NID or passport: ID number, front image, back image (NID only), and a selfie.

## 2. Ostad profile

The profile stores full legal name in both English and Bangla (matching the NID), plus display name, photo, date of birth, and gender. Identity documents and the selfie are internal-only; the public sees the resulting verified badge, never the documents. Contact details are never shown publicly before an accepted offer.

Address follows Division → District → Upazila/Thana → Area. Location is a latitude/longitude set by GPS or manual map pin.

Professional information carries headline, about, occupation, years of experience, and languages spoken. Skills carry category, skill name, level, and years of experience per skill. Education is a repeatable structured history — SSC, HSC, Bachelor, Masters, PhD, and other certifications — each entry carrying education level, certificate/degree name, institution name, and passing year. Experience covers work experience, teaching experience, certifications, and awards. Portfolio supports images, videos, documents, and external links.

Statistics show rating, review count, joined date, and last active. Trust signals show profile completion percentage, identity-verification status, admin-approval status, and the verified badge.

## 3. Map discovery

A Shagred opens a map centered on their current location and sees approved Ostads at their **exact stored pin location**. Because precision is exact, location capture must state plainly that the pin is publicly visible, and the Ostad may place the pin anywhere — a coaching center, shop, or landmark — rather than their residence.

Discovery works by map browsing, a skill-category filter, and keyword search, with a user-adjustable radius slider determining "nearby." A Shagred can pan and search anywhere without sharing their own precise location. Tapping an Ostad opens their full public profile. Only admin-approved Ostads ever appear on the map or in search.

## 4. Contact and offers

A Shagred sends an offer from an Ostad's profile as a free-text message. The Ostad is notified and can take or decline it; a pending offer expires after 7 days. On acceptance, an in-app chat opens between the two and phone numbers are revealed mutually. Teaching location, schedule, and price are arranged in that communication; the platform manages none of them. Contact details are never exposed before acceptance.

## 5. Admin review

Admin review covers identity documents and the full profile content. Submissions enter a queue; the admin approves, rejects with a reason, or requests changes, and the Ostad can amend and resubmit. Approval makes the profile discoverable and grants the verified badge where identity verification passed.

After approval, edits to key fields — legal name, identity documents, skills — return the profile to review; while re-review is pending, the profile stays discoverable showing its last approved version. All other edits publish freely. The admin tool is a separate web dashboard.

## 6. Ratings and trust

Only a Shagred whose offer that Ostad accepted may rate them — one rating per Shagred–Ostad pair, editable by its author. A rating is 1–5 stars plus a written review, aggregating into the profile's average rating and review count. Both roles can report profiles, messages, or users to the admin, and can block users; blocking prevents all contact and chat between the two parties.

## 7. Platform-wide rules

The MVP ships on Flutter for Android and iOS with an English-language UI (Bangla is a planned post-MVP addition; Bangla **data**, such as legal names, is stored from day one). The admin tool is a separate web dashboard. Push notifications cover offers received, offer outcomes, chat messages, and approval-status changes. Identity documents and selfies are stored encrypted, accessible only for admin review, and never displayed publicly. Account deletion is self-service in the app.

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

## MVP acceptance

The MVP is accepted when, in a production environment: an Ostad can register, complete the full profile, submit identity documents, and — after admin approval through the web dashboard — appear on the map with a verified badge; a Shagred can register, find that Ostad by map, category filter, keyword, and radius, view the full profile, and send an offer; the Ostad receives a push notification, accepts, and both parties can chat in-app with phone numbers revealed; the Shagred can then rate and review the Ostad; and reporting, blocking, and self-service account deletion function. No out-of-scope item is present.

## Change control

This baseline is revised only by issuing `mvp-scope-v1.1.md` (or higher) with this file set to `status: superseded`. It is never edited in place.
