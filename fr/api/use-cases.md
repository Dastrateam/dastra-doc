# Cas d'usage de l'API

Cette page donne trois exemples en Python sur les demandes d'exercice de droits : joindre un fichier à une demande, envoyer au demandeur un message avec ce fichier, et lister les nouvelles demandes. Les exemples utilisent la bibliothèque `requests` et s'authentifient avec l'en-tête `X-API-Key` (voir [Authentification](authentication.md)).

```sh
pip install requests
```

Tous les exemples partagent ces réglages :

```python
import os
import requests

API_URL = "https://api.dastra.eu"
WORKSPACE_ID = 123  # identifiant de votre espace de travail
HEADERS = {"X-API-Key": "<votre clé privée>"}
```

## 1. Joindre un fichier à une demande

`POST /v1/ws/{workspaceId}/DataSubjectAttachments/{dataSubjectRequestId}`

Le fichier est envoyé en `multipart/form-data`, dans le champ `file`. La réponse contient l'identifiant de la pièce jointe (`id`), utilisé dans l'exemple suivant.

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

attachment = upload_attachment("<id de la demande>", "export-acces.pdf")
print(attachment["id"], attachment["fileName"])
```

## 2. Envoyer un message avec la pièce jointe

`POST /v1/ws/{workspaceId}/DataSubjectMessages`

Le corps JSON contient l'identifiant de la demande, le texte du message (3 000 caractères au plus) et la liste des pièces jointes (20 au plus). Si la demande a une adresse e-mail, le demandeur est prévenu par e-mail.

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

message = send_message("<id de la demande>", "Bonjour, vous trouverez ci-joint l'export de vos données.", [attachment["id"]])
print(message["id"])
```

## 3. Lister les nouvelles demandes

`GET /v1/ws/{workspaceId}/DataSubjectRequests`

Les filtres se passent en paramètres de requête :

| Paramètre       | Effet                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------- |
| `states`        | État de la demande : `Open`, `IdentityValidation`, `Processing`, `Active`, `Closed`. Répétable. |
| `purposes`      | Type de droit : `Access`, `Rectification`, `Erasure`, `Opposition`, `Portability`, etc. Répétable. |
| `q`             | Recherche texte                                                                             |
| `areaId`        | Unité organisationnelle                                                                     |
| `sortBy`, `asc` | Tri, par exemple `sortBy=dateCreation&asc=false` pour les plus récentes d'abord             |
| `page`, `size`  | Pagination (20 résultats par page par défaut)                                               |

Les demandes archivées sont exclues. La réponse contient les résultats dans `items`, ainsi que les champs `page`, `size` et `total`.

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

La liste complète des points d'accès et de leurs paramètres se trouve dans la [référence de l'API](https://api.dastra.eu/swagger/index.html).
