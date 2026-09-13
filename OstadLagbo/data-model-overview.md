---
project: OstadLagbo
type: data-model
status: current
updated: 2026-09-13
id: OL-DM-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.1.md
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
- **Bilingual data:** fields carrying both scripts are explicit pairs (`*_en`, `*_bn`); collation and search behavior per CL-013.
- **Retention encoding (OL-RET-001):** deletion is a designed operation, not a row drop. Standard fields where applicable: `deleted_at` (deactivation moment), `purge_at` (scheduled hard-purge), `anonymized` (flag for persist-anonymized records), `legal_hold` (suspends purging). Every model document ends with a **retention behavior** section mapping its entities to the policy schedule.
- **Instrumentation:** analytics events are not entities here; they flow to the analytics store per each module's instrumentation requirement. Only *queryable product data* is modeled.
- **Predicates over flags:** where a rule depends on live state elsewhere (discoverability, visibility, duplicate identity), model documents define it as a **query-time predicate** stated once, not a stored flag that can go stale. Established by OSP-DM (discoverability), SGP-DM (permitted-Ostad visibility), ADM-DM (duplicate-ID check).

## Entity ownership map

| Entity | Owner | Referenced by |
|---|---|---|
| `user_account` | REG | everything |
| `otp_request` | REG | — |
| `auth_session` | REG | — |
| `consent_record` | REG | ADM (account detail) |
| `identity_document` | REG | ADM (review), OL-RET (purge) |
| `onboarding_progress` | REG | ADM (funnel) |
| `ostad_profile` (+ children: `skill_entry`, `education_entry`, `experience_entry`, `portfolio_item`) | OSP | MAP, OFR, RNT, ADM |
| `profile_revision` (pending post-approval key-field changes) | OSP | ADM (review case, diff) |
| `shagred_profile` | SGP | OFR (visibility), ADM |
| `ostad_history_entry` | SGP | — (owner-only) |
| `skill_category` (en + bn alias, active flag) | ADM | OSP, MAP |
| `admin_area` (Division → District → Thana → postal code; en + bn) | ADM | OSP, SGP |
| `review_case` (review episode record; not the gate) | ADM | OSP (via profile_revision), REG (via identity_document) |
| `admin_account`, `admin_session`, `admin_audit_entry` | ADM | all admin actions |
| `moderation_action` (warn/suspend/reinstate) | ADM | REG (suspension ref), RNT, OFR |
| `broadcast` | ADM | — |
| `favorite` | MAP | — |
| `offer` | OFR | SGP (visibility), RNT (eligibility), ADM |
| `connection` | OFR | RNT (rating rights), SGP (history), OSP (insights) |
| `chat_thread`, `chat_message` (text or voice ref) | OFR | ADM (report context) |
| `rating` (+ `rating_reply`) | RNT | OSP (aggregate) |
| `report` | RNT | ADM (queue) |
| `block` | RNT | OFR, MAP, SGP (effects) |
| `support_ticket`, `ticket_message` | SUP | ADM (queue) |

## Cross-cutting rules

1. **`user_account` is the identity spine.** Role-specific data lives in `ostad_profile` / `shagred_profile`, one-to-one with the account, never merged into it.
2. **The connection is sacred.** `connection` records are the platform's success unit (ADM-12) and the eligibility anchor for ratings (RNT-01), durable visibility (SGP-05), and Ostad history (SGP-03). They anonymize, never vanish.
3. **Approved vs. pending truth (OSP-10/ADM-06):** the public always reads the last *approved* profile revision; pending edits live separately until verdict. The model, not the UI, enforces this.
4. **No coordinates outside `ostad_profile`.** The schema contains exactly one lat/long pair in the entire system (SGP-02/MAP-10 made structural).
5. **Blocks are checked, not copied:** a single `block` record drives chat freeze, visibility severance, offer refusal, and discovery hiding — modules query it; they don't mirror it.
6. **One canonical owner per status.** `ostad_profile.approval_status` is the publishing gate; `identity_document.verification_status` is the identity state; `user_account.status` is the account state. Workflow records (`review_case`, `moderation_action`) reference these; they never hold a second copy. Per-episode decisions are the audit log's job.

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

**Post-MVP evolution:** when the founder adds team members and admin role tiers become necessary (already marked post-MVP in ADM-20), that is the point data-driven RBAC is introduced — scoped to the admin panel, where multiple tiers actually exist to justify it. The relationship/state policy layer for end-user access is not expected to need this evolution, since its complexity is inherent to the product, not to organizational growth.

## Document sequence

REG ✅ → OSP ✅ → SGP ✅ → ADM ✅ → MAP → OFR → RNT → SUP, each at `modules/<module>/data-model/`, deriving from its requirements document.
