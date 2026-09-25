---
project: OstadLagbo
module: registration-and-verification
type: ui
status: current
updated: 2026-09-25
id: OL-REG-UI-001
derived_from: /OstadLagbo/modules/registration-and-verification/requirements/registration-and-verification-requirements.md
owner: Iftikher
---

# Registration & Verification — UI

Screens for language choice, account creation, authentication, Shagred setup, the Ostad onboarding wizard, review status, account settings, and the suspension shell. Conventions per [UI Overview](/OstadLagbo/ui-overview.md); behaviour and endpoints per [REG API](/OstadLagbo/modules/registration-and-verification/api/registration-and-verification-api.md); field definitions for profile stages belong to the OSP, SGP, and MAP ui/api docs and are cited, not repeated. Error treatments are the overview's mapping table; each screen names only its screen-specific copy.

This is the module that stands up the three shells. A visitor arrives at the **guest shell** (map-first, MAP ui); the screens here are the doors from guest into a Shagred or Ostad shell, plus everything under Settings and the suspension landing.

## Group A — Language and entry (pre-account)

### Language choice — first launch, before anything (REG-14)
- **Purpose:** pick English or Bangla before any other screen.
- **Entry:** first app launch, once, before anything else is shown.
- **Structure:** the two language options, nothing else.
- **States:** none beyond the choice.
- **Data & actions:** stored device-local for a guest; there is no account yet, so no API call. Immediately after the choice the guest lands on the **map** (map-first, MAP-03; MAP ui). The whole UI re-renders in the chosen language and stays there until changed in Settings.
- **Never shows:** nothing about any account.

### Entry points from the guest shell
- **Purpose:** the doors from guest browsing into a Shagred/Ostad account.
- **Where:** there is no standalone welcome screen — **Log in** and **Create account** live in the guest map's chrome (MAP ui), alongside the Terms and Privacy links (`GET /v1/legal/terms|privacy`, reachable without an account, REG-13). Any identity action a guest attempts (offer, favourite, report, block) routes here too and returns afterward (MAP-03).
- **Data & actions:** Log in → login (Group C); Create account → role selection (Group B).
- **Never shows:** whether any phone number has an account.

## Group B — Registration

### Role selection (REG-01)
- **Purpose:** choose Ostad or Shagred — permanent, never changeable.
- **Entry:** Create account.
- **Structure:** the two roles with a one-line description of each, and a plain statement that the choice is permanent.
- **Data & actions:** the choice is held client-side and sent with `register/start`.
- **Copy notes:** the permanence line must be unmissable — there is no role change anywhere later (REG-01).

### Registration form (REG-02, 03, 04, 13)
- **Purpose:** collect everything needed to create the account, and gate on 18+ and consent **before** an OTP is spent.
- **Entry:** after role selection.
- **Structure:** phone (BD mobile), password (≥8, a letter and a number — rules shown inline), date of birth, **optional email**, and the **consent action** — unchecked-by-default acceptance of Terms and Privacy, each openable inline (REG-13).
- **States:** submit disabled until valid; the 18+ and consent checks are enforced here and again server-side.
- **Email is a client-orchestrated two-step:** `register/start` carries no email (REG api), so an email entered here is submitted via `POST /v1/me/email` on the fresh session **immediately after** `register/verify` creates the account; it is stored unverified and verification proceeds exactly as in Settings (REG-04). The field is offered here only as a convenience; nothing about registration blocks on it.
- **Data & actions:** submit → `POST /v1/auth/register/start` with role, phone, password, DOB, `preferred_locale`, and `consent {tos_version, privacy_version}` (from `GET /v1/legal/versions`). On success → OTP screen.
- **Validation & copy (screen-specific):** `validation_failed details.date_of_birth = "under_18"` → the under-18 refusal message, no account created; `details.consent = "outdated"` → re-fetch versions and re-accept; `conflict` (phone in use) → "this number already has an account" with a Log in link; `account_recoverable` → the recovery interstitial (below). Everything else per the mapping table.
- **Never shows:** it *does* reveal that a number is in use or recoverable — this is the one place account existence is disclosed, and deliberately (REG-api → account existence). No other screen does.

