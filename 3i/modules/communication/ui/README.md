---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
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

---

## Matrix

| Screen | Member | Instructor | Admin |
| :---- | :---: | :---: | :---: |
| [Chat room](screens/chat-room.md) | ● | ● | |
| [Report message](screens/report-message.md) | ● | ● | |
| [Admin moderation queue](screens/admin-moderation-queue.md) | | | ● |
| [Instructor room management](screens/instructor-room-management.md) | | ● | |
| [Notification centre](screens/notification-centre.md) | ● | ● | ● |
| [Notification preferences](screens/notification-preferences.md) | ● | ● | ● |
| [Admin email log](screens/admin-email-log.md) | | | ● |

Seven screens.

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