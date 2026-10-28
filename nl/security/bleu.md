---
description: >-
  Dastra is ook beschikbaar op Bleu: een dedicated instantie, geïsoleerd van
  ons standaard SaaS-platform, waarvan de gegevens de Bleu-perimeter niet
  verlaten.
---

# Dastra op Bleu (soevereine cloud)

Sommige organisaties mogen hun compliancegegevens niet hosten op infrastructuur die onderworpen is aan niet-Europese extraterritoriale wetgeving. Daarom is Dastra ook beschikbaar op **Bleu**: een dedicated instantie, los van ons standaard SaaS-platform, waarvan de gegevens de Bleu-perimeter niet verlaten.

## Wat is Bleu?

Bleu is een Frans bedrijf in handen van **Capgemini en Orange** dat Microsoft Azure en Microsoft 365 aanbiedt in een omgeving die geïsoleerd is van de wereldwijde infrastructuur van Microsoft. De diensten worden gehost in datacenters in Frankrijk (Île-de-France en Zuid-Frankrijk) en uitsluitend beheerd door Franse teams. Het aanbod richt zich op de overheid, lokale besturen, zorginstellingen, operatoren van vitaal belang (OIV) en aanbieders van essentiële diensten (OSE), en biedt juridische bescherming tegen extraterritoriale toegangswetten (Cloud Act, FISA).

## SecNumCloud-kwalificatie: hoe staat het ervoor?

De kwalificatie **SecNumCloud 3.2** wordt door de ANSSI afgegeven na vier mijlpalen. Voor het IaaS-, PaaS- en CaaS-domein heeft Bleu **J0** (april 2025, dossier aanvaard) en **J1** (september 2025, evaluatiestrategie aanvaard) behaald. De evaluatie ter plaatse (**J2**) loopt; de kwalificatiebeslissing (**J3**) is nog niet genomen.

{% hint style="warning" %}
Wij presenteren Dastra op Bleu daarom niet als een "SecNumCloud-gekwalificeerd" aanbod zolang de ANSSI haar beslissing niet heeft gepubliceerd.
{% endhint %}

## Wat verandert er ten opzichte van het standaardaanbod

| | Standaardaanbod | Bleu-aanbod |
| --- | --- | --- |
| Applicatie | `app.dastra.eu` | `app-bleu.dastra.eu` |
| API | `api.dastra.eu` | `api-bleu.dastra.eu` |
| Authenticatie | `account.dastra.eu` | `account-bleu.dastra.eu` — afzonderlijke gebruikersdirectory, accounts en ondertekeningssleutels |
| SCIM-provisioning | `scim.dastra.eu` | `scim-bleu.dastra.eu` |
| Hosting | Microsoft Azure France (Parijs, Marseille) | Bleu France Central (Île-de-France) |
| AI-functies | Beschikbaar | Beschikbaar, uitgevoerd door **Mistral AI** (Frans bedrijf, buiten de Bleu-perimeter) en niet door Azure OpenAI |
| Full-textzoeken | Beschikbaar | Beschikbaar, index gehost op Bleu |
| Connectoren (Jira, ServiceNow, LeanIX, DocuSign, Zapier…) en API-sleutels | Beschikbaar | Beschikbaar |
| SSO (SAML, OpenID Connect) | Beschikbaar | Beschikbaar |
| Redactionele inhoud in de applicatie (nieuws, webinars) | Geleverd door het standaardplatform | Idem, alleen-lezen, zonder enige klantgegevens |
| Updateritme | Doorlopend | Dezelfde versies, uitgerold na het standaardplatform |

## Locatie van de gegevens en back-ups

Alle productieresources (databases, bestanden, auditlogs, zoekindex, cache, secretkluis, monitoring) worden gehost in de regio **Bleu France Central**. Ze worden niet buiten Bleu gerepliceerd.

De enige uitgaande stromen zijn oproepen naar de externe diensten die het standaardaanbod al gebruikt: Mistral AI voor de AI-functies (gegevens worden op aanvraag verwerkt) en Brevo (Frans bedrijf) voor het versturen van e-mails.

## Versleuteling, authenticatie en secrets

Tenzij hieronder anders vermeld, gelden de maatregelen die op de pagina [Beveiliging bij Dastra](general.md) worden beschreven ook voor de Bleu-instantie.

* **TLS**: het publieke verkeer wordt beëindigd door het Europese CDN bunny.net, dat de certificaten beheert; op alle resources (applicaties, databases, opslag) wordt minimaal TLS 1.2 afgedwongen.
* **Secrets**: Azure Key Vault gehost op Bleu, uitsluitend toegankelijk voor de managed identities van de applicaties; geen enkel secret in de applicatieconfiguratie.
* **Authenticatie**: eigen identityserver. Een account van het standaardplatform kan niet inloggen op Bleu, en omgekeerd; er bestaat geen federatie tussen beide. De inlogpagina biedt een regiokiezer om gebruikers te sturen.

## Isolatie en omgevingen

De Bleu-instantie is **strikt geïsoleerd** van het standaardplatform: databases, opslag, logs, cache, zoekindex, secretkluis en identiteiten zijn afzonderlijk. De enige stroom tussen beide platformen is de alleen-lezen synchronisatie van onze referentiebibliotheken (sjablonen, referentiekaders) naar Bleu; er circuleren geen klantgegevens.
