---
project: OstadLagbo
type: data-model
status: current
updated: 2026-09-24
id: OL-DM-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.2.md
owner: Iftikher
---

# Data Model — Overview & Conventions

The index and rulebook for the data-model layer. Every entity in the system is owned by exactly one module and defined in that module's `data-model/` document; other modules reference it by ID and never redefine it. This is a **logical model** — true regardless of backend choice (relational, document, or managed platform); backend selection is a separate architecture decision informed by this layer.

## Conventions

- **Naming:** `snake_case` entities and fields; singular entity names (`user_account`, not `user_accounts`).
- **Identifiers:** every entity has `id` (UUID). Foreign references are `<entity>_id`.
- **Timestamps:** `created_at` on everything; `updated_at` where rows mutate; all UTC.
- **Enums:** closed value sets written in the defining document; adding a value is a change to that document.
- **Visibility:** fields inherit the requirements' visibility classes (public / internal / system); each model document marks any field whose exposure isn't obvious.
- **Bilingual data:** fields carrying both scripts are explicit pairs (`*_en`, `*_bn`); collation and search behavior per CL-013. Outbound notifications render in `user_account.preferred_locale`.
- **Retention encoding (OL-RET-001):** deletion is a designed operation, not a row drop. Standard fields where applicable: `deleted_at` (deactivation moment), `purge_at` (scheduled hard-purge), `anonymized` (flag for persist-anonymized records), `legal_hold` (suspends purging). Every model document ends with a **retention behavior** section mapping its entities to the policy schedule.
- **Instrumentation:** analytics events are not entities here; they are stored in the separate `analytics` schema defined by **ADR-002**, fed by each module's instrumentation requirement. Only *queryable product data* is modeled in this layer.
- **Predicates over flags:** where a rule depends on live state elsewhere (discoverability, visibility, duplicate identity, thread writability, reopen windows, active suspension, consent currency), model documents define it as a **query-time predicate** stated once, not a stored flag that can go stale. Established by OSP-DM (discoverability), SGP-DM (permitted-Ostad visibility), ADM-DM (duplicate-ID check, active suspension), OFR-DM (thread writability), SUP-DM (reopen window), REG-DM (consent currency).
- **Tombstone references:** purged accounts persist as tombstone rows (REG-DM), so foreign references from persisting records (connections, ratings, reports, tickets, consent records) remain valid rather than being nulled. Display uses captured snapshots. **Anonymization lives on the persisting record** (`rating.anonymized`, `connection.anonymized`), never on the purged party's own profile — profiles purge outright.
- **Deliberate denormalization:** copying a value across entities is permitted only where an invariant cannot otherwise be expressed, and must be labeled as such in the defining document. Instances: `connection` party ids (survive offer purge), `rating` party ids (pair uniqueness), `report.reported_account_id` (single-table admin reads).
- **Address chain validity:** the four `admin_area` references stored on a profile (division, district, thana, postal code) must form a valid parent chain in `admin_area`; enforced at write time, never assumed.

## Entity ownership map

