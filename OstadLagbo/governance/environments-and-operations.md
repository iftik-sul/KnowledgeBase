---
project: OstadLagbo
type: operations
status: current
updated: 2026-09-26
id: OL-OPS-001
derived_from: /OstadLagbo/decisions/adr-001-platform-architecture.md
owner: Iftikher
---

# Environments, Deployment and Recovery

How code and data move from a laptop to real users, and how they come back if something is lost. NFR-07 requires backups with a 24-hour RPO/RTO and *"a full restore rehearsed in staging before soft launch"*; NFR-05 and NFR-14 require CI with dependency scanning and tests; the Slice 4 gate requires the retention purge *"verified in staging"*. All of that named a staging environment and a CI pipeline that no document defined. This defines them.

## Environments

Two, not three. A solo builder maintaining a third environment spends more than it returns.

| | **Development** | **Staging** | **Production** |
|---|---|---|---|
| Runs on | The builder's machine + a local Supabase | Its **own** Supabase project + Render service | Its own Supabase project + Render service |
| Data | Seed fixtures only | **Synthetic only — never a production copy** | Real |
| Supabase plan | Local / free | Free (accepts auto-pause) | Pro (ADR-001) |
| Who reaches it | The builder | The builder, and reviewers if needed | Everyone |
| Identity documents | Fake images | Fake images | Real — the vault |

**Staging never holds real personal data.** Copying production down to staging is the ordinary way identity documents leak, and under the PDPA those documents are the most consequential thing the platform holds (R-02, CL-025). If a production bug can only be reproduced with real data, it is reproduced **in production, read-only, under audit** — never by copying the vault sideways. Seed staging with generated fixtures instead.

**Separate Supabase projects, not separate schemas.** A shared project means one bad migration or one mistaken `service_role` call reaches real data. Separate projects also mean **separate JWT signing keys** (ADR-005), so a staging key can never mint a token production would accept.

## Secrets

Secrets live in Render's and Supabase's environment configuration, never in the repository (NFR-05). Each environment has its own copy of: the Supabase URL and keys (publishable + secret, per ADR-005), the API's **JWT signing private key**, the Alpha SMS credentials, the Resend key, the FCM service account, and the map tile key (CL-035). A leaked staging secret must be worthless in production, which is only true if none are shared.

Development uses the **OTP stub that logs the code** (ADR-003) and sends no real SMS; only production spends credit. Staging may use the stub too — an OTP that costs money is not a thing to test with.

## CI — on every push

Required by NFR-05 (dependency scanning), NFR-11 and NFR-14 (tests, linting):

1. Lint and format check — API, app, dashboard
2. Type check
3. **Unit and integration tests**, including the ADR-005 signing-key test that runs against a real Supabase project, so a platform-side change to JWT handling fails here rather than in production
4. **Dependency vulnerability scan** (NFR-05) — a failing scan blocks the merge
5. Build both the API and a release-mode app binary

Nothing merges to `main` with CI red. The specification repository (this one) and the code repository are separate (ADR-003); CI runs on the code repository.

## Deployment and migrations

**API and dashboard** deploy from `main`: Render builds and health-checks the API before switching traffic; Vercel deploys the dashboard and website. Both roll back to the previous deployment from their dashboards — that is the rollback plan, and it is one click.

**Database migrations are the part that does not roll back cleanly**, so they follow one rule: **migrations must be backwards-compatible with the currently deployed API.** Add a column before the code that writes it; stop writing a column before dropping it. A migration and the code that needs it therefore ship as two deploys, not one. This is what allows the API rollback above to be safe — rolling back code onto a migrated database must not break.

Order for every release: migration → verify in staging → migration to production → deploy API → deploy app/dashboard. Migrations run through Supabase's migration tooling and are committed to the repository; no schema change is ever made by hand in a dashboard, because a hand change exists in no environment but that one.

**Mobile releases do not roll back** — a published build cannot be recalled, only superseded. This is why the app must tolerate an older version talking to a newer API: API changes are additive, and a removed field is deprecated for at least one app release first.

## Backups and recovery

### Database — Supabase

Daily automated backups on the Pro plan, **retained 90 days at most** so purged data ages out (NFR-07, OL-RET-001). Point-in-time recovery where the plan offers it.

### Storage — the gap this document closes

**Supabase's database backups do not cover Storage.** The identity vault, portfolio images, the intro video and chat voice notes live in object storage, and nothing in the specification backed them up. Losing them means: every Ostad re-uploads their NID and selfie and is re-reviewed, every portfolio is gone, and every voice note in every chat is gone — an unrecoverable trust failure, not an inconvenience.

**Required: a daily job copies new and changed Storage objects to a second location** in a different provider or region, with its own credentials, retained on the same 90-day schedule. The copy is encrypted at rest (NFR-05) and is subject to the same purge and legal-hold rules as the original (OL-RET-001, CL-041) — **a backup that outlives a purge defeats the purge**, and the retention tooling must reach the backup copy too.

Buckets differ in how much they matter, and the plan should say so rather than treat them alike:

| Bucket | If lost | Backup |
|---|---|---|
| **Identity vault** (NID/passport, selfie) | Every Ostad re-verifies; review queue floods | **Daily, encrypted, highest priority** |
| Portfolio images and intro video | Profiles degrade; Ostads must re-upload | Daily |
| **Chat voice notes** | Irreplaceable — the sender cannot re-record a past message | Daily |
| Ticket attachments | Support context lost; evidence in disputes | Daily |

### Restore rehearsal

NFR-07 requires a full restore rehearsed in staging **before soft launch** and quarterly after. The rehearsal must restore **both** halves — database *and* Storage — and confirm they agree: a restored `identity_document` row pointing at an object that no longer exists is a failed restore that a database-only rehearsal would score as a pass. Record the date, the measured RTO, and anything that went wrong.

## Monitoring

NFR-09 requires crash reporting, error tracking with alerting, uptime monitoring and structured PII-free logs, so the founder can answer *"is the app up and are users failing at anything"* in five minutes from a phone. The tools are an engineering choice; the **obligations** are not:

- Alerts reach a phone, not an inbox that is read in the morning.
- Crash reporting scrubs PII before upload (NFR-06) — crash payloads are a common accidental leak of exactly the data the vault protects.
- Uptime monitoring hits `GET /v1/health` (REG api) from outside the platform's own infrastructure.
- Billing alerts on every paid provider (NFR-13), since the cost posture depends on noticing before the bill arrives.

## Open items

*Tracked live in [OL-OPN-001](/OstadLagbo/governance/open-items.md); this list is context.*


1. **Slice 0:** choose and wire the monitoring and crash-reporting tools; NFR-09 names obligations and no products.
2. **Slice 0:** decide where the Storage backup copy lives, and confirm its cost fits the posture (NFR-13). It is currently unbudgeted.
3. **Slice 4:** first full restore rehearsal — database *and* Storage — before soft launch, per NFR-07.
