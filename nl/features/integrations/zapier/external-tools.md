---
description: >-
  Deze pagina beschrijft hoe u Dastra integreert met externe tools, met
  praktische gebruiksscenario's.
---

# Dastra integreren met externe tools

Organisaties moeten de mogelijkheden van Dastra voor compliance en orkestratie vaak koppelen aan externe systemen, zoals tools voor gegevensdetectie en redactie, IT-assetinventarissen, CRM's, leveranciersbeheer of platformen voor taakbeheer. Met deze integraties kunnen teams:

* terugkerende compliancetaken automatiseren;
* gegevens tussen systemen synchroniseren;
* juridische en regelgevende consistentie waarborgen (AVG, CCPA enzovoort);
* meer zicht op en samenwerking rond de gegevens krijgen.

Deze handleiding introduceert drie integratiemodellen (van licht tot bedrijfsklaar), geeft voorbeelden van workflows en beschrijft typische gebruiksscenario's met de bijbehorende API-endpoints van Dastra.

## Integratiemodellen

### 1. Lichte workflows via Zapier (webhooks en API's)

Geschikt voor: eenvoudige automatiseringen met kleine tot gemiddelde gegevensvolumes.

Voorbeeld van een workflow:

1. Trigger in Dastra: een verzoek van een betrokkene (DSAR) of een gebeurtenis activeert een webhook (zie [Webhooks](../../settings/webhooks.md)).
2. Zapier ontvangt de webhook en roept de API van de externe tool aan.
3. De resultaten worden verwerkt: de externe tool stuurt gegevens terug naar Zapier.
4. Bijwerking in Dastra: Zapier gebruikt de REST API van Dastra om de resultaten toe te voegen (`POST /v1/ws/{workspaceId}/DataSubjectAttachments/{dataSubjectRequestId}`, als multipart) of statussen bij te werken (`PATCH /v1/ws/{workspaceId}/DataSubjectRequests/{id}`).

Voordelen: snel op te zetten, geen ontwikkeling nodig.\
Nadelen: beperkte omvang van de payload, time-outs bij uitvoering.

### 2. Middelgrote workflows via Zapier en een microservice

Geschikt voor: workflows van gemiddelde omvang die meer flexibiliteit vragen dan Zapier alleen.

Voorbeeld van een workflow:

1. Trigger in Dastra naar Zapier.
2. Zapier roept een eigen microservice aan (AWS Lambda, Azure Function, GCP Cloud Run).
3. De microservice voert de zware logica uit: nieuwe pogingen, paginering, bestandsverwerking.
4. De microservice stuurt de resultaten terug en werkt Dastra bij via de REST API.

Voordelen: combineert het overzicht van low-code met de robuustheid van een backend.

### 3. Rechtstreekse API-integratie

Geschikt voor: bedrijfsklare implementaties met strikte SLA's, grote volumes en geavanceerde beveiligingseisen.

Voorbeeld van een workflow:

1. Dastra roept rechtstreeks de externe API aan wanneer een trigger optreedt (zie [HTTP / Custom API](../custom-http.md)).
2. Het externe systeem voert de workflow uit (detectie, classificatie, redactie enzovoort).
3. De resultaten worden via de API teruggestuurd naar Dastra (`PATCH /v1/ws/{workspaceId}/DataSubjectRequests/{id}`, `POST /v1/ws/{workspaceId}/DataSubjectAttachments/{dataSubjectRequestId}`).
4. Dastra orkestreert de compliancerespons over de systemen heen.

Voordelen: robuust, schaalbaar, zonder de beperkingen van Zapier.\
Nadelen: vraagt specifieke ontwikkeling, zorgvuldige API-beveiliging en omgang met rate limits.

## De juiste aanpak kiezen

