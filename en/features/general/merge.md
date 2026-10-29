---
description: >-
  The merge tool combines items that are duplicates or very similar, and the
  data quality tool finds them for you.
---

# Merging elements

## What the merge tool does

Dastra's **item merge** feature combines several identical or similar items into a single one, without you having to link each of the associated entities (processing activities, controllers, records, etc.) by hand. It keeps your repository consistent and limits manual handling.

## Which elements can be merged

The merge tool is available for:

* Processing activities
* Assets
* Stakeholders
* Datasets
* Data fields (data glossary)
* Security measures
* Categories of data subject
* Tasks
* Compliance controls (applied controls and reference controls)
* Compliance tests (operational tests and reference tests)
* Risk scenarios and threats of the compliance library

{% hint style="info" %}
Controls, tests, risk scenarios and threats are merged from the library or the project of the Compliance module. For the details of this operation, see the [Controls](../compliance/library/controls.md), [Tests](../compliance/library/tests.md), [Risks](../compliance/library/risks.md) and [Threats](../compliance/library/threats.md) pages.
{% endhint %}

## Merge elements

1. In the list, select the elements to merge. Select fewer than 30 elements.
2. Click **Select a batch action**, then **Merge**.

<figure><img src="../../.gitbook/assets/general-merge-1.png" alt="List with two elements selected and the Select a batch action menu open on Merge"><figcaption><p>Two elements selected and the Merge batch action</p></figcaption></figure>

3. In the **Merging tool** window, choose the element to keep by selecting it in the header of its column: it becomes the **Reference version**. The other columns show the **Keep selected fields** badge: those elements are deleted once the merge is confirmed, and only the fields you select in them are carried over to the reference version.
4. For each field that differs, select the value to keep.
5. Click **Merge**.

<figure><img src="../../.gitbook/assets/generalites-fusion-tool-differences.png" alt="Merging tool window with the reference version and the differing fields"><figcaption><p>The Merging tool window</p></figcaption></figure>

You can also start from a single element: in its actions menu, click **Merge**, select the objects to merge the data with, then click **Next**.

To choose the values to keep more quickly:

* each field whose value differs from one element to another is marked **Different**, and a counter shows the number of rows concerned;
* the table only shows the rows that differ; turn on **View all fields** to show all the comparable fields. Hidden identical fields keep the value of the reference version;
* the **Select all** button, under a column header, keeps its values on all the rows that differ; **Undo selection** reverts it. An empty value never replaces a filled-in value.

{% hint style="info" %}
The entities associated with the deleted elements (processing activities, analyses, tasks, etc.) are automatically re-attached to the reference version, with no loss or disconnection in your record. The **Linked objects kept** section of the window shows how many there are.
{% endhint %}

When an object is updated from the answers to a questionnaire, the same window opens with a **Questionnaire’s responses** column. The existing object always remains the reference version: it keeps its identifier, its history and its links.

## Data quality tool

The **data quality tool** scans your repository for items that are probably duplicates, without any prior selection. It then offers to merge them with the merge tool.

### Where to find it

The tool is available on the lists of processing activities, stakeholders, assets, data fields, datasets and security measures. It is not offered for categories of data subject, which can still be merged from the list.

In the list, click the arrow of the create button at the top right (for example **Create data processing**), then **Data quality tool**. This action requires write access to the module.

### Smart detection

The **Smart detection** tab runs a similarity analysis (Levenshtein distance and Jaccard index) and stores the probable duplicates as suggestions. The analysis starts on its own the first time you open the tab; click **Run analysis** to run it again.

<figure><img src="../../.gitbook/assets/general-merge-2.png" alt="Smart detection tab of the data quality tool with the list of suggestions, their confidence score and their actions"><figcaption><p>The duplicate suggestions of the Smart detection tab</p></figcaption></figure>

Each suggestion pairs two records (**Record A** and **Record B**). The algorithm mostly compares the label, then, depending on the type of element, the description, address, email, phone number or definition. It derives a **Confidence** score from 0% to 100% that you can read before merging anything. A red **Different area** icon flags two records attached to different organizational units.

For each suggestion:

* **Merge** opens the merge tool with the two records;
* **Dismiss** sets the suggestion aside: its status becomes **Dismissed** and the analysis does not propose it again;
* **Reset to pending** puts a dismissed suggestion back among the **Pending** ones.

You can filter the list by status (**All statuses**, **Pending**, **Dismissed**). The tool never deletes a duplicate on its own: only the elements you do not keep during a merge are deleted.

### Exact match

The **Exact match** tab groups the records that have the same value in the column of your choice. Select the column, then click **Merge** next to a group to open the merge tool.
