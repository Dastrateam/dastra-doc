---
description: >-
  Maak een lijst van de technische en organisatorische maatregelen die uw
  gegevens beschermen en koppel ze daarna aan uw activa en verwerkingsactiviteiten.
---

# Beveiligingsmaatregelen

Beveiligingsmaatregelen zijn de technische of organisatorische voorzieningen die zijn getroffen om de gegevens te beschermen: antivirus, applicatiefirewall, toegangscontroles, een clean-deskbeleid enzovoort. In het menu heet de repository **Maatregelen**.

Voer elke maatregel één keer in, met een korte naam, zodat u hem van het ene actief of de ene verwerkingsactiviteit naar de andere kunt hergebruiken. Deze informatie staat vaak in de verwerkersovereenkomst die met een uitgever is ondertekend.

## Een beveiligingsmaatregel toevoegen

Open **Data inventory** > **Referenties** > **Maatregelen**. Klik op **Maak een maatregel** en kies daarna:

* **Create from scratch**, om met een leeg formulier te beginnen;
* **Use a template**, om een maatregel uit de bibliotheek of uit een andere werkruimte te kopiëren;
* **Genereren met de IA**, om de maatregel te beschrijven en de assistent een concept te laten opstellen (deze optie hangt af van de functies die voor uw organisatie zijn ingeschakeld).

De pijl naast **Maak een maatregel** biedt ook **Maak vanuit de bibliotheek**, **Importeren** en **Gegevenskwaliteitsinstrument**. Zie [Uw gegevens importeren (Excel, CSV)](../../general/import.md).

<figure><img src="../../../.gitbook/assets/repositories-security-measures-1.png" alt="Formulier van een beveiligingsmaatregel met de naam, het type en de beschrijving"><figcaption><p>Het formulier van een beveiligingsmaatregel</p></figcaption></figure>

## Het formulier van de beveiligingsmaatregel invullen

| Veld | Inhoud |
| --- | --- |
| **Naam maatregel** | De naam van de maatregel, verplicht. |
| **Interne referentie** | Uw referentie. |
| **Type** | **Techniek**, **Organisatorisch**, **Fysiek** of **People**. |
| **Beschrijf de maatregel** | Een vrije beschrijving. |
| **Beschrijf het potentiële risico gekoppeld aan de maatregel** | Waarvoor de maatregel dient en welk mogelijk risico ze aanpakt. |
| **URL van de documentatie van de maatregel (bijvoorbeeld op de CNIL-website)** | Het adres van de documentatie ervan, bijvoorbeeld op de website van de CNIL. |

U kunt [labels](../../general/tags.md) toevoegen en de [aangepaste velden](../../general/custom-fields.md) die voor maatregelen zijn gedefinieerd, verschijnen in het formulier.

De werkbalk van het formulier geeft toegang tot de bijgevoegde documenten, vragenlijsten en taken die aan de maatregel zijn gekoppeld, afhankelijk van uw rechten en de ingeschakelde functies. Ze bevat ook:

* **Gekoppelde elementen**: de [generieke relaties](../relationships.md) van de maatregel;
* **Gerelateerde verwerkingen**: de verwerkingsactiviteiten die de maatregel gebruiken, met de knop **Link naar gegevensverwerking** om er meer toe te voegen;
* **Historisch**;
* de werkstroomstap van de maatregel, wanneer werkstroomstappen zijn gedefinieerd.

Het actiemenu van het formulier biedt **Dupliceren**, **Samenvoegen** en **Verwijderen**.

## Beveiligingsmaatregelen in de lijst vinden

De filters zijn **Filteren op tags** en **Soorten**. Schakel **Bekijk de wezen** in om de maatregelen te tonen die noch aan een actief, noch aan een verwerkingsactiviteit zijn gekoppeld.

Bij een selectie kunt u **De werkstroomfase wijzigen**, **Velden bewerken**, **Samenvoegen**, **Exporteren** en **Verwijderen**. Zie [Elementen samenvoegen](../../general/merge.md).

## Waar beveiligingsmaatregelen worden gebruikt

* In een actief toont de sectie **Bijbehorende beveiligingsmaatregelen** de maatregelen van het actief. Zie [Activa](assets.md).
* In een verwerkingsactiviteit selecteert u de maatregelen die de verwerking beschermen en geeft u hun implementatiestatus aan. Zie [Beveiligingsmaatregelen](../../ropa/activity/security.md).

{% hint style="warning" %}
Het verwijderen van een maatregel verwijdert de verwijzingen ernaar in alle verwerkingsactiviteiten en bijlagen definitief.
{% endhint %}
