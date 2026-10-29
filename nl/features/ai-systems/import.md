---
description: >-
  Importeer uw bestaande register van AI-systemen in Dastra vanuit een CSV- of
  Excelbestand, met het verwachte formaat van elke kolom.
---

# Uw AI-systemen importeren

Als u al een register van AI-systemen hebt, importeert u het in Dastra in plaats van alles met de hand in te voeren.

1. Klik op **AI-wet** in de zijbalk en daarna op **Register van AI-systemen**.
2. Open rechtsboven het menu van de knop **Een nieuw AI-systeem creëren** en klik op **Importeren**.
3. Voeg op de pagina die opent uw bestand toe onderaan de pagina.

<figure><img src="../../.gitbook/assets/ai-systems-import-1.png" alt="Menu van de knop Een nieuw AI-systeem creëren met de acties Maak vanuit de bibliotheek, Importeren en Exporteren"><figcaption><p>De actie Importeren in het menu van het register van AI-systemen</p></figcaption></figure>

Voor de details van de procedure raadpleegt u [Uw gegevens importeren (Excel, CSV)](../general/import.md).

## Bestandsformaat

Het bestand bevat een koprij met de kolomnamen die hieronder worden beschreven. Alle kolommen zijn optioneel, behalve `Label`.

Kolommen met een opsomming verwachten precies de waarden uit de kolom "Toegestane waarden". Hoofdletters maken niet uit. Een waarde die met geen enkele toegestane waarde overeenkomt, wordt genegeerd.

| Kolom | Beschrijving | Type | Beperkingen | Toegestane waarden |
| --- | --- | --- | --- | --- |
| `Label` | Naam van het systeem | Tekst | Verplicht, 1 tot 120 tekens | Vrije tekst |
| `Ref` | Interne referentie | Tekst | Maximaal 50 tekens | Vrije tekst |
| `Description` | Beschrijving van het systeem | Tekst | Maximaal 4.000 tekens | Vrije tekst |
| `State` | Status van het systeem | `AiSystemState` | | `Draft`, `Cancelled`, `Pending`, `Active` |
| `RiskLevel` | Risiconiveau | `AiSystemRiskLevel` | | `Low`, `Medium`, `High`, `Unacceptable` |
| `RiskLevelJustification` | Motivering van het risiconiveau | Tekst | | Vrije tekst |
| `BenefitLevel` | Niveau van de bedrijfswaarde | `AiSystemBenefitLevel` | | `Low`, `Medium`, `High` |
| `BenefitLevelJustification` | Motivering van de bedrijfswaarde | Tekst | | Vrije tekst |
| `DateArchived` | Datum van verplaatsing naar de prullenbak | Datum | Formaten `DD-MM-YYYY` of `DD/MM/YYYY` | Datum |
| `DateCreation` | Aanmaakdatum | Datum | Hetzelfde formaat | Datum |
| `DateUpdate` | Datum van de laatste wijziging | Datum | Hetzelfde formaat | Datum |
| `DateDeployment` | Datum van ingebruikname | Datum | Hetzelfde formaat | Datum |
| `DateRetirement` | Datum van buitengebruikstelling | Datum | Hetzelfde formaat | Datum |
| `TransparencyNoticeDone` | Er is een transparantiebericht verstrekt | Boolean | | `true` of `false` |
| `TransparencyNoticeHtml` | Inhoud van het bericht | Tekst | | HTML |

### Overeenkomst met de labels in de toepassing

De waarden in het bestand zijn de technische namen, niet de labels die in de toepassing worden getoond. Schrijf het label van het scherm niet in het bestand.

| Kolom | Waarde in het bestand | Getoond label |
| --- | --- | --- |
| `State` | `Draft` | Draft |
| `State` | `Pending` | In de wacht |
| `State` | `Active` | In uitvoering |
| `State` | `Cancelled` | Geannuleerd |
| `RiskLevel` | `Low` | Minimaal |
| `RiskLevel` | `Medium` | Beperkt risico |
| `RiskLevel` | `High` | Hoog risico |
| `RiskLevel` | `Unacceptable` | Onaanvaardbaar |
| `BenefitLevel` | `Low` | Laag |
| `BenefitLevel` | `Medium` | medium |
| `BenefitLevel` | `High` | Hoog |

## Voorbeeldrij

```
"Internal ChatGPT","SYS-001","Internal documentation assistant model","Active","Medium","Moderate risks with responsible use","High","Very high business value","01/02/2024","15/01/2024","01/03/2024","20/03/2024","","false","<p>This AI system is used to assist employees in drafting internal documents.</p>"
```

## Kant-en-klaar sjabloon voor de koprij

Kopieer deze regel in een leeg `.csv`-bestand:

```
Label,Ref,Description,State,RiskLevel,RiskLevelJustification,BenefitLevel,BenefitLevelJustification,DateArchived,DateCreation,DateUpdate,DateDeployment,DateRetirement,TransparencyNoticeDone,TransparencyNoticeHtml
```
