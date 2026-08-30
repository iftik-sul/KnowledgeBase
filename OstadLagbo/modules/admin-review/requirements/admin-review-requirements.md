---
project: OstadLagbo
module: admin-review
type: requirements
status: current
updated: 2026-08-30
id: OL-ADM-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.1.md
owner: Iftikher
---

# Admin Review & Dashboard — Requirements

Derived from MVP Scope Baseline v1.1 §5: a full administrative control panel — review, moderation, user management, business analytics, communication, compliance tooling, and support all ship in the MVP. Report *creation* and blocking are governed by `ratings-and-trust`; profile fields by `ostad-profile` / `shagred-profile`.

The dashboard is a separate web application, English-only, desktop-oriented, and is the **only** interface holding these powers — none exist in the Flutter app.

## A. Overview

### ADM-01 Overview screen
Dashboard home shows KPI cards — pending reviews, open reports, Ostads by status, total Shagreds, suspended accounts, new registrations (today / 7 days), offers sent and **connections made** (7 days), open support tickets — each linking to its filtered view, plus a recent-activity feed (registrations, submissions, reports).

## B. Review management

### ADM-02 Review queue
All Ostad submissions — first submissions and key-field re-reviews — enter one queue, oldest first. Each item opens a review screen showing the complete profile, identity documents and selfie beside the claimed legal names and DOB, and, for re-reviews, a field-level diff against the last approved version. Nothing submitted can bypass the queue.

### ADM-03 Identity verification gate
The reviewer explicitly marks identity **passed** or **failed**. Approval is impossible while identity is not passed — the approve action must not be available in that state, in UI or API. Consequently every live Ostad holds the verified badge. Failed identity leads to request-changes (fixable: blurry image, name mismatch) or reject. **A submission whose ID number matches another active account is automatically flagged on the review screen and cannot be approved until the duplicate is resolved (REG-10, CL-012).**

### ADM-04 Verdicts
**Approve** (discoverable + badge, timestamp and reviewer recorded) · **Request changes** (mandatory written note) · **Reject** (mandatory written reason). Each verdict notifies the Ostad by push and in-app status (REG-11); verdict history is retained per account and neither note nor reason can be empty.

### ADM-05 Resubmission
Unlimited. Each resubmission re-enters the queue carrying full verdict history. (Ops note: abuse triggers a change request for a cooldown, not an ad-hoc rule.)

### ADM-06 Key-field re-review
Per baseline §5 / OSP-10: key-field edits create a re-review item while the public profile keeps serving the last approved version; approving publishes, rejecting (with reason) discards the pending change. At no moment does the public profile show unapproved content.

## C. Moderation

### ADM-07 Reports queue
Reports (created per `ratings-and-trust`) form a second queue: reporter, reported account, category, detail, and the reported content including cited chat messages. Actions: **dismiss** (optional note) / **warn** (message delivered to the account) / **suspend** (ADM-08) / **remove content** (for reports targeting a review or reply, per RNT-06). Every report reaches a recorded resolution; open/resolved status is tracked.

### ADM-08 Suspension and warnings
Admin can warn or suspend any account with a recorded reason. Suspended accounts cannot log in beyond a suspension-notice screen; a suspended Ostad leaves map and search immediately; their chats freeze. Suspension is reversible, and reinstatement restores prior state including approval. Offers pending to or from a suspended account cannot be acted on while the suspension stands; their expiry clocks continue to run. User-initiated deletion (REG-12) is separate.

### ADM-09 Block overview
A read-only view of blocking activity: accounts most blocked, recent blocks. Heavily-blocked accounts are a moderation signal; action goes through the account detail (ADM-10), not this view.

## D. User management

### ADM-10 User directories and account detail
**Ostad list:** every Ostad, filterable by status (draft / pending / changes requested / rejected / approved / suspended), searchable by name, phone, ID number, District, and skill category, sortable by registration and submission date. **Shagred list:** filterable by status, searchable by name and phone. Each row opens an **account detail view**: full profile including internal fields, verdict history, report history (as reporter and reported), audit entries touching the account, and applicable actions (verdicts where a review is open; warn / suspend / reinstate always). Privacy rules in SGP/OSP restrict users, never admin review; every identity-document view is audit-logged (ADM-17). Any account is findable by phone in one search.

## E. Content and taxonomy

### ADM-11 Skill-category management
Create, rename, deactivate categories. Each category carries an English name and an admin-managed **Bangla name/alias**, used for cross-script matching in the typeahead and keyword search (OSP-04, MAP-06; CL-013); per-category usage counts shown. In-use categories cannot be deleted, only deactivated — hidden from new selection while existing profiles keep them until their next skill edit. Renames (either script) propagate immediately. No operation can strand a profile with a nonexistent category.

