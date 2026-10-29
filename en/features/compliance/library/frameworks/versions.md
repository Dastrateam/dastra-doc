---
description: >-
  Evolve a framework through successive versions, publish them, choose the
  current version and update the compliance projects that use it.
---

# Framework versions

Every framework in the Library is versioned. A version has an automatically assigned number (_Version 1_, _Version 2_, etc.), a version note and a status (draft or published). Versions let you evolve a framework (regulatory update, added or reworded requirements, reorganized chapters) without changing the compliance projects that use an earlier version.

<figure><img src="../../../../.gitbook/assets/compliance-framework-detail-version-header.png" alt="Framework header showing the version number, the Current version label and the Published status"><figcaption><p>The version number, the Current version label and the status are displayed under the framework name</p></figcaption></figure>

***

## Version number and current version

The version number is displayed under the framework name, on its card in the list of frameworks and in the **Detail** tab (**Version information** card, together with the version note).

The **Current version** label identifies the version installed by default when the framework is added to a project. A framework has only one current version.

The list of frameworks in the Library shows the current version of each framework. The other versions are available from the framework's **Versions** tab.

***

## Viewing the version history

The **Versions** tab of a framework lists all its versions, from the most recent to the oldest. Each row shows:

* the version number and, where applicable, the **Current version** label,
* the status (draft or published),
* the version note,
* the creation date and the author of the version.

Click a version (or **View** in its actions menu) to open it. A published version opens in read-only mode.

Depending on its status, the actions menu of each version offers:

* **View**: open the version,
* **Edit version note**,
* **Set as current version** (published version that is not the current version),
* **Publish** (draft version),
* **Cancel publication** (published version),
* **Delete** (draft version).

***

## Creating a version

1. Open the framework, then the **Versions** tab.
2. Click **Create a new version**.
3. The window shows the automatically assigned number (**New version:** _Version n_). Optionally enter **Version notes** (up to 3,000 characters), for example _Regulatory update 2026_.
4. Click **Validate**.

The version copies the framework structure (chapters, requirements and linked controls) and is created as a **draft**. It opens directly: click **Edit** to evolve its chapters and requirements (see [Create a custom framework](custom.md)).

The **Import a new version** button in the **Versions** tab also lets you create a version from a JSON or Excel file.

The version note can be changed at any time from the version's actions menu (**Edit version note**).

{% hint style="info" %}
The versions of a framework are not counted separately in the framework quota: creating or importing a version does not consume a framework credit.
{% endhint %}

***

## Publishing, unpublishing or deleting a version

* **Publish**: from the version's actions menu, or with the **Publish** button at the top of the framework page. A published version is offered when the framework is added to a project. Several published versions of the same framework can coexist.
* **Cancel publication**: the version goes back to draft and is no longer offered when the framework is added to a project. The current version cannot be unpublished: set another version as the current version first.
* **Delete**: only a draft version can be deleted. The other versions of the framework are not affected.

{% hint style="warning" %}
The requirements of a published version are locked: the **Edit** button is disabled. To change the chapters or requirements, create a version. The name, logo and description of the framework (**Detail** tab) remain editable on a published version.
{% endhint %}

***

## Setting the current version

In the **Versions** tab, open the actions menu of a published version and click **Set as current version**.

This version becomes the one offered and installed by default when the framework is added to a project. Projects that use another version are not changed.

***

## Updating from the source referential

When a framework was created from a template and a newer version of this source referential is available:

* the framework card in the list displays the **Update available** badge,
* the framework page displays the banner _A newer version of the source referential is available_, followed by the **update** link.

Click **update** to open the **Update from the source referential** window. It shows a preview of the changes on controls, tests, risk scenarios and threats; items removed from the source referential are flagged with the **Removed from the source** label.

Click **Validate**: a published version of the framework is created from the source and becomes the current version. Earlier versions and the projects that use them are not affected.

***

## Versions and compliance projects

### Choosing the version to install

When a framework is added to a project (**Add a framework to project**), only published versions are offered. When several published versions exist, a drop-down list (**Version to install**) appears next to the framework name, with the current version preselected. The project is then attached to the installed version.

### Spotting a project to update

In the project overview, the card of each framework shows the number of the version in use. The **Update available** badge indicates that the project uses a version that is no longer the current version of the framework.

<figure><img src="../../../../.gitbook/assets/compliance-project-overview-framework-update-available.png" alt="Framework card in a project showing the version number and the Update available badge"><figcaption><p>The Update available badge flags a project attached to an earlier version of the framework</p></figcaption></figure>

### Moving a project to another version

1. In the project overview, open the actions menu of the framework card and click **Update the framework version**.
2. Choose the **Target version** among the other published versions. Its version note and a preview of the items added to the project are displayed.
3. Click **Validate**.

During the migration:

* the items introduced by the target version are added to the project,
* the labels, descriptions and tags of the existing controls, tests, risk scenarios and threats are refreshed from the target version,
* results and evidence are kept,
* controls that the target version does not include are dissociated from the requirements but remain in the project (a message shows how many before you confirm).

{% hint style="warning" %}
The migration is always manual: a project is never moved automatically to the current version. It is not possible while an audit is in progress in the project.
{% endhint %}
