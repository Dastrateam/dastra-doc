---
description: >-
  Diese Seite ist ein umfassender Leitfaden, der erklärt, wie Sie Dastra mit
  externen Tools integrieren können, mit praktischen Anwendungsfällen.
---

# Dastra mit externen Tools integrieren

Organisationen möchten häufig **die Compliance- und Orchestrierungsfähigkeiten von Dastra** mit externen Systemen wie Datenentdeckungs-/Schwärzungstools, IT-Asset-Inventaren, CRMs, Lieferantenmanagementsystemen oder Aufgabenverwaltungsplattformen integrieren. Diese Integrationen ermöglichen:

* Automatisierung wiederkehrender Compliance-Aufgaben,
* Datensynchronisierung zwischen Systemen,
* Gewährleistung regulatorischer Konsistenz (DSGVO, CCPA usw.),
* Verbesserung der Transparenz und Zusammenarbeit.

Dieser Leitfaden stellt drei Integrationsmodelle vor (vom einfachsten bis zum robustesten), liefert Workflow-Beispiele und beschreibt **typische Anwendungsfälle** mit den Dastra-API-Endpunkten.

***

### 🔹 Integrationsmodelle

#### 1. Einfache Workflows mit Zapier (Webhooks + APIs)

**Ideal für:** einfache Automatisierungen mit geringen oder mittleren Datenvolumen.

**Beispiel-Workflow:**

1. **Trigger in Dastra** → ein DSAR oder Ereignis sendet einen Webhook.
2. **Zapier empfängt den Webhook** → ruft die API eines externen Tools auf.
3. **Ergebnisse verarbeitet** → das externe Tool sendet die Daten an Zapier zurück.
4. **Aktualisierung in Dastra** → Zapier verwendet die Dastra REST-API, um die Ergebnisse anzuhängen (`POST /requests/{id}/attachments`) oder den Status zu aktualisieren.

✅ **Vorteile:** schnelle Einrichtung, keine Entwicklung erforderlich.\
⚠️ **Einschränkungen:** begrenzte Payload-Größe und Ausführungszeiten.

***

#### 2. Mittlere Workflows mit Zapier + Microservice

**Ideal für:** mittelgroße Workflows, die mehr Flexibilität als Zapier allein erfordern.

**Beispiel-Workflow:**

1. **Trigger in Dastra → Zapier.**
2. **Zapier ruft einen Microservice auf** (AWS Lambda, Azure Function, GCP Cloud Run).
3. **Der Microservice führt die komplexe Logik aus** → Retry-Verwaltung, Paginierung, Verarbeitung großer Dateien.
4. **Der Microservice gibt die Ergebnisse zurück** → die Dastra REST-API aktualisiert die Daten.

✅ **Vorteile:** kombiniert die Einfachheit von Zapier mit der Robustheit eines benutzerdefinierten Backends.

***

#### 3. Direkte API-Integration

**Ideal für:** Enterprise-Deployments mit strengen SLAs, hohen Volumen und erweiterten Sicherheitsanforderungen.

**Beispiel-Workflow:**

1. **Dastra ruft direkt die externe API auf**, wenn ein Trigger eintritt.
2. **Das externe System führt die Verarbeitung aus** (Entdeckung, Klassifizierung, Schwärzung usw.).
3. **Die Ergebnisse werden an Dastra zurückgesendet** über API (`PATCH /requests/{id}`, `POST /requests/{id}/attachments`).
4. **Dastra orchestriert die Compliance-Antwort** über mehrere Systeme hinweg.

✅ **Vorteile:** robust, skalierbar, ohne Zapier-Einschränkungen.\
⚠️ **Einschränkungen:** Entwicklung erforderlich, strenge Sicherheits- und API-Quota-Verwaltung.

***

### 🔹 Die richtige Vorgehensweise wählen

| **Szenario**                              | **Empfohlener Ansatz**   |
| ----------------------------------------- | ------------------------ |
| Proof of Concept, kleine Datensätze       | Zapier (Webhooks + APIs) |
| Mittlere Workflows, moderate Komplexität  | Zapier + Microservice    |
| Großflächige Deployments, stark reguliert | Direkte API-Integration  |

***

### 📘 Anwendungsfälle & API-Endpunkte

