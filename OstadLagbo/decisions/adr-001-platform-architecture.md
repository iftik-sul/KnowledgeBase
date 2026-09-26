---
project: OstadLagbo
type: decision
status: current
updated: 2026-09-26
id: OL-DEC-001
derived_from: /OstadLagbo/data-model-overview.md
owner: Iftikher
decision_status: accepted
accepted: 2026-09-13
---

# ADR-001 — Platform Architecture: Data, Backend, and Frontend Hosting

## Status

**Accepted** — founder approval 2026-09-13. This decision is revisited only by a superseding ADR, never edited in place.

## Context

The MVP needs a place for its data, its backend logic, its mobile app, and its web surfaces (the admin panel and a public website). The choice is being made now — after the data-model layer — so it is judged against what the platform actually demands. Constraints that bind it:

- **What the data models demand** (Data Model Overview, "What the backend must satisfy"): (a) spatial indexing for the map; (b) fuzzy text matching across Latin and Bangla; (c) append-only audit storage; (d) request-log scrubbing of coordinates; (e) partial unique indexes and check constraints; (f) scheduled jobs; (g) multi-write transactions; (h) push delivery with per-recipient locale.
- **What the NFRs demand:** 1,000 Ostads / 20,000 Shagreds / 500 concurrent (NFR-08); 99.5 % availability; cold start ≤ 3 s and first map pins ≤ 2 s on 4G (NFR-02); encryption at rest (NFR-05); backups ≤ 90 days (NFR-07); PII-free logs (NFR-06); **free or free-tier-viable at MVP scale** (NFR-13).
- **Who is building:** a solo founder with an AI development agent. Product time must not become operations time (R-05, R-06). Code the agent writes must be conventional, testable, and portable.
- **The founder's constraint:** **the development phase must cost $0.** Costs may switch on only when real users arrive.
- **Where the users are:** Bangladesh. No provider offers a Bangladesh region; the PDPA 2026's data-residency rules are pending legal review.

## Options considered

| | A · Supabase only | **B · Three-tier (chosen)** | C · AWS assembled |
|---|---|---|---|
| Shape | Database, auth, storage, and all logic inside one platform | Supabase for data services · a conventional API server on Render · web surfaces on Vercel | RDS + Lambda + Cognito + S3, self-assembled |
| Dev-phase cost | $0 | **$0** | $0 for 12 months, then not |
| Production cost | $25 + SMS | ≈ $52 + SMS | $30–100+, unpredictable |
| Ops burden (solo) | Lowest | Low | High |
| Code conventionality / AI-agent fit | Weaker (DB functions, Deno) | **Strongest** (normal server codebase) | Strong |
| Testability & portability | Weaker | **Strongest** | Strong |
| Latency to Dhaka | Best (Mumbai) | Good (Singapore, +1 hop) | Best (Mumbai) |
| Misconfiguration risk | Low | Low | Highest |
| Lock-in | Deeper | Lightest | Moderate |

Option A was the initial draft. Option B was adopted because the builder is an AI agent whose output quality is highest in a conventional server codebase, and because business logic in a normal API is testable and portable in a way database-resident logic is not. Option C remains the scale-out destination — both A and B use standard PostgreSQL, so reaching C later is a database export, not a rewrite.

## Decision

**Adopt Option B — a three-tier architecture:**

| Tier | Platform | What lives there |
|---|---|---|
| **Data services** | **Supabase**, region **Singapore** (ap-southeast-1) | PostgreSQL database (with PostGIS and trigram extensions); **Auth** (phone OTP, sessions, password hashing); **Storage** (encrypted buckets, signed URLs — the identity vault, portfolio media, voice notes); **Realtime** (chat message delivery); **pg_cron** (offer expiry, day-5 reminders, inactivity auto-resolution, retention purges) |
| **Backend API** | **Render**, region **Singapore** | The business logic and the **centralized policy layer** (Overview → authorization model): offer acceptance transaction, verdict effects, termination, report handling, push dispatch, SMS dispatch, analytics emission, all access rules. A single conventional web service; framework is an engineering default (TypeScript/Node recommended for ecosystem breadth and Supabase client maturity) |
| **Web frontend** | **Vercel** | The **admin dashboard** (ADM, TOTP-secured, English-only) and the **public website** (landing/marketing pages, legal documents for guests per MAP-03/REG-13) |
| **Mobile app** | Google Play + Apple App Store | The Flutter app; talks to the Render API (and to Supabase Realtime and Storage directly for chat delivery and media) |
| **Push** | Firebase Cloud Messaging | Delivery only; tokens and payloads, no other user data |
| **OTP SMS** | A Bangladesh SMS gateway | Selected in Slice 0; the largest variable cost |
| **Map tiles** | OpenStreetMap-based via `flutter_map` | No per-load billing |
| **Edge / DNS** | Cloudflare (free) in front of the Render API | Provides infrastructure-level request-log control and rate limiting for requirement (d) and NFR-05 |

