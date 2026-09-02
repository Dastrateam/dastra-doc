---
description: >-
  Meld u aan bij Dastra zonder wachtwoord met passkeys, gebaseerd op de WebAuthn
  / FIDO2-standaarden
---

# Passkeys

## Introductie

Een **passkey** vervangt uw wachtwoord door de biometrie of pincode van uw apparaat: vingerafdruk, gezichtsherkenning of ontgrendelingscode.

Dastra maakt gebruik van de open standaarden [WebAuthn](https://en.wikipedia.org/wiki/WebAuthn) en [FIDO2](https://en.wikipedia.org/wiki/FIDO_Alliance). In de praktijk betekent dit:

* De **privésleutel verlaat uw apparaat nooit** (of uw passkeybeheerder: iCloud Keychain, Google Password Manager, Windows Hello, 1Password, YubiKey…). Dastra bewaart alleen de openbare sleutel.
* Er is **geen gedeeld geheim** om te stelen: met een datalek kan niemand op uw account inloggen.
* Een passkey is **gebonden aan het domein van Dastra** en is daardoor van nature phishingresistent. Een frauduleuze website kan u niet verleiden om hem te gebruiken.

{% hint style="success" %}
Een aanmelding met een passkey met gebruikersverificatie (biometrie of pincode) geldt als **twee authenticatiefactoren**. U hoeft dus geen 6-cijferige code in te voeren, zelfs niet als uw organisatie [sterke authenticatie](mfa.md) verplicht stelt.
{% endhint %}

## Hoe maak ik een passkey aan?

Er zijn twee manieren.

### Via uw beveiligingsinstellingen

* Ga naar [https://app.dastra.eu/general-settings/account-security](https://app.dastra.eu/general-settings/account-security)
* Klik in het blok **Passkeys** op **Beheren**
* Geef uw passkey een naam (bijvoorbeeld "Mijn telefoon" of "MacBook pro") en klik op **Een passkey toevoegen**
* Volg de melding van uw browser of besturingssysteem (vingerafdruk, gezicht, pincode, fysieke beveiligingssleutel…)

### Via de uitnodiging na het inloggen

Na een aanmelding met wachtwoord stelt Dastra voor om een passkey aan te maken als u er nog geen hebt. U kunt:

* meteen **een passkey aanmaken**;
* **Later** kiezen: de uitnodiging wordt 90 dagen niet meer weergegeven in deze browser;
* **Vraag dit niet meer** kiezen: de uitnodiging wordt definitief uitgeschakeld voor uw account (u kunt nog altijd een passkey aanmaken via uw beveiligingsinstellingen).

## Hoe meld ik me aan met een passkey?

* Voer uw e-mailadres in op de aanmeldpagina
* Klik op het volgende scherm op **Aanmelden met een passkey**

<figure><img src="../.gitbook/assets/security-passkey-login-button.png" alt="Knop Aanmelden met een passkey op de aanmeldpagina"><figcaption><p>De knop "Aanmelden met een passkey" verschijnt zodra er een passkey voor uw account is geregistreerd</p></figcaption></figure>

* Bevestig met uw vingerafdruk, gezicht, pincode of beveiligingssleutel

{% hint style="info" %}
De knop verschijnt alleen als uw browser WebAuthn ondersteunt **én** er minstens één passkey op uw account is geregistreerd. Uw wachtwoord en de aanmeldlink per e-mail blijven beschikbaar.
{% endhint %}

## Uw passkeys beheren

Via het scherm **Beheren** (beveiligingsinstellingen van uw account) kunt u:

* **meerdere passkeys registreren** — dit is aan te raden: één per apparaat (telefoon, laptop, fysieke beveiligingssleutel) voorkomt dat u de toegang verliest als u een apparaat kwijtraakt;
* een passkey **hernoemen**;
* een passkey **verwijderen** die niet meer wordt gebruikt (apparaat verkocht, verloren of gestolen).

Het blok **Passkeys** in uw beveiligingsinstellingen toont ook wanneer elke passkey voor het laatst is gebruikt, zodat u verouderde sleutels snel opspoort.

{% hint style="info" %}
Als u geen naam invult, krijgt de passkey automatisch de aanmaakdatum als naam. Het toevoegen en verwijderen van een passkey wordt vastgelegd in de auditlogs van uw organisatie.
{% endhint %}

{% hint style="warning" %}
Als u uw laatste passkey verwijdert terwijl uw account geen wachtwoord heeft, kunt u zich alleen nog aanmelden met een eenmalige code per e-mail. In dat geval wordt om een bevestiging gevraagd.
{% endhint %}

## Beperkingen

* Passkeys zijn **niet beschikbaar voor gebruikers wier organisatie eenmalige aanmelding (SSO) verplicht stelt**: die gebruikers authenticeren zich bij hun identityprovider, die zelf passkeys kan aanbieden.
* Een verouderde browser of een verouderd besturingssysteem ondersteunt WebAuthn mogelijk niet. In dat geval krijgt u een melding.
