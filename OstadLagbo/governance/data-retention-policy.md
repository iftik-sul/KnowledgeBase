---
project: OstadLagbo
type: retention-policy
status: current
updated: 2026-09-26
id: OL-RET-001
approved: 2026-08-30
owner: Iftikher
legal_review: pending
---

# Data Retention & Deletion Policy

Defines how long every category of Ostad Lagbo data lives, what deletion means, and the exceptions. This policy is a hard precondition of operations: **no identity document is collected in production before this policy is in force** (risk R-02). It is executed operationally by the admin panel's retention tooling (ADM-18), and every purge it mandates is audit-logged (ADM-17).

## Legal context

Bangladesh's Personal Data Protection Act, 2026 (in force April 2026) governs this platform's data handling. It requires consent-based collection, disclosure of retention durations to users, honoring erasure rights, and breach notification. This policy supplies the retention durations that the user-facing Privacy Policy discloses; breach handling lives in the Incident Response process. `legal_review: pending` — a Bangladesh-qualified lawyer reviews this policy and its user-facing counterparts before launch.

## Principles

1. Data is kept only as long as it serves the user or protects the platform — never "just in case."
2. Honest users who leave get clean deletion; retention beyond deletion serves only demonstrated bad actors, active legal matters, and a limited identity-traceability window for post-deletion abuse claims.
3. Every duration in this policy appears in the user-facing Privacy Policy; users are never told less than this document says.

## The deletion model

Account deletion is self-service (REG-12). On request: the account **deactivates immediately** — invisible on all surfaces, unusable, chats closed per OFR-06. A **30-day recovery window** follows: logging in restores the account fully. At day 30 without recovery, **permanent purge** executes per the schedule below. This mirrors established marketplace practice (Uber's deletion model) and satisfies PDPA erasure rights.

**Admin termination (CL-019)** follows the same 30-day rhythm from the other direction: a terminated account stays suspended for 30 days — during which it may appeal, and nothing else — then purges under the banned-account exception below. There is no recovery by login; reinstatement is an admin decision on the appeal.

## Retention schedule

| Data category | While account lives | On deletion |
|---|---|---|
| Identity documents (NID/passport/licence images, selfie) | Retained encrypted; admin-review access only. **Draft documents replaced before review are deleted at replacement** (REG-DM) | **Purged at day 30** with the account |
| ID number (NID, passport, or licence number) | Retained | Retained **12 months after deletion** solely for abuse and safety investigations — a report filed against a deleted account within this window can still be traced to a real identity — then purged |
| Account & profile data (names, photos, address, profile content) | Retained | Purged at day 30 |
| Pending registrations (details submitted before the phone is verified) | Deleted at verification (converted into the account) or at 15-minute expiry | — |
| Consent records (accepted document versions and timestamps) | Retained | **Retained 3 years after purge** as proof of lawful basis under the PDPA, alongside the account tombstone; then purged |
| Abandoned Ostad onboarding drafts (incl. uploaded documents) | Purged after **90 days of draft inactivity**, with prior notice | — |
| Abandoned profile revisions (proposed key-field changes, incl. uploaded identity documents and photos) | Discarded after **90 days of inactivity**, with prior notice; their uploads deleted (OSP-10, CL-021) | Purged with the account |
| Chat messages & voice notes | Life of the relationship; one party's deletion freezes the thread, the other keeps history (OFR-06) | Full thread purge **90 days after both parties are gone** |
| Reviews & ratings | Persist | Shown only by the reviewer's first initial (e.g. "R.", CL-028), so nothing changes on deletion; persist with aggregate weight (RNT-05) — a banned account's ratings are retained by decision (CL-024); admins remove individual fraudulent reviews via `remove_content` |
| Connection records (accepted offers) | Persist | Anonymized; Ostad-history entries show "deleted account" (SGP-03) |
| Offers (declined / expired / withdrawn) | Retained 12 months for analytics, then aggregate-only | Purged at day 30 when either party purges |
| Reports & moderation records | Retained | **2 years after resolution**; longer under legal hold |
| Support tickets | Retained | **2 years after resolution**; abandoned non-appeal tickets auto-resolve after 90 days of inactivity so the clock starts |
| Admin audit log | Append-only, **3-year rolling retention** | Unaffected by user deletion (accountability record) |
| OTP codes / OTP request logs | Minutes / **90 days** | — |
| Push device tokens | Retained while the device session lives | Revoked at logout, suspension, or deletion request; purged with the account |
| User-linked analytics events (ADR-002) | **24 months**, then aggregate-only | De-linked at day 30 |
| Backups | Standard cycles | Deleted data ages out of all backups within **90 days** of purge |

## Banned-account exception

When an account is **terminated by admin** (CL-019) for fraud, safety violations, or ban-worthy conduct, the platform retains the minimum needed to prevent re-registration and document the conduct: **ID-number hash, phone number, legal name, and the records of the violating behavior** — for as long as the ban stands. Everything else purges on schedule at the end of the 30-day appeal window. This mirrors industry practice of retaining data relating to fraudulent behavior and the data needed to prevent platform re-access.

## Legal hold

An active report alleging serious harm, a law-enforcement request, litigation, or an insurance-relevant incident suspends purging of the specifically relevant data until the matter resolves, after which the schedule resumes. A report filed against a deleted account within the 12-month ID-number window triggers a hold on that identity data. Legal holds are recorded and audit-logged (`legal_hold_set` / `legal_hold_released`).

**How a hold is placed (CL-041).** An admin sets or releases it from the account detail or retention view (ADM-18), with a written reason; the flag is `user_account.legal_hold`, and every module's retention section already honours it. The tooling ships in **Slice 4** with the rest of ADM-18's automated retention; before then a hold is applied by direct database update, the same interim pattern as manual purge (CL-034). **A separate, automatic protection also applies: an open appeal ticket pauses the purge of the account it contests** — see REG-DM's purgeable predicate.

## No financial retention

The MVP processes no payments, so no tax/financial record retention applies. When payments enter scope (change request), this policy gains a financial-records section before launch of that feature.

## Operational obligations

ADM-18 tooling implements: day-30 purge automation (self-service and termination paths), the 12-month ID-number purge, the 3-year consent-record purge, pending-registration expiry, draft-inactivity purge, abandoned-revision discard, both-parties-gone chat purge, banned-account minimal retention, storage-object deletion in the same operation as the referencing row (with orphan sweeps), and legal-hold flags. Purges are audit-logged. Hosting and backup architecture must honor the 90-day backup age-out and the PDPA's data-residency rules for restricted-category data — the ruling on identity documents stored in Singapore is deferred by founder decision (CL-025, 2026-09-26): Singapore storage is accepted through development, and compliance for restricted-category data (in-country storage or legal sign-off) is required **before public launch**. Real identity documents are collected from Slice 1, so this carries live-data risk from Slice 1 until resolved (R-10, ADR-001).

## Review

Revisited annually, on any PDPA amendment, and on any scope change touching data collection. Changes to durations require founder approval and a change-log entry when they alter user-facing commitments. **Pending for the Privacy Policy v1.1 refresh:** the pending-registration, abandoned-revision, and analytics-store rows added since v1.0.
