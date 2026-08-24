---
description: Send Dastra workflow notifications to your Microsoft Teams channels
---

# Microsoft Teams

### What does the integration do?

The Microsoft Teams integration posts **Dastra workflow notifications as cards in a Microsoft Teams channel**: when a workflow rule fires (a data breach is created, a request changes step…), Dastra sends an Adaptive Card with a title, a message and an optional link back to the record in Dastra.

<!-- 📸 Screenshot: a Dastra notification card rendered in a Teams channel, with the "View in Dastra" button -->

<figure><img src="../../.gitbook/assets/msteams-card.png" alt=""><figcaption><p>A Dastra workflow notification in Teams</p></figcaption></figure>

### Prerequisites

You need a Microsoft Teams channel with an **incoming webhook created through the Workflows app** (Power Automate):

1. In Teams, open the channel and click **⋯ > Workflows**.

<figure><img src="../../.gitbook/assets/teams-workflows-menu.png" alt=""><figcaption><p>The Workflows entry in the channel menu</p></figcaption></figure>

2. Search for "webhook" and choose the template **Send webhook alerts to a channel**.

<figure><img src="../../.gitbook/assets/teams-workflows-template.png" alt=""><figcaption><p>Choosing the webhook template</p></figcaption></figure>

3. Select the team and the channel, then click **Save**.

<figure><img src="../../.gitbook/assets/teams-workflows-config.png" alt=""><figcaption><p>Binding the workflow to the channel</p></figcaption></figure>

4. On the confirmation screen, click **Copy webhook link** — this is the URL you will paste into Dastra (it looks like `https://prod-XX.westeurope.logic.azure.com/workflows/...`).

<figure><img src="../../.gitbook/assets/teams-workflows-link.png" alt=""><figcaption><p>Copying the webhook URL</p></figcaption></figure>

{% hint style="info" %}
Microsoft retired the classic Office 365 incoming webhooks (channel connectors) in April 2026. The Workflows app is Microsoft's replacement, and it is what this integration relies on.
{% endhint %}

### Installation

1. In Dastra, open **Settings > Integrations** and select **Microsoft Teams**.
2. On the use case **Post workflow rule notifications as cards in a Microsoft Teams channel**, click **Add integration**.
3. Add a connection and paste the **Workflows webhook URL**.
4. Click **Connect**. Dastra immediately posts a test card ("*Dastra test notification*") into the channel to validate the URL.

<!-- 📸 Screenshot: the Microsoft Teams connection modal with the "Workflows webhook URL" field -->

<figure><img src="../../.gitbook/assets/msteams-install.png" alt=""><figcaption><p>Installing the Microsoft Teams integration</p></figcaption></figure>

{% hint style="warning" %}
The webhook URL must be an HTTPS Power Automate endpoint (`*.logic.azure.com`, `*.azure-api.net` or `*.api.powerplatform.com`). Other hosts are rejected.
{% endhint %}

To notify **several channels**, create one connection per channel (each Workflows webhook targets a single channel).

### Sending notifications from a workflow rule

Once the integration is installed and enabled, the workflow rule designer offers a new action: **Send a Teams notification**.

Configure it like the e-mail notification action:

* **Card title** — supports merge variables (e.g. the record's name).
* **Message** — rich text with merge variables.
* **Include a link to the object in the card** — adds a **View in Dastra** button to the card.

There is no recipient to pick: the card is delivered to the channel behind the webhook.

<!-- 📸 Screenshot: the workflow rule designer with the "Send a Teams notification" action form (Card title, Message, link switch) -->

<figure><img src="../../.gitbook/assets/msteams-action.png" alt=""><figcaption><p>The "Send a Teams notification" workflow action</p></figcaption></figure>

{% hint style="info" %}
The Teams action only appears in the action picker when the integration is installed and enabled on the workspace.
{% endhint %}

### Uninstalling

When you uninstall the Microsoft Teams integration, the webhook URL is erased and every workflow rule that uses the Teams action is **automatically disabled** (not deleted), so your rules don't start failing. Re-enable them after reinstalling the integration.
