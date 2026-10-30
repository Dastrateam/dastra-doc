---
description: >-
  Configuration of an SSO connection using the OpenId protocol, with a secret
  key or a JWT private key.
---

# OpenId

## Operating principle

The OpenId specifications can be found [here](https://openid.net/connect/).

<figure><img src="../../../.gitbook/assets/openid1.png" alt="OpenID Connect authorization code flow between the relying party, the OpenID provider, the token endpoint and the UserInfo endpoint"><figcaption></figcaption></figure>

Setting up SSO with OpenId takes three steps:

* configure the authentication provider: Active Directory, Google Workspace, etc.;
* configure the service provider: Dastra;
* test the authentication.

## 1. Configure the authentication provider

Set up an OpenId configuration in your authentication provider.

For Active Directory: [https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc)

To link the local accounts (those hosted in Dastra) to the accounts of your provider, Dastra needs a property that contains the user's email. The **User's email address claim name mapping (Used if user does not exist locally)** field in step 2 is prefilled with `email`. If this claim is missing, Dastra also looks for the property named [http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress).

Here is the information you need to fill in the service provider:

* **Authority/Domain**, for example `https://account.oauth.sso.com`;
* **ClientId**;
* **Secret key**, or the elements of the JWT private key (see the client authentication method in step 2);
* **Response type**, `id_token` by default;
* **Scope**, `openid profile email` by default.

To configure your authentication provider, you need the **Redirect Url** shown in the Dastra form, in the format `https://account.dastra.eu/signin-{connection identifier}`. This URL is specific to each connection.

## 2. Configure the service provider

In Dastra, open the [SSO administration page](https://app.dastra.eu/general-settings/sso) (**Organisation Configuration** > **Single sign on**, available to organization owners only) and click **Add a SSO login**. Choose the **OpenID** protocol.

<figure><img src="../../../.gitbook/assets/settings-sso-liste-logins.png" alt="The Single sign on page with the list of SSO logins and the Add a SSO login button"><figcaption></figcaption></figure>

Fill in the form fields with the information from your authentication provider:

<figure><img src="../../../.gitbook/assets/settings-sso-openid-config-modal.png" alt="The OpenID SSO login form in Dastra"><figcaption></figcaption></figure>

The form also shows the values to declare in your authentication provider:

* **Redirect Url**;
* **Back-channel logout url**, optional;
* **Public JSON key URI**, with the JWT private key only. Save the form once to make this endpoint work.

Declare the **Back-channel logout url** in your provider if you want a sign-out at the provider to end the Dastra session too. Dastra supports OpenID Connect Back-Channel Logout: when your provider sends a logout token for a user or a session, Dastra revokes the matching sessions, so the user must sign in again.

### Client authentication method: secret key or JWT private key

Choose how Dastra authenticates with your identity provider:

* **Secret key**: Dastra and your provider both store the same client secret. Enter it in the **Secret key** field.
* **JWT private key**: Dastra signs its authentication with the private key you give it, and your provider checks the signature with the public key. No shared secret is needed, which lowers the risk of a leak. Check that your identity provider supports this method.

<figure><img src="../../../.gitbook/assets/settings-sso-openid-jwt-private-key.png" alt="The OpenID form with the JWT private key option selected"><figcaption></figcaption></figure>

With **JWT private key**, the **Response type** switches to `code` and the form asks for:

* **Private key in PEM text (RAW)**: once saved, the key is no longer displayed. Click **Replace private key** to replace it;
* **Certificate content (RAW format), mandatory for Entra Id**;
* **Key ID (kid)**, optional: enter the key ID assigned by your provider when you uploaded the public key, or leave it empty so that Dastra uses the JWK thumbprint (RFC 7638) of the private key.

Then declare the **Public JSON key URI** in your provider, so that it can retrieve the public key of the connection.

The **Issuer** field is optional. When it is filled in, Dastra checks that the token received was issued by this issuer, for example `https://login.microsoftonline.com/{tenantid}/v2.0`.

{% hint style="danger" %}
You can force all users of the organization to use a particular SSO (**Assign to all users** option). Be careful: if the SSO malfunctions, you can no longer access your account as an administrator. Keep a local fallback account, or exempt users with the **Specific users exempted from SSO (e.g. security administrators)** field (see [Single Sign On (SSO)](README.md)). Managing SSO per user is preferable.
{% endhint %}

{% hint style="warning" %}
**Special case of external users**\
Only accounts internal to a subscription are subject to SSO. Accounts of external users (who have an additional subscription) are not subject to SSO.
{% endhint %}

## 3. Test the SSO with OpenId

When the configuration is complete, test the authentication by clicking **Test** on the right of the connection in the list. If you run into a problem, open a ticket from the [support page](https://app.dastra.eu/general-settings/support).

<figure><img src="../../../.gitbook/assets/settings-sso-openid-card-status.png" alt="An SSO connection in the list, with its status and the Test button"><figcaption></figcaption></figure>