### OTP verification (REG-02)
- **Purpose:** verify the phone and create the account.
- **Entry:** from the registration form.
- **Structure:** 6-digit code entry, a resend control, and the expiry indication.
- **States:** resend disabled until `resend_available_at`; wrong-code shows `details.attempts_remaining`; `locked_out` disables entry with the retry countdown; expired code offers resend or restart.
- **Data & actions:** verify → `POST /v1/auth/register/verify {registration_id, otp}` → the account is created and a session returned. Resend → `POST /v1/auth/register/resend`. On success, route by role: **Shagred → Shagred setup**; **Ostad → onboarding wizard at stage 1**.
- **Never shows:** the code itself in any log or echo; codes render in Latin digits (NFR-11).

### Account-recovery interstitial (REG-02, CL-015)
- **Purpose:** turn a registration attempt on a deletion-window number into a recovery, not a duplicate.
- **Entry:** `register/start` returned `account_recoverable`.
- **Structure:** a short explanation that this number has an account being deleted, and a **Log in to restore** action.
- **Data & actions:** → login (a successful login within the 30-day window recovers the account, REG-02).

## Group C — Authentication

### Login (REG-05)
- **Purpose:** phone + password sign-in.
- **Entry:** Welcome, the recovery interstitial, or any `unauthorized` redirect.
- **Structure:** phone, password, a **Forgot password** link.
- **States:** `unauthorized` shows one message whether phone or password is wrong; `locked_out` shows the retry countdown (5 fails / 15 min, keyed on the phone string).
- **Data & actions:** → `POST /v1/auth/login`. On success: **active** → the role's shell; **`recovered`** → a brief "welcome back, your account is restored" note then the shell; **suspended** → the suspension shell (Group H); a `pending_deletion` number logging in *is* the recovery path.
- **Never shows:** which of phone/password was wrong; whether a number exists (the uniform message and phone-keyed lockout hold, REG-api).

### Password reset (REG-06)
- **Purpose:** reset via OTP to the account's phone.
- **Entry:** Forgot password.
- **Structure:** step 1 phone → step 2 OTP + new password.
- **States:** step 1 **always** proceeds identically whether or not the number exists (no disclosure); OTP states as in registration; on success all sessions are revoked and the user logs in fresh.
- **Data & actions:** `POST /v1/auth/password/reset/start` → `.../verify {phone, otp, new_password}`.
- **Never shows:** whether the number had an account (start responds the same either way).

## Group D — Shagred setup (REG-08)

### Shagred setup
- **Purpose:** the one-time profile setup that lets a Shagred send offers; then the map.
- **Entry:** immediately after `register/verify` for a Shagred (the account summary shows `shagred.profile_complete = false`).
- **Structure:** display name (required), the **cascading address picker** (Division→District→Thana→postal, shared component), optional photo and gender — field rules per the SGP api.
- **States:** first-time setup uses `PUT`; a re-opened, already-complete profile edits via `PATCH` (SGP api) — the client picks by `profile_complete`.
- **Data & actions:** → `PUT /v1/shagred-profile` → on success, the Shagred shell (Map home). Photo via the upload-ticket flow.
- **Note:** the map itself is reachable as a guest, so setup is not a hard gate on the map; it is enforced at **send-offer** (`state_conflict: profile_incomplete` routes back here, per the overview mapping and OFR).
- **Never shows:** any Shagred discovery surface — there is none (SGP).

## Group E — Ostad onboarding wizard (REG-09, REG-10)

The **onboarding shell**: a full-screen, six-stage sequence that owns the screen until submitted. `GET /v1/onboarding` on every open drives it — resume at `resume_stage`, stage *n* locked until 1…*n−1* are complete, completed stages revisitable and editable before submit. Every stage write saves immediately (`PUT /v1/onboarding/stages/{n}`); killing the app never loses data. A progress indicator shows the six stages.

### Stage 1 — Personal information
- **Structure:** legal name (English), legal name (Bangla — accepts Bangla script in either UI language), display name, **profile photo (required)**, gender — fields per OSP api (stage-1 payload).
- **Data:** `PUT /v1/onboarding/stages/1`. Photo via upload ticket (`profile_photo`).
- **Note:** DOB is **not** re-collected — captured at registration (REG-03).

