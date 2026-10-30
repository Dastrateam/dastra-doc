---
description: >-
  Bouw een vragenlijst over de AI-verordening waarvan de antwoorden het
  risiconiveau, de rollen en een aangepast veld van een AI-systeem bij
  Brightmoor Retail Group invullen.
---

# Vragenlijstantwoorden in een record

Brightmoor Retail Group vermeldt zijn AI-systeem "CV screening assistant" al in het register, maar de vermelding is onvolledig. Emma Walsh, de functionaris voor gegevensbescherming, wil dat de persoon die eigenaar is van de tool een vragenlijst over de AI-verordening beantwoordt, en ze wil dat de antwoorden het AI-systeem aanvullen. Dit voorbeeld bouwt die vragenlijst. De referentie is [Een record invullen met de antwoorden](../features/questionnaires/templates/record-mapping.md).

De vragenlijst vult vier velden in: de naam, het risiconiveau, de rollen van Brightmoor onder de AI-verordening en een aangepast veld met de eigenaar binnen de business.

## 1. Het aangepaste veld aanmaken

Kies in **Instellingen voor werkruimte** > **Aangepaste velden** de module van de AI-systemen en maak een tekstveld aan met het label "Business owner". Open het veld en lees de **Naam van de variabele (slug)**: `business_owner`. Die is na het aanmaken alleen-lezen. Zie [Aangepaste velden](../features/general/custom-fields.md).

## 2. Het sjabloon aanmaken

1. Maak in **Vragenlijsten** een aangepast sjabloon met de naam "AI Act intake" aan.
2. Stel **Type audit** in op **Creatie van een AI-systeem**. Het type draagt het gegevensmodel van een AI-systeem.
3. Stel **Gerelateerd aan** in op AI-systemen, zodat elk antwoord aan een AI-systeem kan worden gekoppeld.

## 3. De vragen toevoegen

Open voor elke onderstaande vraag de eigenschappen van de vraag, vink **Wilt u de naam van de variabele aanpassen (alleen voor gevorderde gebruikers)?** aan en stel de naam van de variabele in.

| Vraag | Type vraag | Naam van de variabele | Hoe ze wordt ingesteld |
| --- | --- | --- | --- |
| Name of the AI system | Korte tekst | `label` | **Selecteer een variabele om in kaart te brengen** en daarna de rij `label` |
| What is the risk level of this AI system? | Selectievakjeslijst (slechts één antwoord) | `riskLevel` | **Selecteer een variabele om in kaart te brengen** en daarna de rij `riskLevel` |
| What is the role of Brightmoor? | Lijst op maat | `responsibilities` | **Selecteer een variabele om in kaart te brengen** en daarna de rij `responsibilities` |
| Role (subvraag van de lijst) | Selectievakjeslijst (slechts één antwoord) | `responsibilityType` | Met de hand getypt |
| Who owns this AI system in the business? | Korte tekst | `custom_business_owner` | Met de hand getypt: `custom_` en de technische naam |

Drie punten om te weten:

* Voor `riskLevel` maakt het kiezen van het veld één antwoord per waarde aan: Low, Medium, High en Unacceptable, met precies deze namen van variabelen. Wijzig de labels naar wens, bijvoorbeeld Minimal, Limited, High en Unacceptable, en behoud de namen van de variabelen.
* Voor de rollen zijn de zes waarden van de AI-verordening Provider, Deployer, Distributor, Importer, AuthorizedRepresentative en Manufacturer. Voeg één antwoord per rol toe aan de subvraag, met de waarde als naam van de variabele van het antwoord.
* Het aangepaste veld staat niet in de lijst van variabelen, daarom wordt de naam ervan volledig getypt.

Sla het sjabloon op.

<figure><img src="../.gitbook/assets/examples-questionnaire-1.png" alt="Venster Selecteer een variabele om in kaart te brengen met de velden van een AI-systeem"><figcaption><p>De variabelen die voor een AI-systeem worden aangeboden</p></figcaption></figure>

## 4. Het antwoord aan het AI-systeem koppelen en de antwoorden verzamelen

1. Plan de vragenlijst. Selecteer bij **Auditobject** het AI-systeem "CV screening assistant". Zie [Een audit of PIA plannen](../features/questionnaires/schedule.md).
2. Liam O'Connor antwoordt: naam "CV screening assistant", risiconiveau **Hoog** (een wervingstool is een toepassing met een hoog risico volgens bijlage III van de AI-verordening), rol **Deployer**, eigenaar binnen de business "Sophie Becker, HR".
3. Het antwoord wordt gevalideerd en gepubliceerd.

## 5. De antwoorden samenvoegen in het AI-systeem

Omdat het antwoord aan een bestaand AI-systeem is gekoppeld, ziet de eigenaar ervan de knop **Gegevens samenvoegen**.

1. Klik op **Gegevens samenvoegen**. Het voorbeeld toont het AI-systeem dat uit de antwoorden is opgebouwd. Kies de **Organisatie-eenheid** en klik op **Bestaande maken en samenvoegen**.
2. Vergelijk in het samenvoegvenster het bestaande AI-systeem met het tijdelijke, met het label "CV screening assistant (From Questionnaire)". Behoud de waarden van de vragenlijst voor `riskLevel`, de rollen en het aangepaste veld en behoud de bestaande waarden voor de rest.
3. Bevestig het samenvoegen.

| Veld | Voor | Na |
| --- | --- | --- |
| Risiconiveau | Leeg | Hoog |
| Rollen | Geen | Deployer |
| Business owner (aangepast veld) | Leeg | Sophie Becker, HR |

Het AI-systeem bevat nu de antwoorden. Vóór stap 3 is niets gewijzigd: de antwoorden werken nooit zelf een record bij.

Bestond het AI-systeem niet, dan zou het antwoord geen gekoppeld record hebben. De knop zou **Aanmaak verzoek** heten en **Creëren** zou het AI-systeem aan het register toevoegen.

<figure><img src="../.gitbook/assets/examples-questionnaire-2.png" alt="Pagina van de samenvoegaanvraag met het voorbeeld van het AI-systeem en de knop Bestaande maken en samenvoegen"><figcaption><p>De samenvoegaanvraag van een antwoord</p></figcaption></figure>
