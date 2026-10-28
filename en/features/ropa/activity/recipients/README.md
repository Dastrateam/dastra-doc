---
description: Indicate who are the recipients of the data processing in the activity.
---

# Recipients

[**Article 30 1. d) of the GDPR**](https://gdpr-info.eu/art-30-gdpr/) requires the record to include "_the categories of recipients to whom the personal data have been or will be disclosed including recipients in third countries or international organisations_".

[**Article 4 of the GDPR**](https://gdpr-info.eu/art-4-gdpr/) defines the recipient as "_a natural or legal person, public authority, agency or another body, to which the personal data are disclosed, whether a third party or not. However, public authorities which may receive personal data in the framework of a particular inquiry in accordance with Union or Member State law shall not be regarded as recipients; the processing of those data by those public authorities shall be in compliance with the applicable data protection rules according to the purposes of the processing_".

In other words, the term recipients covers all the entities that will access the data, other than public authorities (authorized third parties such as a supervisory authority, the judicial police in the context of a judicial investigation, or the tax administration, for example). They include the internal departments of the data controller (the HR department, for example), processors, joint controllers and other data controllers (business partners, for example).

## Add a recipient

1. In the **Recipients** section, click **New recipient**.
2. In **Category**, select the type of recipient: **Internal service**, **Processors**, **Third party (autonomous controller)**, **Authorized third party (autonomous controller)**, **Joint controller** or **Data subject**.
3. Identify the recipient:
   * **Directory**: select a stakeholder from your stakeholders directory, or create a new one. With the recipient in the directory, you can map the processing activities related to this stakeholder.
   * **Select an organizational unit**: select one of your organizational units, for example an internal department.
   * **Custom label**: enter a free label. This option is not available for processors. For the **Data subject** category, it is the only option.
4. Optionally, in **Describe how data are processed**, describe what the recipient does with the data.
5. If the recipient has access to the data, switch on **Has the recipient access to data ?** and indicate whether it has **Access to all data (default)** or **Access to certain data sets**. In the second case, select the relevant datasets.
6. If the data is transferred outside the EU, declare the transfer in the same panel (see [Data transfers outside the EU](transfers.md)).
7. Click **Add**.

{% hint style="info" %}
Dastra helps you complete the list:

* the joint controllers declared in the **Parties involved** section are shown as **Suggested recipients**: click **Add** to add them;
* when you select a processor whose subsequent processors are documented in the stakeholders directory, you can add them at the same time under **Add related subprocessors**;
* when the selected stakeholder or organizational unit is located in another country, Dastra suggests adding a transfer.
{% endhint %}

The recipients are listed with their **Category** and their **Transfers**. Use **Reorder by** to sort them by name or by category. From the **...** menu of a recipient, you can **Edit** it, open its stakeholder with **Edit vendor**, **Add a subsequent processor**, **Launch a vendor questionnaire** or **Delete** it, depending on its category.

## Add a subsequent processor

A processor may itself use other processors to process the data. To declare them, open the **...** menu of a recipient of the **Processors** category and click **Add a subsequent processor**. The subsequent processor is displayed under its processor.

## Assess a vendor

From the **...** menu of a recipient registered in the directory, click **Launch a vendor questionnaire** to assess this stakeholder with a questionnaire.

## Generate a DPA

If you use the Contracts module, you can generate a data processing agreement (DPA) directly from the processing activity. In the list of recipients, a **DPA** button appears on the processors of a data controller activity that are registered in the directory. It opens the contract generation with the DPA template, already filled in with the processing activity and the processor. The same action is available in the **...** menu (**Generate DPA**).

Likewise, when a transfer is declared for a processor, or for a third party of a data controller activity, the **SCC transfer** button generates the corresponding standard contractual clauses.

{% content-ref url="../../../contracts/templates.md" %}
[templates.md](../../../contracts/templates.md)
{% endcontent-ref %}