### Stage 2 — Identity verification (REG-10, CL-017)
- **Purpose:** capture the document and the live selfie for admin review.
- **Structure:** document type — **NID / passport / driving licence**; ID number; **per-type document images** (NID front+back · passport photo page · driving licence front+back), by camera *or* gallery; and the **verification selfie — live in-app camera only, no gallery path, taken holding the document beside the face**, with on-screen framing guidance and retake. A plain **privacy statement**: documents are seen only by admin review, never shown publicly.
- **States:** per-type image requirements enforced before the stage can complete (`details.images = "back_required" | "back_not_allowed"`); a selfie that isn't a live-capture ticket is refused (`details.selfie = "invalid_ticket"`).
- **Data:** `PUT /v1/onboarding/stages/2`. Document images via upload tickets (`identity_front`/`identity_back`); the selfie via a `identity_selfie` ticket the app requests **only** from its live-capture flow.
- **Never shows:** a **duplicate-ID flag** is never surfaced to the Ostad — if their ID matches another account it is flagged for admin silently (REG-10, ADM-03); the user sees only normal progress. Captured images are never re-displayed as a public value.

### Stage 3 — Address
- **Structure:** street line + the cascading address picker — fields per OSP api (stage-3 payload).
- **Data:** `PUT /v1/onboarding/stages/3`; `details.address = "invalid_chain"` if the Division→postal chain is inconsistent.

### Stage 4 — Map location (MAP-01)
- **Structure:** set the teaching pin by device GPS or by dragging a manual pin on the map; the **public-pin consent statement** (the pin is publicly visible at exact precision — place it where you teach, not necessarily your home); a **self-preview** of the pin and preview card exactly as the public will see them.
- **States:** works with GPS denied (manual pin); self-preview available regardless of approval state.
- **Data:** `PUT /v1/onboarding/stages/4` (delegates to `PUT /v1/profile/location`, MAP api); self-preview via `GET /v1/profile/location/preview`.
- **Consent surface:** the public-pin statement must appear here (overview → consent surfaces).

### Stage 5 — Professional details
- **Structure:** headline, about, occupation, years of experience, languages; **skills (1–5)** via the fuzzy cross-script category picker plus free-text skill name, level, per-skill years; repeatable **education**; **experience**; and **portfolio** (images / one intro video ≤45 s / documents / links) — all field rules per OSP api (stage-5 payload and portfolio endpoints).
- **Data:** `PUT /v1/onboarding/stages/5`; portfolio via upload tickets. Deactivated categories never offered (`category_inactive` rejected).

### Stage 6 — Review & submit (REG-11)
- **Purpose:** a read-back of every stage, then submit for review.
- **Structure:** a summary of stages 1–5 with per-stage **Edit** jumps; a **push-notification enrollment** prompt (so verdict and offer notifications arrive, REG-12); a submit action.
- **Data:** submit → `POST /v1/onboarding/submit` → `approval_status = pending`; push token via `POST /v1/me/push-tokens`.
- **States:** submit refused with `state_conflict details.incomplete_stages` if any stage is incomplete — the summary flags which.

## Group F — Review status and pending state (REG-11)

### Review status
- **Purpose:** show a pending/approved Ostad where their review stands and carry admin notes.
- **Entry:** a banner across the Ostad shell while not approved, tapping into this screen; and the natural landing after submit.
- **Structure:** the current state — **pending / changes requested / rejected / approved** — and the admin's note where present (`last_verdict`).
- **States:** **pending** → full app access except discoverability (browse, view, edit own profile), a clear "under review" indicator, no offers can arrive; **changes requested / rejected** → the note is shown, app access is **retained** (not locked back into the wizard), and the banner offers **Edit & resubmit**, which re-enters the stages; **approved** → discoverability flips on without re-login, the banner clears.
- **App access after a verdict:** only the **initial** onboarding is full-screen-blocking (before the first submit). Once submitted, the Ostad keeps the running app in every non-approved state; the re-opened wizard is entered from the banner and left again freely, edits saving per stage as before.
- **Data & actions:** `GET /v1/onboarding` (`last_verdict`); on changes/rejected, the banner's Edit & resubmit re-enters the stages (editable) → `POST /v1/onboarding/submit`. Verdicts also arrive by push (verification-verdict category).
- **Never shows:** any reviewer identity.

