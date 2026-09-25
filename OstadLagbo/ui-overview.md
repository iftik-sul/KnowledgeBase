---
project: OstadLagbo
type: ui
status: current
updated: 2026-09-25
id: OL-UI-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.1.md
owner: Iftikher
---

# UI — Overview & Conventions

The rulebook for the ui layer: the surfaces OstadLagbo ships, how they are navigated, and the conventions every module's screen spec obeys. Module ui documents define the screens; this document defines the rules they share. Where this document and a module document disagree, this one wins.

**What a ui document specifies — and what it does not.** These documents specify **structure, behaviour, states, and data bindings**: what a screen is for, how it is reached, what it shows, every state it can be in, which api endpoints feed and drive it, and what it must never reveal. They do **not** specify visual design — colour, typography, spacing, iconography — which is produced later in Figma against a design system. A ui document says "the preview card shows photo, display name, verified badge, headline, rating, and distance"; Figma decides what that looks like. This keeps the layer a build specification a developer (human or AI) can implement, and a brief the visual design can be drawn against.

**Derivation.** Each module ui document derives from that module's **requirements** and cites the **api** and **data-model** documents wherever a screen's behaviour depends on them (project-standards → derivation chain). The screens realise the endpoints of the now-complete api layer; nothing in the ui introduces product behaviour the requirements and api do not already define.

## The surfaces

Four distinct surfaces, three of them separate front-ends (ADR-001):

| Surface | Platform | Audience | Where specified |
|---|---|---|---|
| **The app** | Flutter, Android 8.0+ / iOS 15+ (NFR-01) | Guests, Shagreds, Ostads | The seven app modules' ui docs (REG, OSP, SGP, MAP, OFR, RNT, SUP) |
| **Admin dashboard** | Web (Vercel), English-only (API Overview) | Admins | The ADM ui doc |
| **Public website** | Web (Vercel) | Anyone, pre-install | `ui/public-website.md` (CL-020) |
| **System-sent** | Push (FCM) and SMS (OTP) | All | Each module's ui doc, alongside the screen that triggers them |

The app is the centre of gravity; the dashboard and website are their own documents with their own conventions (the dashboard is a data-dense desktop tool, English-only; the website is marketing-and-legal content). This overview's conventions govern the **app** unless a section says otherwise.

## The three app shells

The app presents one of three shells depending on who is holding the phone. Which shell is active follows the REG account summary (`status`, `role`) and nothing the client decides on its own.

- **Guest shell** — no account. Opens **map-first** (MAP-03): the discovery map, search, filters, full Ostad profiles, reviews, and the legal documents are all reachable with zero registration. Any action needing identity — offer, favourite, report, block — routes to registration and returns to the same screen afterward (MAP-03). No bottom-nav tabs beyond what a guest can use.
- **Shagred shell** — bottom navigation: **Map** (discovery, the home surface), **Offers** (sent-offers inbox), **Chats**, **Favourites**, **Profile/Settings**. The Shagred is never discoverable and has no "my public profile" view of themselves as others see it, because no one sees it (SGP).
- **Ostad shell** — bottom navigation: **Offers** (received-offers inbox, the home surface), **Chats**, **Insights**, **Profile/Settings**. An Ostad has no discovery loop — they are *found*, not finding — so the discovery map is **not** a top-level Ostad tab; an Ostad checks how their own pin looks through the self-preview under Profile (MAP-01). Profile/Settings holds the public profile, the pause toggle, key-field revisions, and account settings; **Insights** (OSP-12) is its own tab.

**Two shells stand apart from the tab bars:**
- **Onboarding** (Ostad) — the fixed stage 1→6 wizard (REG-09), stage 6 being Review & submit, occupies the whole screen until submitted; the tab bar appears only once the account can use it.
- **Suspension notice** — a `suspended` login lands here and nowhere else (REG-api, SUP-04): the notice text, an **Appeal** action, and the user's own ticket threads (create an appeal; read and reply to any ticket they already own), plus language and logout. This is the UI face of the restricted-session whitelist.

