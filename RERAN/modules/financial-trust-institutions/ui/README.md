---
project: RERAN
module: financial-trust-institutions
type: navigation
status: current
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - index
---

# Financial & Trust Institutions — UI Specifications

**Proposed.** The source material gives workflows, channels, output documents and SLAs, but no screen designs. This package applies the UI-spec format established in the Real Estate Developer module.

**Derivation note.** These screens are derived from the roles document, the services overview and the answered open questions — not from the service-flow files, which are currently thin (see issue #23).

> **Corrected 2026-08-15.** This package was reconciled against two decisions: the unified-access model (no role or permission-scope gating; role is audit-trail attribution only) and the corrected payment model (no standing account; per-transaction payment, upfront or at point of service, per `open-questions.md` B1 and B11). The Role × Screen Matrix below, the Service × Form Matrix's ownership column, and the Structural Characteristic section are all rewritten accordingly. `settlement-account.md` is retired and replaced by `payment-history.md`; `service-request.md` is retired and replaced by `screens-unified/submit-application.md` (issue #50, resolved).

---

## Screen Access

Every screen in this package is reachable by any of the institution's four Group C roles — Mortgage Officer, Institution Relationship Manager, Account Trustee, Auditing Bureau Officer. There is no permission-scope gating and no role-restricted variant of any screen. The **Role × Screen Matrix** this document previously carried is removed: under the unified model, that matrix would be a column of `●` repeated four times per row, which conveys nothing a screen list doesn't already say. Each screen's own file describes, where relevant, which role *typically* performs which action in practice — a UX default, not an access rule — under a "typically" framing rather than a Role Variations access table.

The one screen not reachable by any Group C role is [assisted-service-terminal](screens/assisted-service-terminal.md), operated by a Trustee Centre operator (Group G) — see its own entry below.

---

## Service × Form Matrix

All eighteen services use one configurable form — [Submit Application](screens-unified/submit-application.md), a progress-tracked wizard — rather than eighteen form specs. **Corrected 2026-08-15** — previously `service-request.md`, a single-page form; retired in Submit Application's favour after a full field-matrix audit found the per-service field set needs three distinct layout patterns (flat fields, repeatable groups, field-selection), not one generic layout, a finding that applied equally to both screen designs and made the wizard the better fit — see `screens-unified/README.md` for the full reasoning.

| Services | Assisted mode | Internal certification | Escrow-routed |
| :---- | :---: | :---: | :---: |
| #1 institutional approval | — | Optional | — |
| #2 institutional cancellation | — | Optional | — |
| #3–#7 mortgage lifecycle | Where source names centre | Yes when configured | — |
| #8–#11 finance lease lifecycle | Yes | Yes when configured | — |
| #12 fund company registration | Yes | Yes when configured | — |
| #13–#17 title and ownership | Yes | Yes when configured | — |
| #18 contract cancellation | Yes | Yes when configured | — |
| Group B escrow requests | — | — | Yes |

**Corrected 2026-08-15** — the previous "Owner (per answer A4)" column is removed. `open-questions.md` A4 (confirmed 2026-08-15, client decision) settles that no service is role-specific; any of the institution's four roles may act on any of the eighteen, so there is no per-service owner left to list.

Group B escrow requests are not among the eighteen. They arrive from the developer module and are worked in the escrow queue — see answer A2, which confirms from source rows 8–12 that the institution acts inside the platform rather than recording an outcome reached elsewhere.

---

## Screens

| Screen | Purpose |
| :---- | :---- |
| [dashboard](screens/dashboard.md) | Entry point: work in hand, approvals, and expiry warnings, with institution-wide Focus Area summaries |
| [Submit Application](screens-unified/submit-application.md) | The configurable form behind all eighteen services |
| [applications](screens/applications.md) | Search, filter and act on submitted requests, institution-wide |
| [application-details](screens/application-details.md) | One request: particulars, documents, workflow position, audit trail |
| [internal-certification-queue](screens/internal-certification-queue.md) | The institution's own maker-checker gate before RERAN submission |
| [escrow-request-queue](screens/escrow-request-queue.md) | Developer escrow requests awaiting certification |
| [escrow-request-details](screens/escrow-request-details.md) | One escrow request: solvency, milestone evidence, decision |
| [trust-accounts](screens/trust-accounts.md) | Register of trust accounts under the institution's trusteeship |
| [compliance-reports](screens/compliance-reports.md) | Independent compliance reports and escrow audit findings |
| [payment-history](screens/payment-history.md) | Per-transaction payment record: receipts, amounts, service references, status |
| [institution-profile](screens/institution-profile.md) | Approval standing, expiry tracking, and the staff roster |
| [documents](screens/documents.md) | Institution document repository, institution-wide |
| [notifications](screens/notifications.md) | Operational, approval and expiry alerts |
| [assisted-service-terminal](screens/assisted-service-terminal.md) | Group C services operated for a walk-in customer |

**Corrected 2026-08-15** — `settlement-account` is removed from this table; `payment-history` replaces it. `service-request` is removed; [Submit Application](screens-unified/submit-application.md) (a `screens-unified/` file, not `screens/`) replaces it — see the Service × Form Matrix note above. `dashboard`'s and `institution-profile`'s purpose lines drop role-specific and permission-scope language respectively.

Three of the fourteen screens now live in [`screens-unified/`](screens-unified/) rather than `screens/`: [Services Catalog](screens-unified/services-catalog.md) and [Service Details](screens-unified/service-details.md), which have no equivalent in the original 13-screen set and are not listed above, plus [Submit Application](screens-unified/submit-application.md), which replaces one. [Application Review](screens-unified/application-review.md) also has no equivalent and is not listed above, since it is a step inside the Submit Application flow, not a standalone entry in this table.

---

## Shared Documentation

Shared logic is defined once in these files and linked from screens. Screens must not restate it.

* [components.md](components.md) — component library, including the sidebar definition
* [validation-rules.md](validation-rules.md) — validation patterns, corrected 2026-08-15 to remove the retired permission-scope model
* [status-badges.md](status-badges.md) — status vocabularies and their treatments

---

## Screen File Template

Every screen file uses, in order: **Purpose, Layout, Sections, Empty State, Reused Components, Validation, Role Variations, User Flow, Notes.**

**Corrected 2026-08-15** — under the unified model, most screens now have no Role Variations to state and the section is either removed or replaced with a short "typically does X in practice" note. Where a screen's access genuinely doesn't vary by role at all, state that plainly rather than leaving an empty heading.

---

## Structural Characteristic

**Corrected 2026-08-15, superseding the issue #27 correction below.** The two-gate pattern — internal certification inside the institution, then external audit at RERAN — is sourced only for the mortgage and finance-lease lifecycle (Services #3–#11); the remaining services either don't carry the same source language or leave whether a certification gate applies to them as an open question. Where it applies, both gates still exist, but **the internal gate is no longer a permission scope.** It is an unrestricted action any of the institution's four roles may perform, including the filer of the same record (`open-questions.md` A1, confirmed via the 2026-08-14 unified-access decision). Every screen that submits, certifies or approves must still show which gate the record currently sits at and who currently holds it — see [screens/application-details.md](screens/application-details.md#section-1--header) for how that's surfaced — but "who holds it" is never a scope-restricted set of users; it is either the filer, RERAN, or nobody.

> **Superseded 2026-08-14 correction, kept for the record.** This section previously stated that every Group C action passes two gates unconditionally, which overstated what rows 28–45 support; the mortgage/finance-lease-only scoping above was the fix. That fix stands. What's additionally corrected now is the final paragraph that fix left in place: "The internal gate is a permission scope, not a role... filtered by scope, not by job title." Permission scopes are retired module-wide; the internal gate is filtered by nothing at all except whether the service sources it.
