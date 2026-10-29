---
description: Learn how to identify risks in Dastra.
---

# 1. Identify

To create a risk, open **Risk management** > **Risks**, choose the tab of the object type concerned and click **Create a risk**. You can also create it from a processing activity page (see [Attach a risk to a processing activity](../attach-to-processing.md)). The **Identification** section opens.

<figure><img src="../../../.gitbook/assets/risks-identify-1.png" alt="Identification section of a new risk: organizational unit, linked object, risk owner, identification date and risk type"><figcaption><p>The Identification section of a risk</p></figcaption></figure>

Fill in the identification details:

* the organizational unit: by default, the one of the processing activity if the risk is attached to one;
* the object concerned, for example the processing activity;
* the risk owner, who is responsible for monitoring and managing the risk;
* the identification date;
* the type of risk, chosen from the repository;
* a summary of the risk, specific to this object.

{% hint style="info" %}
Dastra lets you build a repository of risk types. The repository saves time and lets you reuse a risk type on other objects.
{% endhint %}

If your risk type is not in the repository, add it from this page with **Create a type of risk**.

## Add a risk type <a href="#add-a-risk-type" id="add-a-risk-type"></a>

You can also manage risk types in **Risk management** > **Type of risks**, with the **Create a type of risk** button.

You reuse a risk type to generate the same risk on as many objects as you wish. For example, you may want to identify the same risk on several of your processors: enter the risk type once, then reuse it for each processor or service provider.

In the **Identification** section of the risk type, give it a name and an internal reference. Tags are optional.

<figure><img src="../../../.gitbook/assets/risks-identify-2.png" alt="Risk type form: name, reference, dreaded event and its description"><figcaption><p>A risk type: name, reference and dreaded event</p></figcaption></figure>

A risk is the combination of a dreaded event and one or more threats that could cause it. It is measured in terms of likelihood (probability of occurrence) and severity (impact).

### Dreaded event

To add a risk type, identify the dreaded event and its impacts. The dreaded event is the consequence of the occurrence of a risk.

Classically, three types of dreaded events are mentioned for information security and privacy. The GDPR calls on you to [guarantee the security](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679#d1e3428-1-1) of personal data along these three lines (Article 32):

* breach of **confidentiality**
* breach of **availability**
* breach of **integrity**

You can create your own categories of dreaded events with **Create dreaded event**, for example an industrial accident or an act of corruption. The number of dreaded events is not limited. The module first focuses on risks to information systems.

For each dreaded event, specify the impacts it causes in the **Description of the dreaded event** field.

Impacts vary with the context and the object for which the risk is addressed. For risks relating to personal data, the impacts are harms to individuals: identity theft, false accusation, loss of civil status and so on.

### Threats

For each dreaded event, identify the threat or threats that enable it to occur. Imagine a scenario: use past events or your imagination to anticipate what might happen.

In the **Threats** section, select an existing threat with **Add a threat** or create one. The **Threat details** field describes the scenario.

<figure><img src="../../../.gitbook/assets/risk-threats-section.png" alt="Threats section of a risk type, with the Add a threat button"><figcaption><p>The Threats section of a risk type</p></figcaption></figure>

Dastra offers templates for generic threats. To import them, open **Risk management** > **Threats**, open the menu of the **Create threat** button and click **Create from library...**.

### Sources

Risk sources are the elements that enable the dreaded event to occur: who or what could be at its origin?

Take into account human sources, for example an IT administrator, a cyber-attacker or a foreign state, and non-human sources, for example water, an earthquake or a non-targeted computer virus.

In the **Sources** section, select or create the sources, then describe them in **Source description**.

<figure><img src="../../../.gitbook/assets/risks-identify-3.png" alt="Sources section of a risk type with two sources selected"><figcaption><p>The Sources section of a risk type</p></figcaption></figure>

### Control points

For each risk type, determine the existing or planned measures that will deal with the risk. These control points can be of several kinds: security, technical, organizational, legal or functional measures.

In the **Control points** section, select existing control points with **Select control points** or create new ones with **Create a control point**. Each control point defines:

* its influence: reducing the impact (mitigation) or the probability (prevention) of the risk;
* its possible answers and their score, from 0 to 100 points. By default, a new control point offers the answers **Yes** (1 point), **No** (0 points) and **Not applicable**;
* its owner, its priority (1 is the highest, 10 the lowest) and, if needed, a recurrent assessment with the number of days between two controls.

<figure><img src="../../../.gitbook/assets/risks-identify-4.png" alt="Control points section of a risk type with three control points selected"><figcaption><p>The Control points section of a risk type</p></figcaption></figure>

For information security risks, ISO 27001 identifies standard control points. The CNIL personal data security guide also proposes several.

### Pre-assessment

In a risk type, you can include an assessment. It is carried over to every risk created from this type, which saves time. It is optional.

The assessment is made in terms of likelihood and severity, according to the scale you have set (see [Assess](assess.md)).

You can set the initial risk: the theoretical risk associated with the activity, before any control measure (internal control).

You can also set the residual risk: the risk remaining after the implementation of control measures, control points in particular. It cannot exceed the initial risk.

<figure><img src="../../../.gitbook/assets/risks-identify-5.png" alt="Pre-assessment section of a risk type with the initial and residual levels"><figcaption><p>The pre-assessment of the initial and residual risk</p></figcaption></figure>
