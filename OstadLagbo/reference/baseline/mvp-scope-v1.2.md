---
project: OstadLagbo
type: baseline
status: current
updated: 2026-09-25
version: "1.2"
approval: written
approved: 2026-09-25
id: OL-BAS-001
supersedes: /OstadLagbo/reference/baseline/mvp-scope-v1.1.md
owner: Iftikher
---

# MVP Scope Baseline — v1.2

## Purpose and standing

This document defines the agreed scope of the Ostad Lagbo MVP and is the instrument change requests are measured against. Version 1.2 consolidates every founder-approved change made during the planning phase after v1.1 — the change-log entries **CL-009 through CL-021** — into the scope prose, so the baseline again reads standalone as the single truthful answer to scope questions. It is issued **before the Execution phase begins**, and from its issuance a **scope freeze** applies (see *Change control*). It supersedes v1.1 in full.

## 1. Registration and verification

One account holds one role — Ostad or Shagred — chosen at registration and permanent. Registration requires a phone number verified by OTP and a password; login is phone + password, with OTP for password reset, and a logged-in user may change their password (with the current one) or their phone number (OTP to the new number). Email is optional and verified if provided; an email address can be linked to only one account. All account holders must be 18 or older, enforced by date of birth at registration; guardians register and act on behalf of minor learners.

**Language is chosen at first launch — English or Bangla — before any other step, stored on the account, and switchable from settings (REG-14).** **Consent is captured at registration:** explicit acceptance of the Terms of Service and Privacy Policy, with the accepted versions and timestamp recorded, and a re-acceptance notice when either document changes materially (REG-13). Registering with a phone number inside its 30-day deletion window routes to **account recovery** (log in to restore), never to a duplicate account (CL-015).

Shagred verification is phone-only in the MVP; Shagred onboarding collects display name and address, then opens the map. Ostad onboarding proceeds in fixed stages — personal information, identity verification, address, map location, professional details — ending in submission for admin review, with progress saved at every stage. An Ostad is discoverable only after admin approval.

**Identity verification accepts NID, passport, or driving licence (CL-017):** ID number and document images **per type** (NID front + back · passport photo page · driving licence front + back), plus a **verification selfie captured live in-app holding the document beside the face — no gallery upload for the selfie**. An ID number already tied to another active account is flagged and cannot reach approval until resolved (CL-012). Documents and the selfie are stored encrypted, admin-review-only, never public.

## 2. Profiles and the address model

**Address (both roles):** a manual street-address text line plus **Thana, District, Division, and Postal Code, each selected from dropdown lists** built on a Bangladesh administrative dataset. Ostads additionally set a **map pin** (GPS or manual placement) as their public discovery location; Shagreds never have a pin or stored coordinates.

**Ostad profile:** full legal name in English and Bangla (matching the ID document), display name, photo, date of birth (internal), gender. Identity documents and selfie are internal-only; the public sees the verified badge. Contact details are never shown before an accepted offer. Professional information (headline, about, occupation, years of experience, languages), skills (admin-managed fixed categories with **Bangla names/aliases** + free-text skill names, with cross-script fuzzy category matching, CL-013), structured education history (SSC → PhD and certifications; level, degree name, institution, passing year per entry), experience (work, teaching, certifications, awards), and portfolio — images, **one natively stored intro video of at most 45 seconds**, documents, and external links. Statistics: rating, review count, joined date, last active. Trust signals: profile completion, verification status, verified badge.

**Key fields and the revision flow (CL-021):** an Ostad's **legal names, identity documents, skills, and profile photo** are *key fields*. Before approval they are set through onboarding; after approval, a key-field change collects in **one pending revision** the Ostad submits for review — locked while under review, editable and resubmittable if changes are requested, published on approval, discarded on rejection — while the public profile keeps serving the last approved values. A never-submitted revision may be discarded; one left inactive for 90 days is discarded automatically, with prior notice, and its uploads deleted. Non-key edits publish immediately. **An approved Ostad has a private insights view (CL-014):** counts only — profile views, offers by outcome, connections — never who viewed or favourited.

