---
description: Learn how to create your first workspace in Dastra.
---

# Create and set up a workspace

This page explains how to create a workspace, invite its first users, declare your first entity and move between your workspaces.

{% embed url="https://www.youtube.com/watch?v=IJE5rzou-EM" %}

## Sign in to Dastra

Start by signing in at [app.dastra.eu](https://app.dastra.eu). If you don't have an account yet, ask an administrator of your organization to invite you. If your organization does not use Dastra yet, [ask for a demo](https://www.dastra.eu/en/contacts/demo).

## Workspace

A workspace is **an organization that holds one or more records of processing activities**. You can create one workspace per record, per legal entity or per branch, as you choose. For the definitions of the other concepts (organization, organizational unit, entity, department), see [Key concepts](key-concepts.md).

{% hint style="warning" %}
A workspace is an environment whose **data is fully partitioned**: the records of one workspace (processing activities, assets, requests and so on) are never accessible from the context of another workspace. You can, however, view **consolidated statistics** across all your workspaces from the cross-workspace dashboard (see [Cross-workspace statistics](workspace.md#cross-workspace-statistics)), and duplicate items (processing activities, assets and so on) from one workspace to another.
{% endhint %}

## Create a workspace

Only organization owners can create a workspace.

1. On the page that lists your workspaces, click **Create Workspace**.
2. Fill in **Choose a label for your workspace**, which is required.
3. Optionally, add the workspace **Logo**: a square image of at least 200 x 200 px, cropped automatically.
4. Choose the language in the **Select the language used to provision the workspace elements** list.
5. Click **Continue**.

<figure><img src="../../.gitbook/assets/getting-started-workspace-3.png" alt="Workspace creation form"><figcaption><p>The workspace creation form</p></figcaption></figure>

To start from the configuration of an existing workspace, tick **Clone settings from another workspace**, choose the **Source workspace** and, if needed, tick **Include assigned users and teams**. The language choice disappears: the new workspace uses the language of the source workspace.

{% hint style="info" %}
Once the workspace is created, you can set up its organizational units and invite users.
{% endhint %}

### Invite the first users

After the creation, Dastra opens the users page of the new workspace. You can add existing users of the organization or invite new users with **Invite user**.

<figure><img src="../../.gitbook/assets/getting-started-workspace-4.png" alt="Step for inviting the first users of a workspace"><figcaption><p>The user invitation step</p></figcaption></figure>

Assign each user the role of your choice, then click **Next**. For the details of the invitation fields, see [Invite users](users.md).

### Create the first entity

In Dastra, a workspace is not a legal entity: it can group several, as in a corporate group. Each entity corresponds to a controller, and an entity has only one legal representative.

To create the first entity, fill in its **Entity name** and its **Country**: these are the two required fields. You can also indicate its representatives (the person in charge and the legal representative) and, if one has been appointed, its data protection officer.

<figure><img src="../../.gitbook/assets/getting-started-workspace-5.png" alt="Form for creating the first entity of the workspace"><figcaption><p>The form for creating the first entity</p></figcaption></figure>

Click **Continue** to enter your workspace. You can also click **Skip this step** and create your entities later.

### Create other entities and departments

Once your workspace is open, fill in the other legal entities and the departments as soon as possible. It simplifies the management of processing activities and the allocation of user rights later.

1. In the left menu, click **Workspace settings**, then **Organizational units**.
2. Click **Create an entity** to add a legal entity, or open the button's menu to choose **Create department**.
3. Repeat until the organization chart of your structure is represented in Dastra.

<figure><img src="../../.gitbook/assets/getting-started-org-units-6.png" alt="Organigram view of the organizational units in Dastra"><figcaption><p>The Organigram view</p></figcaption></figure>

For child departments, child entities, import and deletion, see [Create and set up organizational units](organizational-units.md).

## Access a workspace

1. Sign in to the application with your user account.
2. Click your workspace tile in the list that appears.

<figure><img src="../../.gitbook/assets/getting-started-workspace-1.png" alt="List of workspaces displayed as tiles"><figcaption><p>The list of workspaces</p></figcaption></figure>

You are now in your workspace. To switch workspace at any time, click the workspace selector at the top of the left sidebar.

<figure><img src="../../.gitbook/assets/getting-started-workspace-2.png" alt="Workspace selector open at the top of the left sidebar"><figcaption><p>The workspace selector</p></figcaption></figure>

## Cross-workspace statistics

The cross-workspace dashboard brings together the key indicators of all your workspaces in a single view. Owners access it with the **Reporting** button from the list of workspaces.

<figure><img src="../../.gitbook/assets/workspaces-reporting-button.png" alt="Reporting button in the workspace list"><figcaption><p>The Reporting button opens the cross-workspace dashboard from the workspace list</p></figcaption></figure>

It consolidates the indicators of the main modules: record of processing activities (ROPA), data subject requests, incidents, questionnaires, AI systems and tasks. The data is presented as widgets and charts.

<figure><img src="../../.gitbook/assets/cross-workspace-statistics-dashboard.png" alt="Consolidated cross-workspace statistics dashboard"><figcaption><p>Consolidated indicators of the record of processing activities and data subject requests across all workspaces</p></figcaption></figure>

Dynamic filters let you refine the analysis by workspace, by organizational unit and by type. The **Select a period** button restricts the indicators to a period: select a predefined period (Today, Current week, Current month, Current year, and so on) or a start date and an end date in the calendar, then click **Apply**. When no period is selected, the indicators cover all the data. The **Reset** button removes the selected period. The dashboard can be printed and exported.

## Go further

Follow the tutorial below or start exploring Dastra on your own.

{% content-ref url="../tutorial/README.md" %}
[README.md](../tutorial/README.md)
{% endcontent-ref %}