## Localisation (CL-016, REG-14, NFR-11)

- **English and Bangla from launch.** Every screen renders in the account's `preferred_locale` (guests: device language, default English). A language toggle in Settings calls `PATCH /v1/me/locale`; it also re-renders the current screen.
- **The client never translates API text.** Error messages, notification bodies, status labels, and category/area names arrive already localised from the API (API Overview → localisation). The client localises only its own static chrome (button labels, screen titles) from bundled string tables.
- **Digits are always Latin** for phone numbers, OTP codes, and IDs (NFR-11), regardless of language; counts and dates follow the locale.
- **Both scripts are first-class in input.** Search and the category typeahead accept either script and match across both (MAP-06, OSP-04); the Bangla legal-name field accepts Bangla script whatever the UI language (OSP-01). Layout is left-to-right in both languages (no RTL).

## Error-to-UI mapping — the single source of truth

Every screen handles the API's closed error enum (API Overview) the same way. A module ui doc names only the *screen-specific* copy; the treatment is fixed here.

| `code` | UI treatment |
|---|---|
| `validation_failed` | Inline, at the offending field, from `details`; never a modal. The submit stays disabled until fixed |
| `unauthorized` | Session lost — route to login, preserving the intended destination |
| `forbidden` | "You can't do this" state appropriate to the screen; rare, since the client hides actions a role can't take |
| `suspended` | Drop to the suspension-notice shell; the notice payload is in `details` |
| `not_found` | One neutral "not available" state — **never** distinguishes a block from a deletion or a missing record (opacity rule). The client never says or implies "you've been blocked" |
| `conflict` | Screen-specific, keyed on `details` where present (`duplicate_pending_pair`, `pending_limit_reached`, `open_ticket_limit`, `duplicate_open_appeal`, name-in-use, second rating, second reply) — illustrative, not exhaustive |
| `state_conflict` | Screen-specific, keyed on `details` (`reason`, or `use`/`field` where a module uses them): `ostad_not_accepting` → the not-accepting notice; `profile_incomplete` → route to Shagred setup; `reopen_window_closed` → offer a new ticket; `thread_frozen:<clause>` → the frozen-chat banner; `rating_removed` → "removed by moderation"; `under_review` → the locked-revision state; OSP's `use: onboarding` / `use: patch` → send the edit to the right editor |
| `account_recoverable` | Registration → offer the login/recover path (REG-02) |
| `locked_out` | Disable the action and show the countdown from `details.retry_after_seconds` |
| `app_update_required` | Full-screen forced-update gate; no dismissal |
| `rate_limited` | Soft back-off message; honour `Retry-After` before re-enabling |

## Global states every screen implements

- **Loading** — skeletons, not spinners, on content screens; the map shows first pins within ≈2 s on 4G (NFR-02), progressively.
- **Empty** — a purposeful empty state with the one action that resolves it (discovery zero-result → "widen radius", MAP-04; empty inbox → what to do next). Never a blank screen.
- **Error / offline** — a retry affordance; cached content stays readable where it exists. The device floor (NFR-01) and intermittent 3G/4G (NFR-03) are assumed, not exceptional; the last-loaded map and open chats stay readable offline with a clear indicator.
- **The notification principle** (OFR-03, SUP-03) — every push has an in-app counterpart (inbox state, unread badge), so a user who denied notifications never permanently misses anything. The UI derives badges from data (unread counts, pending states), not from delivery.

## Shared components

Defined once here; module docs reference them by name rather than re-describing them.