**Shagred profile:** deliberately minimal — display name, optional photo, date of birth (internal), optional gender, the address above, joined date, and a **private, immutable Ostad history** (accepted connections) visible only to the Shagred. A Shagred profile is never browsable, searchable, or mapped; it is visible only to an Ostad holding that Shagred's offer, lapsing on decline/expiry/withdrawal and persisting after acceptance. An Ostad who holds or has held a Shagred's offer may **report** that Shagred profile (CL-012).

## 3. Map discovery

The map shows approved Ostads at their **exact stored pin location**; location capture must state the pin is publicly visible and that it may be placed at any teaching location rather than a residence. **The map, search, filters, and full Ostad profiles are browsable by guests without an account; any contact action requires registration.** Discovery works by map browsing (pins only), a skill-category filter, a **gender filter**, and keyword search over category and skill names — matched **fuzzily across both English and Bangla scripts** (CL-013) — under a user-adjustable radius measured from map center. Registered users can **favorite** Ostads (strictly private) and every profile has a **shareable deep link**. Only admin-approved, non-paused Ostads ever appear. An Ostad may **pause their visibility (CL-010):** paused, they leave map and search and receive no new offers, while existing chats, already-received pending offers, and direct profile/favourite access continue with offers disabled.

## 4. Contact and offers

A registered Shagred with a complete profile sends a free-text offer (one pending per pair; five pending globally). The Ostad takes or declines; pending offers expire after 7 days; the Shagred may withdraw a pending offer and may re-offer after any terminal state. On acceptance, an in-app chat opens — **text messages and voice notes only** — and **phone numbers and verified email addresses (where present) are revealed mutually (CL-011)**. Chat messages **cannot be edited or deleted by users** (they are moderation evidence, CL-015); **notification preferences are OS-level only — no per-category settings in the app (CL-015)**. Teaching location, schedule, and price are arranged between the parties; the platform manages none of them. Contact details are never exposed before acceptance; block is the termination instrument.

## 5. Admin panel

Admin review covers identity documents and full profile content; approval requires a passed identity check and a resolved duplicate-ID flag, so every live Ostad holds the verified badge. Verdicts: approve / request changes / reject (reasons mandatory); resubmissions unlimited; key-field edits trigger re-review while the last approved version stays live. **Admin authentication requires email + password + a TOTP second factor (CL-018); admin accounts are provisioned manually.** **The admin panel is a full web control panel, English-only:** review, report, and **support-ticket** queues (CL-009); user directories and account detail; **warnings, suspension, and account termination** with a 30-day appeal window (CL-019); skill-category management with Bangla aliases; full analytics with charts and time-series (connections, funnels, growth, retention, demand intelligence, quality, including Ostad-insight and support metrics); segment push broadcasts **in both languages**; an append-only audit log (every action and every identity-document, chat-context, and Shagred-history view); identity-data retention tooling; an SMS/OTP monitor; and a read-only platform-configuration view.

**Termination (CL-019)** bans an account: it is suspended (if not already), given a mandatory ban-and-appeal notice, and enters a 30-day window during which it may create and follow an appeal ticket and do nothing else; a successful appeal is a reinstatement. At the window's end the account purges under the retention policy's banned-account exception (ID-number hash, phone, legal name, and violation records retained while the ban stands, so the person cannot re-register). Termination is the only route by which a suspended account leaves the platform.

## 6. Ratings and trust

Only a Shagred with an accepted offer may rate that Ostad — one rating per pair, unlocked immediately on connection, editable by its author: 1–5 stars plus a required written review. The Ostad may post one public reply per review. Reviews persist through blocks and survive reviewer account deletion in anonymized form; only admin content-removal takes a living review down, and removal consumes the pair's one rating slot. Both roles can report profiles, messages, reviews, and replies, and can block users; blocking freezes chat, severs visibility, prevents new offers between the pair, and removes each party from the other's discovery surfaces. The reporter's identity is never revealed to the reported account.

## 7. Support

