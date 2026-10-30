---
description: >-
  Ontdek wat bewaartermijnen zijn.
---

# Bewaartermijn van gegevens

## Definitie

Bewaartermijnen zijn een van de grondbeginselen van de bescherming van persoonsgegevens. Ze vloeien voort uit het beginsel van opslagbeperking (artikel 5, lid 1, onder e), van de AVG) en dragen bij aan het recht op wissing.

Belangrijkste artikelen:

* artikel 5 van de AVG (opslagbeperking);
* artikel 30 (documentatie in het verwerkingsregister);
* artikelen 13 en 14 (informatie aan betrokkenen).

Concreet moet u voor elke verwerkingsactiviteit bepalen:

* een vaste termijn (of een reeks termijnen per fase),
* en/of een objectief criterium om die te berekenen (bijvoorbeeld "+3 jaar na het laatste actieve contact").

*

## De levenscyclus van gegevens

De bewaring is georganiseerd in opeenvolgende fasen. Deze levenscyclus bepaalt uw bewaarregels.

| Fase                                | Doel                              | Toegang                          | Voorbeeld van een termijn                    |
| ----------------------------------- | --------------------------------- | -------------------------------- | -------------------------------------------- |
| **Actief gebruik**                  | Operationeel gebruik              | Breed (zakelijk team)            | Duur van het contract + uitvoering           |
| **Tussentijdse archivering**        | Bewijs / verdediging van een recht | Beperkt (need-to-know)           | Wettelijke verjaringstermijn (bijv. 5 jaar)  |
| **Definitieve archivering** (publiek) | Historisch belang               | Zeer beperkt                     | Overdracht / selectie door de archiefdiensten |
| **Anonimisering**                   | Statistieken / onderzoek          | Niet-identificerende gegevens    | Onbeperkt als echt onomkeerbaar              |
| **Verwijdering**                    | Einde van de levenscyclus         | Niet van toepassing              | Aan het einde van de fasen                   |

{% hint style="info" %}
De richtsnoeren van uw nationale gegevensbeschermingsautoriteit over bewaartermijnen gaan doorgaans over: het bijhouden van registers, referentiedocumenten, procedures voor archivering en vernietiging, instructies aan verwerkers enzovoort.
{% endhint %}

*

## Hoe bepaalt u ze (methodologie)

1. **De doeleinden verduidelijken**: Wat doet u precies met de gegevens? Waarvoor worden ze gebruikt?
2. **De fasen in kaart brengen**: actief gebruik, daarna tussentijdse archivering, daarna anonimisering/verwijdering
3. **De rechtsgronden en referenties identificeren**: sectorspecifieke wet- en regelgeving, richtsnoeren van de autoriteit, interne referentiekaders
4. **Een duidelijke regel vaststellen**: "X jaar na \[gebeurtenis], daarna Y jaar archiveren, daarna verwijderen" of "zolang…, daarna Z jaar na / \[criterium]"
5. **De uitvoering organiseren**: automatische of beheerde verwijdering, logging, bewijs van uitvoering
6. **Informeren en documenteren**: privacyverklaring (art. 13-14), verwerkingsregister (art. 30), intern beleid

{% hint style="info" %}
Is er geen duidelijke referentie, kies dan een termijn die evenredig is aan het doeleinde en documenteer de redenering (verantwoordingsplicht).
{% endhint %}

*

## Voorbeeldregels (aan te passen)

| Context          | Gegevens                            | Samengevatte regel                                                             |
| ---------------- | ----------------------------------- | ------------------------------------------------------------------------------ |
| B2B-prospects    | Identiteit, contactgegevens, opt-in-spoor | **3 jaar** na het laatste actieve contact, daarna **verwijdering**         |
| HR, kandidaten   | Cv's, motivatiebrieven, gesprekken  | **2 jaar** na het laatste contact met de kandidaat, tenzij bezwaar             |
| Klanten          | Contract, facturatie                | Contract + **5 jaar** (bewijs), daarna **archivering/verwijdering**            |
| Camerabewaking   | Beelden                             | **maximaal 30 dagen**, behalve bij een incident (bewijsprocedure)              |
| Cookies          | Identificatiegegevens, voorkeuren   | Termijn in overeenstemming met de cookiebanner en het **bewijs van toestemming** |