| Scenario | Aanbevolen aanpak |
| --- | --- |
| Proof of concept, kleine datasets | Zapier (webhooks en API's) |
| Middelgroot, gemiddelde complexiteit | Zapier en microservice |
| Bedrijfsklaar, groot volume, gereguleerd | Rechtstreekse API-integratie |

## Typische gebruiksscenario's en API-endpoints

Hieronder staan veelvoorkomende integratiescenario's, wat ze opleveren en de API-endpoints van Dastra die u daarvoor gebruikt ([API-referentie](https://dastra.readme.io/reference/rate-limiting)):

### 1. Orkestratie van rechten van betrokkenen met externe tools

* Doel: externe workflows voor detectie en redactie starten wanneer een DSAR binnenkomt, en de resultaten bundelen en toevoegen.
* Endpoints:
  * `POST /v1/ws/{workspaceId}/DataSubjectRequests`: een DSAR aanmaken.
  * `POST /v1/ws/{workspaceId}/DataSubjectAttachments/{dataSubjectRequestId}`: exports toevoegen.
  * `PATCH /v1/ws/{workspaceId}/DataSubjectRequests/{id}`: de status bijwerken.

### 2. Integratie met beheer van de IT-assetinventaris

* Doel: IT-assets synchroniseren met Dastra, assets koppelen aan verwerkingsactiviteiten en automatisch bijwerken.
* Endpoints:
  * `GET /v1/ws/{workspaceId}/Assets` en `POST /v1/ws/{workspaceId}/Assets`.
  * `PATCH /v1/ws/{workspaceId}/Assets/{id}`.
  * `POST /v1/ws/{workspaceId}/Assets/import`.

### 3. Integratie met CRM-systemen

* Doel: klantgegevens synchroniseren, toestemming beheren en DSAR's rechtstreeks aanmaken vanuit CRM-gebeurtenissen.
* Endpoints:
  * `GET /v1/ws/{workspaceId}/Actors` en `POST /v1/ws/{workspaceId}/Actors`.
  * `POST /v1/ws/{workspaceId}/DataSubjectRequests`.
  * `GenericRelationships` en `DataProcessingRelationships`.

### 4. Integratie met systemen voor leveranciersbeheer

* Doel: leverancierscontracten beheren, risico's van derden opvolgen en leveranciers koppelen aan verwerkingsactiviteiten.
* Endpoints:
  * `GET /v1/ws/{workspaceId}/Contracts` en `POST /v1/ws/{workspaceId}/Contracts`.
  * `GET /v1/ws/{workspaceId}/Assets` en `Actors`.
  * `GenericRelationships`.

### 5. Integratie met datacatalogussen

* Doel: metadata importeren, velden classificeren en verwerkingsregisters verrijken.
* Endpoints:
  * `GET /v1/ws/{workspaceId}/DataFields`.
  * `POST /v1/ws/{workspaceId}/DataProcessings` en `PATCH /v1/ws/{workspaceId}/DataProcessings/{id}`.
  * `DataProcessingRelationships`.

### 6. Integratie met contentmanagementsystemen (CMS)

* Doel: redactie, archivering of het toevoegen van content en documenten in compliance-workflows automatiseren.
* Endpoints:
  * `CloudStorage`-API's: `GET /v1/ws/{workspaceId}/CloudStorage/{providerName}/{fileId}` en `POST /v1/ws/{workspaceId}/CloudStorage/{providerName}`.
  * `DataSubjectAttachments`.
  * API's voor documentbeheer.

### 7. Integratie met systemen voor taakbeheer

* Doel: compliancetaken (audits, beoordelingen, opvolging) aanmaken en toewijzen, gekoppeld aan workflows van Dastra.
* Endpoints:
  * `GET /v1/ws/{workspaceId}/Tasks` en `POST /v1/ws/{workspaceId}/Tasks`.
  * `PATCH /v1/ws/{workspaceId}/Tasks/{id}`.
  * `Users`, `Teams` en `Workflows` voor toewijzing en levenscyclusbeheer.

## Samengevat

* Zapier en Dastra maken snelle integraties zonder code mogelijk voor eenvoudige gebruiksscenario's.
* Hybride modellen (Zapier en microservices) verwerken middelgrote complexiteit betrouwbaar.
* Rechtstreekse API-integraties zijn de referentie voor bedrijfsklare compliance.
* Met deze modellen koppelen organisaties Dastra aan hun IT-, data- en bedrijfsomgeving.

[Neem contact met ons op](https://www.dastra.eu/en/contacts/demo) voor meer informatie.
