---
description: >-
  Waar u de actuele lijst van Dastra API-endpoints vindt en hoe u ze leest.
---

# Lijst van API-endpoints

Deze pagina legt uit waar u de actuele lijst van de Dastra API-endpoints vindt en hoe u ze leest.

## De referentie raadplegen

De lijst van endpoints wordt door de API zelf gegenereerd en in het OpenAPI-formaat gepubliceerd:

* de Swagger-interface: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html). Ze toont de parameters, gegevensmodellen en antwoordcodes van elk endpoint en laat u een aanroep proberen zodra u uw sleutel met de knop **Authorize** hebt ingevoerd;
* de OpenAPI-definitie in JSON: [https://api.dastra.eu/api/v1/dastra.json](https://api.dastra.eu/api/v1/dastra.json), om een client in uw taal te genereren;
* de API-referentie: [https://dastra.readme.io](https://dastra.readme.io).

Alleen de openbare endpoints van de API staan er. De compliancemodule (kaders, controles, tests, audits) heeft een eigen referentie, waarvan de routes beginnen met `/v1/compliance/ws/{workspaceId}/`: [https://api.dastra.eu/v1/compliance/swagger/index.html](https://api.dastra.eu/v1/compliance/swagger/index.html).

## Een pad lezen

Een pad begint met de versie van de API en, voor een werkruimte, met de identificatie ervan:

| Pad | Gebruik |
| --- | --- |
| `/v1/ws/{workspaceId}/Actors` | De stakeholders van een werkruimte |
| `/v1/ws/{workspaceId}/DataSubjectRequests` | De verzoeken van betrokkenen van een werkruimte |
| `/v1/ws/{workspaceId}/Tags` | De labels van een werkruimte |
| `/v1/Workspaces` | De werkruimten van de organisatie |

De HTTP-methode bepaalt de actie: `GET` leest, `POST` maakt aan, `PUT` of `PATCH` wijzigt en `DELETE` verwijdert. Afhankelijk van de resource bestaan er extra routes, zoals `/batch-delete` om meerdere items te verwijderen of `/export/{format}` om een lijst te exporteren.

Om te controleren of een API-sleutel werkt, roept u `GET https://api.dastra.eu/me` aan.

Voor authenticatie, zie [Authenticatie](authentication.md). Voor verzoeklimieten, aangepaste velden en labels, zie [API-configuratie](configuration.md). Voor voorbeeldaanroepen, zie [Gebruiksscenario's van de API](use-cases.md).
