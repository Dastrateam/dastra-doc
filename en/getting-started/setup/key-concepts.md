---
description: >-
  Definitions of the concepts that structure Dastra: organization, workspace, organizational unit, entity, department and owner.
---

# Key concepts

Before you start using Dastra, take the time to understand the concepts that structure the platform. They help you organize your processing activities, your teams and your responsibilities.

***

## Contents

* [Organization](key-concepts.md#organization)
* [Workspace](key-concepts.md#workspace)
* [Organizational unit](key-concepts.md#organizational-unit)
* [Entity](key-concepts.md#entity)
* [Department](key-concepts.md#department)
* [Organization owner](key-concepts.md#organization-owner)
* [Credits and quotas](key-concepts.md#credits-and-quotas)

***

## Organization

An **organization** groups the accounts and users linked to your Dastra subscription. It is the root structure: it contains all your workspaces.

You see the name of your organization at the top right of the interface, under your user account name.

{% hint style="info" %}
An organization can contain several workspaces, each dedicated to a different project, entity or team. A user can belong to several organizations.
{% endhint %}

***

## Workspace

A **workspace** is the environment in which you collaborate with your team. It groups the modules and data linked to your entities: processing activities, audits, risks, incidents, data subject requests, and so on. The data of a workspace is never accessible from another workspace.

You choose your workspace when you sign in, by clicking its tile in the list of your workspaces.

Give your workspaces explicit names (for example "Group compliance" or "French entities"). It makes navigation easier when the organization has several.

***

## Organizational unit

**Organizational units** structure a workspace according to your internal organization. There are two types: entities and departments.

You attach processing activities, tasks, data subject requests, incidents and risks to an organizational unit. You can also associate access rights for users or teams with it.

{% hint style="info" %}
Organizational units are the reference for reports and for access permissions. See [Create and set up organizational units](organizational-units.md).
{% endhint %}

***

## Entity

An **entity** corresponds to a legal person, so to a **controller**: a company, a subsidiary, an association. It is the level at which you attach processing activities and key legal information.

An entity holds:

* the contact details of the controller,
* the **DPO** (data protection officer),
* the **lead supervisory authority**,
* the departments and child entities attached to it.

Example:

> Entity: _Dastra France SAS_\
> Department: _Marketing_\
> DPO: _Jean Dupont_

***

## Department

A **department** represents a service or a division of an entity (for example HR, IT, marketing, legal). It refines the distribution of activities within one entity.

Departments are used to:

* filter processing activities or audits by scope,
* assign tasks or requests to a targeted group,
* give a team access rights on a precise scope.

A department can have child departments. An entity can also have child entities, for example to represent the subsidiaries of a group.

{% hint style="info" %}
Departments are optional. They are useful as soon as the organization has several services whose processing activities you want to follow separately.
{% endhint %}

***

## Organization owner

The **owner** is the main administrator of the organization. Only owners can create workspaces, change the organization settings, create custom roles, and add or remove other owners.

Limit the number of owners to keep governance clear. Other users receive roles that fit their needs: see [Managing roles and permissions](roles.md).

***

## Credits and quotas

Your subscription sets credits, which are limits on what your organization can create or consume. They are shared by all the workspaces of the organization.

* **Users**: active users plus the users linked to a pending or expired invitation. Removing the user of an invitation frees a seat. See [Invite users](users.md).
* **Entities**: creating an entity consumes one entity credit. See [Create and set up organizational units](organizational-units.md).
* **Questionnaire templates**: the templates of all your workspaces count, including those in the recycle bin. See [Create a questionnaire template](../../features/questionnaires/templates/README.md).
* **Processing activities, document storage, cookie consent logs, activity history**: the **Change plan/Subscription** page of the organization settings shows the credit of your plan for each of them.
* **AI**: a monthly quota of AI credits, described in [How it works](../../features/general/ai-assistant/how-it-works.md#ai-credits-and-quotas).

When a limit is reached, the screen that is concerned says so and offers a link to contact the Dastra team and increase your credit.
