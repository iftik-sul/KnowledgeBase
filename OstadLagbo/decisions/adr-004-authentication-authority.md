---
project: OstadLagbo
type: decision
status: accepted
updated: 2026-09-25
id: OL-DEC-004
supersedes: none
owner: Iftikher
---

# ADR-004 — Authentication authority and token model

Resolves an ambiguity the API Overview and REG documents left open once the code
had to be written: **who verifies passwords and who mints session tokens** — our
API, or Supabase Auth. It does not change any product behaviour; it records the
mechanism the API uses to satisfy what those documents already require.

## Context

The REG api and API Overview describe user tokens as "Supabase-issued JWTs,
obtained only through the API's auth endpoints (the API creates the Supabase Auth
user and session server-side)", and say the account is created at
`register/verify`. But two facts in the same specification only fit one design:

1. `register/verify`'s request body is `{ registration_id, otp }` — **the
   plaintext password is not present**. It was sent once, at `register/start`,
   and REG-DM stores only its **hash** in `pending_registration`. So at the
   moment the account is created, the API no longer holds the plaintext and
   cannot hand a password to Supabase Auth.
2. `user_account` itself carries a **`password_hash`** column (REG-DM), i.e. the
   API is meant to hold the credential of record.

Reconciled, these say the **API is the authentication authority**: it owns the
password and it issues the tokens. Supabase's role is to *accept* those tokens on
its direct channels (Realtime chat, Storage media), which it does by verifying
their signature — it does not need to have minted them.

## Decision

- **The API owns the password.** It is hashed at `register/start` (scrypt, a
  memory-hard function built into the platform — no plaintext, ever, anywhere)
  and stored on `user_account.password_hash`. Login verifies against it. Supabase
  Auth is **not** used as the password store, so no plaintext is needed at verify
  and no partial account exists before the OTP succeeds (REG-03 acceptance holds).
- **The API mints the tokens**, signing them with the **project's Supabase JWT
  secret** (HS256) so they are genuine, Supabase-valid JWTs. This is what "the API
  creates the session server-side" means in practice. Each access token carries
  `sub = user_account.id`, `role = "authenticated"`, `aud = "authenticated"`, and
  a short expiry. Because `auth.uid()` and the row-level-security policies read
  the `sub` claim, and Realtime/Storage validate the signature with the same
  secret, the direct channels accept these tokens exactly as if Supabase Auth had
  issued them — the two lines of defense (policy layer + RLS) are unchanged.
- **Refresh + revocation live in `auth_session`.** The refresh token is a signed
  token bound to an `auth_session` id; refresh checks the row is not revoked and
  the account is still valid, then issues a new access token. Logout, password
  change, suspension, deletion, and termination all revoke by setting
  `auth_session.revoked_at` — the model REG-DM already describes.
- **No `auth.users` row is created.** With the API signing tokens and RLS keying
  off `sub`, a Supabase Auth user record is not required for anything the MVP
  does. This is the **one wording deviation** from the API Overview / REG api
  ("creates the Supabase Auth user"); this ADR is the reconciling record, and
  those documents should be read as "creates the account and its session" — the
  account being `user_account`, the session being the signed tokens.

## Consequences

- One clear authority. Passwords, lockout, the 18+/consent gates, deletion-window
  recovery, and suspension all live in the API and the schema REG-DM already
  defines — nothing depends on Supabase Auth's own user table or flows.
- The **Supabase JWT secret is now a signing secret** held only by the API
  (Render env), never shipped to any client — same handling as the service-role
  key. If it rotates, live access tokens are invalidated at their next verify;
  refresh still works because `auth_session` is the source of truth.
- The admin token family is entirely separate (its own key and audience, ADM-20)
  and unchanged by this record; the two families still never cross.
- **Immediate-suspension window** is unchanged and as the API Overview already
  accepts: a short-lived access token stays valid until it expires; RLS's
  status check and refresh revocation close the window. Access-token lifetime is
  kept short (engineering default) to bound it.

## Alternatives considered

- **Supabase Auth as the authority** (create the auth user with the password,
  use its sessions) — rejected: `register/verify` has no plaintext to give it,
  so the auth user would have to be created at `register/start`, before the OTP,
  which is the partial account REG-03 forbids; and it would split the credential
  of record across two stores.
- **API stores password *and* mirrors it into Supabase Auth** — rejected:
  double storage, two things to keep in sync, and still no plaintext at verify.
- **Opaque API sessions, no JWT** — rejected: the direct Supabase channels
  (Realtime, Storage) must validate a token themselves; a Supabase-valid JWT is
  what lets them, without the API proxying chat and media.
