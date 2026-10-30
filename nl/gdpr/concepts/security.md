---
description: >-
  Ontdek welke beveiligingsmaatregelen de AVG vereist.
---

# Beveiligingsmaatregelen

De AVG (artikel 32) verplicht verwerkingsverantwoordelijken en verwerkers om de beveiliging van persoonsgegevens te waarborgen via passende technische en organisatorische maatregelen. Deze maatregelen moeten evenredig zijn aan de risico's van de verwerking, aan de aard van de gegevens en aan de nagestreefde doeleinden.

> Doel: de vertrouwelijkheid, integriteit, beschikbaarheid en veerkracht van systemen en gegevens waarborgen.

*

## Een risicogebaseerde aanpak

Voordat u maatregelen kiest, moet u:

1. De te beschermen elementen identificeren (gegevens, systemen, stromen).
2. De bedreigingen en kwetsbaarheden beoordelen (menselijke fout, aanval, storing enzovoort).
3. De mogelijke gevolgen bepalen (verlies, openbaarmaking, wijziging…).
4. Passende maatregelen kiezen om deze risico's tot een aanvaardbaar niveau terug te brengen.

> De AVG schrijft geen vaste lijst van maatregelen voor: ze vereist maatregelen die passen bij het risico (artikel 32), rekening houdend met de stand van de techniek, de uitvoeringskosten en de aard, de omvang, de context en de doeleinden van de verwerking. Elke organisatie moet haar aanpak aanpassen aan haar context en kunnen aantonen dat ze dat doet.

*

## Categorieën van beveiligingsmaatregelen

### Technische maatregelen

Technische maatregelen werken rechtstreeks in op informatiesystemen.

| Domein                                | Voorbeelden                                                                         |
| ------------------------------------- | ----------------------------------------------------------------------------------- |
| **Toegangsbeheer**                    | Sterke authenticatie (MFA), beheer van rechten, logging                             |
| **Versleuteling**                     | Gegevens in rust en tijdens het transport, TLS-certificaten, beheerde en vernieuwde sleutels |
| **Pseudonimisering / anonimisering**  | Logische scheiding, hashing, tokens                                                 |
| **Back-ups en veerkracht**            | Regelmatige back-ups, hersteltests, redundantie                                     |
| **Toepassingsbeveiliging**            | Penetratietests, patches, hardening van servers                                     |
| **Monitoring**                        | SIEM, waarschuwingen bij abnormale toegang, detectie van incidenten                 |

*

### Organisatorische maatregelen

Organisatorische maatregelen structureren de governance en het interne gedrag.

| Domein                          | Voorbeelden                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------ |
| **Beveiligingsbeleid**          | IT-handvest, governance van informatiebeveiliging, plan voor incidentbeheer    |
| **Opleiding en bewustmaking**   | Interne campagnes, e-learningmodules, phishingsimulaties                       |
| **Beheer van derden**           | Contractuele clausules, audits van verwerkers, regelmatige beoordelingen       |
| **Interne procedures**          | Autorisatieproces, bedrijfscontinuïteitsplan, periodieke beoordeling           |

*

### Fysieke maatregelen

Fysieke maatregelen beschermen gebouwen, apparatuur en dragers.

| Domein                       | Voorbeelden                                                      |
| ---------------------------- | ---------------------------------------------------------------- |
| **Fysieke toegang**          | Badgecontrole, camerabewaking, beperkte zones                    |
| **Bescherming van hardware** | Kluizen, beveiligde racks, noodstroomvoorzieningen               |
| **Veilige vernietiging**     | Versnipperen, gecertificeerd wissen, beheer van IT-afval         |

*

## Beheercyclus van de beveiliging

1. **Identificeren**: gegevens, systemen, kwetsbaarheden, bedreigingen.
2. **Beoordelen**: risico's en mogelijke gevolgen.
3. **Beschermen**: beveiligingsmaatregelen definiëren en toepassen.
4. **Opvolgen**: incidenten detecteren, controles auditen.
5. **Verbeteren**: acties corrigeren, versterken en documenteren.

*

## Beveiligingsmaatregelen in Dastra

In Dastra kunt u beveiligingsmaatregelen documenteren, beoordelen en opvolgen als onderdeel van de governance van de AVG en de AI-verordening:

* Beschrijf uw maatregelen in de repository **Maatregelen** en koppel ze aan verwerkingsactiviteiten, activa en datalekken.
* Beoordeel risico's met de module voor risicobeheer.
* Plan corrigerende acties met taken en volg hun voortgang.
* Bewaar het bewijs van naleving (beleid, audits, bewijs van uitvoering).
* Volg het conformiteitsniveau van uw organisatie ten opzichte van frameworks zoals ISO 27001 in de module **Conformiteit**.

*

## Nuttige bronnen

* [ICO: guide to data security](https://ico.org.uk/for-organizations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/security/)
* [ISO/IEC 27001: information security management systems](https://www.iso.org/isoiec-27001-information-security.html)
* [ENISA: the EU Agency for Cybersecurity](https://www.enisa.europa.eu/)

*

{% hint style="success" %}
**Goede praktijk:** elk nieuw project, elke nieuwe verwerker en elke nieuwe tool moet worden onderworpen aan een risicobeoordeling en aan een bijwerking van de bijbehorende maatregelen.
{% endhint %}
