---
project: 3i
module: identity-and-access
type: implementation-spec
status: current
updated: 2026-08-18
id: 3I-IDA-IMPL-001
derived_from:
  - 3i/modules/identity-and-access/data-model.md
  - 3i/modules/identity-and-access/requirements/auth-registration-and-authentication.md
  - 3i/modules/identity-and-access/requirements/rbac-roles-and-permissions.md
  - 3i/modules/identity-and-access/requirements/fam-family-accounts-and-profiles.md
tags:
  - implementation
  - backend
  - prisma
  - express
---

# Identity and Access — Backend Implementation Detail

Handed to the developer building this module. Stack: **Node.js, Express, Prisma, PostgreSQL** — compatible with §20.1, which specifies Node.js without naming a framework.

Every model, field, and endpoint below cites the FR code or decision it implements. Where this document adds detail the requirements documents don't specify (exact status codes, field types), that detail is this document's own judgement call, not a restatement of something already decided elsewhere — flag anything that looks wrong rather than assuming it's settled.

All seven pending-scope decisions (014–016, 018–019, 021–022) are approved for build — [3I-DEC register](/3i/decisions/README.md). Build to the amended behaviour throughout, not the original baseline text.

---

## 1. Prisma Schema

```prisma
enum Locale {
  EN
  BN
  HI
  UR
  AR
}

enum SocialProvider {
  GOOGLE
  APPLE
}

// Account type (adult / 13-17 standalone) is DERIVED from dateOfBirth,
// never stored. Compute it in application code, not the schema.
// FR-AUTH-03: under-13 is never persisted as an Account at all.
model Account {
  id              String    @id @default(uuid())
  firstName       String
  lastName        String
  email           String    @unique
  emailVerified   Boolean   @default(false)
  pendingEmail    String?   // set during an email change; not yet verified
  passwordHash    String?   // nullable: social-only accounts have none
  dateOfBirth     DateTime  // FR-AUTH-01/02. Determines account type on every read.
  locale          Locale    @default(EN)

  // FR-AUTH-05 — only populated for 13-17 standalone accounts
  guardianName    String?
  guardianEmail   String?
  guardianNotifiedAt DateTime?

  socialProvider  SocialProvider?
  socialId        String?

  // FR-RBAC-05 — admin accounts only, optional
  totpSecret      String?
  totpEnabled     Boolean   @default(false)

  createdAt       DateTime  @default(now())
  updatedAt       DateTime  @updatedAt

  learners        Learner[]
  devices         Device[]
  deviceChanges   DeviceChangeLog[]
  roleAssignments RoleAssignment[]

  @@index([email])
  @@index([socialProvider, socialId])
}

// FR-FAM-02 as amended by 3I-DEC-014: cap counts NEVER_ACTIVATED + ACTIVE only.
// INACTIVE and DELETED never count toward the 6-profile cap.
enum ProfileState {
  NEVER_ACTIVATED
  ACTIVE
  INACTIVE
  DELETED
}

model Learner {
  id            String       @id @default(uuid())
  accountId     String
  account       Account      @relation(fields: [accountId], references: [id])

  displayName   String
  nameLocked    Boolean      @default(false)  // FR-FAM-05, set true on first certificate issue
  dateOfBirth   DateTime                       // FR-FAM-07: immutable except via admin correction endpoint
  avatarUrl     String?

  pinHash       String                         // FR-FAM-03 as amended by 3I-DEC-018: mandatory, guardian-set

  state         ProfileState @default(NEVER_ACTIVATED)
  seatId        String?      @unique           // set only when state = ACTIVE. 3I-DEC-009: 1:1, never reassigned
  activatedAt   DateTime?
  cancelledAt   DateTime?
  deletedAt     DateTime?

  createdAt     DateTime     @default(now())
  updatedAt     DateTime     @updatedAt

  pinAttempts   PinAttempt[]
  activationLogs ProfileActivationLog[]

  @@index([accountId, state])
}

// 3I-DEC-022: lockout matches FR-AUTH-09 exactly — 5 failed attempts,
// 15-minute lockout, progressive delay, per-IP rate limiting.
model PinAttempt {
  id         String    @id @default(uuid())
  learnerId  String
  learner    Learner   @relation(fields: [learnerId], references: [id])
  succeeded  Boolean
  ipAddress  String
  createdAt  DateTime  @default(now())

  @@index([learnerId, createdAt])
  @@index([ipAddress, createdAt])
}

// FR-FAM-06 as amended: rate-limited to 2 per 30 days, but the limit now
// covers ACTIVATE/CANCEL only — profile CREATE is free and untracked here.
model ProfileActivationLog {
  id         String    @id @default(uuid())
  learnerId  String
  learner    Learner   @relation(fields: [learnerId], references: [id])
  action     String    // "ACTIVATE" | "CANCEL"
  seatId     String?
  createdAt  DateTime  @default(now())

  @@index([learnerId, createdAt])
}

// FR-RBAC-01: permissions are module.action keys, never hard-coded role checks.
model Role {
  id          String            @id @default(uuid())
  name        String            @unique  // "Admin" | "Instructor" | "Member" — 3I-DEC-017 renamed the third
  permissions RolePermission[]
  assignments RoleAssignment[]
}

model Permission {
  id    String            @id @default(uuid())
  key   String            @unique  // e.g. "course.publish", "chat.moderate"
  roles RolePermission[]
}

model RolePermission {
  roleId       String
  permissionId String
  role         Role       @relation(fields: [roleId], references: [id])
  permission   Permission @relation(fields: [permissionId], references: [id])

  @@id([roleId, permissionId])
}

model RoleAssignment {
  id        String   @id @default(uuid())
  accountId String
  roleId    String
  account   Account  @relation(fields: [accountId], references: [id])
  role      Role     @relation(fields: [roleId], references: [id])

  @@unique([accountId, roleId])
}

// FR-AUTH-11 as amended by 3I-DEC-015: allowance = seats + 2, floor 3.
// Allowance itself is computed from commerce's seat count, not stored here.
model Device {
  id         String    @id @default(uuid())
  accountId  String
  account    Account   @relation(fields: [accountId], references: [id])
  name       String
  lastSeenAt DateTime  @default(now())
  createdAt  DateTime  @default(now())

  @@index([accountId])
}

// Swap limit: 2 per 30 days (FR-AUTH-11, unchanged by decision)
model DeviceChangeLog {
  id        String   @id @default(uuid())
  accountId String
  account   Account  @relation(fields: [accountId], references: [id])
  changedAt DateTime @default(now())

  @@index([accountId, changedAt])
}

// FR-AUTH-04: no personal data, hash only. Not analytics — do not repurpose.
model BlockedRegistrationAttempt {
  id           String   @id @default(uuid())
  sessionHash  String
  attemptedAt  DateTime @default(now())

  @@index([sessionHash])
}

// NFR-09: admin/financial action audit log. Used by name-unlock and
// DOB-correction endpoints below.
model AdminAuditLog {
  id          String   @id @default(uuid())
  adminAccountId String
  action      String   // "PROFILE_NAME_UNLOCK" | "PROFILE_DOB_CORRECTION" | ...
  targetType  String   // "Learner" | "Account" | ...
  targetId    String
  reason      String
  metadata    Json?
  createdAt   DateTime @default(now())

  @@index([targetType, targetId])
}
```