- **Ostad preview card / map pin** — the map projection (MAP): photo, display name, verified badge, headline, rating + count (or "New" when count is 0), distance (computed on-device from map centre). Tapping opens the public profile.
- **Public Ostad profile** — the full `GET /v1/ostads/{id}` shape (OSP): identity, skills, education, experience, portfolio, exact map pin, reviews, trust signals, and — for a signed-in viewer — their own offer/favourite state. Paused Ostads show the not-accepting banner.
- **Shagred projection** — the fixed narrow card an Ostad sees (SGP): name, photo, gender, area (district + thana), joined date. Never more, and it disappears when an offer lapses.
- **Rating stars & review** — 1–5 display and input, the written review, the Ostad's reply beneath, "Former Shagred" for anonymised authors.
- **Verified badge** — shown only for approved Ostads; granted solely by admin (ADM-03/RNT-09).
- **Offer row** — status, countdown for pending, the action set for the role (withdraw / accept-decline), the status-dependent counterpart projection.
- **Chat bubble & composer** — text and voice notes only (OFR-05), delivery/read ticks, the frozen-chat banner when the writable predicate fails, the revealed-contact header on connection.
- **Cascading address picker** — Division→District→Thana→postal, from `GET /v1/admin-areas` (OSP/SGP/REG).
- **Fuzzy category picker** — the cross-script typeahead from `GET /v1/skill-categories?q=` (OSP-04).
- **Media viewers & capture** — signed-URL image/video/document viewers; the **in-app live selfie capture** for identity (CL-017, gallery closed); the voice recorder capped at 2 minutes (OFR-05); upload progress against the upload-ticket flow.

## Consent and privacy surfaces (must appear where specified)

- **18+ gate** at registration (REG-03) — before any account.
- **Location public-pin consent** — the plain statement that the pin is publicly visible at exact precision, on every location-setting surface (MAP-01).
- **Contact-reveal confirmation** — acceptance states that phone and verified email will be shared, before the Ostad accepts (OFR-04).
- **Legal documents** — Terms and Privacy reachable from the guest map, registration, and Settings (REG-13, MAP-03), served by `GET /v1/legal/*`.

## Accessibility and input (NFR-10)

Build-time requirements the visual design and implementation both inherit: touch targets **≥ 44 dp**; text respects **OS font scaling** without layout breaking; colour contrast meets **WCAG AA**; interactive elements are **labelled for screen readers** on at least registration, onboarding, map, offers, and chat. **Bangla rendering is complete and tested** on the reference device — conjunct consonants, vowel signs, and numerals render correctly with the chosen Bangla typeface, never assumed. Portrait-first; no landscape requirement in the MVP (NFR-01).

## Notifications (OFR-03, SUP-03, CL-015)

Push categories: offer received; offer accepted/declined; day-5 expiry reminder; new chat message (suppressed while that chat is open); **verification verdict** — approved / changes requested / rejected (REG-11, OSP/ADM); ticket reply; admin warning; broadcast. Each deep-links to its screen. There are **no per-category preferences** in the MVP — control is at the OS level only. Every category has its in-app counterpart per the notification principle.

## The screen-spec template

Each module ui document lists its screens in a fixed shape:

- **Screen** — name and which shell(s) it belongs to.
- **Purpose** — the one job it does (one line).
- **Entry points** — how it is reached (nav tab, deep link, push, another screen's action).
- **Structure** — the content regions and the components (above) they use, top to bottom.
- **States** — loading / empty / error, plus every screen-specific state (e.g., paused, frozen, under-review), each mapped to what the user sees.
- **Data & actions** — the api endpoints that populate it and that its actions call, with the request each action sends.
- **Validation & copy notes** — field rules and the screen-specific error copy (treatment per the mapping table above).
- **What it never shows** — the privacy boundary at the screen, mirroring each api's "what this module does not expose".

followed by **flows** (multi-screen sequences) where a task crosses screens.

## Document sequence

`ui-overview.md` (this) → REG ✅ → OSP ✅ → SGP ✅ → MAP ✅ → OFR ✅ → RNT ✅ → SUP ✅ → ADM ✅ (dashboard) → `ui/public-website.md` ✅ (CL-020). Each derives from its requirements, cites its api/data-model, is drafted, adversarially reviewed, then approved — the same discipline as the api layer.