**In-app help and appeals (CL-009).** A Help & Support screen (both roles, including pending Ostads) offers categorized tickets — Account & login / Verification & review / Technical problem / Appeal a decision / Other — each a private thread with support carrying an optional single screenshot, resolved by an admin with a closing reply and reopenable within 14 days. The **suspension-notice screen** carries an *Appeal this decision* action that creates an appeal ticket — the only write a suspended or terminated account can make. Tickets are not the abuse-report channel and are not real-time chat.

## 8. Platform-wide rules

Flutter for Android and iOS; **full bilingual English and Bangla UI from launch (CL-016)** — localization architecture from the first commit, language chosen at first launch and switchable in settings, English the source language for specs with Bangla copy authored by the founder, and Bangla versions of the Privacy Policy and Terms of Service required at launch. A separate **web admin dashboard (English-only)** and a **public marketing-and-legal website (CL-020)** — guest-reachable Terms and Privacy plus landing pages — both hosted per ADR-001. Push notifications cover offers, offer outcomes, chat messages, verification verdicts, and approval-status changes, plus admin broadcasts; the device push token is registered against the account and revoked on logout, suspension, deletion request, or termination. Identity documents and selfies are stored encrypted, admin-review-only, never public. Account deletion is self-service with a 30-day recovery window (suspended accounts cannot self-delete; termination is their only exit). Analytics events for the admin panel's metrics are instrumented from first release.

## Out of scope

| Excluded from the MVP | Notes |
|---|---|
| Payments, banking, payouts | Post-MVP; trust layer comes first |
| Platform-set or stored pricing | Agreed directly between participants |
| Availability calendars and bookings | Arranged in direct communication |
| Platform-managed teaching location after discovery | Participants decide together |
| Preference matching | Proximity + search are the only discovery signals |
| Accounts under 18 | Guardians register and act on behalf of minor learners |
| Images, documents, or video in chat | Text + voice notes only |
| Per-category notification preferences | OS-level control only (CL-015) |
| Admin role tiers; editable platform configuration | Post-MVP; all admins full-permission, config is deployment-time |
| Revenue/monetization metrics | Absent by design while payments are out of scope |

## MVP acceptance

The MVP is accepted when, in production: a visitor chooses their language, and an Ostad registers, completes the full profile including address and pin, submits identity documents (with the live held-document selfie), and — after approval via the TOTP-protected web panel — appears on the map with a verified badge; a guest can browse the map and open that profile without an account, in either language; a registered Shagred finds the Ostad by map, category, gender filter, cross-script keyword, and radius, favorites them, shares their link, and sends an offer; the Ostad receives a push, accepts, both chat by text and voice with phone and verified email revealed; the Shagred rates and reviews, and the Ostad replies once; reporting, blocking, visibility pause, in-app support with the suspension appeal, self-service deletion with recovery, and the admin panel's queues, directories, analytics, broadcast, termination, and audit log all function; and the public website serves the legal documents to a guest. No out-of-scope item is present.

## Change control and scope freeze

This baseline is revised only by issuing v1.3 (or higher) with this file set to `status: superseded`, and a corresponding change-log entry; it is never edited in place.

**A scope freeze is in effect from v1.2 (build-sequence OL-BLD-001, principle 4).** During the build, a new idea is logged as a change request for **v1.3** and is not implemented unless it blocks a slice gate. This keeps the Execution phase building against a fixed target.

## Changes absorbed since v1.1 (consolidated into this version)

CL-009 in-app support module · CL-010 Ostad visibility pause · CL-011 verified-email reveal on acceptance · CL-012 consent capture, guest-reachable legal, ID-number uniqueness, Shagred-profile reporting, password change, offer inboxes · CL-013 Bangla-script category matching · CL-014 Ostad self-insights · CL-015 deletion-window recovery, no message edit/delete, OS-level notifications only · CL-016 bilingual MVP · CL-017 identity hardening (driving licence, per-type images, live held-document selfie) · CL-018 admin TOTP · CL-019 admin termination with appeal window · CL-020 public website · CL-021 profile photo as a key field and the revision flow.
