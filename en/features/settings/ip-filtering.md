---
description: >-
  Restrict sign-in to Dastra to allowed IP address ranges: scope, behaviour,
  blocking and points of attention.
---

# IP filtering

IP filtering lets you restrict access to your Dastra organisation to a list of allowed IP address ranges (for example your offices or your corporate VPN). It is configured in **Configuration** > **Security**.

{% hint style="info" %}
This feature is reserved for the Enterprise plan or a paid option. Contact your Dastra representative to enable it.
{% endhint %}

{% hint style="danger" %}
A warning states "This action is not reversible". In practice, a filtering rule cannot be deleted or disabled from the interface: **only the Dastra administration team** can remove it. Check your ranges carefully before saving them, or you may lock yourself out.
{% endhint %}

## Defining rules

* Rules apply to the **whole organisation** (not to a single workspace).
* Each rule is a range with a **start address** and an **end address**. CIDR notation (e.g. `10.0.0.0/24`) is not supported: convert your networks into start and end addresses.
* Both **IPv4 and IPv6** addresses are accepted.
* There is no limit to the number of rules.

## Who is affected?

Filtering applies to **all users of the organisation, administrators included**. There is no administrator exemption and no exemption list.

It covers every sign-in method, because the check happens after authentication:

* username and password;
* SSO (SAML 2, OpenID, ADFS, Entra, Okta);
* passkey;
* magic link or e-mail invitation.

Local service accounts exempted from SSO are **not** exempted from IP filtering.

## When is the check performed?

The IP address is checked at sign-in, then at every **token renewal**. An already open session is therefore not cut instantly if the user changes network (for example from the office to remote work): it ends at the next token renewal.

Token validity:

| Session type | Token validity |
|---|---|
| Web application | 6 minutes (renewed automatically) |
| Standard session | 1 hour |
| "Remember me" | 30 days |

## Which IP address is used?

Dastra uses the public IP address seen by its access infrastructure (the layer that receives your request before the application). A user going through a VPN or corporate proxy is therefore filtered on the VPN or proxy **exit address**: this is the address you must allow.

## What a blocked user sees

The user is redirected to an error page displaying:

> IP Address not allowed — Your IP address is not allowed by your organization. Please contact your account's administrator.

{% hint style="warning" %}
Blocked attempts are **not** recorded in the audit log and are not sent to [SIEM streaming](siem.md).
{% endhint %}

## What filtering does not cover

| Access | Filtered? |
|---|---|
| API calls using an [API key](api-keys.md) | No |
| [SCIM](scim.md) | No |
| [SIEM streaming](siem.md) and BI connectors | No |
| External questionnaire respondents (public link) | No |
| Data subject rights portal and Privacy Hub | No, they have their own settings (see [Privacy Hub - Security](../trust-center/configuration/security.md)) |

## Dastra support

Dastra support is also subject to filtering: it can no longer access your account (impersonation) from a non-allowed address. To delete or disable a rule, contact Dastra support.
