---
description: >-
  Beperk het inloggen bij Dastra tot toegestane IP-adresbereiken: bereik,
  werking, blokkering en aandachtspunten.
---

# IP-filtering

Met IP-filtering beperkt u de toegang tot uw Dastra-organisatie tot een lijst met toegestane IP-adresbereiken (bijvoorbeeld die van uw kantoren of uw bedrijfs-VPN). U configureert dit onder **Configuratie** > **Beveiliging**.

{% hint style="info" %}
Deze functie is voorbehouden aan het Enterprise-abonnement of een betaalde optie. Neem contact op met uw Dastra-contactpersoon om ze te activeren.
{% endhint %}

{% hint style="danger" %}
Een waarschuwing meldt: "Deze actie is niet omkeerbaar". In de praktijk kan een filterregel niet via de interface worden verwijderd of uitgeschakeld: **alleen het beheerteam van Dastra** kan ze verwijderen. Controleer uw bereiken zorgvuldig voordat u ze opslaat, anders kunt u uzelf buitensluiten.
{% endhint %}

## Regels definiëren

* De regels gelden voor de **hele organisatie** (niet voor één specifieke werkruimte).
* Elke regel is een bereik met een **beginadres** en een **eindadres**. CIDR-notatie (bv. `10.0.0.0/24`) wordt niet ondersteund: zet uw netwerken om in begin- en eindadressen.
* **IPv4- en IPv6**-adressen worden geaccepteerd.
* Er is geen limiet op het aantal regels.

## Wie wordt getroffen?

De filtering geldt voor **alle gebruikers van de organisatie, beheerders inbegrepen**. Er is geen uitzondering voor beheerders en geen uitzonderingenlijst.

Ze geldt voor alle inlogmethoden, omdat de controle na de authenticatie plaatsvindt:

* gebruikersnaam en wachtwoord;
* SSO (SAML 2, OpenID, ADFS, Entra, Okta);
* passkey;
* magische link of uitnodiging per e-mail.

Lokale serviceaccounts die van SSO zijn vrijgesteld, zijn **niet** vrijgesteld van IP-filtering.

## Wanneer vindt de controle plaats?

Het IP-adres wordt gecontroleerd bij het inloggen en bij elke **vernieuwing van het token**. Een reeds geopende sessie wordt dus niet onmiddellijk beëindigd als de gebruiker van netwerk wisselt (bv. van kantoor naar thuiswerk): ze eindigt bij de volgende vernieuwing van het token.

Geldigheidsduur van de tokens:

| Type sessie | Geldigheid van het token |
|---|---|
| Webapplicatie | 6 minuten (automatisch vernieuwd) |
| Standaardsessie | 1 uur |
| "Onthoud mij" | 30 dagen |

## Welk IP-adres wordt gebruikt?

Dastra gebruikt het openbare IP-adres dat zijn toegangsinfrastructuur ziet (de laag die uw verzoek ontvangt vóór de applicatie). Een gebruiker die via een VPN of bedrijfsproxy gaat, wordt dus gefilterd op het **uitgangsadres** van de VPN of proxy: dit adres moet u toestaan.

## Wat een geblokkeerde gebruiker ziet

De gebruiker wordt doorgestuurd naar een foutpagina met de melding:

> IP Address not allowed — Your IP address is not allowed by your organization. Please contact your account's administrator.

{% hint style="warning" %}
Blokkeringen worden **niet** vastgelegd in het auditlogboek en niet naar [SIEM-streaming](siem.md) gestuurd.
{% endhint %}

## Wat de filtering niet dekt

| Toegang | Gefilterd? |
|---|---|
| API-aanroepen met een [API-sleutel](api-keys.md) | Nee |
| [SCIM](scim.md) | Nee |
| [SIEM-streaming](siem.md) en BI-connectoren | Nee |
| Externe respondenten van vragenlijsten (openbare link) | Nee |
| Portaal voor rechtenverzoeken en Trust Center | Nee, ze hebben hun eigen instellingen (zie [Trust Center - Beveiliging](../trust-center/configuration/security.md)) |

## Dastra-support

Ook de Dastra-support valt onder de filtering: ze heeft vanaf een niet-toegestaan adres geen toegang meer tot uw account (impersonatie). Neem contact op met de Dastra-support om een regel te verwijderen of uit te schakelen.
