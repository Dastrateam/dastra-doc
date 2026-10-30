# Liste der API-Endpunkte

Diese Seite erklärt, wo Sie die aktuelle Liste der Dastra-API-Endpunkte finden und wie Sie sie lesen.

## Die Referenz durchsuchen

Die Liste der Endpunkte wird aus der API selbst erzeugt und im OpenAPI-Format veröffentlicht:

* die Swagger-Oberfläche: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html). Sie zeigt die Parameter, Datenmodelle und Antwortcodes jedes Endpunkts und erlaubt es, einen Aufruf auszuprobieren, sobald Sie Ihren Schlüssel mit der Schaltfläche **Authorize** eingegeben haben;
* die OpenAPI-Definition als JSON: [https://api.dastra.eu/api/v1/dastra.json](https://api.dastra.eu/api/v1/dastra.json), um einen Client in Ihrer Sprache zu erzeugen;
* die API-Referenz: [https://dastra.readme.io](https://dastra.readme.io).

Dort sind nur die öffentlichen Endpunkte der API aufgeführt. Das Compliance-Modul (Frameworks, Kontrollen, Tests, Audits) hat eine eigene Referenz, deren Routen mit `/v1/compliance/ws/{workspaceId}/` beginnen: [https://api.dastra.eu/v1/compliance/swagger/index.html](https://api.dastra.eu/v1/compliance/swagger/index.html).

## Einen Pfad lesen

Ein Pfad beginnt mit der API-Version und, bei einem Mandanten, mit dessen Kennung:

| Pfad | Verwendung |
| --- | --- |
| `/v1/ws/{workspaceId}/Actors` | Die Stakeholder eines Mandanten |
| `/v1/ws/{workspaceId}/DataSubjectRequests` | Die Anfragen betroffener Personen eines Mandanten |
| `/v1/ws/{workspaceId}/Tags` | Die Tags eines Mandanten |
| `/v1/Workspaces` | Die Mandanten der Organisation |

Die HTTP-Methode gibt die Aktion an: `GET` liest, `POST` erstellt, `PUT` oder `PATCH` ändert und `DELETE` löscht. Je nach Ressource gibt es zusätzliche Routen, etwa `/batch-delete`, um mehrere Elemente zu löschen, oder `/export/{format}`, um eine Liste zu exportieren.

Um zu prüfen, ob ein API-Schlüssel funktioniert, rufen Sie `GET https://api.dastra.eu/me` auf.

Zur Authentifizierung siehe [Authentifizierung](authentication.md). Zu Anfragelimits, benutzerdefinierten Feldern und Tags siehe [API-Konfiguration](configuration.md). Beispielaufrufe finden Sie unter [API-Anwendungsfälle](use-cases.md).