**Why Supabase is not "database only":** Auth, Storage, and Realtime are included in the plan and are hard to build safely — hand-rolled login is how identity data gets breached (NFR-05). The API owns *logic*; Supabase owns *data services*. Row-level security is retained as a **second line of defense** behind the API's policy layer, so a bug in one endpoint still cannot expose data the database itself refuses to serve.

**Why Singapore for both:** Render has no Mumbai region; keeping the API and the database in the same region avoids a cross-region round trip on every query. A Dhaka latency test in Slice 0 confirms this meets NFR-02.

**Where the eight requirements land:** (a), (b), (e), (g) in PostgreSQL natively; (c) database-level permissions denying update/delete on the audit table, enforced below the API; (d) Cloudflare log configuration plus API middleware; (f) pg_cron for database-side jobs, with the API handling any step that calls an external service (push, SMS); (h) the API calls FCM with the recipient's `preferred_locale`.

## Phased cost model

The founder's constraint is honored: **development costs nothing.** The meter turns on at the Slice 1 gate of the build sequence — the moment the first real Ostad is recruited — because free-tier behaviors that are harmless in development (auto-pause, cold starts) are unacceptable for a real person.

| Line | Development (Slices 0–3, internal) | From the first real user (Slice 1 seeding onward) |
|---|---|---|
| Supabase | Free plan: 500 MB DB, 1 GB storage, 50K MAU; pauses after 7 idle days (one click resumes) | **Pro $25/mo** — 8 GB DB, 100 GB storage, spend cap on by default; required because auto-pause would take the app offline |
| Render API | Free web service; spins down after 15 min idle, ~1 min wake | **Starter $7/mo** — always on; required because a 1-minute cold start fails NFR-02 |
| Vercel (website + admin) | Hobby plan, free | **Pro $20/mo** — the Hobby plan is licensed for non-commercial use only; Ostad Lagbo is commercial. *(Founder-selected; Cloudflare Pages remains the free alternative if this line is ever unwelcome.)* |
| Firebase Cloud Messaging | Free | Free at any volume |
| OTP SMS | **$0** — Supabase Auth test phone numbers with fixed OTP codes; no real SMS sent | Per-SMS BDT rate × (signups + resets + phone changes); monitored by ADM-19 |
| Map tiles | Free | Free (paid tile CDN only at scale) |
| Cloudflare edge | Free | Free |
| Apple Developer account | Not needed for simulator; **$99/yr before any physical-iPhone or TestFlight testing** | $99/yr |
| Google Play | Not needed until submission | $25 one-time |
| **Total** | **$0/month** | **≈ $52/month + SMS** (+ store accounts) |

## Consequences

**Positive:** the data models implement without translation — their constraints, predicates, and transactions are relational, and PostgreSQL is relational. The API is a normal codebase the AI agent builds and tests conventionally, portable to any host. Backups, encryption at rest, and availability of the data tier are Supabase's job; API uptime is Render's. The whole stack is four consoles (Supabase, Render, Vercel, Firebase) plus the SMS gateway.

