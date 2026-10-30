---
description: >-
  Inventory the software, servers and other media that hold your personal
  data, describe each asset and create a processing activity from it.
---

# Assets

Assets are the elements that help you manage data: data media, premises, and tangible or intangible equipment. This repository lists the assets, internal or external to the organization (applications, resources, buildings, etc.).

Use it to record the applications, software and other items that serve as data media. For example, if you use customer relationship management software such as a CRM, add it to this list. You then keep control of your data media and link them to your data catalog.

{% hint style="info" %}
Assets are not necessarily linked to processors. For example, an asset can be software installed on your own server, with no involvement of its publisher in the processing of personal data.
{% endhint %}

## Add an asset

To add an asset, you can:

* start from a template: click the arrow next to the **Add an asset** button, then **Create from library...**;
* use AI: click the AI button to the left of **Add an asset**, or choose **AI generated** in the creation window (this option depends on the features enabled for your organization);
* create the asset directly in the repository: click **Add an asset**, then choose **Personalized**;
* import assets from an Excel, CSV or JSON file: click the arrow next to the **Add an asset** button, then **Import**. See [Import your data (Excel, Csv)](../../general/import.md);
* create the asset from a questionnaire: this requires a questionnaire template of type **Asset creation**. See [Create a questionnaire template](../../questionnaires/templates/README.md).

## Complete the asset form

The form of an asset groups the following information.

| Section | Field | Content |
| --- | --- | --- |
| **General information** | **Name**, **Internal reference** | The name of the asset and your internal reference. |
| | **Organizational unit** | The unit the asset belongs to. See below. |
| | **Type of asset** | The type of asset, required. |
| | **Asset owner** | The user in charge of implementing the asset. The owner is preferably assigned to the questionnaires and tasks linked to the asset. |
| | **Publisher** | The organization that publishes, hosts or manages the asset. It can be referenced as a processor when the asset is mentioned in a processing activity. Example: the publisher of Office 365 is Microsoft. |
| | **Description**, **Privacy policy url** | A free description and the address of the asset's privacy policy. |
| | **Software type**, **Software status**, **Hosting type**, **Development type**, **Support type**, **Maintenance type** | These six fields appear when the type of asset is **Software**. |
| **Data localization** | **Country**, **Address**, **City**, **State/Province/Region**, **Postcode** | Where the asset is located. |
| | **Data localization information** | Free text to specify where the data is hosted. |
| **Datasets** | | The datasets held in the asset. Save the asset once before you create them. |
| **Attached security measures** | | The security measures of the asset, often named in the DPA. Prefer short names so that you can reuse them from one asset to another. |

The [custom fields](../../general/custom-fields.md) defined for assets are added to this form.

The toolbar of the form gives access to the attached documents, comments, questionnaires, tasks, contracts, AI systems and risks linked to the asset, depending on your permissions and the enabled features. It also contains:

* **Linked elements**: the [generic relationships](../relationships.md) of the asset, with their number;
* **Related processing**: the number of processing activities that use the asset, and their list;
* **Activity history**: the successive changes to the form, which you can restore;
* the regular review of the asset. See [Regular review (freshness)](../../regular-review.md).

## Create a processing activity from an asset

This action reuses the information of the asset to prepare a processing activity, so you do not enter it again.

1. Open the asset.
2. In the actions menu of the form, click **Create a data processing from an asset**.
3. If processing activities have been suggested for this asset, choose one from the list, or click **Skip this step**.
4. Enter the **Data processing label**, choose the **Organisational unit of destination**, then click **Next**.
5. Select the datasets of the asset to reuse in the processing activity, then click **Next**.
6. Check the **Summary**: label, description, datasets, security measures, purposes and data subjects. Click **Create processing**.

To link assets to an existing processing activity afterwards, see the [Assets](../../ropa/activity/assets.md) page of the processing activity.

## Create a copy, merge and delete

The actions menu of the form offers **Create a copy**, **Merge** and **Delete**. From the list, **Data quality tool** detects duplicate assets. See [Merging elements](../../general/merge.md).

## Attach an asset to an organizational unit

By default, an asset created in Dastra is available to the whole organization (global scope). You can attach an asset to a specific organizational unit to limit its visibility to the users of that entity or department.

To do so, when you create or edit the asset, select the organizational unit in the **Organizational unit** field. The asset is then visible only to users who have access to that organizational unit.