**Not modelled here, owned elsewhere:** the Stripe seat/subscription record (`commerce`), the Learner-to-enrolment/certificate relations (`learning-delivery`, `certification`), chat message tombstoning (`communication` — but see §4 below for the deletion cascade contract).

---

## 2. Auth Endpoints

### `POST /auth/register`

FR-AUTH-01–02, FR-AUTH-06.

1. Validate fields. Compute age from `dateOfBirth`.
2. **Age < 13:** do not create an Account. Insert `BlockedRegistrationAttempt` with a hashed session identifier (FR-AUTH-04). Return `403` with the neutral, sign-off-gated message from [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) — do not hard-code English text here; pull from the exempt string set, per locale.
3. **Age 13–17:** require `guardianName`, `guardianEmail` (FR-AUTH-05). Create Account. Send guardian notification (also exempt-set copy). Set `guardianNotifiedAt`. Log the send with timestamp and address — this is an acceptance criterion, not optional instrumentation.
4. **Age 18+:** create Account normally.
5. In all non-blocked cases: hash password with Argon2id (FR-AUTH-08), run breach check via k-anonymity (send only the SHA-1 prefix, never the password), send verification email.
6. Response: `201`, account is unverified (`emailVerified: false`).

### `POST /auth/register/social/callback`

FR-AUTH-07.

On **first** login via Google/Apple: capture `dateOfBirth` before any Account row is written, then run the exact same age branch as `/auth/register` above. **No exception for this path** — the acceptance criterion is explicit that under-13 cannot succeed by any route.

### `POST /auth/login`

FR-AUTH-09, FR-AUTH-13.

Email + password only, or delegate to social callback. On failure, do not distinguish "wrong password" from "no such account" in the response. Track failures per account (not globally); 5 failures → 15-minute lockout with progressive delay on top, plus per-IP rate limiting independent of the account-level counter. No phone/OTP path exists in this router at all.

