# API use cases

This page gives three Python examples for data subject requests: attach a file to a request, send the requester a message with that file, and list the new requests. The examples use the `requests` library and authenticate with the `X-API-Key` header (see [Authentication](authentication.md)).

```sh
pip install requests
```

All the examples share these settings:

```python
import os
import requests

API_URL = "https://api.dastra.eu"
WORKSPACE_ID = 123  # your workspace identifier
HEADERS = {"X-API-Key": "<your private key>"}
```

## 1. Attach a file to a request

`POST /v1/ws/{workspaceId}/DataSubjectAttachments/{dataSubjectRequestId}`

The file is sent as `multipart/form-data`, in the `file` field. The response contains the attachment identifier (`id`), used in the next example.

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

## 2. Send a message with the attachment

`POST /v1/ws/{workspaceId}/DataSubjectMessages`

The JSON body contains the request identifier, the message text (3,000 characters at most) and the list of attachments (20 at most). If the request has an email address, the requester is notified by email.

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

## 3. List the new requests

`GET /v1/ws/{workspaceId}/DataSubjectRequests`

Filters are passed as query parameters:

| Parameter       | Effect                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------ |
| `states`        | State of the request: `Open`, `IdentityValidation`, `Processing`, `Active`, `Closed`. Can be repeated. |
| `purposes`      | Type of right: `Access`, `Rectification`, `Erasure`, `Opposition`, `Portability`, etc. Can be repeated. |
| `q`             | Text search                                                                                |
| `areaId`        | Organizational unit                                                                        |
| `sortBy`, `asc` | Sort order, for example `sortBy=dateCreation&asc=false` for the most recent first          |
| `page`, `size`  | Pagination (20 results per page by default)                                                |

Archived requests are excluded. The response contains the results in `items`, and the `page`, `size` and `total` fields.

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

The full list of endpoints and parameters is in the [API reference](https://api.dastra.eu/swagger/index.html).
