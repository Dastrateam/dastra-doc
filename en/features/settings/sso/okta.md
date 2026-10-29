---
description: >-
  Set up Okta as an identity provider in Dastra with the OpenID Connect
  protocol.
---

# Okta

This page explains how to set up Okta SSO login in Dastra with the **OpenID Connect** protocol. You can also do it with SAML: see [SAML 2](saml.md).

1. Sign in to the Okta admin console.
2. Open the **Applications** > **Applications** menu, then click **Create App Integration**.
3. Select **OIDC - OpenID Connect**.
4. Select the application type **Web application**.
5. Configure the application and tick **Implicit (hybrid)** under **Grant type**. For the application logo, you can [use this one](https://www.dastra.eu/img/press/logodastra.png).
6. In Dastra, get the redirect URL: open the [SSO management page](https://app.dastra.eu/general-settings/sso), click **Add a SSO login** and choose **OpenID**. In the **Configuration** section, at the bottom of the form, copy the redirect URL.

   <figure><img src="../../../.gitbook/assets/settings-okta-1.png" alt="The bottom of the Configuration section of the OpenID form, with the redirect URL to copy"><figcaption><p>The redirect URL shown by Dastra</p></figcaption></figure>
7. Go back to Okta and paste the redirect URL into **Sign-in redirect URIs**. Select the Okta users you want to give access to Dastra (by default, you can tick **Allow everyone**), then click **Save**.
8. Okta displays the settings page of the new application: the client ID (Client ID), the secret key (Client secret) and the Okta domain, which serves as the authority.
9. Go back to Dastra and fill in the form fields:

   * **ClientId**: copy the Client ID from Okta.
   * **Authority/Domain**: enter the Okta domain with the protocol (`https://<your domain>.okta.com`).
   * **Issuer**: leave the field empty.
   * **Secret key**: copy the client secret from Okta.
   * **Scope**: `openid profile email`.
   * **Response type**: `id_token`.

   <figure><img src="../../../.gitbook/assets/settings-okta-2.png" alt="The Dastra OpenID form filled in with the Okta values, with the secret values masked"><figcaption><p>The Dastra OpenID form</p></figcaption></figure>
10. Click **Save changes**, then click **Test** on the connection card. If Okta redirects you to Dastra, the setup is complete.
