---
description: >-
  Meld u aan bij Dastra met een wachtwoord, een passkey, een link per e-mail of SSO en beveilig uw account.
---

# Aanmelden en authenticatie beheren

Deze pagina legt uit hoe u zich aanmeldt bij Dastra, hoe u uw wachtwoord opnieuw instelt en hoe u de beveiliging van uw account versterkt: sterke authenticatie, passkeys en actieve sessies.

## Aanmelden bij Dastra

Aanmelden gaat in twee stappen: u vult eerst uw e-mailadres in en kiest daarna hoe u zich authenticeert.

### Met uw e-mailadres en wachtwoord

1. Ga naar [app.dastra.eu](https://app.dastra.eu).
2. Vul bij **E-mail** uw zakelijke e-mailadres in en klik op **Ga verder**.
3. Vul **Je wachtwoord** in en klik op **Verbinding**.

<figure><img src="../../.gitbook/assets/getting-started-login-1.png" alt="Eerste aanmeldstap: zakelijk e-mailadres en de knop Ga verder"><figcaption><p>Eerste stap: het e-mailadres</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/getting-started-login-2.png" alt="Tweede aanmeldstap: wachtwoord en andere aanmeldopties"><figcaption><p>Tweede stap: het wachtwoord en de andere aanmeldopties</p></figcaption></figure>

{% hint style="info" %}
Vink **Onthoud mijn wachtwoord** alleen aan op een persoonlijk apparaat.
{% endhint %}

### Met een Google- of Microsoft-account

Klik op de eerste stap onder **Of** op **Maak contact met** gevolgd door Google of Microsoft en volg daarna de procedure van de provider. U koppelt een extern account aan uw Dastra-account via **beveiliging** > **Externe aanmeldingen**.

### Met SSO

Als uw organisatie [single sign-on (SSO)](../../features/settings/sso/README.md) heeft ingesteld, meldt u zich aan met uw identiteitsprovider.

1. Klik op de eerste stap op **Maak verbinding met SSO**.
2. Vul **E-mailadres in je organisatie** in en klik op **Ga verder**.
3. Volg de authenticatieprocedure van uw organisatie. Dastra stuurt u daarna door naar uw werkruimte.

<figure><img src="../../.gitbook/assets/getting-started-login-3.png" alt="Aanmeldpagina voor SSO: veld voor de SSO-gebruikersnaam en de knop Ga verder"><figcaption><p>Aanmelden met SSO</p></figcaption></figure>

Met SSO blijven uw inloggegevens bij uw identiteitsprovider: Dastra ontvangt uw wachtwoord niet.

### Met een passkey

Een passkey vervangt het wachtwoord door uw vingerafdruk, uw gezicht of de pincode van uw apparaat. Klik op de tweede stap op **Inloggen met een passkey**.

U registreert uw passkeys via **beveiliging** > **Beheer mijn passkeys**. Zie [Passkeys](../../security/passkey.md).

### Met een aanmeldlink per e-mail

Klik op de tweede stap op **Stuur de toegang link per e-mail**. Dastra stuurt een link naar uw e-mailadres waarmee u zich zonder wachtwoord aanmeldt.

## Uw wachtwoord opnieuw instellen

1. Klik op de tweede aanmeldstap op **Wachtwoord vergeten ?**.
2. Vul het e-mailadres in dat aan uw account is gekoppeld.
3. Open de e-mail die u ontvangt en volg de link om het wachtwoord opnieuw in te stellen.
4. Kies een nieuw wachtwoord.

<figure><img src="../../.gitbook/assets/getting-started-login-4.png" alt="Pagina om het wachtwoord opnieuw in te stellen"><figcaption><p>De pagina om het wachtwoord opnieuw in te stellen</p></figcaption></figure>

Werkt de link niet meer, begin dan opnieuw. Eenmaal aangemeld kunt u ook in **beveiliging** op **Wachtwoord wijzigen** klikken: Dastra stuurt u een e-mail met een link om het wachtwoord opnieuw in te stellen.

## De beveiliging van uw account beheren

Open het profielmenu rechtsboven, klik op **Gebruikersprofiel** en klik daarna in het linkermenu op **beveiliging**. De pagina groepeert:

* **Wachtwoord**: de knop **Wachtwoord wijzigen**;
* de sterke authenticatie, ook tweefactorauthenticatie genoemd;
* de passkeys;
* **Externe aanmeldingen**;
* **Actieve sessies**;
* uw **Historisch** (activiteitsgeschiedenis).

<figure><img src="../../.gitbook/assets/getting-started-login-5.png" alt="Pagina beveiliging met de secties wachtwoord, sterke authenticatie en passkeys"><figcaption><p>De pagina beveiliging</p></figcaption></figure>

### Sterke authenticatie inschakelen

Sterke authenticatie voegt een stap toe aan het aanmelden: een code van 6 cijfers die een authenticator-app op uw telefoon genereert.

1. Klik in **beveiliging** op **Sterke authenticatie inschakelen**.
2. Scan de QR-code met een authenticator-app (Microsoft Authenticator, Google Authenticator, 1Password enzovoort).
3. Vul de gegenereerde code in om de activering te bevestigen.
4. Bewaar de herstelcode die tijdens de activering wordt getoond.

{% hint style="warning" %}
Met de herstelcode krijgt u opnieuw toegang tot uw account als u uw authenticator-app kwijtraakt. Zonder de code moet u de eigenaar van de organisatie vragen de sterke authenticatie van uw account opnieuw in te stellen.
{% endhint %}

Zodra de sterke authenticatie is ingeschakeld, vult u uw wachtwoord in en daarna de code van 6 cijfers uit uw app.

### Actieve sessies beheren

1. Zoek in **beveiliging** de sectie **Actieve sessies**: ze toont de apparaten en browsers die met uw account zijn verbonden.
2. Klik naast de te sluiten sessie op **Verbreken**.

Sluit een sessie die u niet herkent onmiddellijk.

## Aanbevelingen voor de beveiliging

* Gebruik een lang en uniek wachtwoord voor Dastra.
* Deel uw inloggegevens nooit, ook niet intern.
* Schakel sterke authenticatie in of registreer een passkey.
* Meld u af op gedeelde of openbare apparaten.
* Controleer regelmatig uw actieve sessies.

## Zie ook

* [Uw gebruikersprofiel instellen](profile.md)
* [Meldingen](../../features/settings/notifications.md)
* [Beveiliging bij Dastra](../../security/general.md)
