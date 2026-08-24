---
description: Overview of the integration changes shipped in Dastra 2.0.6
---

# Integrations — What's new in 2.0.6

Dastra 2.0.6 ships a complete overhaul of the native integrations, two new connectors and a new SIEM streaming capability.

### A redesigned integration experience

The integration store and the setup flow have been rebuilt around three concepts: **connections**, **use cases** and **field mapping**.

* A **connection** stores how Dastra authenticates against the external tool (credentials or an OAuth authorization). You can create several connections to the same tool (different accounts or environments) and choose which one each use case relies on.
* Each integration exposes one or more **use cases** (e.g. *import applications as assets*, *sync data subject requests*). Use cases are installed, enabled, configured and uninstalled independently.
* Import use cases come with a **field mapping editor**: for each Dastra field, choose the external field that fills it, define default values, transcode source values into Dastra values, and let the AI assistant suggest a mapping.

<!-- 📸 Screenshot: the integration detail page of ServiceNow or SAP LeanIX, showing the use case cards and the "Manage connections" button -->

<figure><img src="../../.gitbook/assets/integration-page-usecases.png" alt=""><figcaption><p>The new integration page: use cases on top, connections managed separately</p></figcaption></figure>

Read the details in [Connections, use cases and field mapping](connections-and-field-mapping.md).

### New connector: Microsoft Teams

Send Dastra workflow notifications to your Microsoft Teams channels. Once the integration is installed, a new **Send a Teams notification** action is available in the workflow rule designer, and posts an Adaptive Card (title, message with variables, link back to Dastra) into the channel of your choice.

Read more: [Microsoft Teams](microsoft-teams.md).

### New connector: SAP LeanIX

Import your SAP LeanIX **Application** fact sheets into the Dastra asset registry and keep them in sync daily. The connector discovers your LeanIX data model live — including custom attributes — and ships with a ready-to-use default mapping (display name, description, lifecycle → application state).

Read more: [SAP LeanIX](sap-leanix.md).

### New: SIEM streaming

Stream your account's security audit events (logins, permission changes, API keys, SSO, deletions…) to your SIEM in real time — Splunk HEC (JSON), CEF or Syslog RFC 5424 — or export them manually from the audit logs page in the same formats.

Read more: [SIEM streaming](../../features/settings/siem-streaming.md).

{% hint style="info" %}
SIEM streaming is available on the Enterprise plan and is configured by the account owner in the **Security center**.
{% endhint %}

### Improved connectors

* **Jira** — the setup now uses the unified integration page: named connections (API token, or **Sign in with Atlassian** where OAuth is available), a single configuration screen with field mapping (including Jira custom fields and value transcoding), mapping of DSR workflow steps to Jira transitions, and a webhook step with optional one-click registration in Jira.
* **ServiceNow** — OAuth 2.0 is now supported next to Basic authentication, and the synchronization options gain configurable deduplication (match on **Label** or **Reference**) and error notifications.
* **Import connectors** (ServiceNow, SAP LeanIX, Filerskeepers) — a **Run synchronization now** action triggers an immediate sync, and execution logs (created / updated / flagged items) are available from the use case card.

### Security hardening

* Integration credentials and tokens are stored encrypted, are never returned by the API, and are erased when you uninstall an integration or delete a workspace.
* OAuth flows now strictly validate callbacks (state validation, workspace binding).
* The inbound webhook endpoints are rate-limited.
