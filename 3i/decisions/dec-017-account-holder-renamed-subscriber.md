---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-017
tags: [decision, rbac, terminology]
---

# The Account Holder Role Is Renamed Subscriber

## Context

"Account holder" does three jobs in the baseline at once:

1. An account **type** in §3.2 — "Adult account holder"
2. A **role** in §4.1
3. Plain English, in FR-FAM-01 and FR-WAV-01 — "an account holder aged 18+"

A sentence like "the account holder must be an account holder" is not obviously nonsense, which is the problem.

## Decision

**The role is renamed `Subscriber`.** Taken 2026-08-18. The account type and the plain-English usage are unchanged.

Three seeded roles remain (FR-RBAC-02): **Admin**, **Instructor**, **Subscriber**.

## Reasoning

The commercial relationship is precisely what distinguishes this role from Admin and Instructor. `Subscriber` does not collide with `Account` or `Learner`, matches Stripe's own vocabulary, and FR-REP-01 already uses the word for churn reporting.

A 100% waiver produces a live subscription rather than a flagged free account (FR-WAV-06), so waived accounts are still subscribers.

## No Admin UI for Roles

Settled in the same review: **there is no admin screen for managing roles at launch.** FR-RBAC-04 requires that adding a role need no code change — that requirement is satisfied by roles being data. Creating one is a database operation.

This is consistent with §23 item 5, which defers the sub-admin roles and permission matrix. Admin remains the single administrative role.

## Consequences

- The permission key namespace is unaffected — keys are `module.action` (FR-RBAC-01), never role-named.
- Anywhere the baseline says "account holder" in the plain-English sense, it still means the adult who holds the account. Only the role label changes.

## Cost

The repository and the baseline now disagree on one label. FR-RBAC-02's seeded role list says "Account holder"; this project says `Subscriber`. That divergence is recorded here deliberately rather than left for someone to notice as an inconsistency.
