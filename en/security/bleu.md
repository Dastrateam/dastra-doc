---
description: >-
  Dastra is also available on Bleu: a dedicated instance, isolated from our
  standard SaaS platform, whose data never leaves the Bleu perimeter.
---

# Dastra on Bleu (sovereign cloud)

## Who is this offering for?

Some organisations cannot or do not wish to host their compliance data on infrastructure exposed to non-European extraterritorial laws. Dastra meets these requirements through **Bleu**: a dedicated instance, separate from our standard SaaS platform, whose data never leaves the Bleu perimeter.

## What is Bleu?

Bleu is a French company owned by **Orange and Capgemini** that distributes Microsoft Azure and Microsoft 365 in an environment isolated from Microsoft's global infrastructure. The services are hosted in datacenters located in France (Île-de-France and southern France) and operated exclusively by French teams. The offering targets the French State, local authorities, healthcare institutions, operators of vital importance (OIV) and essential service operators (OSE), and provides legal protection against extraterritorial access laws (Cloud Act, FISA).

## SecNumCloud qualification: where do things stand?

The **SecNumCloud 3.2** qualification is issued by ANSSI at the end of a four-milestone process. For its IaaS, PaaS and CaaS scope, Bleu has passed **J0** (April 2025, application accepted) and **J1** (November 2025, evaluation strategy accepted). Bleu appears on the list of SecNumCloud providers in the course of qualification published by ANSSI. The next steps, the on-site evaluation (**J2**) and then the qualification decision (**J3**), have not yet been announced as completed; Bleu expects to complete the process by the end of 2026.

{% hint style="warning" %}
We therefore do not present Dastra on Bleu as a "SecNumCloud qualified" offering until ANSSI has published its decision.
{% endhint %}

## What changes compared with the standard offering

| | Standard offering | Bleu offering |
| --- | --- | --- |
| Application | app.dastra.eu | app-bleu.dastra.eu |
| API | api.dastra.eu | api-bleu.dastra.eu |
| Authentication | account.dastra.eu | <p>account-bleu.dastra.eu<br>(separate user directory, accounts and signing keys)</p> |
| SCIM provisioning | scim.dastra.eu | scim-bleu.dastra.eu |
| Hosting | Microsoft Azure France (Paris, Marseille) | Bleu France Central (Île-de-France) |
| AI features | Available | Available, run by **Mistral AI** (a French company, outside the Bleu perimeter) rather than Azure OpenAI |
| Full-text search | Available | Available, index hosted on Bleu |
| Connectors (Jira, ServiceNow, SAP LeanIX, DocuSign, Zapier, etc.) and API keys | Available | Available |
| SSO (SAML, OpenID Connect) | Available | Available |
| Editorial content inside the application (news, webinars) | Served by the standard platform | Same, read-only, with no customer data involved |
| Release cadence | Continuous | Same versions, deployed after the standard platform |

## Data location and backups

All production resources (databases, files, audit logs, search index, cache, secret vault, monitoring) are hosted in the **Bleu France Central** region. They are not replicated outside Bleu.

The only outbound flows are calls to the third-party services the standard offering already uses: Mistral AI for AI features (data processed on demand) and Brevo (a French company) for sending emails.

## Encryption, authentication and secrets

Unless stated otherwise below, the measures described on the [Security at Dastra](general.md) page apply to the Bleu instance.

* **TLS**: public traffic is terminated by the European CDN bunny.net, which manages the certificates; TLS 1.2 minimum is enforced on every resource (applications, databases, storage).
* **Secrets**: Azure Key Vault hosted on Bleu, accessible only to the applications' managed identities; no secret is stored in the application configuration.
* **Authentication**: dedicated identity server. An account from the standard platform cannot sign in on Bleu, and vice versa; there is no federation between the two. The sign-in page offers a region selector to direct users.

## Isolation and environments

The Bleu instance is **strictly isolated** from the standard platform: databases, storage, logs, cache, search index, secret vault and identities are all separate. The only flow between the two platforms is the read-only synchronisation of our reference libraries (templates, frameworks) towards Bleu; no customer data is transferred.
