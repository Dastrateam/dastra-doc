---
description: >-
  Maintain the list of data fields, the most atomic level of the data mapping,
  with their category and sensitivity level.
---

# Data glossary

A data field is a piece of information, such as a name, an email address or a health record number. It is the most atomic level of the mapping: [datasets](datasets.md) are made of data fields.

List each field once in this glossary, so that every dataset describes the same data in the same way.

## Add a data field

Open **Data inventory** > **Repositories** > **Data glossary**. You can:

* click **Create a data field** to open an empty form;
* click the arrow next to **Create a data field**, then **Create from library...** to copy fields of the library;
* import fields from a file: arrow next to **Create a data field**, then **Import**. See [Import your data (Excel, Csv)](../../general/import.md).

You can also create a field directly from the **Data fields** section of a dataset.

## Complete the data field form

| Field | Content |
| --- | --- |
| **Name** | The name of the field, required. |
| **Internal reference** | Your reference. |
| **Category of data** | The category of personal data the field belongs to. |
| **Sentivity level** | **Standard** (name, first name, phone number), **Data of a highly personal nature** (financial data, location, communications) or **Special categories (sensitive)** (racial or ethnic origin, political opinions, religion, health, sexual orientation). |
| **Lawful basis for collection**, **Justification for collecting sensitive personal data** | Displayed for the **Special categories (sensitive)** level only: the lawful basis chosen in the list, and your justification. |
| **Description of the data**, **Technical description** | A free description, and the technical definition of the field. |
| **Data type** | The generic type of the data. |

The [custom fields](../../general/custom-fields.md) defined for data fields are added to the form. The toolbar gives access to the comments and tasks linked to the field, to the activity history and, when workflow steps are defined, to the workflow step. The button with the database icon lists the datasets that contain the field.

The actions menu of the form offers **Merge** and **Delete**.

## Find data fields in the list

The filters are **Category of data** and **Data types**. The **Datasets** column, hidden by default in **Customize columns**, can be filtered with **Is empty** or **Is not empty**: use it to find the fields that belong to no dataset.

From a selection, you can **Switch workflow stage**, **Edit fields...**, **Merge**, **Export** and **Delete**. **Data quality tool**, in the menu of **Create a data field**, detects duplicates. See [Merging elements](../../general/merge.md).

## Where data fields are used

Data fields reach your processing activities through datasets. See [Datasets and retention](../../ropa/activity/datasets.md), where you can also add the fields of a dataset to a processing activity.

{% hint style="warning" %}
Deleting a data field permanently removes all its references to datasets. The linked conversations are deleted.
{% endhint %}
