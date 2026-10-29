---
description: >-
  Build your organization's repository of AI models, import it or generate it
  with the AI assistant, then link the models to your AI systems.
---

# AI models repository

For each AI system you register, you enter the AI model or models it uses. You describe each model once, in a repository, then link it to the systems that use it.

## Definition

An artificial intelligence model is a computer program designed to perform specific tasks using machine learning and data analysis techniques.

* Foundations: an AI model is based on specific algorithms and architectures, such as the neural networks of deep learning, which let it learn from data.
* Learning: the model is trained on large data sets to identify patterns and relationships. It can then make predictions or generate content from new data.
* Functionality: this is the purpose for which the model is used, for example image generation for the Midjourney model.
* Use: these models are deployed in a wide range of applications, from chatbots and virtual assistants to data analysis and content creation.

## Open the repository

Click **AI governance** in the sidebar, then **AI models**.

<figure><img src="../../.gitbook/assets/ai-systems-models-1.png" alt="List of AI models with the Creating a new AI model button and its menu"><figcaption><p>The AI models repository</p></figcaption></figure>

The **Creating a new AI model** button opens the creation window. Its menu also offers:

* **Create from library...**: choose a model from the Dastra library;
* **Import**: import a list of models from a file, see below;
* **Export**: export the list as CSV, Excel, JSON or Markdown.

## Create an AI model

Click **Creating a new AI model**. The window offers three options:

* **Generate with AI**: the AI assistant fills in the record from a name or a description, see the next section;
* **Built-in template**: create the record from our library or from another workspace;
* **Personalized**: enter the record yourself.

<figure><img src="../../.gitbook/assets/ai-systems-models-2.png" alt="Creating a new AI model window with the three options Generate with AI, Built-in template and Personalized"><figcaption><p>The three options to create an AI model</p></figcaption></figure>

With **Personalized**, enter the model name, then complete the record in the **AI model** panel:

| Field | Content |
| --- | --- |
| **Model name** | Required, 120 characters at most. Example: GPT 4, Mistral AI, MidJourney. |
| **Version** | The exact version of the model, 30 characters at most. Example: gpt-4o-2024-05-13. |
| **Reference** | Your own reference for the model, 120 characters at most. |
| **Publisher** | The publisher of the model, chosen among the stakeholders of your workspace. You can create one from the list. |
| **Tags** | The tags that classify the model. |
| **Describe the AI model** | The description, 3,000 characters at most. Detail the features and the information you have. |
| **Learning type of the AI** | The method used to train the model, see below. |
| **Is this model a General Purpose AI ?** | Yes or no. A general purpose AI (GPAI) model is versatile and can be integrated into many downstream systems. A tooltip recalls the AI Act definition. |
| **Does this model present a systemic risk?** | Yes or no. The question only appears if the model is general purpose. A tooltip recalls the definition of systemic risk. |
| **Documentation** | A text editor for the documentation of the model. |

<figure><img src="../../.gitbook/assets/ai-systems-models-3.png" alt="AI model panel with the name, version, publisher, learning type fields and the questions on general purpose and systemic risk"><figcaption><p>The record of an AI model</p></figcaption></figure>

The learning type describes how the model was trained to perform its tasks. It influences how the model generalizes what it has learned. Dastra offers four, each with its definition in the list:

* Supervised Learning: learning with labeled data to make predictions;
* Unsupervised Learning: learning without labeled data to find patterns;
* Reinforcement Learning: learning through rewards and punishments to optimize actions;
* Transfer Learning: using knowledge from one domain to improve learning in another.

### Generate the record with the AI assistant

The **Generate with AI** option of the creation window generates an AI model record from a simple name or description. It is available if your plan includes the matching AI features. The assistant uses web browsing to look up and fill in the relevant information.

1. Click **Creating a new AI model**, then **Generate with AI**.
2. Enter the model name or a short description, for example "GPT-4o by OpenAI".
3. Review and complete the generated record before you validate it.

The generated content is a suggestion. Check and complete the information before you validate, as AI-generated content may contain errors.

<figure><img src="../../.gitbook/assets/ai-systems-create-generate-form.png" alt="AI model generation window with input field, language selector and samples"><figcaption><p>Describe the AI model to generate (name, publisher...): web browsing is used to complete the information</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/ai-system-generate-result.png" alt="AI model record generated by the assistant, to review before validation"><figcaption><p>The generated record should be reviewed before validation</p></figcaption></figure>

### Import and export models

To import several models, open the menu of the **Creating a new AI model** button and click **Import**. The procedure is the same as in the other modules: see [Import your data (Excel, Csv, JSON)](../general/import.md). The file can contain the following columns:

| Column | Description |
| --- | --- |
| `Label` | Model name, required. |
| `Ref` | Your reference for the model. |
| `Description` | Description of the model. |
| `VersionName` | Version of the model. |
| `LearningType` | `SupervisedLearning`, `UnSupervisedLearning`, `ReinforcedLearning` or `TransferLearning`. |
| `IsGeneralPurposeAi` | `true` if the model is general purpose, otherwise `false`. |
| `SystemicRisk` | `true` if the model presents a systemic risk, otherwise `false`. |
| `DocumentationHtml` | Documentation of the model, as HTML. |

The **Export** action produces a CSV, Excel, JSON or Markdown file of the list.

## Link a model to an AI system

Open the record of the AI system concerned. The **AI models** step is the third one, after **General** and **Responsibility**.

1. In the **Select AI models** selector, choose one or more models from your repository. You can also create one from the selector.
2. For each model, fill in the **Usage description**. This field explains how the model is used in this AI system.
3. Save the record.

An alert icon flags the models that present a systemic risk.

<figure><img src="../../.gitbook/assets/ai-systems-models-4.png" alt="AI models step of an AI system with one model selected and its usage description"><figcaption><p>Linking a model to an AI system</p></figcaption></figure>
