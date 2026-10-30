---
description: >-
  Record the companies and people you work with (processors, publishers,
  recipients, DPO, customers), their sub-processors and the assets they
  publish.
---

# Stakeholders

Stakeholders are the companies and individuals linked to your data processing: processors, software publishers, AI model providers, joint controllers, public bodies, customers, and so on. Unlike users, they do not sign in to Dastra.

Enter each stakeholder once in this repository. Assets, processing activities, contracts and data breaches then reference it, so a change to its details applies everywhere.

## Add a stakeholder

Open **Data inventory** > **Repositories** > **Stakeholders**. You can:

* click **Create stakeholder**, then choose **Built-in template** to start from a template of the library, or **Personalized** to start from scratch;
* click the AI button to the left of **Create stakeholder** to describe the stakeholder and let the assistant draft it (this option depends on the features enabled for your organization);
* click the arrow next to **Create stakeholder**, then **Create from library...**;
* import stakeholders from a file: arrow next to **Create stakeholder**, then **Import**. See [Import your data (Excel, Csv)](../../general/import.md);
* turn emails into stakeholders: arrow next to **Create stakeholder**, then **Transform emails to stakeholders**. This opens the incoming mail integration of the workspace settings.

<figure><img src="../../../.gitbook/assets/repositories-stakeholders-1.png" alt="List of stakeholders with the Create stakeholder menu open"><figcaption><p>The list of stakeholders</p></figcaption></figure>

## Complete the stakeholder form

| Section | Field | Content |
| --- | --- | --- |
| **General information** | **Person** or **Company** | The nature of the stakeholder. The name field is **Full name** for a person and **Company's name** for a company, required. |
| | **Internal reference**, **Organizational unit** | Your reference, and the unit that can see the stakeholder. Without a unit, all units see it. |
| | **Stakeholder owner** | The user in charge of the stakeholder. |
| | **Description/Biography**, **Website url** | A free description and the address of the website. |
| | **Company registration number** | Company only. When the SIRET integration is enabled, you can search the SIRET database and the address is filled in for you. |
| | **Address** | **Country**, **Address**, **City**, **Postcode** and **State/Province/Region**. |
| | **Contact details** | **Contact name**, **Contact job title**, **Contact email** and **Contact phone number**. |
| **Subsequent processors** | | The sub-processors of the stakeholder, often named in the DPA. Select them in the list or create them, then enter the **Data location country** and a description for each. This maps the whole subcontracting chain. |
| **Related assets** | | The assets published by the stakeholder. Selecting an asset makes the stakeholder its **Publisher**: if the asset already has another publisher, Dastra asks you to confirm the replacement. |

The [custom fields](../../general/custom-fields.md) defined for stakeholders are added to the form, and you can attach a logo and [tags](../../general/tags.md).

The toolbar of the form gives access to the attached documents, comments, questionnaires, tasks, contracts and risks linked to the stakeholder, depending on your permissions and the enabled features. It also contains:

* **Linked elements**: the [generic relationships](../relationships.md) of the stakeholder;
* **Related processing**: the processing activities that use the stakeholder, with a **Link to data processing** button to add more;
* **Activity history**;
* the regular review of the stakeholder. See [Regular review (freshness)](../../regular-review.md);
* the workflow step of the stakeholder, when workflow steps are defined.

The actions menu of the form offers **Create a copy**, **Merge**, **Export** and **Delete**.

## Find stakeholders in the list

Besides the filters described in [Repositories](README.md), the list offers:

* the **Responsibility** filter: software publisher (publisher of at least one asset), AI model provider (publisher of at least one AI model), or recipient in a processing activity (processor, joint controller, public body, etc.);
* the **Type**, **Country**, **Steps** and **Filter by tags** filters, and the organizational unit;
* the table and card views;
* the **Subsequent processors** and **Related contracts** columns, hidden by default, in **Customize columns**.

From a selection, the bulk actions include **Link to data processing**, **Send questionnaires**, **Review**, **Merge** and **Export**.

## Where stakeholders are used

* In a processing activity, a stakeholder can be a data controller, a joint controller, a processor or another recipient. See [Stakeholders](../../ropa/activity/stakeholders.md) and [Recipients](../../ropa/activity/recipients/README.md) of the activity.
* As the **Publisher** of an asset. See [Assets](assets.md).
* In contracts, data breaches, risks and questionnaires.

{% hint style="warning" %}
Deleting a stakeholder removes its references in processing activities (recipients, data controller, stakeholder), incidents, organizational units and discussions. Tasks, questionnaires and attached files are kept.
{% endhint %}
