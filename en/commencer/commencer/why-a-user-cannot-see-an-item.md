---
description: >-
  A user cannot see a processing activity or a tab, or gets a 403 error?
  Understand how roles, teams and organisational units determine what they can
  see.
---

# Why can't a user see a processing activity?

Two users with the same role do not necessarily see the same items. In Dastra, access depends on **two levels** that add up:

1. **Their roles**: they determine what the user can do in each module (read, write, create, export…) and in which workspaces.
2. **The organisational units they can access**: they determine on which scope (entity, department) the user can view and edit items.

If either is missing, the item does not appear, or an access error (403, "Resource inaccessible") is displayed.

## 1. Check roles

* Organisation **owners** have access to all active workspaces, all organisational units and all permissions.
* Other users only have the permissions of the **roles assigned to them**, workspace by workspace. A role can be assigned to a specific workspace or to all workspaces.
* A role with no permission ticked gives access to nothing.
* A user can hold several roles.

In **Settings > Users** (of the relevant workspace), check which roles are assigned, then in **Configuration > Roles and permissions** that the module has at least the **Read** permission. See [Roles and permissions](../../features/settings/roles-et-permissions.md).

{% hint style="info" %}
The **Read/Edit your own items** permission only gives access to items assigned to the user, not to all items in the module.
{% endhint %}

## 2. Check access to the organisational unit

Each processing activity is attached to an organisational unit. If the user has no access to that unit, they do not see its processing activities, even with the right role.

The rules are:

* By default, an organisational unit is **accessible to everyone** in the workspace: the message "Everyone is allowed to view or edit…" appears in its permissions.
* As soon as you **set permissions** on a unit (allowed users or teams), only the listed users and members of listed teams can access it.
* **Child** units **inherit** the permissions of their parent unit (shown as "Inherited") as long as they have none of their own. If a child unit sets its own permissions, they replace the parent's.

To view or change these rules, open **Settings > Organisational units**, then in the menu of the relevant unit choose **Set permissions for…**. This action is restricted to users with the advanced management right.

{% hint style="warning" %}
Frequent cause: a team was added on a parent unit and the user does not belong to that team. They then lose access to all child units that have no permissions of their own. Check which [teams](create-and-assign-teams.md) they belong to.
{% endhint %}

## Quick checklist

| Symptom | What to check |
|---|---|
| No processing activity visible, or a tab is missing | Is a role with the module's **Read** permission assigned in this workspace? |
| Only some processing activities are visible | Organisational unit access, inheritance from the parent unit, team membership |
| A colleague with the same role sees more items | They probably belong to a team allowed on the unit, and you do not |
| The save button is greyed out | Missing **Write** permission (or **Create** for a new item) |
| 403 "Resource inaccessible" error | Access to the item's organisational unit, or no role in this workspace |

If everything is correct and the item stays invisible, contact Dastra support with the workspace, the user and the item concerned.
