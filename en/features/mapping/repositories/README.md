---
description: >-
  The record of processing activities relies on repositories: assets,
  stakeholders, datasets and security measures. Dastra lets you manage them
  separately from the record to limit data entry errors.
---

# Repositories

To limit data entry errors, Dastra lets you manage one or more repositories independently from the record of processing activities. The processing activities of the record then reuse the elements of these repositories.

## Access the repositories

In the side menu, under **Data inventory**, click **Repositories**. The menu offers:

* **Overview**: the number of elements in each repository.
* **Graphs**: a graphic representation of your assets and stakeholders.
* **Assets**, **Stakeholders**, **Datasets**, **Data glossary**, **Measures** and **Cat. of data subject**: the six repositories.

## Repositories provided by Dastra

* **Assets**: assets are the elements that help you manage data, such as data media, premises, and tangible or intangible equipment. See [Assets](assets.md).
* **Stakeholders**: stakeholders differ from users because they do not need to sign in to the platform.
* **Datasets**: datasets are groups of data that form coherent sets, with their retention rules.
* **Data glossary**: data fields are the pieces of information. They are the most atomic level in Dastra.
* **Measures**: security measures are the technical or organizational provisions put in place to protect the data.
* **Cat. of data subject**: categories of data subjects group categories of individuals.

## Features shared by the lists

The lists of the six repositories share several features:

* **Create from library...** adds an element from the template library.
* **Import** adds elements from a file. See [Import your data (Excel, Csv)](../../general/import.md).
* **Export** exports the list.
* **Data quality tool** detects duplicates, and **Merge** combines them. The data quality tool does not exist for categories of data subjects. See [Merging elements](../../general/merge.md).

## Overview and graphs

The **Overview** page shows one card per repository with its number of elements. Click a card to open the matching list. The **Add an asset** button creates an asset from this page.

The **Graphs** page offers four representations, which you choose in the drop-down list at the top left:

* **Node mapping**: a graph of assets, their publishers, their datasets and their tags. [Generic relationships](../relationships.md) appear as links.
* **Mapping of stakeholders**: a graph of stakeholders, their assets and their subsequent processors, which you can filter by **Responsibility**.
* **Sankey diagram**: a diagram of the distribution of data by asset, which you can filter by type (data fields, processing activities, owners, countries, data categories).
* **Hierarchy chart**.

The **Print** and **Refresh** buttons are available at the top of the page.

## What is specific to each repository

### Stakeholders

A stakeholder can be attached to an organizational unit, which limits its visibility to the users of that unit. The **Create stakeholder** button offers to start from a template (**Built-in template**) or from scratch (**Personalized**).

On the form, the **Subsequent processors** section lets you save the organization's sub-processors, often named in the DPA, and map the whole subcontracting chain.

In the list, the **Responsibility** filter finds stakeholders according to how you use them: software publisher (publisher of at least one asset), AI model provider (publisher of at least one AI model), or recipient in a processing activity (processor, joint controller, public organism, etc.).

### Datasets

A dataset groups data fields, sensitive or not, with the retention rules that apply to their life cycle: paper pay slips or customer records in a CRM, for example. Fill in the **Data source origin**, the **Active database retention** and the **Archived database retention**, then add the data in **Data fields**.

The **View orphan** filter lists the datasets that are not attached to any asset. You can attach them from the **Linked asset** field.

### Data glossary

Each data field has a **Sentivity level**:

* **Standard**, for example name, first name or phone number.
* **Data of a highly personal nature**, for example financial data, location or communications.
* **Special categories (sensitive)**, for example racial or ethnic origin, political opinions, religion, health or sexual orientation.

The **Special categories (sensitive)** level displays the **Lawful basis for collection** field. The **Datasets** column, hidden by default, can be filtered with **Is empty** or **Is not empty**: use it to find the data fields that belong to no dataset.

### Measures

A measure has a name, a **Type** and, optionally, the address of its documentation, for example on the CNIL website. The **View orphans** filter lists the measures that are attached to neither an asset nor a processing activity.

### Categories of data subjects

A category has a name and a **Vulnerable natural persons involved** option. Tick it when the category groups people in an unbalanced situation, such as minors, employees or elderly people.
