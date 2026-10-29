---
description: Find out how to manage roles and permissions in Dastra.
---

# Managing roles and permissions

When you invite a user, Dastra offers **five roles** by default:

* **Administrator**: administrators have contributor rights and can administer workspace settings. Administrators are the only ones who can set a processing activity to "published" status, create organizational units and invite new users to the workspace.
* **Contributor**: contributors can read and edit workspace content. They can create items and modify drafts that have not yet been published. They cannot modify workspace settings.
* **Reader**: readers can only view workspace content. They cannot edit content or modify workspace settings.
* **Auditor**: role of the compliance module. It gives read access to files and attachments, and lets you edit your own compliance audit items.
* **Compliance tester**: role of the compliance module. It gives read and write access to files and attachments, and lets you edit your own compliance operational items.

{% hint style="info" %}
Only **owners** can modify the organization account settings and create workspaces.
{% endhint %}

## Assign a role to a user

In Dastra, a user can have several roles. You can assign them from two places.

### In the current workspace

1. In the left menu, click **Workspace settings**, then **Users**.
2. Open the menu of the user's row, then click **Assign roles**. The number in brackets is the number of roles the user already has.
3. Select the role or roles to assign.

### In several workspaces at once

Only the owners of the organization can use this method.

1. Click your profile icon at the top right of the screen, then **Organisation Configuration**, then **Users**.
2. Open the menu of the user's row, then click **Workspaces**.
3. Click **Assign**, select the role, and choose the scope: **All workspaces from organization** or **Customized workspaces selection**.

<figure><img src="../../.gitbook/assets/getting-started-roles-1.png" alt="Role assignment window with the role list and the choice of workspaces"><figcaption><p>Assigning a role to all workspaces or to a selection</p></figcaption></figure>

You can also create custom roles, which may fit your organization better.

## Create a custom role

To create a custom role, you must be the owner of the organization.

1. Click your profile icon at the top right of the screen, then **Organisation Configuration**.
2. In the configuration panel, click **Roles and permissions**.

<figure><img src="../../.gitbook/assets/getting-started-roles-2.png" alt="Profile menu with the Organisation Configuration entry"><figcaption><p>The profile menu</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/getting-started-roles-3.png" alt="Organization configuration panel with the Roles and permissions button"><figcaption><p>The organization configuration panel</p></figcaption></figure>

The list of roles and permissions appears.

<figure><img src="../../.gitbook/assets/getting-started-roles-4.png" alt="List of base roles and custom roles"><figcaption><p>The list of roles, with examples of custom roles</p></figcaption></figure>

{% hint style="info" %}
Only the organization's owners can access the roles and permissions management screen.
{% endhint %}

3. Click **Create new role** and give it a name.
4. Tick the permissions linked to each feature (**Read**, **Write**, **Create**, **Import**, **Export**, and so on). In the modules that offer it, the **Create** permission allows the creation of new items, independently of the **Write** permission, which allows their modification (see [Roles and permissions](../../features/settings/roles.md)).
5. Click **Save changes** at the bottom of the screen.

To start from an existing role, click **Clone** next to it. **View permissions** displays the permissions of a role without changing it.

{% hint style="info" %}
To take effect, the new role must be assigned to one or more users, from the **Users** page described above.
{% endhint %}

You can now follow the tutorial or start exploring Dastra's features on your own.

{% content-ref url="../tutorial/README.md" %}
[README.md](../tutorial/README.md)
{% endcontent-ref %}
