---
description: Deze pagina beschrijft de implementatie van SSO binnen Dastra
---

# Single Sign On (SSO)

## Hoe het werkt

Single sign-on (SSO) is een methode die een gebruiker toegang geeft tot verschillende IT-applicaties (of beveiligde websites) door middel van één authenticatieproces.

Het bedrijf kan **eigen authenticatiesysteem** gebruiken in plaats van de lokale login die standaard door Dastra wordt voorgesteld. De meest gebruikte SSO-systemen zijn Microsoft Active Directory, Google Workspace (voorheen GSuite), Auth0, enz.

**Het werkt als volgt:**&#x20;

Een gebruiker (**User Agent**) vraagt een verbinding aan met de serviceprovider (**Service Provider**), die een identiteitsaanbieder (**Identity Provider**) vraagt om de gebruiker te authenticeren. Deze authenticatie wordt dan teruggestuurd naar de dienstverlener, die het verbindingsverzoek van de gebruiker accepteert &#x20;

In ons geval is de User Agent de **browser van een Dastra-gebruiker**. De Service Provider is **Dastra** en de Identity Provider is uw **gunstige authenticatie provider** (bijvoorbeeld: Active Directory).  &#x20;



![Hoe SSO werkt met het SAML 2 protocol](<../../../.gitbook/assets/image (115).png>)

## Implementatie

Binnen een Dastra abonnement heb je de mogelijkheid, als je geabonneerd bent op de functionaliteit, om één of meer SSO aanmeldingen te beheren. Om toegang te krijgen tot de SSO-configuratie, gaat u naar [de SSO logins configuratiepagina](https://app.dastra.eu/general-settings/sso) op het tabblad beveiliging van het configuratiepaneel van de abonnementsaccount.

{% hint style="info" %}
**Waarschuwing**: u moet de eigenaar van de organisatie zijn om toegang te krijgen tot deze pagina.
{% endhint %}

Dastra biedt twee eenmalige aanmeldprotocollen, [**SAML 2**](saml-2.md) en [**Open ID**](openid.md). Klik op de onderstaande koppelingen om de configuratiehulp te openen.&#x20;

{% content-ref url="saml-2.md" %}
[saml-2.md](saml-2.md)
{% endcontent-ref %}

{% content-ref url="openid.md" %}
[openid.md](openid.md)
{% endcontent-ref %}

{% content-ref url="adfs.md" %}
[adfs.md](adfs.md)
{% endcontent-ref %}

## Hoe schakel ik automatische gebruikers provisioning in?

Als u niet wilt dat de gebruikers van uw identity provider accounts moeten aanmaken om toegang te krijgen tot de entiteit, kunt u het vakje "automatic user provisioning" aanvinken. Als je je gebruikers voorziet van een SSO provider url zoals deze: https://account.dastra.eu/account/loginexternal?provider={id van je provider}&returnUrl=https://www.dastra.eu&#x20;

\=> zullen ze in het geval van een gevalideerde authenticatie automatisch een account aanmaken in Dastra.

{% hint style="warning" %}
Als het account van de gebruiker verwijderd of ongeldig gemaakt wordt in de authenticatie provider, zal hun account niet verwijderd worden in Dastra, maar ze zullen niet langer verbinding kunnen maken. U kunt hun accounts verwijderen [via de gebruikersbeheerder voor abonnementen](https://app.dastra.eu/general-settings/users)
{% endhint %}

U kunt **de rol kiezen die standaard** wordt toegewezen aan alle organisaties die zijn gekoppeld aan uw abonnement.

![](<../../../.gitbook/assets/image (124).png>)

{% hint style="info" %}
Dastra ondersteunt momenteel geen rolbinding via authenticatieserver eigenschappen. Als deze functie belangrijk is, laat het ons dan weten via de [ondersteuningspagina](https://app.dastra.eu/general-settings/support).
{% endhint %}



### Teams binden

Het is mogelijk om teams in een werkruimte te binden aan een eigenschap (Claim) die wordt geretourneerd door je authenticatieservers.

<figure><img src="../../..gitbook/assets/image (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>



## Hoe beheer ik gebruikerslogins?

U kunt het type gebruikersaanmelding configureren door naar [de gebruikersbeheerpagina voor abonnementen] (https://app.dastra.eu/general-settings/users) te gaan. Door naar een gebruikersprofiel te gaan, kunt u de gewenste SSO login kiezen. Gebruikers die verbinding maken met Dastra met hun e-mailadres worden automatisch doorgestuurd naar de inlogpagina van de authenticatie provider die u heeft ingesteld.

![](<../../..gitbook/assets/image (118).png>)

Je kunt ook het login type instellen bij het uitnodigen van nieuwe gebruikers.