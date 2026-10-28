---
description: Make an inventory of the data flowing outside the EU.
---

# Data transfers outside the EU

A transfer can be defined as any communication, copy or movement of personal data intended to be processed in a country outside the European Union.

Data transfers outside the European Union are prohibited in principle.

[Articles 44 to 49 of the GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj#d1e4227-1-1) provide for exceptions to this prohibition. They provide for the use of tools that frame the transfer:

* an adequacy decision of the European Commission regarding certain countries ensuring an adequate level of protection;
* standard contractual clauses (SCC) of the European Commission;
* binding corporate rules (BCR);
* specific contractual clauses (considered compliant with the European Commission's model clauses);
* standard contractual clauses adopted by a supervisory authority and approved by the European Commission;
* an approved code of conduct (including a binding and enforceable commitment by the non-EU recipients to apply appropriate safeguards);
* an approved certification mechanism (including a binding and enforceable commitment by the non-EU recipients to apply appropriate safeguards);
* an administrative arrangement or a legally binding and enforceable instrument adopted to enable cooperation between public authorities (Memorandum of Understanding or MoU, international convention, etc.).

Derogations are provided for in [Article 49 of the GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj#d1e4535-1-1). If a derogation justifies the transfer, the nature of the derogation must be indicated and, if necessary, the assessment of the circumstances of the transfer and the appropriate safeguards must be detailed.

## Declare a transfer in Dastra

Transfers are declared on each recipient, in the **Recipients** section of the processing activity.

1. Open the recipient, or create a new one with **New recipient**.
2. At the bottom of the recipient panel, click **Create a transfer**.
3. Fill in the **Edit a data transfer** panel:
   * **Description of the data transfer** (optional);
   * **Country**: the country the data is transferred to;
   * **Data transfer mechanism** (required): the tool that frames the transfer;
   * **Description of the data transfer mechanism** (optional), for example to detail a derogation.
4. Click **Add** in the transfer panel, then click **Add** (or **Edit** for an existing recipient) in the recipient panel.

The **Data transfer mechanism** list offers the following options:

* **Undefined**
* **Transfer regulated by the GDPR**
* **EU standard contractual clauses**
* **Binding corporate rules**
* **Adequacy decision**
* **Derogation (art. 49)**
* **Standard data protection clauses adopted by a supervisory authority**
* **Approved code of conduct**
* **Approved certification mechanism**
* **Contractual clauses authorized by a supervisory authority**
* **administrative arrangements authorized by a supervisory authority**
* **International agreement**
* **Other**

The transfers of a recipient are listed in its panel with their **Country**, their description and their **Data transfer mechanism**, and are summarized in the **Transfers** column of the list of recipients.

{% hint style="info" %}
When the stakeholder or the organizational unit you select as a recipient is located in another country, Dastra suggests adding a transfer to this country: click **Add** in the suggestion.
{% endhint %}

## Go further

* If you use [questionnaires](../../../questionnaires/README.md), Dastra suggests creating a transfer impact assessment (TIA) as soon as a transfer is declared: **Create a transfer impact questionnaire (TIA)**.
* If you use the Contracts module, the **SCC transfer** button of a recipient generates the standard contractual clauses for its transfers (see [Recipients](README.md#generate-a-dpa)).
* A transfer to a country without an adequate level of protection increases the **Sensitivity** indicator of the processing activity.
* All the transfers of your processing activities can be viewed on the [transfers map](../../visualization/transfers-map.md).