## F. Analytics and business intelligence

All metrics below render as full charts and time-series with 7/30/90-day ranges. Every event they need must be instrumented in the app from day one — analytics is part of the build, never retrofitted. Chart rendering uses a standard library.

### ADM-12 Connections and marketplace funnels
The connection — an accepted offer — is the platform's success unit and is tracked explicitly:

- **Contacts made:** offers sent, offers accepted (= connections), unique Shagred–Ostad pairs connected, currently active chat relationships, messages exchanged, phone reveals — each as running totals and time-series.
- **Supply funnel:** registrations → onboarding completion → submission → approval, with stage conversion rates.
- **Demand funnel:** map sessions → profile views → offers sent → connections, with stage conversion rates.
- **Offer health:** response-time distribution; acceptance / decline / expiry shares.

### ADM-13 Growth and retention
- **Growth:** new registrations by role, approvals, and connections as daily/weekly series.
- **Activation:** share of new Shagreds sending ≥1 offer within 7 days; share of new Ostads reaching approval within 14 days; median time from Ostad registration to approval.
- **Retention:** returning users per week by role; repeat Shagreds (≥2 connections); Ostads receiving repeat offers.
- **Dormancy:** approved Ostads with no activity in 30 days (distinguishing paused per OSP-11 from inactive); Shagreds inactive since first week.

### ADM-14 Demand intelligence
Where demand outruns supply — the recruitment compass:
- Searches and category filters with **zero or few results**, grouped by category and map area.
- Top searched categories and keywords vs. approved-Ostad coverage by District and category.
- Profile views and offers concentrated on few Ostads (supply shortage signal in a category/area).

### ADM-15 Quality and operations
Ratings distribution and trend; review-submission rate among connections; reports per 100 weekly-active users; actual review turnaround vs. the 48h target; report resolution time; suspension and reinstatement counts; support ticket volume by category, resolution time, and reopen rate (SUP-06).

## G. Communication

### ADM-16 Broadcast notifications
Admin composes push broadcasts to a segment — all users, all Ostads, or all Shagreds — with title and body. Broadcasts are recorded (content, segment, sender, timestamp, recipient count). No per-user targeting beyond segments in MVP; warn messages (ADM-08) remain the individual channel.

## H. Operations and compliance

### ADM-17 Audit log
Every admin action — verdicts, identity marks, warns, suspensions, reinstatements, category changes, report resolutions, content removals, support replies and resolutions, broadcasts, and each viewing of identity documents — writes to an **append-only** audit log: actor, action, target, timestamp. The dashboard provides a searchable, filterable viewer (by actor, action type, target, date range). Entries cannot be edited or deleted from any interface. (Risk R-02 mitigation.)

### ADM-18 Identity-data retention tools
Dashboard tooling to execute the retention policy: view identity-document storage status per account, and purge identity documents of deleted accounts per policy schedule. Purges are themselves audit-logged. (Makes R-02's "retention and deletion policy" operational.)

### ADM-19 SMS/OTP monitor
Usage view: OTP volume by day, per-number rate-limit hits, estimated spend. Read-only; limits themselves are engineering config. (Risk R-08.)

### ADM-20 Admin accounts and access
Admin accounts are provisioned manually (no registration path), authenticate with email + password under REG-05 lockout rules. All admins currently hold full permission; role tiers are post-MVP. Admin sessions expire after 24 hours of inactivity.

## I. Settings

### ADM-21 Platform configuration (read-only)
A settings page displaying current platform values — offer expiry days, radius limits, portfolio limits, OTP parameters — read-only in MVP; changing them is an engineering deployment. Editable configuration is post-MVP.

## J. Support

### ADM-22 Support queue
Tickets created per the `support` module (SUP-02) arrive in a third queue: filterable by state (open / resolved) and category, with **Appeal**-category tickets flagged and sorted first. Opening a ticket shows the thread, the user's account context (linking to ADM-10 detail), and the attachment if present. Admin actions: **reply** (push-notifies the user, per SUP-03) and **resolve** (requires a closing reply). Reopened tickets return to the queue marked reopened. All replies and resolutions are audit-logged (ADM-17).

## Operational notes (non-binding)

Target first-verdict turnaround: 48 hours while the founder is sole reviewer. This dashboard is a full product surface (see risk R-06): build with managed services and standard libraries throughout; the audit log and this document keep every admin role transferable (risk R-05). Revenue metrics are absent by design — payments are out of MVP scope; when monetization enters scope, section F gains a revenue group via change request.
