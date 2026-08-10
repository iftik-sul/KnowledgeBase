---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - components
---

# Components

**Proposed.** Shared components used across the Group C screens. Screens link here rather than restating definitions.

---

## Institution Operations Sidebar

The module's primary navigation. Its structure, the role × menu × scope matrix and the access rules governing it are defined in [navigation.md](../navigation.md) — navigation is a module-level concern, not a component-library one.

As a component: fixed left rail, active item highlighted, count badges on items carrying actionable work (Internal Certification, Escrow Requests, Applications, Notifications).

## Top Bar

Title, subtitle and search placeholder are set per screen and per role. Carries the institution name, the signed-in user's name and their active permission scopes.

The page uses the shared **Background + HorizontalBorder** component.

## Institution Context Header

A persistent strip below the top bar showing the institution's approval standing and settlement position — the two things that can block any action in the module.

* Approved status and expiry countdown (amber inside 60 days, red inside 14 — see [validation-rules.md](validation-rules.md))
* Available settlement balance and low-balance state

Suppressed on Institution Profile and Settlement Account, where the same information is the screen's subject.

## KPI Summary Cards

A row of metric cards at the head of list screens. Selecting a card filters the table beneath it. Card sets are defined per screen.

## Filter Bar

Search field plus dropdown filters and a Reset action. Filter sets are defined per screen. Every list screen carries a date-range filter and a sort control.

## Data Table

Column sets are defined per screen. All tables support column sort, row selection, a row action menu and pagination.

## Pagination

Rows per page, Previous, Next, page number, total records. Sits at the foot of every table.

## Status Badge

See [status-badges.md](status-badges.md) for every vocabulary and its treatment.

## Progress Tracker

A horizontal stepper showing a record's position across the two-gate pipeline:

`Draft → Internal Certification → Submitted → RERAN Review → Approved → Settled → Completed`

Steps are marked complete, current, pending or failed. Where an institution has not enabled internal certification, the second step is omitted rather than shown as skipped.

## Decision Panel

The action block on any screen where a user certifies, returns, approves or rejects. Contains the permitted actions for the current status and scope, a reason field, and an attachment control.

A reason is mandatory on every negative or returning action. This implements FR-04's requirement for documented reasoning and is enforced in [validation-rules.md](validation-rules.md).

**Some contexts extend this with structured fields in place of the bare reason box** — [screens/escrow-request-details.md](screens/escrow-request-details.md)'s milestone certification is the example, per answer A3's requirement that certification be a structured assessment rather than a document upload. The base panel (actions, reason, attachment) still applies underneath; the extension adds domain-specific fields the decision depends on, not a different mechanism.

## Document Uploader

Drag-and-drop plus file picker. Shows required versus optional documents for the current service, accepted formats, size limits and per-file validation state. Documents already held in the institution repository can be attached by reference rather than re-uploaded.

## Document Reference Picker

Attach a document already in the institution repository to a new request. Prevents the same instrument being uploaded once per transaction.

## Audit Timeline

A reverse-chronological record of every action on a record: actor, permission scope used, action, timestamp, reason where given, and any attachment added. Read-only and never editable, per FR-22.

## Information Cards

Grouped read-only field display used on detail screens.

## Balance Card

Available balance, pending charges and projected balance after committed fees. Shows the low-balance state and a Fund Account action where the user's scope permits it.

## Ledger Table

Date, description, linked application, charge, credit, balance-after, receipt reference. Exportable.

## Empty State

Illustration, message, primary action and secondary action. Message and actions are defined per screen — a generic empty state is not acceptable, because the empty state is where a user learns what the screen is for.

## Buttons

Primary, secondary, destructive and overflow menu. Destructive actions require confirmation.
