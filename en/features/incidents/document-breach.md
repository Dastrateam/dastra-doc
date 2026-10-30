---
description: >-
  Create an incident in Dastra and fill in each step of the form: description,
  data, risk assessment, notification to the authority, communication to the
  data subjects and post-mortem.
---

# Document a new data breach

This page explains how to create an incident in Dastra and how to fill in each step of its form. If your organization acts as a processor, also read [Incidents as a processor](as-processor.md).

## Create an incident

There are three ways to create an incident:

* manually, with the **Create an incident** button;
* by importing an Excel, CSV or text file: in the record, open the arrow of the **Create an incident** button, choose **Import** and follow the wizard described in [Import your data (Excel, Csv)](../general/import.md);
* by email: a collection address turns every email it receives, with its attachments, into an incident. See [Incoming mail data collection](../settings/mailboxes.md).

### Create an incident manually

1. Open **Operations** > **Incidents** > **Record of incidents**, then click **Create an incident**.
2. Type the **Incident Title** and choose the **Organizational unit**. Both fields are required.
3. Answer the question **In the case of this data breach, are you a sub processor?**. The default answer is **No**.
4. Click **Create**. The incident form opens on its first step.

<figure><img src="../../.gitbook/assets/incidents-document-breach-1.png" alt="Create an incident dialog with the title, the organizational unit and the role question"><figcaption><p>The dialog to create an incident</p></figcaption></figure>

Answer **Yes** only if your organization processes the affected data on behalf of a controller. The form is then adapted, as explained in [Incidents as a processor](as-processor.md).

## Move through the form

The steps of the form are listed on the left. A counter shows how many items are filled in for the steps that have a list. Go through them in order with **Next** and **Back**, or jump straight to the step you want.

<figure><img src="../../.gitbook/assets/incidents-document-breach-2.png" alt="Incident form on the General step, with the list of steps on the left"><figcaption><p>The incident form, here on the General step</p></figcaption></figure>

* Click **Save changes** to keep your edits, or open the arrow of the button and choose **Save and exit**.
* At the top of the form, tabs give access to the discussions, the related tasks, the relationships with other objects, the history and the audits.
* The workflow stage selector moves the incident forward in your workflow. See [Workflow stages](../settings/workflow-stages.md) to configure them.
* The menu of the **Save changes** button also gives access to **Export**, **Share**, **Workflow rule**, **Custom fields**, **Create a copy** and **Move to recycle bin**.

The **Notification** step does not appear for an incident handled as a processor, and the **AI systems** step only appears if the AI systems module is enabled.

## General step

Describe the incident and its circumstances:

* **Incident Title**, **Internal reference**, **Organizational unit** and **Tags**;
* **Incident type**: **Loss of confidentiality**, **Loss of integrity** or **Loss of availability**. You can tick several;
* **Start date**, **End date** and the **Still ongoing** box;
* **Observation date**;
* **Incident Manager**;
* **Describe incident** and **Incident localization**;
* **Main cause of incident** (Unknown, Internal & intentional, Internal & accidental, External & intentional, External & accidental or Other reason), an optional secondary reason and further details on the cause;
* **Were any processors involved?** If you answer **Yes**, list the processors involved among the stakeholders of your workspace.

{% hint style="info" %}
The observation date is the starting point of the notification deadline. Enter the date and time when you became aware of the breach, not the time it started.
{% endhint %}

## Data step

Indicate the personal data affected:

* **Datasets involved in the incident**: select the datasets of your workspace;
* **Data volume**: choose a value in a list (**Select**) or type a number (**Type a value**). This is the approximate number of records affected;
* **Data source**;
* **Was sensitive data involved?** The answer feeds the **With sensitive data** indicator of the record.

## Measures step

Describe the security measures in two parts:

* **Security measures existing before the incident**: select existing security measures and complete with a text;
* **Security measures adopted after the incident**, presented the same way.

This is the information that Article 33(3) of the GDPR asks you to describe in the notification to the supervisory authority.

## Data subject categories step

Click **Add a category of data subjects** for each category affected. In the dialog, choose the category, type the **Data subject volume** and add a comment if needed. You can edit or delete each row afterwards.

## Data processing step

Under **Data processing involved**, select the processing activities of the record that are concerned, then complete **Additional informations** if needed. Dastra also uses these links to find the data controllers of an incident handled as a processor.

## AI systems step

When a breach involves an AI system, whether as the cause, the vector, or because it processes the affected data, select it under **Select the AI systems linked to this incident**. You can link several, among the AI systems of your workspace.

<figure><img src="../../.gitbook/assets/incidents-document-breach-7.png" alt="AI systems step of an incident with the list of linked systems"><figcaption><p>The AI systems step</p></figcaption></figure>

This link lets you:

* display the **Ai systems** column in the record and filter incidents with **AI systems** or **Linked to an AI system**;
* follow the share of incidents that involve an AI system with the **With an AI system** indicator of the record and of the **Reporting** page;
* have the AI-generated post-mortem take these systems into account.

## Risk assessment step

The risk assessment determines whether you must notify the supervisory authority and inform the data subjects.

