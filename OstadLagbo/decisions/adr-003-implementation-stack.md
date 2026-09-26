---
project: OstadLagbo
type: decision
status: current
updated: 2026-09-26
id: OL-DEC-003
supersedes: none
owner: Iftikher
decision_status: accepted
accepted: 2026-09-25
---

# ADR-003 — Implementation stack and repository

Closes the Slice 0 open item ADR-001 left as "API framework and RLS baseline," and records the codebase layout. ADR-001 fixed the *hosting and services* (Supabase, Render, Vercel, Cloudflare, FCM, an SMS gateway, OSM tiles); this record fixes the *languages and frameworks* built on them, so Execution begins from one decision rather than many implicit ones.

## Context

A solo founder with no coding background, building through an AI agent, needs a stack that is (a) coherent — as few languages as possible, so one mental model spans most of it; (b) structured — an opinionated shape an AI and a future maintainer can navigate without tribal knowledge (risk R-05, transferability); (c) free through development and cheap to run (ADR-001 cost posture, NFR-13); and (d) a natural fit for the API Overview's centralized policy layer and the data models' row-level-security mirror.

## Decision

- **Language:** **TypeScript** everywhere except the app. One language spans the API, the admin dashboard, the public website, and all shared types, so a change to a shape is made once.
- **Database:** **Supabase (PostgreSQL)** — schema and row-level security as **SQL migrations** checked into the repo (the single source of truth for the database), applied to Supabase. PostGIS for the map spatial index and pg_trgm for the cross-script fuzzy match (MAP-DM). pg_cron for the scheduled jobs (offer expiry, reminders, retention purges).
- **API (Render):** **NestJS** (Node + TypeScript). Its module/provider structure gives the centralized policy layer a natural home (a guard/policy module every route passes through, per the API Overview) and keeps the surface legible as it grows. Zod (or class-validator) for request validation against the closed error enum.
- **Admin dashboard + public website (Vercel):** **Next.js** (React + TypeScript), English-only dashboard and bilingual public site; server components for the static/edge-rendered legal and marketing pages (public-website ui).
- **App:** **Flutter (Dart)** for Android and iOS, bilingual from the first commit (CL-016) — the one non-TypeScript surface, fixed by ADR-001.
- **Shared:** a `packages/shared` workspace of TypeScript types and the error-code enum, generated from / kept in step with the data models and API Overview, imported by the API, admin, and web so they cannot drift.
- **Repository:** a **single monorepo, `iftik-sul/athena`**, holding all surfaces plus the migrations, with a root `CLAUDE.md` that names this KnowledgeBase (`iftik-sul/KnowledgeBase`, `OstadLagbo/`) as the authoritative specification the code is built from. The KB stays separate — spec and implementation do not mix.

## Layout

```
athena/
  db/            SQL migrations + seed (Supabase); the schema source of truth
  api/           NestJS service (Render) — the single write path, policy layer, all /v1 endpoints
  admin/         Next.js admin dashboard (Vercel, English-only)
  web/           Next.js public marketing + legal site (Vercel, bilingual)
  app/           Flutter mobile app (Android + iOS, bilingual)
  packages/
    shared/      shared TS types + the closed error-code enum
  CLAUDE.md      build guide; points at the KnowledgeBase as the spec
```

## Consequences

- One language (TypeScript) across three of the five surfaces; Dart only in the app; SQL for the schema. A small stack for a solo build.
- NestJS is heavier than a micro-framework, but its structure is the point: the policy layer, guards, and module boundaries map directly onto the API Overview, and the shape stays navigable at MVP size and beyond.
- All free-tier through development (ADR-001); paid tiers switch on at Slice 1.
- **Still open (unchanged by this record):** the SMS/OTP gateway is not yet selected — OTP delivery uses a development stub (logged codes) until it is, a Slice 0 open item; and ADR-001's PDPA data-residency ruling must close before Slice 1 captures a real identity document.

## Amendments

The decision body above is preserved as accepted. Later records revised parts of the context it cites (an accepted ADR is immutable, so this is recorded here rather than edited above):

- **Map tiles (2026-09-26, CL-035).** The Context section describes ADR-001 as having fixed "OSM tiles" among the hosting and services. That remains an accurate account of what ADR-001 said, but the decision itself has since been amended: OpenStreetMap's public tiles are **development-only**, the shipping basemap must be **raster** (MapLibre cannot shape Bengali), and the provider is selected at a Slice 0 bake-off. Nothing in this ADR's own decision — the languages, frameworks, or codebase layout — is affected, except that the Flutter map package is no longer settled: `flutter_map` holds unless the bake-off selects Google's mobile SDK, which replaces it.

## Alternatives considered

- **Fastify/Hono for the API** — lighter and faster to start, but the policy layer and growing surface benefit from NestJS's imposed structure in a build with no human engineering team to hold conventions.
- **A second backend language (e.g., Python/Go)** — rejected: it would split the stack for no gain here and break the shared-types workspace.
- **Separate repos per surface** — rejected for a solo build: more overhead to keep aligned than isolation is worth (revisit if a team forms).
