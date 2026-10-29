# Gebruiksscenario's van de API

Deze pagina geeft drie Python-voorbeelden voor verzoeken van betrokkenen: een bestand aan een verzoek koppelen, de aanvrager een bericht met dat bestand sturen en de nieuwe verzoeken weergeven. De voorbeelden gebruiken de bibliotheek `requests` en authenticeren met de header `X-API-Key` (zie [Authenticatie](authentication.md)).

```sh
pip install requests
```

Alle voorbeelden gebruiken deze instellingen:

```python
import os
import requests

API_URL = "https://api.dastra.eu"
WORKSPACE_ID = 123  # your workspace identifier
HEADERS = {"X-API-Key": "<your private key>"}
```

## 1. Een bestand aan een verzoek koppelen

`POST /v1/ws/{workspaceId}/DataSubjectAttachments/{dataSubjectRequestId}`

Het bestand wordt verzonden als `multipart/form-data`, in het veld `file`. Het antwoord bevat de identifier van de bijlage (`id`), die u in het volgende voorbeeld gebruikt.

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

## 2. Een bericht met de bijlage versturen

`POST /v1/ws/{workspaceId}/DataSubjectMessages`

De JSON-body bevat de identifier van het verzoek, de tekst van het bericht (maximaal 3.000 tekens) en de lijst met bijlagen (maximaal 20). Heeft het verzoek een e-mailadres, dan ontvangt de aanvrager een melding per e-mail.

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

## 3. De nieuwe verzoeken weergeven

`GET /v1/ws/{workspaceId}/DataSubjectRequests`

Filters worden als queryparameters meegegeven:

| Parameter       | Effect                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------ |
| `states`        | Status van het verzoek: `Open`, `IdentityValidation`, `Processing`, `Active`, `Closed`. Kan worden herhaald. |
| `purposes`      | Type recht: `Access`, `Rectification`, `Erasure`, `Opposition`, `Portability` enzovoort. Kan worden herhaald. |
| `q`             | Zoeken in tekst                                                                            |
| `areaId`        | Organisatorische eenheid                                                                   |
| `sortBy`, `asc` | Sorteervolgorde, bijvoorbeeld `sortBy=dateCreation&asc=false` voor de meest recente eerst  |
| `page`, `size`  | Paginering (standaard 20 resultaten per pagina)                                            |

Gearchiveerde verzoeken worden uitgesloten. Het antwoord bevat de resultaten in `items` en de velden `page`, `size` en `total`.

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

De volledige lijst met endpoints en parameters staat in de [API-referentie](https://api.dastra.eu/swagger/index.html).
