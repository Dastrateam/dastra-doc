---
description: >-
  Keep your organization's record of incidents and data breaches, track
  notification deadlines and view the statistics.
---

# Incidents and data breaches

The **Incidents** module of Dastra documents security incidents that affect personal data, tracks the notifications to the supervisory authority and to the data subjects, and keeps a record of every incident. It is meant for data protection officers (DPOs), security teams and legal departments.

To learn what a personal data breach is and what your obligations are, read the [Data breach notifications](../../gdpr/concepts/breaches.md) page.

## Why keep a record of breaches

Article 33(5) of the GDPR requires every organization to document all personal data breaches: the facts, their effects and the measures taken. This applies even when the breach is not notified to the supervisory authority.

The record also helps you meet notification deadlines and identify preventive measures. For more information, see the [dedicated page of the Dastra website](https://www.dastra.eu/en/product-features/data-breach).

## Open the record of incidents

In the left-hand menu, open **Operations** > **Incidents** > **Record of incidents**.

<figure><img src="../../.gitbook/assets/incidents-readme-1.png" alt="Left-hand menu with the Operations group and the Incidents entry expanded"><figcaption><p>The Incidents module in the left-hand menu</p></figcaption></figure>

The module only appears if the feature is enabled for your organization and your role gives access to incidents.

## Read the record

The record lists the incidents of the workspace, one per row.

<figure><img src="../../.gitbook/assets/incidents-readme-2.png" alt="Record of incidents with the indicator bar above the table"><figcaption><p>The record of incidents</p></figcaption></figure>

### Indicator bar

Above the table, an indicator bar counts the incidents:

* **Total**, **In progress** (Active status) and **Closed**;
* **Without risk analysis** and **With sensitive data**;
* **With an AI system**, if the AI systems module is enabled.

Click an indicator to filter the table on the incidents it counts.

### Columns and filters

You choose the columns of the table. The **Authority control notification** column shows, for each incident whose notification is mandatory, the number of hours left (green badge) or overdue (red badge), then **You have notified the data protection authority** once the notification is recorded. When no notification is needed, the cell shows **Notification is not mandatory**.

The filters include the organizational unit, tags, **Incident types**, **Status** (New, Active, Closed), **Type** (processor or data controller), the workflow **Steps** and the **Incident Manager**. Tick **With notification** to keep only the incidents that were notified, or **Linked to an AI system** for the incidents that involve an AI system. For advanced filters and custom views, see [Advanced filters](../general/filters.md).

### Actions on incidents

* Click a row to open the incident.
* The menu at the right of a row offers **Edit**, **Edit fields...** and **Move to recycle bin**.
* Tick several rows to act on the selection: **Switch workflow stage**, **Edit fields...**, **Export**, **Share** or **Move to recycle bin**.
* The **Create an incident** button creates an incident. Its arrow opens a menu with **Import**, **Export**, **Share** and **Read the documentation**.

### Recycle bin

**Move to recycle bin** removes the incident from the record without erasing it. Tick **View recycle bin** to display the incidents in the bin, then choose **Restore** to put them back in the record or **Delete** to erase them.

{% hint style="warning" %}
**Delete** erases the incident permanently. Article 33(5) still requires you to be able to justify every breach: do not delete the trace of a breach that you must document.
{% endhint %}

## View the statistics

Open **Operations** > **Incidents** > **Reporting** for an overview of the record. The **Print** button produces a printable version of the page.

<figure><img src="../../.gitbook/assets/incidents-readme-3.png" alt="Incidents Reporting page with the indicators and the charts"><figcaption><p>The Reporting page of the incidents</p></figcaption></figure>

The page shows:

* indicators: **Total number of data breaches**, **With a written post-mortem**, **With risk analysis**, **Without risk analysis**, **With sensitive data** and **With an AI system**;
* the charts **Workflow stages breakdown**, **Tags breakdown**, **Role breakdown** and **Incidents by organisational units**.

## Go further

{% content-ref url="document-breach.md" %}
[Document a new data breach](document-breach.md)
{% endcontent-ref %}

{% content-ref url="as-processor.md" %}
[Incidents as a processor](as-processor.md)
{% endcontent-ref %}

{% content-ref url="export.md" %}
[Export your data breaches](export.md)
{% endcontent-ref %}
