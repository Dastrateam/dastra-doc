---
description: Learn how to conduct a Privacy Impact Assessment (PIA) or Data Protection Impact Assessment (DPIA) with Dastra.
---

# Privacy Impact Assessment (PIA / DPIA)

## What is a PIA / DPIA?

A Data Protection Impact Assessment (DPIA), also known as a Privacy Impact Assessment (PIA), is a process required under Article 35 of the GDPR when a processing activity is likely to result in a high risk to the rights and freedoms of individuals.

A DPIA must be carried out before starting a processing activity that presents such risks, and reviewed whenever the nature of the processing changes significantly.

## Does this processing need a DPIA?

In Dastra, the **Impact assessment** tab of each processing activity helps you determine whether a DPIA is required. It evaluates 9 risk criteria defined by the EDPB:

* Evaluation or scoring including profiling and prediction activities
* Automated decision making with significant effects
* Systematic monitoring
* Sensitive personal data
* Data processed on a large scale
* Combining, linking or cross-referencing data
* Data concerning vulnerable individuals
* Innovative use or application of new technologies
* Processing that prevents data subjects from exercising their rights

For each criterion, select "Yes", "No" or "Not applicable". **Two "Yes" answers are generally sufficient** to trigger a DPIA requirement, though a single criterion may be sufficient depending on context.

To save time, click **Generate assessment**, next to the **Assessment of the 9 criteria for the DPIA (EDPB)** title: the AI assistant suggests an answer for each criterion, with a justification, based on the information already entered in the processing activity. You review the proposal before applying it to the form, and every answer remains editable. For the detailed procedure, see the [Impact analysis](../../ropa/activity/impact-analysis.md) page.



{% hint style="info" %}
The list of processing activities requiring a DPIA depends on your national supervisory authority's recommendations. Dastra provides a DPIA Guide with country-specific recommendations to help you identify your obligations.
{% endhint %}

Dastra will display one of two results:

* **"A DPIA is not required"** — the processing does not meet the threshold
* **"You need to carry out a data protection impact assessment (DPIA)"** — a "Create a DPIA" button appears to launch the assessment directly

## PIA / DPIA templates in Dastra

Several PIA/DPIA templates are available in the Dastra library, including:

* **PIA (CNIL) - Privacy Impact Analysis** (57 questions): the standard PIA model from the French data protection authority, for a single processing activity
* **PIA (CNIL) - Privacy Impact Analysis (multi-processing)** (57 questions): the CNIL model adapted for assessments covering multiple processing activities
* **Privacy impact assessment (PIA)** (114 questions): a comprehensive generic PIA template
* **EDPB DPIA Template 2026** (82 questions): the template recommended by the European Data Protection Board
* **DPIA Template for AI Systems** (90 questions): for processing activities involving high-risk AI systems (GDPR + EU AI Act)
* **DPC DPIA Questionnaire - Ireland** (9 questions): the template from the Irish data protection authority
* **DPIA Questionnaire (ICO)** (9 questions): the template from the UK data protection authority
* **US PIA (cross-state)** (86 questions): for US-based processing activities

To access these templates, go to the "Questionnaire templates" tab and click **"Create a template"** → **"Automated questionnaires"**, then filter by type "Privacy impact".

## Structure of the PIA (CNIL) questionnaire

The PIA (CNIL) template is structured around three main parts:

1. **Context** — describe the processing activity: general information, purpose, data involved, stakeholders (controller, processors, joint controllers)
2. **Basic principles** — assess proportionality and data need, and document measures to protect individuals' rights
3. **Risks related to data security** — evaluate risks across four threat categories: security measures implemented, illegitimate access to data, unwanted modification of data, and disappearance of data

{% hint style="info" %}
The PIA (CNIL) questionnaire offers two response modes. The difference between the two modes is solely about the visibility of additional fields per question: in **Expert mode**, the **Justification of the answer**, **Attachments** and **Annotations** fields are displayed for each question. In **Simple mode**, these fields are hidden. You can switch between modes at any time.
{% endhint %}

## Linking a PIA to a processing activity

To get the most out of the PIA functionality in Dastra, configure your PIA template as follows:

1. Set the **template type** to "Impact analysis" — this enables the risk heat map in the questionnaire dashboard and integrates data from the linked processing activity.
2. In the **Assessed element** section, select "Processing activity" — this links each PIA response to a specific processing activity and automatically updates the processing activity's **Last DPIA Date** when the DPIA is published (see "Updating the last DPIA date" below).

{% hint style="info" %}
Once a PIA is linked to a processing activity, you can access it directly from the **"Impact assessment"** tab within that processing activity, and launch it with the "Create a DPIA" button when the threshold is met.
{% endhint %}



### Updating the last DPIA date

When a DPIA linked to a processing activity is published, Dastra copies its publication date into the **Last DPIA Date** field of the processing activity's **Impact assessment** step. This update applies whatever the origin of the DPIA (launched from the processing activity or scheduled from the Questionnaires module), provided the template type is "Impact analysis" and the assessed element is a processing activity.

Publication happens:

* when the last required respondent finalises the questionnaire, if the validation step is disabled;
* when the reviewers validate the questionnaire, in all other cases.

An information message flags it at publication time:

* in the **Finalize questionnaire** window: "The date of the last DPIA of the linked data processing record will be updated.", or "The date of the last DPIA of the linked data processing record will be updated once this questionnaire is validated." when a validation is expected;
* in the questionnaire validation window: "The date of the last DPIA of the linked data processing record will be updated."

When the processing activity requires a DPIA, the **Impact assessment** step then displays the message "A DPIA has been done".

{% hint style="info" %}
The publication date overwrites any value already entered in the **Last DPIA Date** field.
{% endhint %}

## Importing a PIA from the CNIL tool

If you have already conducted a PIA using the CNIL's dedicated tool, you can import it directly into Dastra:

1. Export your PIA from the CNIL tool in **.json format**
2. In Dastra, select the PIA (CNIL) template and click **"Import your CNIL PIA"**
3. A large part of the elements will be automatically imported into Dastra

## Conducting a DPIA on multiple processing activities

A single DPIA may cover several processing activities that are similar in nature, scope, context, purposes and risks. Use the **PIA (CNIL) - Privacy Impact Analysis (multi-processing)** template, or configure your template so that it is **not linked to a specific processing activity**. You can then conduct the DPIA, export it, and attach it to the documentation of the relevant processing activities.

## Go further

{% content-ref url="tia.md" %}
[tia.md](tia.md)
{% endcontent-ref %}

{% content-ref url="lia.md" %}
[lia.md](lia.md)
{% endcontent-ref %}
