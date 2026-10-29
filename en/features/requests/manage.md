---
description: >-
  Learn how to import, create, modify and delete a data subject right request
  via Dastra.
---

# Manage data subject right requests

## Creating a request

There are 5 ways to create a data subject right request in Dastra:

1. Manually, from the record of requests.
2. By importing a file (see [Importing and exporting requests](manage.md#importing-and-exporting-requests)).
3. Automatically, through a collection email address.
4. Automatically, through a request collection form.
5. Automatically, through the REST API.

### Creating a request manually

To create a request manually from the record, click **Requests** in the sidebar, then **Record of requests**, then the **Create a request** button.

<figure><img src="../../.gitbook/assets/requests-manage-1.png" alt="The record of requests, with the Create a request button"><figcaption><p>The record of requests</p></figcaption></figure>

{% hint style="info" %}
You can also create requests automatically (see below).
{% endhint %}

### Creating a request through a collection email address

To create requests from a collection email address, first activate the **Incoming mail data collection** integration (see [Incoming mail data collection](../settings/mailboxes.md)).

To do this, open **Workspace settings**, then the **Integrations** section, and click the **Incoming mail data collection** card.

<figure><img src="../../.gitbook/assets/requests-manage-2.png" alt="The card of the incoming mail data collection integration"><figcaption><p>The "Incoming mail data collection" integration in Dastra</p></figcaption></figure>

{% hint style="info" %}
If this integration is not installed yet, install it. From the record of requests, the **Convert emails into requests** entry of the **Create a request** button menu leads there directly.
{% endhint %}

Next, in the **Preconfigured use cases** list, click **Add integration** on the line **Transform an incoming email into a request to exercise rights with associated attachments**. An email address is generated automatically.

<figure><img src="../../.gitbook/assets/requests-manage-3.png" alt="The preconfigured use case that turns an incoming email into a request"><figcaption></figcaption></figure>

Each email sent to this address then becomes a request in Dastra, with its attachments.

### Creating a request through a collection form

To create requests automatically from a collection form (widget), see the "Set up a data subject right request widget" page:

{% content-ref url="widget.md" %}
[set-up-a-data-subject-right-request-widget.md](widget.md)
{% endcontent-ref %}

### Creating a request through the API

Requests can also be created from another tool through the Dastra REST API. See the "API integration" page:

{% content-ref url="api.md" %}
[api.md](api.md)
{% endcontent-ref %}

## Importing and exporting requests

Click the arrow next to the **Create a request** button, then click **Import**.

Then follow the guide to [importing data into Dastra](../general/import.md).

To export, click **Export** in the same menu.