## Group G — Settings (both roles)

### Settings home
- **Structure:** **Language** toggle (`PATCH /v1/me/locale`, re-renders immediately); **Account** (phone, email, password); **Legal** (Terms, Privacy); **Notifications** note (OS-level only — no in-app per-category toggles, CL-015); **Log out** (`POST /v1/auth/logout`, optionally all devices); **Delete account**.
- **Data:** `GET /v1/me` for the current values.

### Change phone (REG-07) · Manage email (REG-04) · Change password (REG-06)
- **Change phone:** new number → OTP **on the new number** → done; `conflict` if the number belongs to another account (reported only to this caller). `POST /v1/me/phone/change/start|verify`.
- **Manage email:** add (stored unverified) → verify by code → verified; remove; `conflict` if the email is verified on another account. `POST /v1/me/email`, `/email/verify`, `DELETE /v1/me/email`.
- **Change password:** current + new; all other sessions end on success. `PATCH /v1/me/password`; `unauthorized` if the current password is wrong.

### Delete account (REG-12)
- **Purpose:** self-service deletion for both roles.
- **Structure:** a plain statement of consequences (30-day recovery window; what leaves and when, per the retention policy) and a **password re-confirmation**.
- **Data & actions:** → `DELETE /v1/me {password}` → status `pending_deletion`, all sessions and push tokens revoked, pending offers resolved, chats freeze; the app returns to the signed-out Welcome. A message notes that logging in within 30 days restores everything.
- **States:** a **suspended** user cannot self-delete (`suspended`) — the action is hidden in that shell anyway.
- **Never shows:** it does not hard-delete on the spot; it is a reversible 30-day window (REG-02/CL-015).

### Consent re-acceptance notice (REG-13)
- **Purpose:** capture re-acceptance when Terms or Privacy change materially.
- **Entry:** shown on next open when the account summary reports `consent_current = false`.
- **Structure:** what changed, the documents, and an accept action; blocks nothing destructive but is surfaced until accepted.
- **Data:** `POST /v1/me/consent {tos_version, privacy_version}`.

## Group H — Suspension shell (REG-api, SUP-04)

### Suspension notice
- **Purpose:** the only screen a suspended (or terminated) account can reach.
- **Entry:** a `suspended` login lands here; any other call in this state returns `suspended` and returns here.
- **Structure:** the **suspension notice** (from `details`/the reduced account summary), an **Appeal** action, the user's **own ticket threads** (create an appeal; read and reply to any ticket they already own — SUP ui), a **language** toggle, and **log out**. Nothing else in the app is reachable.
- **Data & actions:** appeal and tickets are the SUP api; `PATCH /v1/me/locale`, `POST /v1/me/push-tokens` (so the reply reaches them), `POST /v1/auth/logout` all work; the reduced summary comes from `GET /v1/me`.
- **Never shows:** the full account summary (only id, role, status, locale, `banned_at`, `suspension_notice`); no profile, map, chat, or offer surface.

## Flows

**Install → browsing (guest).** Language choice → Welcome → Explore → the guest map (MAP ui). No account, no steps.

**Install → Shagred on the map.** Language → Create account → role: Shagred → registration form (18+, consent) → OTP → account created → Shagred setup (name + address) → map. (The baseline's minimum path: role, phone+OTP, password, DOB, name, address — REG-08.)

**Install → Ostad submitted for review.** Language → Create account → role: Ostad → registration → OTP → onboarding wizard stages 1–6 (each saving on completion; resumable) → submit → pending, with the review-status banner. On *changes requested*, the note shows and the stages re-open; on *approved*, discoverability turns on with no re-login.

**Suspension and appeal.** Login while suspended → suspension shell → Appeal → an appeal ticket (SUP) → follow it in-thread; nothing else in the app opens until reinstated.

## What this module's screens never show

No screen reveals whether a phone number has an account except the registration form itself (deliberate, REG-api); no screen shows another user's phone, email, DOB, or identity documents (contact reveal is OFR's, on acceptance); no screen shows an Ostad their duplicate-ID flag or any reviewer identity; the suspension shell exposes nothing beyond the notice, appeal, and owned tickets; and deletion is always the reversible 30-day window, never an instant erase.
