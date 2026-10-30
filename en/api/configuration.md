# Configuration

This page describes the Dastra REST API: its address, its usage limits, and how to handle custom fields and tags in it. To get a key and call the API, see [Authentication](authentication.md).

## Setting up APIs in Dastra

API stands for _**application programming interface**_.

APIs let you connect the Dastra platform to other external tools.

The possibilities are numerous: connection with CRM software to retrieve stakeholders automatically, synchronization of a rights management tool with the Dastra module, etc.

Dastra is based on the **REST API** standard, including the following HTTP requests:

| URI                                                                | GET                                                                                                | POST                                                                                                                                                                                                                    | PUT                                                                                                                                                                             | PATCH                                                                                                                                                                         | DELETE                                                                        |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Resource collection, such as `http://api.exemple.com/collection/`  | Retrieves the URIs of the member resources of the resource collection in the body of the response. | Creates a member resource in the collection resource using the instructions in the request body. The URI of the created member resource is automatically assigned and returned in the response's Location header field. | Replaces all representations of the collection resource's member resources with the representation in the request body, or creates the collection resource if it doesn't exist. | Updates all representations of the resource collection's member resources using the instructions in the request body, or creates the resource collection if it doesn't exist. | Deletes all representations of member resources from the collection resource. |
| Member resource, such as `http://api.exemple.com/collection/item3` | Retrieves a representation of the member resource in the body of the response.                     | Creates a member resource in the member resource using the instructions in the request body. The URI of the created member resource is automatically assigned and returned in the response's Location header field.     | Replaces all representations of the member resource, or creates the member resource if it doesn't exist, with the representation in the request body.                           | Updates all representations of the member resource, or creates the member resource if it doesn't exist, using statements in the request body.                                 | Deletes all representations of the member resource.                           |

Source: [_Wikipedia_](https://en.wikipedia.org/wiki/Representational_state_transfer)

## Address and versions

The Dastra API is available at `https://api.dastra.eu`. Routes are versioned and start with `/v1/`.

* The routes of a workspace contain its identifier: `/v1/ws/{workspaceId}/{resource}`, for example `/v1/ws/{workspaceId}/DataSubjectRequests`. The identifiers are in the **tenantId & workspaceId** tab of the **Api keys & MCP** page.
* The routes that concern the whole organization have no workspace identifier, for example `/v1/Workspaces`.

## Endpoint reference

The list of endpoints, with their parameters and data models, is published in the OpenAPI format:

* the Swagger interface: [https://api.dastra.eu/swagger/index.html](https://api.dastra.eu/swagger/index.html);
* the OpenAPI definition in JSON: [https://api.dastra.eu/api/v1/dastra.json](https://api.dastra.eu/api/v1/dastra.json).

It only contains the public endpoints of the API. The compliance module (frameworks, controls, tests, audits) has its own API, whose routes start with `/v1/compliance/`: [https://api.dastra.eu/v1/compliance/swagger/index.html](https://api.dastra.eu/v1/compliance/swagger/index.html).

The references are also available on [dastra.readme.io](https://dastra.readme.io). For a complete example, see [API use cases](use-cases.md).

## Limitations

Requests are counted per user, that is the owner of the API key, according to their type:

| Request type | Limit |
| --- | --- |
| Read (`GET`) | 500 per minute and 10,000 per 10-minute period |
| Write (`POST`, `PUT`, `PATCH`, `DELETE`) | 75 per minute and 1,000 per 10-minute period |
| Sensitive endpoints | 5 per 5-minute period |

A few endpoints, such as the AI assistant ones, have stricter limits.

Beyond a limit, the API answers with HTTP status 429 and a `Retry-After` header that gives, in seconds, the delay before you can try again. Wait for that delay before sending the request again.

To check your counters, call `GET https://api.dastra.eu/rate-limiting-state`.

Security options, such as [IP filtering](../features/settings/ip-filtering.md), do not apply to calls made with an API key.

## Exposing custom fields in the Dastra API

In Dastra, you can expose in the API the [custom fields](../features/general/custom-fields.md) designed in your Dastra workspace.

Custom fields are specific to each workspace. To include them in the API, first define the **Variable name (slug)** in the definition of the custom field:

<figure><img src="../.gitbook/assets/general-custom-fields-4.png" alt="The Add custom field window with the label and the variable name (slug)"><figcaption><p>The variable name of a custom field</p></figcaption></figure>

{% content-ref url="../features/general/custom-fields.md" %}
[custom-fields.md](../features/general/custom-fields.md)
{% endcontent-ref %}

Most entities that can be modified through the API expose a `customFields` property that you can modify.

If you define the following fields in your workspace:

* `my_string_field`: a **Text** field;
* `my_boolean_field`: a **Boolean** field;
* `my_numeric_field`: a **Number (integer)** field;
* `my_checkbox_field`: a **Check box** field.

you can modify them like this:

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

For a **Check box** field, the value is the list of the labels of the ticked answers.

## The case of tags

To link tags to an entity, first retrieve the existing tags with `GET /v1/ws/{workspaceId}/Tags`, then add the ones you want to the `tags` property of the entity, using their `id`.

## MCP server

The MCP (Model Context Protocol) server lets an AI assistant, a code editor or a terminal work with your Dastra data. You set it up in the **MCP Server** tab of the **Api keys & MCP** page, and it requires the Dastra AI Pro plan. See [The MCP server](../features/general/ai-assistant/mcp.md).

{% hint style="warning" %}
Calls that create, modify or delete data act on your real records. Test them first on a dedicated workspace.
{% endhint %}

API keys are managed in the **Api keys & MCP** page, which is reserved to organization owners. See [API key management](../features/settings/api-keys.md).
