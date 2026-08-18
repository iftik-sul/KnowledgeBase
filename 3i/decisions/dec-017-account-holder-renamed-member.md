---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-017
tags: [decision, rbac, terminology]
---

# The Account Holder Role Is Renamed Member

## Context

"Account holder" does three jobs in the baseline at once:

1. An account **type** in §3.2 — "Adult account holder"
2. A **role** in §4.1
3. Plain English, in FR-FAM-01 and FR-WAV-01 — "an account holder aged 18+"

A sentence like "the account holder must be an account holder" is not obviously nonsense, which is the problem.

## Decision

**The role is renamed `Member`.** Taken 2026-08-18. The account type and the plain-English usage are unchanged.

Three seeded roles remain (FR-RBAC-02): **Admin**, **Instructor**, **Member**.

## Reasoning

`Member` describes belonging to the institute rather than paying it, which is what makes it correct in the cases where a billing-derived name would be wrong:

- **A lapsed account.** FR-BILL-06 suspends access at final payment failure. The account still holds its role and its profiles; it is simply not paying.
- **A free account.** FR-WAV-06 notes admin-created free accounts are a separate mechanism from waivers.
- **A waived account.** A 100% waiver produces a live subscription with a zero invoice.

A name like `Subscriber` would be wrong in exactly those three cases — which are the ones that generate support tickets. `Member` is true in all of them.

It also fits an educational institution's own vocabulary, and collides with nothing: not `Account`, not `Learner`, not the baseline's plain-English "account holder".

### Rejected

| Candidate | Why not |
| :---- | :---- |
| `Subscriber` | Ties a permission role to a billing state. Wrong for lapsed, free, and suspended accounts |
| `Guardian` | An adult studying alone holds this role and is guardian to nobody |
| `Student` | §3 explicitly refuses the word as ambiguous. Reintroducing it as a role label would undo what the identity model exists to prevent |

## No Admin UI for Roles

Settled in the same review: **there is no admin screen for managing roles at launch.** FR-RBAC-04 requires that adding a role need no code change — satisfied by roles being data. Creating one is a database operation.

Consistent with §23 item 5, which defers sub-admin roles and the permission matrix. Admin remains the single administrative role.

## Consequences

- The permission key namespace is unaffected — keys are `module.action` (FR-RBAC-01), never role-named.
- Anywhere the baseline says "account holder" in the plain-English sense, it still means the adult who holds the account. Only the role label changes.

## Cost

The repository and the baseline now disagree on one label. FR-RBAC-02's seeded role list says "Account holder"; this project says `Member`. Recorded here deliberately rather than left for someone to notice as an inconsistency.
