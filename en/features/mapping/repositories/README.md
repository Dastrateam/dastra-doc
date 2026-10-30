---
description: >-
  The record of processing activities relies on repositories: assets,
  stakeholders, datasets, data fields, security measures and categories of data
  subjects. Dastra lets you manage them separately from the record to limit
  data entry errors.
---

# Repositories

To limit data entry errors, Dastra lets you manage repositories independently from the record of processing activities. The processing activities of the record then reuse the elements of these repositories.

## Access the repositories

In the side menu, under **Data inventory**, click **Repositories**. The menu offers:

* **Overview**: the number of elements in each repository.
* **Graphs**: a graphic representation of your assets and stakeholders.
* **Assets**, **Stakeholders**, **Datasets**, **Data glossary**, **Measures** and **Cat. of data subject**: the six repositories.

What you can do depends on the data mapping and repositories permissions of your role. See [Roles and permissions](../../settings/roles.md).

## The six repositories

* [Assets](assets.md): data media, premises, and tangible or intangible equipment.
* [Stakeholders](stakeholders.md): the companies and people linked to your processing, which do not need to sign in to the platform.
* [Datasets](datasets.md): groups of data fields that form coherent sets, with their retention rules.
* [Data glossary](data-glossary.md): the data fields, the most atomic level in Dastra.
* [Security measures](security-measures.md): the technical or organizational provisions that protect the data. The menu entry is **Measures**.
* [Categories of data subjects](subject-categories.md): the groups of individuals whose data you process. The menu entry is **Cat. of data subject**.

Each page describes the fields of the form, how to create, import and merge elements, and where the repository is used. How a processing activity uses these elements is described once, in the pages of the activity: see [Complete a data processing activity](../../ropa/activity/README.md).

## Features shared by the lists

The lists of the six repositories share several features:

* **Create from library...** adds an element from the template library. For most repositories, an AI button next to the create button drafts an element from a short description, when the feature is enabled for your organization.
* **Import** adds elements from a file. See [Import your data (Excel, Csv)](../../general/import.md).
* **Export** exports the list, or only the selected lines.
* **Data quality tool** detects duplicates, and **Merge** combines them. The data quality tool does not exist for categories of data subjects. See [Merging elements](../../general/merge.md).
* Filters, custom columns and custom views. See [Advanced filters](../../general/filters.md).
* Bulk actions on a selection of lines. See [Lists, bulk actions and recycle bin](../../general/lists.md). **Edit fields...**, where it is offered, changes the same field on all the selected elements.
* The table and card views, for assets and stakeholders.

In the repositories, **Delete** asks for confirmation and deletes the element permanently: the recycle bin described in the lists page does not apply.

The forms also share the [custom fields](../../general/custom-fields.md), except for categories of data subjects, and, in the toolbar, the [generic relationships](../relationships.md) of the element, where it is offered.

## Overview and graphs

The **Overview** page shows one card per repository with its number of elements. Click a card to open the matching list. The **Add an asset** button creates an asset from this page.

The **Graphs** page offers four representations, which you choose in the drop-down list at the top left:

* **Node mapping**: a graph of assets, their publishers, their datasets and their tags. [Generic relationships](../relationships.md) appear as links.
* **Mapping of stakeholders**: a graph of stakeholders, their assets and their subsequent processors, which you can filter by **Responsibility**.
* **Sankey diagram**: a diagram of the distribution of data by asset, which you can filter by type (data fields, processing activities, owners, countries, data categories).
* **Hierarchy chart**.

The **Print** and **Refresh** buttons are available at the top of the page.
