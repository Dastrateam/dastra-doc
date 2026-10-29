---
description: Learn how to respond to data subject right requests.
---

# Data subject right request

With the GDPR, European citizens can ask a company or organization that processes their personal data to let them exercise their rights. The organization is required to make it easy to exercise those rights.

{% content-ref url="../../gdpr/concepts/rights.md" %}
[data-subject-rights.md](../../gdpr/concepts/rights.md)
{% endcontent-ref %}

To do this, the organization must set up procedures to answer these requests and to provide proof that it did so. This means defined steps and documentation kept in a register.

## The process for managing a data subject right request

Managing a request to exercise a right comes down to 4 main steps:

<figure><img src="../../.gitbook/assets/dsr-request-lifecycle-flowchart.png" alt="The four steps of managing a request: collection, identity check, processing, communication to the data subject, then closing or archiving"><figcaption><p>The DSR management process</p></figcaption></figure>

For more details on managing requests, see this page:

{% content-ref url="manage.md" %}
[manage-data-subject-right-requests.md](manage.md)
{% endcontent-ref %}

## The record of data subject right requests

Dastra lets you build a register that centralizes all past, present and future requests. To open it, click **Requests** in the sidebar, then **Record of requests**.

<figure><img src="../../.gitbook/assets/requests-readme-1.png" alt="The record of requests, with the Create a request button and the module menu"><figcaption><p>The record of requests</p></figcaption></figure>

The **Requests** menu gives access to five pages:

* **Record of requests**: the list of all requests, with their filters and columns.
* **Reporting**: the follow-up indicators (see [Request statistics](process.md#request-statistics)).
* **Messages**: the exchanges with requesters (see [Requester messages](process.md#requester-messages)).
* **Forms**: the widgets that collect requests on your website. This page is only available to users allowed to manage collection forms.
* **Requests processing**: the interface for asset owners (see [Request processing interface](advanced/asset-owners.md)).

## Add a new data subject right request

There are 5 ways to add a new request in Dastra:

1. [Enter the request directly in the tool](manage.md#creating-a-request-manually).
2. [Import requests from an Excel, CSV or text file](manage.md#importing-and-exporting-requests).
3. [Receive requests through a collection email address](manage.md#creating-a-request-through-a-collection-email-address).
4. [Set up a collection form (widget)](widget.md) on your website.
5. [Create requests through the REST API](api.md).

### Creating a request manually

Click **Create a request**. In the window that opens, fill in the title, the request type or types, the date, the language of the requester, the email address (optional) and the organizational unit, then click **Create**. Dastra opens the request so that you can detail and process it.

<figure><img src="../../.gitbook/assets/requests-readme-2.png" alt="The window for creating a request"><figcaption><p>The window for creating a request</p></figcaption></figure>

### Importing and exporting the request register

The whole register can be imported and exported. To import requests, click the arrow next to the **Create a request** button, then click **Import**.

<figure><img src="../../.gitbook/assets/requests-readme-3.png" alt="The drop-down menu of the Create a request button, with the Import, Export, Convert emails into requests and Read the documentation entries"><figcaption></figcaption></figure>

On the import screen, click **Download the file template** to see the expected format (**View columns format** lists the columns), then drop your file (csv, txt or xlsx) in the upload area. Follow the steps of the wizard (data importing, columns mapping, import and result) to import the requests into Dastra. Once imported, the requests are available in the register.

<figure><img src="../../.gitbook/assets/requests-readme-4.png" alt="The first step of the request import: downloading the template and uploading the file"><figcaption></figcaption></figure>

### Setting up a request widget

Requests can also come from a dedicated widget that you configure in Dastra.

See our [guide on setting up the data subject right request widget](widget.md).

{% content-ref url="widget.md" %}
[set-up-a-data-subject-right-request-widget.md](widget.md)
{% endcontent-ref %}
