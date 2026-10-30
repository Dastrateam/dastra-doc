---
description: >-
  Het adres, de gebruikslimieten en het beheer van aangepaste velden en labels
  van de Dastra REST API.
---

# API-configuratie

Deze pagina beschrijft de Dastra REST API: het adres, de gebruikslimieten en de omgang met aangepaste velden en labels. Om een sleutel te verkrijgen en de API aan te roepen, zie [Authenticatie](authentication.md).

## API's instellen in Dastra

API staat voor _**application programming interface**_.

Met API's verbindt u het Dastra-platform met andere externe tools.

De mogelijkheden zijn talrijk: een koppeling met CRM-software om stakeholders automatisch op te halen, de synchronisatie van een tool voor rechtenbeheer met de Dastra-module enzovoort.

Dastra is gebaseerd op de **REST API**-standaard, met onder meer de volgende HTTP-verzoeken:

| URI | GET | POST | PUT | PATCH | DELETE |
| --- | --- | --- | --- | --- | --- |
| Resourcecollectie, zoals `http://api.exemple.com/collection/` | Haalt in de body van het antwoord de URI's van de lidresources van de resourcecollectie op. | Maakt in de resourcecollectie een lidresource aan volgens de instructies in de body van het verzoek. De URI van de aangemaakte lidresource wordt automatisch toegekend en teruggegeven in het headerveld Location van het antwoord. | Vervangt alle representaties van de lidresources van de collectie door de representatie in de body van het verzoek, of maakt de resourcecollectie aan als ze niet bestaat. | Werkt alle representaties van de lidresources van de collectie bij volgens de instructies in de body van het verzoek, of maakt de resourcecollectie aan als ze niet bestaat. | Verwijdert alle representaties van de lidresources uit de resourcecollectie. |
| Lidresource, zoals `http://api.exemple.com/collection/item3` | Haalt in de body van het antwoord een representatie van de lidresource op. | Maakt in de lidresource een lidresource aan volgens de instructies in de body van het verzoek. De URI van de aangemaakte lidresource wordt automatisch toegekend en teruggegeven in het headerveld Location van het antwoord. | Vervangt alle representaties van de lidresource door de representatie in de body van het verzoek, of maakt de lidresource aan als ze niet bestaat. | Werkt alle representaties van de lidresource bij volgens de instructies in de body van het verzoek, of maakt de lidresource aan als ze niet bestaat. | Verwijdert alle representaties van de lidresource. |

