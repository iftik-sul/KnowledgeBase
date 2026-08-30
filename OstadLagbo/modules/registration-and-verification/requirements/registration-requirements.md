---
project: OstadLagbo
module: registration-and-verification
type: requirements
status: current
updated: 2026-08-30
id: OL-REG-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.1.md
owner: Iftikher
---

# Registration & Verification — Requirements

Derived from MVP Scope Baseline v1.1 §1 and §7. Governs account creation, authentication, and Ostad onboarding through submission for review. Admin-side review is governed by the `admin-review` module; profile field definitions by `ostad-profile` and `shagred-profile`.

## Actors

**Visitor** — no account. **Shagred** — learner account. **Ostad (pending)** — Ostad account not yet approved. **Ostad (approved)** — discoverable Ostad. **System** — automated behavior.

## REG-01 Role selection

A visitor registering must choose exactly one role: Ostad or Shagred. The role is permanent for the account's lifetime and is never changeable in any interface.

**Acceptance:** role is required before any other registration step; no role-change mechanism exists anywhere in app or API.

## REG-02 Phone registration and OTP

Registration requires a Bangladeshi mobile number, verified by OTP before the account is created. Proposed defaults: 6-digit OTP, 5-minute expiry, resend allowed after 60 seconds, maximum 5 OTP requests per number per 24 hours, maximum 5 wrong attempts per OTP before it is invalidated. One account per phone number per role is not enforced — one account per phone number, full stop.

**Acceptance:** unverified numbers never produce accounts; rate limits verifiably block the 6th request in 24h; a phone number in use cannot register a second account.

## REG-03 Password and date-of-birth gate

At registration the user sets a password (minimum 8 characters, at least one letter and one number) and provides date of birth. If the date of birth yields age under 18, registration is refused with a clear message; no account or partial record is created.

**Acceptance:** under-18 DOB cannot produce an account by any path; password rules enforced server-side.

## REG-04 Optional email

Email may be added at registration or later from settings. An added email must be verified by a link or code before it is marked verified. Unverified emails are stored but never displayed as verified and never used for account recovery. An email address may be linked to only one account; adding an email already verified elsewhere is refused. A verified email is revealed mutually on offer acceptance where present, per OFR-04.

**Acceptance:** verified flag only after confirmed verification; recovery flows ignore unverified emails; a verified email cannot be attached to a second account.

## REG-05 Login and sessions

Login is phone + password. Sessions persist until logout (no forced expiry in MVP). Multiple simultaneous devices are permitted. Proposed default: 5 failed logins per account per 15 minutes triggers a temporary lockout with retry-after messaging.

**Acceptance:** correct credentials log in on Android and iOS; lockout engages and releases as specified.

## REG-06 Password reset and change

Reset is via OTP to the account's verified phone number, then a new password. The same OTP rate limits as REG-02 apply. A logged-in user may also change their password from settings by providing the current password; all other sessions are invalidated on change.

**Acceptance:** reset works with phone access alone; old password is invalidated immediately on reset or change; logged-in change requires the current password.

## REG-07 Phone number change

A logged-in user may change their phone number by verifying an OTP on the **new** number. The new number must not belong to another account. On success the old number is released and login uses the new number immediately.

**Acceptance:** change requires new-number OTP; collision with an existing account is refused; old number no longer authenticates.

## REG-08 Shagred onboarding

After registration a Shagred provides display name (required) and address (street line plus Thana, District, Division, and Postal Code dropdowns, per SGP-02), and may add profile basics per the `shagred-profile` module. They then land on the map. No identity verification is collected from Shagreds in the MVP.

**Acceptance:** a Shagred can go from app install to viewing the map with only: role, phone+OTP, password, DOB, display name, address.

## REG-09 Ostad onboarding wizard

Ostad onboarding is a fixed sequence of stages, in this order: **1 Personal information → 2 Identity verification → 3 Address → 4 Map location → 5 Professional details (profession, skills, education, experience, portfolio) → 6 Review & submit.** Field definitions belong to the `ostad-profile` module. Each stage saves on completion (and drafts save on field entry where practical); closing the app never loses entered data. Reopening the app resumes at the first incomplete stage. A stage cannot be entered until all previous stages are complete; completed stages can be revisited and edited before submission.

**Acceptance:** kill-and-reopen at every stage resumes without data loss; stage order is enforced; submission is impossible with any incomplete stage.

## REG-10 Identity document capture

Stage 2 collects: document type (NID or passport), ID number, front image, back image (NID only), and a selfie. Images are captured by camera or gallery upload. The stage states plainly that documents are seen only by admin review and never shown publicly. **An ID number already associated with another active account is flagged at submission; approval is blocked until the duplicate is resolved (ADM-03).**

**Acceptance:** NID requires both images; passport requires one; selfie is always required; the privacy statement is displayed on the stage; a duplicate ID number cannot reach approval.

## REG-11 Submission and pending state

Completing stage 6 submits the profile for admin review and sets the account to **pending**. A pending Ostad has full app access — browsing the map, viewing profiles, editing their own profile — but is not discoverable and cannot receive offers. The app shows current review status (pending / changes requested / rejected / approved) and any admin reason. Editing and resubmitting after rejection or change requests follows the `admin-review` module's rules.

**Acceptance:** pending Ostads never appear in map, search, or category results; status and admin reasons are visible in-app; approval flips discoverability without re-login.

## REG-12 Platform rules inherited

18+ applies to both roles (REG-03). Push notification enrollment is requested during onboarding (delivery rules per `contact-and-offers`). Self-service account deletion exists in settings for both roles; deletion of identity data follows the retention policy (see risk R-02).

## REG-13 Consent capture

Registration requires explicit acceptance of the Terms of Service and Privacy Policy (unchecked-by-default consent action) before an account is created; the accepted **document versions and timestamp are recorded** per account. When either document changes materially, users receive an in-app notice before the change takes effect (as both documents promise); continued use after notice is recorded against the new version. The Privacy Policy and Terms are also reachable **without an account** from the guest map screen (see MAP-03), satisfying app-store requirements.

**Acceptance:** no account exists without a recorded consent version; a material policy change produces an in-app notice; a guest can open both documents without registering.

## Proposed technical defaults summary

OTP 6 digits / 5 min / resend 60s / 5 per number per day / 5 attempts · password min 8 chars, letter + number · login lockout 5 fails per 15 min · sessions persistent, multi-device. These are engineering defaults, changeable without founder re-approval; everything else in this document changes only with founder approval.