| Entity | Owner | Referenced by |
|---|---|---|
| `user_account` | REG | everything |
| `pending_registration` (15-minute pre-account state) | REG | — (the registration flow only) |
| `otp_request` | REG | — |
| `auth_session` (incl. restricted sessions for suspended accounts) | REG | REG (push tokens) |
| `device_push_token` | REG | OFR, ADM (notification and broadcast delivery), SUP |
| `consent_record` | REG | ADM (account detail) |
| `identity_document` (many per account; one current; drafts replaced in place) | REG | ADM (review), OSP (revision resubmission), OL-RET (purge) |
| `onboarding_progress` | REG | ADM (funnel) |
| `ostad_profile` (+ children: `skill_entry`, `education_entry`, `experience_entry`, `portfolio_item`) | OSP | MAP, OFR, RNT, ADM |
| `profile_revision` (pending post-approval key-field changes) | OSP | ADM (review case, diff) |
| `shagred_profile` | SGP | OFR (visibility), ADM |
| `ostad_history_entry` | SGP | — (owner-only) |
| `skill_category` (en + bn alias, active flag; seeded from OL-SKC-001) | ADM | OSP, MAP |
| `admin_area` (Division → District → Thana → postal code; en + bn) | ADM | OSP, SGP |
| `review_case` (review episode record; not the gate) | ADM | OSP (via profile_revision), REG (via identity_document) |
| `admin_account`, `admin_session`, `admin_audit_entry` | ADM | all admin actions |
| `moderation_action` (warn/suspend/reinstate/terminate) | ADM | REG (suspension ref, termination), RNT, OFR, SUP (appeals) |
| `broadcast` | ADM | REG (token resolution) |
| `favorite` | MAP | — |
| `offer` | OFR | SGP (visibility), RNT (eligibility, report eligibility), ADM |
| `connection` | OFR | RNT (rating rights), SGP (history), OSP (insights) |
| `chat_thread`, `chat_message` (text or voice ref) | OFR | ADM (report context), RNT (report targets) |
| `rating` (+ `rating_reply`) | RNT | OSP (aggregate) |
| `report` | RNT | ADM (queue) |
| `block` | RNT | OSP, SGP, MAP, OFR (the canonical predicate) |
| `support_ticket`, `ticket_message` | SUP | ADM (queue) |

## Cross-cutting rules

1. **`user_account` is the identity spine.** Role-specific data lives in `ostad_profile` / `shagred_profile`, one-to-one with the account, never merged into it.
2. **The connection is sacred.** `connection` records are the platform's success unit (ADM-12) and the eligibility anchor for ratings (RNT-01), durable visibility (SGP-05), and Ostad history (SGP-03). They anonymize, never vanish.
3. **Approved vs. pending truth (OSP-10/ADM-06):** the public always reads the last *approved* profile revision; pending edits live separately until verdict. The model, not the UI, enforces this.
4. **No coordinates outside `ostad_profile`.** The schema contains exactly one lat/long pair in the entire system (SGP-02/MAP-10 made structural).
5. **Blocks are checked, not copied:** a single `block` record drives chat freeze, visibility severance, offer refusal, and discovery hiding — modules query it; they don't mirror it. The canonical predicate is defined in RNT-DM.
6. **One canonical owner per status.** `ostad_profile.approval_status` is the publishing gate; `identity_document.verification_status` (on the current row) is the identity state; `user_account.status` is the account state. Workflow records (`review_case`, `moderation_action`) reference these; they never hold a second copy. Per-episode decisions are the audit log's job.
7. **The suspended account has exactly one write path.** A suspended account may create and follow an `appeal` support ticket (SUP-DM), plus the three operations that make an appeal usable — requesting a `ticket_attachment` upload, registering a push token from its restricted session, and changing its language or logging out — and nothing else, including during the 30-day window after termination (REG-DM). Every other model treats `suspended` as read-only for the user, and every direct-access channel (Supabase Realtime and Storage) refuses it at the row-level-security layer (OL-API-001).

## Authorization model

OstadLagbo uses **static role-based access, not data-driven RBAC**, deliberately. There are exactly four actors — guest, Shagred, Ostad, admin — role is permanent at registration (REG-01), and MVP admins hold one fixed full-permission tier (ADM-20). Building role/permission tables for four fixed, non-configurable roles is machinery without a customer; each role's permissions are fixed in application code instead.

**The real access-control complexity in this platform is relationship- and state-based, not role-based**, and is enforced through a **single centralized policy layer** — one module every other module calls into, so no access rule is ever implemented twice or drifts between endpoints. The canonical rules that layer enforces:

