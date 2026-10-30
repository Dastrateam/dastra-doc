---
description: >-
  Ontdek hoe u meldingen van datalekken beheert.
---

# Meldingen van datalekken

## Definitie

Volgens [artikel 4, lid 12 van de AVG](https://gdpr-info.eu/art-4-gdpr/) is een **inbreuk in verband met persoonsgegevens**:

> _Een inbreuk op de beveiliging die per ongeluk of op onrechtmatige wijze leidt tot de vernietiging, het verlies, de wijziging of de ongeoorloofde verstrekking van of de ongeoorloofde toegang tot doorgezonden, opgeslagen of anderszins verwerkte gegevens._

Het gaat met andere woorden om elk **beveiligingsincident**, **opzettelijk of onopzettelijk**, dat het volgende in gevaar brengt:

* **Vertrouwelijkheid** (ongeoorloofde toegang, openbaarmaking),
* **Integriteit** (wijziging, vervalsing),
* **Beschikbaarheid** (verlies, verwijdering, onbeschikbaarheid).

***

## Typische voorbeelden

* Het per ongeluk wissen van medische gegevens waarvan elders geen back-up bestaat.
* Het verlies van een niet-versleutelde USB-stick met een klantendatabase.
* Een hack van een server waarbij e-mailadressen en wachtwoorden zichtbaar worden.
* Een e-mail met persoonsgegevens die naar de verkeerde ontvanger wordt gestuurd.
* HR-informatie die wordt openbaar gemaakt op een onbeveiligde gedeelde ruimte.

***

## Drie hoofdtypen van inbreuken

| Type                | Beschrijving                                  | Voorbeeld                         |
| ------------------- | --------------------------------------------- | --------------------------------- |
| **Vertrouwelijkheid** | Ongeoorloofde toegang of openbaarmaking     | Openbaarmaking via phishing       |
| **Integriteit**     | Ongeoorloofde wijziging of vervalsing         | Wijziging van een medisch dossier |
| **Beschikbaarheid** | Onopzettelijk verlies of onopzettelijke vernietiging | Gegevens verwijderd zonder back-up |

***

## Wettelijke verplichtingen van de verwerkingsverantwoordelijke

### Melding aan de toezichthoudende autoriteit

* **Termijn**: indien mogelijk uiterlijk 72 uur nadat u kennis hebt genomen van de inbreuk. Een melding is niet vereist wanneer het onwaarschijnlijk is dat de inbreuk een risico inhoudt voor de rechten en vrijheden van personen.
* **Inhoud**:
  * de aard van de inbreuk,
  * de categorieën en de hoeveelheid betrokken gegevens,
  * de waarschijnlijke gevolgen,
  * de genomen of geplande maatregelen.

> Kan de melding niet binnen 72 uur worden gedaan, dan moet de **vertraging worden gemotiveerd**.

Referentie: [artikel 33 van de AVG](https://gdpr-info.eu/art-33-gdpr/)

***

### Mededeling aan de betrokkenen

Als de inbreuk **een hoog risico inhoudt voor de rechten en vrijheden van personen**, moeten zij **onverwijld** worden geïnformeerd over:

* de aard van de inbreuk,
* de betrokken gegevens,
* de genomen maatregelen,
* aanbevelingen om de gevolgen te beperken (bijvoorbeeld het wachtwoord wijzigen).

Referentie: [artikel 34 van de AVG](https://gdpr-info.eu/art-34-gdpr/)

***

### Verplichte interne documentatie

Ook wanneer geen melding vereist is, moet **elke inbreuk worden vastgelegd** in een intern register dat het volgende bevat:

* de feiten met betrekking tot de inbreuk,
* de gevolgen ervan,
* de genomen corrigerende maatregelen.

> Dit register **toont de naleving aan** (verantwoordingsplicht).

***

## De cyclus voor het beheer van inbreuken

1. **Detectie** → identificatie van een incident of afwijkend gedrag.
2. **Kwalificatie** → nagaan of er persoonsgegevens bij betrokken zijn.
3. **Risicobeoordeling** → impact op de privacy van personen.
4. **Melding (indien vereist)** → toezichthoudende autoriteit binnen 72 uur, betrokkenen bij een hoog risico.
5. **Herstel** → corrigerende en preventieve maatregelen.
6. **Documentatie** → vermelding in het register van inbreuken.
7. **Geleerde lessen** → organisatorische of technische aanpassingen.

***

## Best practices voor beveiliging

* Stel een **incidentbeheerplan** op en test het regelmatig.
* Train teams in het **snel detecteren en doorgeven** van incidenten.
* Zet **preventieve maatregelen** in (MFA, netwerksegmentatie, back-ups).
* Gebruik een **gecentraliseerd register** om elke inbreuk en de afhandeling ervan op te volgen.
* Beoordeel de ernst met een **gestandaardiseerd risicoraster** (bijvoorbeeld een raster van uw toezichthoudende autoriteit, of ISO/IEC 27005).

***

## Inbreuken beheren in Dastra

De module **Incidenten** van Dastra documenteert en volgt inbreuken in verband met persoonsgegevens op:

| Stap         | Functie van Dastra                                                                                                    |
| ------------ | --------------------------------------------------------------------------------------------------------------------- |
| Declaratie   | Inbreukdossier in het register van incidenten                                                                         |
| Beoordeling  | Risiconiveau berekend op basis van de waarschijnlijkheid van identificatie en de ernst van de gevolgen                |
| Melding      | Opvolging van de melding aan de autoriteit (aftelling van 72 uur) en van de mededeling aan personen                   |
| Opvolging    | Gekoppelde taken, maatregelen die na het incident zijn genomen, post-mortem en geschiedenis                           |
| Rapportage   | Pagina **Statistieken** met indicatoren over incidenten                                                               |

***

## Nuttige bronnen

* [ICO: reporting a data breach](https://ico.org.uk/for-organizations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/personal-data-breaches/)
* [ENISA: the EU Agency for Cybersecurity](https://www.enisa.europa.eu/)
* [ISO/IEC 27035: information security incident management](https://www.iso.org/standard/60803.html)

***

{% hint style="success" %}
Goede praktijk: een snel gemeld incident beperkt de impact, versterkt de transparantie en toont aan dat u de naleving beheerst. Dastra helpt u elke stap van het proces te structureren en te documenteren.
{% endhint %}

***

## Meer informatie

{% content-ref url="../../features/incidents/README.md" %}
[Inbreuken](../../features/incidents/README.md)
{% endcontent-ref %}

{% content-ref url="../../features/incidents/document-breach.md" %}
[Een nieuw inbreuk documenteren](../../features/incidents/document-breach.md)
{% endcontent-ref %}