> Deze waarden verschillen naargelang de toepasselijke teksten, uw sector en uw risico's: documenteer uw keuzes.

*

## Wie betrekt u erbij

* Verantwoordelijke van de verwerking binnen de business: operationele behoeften, aanleidingen
* FG / juridische dienst: naleving, toepasselijke teksten, afweging van rechten en vrijheden
* CISO / IT: verwijdering, anonimisering, beperking van de toegang, logs
* Verwerkers: naleving van de schriftelijke instructies

*

## De uitvoering controleren (audits)

* Controleer periodiek: de relevantie van de termijnen, de uitvoering van verwijderingen, de toegang tot archieven, de anonimisering
* Registreer de handelingen: vernietigingsverslagen, verslagen van verwijderingen, logs
* Herzie bij elke wijziging van doeleinde, rechtsgrond of leverancier

*

## Uitvoering in Dastra

### 1) In het verwerkingsregister

* Geef per dataset een leesbare regel op: "_3 jaar na het laatste actieve contact (prospect), daarna verwijdering_"
* Voeg het aanleidende criterium toe (bijvoorbeeld "datum van de laatste CRM-activiteit", "einddatum van het contract")
* Koppel referenties (wettekst, intern referentiekader)

### 2) De verwijdering automatiseren/beheren

* Plan taken (beoordelingen, verwijderingen, bewijsextracties)
* Gebruik werkstroomregels en regelmatige beoordelingen voor de termijnen

### 3) Bewijs

* Bewaar vernietigingsverslagen, verslagen van verwijderingen, scripts en uitvoeringstickets in de sectie **Documentatie** van de verwerkingsactiviteit

*

## Tussentijdse archivering en beveiliging

* Beperk de toegang (RBAC, compartimentering)
* Registreer raadplegingen
* Logische scheiding (archiefkluis/-zone)
* Versleutel waar relevant
* Plan omkeerbaarheid met verwerkers

*

## Anonimisering versus pseudonimisering

* Anonimisering: onomkeerbaar → buiten het toepassingsgebied van de AVG als de gegevens echt niet opnieuw kunnen worden geïdentificeerd
* Pseudonimisering: omkeerbaar met een sleutel → blijft persoonsgegevens → Documenteer de methode, test de heridentificeerbaarheid en houd rekening met aanvullende gegevens.

*

## AI en bewaartermijnen

Bepaal voor AI-systemen afzonderlijke bewaartermijnen voor:

* Training (datasets, versies),
* Validatie / testen,
* Inferentielogs (traceerbaarheid, transparantie),
* Evaluatiesets (bias, robuustheid).

Koppel deze termijnen aan uw register van AI-systemen om de consistentie tussen de AVG en de AI-verordening te waarborgen.

*

## Nuttige referenties

* Richtsnoeren over bewaring die uw nationale toezichthoudende autoriteit publiceert (bijvoorbeeld de gids van de CNIL over bewaartermijnen in Frankrijk)
* Sectorspecifieke wet- en regelgeving die minimale of maximale bewaartermijnen vastlegt
* Gedragscodes en normen van uw sector
* Collectieve arbeidsovereenkomsten

*

{% hint style="success" %}
**Goede praktijk:** schrijf _uitvoerbare_ regels ("X jaar na \[gebeurtenis], daarna verwijdering of anonimisering"), test ze op een beperkte reikwijdte en rol ze daarna breed uit. Dastra helpt u de uitvoering te **documenteren**, te **plannen** en te **bewijzen**.
{% endhint %}

*

## Meer informatie

{% content-ref url="../../features/ropa/activity/datasets.md" %}
[Gegevens en retentie](../../features/ropa/activity/datasets.md)
{% endcontent-ref %}

{% content-ref url="../../features/tasks/README.md" %}
[Planning](../../features/tasks/README.md)
{% endcontent-ref %}