| Rule | Source | Structural mechanism |
|---|---|---|
| A Shagred profile is visible to an Ostad only while an offer is pending or a connection exists | SGP-05 | Query joins through live `offer`/`connection` state, never a standing grant |
| A chat thread is readable only by its two participants | OFR-07 | `chat_thread` carries exactly two participant IDs; no third-party read path |
| A block severs chat, visibility, offers, and discovery in both directions | RNT-08 | Every affected query checks `block` before returning data (rule 5, above) |
| A paused Ostad is excluded from discovery and cannot receive new offers, but existing relationships continue | OSP-11 | `ostad_profile.paused_at` checked at discovery and offer-creation time only, not at relationship read time |
| A pending Ostad has full app access but is not discoverable | REG-11 | `ostad_profile.approval_status` gates discovery queries, not authentication |
| Admin reads chat content only when a report cites it, and every read is audit-logged | OFR-07, ADM-17 | No general chat-browse query exists in the admin surface; the only read path originates from a `report` record and writes an audit entry as a side effect |
| Non-key-field profile edits publish instantly; key-field edits require approval before going public | OSP-10 | Public reads never join an open `profile_revision` (rule 3) |
| A suspended account may appeal and do nothing else | SUP-04, ADM-08 | The policy layer permits the appeal operations and their three supporting operations for restricted sessions only (rule 7); RLS refuses suspended accounts on every direct channel |

**Implementation under ADR-001 (two lines of defense):** the policy layer is a module of the **Render API** — every endpoint calls it; no endpoint evaluates access itself. **Supabase row-level security mirrors the same rules at the database**, so a defect in one endpoint still cannot return data the database itself refuses to serve. The API layer is the primary guard and the source of truth for these rules; RLS is the safety net, and the two are kept in sync by treating this table as the specification for both. Because Supabase Realtime and Storage are reached directly by the app, **every RLS policy on a directly accessed table or bucket additionally requires the caller's account status to be `active`** — the API's refusal of suspended accounts cannot be bypassed through those channels (OL-API-001).

**Post-MVP evolution:** when the founder adds team members and admin role tiers become necessary (already marked post-MVP in ADM-20), that is the point data-driven RBAC is introduced — scoped to the admin panel, where multiple tiers actually exist to justify it. The relationship/state policy layer for end-user access is not expected to need this evolution, since its complexity is inherent to the product, not to organizational growth.

## What the backend architecture decision must satisfy

Collected from the module models, for the architecture decision record: **(a)** a spatial index with bounding-box and radius queries over ~1,000–10,000 points, with server-side cluster aggregation above a cap (MAP-DM); **(b)** fuzzy text matching across Latin and Bangla scripts with per-script normalization (MAP-DM, OSP-DM); **(c)** append-only storage for the audit log, enforced below the application layer (ADM-DM, NFR-05); **(d)** request-log scrubbing of coordinate parameters at the infrastructure layer (MAP-DM, NFR-06); **(e)** partial unique indexes (offers, reports, appeals, blocks) and check constraints (message authorship) — or equivalent guarantees; **(f)** scheduled jobs for offer expiry, day-5 reminders, inactivity auto-resolution, and retention purges on both deletion paths; **(g)** transactional multi-write for offer acceptance (five writes, one commit) and for termination (moderation action + account fields + session/token revocation + offer resolution); **(h)** push delivery to platform tokens with per-recipient locale rendering. A backend that provides these natively is strongly preferred over one requiring auxiliary services at MVP scale (NFR-13). **Resolved by ADR-001** (accepted 2026-09-13): (a), (b), (e), (g) in Supabase PostgreSQL; (c) database permissions; (d) Cloudflare + Render log configuration; (f) pg_cron with the API handling external calls; (h) the API via Firebase Cloud Messaging. **Analytics storage resolved by ADR-002** (accepted 2026-09-24).

## Document sequence

REG ✅ → OSP ✅ → SGP ✅ → ADM ✅ → MAP ✅ → OFR ✅ → RNT ✅ → SUP ✅ — **layer complete 2026-09-13**, then revised the same day by a **cross-layer review** that found five significant seams between models (banned-account termination had no mechanism; profile anonymization was a phantom; push tokens, locale, and the reminder flag were unmodeled; identity-document cardinality was undefined; consent records had no retention rule) and fixed them across REG, SGP, OFR, ADM, this overview, and OL-RET-001. Revised again 2026-09-24 when the REG api review surfaced `pending_registration`, restricted sessions, draft identity-row replacement, and the suspended-account push and upload operations. Each at `modules/<module>/data-model/`, deriving from its requirements document.
