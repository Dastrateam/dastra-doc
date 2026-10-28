---
description: Learn how to edit the record of processing.
---

# Record of processing activities

## Introduction

The record of processing activities allows you to map your **data processing** and to have **an overview** of what you do with the personal data concerned. Keeping a complete record is a **requirement** of Article 30 of the GDPR, but beyond the legal obligation, it is above all **a tool to better understand your data** and **control the associated value chain**, from the moment the data is produced to the way it is used.

Dastra provides a record and **questionnaires** that guide you step by step as you map your processing activities.

## The Dastra record in a few words

Dastra's record of processing activities meets all regulatory requirements. Both records, the data controller record and the data processor record, rely on repositories (stakeholders, assets, datasets, data, risks and security measures) that allow you **to map your processing activities** and **save time** in your day-to-day management.

Processing activities can be copied, and processing activity templates are available in a library freely accessible to all our users. A workflow is built in, a search function is available natively, and you can export processing activities in different formats (PDF, Word, HTML, Excel, CSV, JSON, Markdown) and import them from CSV, Excel or JSON files. You can also attach documents, data breaches or risks to your processing activities.

<figure><img src="../../.gitbook/assets/ropa-readme-1.png" alt="Record of processing activities list with its indicator tiles and toolbar"><figcaption><p>The record of processing activities: indicator tiles at the top, then the list of processing activities</p></figcaption></figure>

## "Data controller" record versus "Data processor" record

Article 30 of the GDPR sets out specific obligations for the _controller's record_ and the _processor's record_. If your organization acts as both a processor and a controller, your record must therefore clearly distinguish the two categories of activities.

**In practice, in this case, the French CNIL recommends that you keep 2 records:**

1. one for the processing of personal data for which you yourself are responsible,
2. another for the processing operations that you carry out, as a processor, on behalf of your clients.

{% content-ref url="controller.md" %}
[data-controller-record.md](controller.md)
{% endcontent-ref %}

{% content-ref url="processor.md" %}
[data-processor-record.md](processor.md)
{% endcontent-ref %}

## The different methodologies for setting up the record of processing activities

There are two methodologies for creating a processing record:

* **Top-Down design**: you start the project by drawing up the inventory of data processing activities, and then you collect the information specific to each processing activity (data, processors, etc.).
* **Bottom-Up design**: you start by making an inventory of the data (software, datasets and personal data fields) and you create the processing activities from it.

### Which record methodology to choose?

There is no right or wrong method: everything depends on the context of your organization, the skills of the DPO team, how easily you can reach the people who operate the data...

Here is a table comparing the two approaches:

<table><thead><tr><th width="129">Methodology</th><th width="178">Target</th><th>Benefits</th><th>Disadvantages</th></tr></thead><tbody><tr><td><strong>Top-Down</strong></td><td>Small organizations or local authorities<br>Companies with a weak data culture<br>Legal team with little affinity for IT</td><td>Quick to set up<br>Less work<br>Matches the legal expectations of the GDPR well</td><td>May cause difficulties if the team setting up the record does not know the organization's data<br>More demanding for operational staff<br>The data inventory is much less valuable because it is modeled for legal purposes only<br>More complex to maintain over the long term</td></tr><tr><td><strong>Bottom-Up</strong></td><td>Large or medium-sized organizations<br>With a strong data culture<br>Legal team with a strong IT affinity</td><td>Taking an inventory of the data is less abstract than creating processing activities directly<br>The record reflects the reality of the organization<br>The record is easier to maintain in the long run<br>More members of the organization are involved<br>Creating processing activities is more automated</td><td>Overall more difficult and time-consuming to implement<br>The project requires good governance</td></tr></tbody></table>

Dastra supports both approaches. For a top-down approach, create processing activities [from templates](templates.md). If you prefer the bottom-up approach, you can [build your data map](../mapping/README.md) first and then create a processing activity directly from an asset (software, database).

## How to set up your processing activity record?

If you want to learn how to design and manage your record of processing activities, start here:

{% content-ref url="establish.md" %}
[establish-your-record.md](establish.md)
{% endcontent-ref %}

If you want to learn how to design and manage one of your processing activities, start here:

{% content-ref url="declare.md" %}
[declare-a-treatment.md](declare.md)
{% endcontent-ref %}

If you want to understand the different stages of the questionnaire, click here:

{% content-ref url="activity/README.md" %}
[remplir-le-questionnaire](activity/README.md)
{% endcontent-ref %}

If you want to learn how to share the record of processing, click here:

{% content-ref url="share.md" %}
[partager-le-registre.md](share.md)
{% endcontent-ref %}

## How to act on several processing activities at once?

In **List view**, tick the boxes on the left of the processing activities you want to work on. The **Select a batch action** button then appears above the list. Depending on your permissions and on the features enabled in your workspace, it offers the following actions:

* **Switch workflow stage**
* **Export**
* **Linking stakeholders**: add or remove stakeholders or recipients on all the selected processing activities
* **Edit fields...**: change the value of one or more fields on all the selected processing activities
* **Merge**: see [Merging elements](../general/merge.md)
* **Send questionnaires**
* **Review**
* **Share**
* **Move to recycle bin**

## For more information

{% content-ref url="../../gdpr/concepts/ropa.md" %}
[record-of-processing-activities.md](../../gdpr/concepts/ropa.md)
{% endcontent-ref %}

{% content-ref url="../risks/attach-to-processing.md" %}
[attach-a-risk-to-a-processing-activity.md](../risks/attach-to-processing.md)
{% endcontent-ref %}

{% content-ref url="../tasks/README.md" %}
[planifier](../tasks/README.md)
{% endcontent-ref %}
