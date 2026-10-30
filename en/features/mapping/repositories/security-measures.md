---
description: >-
  List the technical and organizational measures that protect your data, then
  attach them to your assets and processing activities.
---

# Security measures

Security measures are the technical or organizational provisions put in place to protect the data: antivirus, application firewall, access controls, a clean desk policy, and so on. In the menu, the repository is called **Measures**.

Enter each measure once, with a short name, so that you can reuse it from one asset or processing activity to another. This information often appears in the DPA signed with a publisher.

## Add a security measure

Open **Data inventory** > **Repositories** > **Measures**. Click **New security measure**, then choose:

* **Create from scratch**, to start from an empty form;
* **Use a template**, to copy a measure from the library or from another workspace;
* **Generate with AI**, to describe the measure and let the assistant draft it (this option depends on the features enabled for your organization).

The arrow next to **New security measure** also offers **Create from library...**, **Import** and **Data quality tool**. See [Import your data (Excel, Csv)](../../general/import.md).

<figure><img src="../../../.gitbook/assets/repositories-security-measures-1.png" alt="Form of a security measure with its name, type and description"><figcaption><p>The form of a security measure</p></figcaption></figure>

## Complete the security measure form

| Field | Content |
| --- | --- |
| **Name of the measure** | The name of the measure, required. |
| **Internal reference** | Your reference. |
| **Type** | **Technical**, **Organizational**, **Physical** or **People**. |
| **Describe this measure** | A free description. |
| **Purpose of the measure** | What the measure is for and the potential risk it addresses. |
| **URL related to the measure** | The address of its documentation, for example on the CNIL website. |

You can add [tags](../../general/tags.md), and the [custom fields](../../general/custom-fields.md) defined for measures appear in the form.

The toolbar of the form gives access to the attached documents, questionnaires and tasks linked to the measure, depending on your permissions and the enabled features. It also contains:

* **Linked elements**: the [generic relationships](../relationships.md) of the measure;
* **Related processing**: the processing activities that use the measure, with the **Associate with data processing** button to add more;
* **Activity history**;
* the workflow step of the measure, when workflow steps are defined.

The actions menu of the form offers **Create a copy**, **Merge** and **Delete**.

## Find security measures in the list

The filters are **Filter by tags** and **Types**. Turn on **View orphans** to list the measures that are attached to neither an asset nor a processing activity.

From a selection, you can **Switch workflow stage**, **Edit fields...**, **Merge**, **Export** and **Delete**. See [Merging elements](../../general/merge.md).

## Where security measures are used

* In an asset, the **Attached security measures** section lists the measures of the asset. See [Assets](assets.md).
* In a processing activity, you select the measures that protect the processing and give their deployment status. See [Security measures](../../ropa/activity/security.md).

{% hint style="warning" %}
Deleting a measure permanently removes its references in all processing activities and attachments.
{% endhint %}
