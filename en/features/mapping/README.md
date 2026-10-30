---
description: Learn how to map your organization's personal data in Dastra
---

# Data Mapping

## It all starts with data mapping

Before you create your processing activities, map your organization's data as accurately as you can. In the application, this module is called **Repositories**. The mapping links four kinds of elements: the publisher of an asset, the asset itself, the security measures applied to it, and the datasets it holds, which are made of data fields.

<figure><img src="../../.gitbook/assets/mapping-schema-1.png" alt="Data mapping diagram: the publisher provides assets, which are linked to security measures and to datasets made of fields"><figcaption><p>Structure of the data mapping</p></figcaption></figure>

To inventory all the personal data of your information system, follow this procedure:

1. **Identify the assets**: software, files, plugins, servers, machines, etc.
2. **Identify the publisher of the asset, if applicable**: enter the details of the company that produces this asset. It can then be listed among your processors when you build the record of processing activities.
3. **Inventory the data**: list the associated datasets (you can refer to the DPA signed with the processor). For more information, see [Datasets and retention](../ropa/activity/datasets.md).
4. **List the security measures** in place.

This mapping makes it easier to create processing activities, because you start from the reality of your data.

If you prefer not to build this inventory, or if the software you use is standard, create your asset repository from the library of predefined templates, which contains common assets on the market (Salesforce, Jira, etc.).

## Access the data mapping

1. [Open your workspace](../../getting-started/setup/workspace.md#access-a-workspace).
2. In the side menu, under **Data inventory**, click **Repositories**.
3. The **Overview** page opens: one card per repository, with the number of elements it contains.

Then click the repository you want to open. For the access path, the list features shared by all repositories and the graphs, see [Repositories](repositories/README.md).

## The repositories of the mapping

Each repository has its own page:

* [Assets](repositories/assets.md): the software, servers and other media that hold your data.
* [Stakeholders](repositories/stakeholders.md): the processors, publishers and other companies and people you work with, and their sub-processors.
* [Datasets](repositories/datasets.md): the groups of data fields, with their retention rules.
* [Data glossary](repositories/data-glossary.md): the data fields, with their category and sensitivity level.
* [Security measures](repositories/security-measures.md): the technical and organizational measures that protect the data.
* [Categories of data subjects](repositories/subject-categories.md): the groups of people whose data you process.

To document a connection that the platform does not infer, for example an asset linked to a stakeholder, see [Generic relationships](relationships.md). To reuse these repositories in your record, see [Record of processing activities](../ropa/README.md).

## Build your list of security measures

Security measures have their own repository (see [Security measures](repositories/security-measures.md)): enter them once, then attach them to assets in the **Attached security measures** section of the asset form. This information often appears in the DPA signed with the publisher. Prefer short names (Antivirus, Application firewall, Access controls) so that a measure can be reused from one asset to another.

## Manage your processors

A processor is a [stakeholder](repositories/stakeholders.md) in your mapping. Enter it as the **Publisher** of the asset: it can then be referenced as a processor when the asset is mentioned in a processing activity. On the stakeholder form, you can also save the processor's sub-processors, to map the whole subcontracting chain.
