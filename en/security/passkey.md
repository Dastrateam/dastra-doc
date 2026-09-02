---
description: >-
  Sign in to Dastra without a password using passkeys, built on the WebAuthn /
  FIDO2 standards
---

# Passkeys

## Introduction

A **passkey** replaces your password with your device's biometrics or PIN: fingerprint, face recognition or unlock code.

Dastra relies on the open [WebAuthn](https://en.wikipedia.org/wiki/WebAuthn) and [FIDO2](https://en.wikipedia.org/wiki/FIDO_Alliance) standards. In practice:

* The **private key never leaves your device** (or your passkey manager: iCloud Keychain, Google Password Manager, Windows Hello, 1Password, YubiKey…). Dastra only stores the public key.
* There is **no shared secret** to steal: a database leak cannot be used to sign in to your account.
* A passkey is **bound to the Dastra domain**, which makes it phishing-resistant by design. A fraudulent website cannot trick you into using it.

{% hint style="success" %}
A passkey login with user verification (biometrics or PIN) counts as **two authentication factors**. You therefore have no 6-digit code to enter, even if your organization enforces multi-factor authentication.
{% endhint %}

## How to create a passkey

There are two ways.

### From your security settings

* Go to [https://app.dastra.eu/general-settings/account-security](https://app.dastra.eu/general-settings/account-security)
* In the **Passkeys** card, click **Manage**
* Give your passkey a name (for example "My phone" or "MacBook pro"), then click **Add a passkey**
* Follow the prompt from your browser or operating system (fingerprint, face, PIN, hardware security key…)

### From the prompt shown after signing in

After a password login, Dastra invites you to create a passkey if you do not have one yet. You can:

* **Create a passkey** right away;
* choose **Later**: the prompt will not be shown again on this browser for 90 days;
* choose **Don't ask me again**: the prompt is permanently disabled for your account (you can still create a passkey from your security settings).

## How to sign in with a passkey

* Enter your email address on the login page
* On the next screen, click **Sign in with a passkey**
* Confirm with your fingerprint, face, PIN or security key

{% hint style="info" %}
The button only appears if your browser supports WebAuthn **and** at least one passkey is registered on your account. Your password and the email login link remain available.
{% endhint %}

## Managing your passkeys

From the **Manage** screen (your account security settings) you can:

* **register several passkeys** — this is recommended: one per device (phone, laptop, hardware security key) prevents you from losing access if you lose a device;
* **rename** a passkey;
* **delete** a passkey that is no longer used (device sold, lost or stolen).

The **Passkeys** card in your security settings also shows the last time each passkey was used, which makes it easy to spot an obsolete one.

{% hint style="info" %}
If you leave the name empty, the passkey is named automatically after its creation date. Adding and deleting a passkey are recorded in your organization's audit logs.
{% endhint %}

{% hint style="warning" %}
If you delete your last passkey while your account has no password, you will only be able to sign in with a one-time code sent by email. A confirmation is requested in that case.
{% endhint %}

## Limitations

* Passkeys are **not available to users whose organization enforces single sign-on (SSO)**: those users authenticate against their identity provider, which may itself offer passkeys.
* An outdated browser or operating system may not support WebAuthn. A message informs you if that is the case.
