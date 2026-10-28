---
description: Learn how to create and modify a questionnaire template with Dastra.
---

# Create a questionnaire template

## Introduction

Creating or modifying a questionnaire template in Dastra is a breeze. To do so, access the "Questionnaires" functionality.

## Create or modify a questionnaire template

To create a questionnaire template, click the "Create Template" button on the "Questionnaires" tab. Then you can select one of the template types available in Dastra: automated, custom, or import from file.

<figure><img src="../../.gitbook/assets/create-audit.png" alt=""><figcaption></figcaption></figure>

This brings you to the template type selection interface:

<figure><img src="../../.gitbook/assets/audit-type.png" alt=""><figcaption></figcaption></figure>

* By clicking on the "Automated Questionnaire" tab, you will choose an existing predefined questionnaire template from the Dastra Questionnaire Library.
* By clicking on "Custom Questionnaire" you can build your own questionnaire template.
* By clicking on "**Create from AI**", the AI assistant generates the template from your description. You can attach documents with the **+** button (an internal audit grid in Word, a security questionnaire in PDF, etc.): the assistant transposes the questionnaire provided into sections, questions, question types and answer options. The questionnaire type, the generation language and the advanced options apply as for any generation, and you preview the result before creating the template.

<figure><img src="../../.gitbook/assets/audit-create-ai-template-attachments.png" alt="Window for creating a questionnaire template with AI, with attached documents"><figcaption><p>Creating a questionnaire template with AI from a document</p></figcaption></figure>

{% hint style="info" %}
Unlike automated questionnaires, custom questionnaires are fully customisable. Based on the answers selected by respondents, you will be able to automatically generate an action plan or map the risks associated with the model.
{% endhint %}

## Automated questionnaire templates

Dastra offers a number of automated questionnaire templates to document compliance and drive processes. These include templates for privacy impact analysis (PIA/DPIA), legitimate interests assessment (LIA), transfer impact assessment (TIA), processor assessments, and more.

<figure><img src="../../.gitbook/assets/automatic-audit.png" alt=""><figcaption></figcaption></figure>

Once you have selected a template, you will be taken to the planning screen where you can either:

* modify the template by clicking on the "Modify template" button, or
* schedule a questionnaire by clicking on the "Schedule a questionnaire" button.

{% hint style="info" %}
Some questionnaire types (PIA, TIA, LIA) can also be launched directly from within a processing activity — for example from the "Impact assessment", "Recipients" or "Purposes" tabs. See the dedicated pages below for details.
{% endhint %}

## Customised questionnaire templates

In Dastra, you can create your own custom questionnaire template. To do this, click on the "Custom Questionnaire" option. This will take you to the questionnaire template editing interface.

Build the questionnaire template you want and click on "Save and Continue".

<figure><img src="../../.gitbook/assets/creation-assessement-template-2.png" alt=""><figcaption></figcaption></figure>

### Scoring calculation rule for multiple-choice questions

For a multiple-choice question whose answers carry a score, the **Scoring calculation rule** field determines the score kept:

* **Sum of values** (default): adds the scores of all selected answers;
* **Maximum value**: keeps only the highest score among the selected answers. For example, in a DPIA, the risk level of a "Data categories" question then reflects the most sensitive category, not the total of the categories ticked.

The question's **Score max** is shown under the selector. The rule applies to the overall score, the percentage score and the score by category, and it is saved with the template.

<figure><img src="../../.gitbook/assets/audit-template-question-scoring-rule.gif" alt="Choosing the scoring calculation rule of a multiple-choice question"><figcaption><p>Scoring calculation rule of a multiple-choice question</p></figcaption></figure>

## Items assessed

You can link questionnaires to items in Dastra. By choosing the type of item being assessed, you force all questionnaire responses based on that template to be linked to an object of the chosen type. For example, you can choose that this questionnaire template will always be linked to a process.

<figure><img src="../../.gitbook/assets/element-audite.png" alt=""><figcaption></figcaption></figure>

You can choose not to link a questionnaire to a particular object. In this case, the response will always be linked to an organisational unit. This may be the case for global compliance questionnaires for example.

## Types of templates

When creating a custom template, you will need to choose a template type.

<figure><img src="../../.gitbook/assets/assessment-template-create-label-required.png" alt=""><figcaption></figcaption></figure>

These types allow for some customisation of questionnaire models.