Bron: [_Wikipedia_](https://en.wikipedia.org/wiki/Representational_state_transfer)

## Adres en versies

De Dastra API is beschikbaar op `https://api.dastra.eu`. De routes zijn geversioneerd en beginnen met `/v1/`.

* De routes van een werkruimte bevatten de identificatie ervan: `/v1/ws/{workspaceId}/{resource}`, bijvoorbeeld `/v1/ws/{workspaceId}/DataSubjectRequests`. De identificaties staan op het tabblad **tenantId & workspaceId** van de pagina **API-sleutels**.
* De routes die de hele organisatie betreffen, hebben geen identificatie van een werkruimte, bijvoorbeeld `/v1/Workspaces`.

## Referentie van de endpoints

De lijst van endpoints, met hun parameters en gegevensmodellen, wordt in het OpenAPI-formaat gepubliceerd:

* de Swagger-interface: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html);
* de OpenAPI-definitie in JSON: [https://api.dastra.eu/api/v1/dastra.json](https://api.dastra.eu/api/v1/dastra.json).

Ze bevat alleen de openbare endpoints van de API. De compliancemodule (kaders, controles, tests, audits) heeft een eigen API, waarvan de routes beginnen met `/v1/compliance/`: [https://api.dastra.eu/v1/compliance/swagger/index.html](https://api.dastra.eu/v1/compliance/swagger/index.html).

De referenties zijn ook beschikbaar op [dastra.readme.io](https://dastra.readme.io). Voor een volledig voorbeeld, zie [Gebruiksscenario's van de API](use-cases.md).

## Beperkingen

Verzoeken worden geteld per gebruiker, dat wil zeggen de eigenaar van de API-sleutel, volgens hun type:

| Type verzoek | Limiet |
| --- | --- |
| Lezen (`GET`) | 500 per minuut en 10.000 per periode van 10 minuten |
| Schrijven (`POST`, `PUT`, `PATCH`, `DELETE`) | 75 per minuut en 1.000 per periode van 10 minuten |
| Gevoelige endpoints | 5 per periode van 5 minuten |

Enkele endpoints, zoals die van de AI-assistent, hebben strengere limieten.

Boven een limiet antwoordt de API met HTTP-status 429 en een header `Retry-After` die in seconden de wachttijd aangeeft voordat u het opnieuw kunt proberen. Wacht die tijd af voordat u het verzoek opnieuw verstuurt.

Om uw tellers te controleren, roept u `GET https://api.dastra.eu/rate-limiting-state` aan.

Beveiligingsopties, zoals [IP-filtering](../features/settings/ip-filtering.md), gelden niet voor aanroepen die met een API-sleutel worden gedaan.

## Aangepaste velden beschikbaar stellen in de Dastra API

In Dastra kunt u de [aangepaste velden](../features/general/custom-fields.md) die in uw Dastra-werkruimte zijn ontworpen, in de API beschikbaar stellen.

Aangepaste velden zijn specifiek voor elke werkruimte. Om ze in de API op te nemen, definieert u eerst de **Naam van de variabele (slug)** in de definitie van het aangepaste veld:

<figure><img src="../.gitbook/assets/general-custom-fields-4.png" alt="Het venster voor het toevoegen van een aangepast veld met het label en de naam van de variabele (slug)"><figcaption><p>De naam van de variabele van een aangepast veld</p></figcaption></figure>

{% content-ref url="../features/general/custom-fields.md" %}
[Aangepaste velden](../features/general/custom-fields.md)
{% endcontent-ref %}

De meeste entiteiten die via de API kunnen worden gewijzigd, hebben een eigenschap `customFields` die u kunt wijzigen.

Als u de volgende velden in uw werkruimte definieert:

* `my_string_field`: een veld van het type **Tekst**;
* `my_boolean_field`: een veld van het type **Booleaans**;
* `my_numeric_field`: een veld van het type **Aantal (geheel getal)**;
* `my_checkbox_field`: een veld van het type **Selectievakje**.

kunt u ze als volgt wijzigen:

```json
{
  "label": "Google Analytics 4",
  "customFields": {
    "my_string_field": "Value of my field",
    "my_boolean_field": true,
    "my_numeric_field": 1,
    "my_checkbox_field": ["Apple", "Banana"]
  }
}
```

Voor een veld van het type **Selectievakje** is de waarde de lijst met de labels van de aangevinkte antwoorden.

## Het geval van labels

Om labels aan een entiteit te koppelen, haalt u eerst de bestaande labels op met `GET /v1/ws/{workspaceId}/Tags` en voegt u daarna de gewenste labels toe aan de eigenschap `tags` van de entiteit, met hun `id`.

## MCP-server

Met de MCP-server (Model Context Protocol) kan een AI-assistent, een code-editor of een terminal met uw Dastra-gegevens werken. U stelt hem in op het tabblad **MCP Server** van de pagina **API-sleutels**. Hij vereist het abonnement Dastra AI Pro. Zie [De MCP-server](../features/general/ai-assistant/mcp.md).

{% hint style="warning" %}
Aanroepen die gegevens aanmaken, wijzigen of verwijderen, werken op uw echte records. Test ze eerst op een speciale werkruimte.
{% endhint %}

API-sleutels worden beheerd op de pagina **API-sleutels**, die is voorbehouden aan de eigenaars van de organisatie. Zie [API-sleutelbeheer](../features/settings/api-keys.md).
