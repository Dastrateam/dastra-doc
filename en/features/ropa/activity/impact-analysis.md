---
description: Assess the privacy impact of the processing.
---

# Impact assessment

The **Impact assessment** section helps you assess in a simple way whether your processing must be subject to a data protection impact assessment (DPIA), as provided for by [Article 35 of the GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj#d1e3546-1-1).

This section is only available for **Data controller** processing activities.

What is a DPIA? A process to assess the necessity and proportionality of the processing and to manage its risks.

Under what conditions should I carry out a DPIA? When the processing is likely to result in a high risk to the rights and freedoms of the data subjects. The European Data Protection Board (EDPB) has clarified the scope of this requirement. Specifically, if the processing meets at least two of the following criteria, a DPIA is required:

* Evaluation or scoring
* Automated decision-making with legal or similar significant effect
* Systematic monitoring
* Sensitive data or data of a highly personal nature
* Data processed on a large scale
* Matching or combining of datasets
* Data concerning vulnerable data subjects
* Innovative use or application of new technological or organizational solutions
* Processing that prevents data subjects from exercising a right or using a service or a contract

Sometimes, for a processing that is particularly sensitive for the data subjects, a single criterion may be enough.

## Fill in the Impact assessment section

1. If the processing belongs to a type of processing for which a supervisory authority does not require a DPIA, answer **Yes** to **A DPIA for this kind of processing operations is exempted by a supervisory authority?** and explain why in **Please explain why a DPIA is not required**. The criteria are then hidden.
2. Otherwise, answer **No**, and if a DPIA has already been carried out, enter its date in **Last DPIA Date**.
3. Under **Assessment of the 9 criteria for the DPIA (EDPB)**, answer **Not applicable**, **No** or **Yes** for each criterion. Hover over the information icon next to a criterion to display examples.

The criteria are displayed in the application as follows:

* **Evaluation or scoring including profiling and prediction activities**
* **Automated decision making with significant effects**
* **Systematic monitoring**
* **special categories data**
* **Data processed on a large scale**
* **Combining, linking or cross-referencing**
* **Data concerning vulnerable data subjects**
* **Innovation and technology**
* **Rights and contractual obligations**

As soon as you answer **Yes** to at least two criteria, Dastra considers that a DPIA is required. If you use [questionnaires](../../questionnaires/README.md), a message at the top of the section then reminds you that **You need to carry out a data protection impact assessment (DPIA)**, with a **Create a DPIA** button to start a [DPIA questionnaire](../../questionnaires/types/dpia.md). Once the date of the DPIA is entered, the message becomes **A DPIA has been done** and reminds you to renew it regularly. When the criteria are answered and fewer than two are met, or when the processing is exempted, Dastra displays **A DPIA is not required**.

{% hint style="info" %}
The list of processing operations concerned depends on the recommendations of your national supervisory authority. See our [DPIA guidance, country by country](../../../other/dpia-by-country.md) to identify your obligations.
{% endhint %}

## Generate the assessment with the AI assistant

The AI assistant can suggest an answer for each of the 9 criteria based on the information already entered in the processing activity: name, description, purposes, data subject categories, personal data categories, assets and recipients.

<figure><img src="../../../.gitbook/assets/ropa-impact-analysis-1.png" alt="Generate assessment button next to the Assessment of the 9 criteria for the DPIA (EDPB) title in the Impact assessment section"><figcaption><p>The Generate assessment button starts the analysis of the 9 criteria by the AI assistant</p></figcaption></figure>

1. In the **Impact assessment** section of the processing activity, click **Generate assessment**, next to the **Assessment of the 9 criteria for the DPIA (EDPB)** title.
2. Check the **Data shared with the AI model** section: it lists the information from the processing activity that is sent to the assistant.
3. Click **Generate**.
4. Review the proposal: for each criterion, the assistant gives an answer (Yes, No or Not applicable) with a justification, along with a confidence score for the analysis. Where relevant, the **Missing information that could change the assessment** section lists the items to complete in the record to make the result more reliable.
5. Click **Apply to the form** to copy the answers into the section, or **Back** to return to the previous screen.

You stay in control of every answer: once applied, each criterion can still be edited individually. The assistant's proposal supports your analysis and does not replace your own assessment.

## Lists published by the supervisory authorities

In addition, supervisory authorities publish a list of the types of processing for which a DPIA is mandatory, and may publish a list of the types of processing for which a DPIA is not required.

The French CNIL has published these two lists (in French), which can be accessed here:

[List of types of processing for which a DPIA is not required](https://www.cnil.fr/sites/default/files/atoms/files/liste-traitements-aipd-non-requise.pdf)

[List of types of processing for which a DPIA is mandatory](https://www.cnil.fr/sites/default/files/atoms/files/liste-traitements-aipd-requise.pdf)

Note that [Article 30 of the GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj#d1e3265-1-1) does not require you to specify whether a DPIA has been carried out on the processing.
