---
project: OstadLagbo
module: support
type: requirements
status: current
updated: 2026-08-30
id: OL-SUP-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.1.md
owner: Iftikher
---

# Support — Requirements

Added by founder decision 2026-08-30 (change log CL-009; to be absorbed in baseline v1.2). Gives users an in-app channel for help and appeals. Ticket *handling* lives in the admin panel (ADM-22); abuse reporting is a separate system (RNT-07) and is never replaced by tickets.

## SUP-01 Help & Support screen

Reachable from settings for both roles (including pending Ostads). Contains: **create a ticket**, **my tickets** (history and open threads), and links to the Privacy Policy and Terms of Service. Guests do not see this screen; the store listing and the platform's public contact email remain their channel.

## SUP-02 Creating a ticket

A ticket has: a **category** — Account & login / Verification & review / Technical problem / Appeal a decision / Other — a free-text description (proposed cap 1,000 characters), and optionally **one image attachment** (screenshot; OSP image rules; visible only to support/admin). Proposed limit: 5 open tickets per user. Submission confirms in-app and the ticket appears in "my tickets."

**Acceptance:** every category creates a ticket reaching the admin queue; the attachment is never visible to any other user.

## SUP-03 Ticket thread and lifecycle

Each ticket is a private thread between the user and support: the admin replies from ADM-22, the user is push-notified and can respond in-thread. States: **open → resolved** (by admin, with a closing reply). The ticket list shows each ticket's state and an unread-reply indicator; per the platform's notification principle (OFR-03), every push has an in-app counterpart, so a user with notifications denied misses nothing. A user may add to a resolved ticket within **14 days**, which reopens it; after that, a new ticket. Threads follow the retention policy's reports-and-moderation schedule (2 years after resolution).

**Acceptance:** replies notify the user and set the unread indicator; reopening works inside 14 days and not after; ticket threads never mix with offer chat.

## SUP-04 Appeals from suspension

The suspension-notice screen (ADM-08) — the only screen a suspended user can reach — includes **"Appeal this decision"**, which creates a ticket in the *Appeal* category without granting any other app access. This closes the loop the Terms of Service §7 promises. Banned/deleted users who cannot log in retain the public contact email as fallback.

**Acceptance:** a suspended account can create and follow an appeal ticket and do nothing else; the appeal reaches ADM-22 flagged as an appeal.

## SUP-05 What tickets are not

Tickets are not the abuse-reporting channel — report actions (RNT-07) remain in place on profiles, messages, and reviews, and the app steers users filing abuse content in a ticket toward the report flow. Tickets are not real-time chat: no delivery/read states, no voice notes; expectations set as "we reply as soon as we can."

## SUP-06 Instrumentation

Emitted for ADM-15: tickets created by category, resolution time, reopen rate.

## Proposed technical defaults summary

Description cap, open-ticket limit, image rules, and the 14-day reopen window are engineering defaults. The category set, the suspension-appeal path, one-image maximum, and the ticket/report separation change only with founder approval.
