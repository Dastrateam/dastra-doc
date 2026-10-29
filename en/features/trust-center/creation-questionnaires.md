---
description: >-
  Collect processing activity, incident, asset, contract, AI system or
  stakeholder projects from a Trust Center with creation questionnaire
  templates.
---

# Collect processing activity, incident, asset, contract, AI system or stakeholder projects from a Trust Center

Questionnaire templates are designed to work with a Trust Center. They work like other templates, but once the response is validated, its data can be turned into a Dastra object. Six template types exist:

* **Data processing project**: a processing activity;
* **Data breach creation request**: a data breach;
* **Asset creation**: an asset of the repository;
* **Contract creation**: a contract;
* **AI System creation**: an AI system;
* **Stakeholder creation**: a stakeholder.

## Add a template

1. In the Questionnaires module, open the **Questionnaire templates** list and click **Create a template**.
2. In the **Choose a questionnaire template type** window, choose **Automated questionnaires**.
3. In the library, filter by **Types** or search for the template you want, then click it.

The template is added to your workspace and you are redirected to its management page. To offer it to visitors, add it to your Trust Center afterwards: see [Questionnaires](configuration/questionnaires.md). For the details of creating a template, see [Create a questionnaire template](../questionnaires/templates/README.md).

## Template content

Each template includes a list of questions that cover the fields needed to create the matching object in Dastra.

## Turn a response into an object

Responses given from the Trust Center arrive in the Questionnaires module, in the Trust Center's organizational unit. The conversion button only appears when the response is validated. It is active for the approvers of the response.

On the page of the validated response, the button is called:

* **Creation request** followed by the object type, for example **Creation request (Processing activity)**, as long as the response is not linked to an object;
* **Merge request** followed by the object type, when the response is already linked to an object.

Each response is linked to the matching field of the object. For the full procedure, see [Merging responses into the linked object](../questionnaires/monitor.md#merging-responses-into-the-linked-object).

## Modify the template

Each question is linked to a field of the object to create, so modifying the template can prevent responses from being converted. We recommend using the template as it is provided in the library.
