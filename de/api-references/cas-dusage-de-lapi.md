# API-Anwendungsfälle

Basierend auf den Spezifikationen der Dastra-API-Dokumentation finden Sie hier einen Leitfaden für drei Anwendungsfälle sowie Beispiele in Python mit AIOHTTP zur Durchführung der Anfragen:

#### Voraussetzungen

Stellen Sie sicher, dass AIOHTTP in Ihrer Umgebung installiert ist:

```sh
pip install aiohttp
```

#### 1. Einen Anhang für einen Betroffenenanfrage erstellen

**Endpunkt**: `/datasubjectattachments`

**Methode**: POST

**Beschreibung**: Dieser Endpunkt wird verwendet, um einen Anhang zu erstellen, der mit einer Betroffenenanfrage verknüpft ist.

**Beispiel-Anfrage**:

```python
import aiohttp
import asyncio

async def create_attachment(workspace_id, api_key, attachment_data):
    url = f"https://api.dastra.eu/v1/ws/{workspace_id}/datasubjectattachments"
    
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=attachment_data, headers=headers) as response:
            return await response.json()

# Beispiel-Verwendung
workspace_id = "votre_workspace_id"
api_key = "votre_api_key"
attachment_data = {
    # Füllen Sie die Daten Ihres Anhangs aus
    "dataSubjectRequestId": "id_de_la_demande",
    "fileName": "exemple.pdf",
    "fileContent": "contenu_encodé_base64"
}

response = asyncio.run(create_attachment(workspace_id, api_key, attachment_data))
print(response)
```

#### 2. Eine Nachricht mit Anhang in einer Betroffenenanfrage senden

**Endpunkt**: `/datasubjectmessages`

**Methode**: POST

**Beschreibung**: Dieser Endpunkt wird verwendet, um eine Nachricht mit einem Anhang in einer Betroffenenanfrage zu senden.

**Beispiel-Anfrage**:

```python
import aiohttp
import asyncio

async def send_message_with_attachment(workspace_id, api_key, message_data):
    url = f"https://api.dastra.eu/v1/ws/{workspace_id}/datasubjectmessages"
    
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=message_data, headers=headers) as response:
            return await response.json()

# Beispiel-Verwendung
workspace_id = "votre_workspace_id"
api_key = "votre_api_key"
message_data = {
    # Füllen Sie die Daten Ihrer Nachricht aus
    "requestId": "id_de_la_demande",
    "subject": "Betreff der Nachricht",
    "body": "Inhalt der Nachricht",
    "attachmentId": "id_de_la_pièce_jointe"  # ID des zuvor erstellten Anhangs
}

response = asyncio.run(send_message_with_attachment(workspace_id, api_key, message_data))
print(response)
```

#### 3. Neue Anfragen nach Filtern abrufen

**Endpunkt**: `/DataSubjectRequests`

**Methode**: GET

**Beschreibung**: Dieser Endpunkt wird verwendet, um neue Betroffenenanfragen anhand bestimmter Filter abzurufen.

**Beispiel-Anfrage**:

```
import aiohttp
import asyncio

async def get_new_requests(workspace_id, api_key, filters):
    url = f"https://api.dastra.eu/v1/ws/{workspace_id}/DataSubjectRequests"
    
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key
    }

    params = {
        "filters": filters  # Die Filter müssen ein JSON-String sein
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            return await response.json()

# Beispiel-Verwendung
workspace_id = "votre_workspace_id"
api_key = "votre_api_key"
filters = '{"field":"status","operator":"equal","value":"new"}'  # Beispiel-Filter

response = asyncio.run(get_new_requests(workspace_id, api_key, filters))
print(response)
```

#### Fazit

Dieser Leitfaden bietet eine schrittweise Anleitung zur Interaktion mit der Dastra-API unter Verwendung von Python und AIOHTTP. Ersetzen Sie die Platzhalter wie `workspace_id`, `api_key` und die Anfragedaten durch Ihre tatsächlichen Daten.

Passen Sie die Filterkriterien und Anfrage-Payloads gerne an Ihre Bedürfnisse an.
