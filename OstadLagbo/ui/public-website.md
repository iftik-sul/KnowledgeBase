---
project: OstadLagbo
type: ui
status: current
updated: 2026-09-25
id: OL-UI-002
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.2.md
owner: Iftikher
---

# Public Website — UI

The pages of the public marketing-and-legal website (CL-020), hosted on Vercel (ADR-001). Conventions per [UI Overview](/OstadLagbo/ui-overview.md) where they apply, plus this document's own (below); the legal text and its version are the same the app serves via `GET /v1/legal/*` (REG api). This is the ui layer's one non-app, non-dashboard surface.

## What the website is — and is not

The website is a **marketing and legal front door**, not a web version of the marketplace. It exists to explain Ostad Lagbo, send visitors to the app, and host the legal documents an app store and PDPA require to be reachable without an account.

- It has **no accounts, no sign-in, and no marketplace browsing.** Discovering Ostads, viewing profiles, offers, and chat are **app-only** — the guest map (MAP-03) lives in the app, not the web. The website never queries product data or a user's data; the only dynamic content it reads is the legal documents and their version.
- It is **bilingual — English and Bangla** (CL-016), matching the Bangla-first brand **ওস্তাদ লাগবো**; a language switch is present on every page, and the Bangla legal versions are first-class (required at launch).
- It is a **static/edge-rendered** site (no login, cacheable, SEO-friendly), which suits the cost posture (NFR-13) and the guest-reachability requirement.

## Build order (CL-020)

The **legal pages** ship in **Slice 2** (they gate registration consent and app-store submission); the **marketing pages** ship in **Slice 5**. This document specs both; the slices sequence them.

## Group A — Legal pages (Slice 2, guest-reachable)

### Terms of Service · Privacy Policy
- **Purpose:** the legal documents, reachable **without an account**, satisfying app-store and PDPA requirements (REG-13, MAP-03).
- **Structure:** the full document text in the visitor's chosen language (English or Bangla), the **effective date and version**, and a link between the two documents.
- **Data:** the same content the app serves — `GET /v1/legal/terms|privacy` and `GET /v1/legal/versions` — read from that one source and revalidated so the public copy tracks the current version. **Consent is captured in the app**, against the live version at registration (REG-13), so the website's copy is the **informational public reference**, not the consent-binding surface; it should still show the current version and effective date. PDPA-required disclosures live here (data residency, retention, rights).
- **Reached from:** direct URL, the app's in-app legal links (REG/SUP ui point to the same content), footers across the site, and app-store listing links.

## Group B — Marketing pages (Slice 5)

### Home / landing
- **Purpose:** say what Ostad Lagbo is in one screen and send the visitor to the app.
- **Structure:** the brand and one-line promise (find a trusted nearby Ostad, or be found as one); a short how-it-works; **Get the app** buttons (Google Play, App Store); and a language switch. Bangla-first tone.

### How it works
- **Purpose:** the map-first model in a few steps for each side — a Shagred discovers nearby Ostads and sends an offer; an Ostad sets up a verified profile and takes offers; the two connect and arrange details directly. States plainly that the platform is for **discovery and connection**, not payments or scheduling (MVP scope).

### For Ostads
- **Purpose:** recruit supply (the harder side of the marketplace). What an Ostad gets — a credible, verified profile, a map presence, and control over which offers to take; what verification involves (identity check, live selfie) and that documents are private to review; the free-to-use posture. A **Get the app / become an Ostad** call to action.

### For Shagreds
- **Purpose:** explain finding and contacting an Ostad — search and map by skill and area, judge profiles and reviews, send an offer, connect. A **Get the app** call to action.

### Trust & safety
- **Purpose:** the trust story — identity verification and the verified badge, admin review, ratings and reviews, reporting and blocking, and the privacy posture (Ostad location is a chosen public pin, Shagreds are never findable, contact shared only on a mutual accept). Links to the legal pages.

### About / contact
- **Purpose:** who is behind the platform and how to reach support.
- **Structure:** a short about, and the **public contact email** — the support channel for visitors, and the stated fallback for **banned or deleted users who cannot log in** to use in-app support (SUP-04). No contact form that collects data beyond what an email needs.

## Group C — Shared-profile deep-link landing (MAP-07)

### Profile link landing
- **Purpose:** resolve a shared Ostad profile link for someone who opens it in a browser.
- **Behaviour:** a link from the app's Share action (`GET /v1/ostads/{id}/share`) opening on the web lands on a lightweight page that tries to **open the app to that profile** (deferred deep link) and otherwise offers the **app-store download**, so the profile opens after install. The web page itself **does not render the Ostad's profile** — profiles are app-only; it is a hand-off, not a public profile view.
- **Never shows:** an Ostad's profile, pin, or any product data on the web — only the app hand-off and store links.

## What this website never does

It holds no accounts and no sign-in; it never browses, searches, lists, or renders Ostads or Shagreds, or any offer, chat, review, or map, on the web (the marketplace is app-only); it never reads a user's data or writes anything; it shows a legal version that always matches the app's; and it collects no personal data beyond an ordinary contact email. Its only dynamic reads are the public legal documents.
