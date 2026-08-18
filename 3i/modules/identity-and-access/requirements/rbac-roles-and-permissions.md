---
project: 3i
module: identity-and-access
type: requirements
status: current
updated: 2026-08-18
id: 3I-IDA-REQ-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - rbac
---

# Roles and Permissions

Baseline §4. Five requirements — the smallest set in this module and the one with the strictest acceptance criterion.

---

## Roles at Launch

| Role | Description |
| :---- | :---- |
| **Admin** | Full platform control. Single role at launch |
| **Instructor** | Creates and manages own courses, batches, questions, exams. Grades and marks attendance |
| **Member** | Manages profiles, subscription, enrolments. May also be a learner. Renamed from the baseline's "Account holder" — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md) |

Three roles ship. **Admin** is the single *administrative* role — sub-admin roles and the wider permission matrix are deferred (§23 item 5), with the RBAC foundation built. **No admin UI for role management is planned at launch**; FR-RBAC-04's "no code change" requirement is satisfied by roles being data, and creating one at this stage is a database operation rather than a screen.

Role and learner status are orthogonal: a Member may also be a learner.

---

## Requirements

| ID | Requirement |
| :---- | :---- |
| **FR-RBAC-01** | Permissions are modelled as discrete keys (`module.action`) assigned to roles, assigned to users. **No hard-coded role checks anywhere in the codebase** |
| **FR-RBAC-02** | The system ships with three seeded roles. Admin holds every permission |
| **FR-RBAC-03** | Every API route declares the permission key it requires |
| **FR-RBAC-04** | Adding a new role must require **no code change** — only data |
| **FR-RBAC-05** | Admin accounts support optional TOTP two-factor authentication |

---

## Acceptance Criteria

From §4.

1. A new role can be created in the database with a subset of permissions and behaves correctly **without deployment**.
2. **No occurrence of `isAdmin`, `role === 'admin'`, or equivalent exists in application logic.**
3. Every route returns **403** when the required permission is absent.

Criterion 2 is unusual: it is a constraint on the source code itself, not on observable behaviour. It is greppable, and it should be enforced in review or CI rather than checked once at sign-off, because it is the kind of thing that passes at delivery and decays afterwards.

---

## The Regression to Watch For

With only three coarse roles shipped, every permission check looks redundant. A developer optimising for readability will be tempted to collapse `can('course.publish')` into `if (user.role === 'admin')`, and it will work — until the fourth role exists, at which point every such check is wrong and invisible.

This is the entire reason FR-RBAC-01 and FR-RBAC-04 exist, and why [3I-DEC-007](/3i/decisions/dec-007-rbac-without-hardcoded-roles.md) records it. The discipline is invisible while it is working.

---

## Note on 403 versus 404

Criterion 3 requires **403** for a missing permission. This is the general rule.

**The question bank is an exception.** FR-QB-04 requires **404** for another instructor's bank, because a 403 confirms the bank exists and instructor questions are private even from admins (FR-QB-03). See [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md).

Anyone implementing a generic permission middleware needs to know that `assessment` overrides the default. It is the only place in the project that does.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-IDA-DM-001](../data-model.md) |
| Question bank exception | [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md) |
| Role renamed to Member | [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md) |
| Audit logging of admin actions | NFR-09 |
