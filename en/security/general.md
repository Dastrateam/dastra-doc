---
description: >-
  Hosting, encryption, authentication, access control and backups: the security
  measures Dastra applies to protect your data.
---

# Security at Dastra

This page describes the security measures Dastra applies to protect your data: hosting, encryption, authentication, access control and backups.

{% hint style="info" %}
The organization security settings (mandatory strong authentication, IP address filtering, email domain filtering, password renewal policy, automatic sign-out, security log retention, SIEM streaming) are reserved for organization owners and for the Enterprise plan. They are in **Organisation Configuration** > **Security**. For each setting, see [Organization security and security logs](../features/settings/security-center.md).
{% endhint %}

## Secure cloud hosting

We host the platform data with Microsoft Azure. We chose this platform because most of our customers already use it (Microsoft 365, etc.) and because it offers a security level [among the highest on the market](https://learn.microsoft.com/en-us/azure/compliance/).

Data is stored in France: in Paris for production data and in Marseille for backups. Data is also replicated in the Amsterdam data center for redundancy.

For a dedicated instance on a sovereign cloud, see [Dastra on Bleu](bleu.md).

## Two-factor authentication

Two-factor authentication uses the TOTP protocol.

Each user can enable two-factor authentication for their own account. Organization owners can also make it mandatory for all internal users managed by the organization.

See [Strong authentication](mfa.md).

## Single sign-on (SSO) and SCIM

Depending on the plan you choose, or as an option, Dastra offers [self-service SSO](../features/settings/sso/README.md). We support the SAML2P and OpenID protocols, which are compatible with most corporate directories. You can also automatically provision the users of your directory with our [SCIM](../features/settings/scim.md) server.

## Encryption of data in transit

All data exchanged between our customers and applications is encrypted in transit with the TLS (Transport Layer Security) protocol and PFS (Perfect Forward Secrecy). The certificate authority is Cloudflare, Inc.

## Encryption of data at rest

The data disks of the servers that host customer data in the Azure cloud are encrypted at rest with [Transparent Data Encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver16).

Files are also encrypted at rest in the Azure Storage service, with transparent 256-bit [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) encryption, which is FIPS 140-2 compliant.

All encryption keys are stored in a key vault managed by Dastra, with automatic rotation.

## Penetration tests (pentests)

We have the security of the application audited every year by an independent third party.

The latest test found no critical vulnerability.

Our testing methodology follows the **OWASP** recommendations and has several phases, from open-source information gathering (reconnaissance) to the exploitation of the vulnerabilities found.

## Security audit logs

Organization administrators can track all changes to user management, workspaces and access permissions.

Organization owners set how long security logs are kept in **Organisation Configuration** > **Security**, card **Security logs retention**: from 30 days to 3 years (180 days recommended). Logs older than this period are purged every night.

To stream these events continuously to your monitoring tool, see [SIEM streaming](../features/settings/siem.md).

## Unique identifiers

Each user has a unique identifier. Accounts shared between several users are not allowed.

## Data backup

All the data (Azure SQL) and files (Azure Blob Storage) of our users are backed up regularly, with a 3-month history (long-term retention) and point-in-time restore (PITR) over 7 days.

## Data archiving rules

When an account is deleted, its data is kept for 1 month before it is permanently deleted.

## Password policy

* At least **10 characters**, with **4 types of characters**: uppercase letters, lowercase letters, digits and special characters.
* Delay in accessing the account after several failed sign-in attempts.
* Encryption of passwords in the database.

## Password renewal policy

Organization owners can set a password lifetime in [Organisation Configuration > Security](https://app.dastra.eu/general-settings/security), card **Password reset policy**. It applies to the internal users of the organization who do not use SSO. When the period expires, the user creates a new password at their next sign-in.

## Automatic sign-out

Organization owners can turn on the **Idle timeout automatic logout** card: all internal users managed by the organization are then signed out after 1 hour of inactivity.

## API token controls

View and manage all the [API keys](../features/settings/api-keys.md) used by the developers of your organization. You can also limit the scope of a key to one workspace and to specific permissions.

## Access control

Dastra uses the [RBAC](https://en.wikipedia.org/wiki/Role-based_access_control) (Role-Based Access Control) access management model. The organization owner chooses the [roles and permissions](../features/settings/roles.md) of each user with fine granularity.

## Secure authentication based on OpenID Connect for all our sites

The authentication authority is [https://account.dastra.eu](https://account.dastra.eu). It uses OpenID to authenticate all our users.

**OpenID** is a decentralized [authentication](https://en.wikipedia.org/wiki/Authentication) system that enables [single sign-on](https://en.wikipedia.org/wiki/Single_sign-on) as well as attribute sharing. It lets a user authenticate with several sites that support this technology, using a single OpenID identifier, without having to remember a separate identifier for each of them.

## IP address allow list

You can restrict access to the organization to allowed IP address ranges. Filtering applies to all users (administrators included) and to every sign-in method (password, SSO, passkey, magic link), at sign-in and at every token renewal. It does not apply to APIs, SCIM or SIEM streaming.

Dastra checks that your own IP address belongs to the allowed ranges. Check your ranges carefully before you save them: a rule cannot be removed from the interface. For details, see the [IP filtering](../features/settings/ip-filtering.md) page.

## Email domain allow list

Organization owners can define the list of allowed email domains (for example `example.com`): only users whose email address belongs to one of these domains can sign in. Go to **Organisation Configuration** > **Security**, card **Filter the domains of your users' emails**. The configuration can take a few minutes to apply.

## Strict isolation between production and development environments

With the exception of a few authorized people, application developers never use or access production environment data. This isolation is strict and cannot be bypassed.

In test and pre-production environments, we only use test data sets that we created ourselves.
