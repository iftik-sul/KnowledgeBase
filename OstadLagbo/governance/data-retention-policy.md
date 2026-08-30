---
project: OstadLagbo
type: retention-policy
status: current
updated: 2026-08-30
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

## Retention schedule

| Data category | While account lives | On deletion |
|---|---|---|
| Identity documents (NID/passport images, selfie) | Retained encrypted; admin-review access only | **Purged at day 30** with the account |
| ID number (NID or passport number) | Retained | Retained **12 months after deletion** solely for abuse and safety investigations — a report filed against a deleted account within this window can still be traced to a real identity — then purged |
| Account & profile data (names, photos, address, profile content) | Retained | Purged at day 30 |
| Abandoned Ostad onboarding drafts (incl. uploaded documents) | — | Purged after **90 days of draft inactivity**, with prior notice |
| Chat messages & voice notes | Life of the relationship; one party's deletion anonymizes their side, the other keeps history (OFR-06) | Full thread purge **90 days after both parties are gone** |
| Reviews & ratings | Persist | Anonymized ("Former Shagred"), persist with aggregate weight (RNT-05) |
| Connection records (accepted offers) | Persist | Anonymized; Ostad-history entries show "deleted account" (SGP-03) |
| Offers (declined / expired / withdrawn) | Retained 12 months for analytics, then aggregate-only | Purged at day 30 |
| Reports & moderation records | Retained | **2 years after resolution**; longer under legal hold |
| Admin audit log | Append-only, **3-year rolling retention** | Unaffected by user deletion (accountability record) |
| OTP codes / OTP request logs | Minutes / **90 days** | — |
| User-linked analytics events | **24 months**, then aggregate-only | De-linked at day 30 |
| Backups | Standard cycles | Deleted data ages out of all backups within **90 days** of purge |

## Banned-account exception

When an account is suspended for fraud, safety violations, or ban-worthy conduct and is deleted (by the user or the platform), the platform retains the minimum needed to prevent re-registration and document the conduct: **ID-number hash, phone number, legal name, and the records of the violating behavior** — for as long as the ban stands. Everything else purges on schedule. This mirrors industry practice of retaining data relating to fraudulent behavior and the data needed to prevent platform re-access.

## Legal hold

An active report alleging serious harm, a law-enforcement request, litigation, or an insurance-relevant incident suspends purging of the specifically relevant data until the matter resolves, after which the schedule resumes. A report filed against a deleted account within the 12-month ID-number window triggers a hold on that identity data. Legal holds are recorded and audit-logged.

## No financial retention

The MVP processes no payments, so no tax/financial record retention applies. When payments enter scope (change request), this policy gains a financial-records section before launch of that feature.

## Operational obligations

ADM-18 tooling implements: day-30 purge automation, the 12-month ID-number purge, draft-inactivity purge, both-parties-gone chat purge, banned-account minimal retention, and legal-hold flags. Purges are audit-logged. Hosting and backup architecture must honor the 90-day backup age-out and the PDPA's data-residency rules for restricted-category data (engineering + legal checkpoint before infrastructure selection).

## Review

Revisited annually, on any PDPA amendment, and on any scope change touching data collection. Changes to durations require founder approval and a change-log entry when they alter user-facing commitments.
