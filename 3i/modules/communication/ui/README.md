---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-24
id: 3I-CMN-UI-000
derived_from:
  - requirements/chat-group-chat-and-moderation.md
  - requirements/not-notifications.md
tags:
  - ui
  - matrix
---

# Communication — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Member** | Participating in a room, directly or on behalf of an under-13 profile |
| **Instructor** | Moderating their own courses' rooms |
| **Admin** | |
| **Mobile (Flutter)** | Not a role — a platform column marking which screens are in scope for the native app. See [mobile-scope.md](/3i/mobile-scope.md) |

---

## Matrix

| Screen | Member | Instructor | Admin | Mobile |
| :---- | :---: | :---: | :---: | :---: |
| [Chat room](screens/chat-room.md) | ● | ● | | ● |
| [Report message](screens/report-message.md) | ● | ● | | ● |
| [Admin moderation queue](screens/admin-moderation-queue.md) | | | ● | |
| [Instructor room management](screens/instructor-room-management.md) | | ● | | ● |
| [Notification centre](screens/notification-centre.md) | ● | ● | ● | ● |
| [Notification preferences](screens/notification-preferences.md) | ● | ● | ● | ● |
| [Admin email log](screens/admin-email-log.md) | | | ● | |

Seven screens, five in scope for mobile — see [mobile-scope.md](/3i/mobile-scope.md#2-scope-by-module).

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | Message Bubble, Guardian Attribution Tag, Notification Row |
| [validation-rules.md](validation-rules.md) | Message length/content, report reason requirement |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| None. | |
