# List of API endpoints

This page explains where to find the up-to-date list of Dastra API endpoints and how to read it.

## Browse the reference

The list of endpoints is generated from the API itself and published in the OpenAPI format:

* the Swagger interface: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html). It shows the parameters, data models and response codes of each endpoint, and lets you try a call once you have entered your key with the **Authorize** button;
* the OpenAPI definition in JSON: [https://api.dastra.eu/api/v1/dastra.json](https://api.dastra.eu/api/v1/dastra.json), to generate a client in your language;
* the API reference: [https://dastra.readme.io](https://dastra.readme.io).

Only the public endpoints of the API are listed there. The compliance module (frameworks, controls, tests, audits) has its own reference, whose routes start with `/v1/compliance/ws/{workspaceId}/`: [https://api.dastra.eu/v1/compliance/swagger/index.html](https://api.dastra.eu/v1/compliance/swagger/index.html).

## Read a path

A path starts with the API version and, for a workspace, with its identifier:

| Path | Use |
| --- | --- |
| `/v1/ws/{workspaceId}/Actors` | The stakeholders of a workspace |
| `/v1/ws/{workspaceId}/DataSubjectRequests` | The data subject requests of a workspace |
| `/v1/ws/{workspaceId}/Tags` | The tags of a workspace |
| `/v1/Workspaces` | The workspaces of the organization |

The HTTP method tells the action: `GET` reads, `POST` creates, `PUT` or `PATCH` modifies and `DELETE` deletes. Depending on the resource, additional routes exist, such as `/batch-delete` to delete several items or `/export/{format}` to export a list.

To check that an API key works, call `GET https://api.dastra.eu/me`.

For authentication, see [Authentication](authentication.md). For request limits, custom fields and tags, see [Configuration](configuration.md). For example calls, see [API use cases](use-cases.md).
