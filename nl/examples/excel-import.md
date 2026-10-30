---
description: >-
  Importeer vijf activa van Brightmoor Retail Group uit een CSV-bestand:
  kolommen, mapping, de modus Samenvoegen met een matchingveld en een aangepast
  veld.
---

# Activa importeren uit een spreadsheet

Brightmoor Retail Group houdt de lijst van zijn systemen bij in een spreadsheet. Dit voorbeeld importeert ze in de repository **Activa**. Een deel van de lijst staat al in Dastra, dus de import moet de bestaande activa bijwerken en de andere aanmaken. De methode is dezelfde voor verwerkingsactiviteiten en de andere objecten: zie [Uw gegevens importeren (Excel, CSV)](../features/general/import.md) voor de volledige referentie.

## Het voorbeeldbestand

Download het bestand: [examples-assets-import.csv](../.gitbook/assets/examples-assets-import.csv). Het is een CSV-bestand met het scheidingsteken `;` en de codering UTF-8, het formaat dat de import verwacht. Het bevat vijf rijen.

| Kolom | Inhoud | Mogelijke waarden |
| --- | --- | --- |
| `Ref` | Interne referentie, maximaal 100 tekens | Vrije tekst |
| `Label` | Naam van het actief, verplicht | Vrije tekst |
| `Type` | Categorie van het actief | `Software`, `Building`, `Network`, `Material`, `Data`, `People`, `Process`, `Algorithm` |
| `Description` | Beschrijving | Vrije tekst |
| `Address`, `ZipCode`, `City` | Locatie | Vrije tekst |
| `CountryCode` | Land, 2 tekens | ISO-code, bijvoorbeeld `DE` |
| `State` | Status van het actief | `Draft`, `Active` |
| `ApplicationType` | Type toepassing | `Software`, `WebApp`, `Saas`, `Module`, `Other` |
| `HostingType` | Hosting | `InHouse`, `OutSourced` |
| `ApplicationState` | Levenscyclus | `InProduction`, `InDevelopment`, `Stopped` |
| `CustomFields.criticality` | Een aangepast veld van de werkruimte | Vrije tekst |

De mogelijke waarden zijn in het Engels, zoals in het sjabloon. Een waarde die met geen enkele keuze overeenkomt, wordt vervangen door de standaardwaarde van de kolom: controleer ze vóór de import.

In de toepassing toont **Zie kolomindeling** in de importwizard de kolommen en waarden van uw versie.

## 1. Het aangepaste veld aanmaken

De laatste kolom voedt een aangepast veld. Maak het eerst aan.

1. Klik in de zijbalk op **Instellingen voor werkruimte**, daarna op **Aangepaste velden** en kies de module van de activa.
2. Klik op **Een veldtype maken**, geef de groep de naam "Brightmoor data" en sla op.
3. Sleep een tekstveld naar de groep. Voer "Criticality" in als label van het veld.
4. Controleer of de **Naam van de variabele (slug)** `criticality` is en sla daarna op. De slug kan achteraf niet meer worden gewijzigd.

Een aangepast veld wordt geïmporteerd via een kolom met de naam `CustomFields.` gevolgd door de slug ervan: `CustomFields.criticality`. Zie [Aangepaste velden](../features/general/custom-fields.md).

## 2. De import starten

1. Open **Data inventory** > **Referenties** > **Activa**.
2. Klik op de pijl naast de knop **Een app toevoegen** en daarna op **Importeren**.

De wizard biedt **Het bestandssjabloon downloaden** als u liever met een leeg bestand begint.

## 3. De modus Samenvoegen en het matchingveld kiezen

Het actief "Brightmoor customer portal" bestaat al in de werkruimte met de referentie `BRM-A001`. Kies in de groep **Conflictbeheer** **Samenvoegen: Overschrijven van gegevens van overeenkomende rijen (gevaarlijk!)**.

Kies daarna het **veld dat u wilt gebruiken voor het matchen van gegevens**. Voor activa zijn de matchingvelden `Ref` en `Label`. Brightmoor kiest `Ref`, dat niet verandert wanneer een actief wordt hernoemd. Een rij komt overeen met een record wanneer de waarde strikt identiek is, hoofdletters en kleine letters inbegrepen.

Met deze keuze:

* werkt rij `BRM-A001` het bestaande actief bij;
* maken de vier andere rijen nieuwe activa aan.

{% hint style="warning" %}
**Samenvoegen** vervangt de opgeslagen waarden door die van het bestand. Een lege cel laat de bestaande waarde ongewijzigd, behalve in kolommen met een verplichte keuze, zoals het type of de status, die dan hun standaardwaarde krijgen: vul ze altijd in. De bewerking kan niet ongedaan worden gemaakt.
{% endhint %}

Met **Samenvoegen** worden ook de aangepaste velden bijgewerkt. Een rij met een lege `CustomFields.criticality` laat de opgeslagen waarde ongewijzigd.

Om het bestaande actief ongewijzigd te laten, kiest u in plaats daarvan **Behoud: wijzig de gegevens die aan een voorwaarde voldoen niet**: rij `BRM-A001` wordt overgeslagen.

<figure><img src="../.gitbook/assets/examples-import-2.png" alt="Conflictbeheer met Samenvoegen geselecteerd en Ref als matchingveld"><figcaption><p>De modus Samenvoegen met het matchingveld Ref</p></figcaption></figure>

## 4. Het bestand verzenden en de kolommen koppelen

1. Klik op **Verstuur/verplaats hier bestanden** en kies het CSV-bestand. Dastra leest de eerste rijen.
2. In de stap **Correspondentie** koppelt Dastra de kolommen van het bestand aan de kolommen van de import wanneer de kop gelijk is aan de naam of het label van de kolom. De kolom **Bestandsgegevens** toont de eerste waarden van uw bestand.
3. Gebruik de tabbladen **Alle kolommen**, **Geen overeenkomst** en **Correspondentie (geïmporteerd bestand)** om de lijst te filteren. Komt een kop niet overeen, kies dan de juiste kolom in de lijst van de rij. De koppeling van `CustomFields.criticality` verschijnt zoals de andere.
4. De knop **Ga verder** blijft uitgeschakeld zolang een verplichte kolom, zoals `Label`, geen overeenkomst heeft.

<figure><img src="../.gitbook/assets/examples-import-1.png" alt="Stap Correspondentie van de activa-import met het voorbeeldbestand"><figcaption><p>De kolommen van het voorbeeldbestand, gekoppeld</p></figcaption></figure>

## 5. Het resultaat lezen

Klik op **Ga verder**. Het scherm **Resultaat** toont het aantal verwerkte, aangemaakte, bijgewerkte en overgeslagen regels. Verwacht voor het voorbeeldbestand in de modus Samenvoegen vijf verwerkte regels, vier aangemaakte activa en één bijgewerkt. Klik op **Tonen** om de lijst te openen.

Is een rij ongeldig, bijvoorbeeld een `CountryCode` die geen land is, dan stopt de hele import en wordt niets opgeslagen. De melding geeft de betrokken rij, waarbij de kop als rij 1 telt. Corrigeer het bestand en begin opnieuw.
