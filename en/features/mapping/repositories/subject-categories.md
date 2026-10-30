---
description: >-
  Maintain the categories of data subjects, flag vulnerable persons, and see
  or import the datasets linked to each category.
---

# Categories of data subjects

A category of data subjects groups people whose data you process: employees, customers, candidates, minors, and so on. In the menu, the repository is called **Cat. of data subject**.

Create each category once here, then select it in your datasets, processing activities, data breaches and requests, so that your reports count the same populations everywhere.

## Add a category

Open **Data inventory** > **Repositories** > **Cat. of data subject**. You can:

* click **Create a new categorie of data subjects** to open an empty form;
* click the arrow next to that button, then **Create from library...** to copy categories of the library;
* import categories from a file: arrow next to the button, then **Import**. See [Import your data (Excel, Csv)](../../general/import.md).

<figure><img src="../../../.gitbook/assets/repositories-subject-categories-1.png" alt="List of categories of data subjects with the Datasets column displayed"><figcaption><p>The list of categories, with the Datasets column</p></figcaption></figure>

## Complete the category form

| Field | Content |
| --- | --- |
| **Categorie of data subjects** | The name of the category, required. |
| **Summary** | A free description. |
| **Vulnerable natural persons involved** | Tick it when the category groups people in an unbalanced situation, such as minors, employees or elderly people. |

The toolbar of the form gives access to the tasks and AI systems linked to the category, depending on your permissions and the enabled features. It also contains the processing activities that use the category, the datasets of the category (see below), the activity history and, when workflow steps are defined, the workflow step.

The actions menu of the form offers **Merge** and **Delete**. There is no **Data quality tool** for categories.

## Datasets of a category

A dataset can relate to several categories, and a category to several datasets. This link helps you find, for a given population, which data you hold, for example when you handle a [data subject request](../../requests/README.md).

* To see the datasets of a category, open its form: the button with the number of datasets lists them. Click a dataset to open it. In the list of categories, turn on the **Datasets** column in **Customize columns**: you can also filter the list by dataset.
* To link or unlink a dataset, open the dataset, then add or remove the category in its **Related subject categories** field. See [Datasets](datasets.md). The list of datasets can also be filtered by **Cat. of data subject**.
* To import the links, use the **Datasets** column of the import file of the categories. It holds the names or identifiers of datasets, separated by a pipe (`|`). Only the datasets that already exist in the workspace are linked: Dastra does not create the others.
* To export the links, the **Datasets** column is included in the export of the list.

## Find categories in the list

From a selection, you can **Switch workflow stage**, **Merge** and **Delete**.

## Where categories are used

* In a processing activity, the **Data subject** section lists the categories concerned, with their volume. See [Data subjects](../../ropa/activity/data-subjects.md).
* In datasets, through **Related subject categories**. See [Datasets](datasets.md).

{% hint style="warning" %}
Deleting a category removes all its references in processing activities, data breaches, requests to exercise rights and datasets.
{% endhint %}
