---
description: Identify the key parties involved in data processing.
---

# Stakeholders

The **Parties involved** section (formerly called **Stakeholders**) is the second section of a processing activity. It brings together two lists:

* the **users**: people who have an account on the Dastra platform and who are assigned to the processing activity;
* the **stakeholders**: the organizations, departments or people involved in the processing, such as the data controller, its data protection officer, joint controllers or the processing implementation manager.

## Add users to a processing activity

Dastra allows you to attach users to a processing activity.

Note that these are not stakeholders but users (individuals who have an account on the Dastra platform).

1. In the **Parties involved** section, click **Add users**.
2. In **Data processing user**, select one or more users.
3. In **Assign roles**, choose the role of these users.
4. Click **Add**.

The users appear in the table with their **Assignment**, which you can change at any time from the table.

The roles defined this way help you organize the management and implementation of your processing activities in Dastra:

* **Accountable**: the user in Dastra who is in charge of validating that the processing activity and its associated elements, as described in Dastra, meet the organization's expectations. This person may be different from the data controller's signatory. For example, it could be a department manager, a DPO, or a DPO relay.
* **Responsible**: the user who carries out the necessary actions on the processing activity and describes it. This could involve implementing data security measures, managing access, or any other task required to ensure the compliance of the processing. This could be a project manager or a dedicated business manager.
* **Informed**: users who need to be kept informed of the progress and status of the processing activity without having an active role in its validation or implementation. This may include members of the management team, project managers, or other stakeholders who have an interest in the processing.

Assigned users are notified of the actions taken on the processing activity and are the default recipients of the related tasks and notifications.

{% hint style="info" %}
Assigning a user does not restrict access to the processing activity. To limit access, use the roles and permissions system.
{% endhint %}

## Identify the main stakeholders of the processing activity

You can indicate the stakeholders involved in the implementation of the processing. This can be, for example, a department of a company (such as the human resources department) but also a dedicated person in the case of a project (a project manager, for example).

You also indicate, where applicable, the representative of the data controller and the joint controller(s).

The first rows of the stakeholders table are inherited from the entity of the organizational unit selected in the **General** section, and are marked with a lock icon:

* the **Data controller** (or **Current entity (Data processor)** for a data processor activity),
* its **Data protection officer**,
* its **Representative**.

To change them, edit the entity in the management of organizational units.

## Add a specific stakeholder

1. In the **Parties involved** section, click **Add a specific stakeholder**.
2. In **Select a stakeholder**, search the stakeholder directory, or click **Create stakeholder** to add a new one.
3. In **Choose a category**, select the role of this stakeholder: **Joint controller**, **Data controller representative**, **Processing implementation manager**, **Operational Data Controller** or **Other**. If you choose **Other**, enter the role in **Category label**.
4. Click **Add**.

<figure><img src="../../../.gitbook/assets/ropa-stakeholders-1.png" alt="Choose a category list open in the Add a specific stakeholder window"><figcaption><p>Categories available for a specific stakeholder</p></figcaption></figure>

## Add a joint controller (co-controller)

To add a joint controller, add a new stakeholder and select **Joint controller** in **Choose a category**.

<figure><img src="../../../.gitbook/assets/ropa-stakeholders-2.png" alt="Add a specific stakeholder window with the Joint controller category selected"><figcaption><p>Adding a joint controller to the processing activity</p></figcaption></figure>

## Add a processing implementation manager

The processing implementation manager is the department that is operationally responsible for the processing. This is generally the department that uses the data and carries out the processing activity.

It can be either a department or an individual.

In Dastra, add it as a stakeholder with the **Processing implementation manager** category.

## Add a data controller representative

The data controller representative is the operational representative of the data controller (DC). For example, this could be a member of the executive committee or a municipal councilor (with the DC being represented by the mayor).

In Dastra, add it as a stakeholder with the **Data controller representative** category.

## Add an Operational Data Controller (ODC)

The **Operational Data Controller (ODC)** is a concept used internally by some organizations to designate a person with specific responsibilities in the **operational management of personal data processing**.

In Dastra, add it as a stakeholder with the **Operational Data Controller** category.

📌 **Role of the ODC in GDPR governance**\
The **ODC** is not a concept defined by the GDPR, but some organizations use it internally to designate a person with specific **operational responsibilities** in managing data processing activities.

#### **Implementation of data processing**

* The ODC often serves as an **operational relay for the Data Controller (DC)** within a business unit (e.g., HR, Marketing, IT, etc.).
* They are responsible for carrying out data processing activities on a daily basis, in accordance with the **instructions of the Data Controller** and in compliance with data protection principles.

#### **Application of compliance measures**

* The ODC ensures that processing activities are carried out in accordance with **internal compliance policies** and data protection obligations.
* They apply the **technical and organizational measures** defined by the company to ensure the **security and confidentiality** of personal data.

#### **Collaboration with the DPO and the Data Controller**

* The ODC works closely with the **Data Protection Officer (DPO)** to ensure that data processing activities comply with data protection rules.
* They can act as a key contact for the **DPO**, particularly when handling **data subject requests** (e.g., access, rectification, deletion).

#### **Incident and data breach management**

* The ODC may be involved in **detecting and managing data breaches**, applying internal procedures to **react quickly and notify** incidents if necessary.
* They monitor incidents and help implement **corrective actions**.

#### **Documentation and maintenance of the record of processing activities**

* The ODC contributes to updating the **record of processing activities**, documenting the processing under their responsibility and ensuring that relevant information is properly reported to the **Data Controller or DPO**.

🎯 **Difference between the Data Controller and the Operational Data Controller**

| **Criteria**                 | **Data Controller (DC)**                                 | **Operational Data Controller (ODC)**        |
| ---------------------------- | -------------------------------------------------------- | -------------------------------------------- |
| **Role**                     | Defines the **purposes** and **means** of processing     | Implements processing activities in practice |
| **Decision-making**          | Decides **why and how** data is processed                | Applies decisions and manages execution      |
| **Legal responsibility**     | Holds **legal responsibility** in case of non-compliance | Operates under the **authority of the DC**   |
| **Interaction with the DPO** | Works with the **DPO** to define policies                | Implements **DPO recommendations**           |
