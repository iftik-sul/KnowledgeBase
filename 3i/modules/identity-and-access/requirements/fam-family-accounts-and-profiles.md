---
project: 3i
module: identity-and-access
type: requirements
status: current
updated: 2026-08-18
id: 3I-IDA-REQ-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - family-accounts
---

# Family Accounts and Learner Profiles

Baseline §6. Ten requirements.

This is where the platform's approach to children actually lives. A guardian holds the account; children exist as profiles beneath it with no credentials of their own.

---

## Creation and Limits

| ID | Requirement |
| :---- | :---- |
| **FR-FAM-01** | Only an account holder aged **18+** may create learner profiles |
| **FR-FAM-02** | Maximum **6 learner profiles** per account |
| **FR-FAM-03** | A profile carries display name, date of birth, optional avatar, and optional 4-digit PIN. It has **no email address and no credentials** |
| **FR-FAM-04** | Profile selection occurs after account login via a profile picker |
| **FR-FAM-06** | Profile creation and deletion are rate-limited to **2 changes per 30 days** |

**FR-FAM-01 excludes 13–17 standalone accounts from creating profiles.** A 17-year-old holds an account and studies, but cannot carry dependents. The acceptance criteria test this explicitly.

**FR-FAM-02's cap was reviewed and retained.** Removal was considered on 2026-08-18 and rejected — see [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md).

**FR-FAM-06's scope has been narrowed by decision.** The rate limit now applies to **activation and cancellation**, not to profile creation. Creating a profile is free, touches no seat, and is untracked against the limit; only the paid, seat-consequential actions are throttled. The baseline's own wording is "profile creation and deletion" — the divergence is deliberate and must be stated wherever this is implemented.

---

## Immutability

| ID | Requirement |
| :---- | :---- |
| **FR-FAM-05** | A profile's name **locks permanently once a certificate has been issued** to it. Admin may unlock on request, with a reason recorded |
| **FR-FAM-07** | Profile date of birth is set at creation and is **not user-editable**. Corrections go through admin |

These two are safeguarding and integrity controls, not conveniences.

**FR-FAM-07 is the control that makes the age model hold.** Chat access is derived from profile age (FR-FAM-08). If a guardian could edit a date of birth, they could lift a child's chat restriction by editing a field. Making it admin-only is what prevents that.

**FR-FAM-05 protects the certificate, not the profile.** A certificate snapshots the learner name at issue ([3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)), so a later rename would leave the certificate and the profile disagreeing about who earned it.

---

## Chat Access

| ID | Requirement |
| :---- | :---- |
| **FR-FAM-08** | Chat access is derived from profile age: **under 13 is permanently off; 13–17 is a guardian-controlled toggle** |

Derived, never stored. A stored permission can drift from the age it was derived from; a derived one cannot.

Full chat rules are in [age-and-safeguarding.md](/3i/age-and-safeguarding.md) and the `communication` module. Note that an under-13 learner has no route into a room at all — the guardian participates on their behalf, displayed as *"Fatima (guardian of Aisha)"* (FR-CHAT-06).

---

## Guardian Dashboard

| ID | Requirement |
| :---- | :---- |
| **FR-FAM-09** | The guardian dashboard shows per-profile progress, enrolments, attendance, exam results, and certificates |

This dashboard must now represent **three** profile states, not two — active, inactive, deleted. Inactive is new, introduced by [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) and absent from the baseline.

Blocked by [OQ-08](/3i/open-questions.md#oq-08--do-inactive-profiles-count-against-the-six-profile-cap) until it is decided whether inactive profiles occupy cap slots.

---

## Deletion

| ID | Requirement |
| :---- | :---- |
| **FR-FAM-10** | Deleting a profile removes progress, enrolments, and exam results. **Issued certificates remain valid and publicly verifiable** |

Deletion is the destructive action. Seat cancellation is not — it deactivates a profile while preserving everything. **The two must remain visibly distinct in every interface**, since they now sit close together and one is irreversible.

What deletion does to chat history is contested. FR-CHAT-14 retains messages on *account* deletion and anonymises authorship to "Deleted user"; the decision taken for *profile* deletion removes them. Unresolved — [OQ-06](/3i/open-questions.md#oq-06--chat-history-on-profile-deletion) and [3I-DEC-012](/3i/decisions/dec-012-chat-history-on-profile-deletion.md).

---

## Acceptance Criteria

From §6.

1. A **17-year-old standalone account cannot create profiles**.
2. A **seventh profile is refused**.
3. A renamed profile is refused once a certificate exists, **with the reason shown**.
4. After profile deletion, the **certificate verification URL still resolves correctly**.

Criterion 4 is the one most likely to fail late. It requires the certificate to survive with no reference back to the profile — which only works because the learner name was snapshotted at issue.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-IDA-DM-001](../data-model.md) |
| Registration and the age gate | [3I-IDA-REQ-001](auth-registration-and-authentication.md) |
| Age rules | [age-and-safeguarding.md](/3i/age-and-safeguarding.md) |
| Seats and activation | [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) |
| Certificate snapshotting | [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md) |
