---
description: Dastra integrates with Zapier automation platform and many other tools
---

# Integrations

## Integrations

Dastra connects to the tools your teams already use: import your application inventory from your ITAM or CMDB, synchronize data subject requests with your ticketing tool, post notifications in your collaboration channels, stream your security audit logs to your SIEM, or attach files from your cloud drives. Native connectors cover the most common tools; Zapier covers everything else.

The integration store is available in **Settings > Integrations** of your workspace. It lists every available integration, filterable by category and by the Dastra object it targets, with an **All / Installed** switch.

#### How native integrations work

Every native integration is built on three concepts:

* **Use cases** — each integration exposes one or more use cases (for example _import applications as assets_ or _synchronize data subject requests_). Use cases are installed, enabled, configured and uninstalled independently.
* **Connections** — a connection stores how Dastra authenticates against the external tool: credentials stored encrypted by Dastra, or a delegated OAuth authorization. You can create several connections to the same tool (a production and a sandbox instance, for instance) and choose which one each use case relies on. Connections display their health and can be tested at any time.
* **Field mapping** — import use cases let you choose, for each Dastra field, the external field that fills it, with default values, value transcoding for closed lists (statuses, lifecycle stages…) and AI-assisted suggestions.

Import connectors synchronize once a day and on demand with **Run synchronization now**. Every execution is traced in the integration logs, with the number of created, updated, flagged and in-error items.

<figure><img src="../../.gitbook/assets/integrations-catalog.png" alt=""><figcaption></figcaption></figure>

Read the details in [Connections, use cases and field mapping](connections.md).

#### Available integrations

| Integration                 | What it does                                                                                                                               | Documentation                                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **ServiceNow**              | Imports the business applications of your CMDB as assets and keeps them in sync daily                                                      | [ServiceNow](servicenow.md)                                                         |
| **SAP LeanIX**              | Imports your Application fact sheets as assets and keeps them in sync daily                                                                | [SAP LeanIX](sap-leanix.md)                                                         |
| **Jira**                    | Creates and tracks data subject requests from your Jira project, and sends your tasks to Jira as issues kept in sync (status, assignee, mapped fields) | [Jira](jira.md)                                                                     |
| **Filerskeepers**           | Integrates your Filerskeepers retention policies with Dastra                                                                               | [Filerskeepers](filerskeepers.md)                                                   |
| **Microsoft Teams**         | Posts your workflow rule notifications as cards in a Teams channel                                                                         | [Microsoft Teams](microsoft-teams.md)                                               |
| **HTTP / Custom API**       | Calls any external API from your workflow rules with a custom HTTP request — method, URL, headers and a JSON or XML body built from the record | [HTTP / Custom API](custom-http.md) |
| **Slack**                   | Delivers Dastra notifications in your Slack workspace                                                                                      | —                                                                                                                                       |
| **Docusign**                | Sends your contracts to your subcontractors for electronic signature                                                                       | [Docusign integration](../contracts/docusign.md)                                          |
| **OneDrive & SharePoint / Google Drive** | Attaches files from your OneDrive, SharePoint libraries or Google Drive to your actors, security measures, processing activities, tasks, incidents… | [OneDrive & SharePoint / Google Drive integrations](../settings/cloud-storage.md)                   |
| **Office 365 / Gmail**      | Sends Dastra emails from your own mailbox                                                                                                  | [SMTP configuration](../settings/smtp/README.md)                                                |
| **Incoming mail**           | Turns the emails sent to a dedicated collection address into tasks, requests, data breaches, contracts or processing activities            | [Incoming mail data collection](../settings/mailboxes.md)                                 |
| **SIRENE (INSEE)**          | Fills in your stakeholders' details from the French company registry                                                                       | —                                                                                                                                       |
| **AI provider**             | Connects any OpenAI-compatible AI provider to the Dastra assistant                                                                         | —                                                                                                                                       |
| **Single sign-on (SSO)**    | Lets your users sign in with your own identity provider                                                                                    | [Single Sign On (SSO)](../settings/sso/README.md)                                                 |
| **SIEM streaming**          | Streams your security audit events to your SIEM in real time                                                                               | [SIEM streaming](../settings/siem.md)                                                           |
| **Zapier**                  | Connects Dastra to more than 3,000 applications through automated workflows                                                                | [Integrating Dastra with external tools](zapier/external-tools.md) |

Some integrations apply to your whole organization rather than to a workspace — single sign-on, SIEM streaming, Office 365 / Gmail and the AI provider. Their tile in the store takes you to the corresponding organization settings, where they are configured by an account owner.

#### Zapier: connect everything else

Zapier is an online automation tool that connects your applications and services without code. A **Zap** is an automated workflow made of a **trigger** and one or more **actions**: when the trigger event occurs, the actions run.

On the Dastra side, Zapier can react to two triggers — _new data subject request created_ and _new task created_ — and perform six actions: create a task, create an actor, create a data subject request, link an actor to an existing processing activity, search an actor, and find or create an actor. You can therefore start from a Dastra event to act in a third-party application, or start from a third-party event to act in Dastra.

Pre-configured templates (Salesforce, Zoho, Trello, Google Sheets, Excel, Outlook, Azure DevOps…) are available from the [Dastra page of the Zapier catalog](https://zapier.com/apps/dastra/integrations), and the Zap editor lets you build your own workflow from scratch. See [Integrating Dastra with external tools](zapier/external-tools.md) and the [Zapier FAQ](zapier/faq.md).

#### Security and data protection

* Integration credentials and tokens are stored encrypted, are never returned by the API, and are erased when you uninstall an integration or delete a workspace.
* OAuth flows strictly validate their callbacks, and the inbound webhook endpoints are rate-limited.
* Integrations are scoped to a workspace: data from one workspace is never visible from another.
* Records created by an integration (assets, requests…) belong to your workspace and are kept when the integration is uninstalled.

#### Need something else?

If no integration matches your need, the [Dastra REST API](../../api/configuration.md) lets you build your own scripts and connectors, and you can submit a connector request to the Dastra team through the support.