Hier einige häufige Szenarien, ihre Ziele und die zu verwendenden **Dastra-Endpunkte** ([API-Dokumentation](https://dastra.readme.io/reference/rate-limiting)):

#### 1. Orchestrierung der Betroffenenrechte (DSAR) mit externen Tools

* **Ziel:** Entdeckungs-/Schwärzungs-Workflows bei Eingang eines DSAR auslösen; Ergebnisse aggregieren und anhängen.
* **Endpunkte:**
  * `POST /v1/ws/{workspaceId}/DataSubjectRequests`.
  * `POST /v1/ws/{workspaceId}/DataSubjectAttachments/{dataSubjectRequestId}`.
  * `PATCH /v1/ws/{workspaceId}/DataSubjectRequests/{id}`.

***

#### 2. Integration mit IT-Asset-Inventarsystemen

* **Ziel:** IT-Assets mit Dastra synchronisieren, mit Verarbeitungen verknüpfen und automatisch aktualisieren.
* **Endpunkte:**
  * `GET /v1/ws/{workspaceId}/Assets` / `POST /v1/ws/{workspaceId}/Assets`.
  * `PATCH /v1/ws/{workspaceId}/Assets/{id}`.
  * `POST /v1/ws/{workspaceId}/Assets/import`.

***

#### 3. CRM-Integration

* **Ziel:** Kundendaten synchronisieren, Einwilligungen verwalten, DSARs direkt aus CRM-Ereignissen erstellen.
* **Endpunkte:**
  * `GET /v1/ws/{workspaceId}/Actors`, `POST /v1/ws/{workspaceId}/Actors`.
  * `POST /v1/ws/{workspaceId}/DataSubjectRequests`.
  * `GenericRelationships` / `DataProcessingRelationships`.

***

#### 4. Integration mit Lieferantenmanagementsystemen

* **Ziel:** Verträge verwalten, Drittparteirisiken überwachen, Lieferanten und Datenverarbeitungen verknüpfen.
* **Endpunkte:**
  * `GET /v1/ws/{workspaceId}/Contracts`, `POST /v1/ws/{workspaceId}/Contracts`.
  * `GET /v1/ws/{workspaceId}/Assets` / `Actors`.
  * `GenericRelationships`.

***

#### 5. Integration mit Datenkatalogen

* **Ziel:** Metadaten importieren, Felder klassifizieren, Verarbeitungsverzeichnisse anreichern.
* **Endpunkte:**
  * `GET /v1/ws/{workspaceId}/DataFields`.
  * `POST /v1/ws/{workspaceId}/DataProcessings`, `PATCH /v1/ws/{workspaceId}/DataProcessings/{id}`.
  * `DataProcessingRelationships`.

***

#### 6. Integration mit CMS (Content Management Systemen)

* **Ziel:** Archivierung, Löschung oder Anhängen von Inhalten/Dokumenten in Compliance-Workflows automatisieren.
* **Endpunkte:**
  * `GET /v1/ws/{workspaceId}/CloudStorage/{providerName}/{fileId}`.
  * `POST /v1/ws/{workspaceId}/CloudStorage/{providerName}`.
  * `DataSubjectAttachments`.

***

#### 7. Integration mit Aufgabenverwaltungssystemen

* **Ziel:** Compliance-Aufgaben (Audits, Reviews, Nachverfolgungen) erstellen und zuweisen, die mit Dastra-Workflows verknüpft sind.
* **Endpunkte:**
  * `GET /v1/ws/{workspaceId}/Tasks`, `POST /v1/ws/{workspaceId}/Tasks`.
  * `PATCH /v1/ws/{workspaceId}/Tasks/{id}`.
  * `Users`, `Teams`, `Workflows`.

***

### 🚀 Kernpunkte

* **Zapier + Dastra** = schnelle, codefreie Integrationen für einfache Fälle.
* **Hybride Modelle** (Zapier + Microservices) = Flexibilität und Zuverlässigkeit für mittlere Workflows.
* **Direkte API-Integrationen** = Robustheit und Skalierbarkeit für große Organisationen.
* Mit diesen Modellen kann sich Dastra nahtlos in IT-, Daten- und Business-Ökosysteme integrieren.

[Kontaktieren Sie uns](https://www.dastra.eu/de/contacts/demo) für weitere Informationen.