<figure><img src="../../.gitbook/assets/incidents-document-breach-3.png" alt="Risk assessment step with the two scores and the resulting risk level"><figcaption><p>The Risk assessment step, with the calculated risk level</p></figcaption></figure>

First answer **Risk assessment done?**.

* With **No**, assess the incident in Dastra. Choose a score from 1 (negligible) to 4 (maximum) for **Data subject identification probability**, which measures how easy it is to identify people from the data, and for **Impact on data subject**, which measures how serious the consequences are for them. Dastra adds the two scores and displays the **Risk level**.
* With **Yes**, you have already carried out your own analysis. Choose the level in **Risk assessment conclusion**, then click **Send your analysis** to attach the document in the Documentation step.

| Sum of the two scores | Risk level | Consequence displayed by Dastra |
| --- | --- | --- |
| 2 and 3 | Low risk | Notification to the supervisory authority and communication to persons are not necessary |
| 4 and 5 | Medium risk | You must notify the supervisory authority |
| 6 to 8 | High risk | Notification to the supervisory authority and communication to data subjects mandatory |

For the legal framework of this assessment (Articles 33 and 34 of the GDPR), see [Data breach notifications](../../gdpr/concepts/breaches.md).

## Notification step

The **Notification** step tracks the notification to the supervisory authority. The GDPR requires you to notify the breach without undue delay and, where feasible, no later than 72 hours after becoming aware of it (Article 33).

<figure><img src="../../.gitbook/assets/incidents-document-breach-4.png" alt="Notification step with the 72-hour countdown"><figcaption><p>The Notification step and its countdown</p></figcaption></figure>

As soon as the risk assessment concludes to a medium or high risk, a message counts the 72 hours from the observation date. It shows the number of hours left, then "72 hours deadline exceeded" when you are late, then "You have notified the data protection authority" once the notification is recorded. For a low risk, the message states that you are not required to notify the authority.

To record a notification:

1. Click **Add a notification**.
2. Click the link "Go to the website of the competent authority" to declare the breach on the authority's website. Dastra does not send the notification: it keeps a record of it.
3. Fill in the date of the notification (labeled **Communication's date** in the app), the **Notification's number (provided by the DPA)** and the **Observations**.
4. Confirm the dialog, then save the form.

The authority offered is the one of the organizational unit of the incident. If none is defined, the dialog shows "No control authority has been defined for your entity" and a link to the organizational unit settings. See [Add a lead authority](../../getting-started/setup/lead-authority.md).

## Communication step

This step tracks the information of the data subjects. Article 34 of the GDPR requires it when the breach is likely to result in a high risk to their rights and freedoms.

A message reminds you of what the risk assessment implies. Then answer **Did you contact individuals?** with **Not applicable**, **Yes** or **No**.

* With **Yes**, click **Add a communication** and fill in the **Support - Method of communication** (email, letter, phone call, website banner, communication campaign or other way), the **Communication's date**, the **Number of individuals notified** and the content sent.
* With **No**, answer **Why have you not informed individuals concerned?**: "No likely high risk to individuals" or "Personal data was inaccessible to unauthorised persons (encrypted, pseudonymised, or otherwise protected)". Explain your choice in **Justification**.

<figure><img src="../../.gitbook/assets/incidents-document-breach-5.png" alt="Add a communication dialog with the method, the date, the number of people and the content"><figcaption><p>The Add a communication dialog</p></figcaption></figure>

## Post-mortem step

A post-mortem is a detailed review of the incident once it is resolved. It is recommended, not mandatory. Answer **Would you like to include a post-mortem ?**. With **Yes**, enter the **Date**, then choose one of three methods:

* type the **Document's reference, emplacement or url** if the document already exists elsewhere;
* click **Add Post-Mortem as an attachment**;
* write the text in the editor, using **Use the template** to start from a standard outline, or **Generate with AI**.

<figure><img src="../../.gitbook/assets/incidents-document-breach-6.png" alt="Post-mortem step with the Use the template, Generate with AI and Save as PDF buttons"><figcaption><p>The Post-mortem step</p></figcaption></figure>

**Generate with AI** writes a draft from the information of the incident: context (including the linked processing activities and AI systems), timeline, impacts, measures and risk assessment, communications, lessons learned and improvement ideas. Review and correct the text before saving it. **Save as PDF** exports the written post-mortem.

## Documentation step

Gather here everything that documents the incident: free text with links and images, and attached files such as the post-mortem or the notification report.

## Summary step

The **Summary** step gathers all the information of the incident in read-only form. Use **Collapse all** and **Deploy all** to browse the sections, and **Print** to get a paper copy.

## Invite colleagues to complete the incident

Several people often work on an incident. Click the users button at the top right of the form, next to the workflow stage selector. In the dialog, choose the **Section** to complete, **Select users to invite**, type your message (you can start from a template with **Select a template**), then click **Send invitation**.

<figure><img src="../../.gitbook/assets/incidents-document-breach-8.png" alt="Invitation dialog with the section, the users and the message"><figcaption><p>The dialog to invite colleagues to complete an incident</p></figcaption></figure>

## Share an incident

**Share**, in the menu of the **Save changes** button or in the menu of the **Create an incident** button of the record, opens the window to create a sharing link. For how sharing links work in general, see [Share the record of processing](../ropa/share.md).
