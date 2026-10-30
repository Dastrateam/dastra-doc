# API-Anwendungsfälle

Diese Seite zeigt drei Python-Beispiele zu Anfragen betroffener Personen: eine Datei an eine Anfrage anhängen, der anfragenden Person eine Nachricht mit dieser Datei senden und die neuen Anfragen auflisten. Die Beispiele verwenden die Bibliothek `requests` und authentifizieren sich mit dem Header `X-API-Key` (siehe [Authentifizierung](authentication.md)).

```sh
pip install requests
```

Alle Beispiele verwenden diese Einstellungen:

```python
import os
import requests

API_URL = "https://api.dastra.eu"
WORKSPACE_ID = 123  # your workspace identifier
HEADERS = {"X-API-Key": "<your private key>"}
```

## 1. Eine Datei an eine Anfrage anhängen

`POST /v1/ws/{workspaceId}/DataSubjectAttachments/{dataSubjectRequestId}`

Die Datei wird als `multipart/form-data` im Feld `file` gesendet. Die Antwort enthält die Kennung des Anhangs (`id`), die im nächsten Beispiel verwendet wird.

```python
def upload_attachment(request_id, path):
    with open(path, "rb") as f:
        response = requests.post(
            f"{API_URL}/v1/ws/{WORKSPACE_ID}/DataSubjectAttachments/{request_id}",
            headers=HEADERS,
            files={"file": (os.path.basename(path), f, "application/pdf")},
        )
    response.raise_for_status()
    return response.json()

attachment = upload_attachment("<request id>", "access-export.pdf")
print(attachment["id"], attachment["fileName"])
```

## 2. Eine Nachricht mit dem Anhang senden

`POST /v1/ws/{workspaceId}/DataSubjectMessages`

Der JSON-Body enthält die Kennung der Anfrage, den Nachrichtentext (höchstens 3.000 Zeichen) und die Liste der Anhänge (höchstens 20). Wenn die Anfrage eine E-Mail-Adresse hat, wird die anfragende Person per E-Mail benachrichtigt.

```python
def send_message(request_id, text, attachment_ids):
    response = requests.post(
        f"{API_URL}/v1/ws/{WORKSPACE_ID}/DataSubjectMessages",
        headers=HEADERS,
        json={
            "dataSubjectRequestId": request_id,
            "message": text,
            "attachments": [{"id": attachment_id} for attachment_id in attachment_ids],
        },
    )
    response.raise_for_status()
    return response.json()

message = send_message("<request id>", "Hello, please find attached the export of your data.", [attachment["id"]])
print(message["id"])
```

## 3. Die neuen Anfragen auflisten

`GET /v1/ws/{workspaceId}/DataSubjectRequests`

Die Filter werden als Query-Parameter übergeben:

| Parameter       | Wirkung                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------- |
| `states`        | Status der Anfrage: `Open`, `IdentityValidation`, `Processing`, `Active`, `Closed`. Wiederholbar. |
| `purposes`      | Art des Rechts: `Access`, `Rectification`, `Erasure`, `Opposition`, `Portability` usw. Wiederholbar. |
| `q`             | Textsuche                                                                                   |
| `areaId`        | Organisationseinheit                                                                        |
| `sortBy`, `asc` | Sortierung, zum Beispiel `sortBy=dateCreation&asc=false` für die neuesten zuerst            |
| `page`, `size`  | Seitenaufteilung (standardmäßig 20 Ergebnisse pro Seite)                                    |

Archivierte Anfragen sind ausgeschlossen. Die Antwort enthält die Ergebnisse in `items` sowie die Felder `page`, `size` und `total`.

```python
def list_new_requests():
    response = requests.get(
        f"{API_URL}/v1/ws/{WORKSPACE_ID}/DataSubjectRequests",
        headers=HEADERS,
        params={"states": "Open", "sortBy": "dateCreation", "asc": "false", "size": 50},
    )
    response.raise_for_status()
    return response.json()["items"]

for request in list_new_requests():
    print(request["id"], request["title"])
```

Die vollständige Liste der Endpunkte und Parameter finden Sie in der [API-Referenz](https://api.dastra.eu/swagger/index.html).