* **Standard questionnaire**: this is a standard questionnaire
* **Compliance questionnaire**: currently a standard questionnaire
* **Impact analysis**: this questionnaire template allows a risk matrix to be displayed (with the required configuration) and to be called up at the PIA stage of a processing activity
* **Subcontractor questionnaire**: this questionnaire template is called at the subcontractor recipients stage of a processing activity
* **Transfer Impact Assessment (TIA)**: a questionnaire to analyse the risks related to a data transfer outside the EU
* **Legitimate Interest Assessment (LIA)**: questionnaire of the legal basis of legitimate interests to ensure that the interests do not override the rights and freedoms of individuals
* **Training questionnaire**: a questionnaire for conducting training quizzes. This type of questionnaire makes it possible to select a correct answer from the answers and to display the correct answers at the end of the questionnaire.

## Dynamic selection questions

Among the question types available in the template editor, two types allow you to connect a question directly to data in your Dastra workspace: **"Single dynamic selection"** and **"Multiple dynamic selection"**.

These question types display a list of objects from Dastra to the respondent: assets, processing activities, stakeholders, security measures, datasets, data fields, AI systems, contracts, etc. The respondent selects one or more items from their library as their answer.

{% hint style="warning" %}
For the list to display correctly, the respondent must have **read access** to the corresponding objects in Dastra. An external respondent without a Dastra account, or without the appropriate permissions, will not be able to see the list.
{% endhint %}

## Populate custom fields from a questionnaire

You can use a questionnaire to automatically populate custom fields in Dastra registers. Configure the question variable with the `custom_` prefix, followed by the field’s technical name.

{% stepper %}
{% step %}
### Configure the template question

In **Questionnaires**, open the relevant template and add the question that should populate the custom field. Choose a question type that is compatible with the field type.

Open the question properties, then enable **Do you want to customize the variable name?**. In **Variable name**, enter `custom_` followed by the field’s technical name.

For a field with the technical name `business_owner`, use:

```
custom_business_owner
```

Then save the template changes.
{% endstep %}
{% endstepper %}

### Variable syntax

The variable name must follow the `custom_variable_name` format. Use the field’s technical name exactly as written after the prefix.

{% hint style="info" %}
The custom field does not need to appear under **Select a variable to map**. Enter the full variable name directly.
{% endhint %}

{% hint style="warning" %}
The `custom_` prefix is required. For the `business_owner` field, use `custom_business_owner`, not `business_owner`.
{% endhint %}

## Template version management

When modifying a template that is already in use, Dastra offers two options:

* **Overwrite the current version**: the changes replace the template in place, with no version history. Existing answers are kept, but answers to questions that were removed or restructured may no longer be shown or counted. Before you confirm, a comparison between the saved version and your changes is shown, and you can still cancel.
* **Create a new version**: a new version of the template is created. You can leave it as a **draft** while preparing it, then promote it to **main version** when it is ready. Existing questionnaires continue to use the previous main version until you explicitly switch.

To navigate between versions, use the version selector available in the template interface. The version marked as main is the one used for all new campaigns.

The **Compare versions** action shows two versions side by side. Each section and each question has a status: **Unchanged**, **Modified**, **Removed**, **Added** or **Moved**; an item that was only moved is not reported as removed and then added. A reminder of the impact on the answers already collected comes with the comparison.

<figure><img src="../../.gitbook/assets/audit-template-version-compare-modal.png" alt="Comparison of two versions of a questionnaire template"><figcaption><p>Comparing two versions of a questionnaire template</p></figcaption></figure>

{% hint style="info" %}
The number of available templates depends on your subscription plan. This quota is shared across all workspaces in your organisation. The template recycle bin counts towards the quota — remember to empty it regularly to free up slots.
{% endhint %}

## Load a questionnaire template you own

Finally, it is possible to import one of your questionnaire templates, in json format. To do this, when creating the questionnaire, select the "Load a template" option.

## Go further

{% content-ref url="scheduling-an-audit-or-a-pia.md" %}
[scheduling-an-audit-or-a-pia.md](scheduling-an-audit-or-a-pia.md)
{% endcontent-ref %}

{% content-ref url="share-an-audit-report-or-pia.md" %}
[share-an-audit-report-or-pia.md](share-an-audit-report-or-pia.md)
{% endcontent-ref %}

{% content-ref url="questionnaire-types/pia-dpia.md" %}
[questionnaire-types/pia-dpia.md](questionnaire-types/pia-dpia.md)
{% endcontent-ref %}

{% content-ref url="questionnaire-types/tia.md" %}
[questionnaire-types/tia.md](questionnaire-types/tia.md)
{% endcontent-ref %}

{% content-ref url="questionnaire-types/lia.md" %}
[questionnaire-types/lia.md](questionnaire-types/lia.md)
{% endcontent-ref %}
