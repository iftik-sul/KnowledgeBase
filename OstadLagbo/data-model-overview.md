---
project: OstadLagbo
type: data-model
status: current
updated: 2026-08-30
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
| `profile_revision` (approved vs pending versions) | OSP | ADM (diff, re-review) |
| `shagred_profile` | SGP | OFR (visibility), ADM |
| `ostad_history_entry` | SGP | — (owner-only) |
| `skill_category` (en + bn alias, active flag) | ADM | OSP, MAP |
| `review_case` (queue item + verdicts) | ADM | REG (status), OSP |
| `admin_account`, `admin_audit_entry` | ADM | all admin actions |
| `moderation_action` (warn/suspend/reinstate) | ADM | RNT, OFR |
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

## Document sequence

REG → OSP → SGP → ADM → MAP → OFR → RNT → SUP, each at `modules/<module>/data-model/`, deriving from its requirements document.