**Costs and obligations:**
- Two backends to monitor (NFR-09's observability applies to both).
- One extra network hop per request; acceptable within NFR-02, to be confirmed by the Slice 0 latency test.
- The policy layer must be enforced in the API with discipline; RLS is the safety net, not the primary guard.
- **Data residency is unresolved and is this ADR's one hard dependency on legal review:** identity documents will be stored in Singapore. If the PDPA requires an in-country copy for restricted-category data, the mitigation is an encrypted backup replica to Bangladesh-hosted storage — an addition, not a platform change.
- Vendor dependency is bounded: standard PostgreSQL, a portable API, static frontends. Nothing here is a rewrite to leave.
- The public website is a new deliverable not present in the MVP baseline's module scope; this ADR records where it deploys, and its content (marketing pages, guest-reachable legal documents) is planned with the ui layer.

## Open items created by this decision

1. **Legal:** PDPA data-residency ruling on identity documents stored in Singapore — before Slice 1 collects the first NID.
2. **Engineering (Slice 0):** Dhaka latency test against Singapore for the phone → Render → Supabase path; confirm NFR-02.
3. **Procurement (Slice 0):** select the Bangladesh SMS gateway; record per-SMS cost; feed ADM-19 and the budget document.
4. **Engineering (Slice 0):** verify trigram fuzzy matching against Bangla test strings with OSP-04/MAP-06's normalization rules.
5. **Engineering (Slice 0):** confirm coordinate scrubbing at the Cloudflare and Render log layers for MAP-DM's query parameters.
6. **Engineering (Slice 0):** choose the API framework (engineering default) and establish the Supabase RLS baseline as the second-line guard.
7. **Budget:** Apple Developer account timing — before the first physical-iPhone test.
8. **Budget:** confirm the Vercel Pro line at launch or switch the web tier to Cloudflare Pages.

## Amendments

The decision body above is preserved as accepted on 2026-09-13. Two later ADRs revised parts of it (an accepted ADR is immutable, so these are recorded here rather than edited into the tables above):

- **Auth (2026-09-25, ADR-004).** The "Auth (phone OTP, sessions, password hashing)" line in the Data-services row, and the "hand-rolled login is how identity data gets breached" note, are superseded in part: the **API** is the authentication authority — it owns `user_account.password_hash` (scrypt) and mints Supabase-valid JWTs (signed with an imported ES256 signing key — ADR-005 corrected ADR-004's reference to the now-deprecated legacy shared secret); **no `auth.users` row is created**. Supabase Auth is not the password store or token issuer. Supabase still verifies those tokens' signatures on its direct channels (Realtime, Storage), and RLS remains the second line of defense — so ADR-001's security rationale (don't expose identity data; keep RLS behind the policy layer) stands. The warning against "hand-rolled login" is satisfied by using the platform's built-in scrypt and Supabase-valid JWTs, not a bespoke scheme.
- **OTP in development (2026-09-25, ADR-003).** The cost-model line "Supabase Auth test phone numbers with fixed OTP codes" no longer applies (Supabase Auth is not used). In development, OTP uses a **stub that logs the code**; no real SMS is sent until the Slice 0 gateway is selected. The $0-in-development outcome is unchanged.

- **Map tiles (2026-09-26, CL-035).** The service-map row "Map tiles | OpenStreetMap-based via `flutter_map` | No per-load billing" and the cost-model row "Map tiles | Free | Free (paid tile CDN only at scale)" are **corrected, not merely refined — both were factually wrong**. OpenStreetMap's tile usage policy forbids commercial products on its community-funded servers, forbids prefetching, and states that "offline use is not permitted"; OSM public tiles are therefore **development-only** and are never shipped. Separately, every *vector* basemap on mobile renders through MapLibre, which **cannot shape Bengali script** — ruling out the free vector options for a Bangla-first product. The shipping provider is a **raster** vendor (≈ $20–30/month, free tiers being non-commercial) **or** Google's own mobile SDK ($0, but it replaces `flutter_map`). The provider is selected in **Slice 0, before any MAP screen is built**; the development-phase outcome ($0) is unchanged, but the "from the first real user" total rises from ≈ $52/month to ≈ $72–82/month + SMS unless Google is chosen.

- **SMS gateway and email provider selected (2026-09-26, CL-036).** Closes open item 3. **OTP SMS: Alpha SMS** (`sms.net.bd`) — ৳0.64/SMS masked, ৳0.40 non-masked, ৳1,500 minimum top-up, English REST API, and **payable in BDT via bKash/Nagad**, which no international provider allows. International CPaaS (Twilio, Plivo, Vonage) was rejected: ৳34–56/SMS is 60–90× the local rate, and since **8 September 2025** Grameenphone, Robi and Teletalk **block unregistered sender IDs** anyway, so it buys neither cost nor speed. Firebase Phone Auth is doubly unavailable — $0.20/SMS for Bangladesh, and the platform does not use Supabase Auth (ADR-004). **Email: Resend** free tier (3,000/month) — email is only ever used to carry a verification code (REG-04), so volume is negligible; its **100/day cap** is an engineering obligation to monitor, because exceeding it fails verification silently. The cost-model row "OTP SMS | Per-SMS BDT rate" now has its rate: at a soft-launch estimate of ~2,000 signups/month, ≈ ৳1,280/month (~$11) masked.

## Superseded by

In part by **ADR-004** (authentication authority — the Auth line) and **ADR-003** (implementation stack — the development-OTP line). The architecture (three tiers, Singapore, RLS-as-second-line, the cost model) otherwise stands.