If `totpEnabled`, respond `202` requiring `POST /auth/login/totp` with the code before issuing a session.

### `POST /auth/password-reset/request` / `POST /auth/password-reset/confirm`

FR-AUTH-10. Token: single-use, 30-minute expiry, invalidate on use or expiry with an identical "link no longer valid" message for both cases.

### `POST /account/email/change`

Not in the baseline as a named requirement; specified in [3I-IDA-REQ-001](/3i/modules/identity-and-access/requirements/auth-registration-and-authentication.md#registration).

Sets `pendingEmail`, sends verification to the *new* address. `emailVerified` and login access on the *old* address are untouched until the new one confirms — do not flip `emailVerified` to `false` mid-change.

### `POST /account/email/verify`

On valid token: if `pendingEmail` is set, promote it to `email` and clear `pendingEmail`. Otherwise this is the original registration verification — set `emailVerified: true`.

---

## 3. Device Endpoints

### `GET /account/devices`

Returns devices plus **the account's current allowance**, computed as `max(3, seatCount + 2)` per [3I-DEC-015](/3i/decisions/dec-015-device-allowance-scales-with-seats.md). `seatCount` is read from `commerce` — this endpoint calls into (or is joined with) the commerce seat count at request time; do not cache it here, since it changes independently of this module.

### `POST /account/devices`

Refuse with `403` if `devices.length >= allowance`, naming the current allowance in the response body. Check `DeviceChangeLog` for the account: refuse registration-as-swap if 2 changes already logged in the trailing 30 days.

### `DELETE /account/devices/:id`

De-authorise. Insert a `DeviceChangeLog` row only if this delete is paired with a registration within the same session (i.e. counts as a swap) — a de-authorisation with no replacement device does not consume swap allowance. Confirm this interpretation with product before shipping; the baseline doesn't disambiguate "swap" from "remove."

---

## 4. Profile Endpoints

### `POST /account/profiles`

FR-FAM-01–03.

Gate: caller's own `Account.dateOfBirth` must resolve to 18+. Count existing Learners in `NEVER_ACTIVATED` or `ACTIVE` state for this account; refuse with `403` if already 6 ([3I-DEC-014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md)) — the error body should be distinguishable from a seat-unavailable error (different `code` field), since a Member conflating the two will file the wrong support ticket.

Requires `pinHash` set on creation (hash a guardian-supplied 4-digit PIN with the same algorithm as passwords — Argon2id is fine for 4 digits despite the small keyspace, since lockout is the real defence, not hash cost).

**Not rate-limited** by `ProfileActivationLog` — that log only covers activate/cancel.

### `PATCH /account/profiles/:id`

FR-FAM-05, FR-FAM-07.

`displayName`, `avatarUrl` editable. **`dateOfBirth` is not an accepted field on this route at all** — omit it from the request schema entirely rather than accepting-and-ignoring it, so a client sending it gets a validation error, not silent data loss.

If `nameLocked === true`, refuse `displayName` changes with `403` and a reason ("locked after certificate issue").

### `POST /account/profiles/:id/pin/reset`

[3I-DEC-018](/3i/decisions/dec-018-profile-pin-mandatory-guardian-controlled.md). Guardian-only (caller must be the owning Account, no learner-facing path exists for this at all). No email/token flow — this is a same-session, already-authenticated action.

### `POST /profiles/:id/select`

The profile-picker action. FR-FAM-04, [3I-DEC-022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md).

Accepts a 4-digit PIN. Check `PinAttempt` history for this learner: if 5 failures in the trailing window, refuse with `429` and a `retryAfter`. On success, insert a `succeeded: true` `PinAttempt` row (also useful for audit) and issue a profile-context token/session marker. On failure, insert `succeeded: false` and apply the same progressive-delay shape as `/auth/login`.

### `POST /account/profiles/:id/activate`

Called after `commerce` confirms a seat purchase (webhook-driven, per FR-BILL-03 — **never** from a client-side success redirect). Sets `state: ACTIVE`, `seatId`, `activatedAt`. Insert `ProfileActivationLog` action `"ACTIVATE"`; refuse (`403`) if 2 activate/cancel actions already logged for this learner in the trailing 30 days (FR-FAM-06 as amended).

### `POST /account/profiles/:id/cancel`

[3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md). Sets `state: INACTIVE`, `cancelledAt`, clears `seatId` (the seat itself is released back to `commerce` for a *new* purchase — it is not reassignable to another Learner directly). Insert `ProfileActivationLog` action `"CANCEL"`, same rate-limit check as activate. **Does not touch** progress, enrolments, exam results, or chat history — those tables are untouched by this call, which is precisely what distinguishes cancel from delete below.

### `DELETE /account/profiles/:id`

FR-FAM-10, [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md).

This endpoint's own responsibility is narrow: set `state: DELETED`, `deletedAt`, and remove progress/enrolment/exam-result rows it owns (delegate to `learning-delivery`/`assessment` via event or direct call — implementation detail for the developer to choose). **Certificates are untouched** — they read from a snapshot, not from the Learner row (see [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)), so no cascade is needed there at all.

**Chat cascade contract, owned by `communication` but triggered from here:** on delete, emit an event (or call) that causes `communication` to tombstone this Learner's message content and anonymise authorship to "Deleted learner," while retaining `reports` and `moderation actions` referencing those messages. This module does not implement that logic — it is `communication`'s table — but this endpoint is the trigger point and should not return success until that cascade is confirmed (synchronous call) or reliably queued (async with a dead-letter path) — developer's choice, flag which was chosen in the PR description since it affects the deletion-confirmation UI's guarantees.

Requires the confirmation payload specified in [Profile deletion confirmation](/3i/modules/identity-and-access/ui/screens/profile-deletion-confirmation.md) (typed display-name match or equivalent) — enforce that in the request validation, not just the frontend.

---

## 5. Admin Endpoints

### `POST /admin/profiles/:id/unlock-name`

FR-FAM-05. Sets `nameLocked: false`. Requires `reason` in the body, written to `AdminAuditLog`. **Does not touch any already-issued certificate row** — those are immutable snapshots regardless of what happens to the live profile afterward.

### `PATCH /admin/profiles/:id/dob`

FR-FAM-07, [3I-DEC-022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md).

**The single highest-leverage endpoint in this module.** Before writing the new `dateOfBirth`:

1. Compute old chat eligibility and new chat eligibility (derive from age, per FR-FAM-08 / [age-and-safeguarding.md](/3i/age-and-safeguarding.md)).
2. Write the new `dateOfBirth`. Write `AdminAuditLog` with `reason` — required field, no default.
3. **If eligibility changed**, trigger a notification to the account holder via the standard channel (FR-NOT-01–08: push + email, profile named in body). Do not trigger if eligibility is unchanged.
4. All other age-derived reads (catalogue filtering, age band badge) pick up the new value automatically on next read — no separate cascade needed, since those modules compute from `Learner.dateOfBirth` live rather than caching it.

Permission key: something narrow like `identity.correct_dob` rather than a blanket admin check — even though only one Admin role exists at launch (FR-RBAC-04's "no hard-coded checks" applies here as much as anywhere, and this is the endpoint most worth being able to restrict later without a redeploy).

### `POST /admin/roles`, role management generally

**Not built at launch.** [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md) confirms role creation is a direct database/seed operation at this stage, not an API surface. Do not scaffold this route; add it only when sub-admin roles are actually approved (§23 item 5, currently deferred).

---

## 6. Middleware

| Middleware | Purpose |
| :---- | :---- |
| `requireAuth` | Valid session/JWT present |
| `requireVerifiedEmail` | Blocks enrolment/checkout/chat routes per FR-AUTH-06. Does **not** block `/account/email/*` or `/auth/*` routes themselves |
| `requirePermission(key)` | Looks up `RoleAssignment → Role → RolePermission → Permission`. Default: `403` if absent. **Exception, not implemented here but worth knowing:** `assessment`'s question-bank routes return `404` instead — [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md). Keep this middleware's default at 403 and let `assessment` override per-route, rather than building a global 404 mode |
| `pinLockout` | Applied to `/profiles/:id/select` only. FR-AUTH-09 shape, per [3I-DEC-022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md) |

**No occurrence of `req.user.role === 'admin'` or equivalent anywhere in route handlers** — this is FR-RBAC-03's acceptance criterion and should be enforced in code review or a CI grep step, not just at delivery.

---

## 7. Open Items the Developer Should Know About

| Item | Status |
| :---- | :---- |
| OQ-11 — minimum sessions before an attendance certificate | Open, not this module's concern directly, but touches the same `learning-delivery`/`certification` boundary this module's delete cascade interacts with |
| Device swap vs. remove distinction (§3 above) | My interpretation, not confirmed — verify before shipping |
| Chat cascade: sync vs. async on profile delete (§4 above) | Developer's implementation choice; state it explicitly |
| Safeguarding string sign-off | The exempt strings referenced in §2 do not exist as translated, signed-off copy yet — [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md). Backend can ship with English placeholders; do not localise these five particular strings via the normal AI pipeline even as a stopgap |
