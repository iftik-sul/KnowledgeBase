---
project: OstadLagbo
type: decision
status: current
updated: 2026-09-26
id: OL-DEC-005
supersedes: adr-004 (in part — the signing-key clause only)
owner: Iftikher
decision_status: accepted
accepted: 2026-09-26
---

# ADR-005 — Token signing key

Corrects **one clause** of ADR-004. That record decided the right thing — the API is the authentication authority and mints its own Supabase-valid JWTs — but named a signing mechanism Supabase has since deprecated and which **a project created today may not have at all**. Nothing else in ADR-004 changes: not the authority, not `auth_session`, not the absence of `auth.users`.

## Context

ADR-004 says the API signs tokens "with the **project's Supabase JWT secret** (HS256)" — the single shared secret historically found in the Supabase dashboard. Verified against Supabase's own documentation on 2026-09-26 (audit M7), three things are now true:

1. **The legacy JWT secret is deprecated.** Supabase's signing-keys guide describes it as *"No longer recommended. Available for backward compatibility."*
2. **New projects do not get it.** Supabase's announcement states: *"Starting October 1, 2025, all new projects will use asymmetric JWTs by default."* **Ostad Lagbo's Supabase project does not exist yet** — it is created in Slice 0, well after that cutoff. So ADR-004 names a key the project will most likely never be issued.
3. **Symmetric signing is discouraged generally.** Even inside the current system, where a shared secret remains a selectable key type, Supabase marks HS256 *"Not recommended for production applications"*, noting that a leaked shared secret lets an attacker impersonate any user *"far into the future."*

What has **not** changed is the pattern itself. Supabase explicitly documents minting your own JWTs against a signing key you control, and those tokens are accepted by the Data API, Storage and Realtime, with RLS evaluating their claims. The architecture is fine; the key type is stale.

## Decision

- **The API signs with an asymmetric signing key we generate and import — ES256.** The key pair is generated with `supabase gen signing-key --algorithm ES256`, the **private key is held only by the API** (Render environment, never shipped to any client), and the public half is imported into the project's **JWT Signing Keys** (Settings → JWT Keys) as a standby key, then rotated to current. Supabase verifies; it never holds the signing half. This is the same trust shape ADR-004 intended, with the secret no longer shared between two parties.
- **The token carries a `kid` header.** Headers are `alg: ES256`, `kid: <the imported key's id>`, `typ: JWT`. The `kid` is how Supabase selects the verification key — ADR-004 omitted it, and without it verification is not reliable where a project holds more than one key.
- **The payload claim contract is `sub`, `role`, `exp`** — `sub` = `user_account.id` (which must remain a **UUID**, since `auth.uid()` casts it), `role` = `"authenticated"` (which must be a **real Postgres role** — application roles never go here), and a short `exp`. `aud: "authenticated"` is retained from ADR-004 as harmless but is not required. Any application-level role or flag belongs in `app_metadata`, read in policies via `auth.jwt()`.
- **The `apikey` header uses a publishable key** (`sb_publishable_…`), never a minted token — Supabase requires the two separately, and the legacy `anon` / `service_role` keys are scheduled for removal in late 2026.
- **Rotation is a supported, zero-downtime operation.** Standby → current → previously-used means a compromised key is replaced without signing anyone out, which is a strict improvement on ADR-004's note that rotation invalidates live access tokens.

## Consequences

- **`sub` is a bare UUID with no row behind it.** Since no `auth.users` record exists (ADR-004), nothing may foreign-key or join to `auth.users`; `user_account` is the only user table, and its `id` must stay a UUID. This was already true — it is stated here because it becomes load-bearing at the RLS layer.
- **The incident playbook changes shape.** Rotating a compromised signing key no longer means "invalidate every live token"; it means promoting a standby key. Playbook 2 is updated accordingly.
- **Self-minted tokens are a second-class path on the platform, and that is a standing risk.** In July 2025 a PostgREST upgrade tightened JWT validation and broke custom-JWT projects until they re-imported their signing key. Supabase Auth users were unaffected. This design should therefore be covered by an integration test that runs against a real Supabase project on every deploy, so a platform-side change surfaces in CI rather than in production.
- **Local/production parity needs checking in Slice 0.** Open Supabase CLI issues suggest configuring ES256 for the local stack is rougher than for the hosted project. If local parity proves impractical, the fallback is an imported **shared-secret** signing key for local development only, never for production.

## Open items

*Tracked live in [OL-OPN-001](/OstadLagbo/governance/open-items.md); this list is context.*


1. **Slice 0, 60 seconds:** on creating the Supabase project, confirm in Settings → JWT Keys whether any legacy JWT secret exists. Documentation does not state this outright for brand-new projects, and it is the one fact that could not be settled from the docs.
2. **Slice 0:** verify the ES256 signing key works end-to-end against **Realtime** (chat, private channels) and **Storage** (signed URLs) — not just the Data API — before Slice 3 depends on it.
3. **Slice 0:** confirm local-versus-hosted signing parity, and record the fallback if it fails.

## Alternatives considered

- **Keep an HS256 shared-secret signing key** (still selectable inside the new system) — rejected. It is the same shared-secret risk under a new name, Supabase marks it not recommended for production, and a project on HS256 publishes no JWKS at all, foreclosing any future integration that expects one. The only argument for it was familiarity.
- **Supabase Third-Party Auth** — **not available to us.** It supports exactly five named providers (Clerk, Firebase, Auth0, AWS Cognito, WorkOS), requires an OIDC discovery endpoint, and explicitly states *"Using symmetrically signed JWTs is not possible."* There is no generic custom-issuer option. Supabase's own documentation describes our technique as a "workaround" and offers this feature only to those vendors' customers.
- **Adopt Supabase Auth after all** — rejected for the reasons ADR-004 already gave (no plaintext password at `register/verify`, and a split credential of record). Nothing in this correction weakens those.
- **Proxy Realtime and Storage through the API** so no Supabase-valid token is needed — rejected: it puts chat delivery and media transfer on the API's critical path, which is exactly what ADR-001 avoided.
