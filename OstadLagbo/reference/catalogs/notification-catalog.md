---
project: OstadLagbo
type: catalog
status: current
updated: 2026-09-26
id: OL-CAT-NTF-001
derived_from: /OstadLagbo/modules/contact-and-offers/requirements/contact-and-offers-requirements.md
owner: Iftikher
---

# Notification Catalog

Every notification the platform sends, in one place — collected from OFR-03, ADM-03/16, SUP-03 and REG-11, which specified them one screen at a time. Two gaps surfaced in the collecting; they are flagged below rather than quietly filled.

## Rules that govern every notification

1. **Locale.** Rendered in the recipient's `user_account.preferred_locale` (REG-14) — which is why locale is stored on the account rather than held on the device.
2. **Every push has an in-app counterpart** (OFR-03). A user who denies notifications must never permanently miss anything; they simply learn it later, from the inbox, badge, or status screen.
3. **No per-category preferences** (CL-015). Users control notifications at the OS level only. There is no in-app notification settings screen, and none may be added without a change request.
4. **Delivery** goes to every non-revoked `device_push_token` of the account (REG-DM). Suspended accounts receive **only** appeal-ticket notifications; pending-deletion accounts hold no tokens and receive nothing.
5. **Silence is sometimes the specification.** A blocked user is never notified (RNT-08); a favourited Ostad is never notified (MAP-08). These are privacy guarantees, not omissions.
6. **The SMS channel is separate and regulated.** OTP SMS is not a notification in this sense: it is always Bangla per BTRC (REG-02, CL-036) and does **not** follow `preferred_locale`.

## Push notifications

### To an Ostad

| # | Notification | Trigger | In-app counterpart | Source |
|---|---|---|---|---|
| N-01 | **Offer received** | A Shagred sends an offer | Received-offers inbox, badge | OFR-03 |
| N-02 | **Offer expiring** | Day 5 of a 7-day pending offer | Pending offer shows days remaining | OFR-03 |
| N-03 | **New message** | Counterpart sends text or voice | Chat badge | OFR-03 |
| N-04 | **Verification approved** | Admin approves | Review-status screen, verified badge | ADM-03, REG-11 |
| N-05 | **Changes requested** | Admin requests changes (note mandatory) | Review-status screen with the note | ADM-03, REG-11 |
| N-06 | **Application rejected** | Admin rejects (reason mandatory) | Review-status screen with the reason | ADM-03, REG-11 |
| N-07 | **Support reply** | Admin replies to a ticket | Ticket thread | SUP-03, ADM-22 |
| N-08 | **Broadcast** | Admin sends to a segment | — (transient by design) | ADM-16 |

### To a Shagred

| # | Notification | Trigger | In-app counterpart | Source |
|---|---|---|---|---|
| N-09 | **Offer accepted** | Ostad takes the offer — contact revealed, chat opens | Sent-offers inbox, new chat | OFR-03, OFR-04 |
| N-10 | **Offer declined** | Ostad declines | Sent-offers inbox | OFR-03 |
| N-11 | **New message** | Counterpart sends text or voice | Chat badge | OFR-03 |
| N-12 | **Support reply** | Admin replies to a ticket | Ticket thread | SUP-03 |
| N-13 | **Broadcast** | Admin sends to a segment | — | ADM-16 |

### Suppression

- **New-message pushes are suppressed while that chat is open on-screen** (OFR-03) — the only suppression rule in the MVP.
- A **frozen** thread (block, suspension, deletion) emits nothing further; the freeze is shown as a neutral client banner, never as a message (CL-030).

## In-app only — no push

| Surface | Why no push |
|---|---|
| Consent re-acceptance notice (REG-13) | Shown on next open; a legal notice does not need to interrupt |
| Suspension notice (ADM-08) | **Tokens are revoked by the suspension itself**, so no push is deliverable — see gap G-B below |
| Offer withdrawn by the Shagred | The Ostad simply stops seeing it; no action is owed |
| Favourite added (MAP-08) | Privacy guarantee — the Ostad must never learn who favourited them |
| Block created or reversed (RNT-08) | Privacy guarantee — opacity is the point |

## Gaps found while compiling this catalog

**G-A — an Ostad is not told when they receive a review.** RNT-04 grants the Ostad exactly one public reply per review, and ratings are visible on a profile that drives their livelihood. Nothing in the specification tells them a review exists. As written, an Ostad discovers a one-star review by chance, and the reply right they hold is unusable in practice. *Recommended: add a push + in-app indicator on a new review. This is a scope change (v1.3), not a wording fix, so it needs founder approval and a CL entry — it is deliberately not applied here.*

**G-B — suspension revokes push tokens before it could notify.** The `suspend` action revokes sessions **and push tokens** in the same transaction (ADM-DM), so a suspension push is undeliverable by construction; the user learns of it at their next login, from the suspension shell. This is defensible and may well be intended — but it is currently an accident of ordering rather than a stated decision. *Recommended: state it explicitly in ADM-08, or reorder so the notice is sent before revocation.*

## Obligations

1. Every notification here is **dispatched by the API**, never by a client, and the dispatch is what resolves tokens and locale (ADR-001's policy layer).
2. Adding a notification means adding it here **and** giving it an in-app counterpart — rule 2 is not optional.
3. Copy for all of these must exist in **both** locale files before Slice 3, where the first real pushes are sent.
