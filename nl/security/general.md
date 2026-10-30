---
description: >-
  Hosting, versleuteling, authenticatie, toegangsbeheer en back-ups: de
  beveiligingsmaatregelen die Dastra toepast om uw gegevens te beschermen.
---

# Beveiliging bij Dastra

Deze pagina beschrijft de beveiligingsmaatregelen die Dastra toepast om uw gegevens te beschermen: hosting, versleuteling, authenticatie, toegangsbeheer en back-ups.

{% hint style="info" %}
De beveiligingsinstellingen van de organisatie (verplichte sterke authenticatie, filtering op IP-adres, filtering op e-maildomein, beleid voor wachtwoordvernieuwing, automatisch afmelden, bewaartermijn van beveiligingslogs, SIEM-streaming) zijn voorbehouden aan organisatie-eigenaren en aan het Enterprise-abonnement. U vindt ze onder **Organisatie-instellingen** > **Beveiliging**. Voor elke instelling, zie [Beveiliging van de organisatie en beveiligingslogboeken](../features/settings/security-center.md).
{% endhint %}

## Veilige cloudhosting

Wij besteden de hosting van de gegevens van het platform uit aan Microsoft Azure. Wij hebben dit platform gekozen omdat de meeste van onze klanten het al gebruiken (Microsoft 365 enz.) en omdat het een beveiligingsniveau biedt dat [tot de hoogste op de markt behoort](https://learn.microsoft.com/en-us/azure/compliance/).

Gegevens worden in Frankrijk opgeslagen: in Parijs voor de productiegegevens en in Marseille voor de back-ups. De gegevens worden ook gerepliceerd in het datacenter van Amsterdam voor redundantie.

Voor een dedicated instantie op een soevereine cloud, zie [Dastra op Bleu](bleu.md).

## Tweefactorauthenticatie

Tweefactorauthenticatie werkt met het TOTP-protocol.

Elke gebruiker kan tweefactorauthenticatie inschakelen voor zijn eigen account. Organisatie-eigenaren kunnen het ook verplicht stellen voor alle interne gebruikers die door de organisatie worden beheerd.

Zie [Sterke authenticatie](mfa.md).

## Single sign-on (SSO) en SCIM

Afhankelijk van het gekozen abonnement, of als optie, biedt Dastra [self-service SSO](../features/settings/sso/README.md). Wij ondersteunen de protocollen SAML2P en OpenID, die compatibel zijn met de meeste bedrijfsdirectory's. U kunt ook de gebruikers van uw directory automatisch laten aanmaken met onze [SCIM](../features/settings/scim.md)-server.

## Versleuteling van gegevens onderweg

Alle gegevens die tussen onze klanten en applicaties worden uitgewisseld, worden tijdens het transport versleuteld met het TLS-protocol (Transport Layer Security) met PFS (Perfect Forward Secrecy). De certificeringsautoriteit is Cloudflare, Inc.

## Versleuteling van gegevens in rust

De gegevensschijven van de servers die klantgegevens hosten in de Azure-cloud zijn in rust versleuteld met [Transparent Data Encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver16).

Bestanden worden ook in rust versleuteld in de Azure Storage-service, met transparante 256-bits [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)-versleuteling die voldoet aan FIPS 140-2.

Alle versleutelingssleutels worden bewaard in een door Dastra beheerde sleutelkluis, met automatische rotatie.

## Penetratietests (pentests)

Wij laten de beveiliging van de applicatie elk jaar controleren door een onafhankelijke derde partij.

De laatste test heeft geen kritieke kwetsbaarheid aan het licht gebracht.

Onze testmethodologie volgt de aanbevelingen van **OWASP** en bestaat uit verschillende fasen, van het zoeken naar open-sourceinformatie (reconnaissance) tot de exploitatie van de ontdekte kwetsbaarheden.

## Beveiligingsauditlogs

Organisatiebeheerders kunnen alle wijzigingen in gebruikersbeheer, werkruimten en toegangsmachtigingen bijhouden.

Organisatie-eigenaren bepalen hoelang beveiligingslogs worden bewaard onder **Organisatie-instellingen** > **Beveiliging**, in het blok **Veiligheidslogboeken bijhouden**: van 30 dagen tot 3 jaar (180 dagen aanbevolen). Logs die ouder zijn dan deze periode worden elke nacht verwijderd.

Om deze gebeurtenissen continu naar uw monitoringtool te streamen, zie [SIEM-streaming](../features/settings/siem.md).

## Unieke identificatiecodes

Elke gebruiker heeft een unieke identificatiecode. Accounts die door meerdere gebruikers worden gedeeld, zijn niet toegestaan.

## Back-up van gegevens

Van alle gegevens (Azure SQL) en bestanden (Azure Blob Storage) van onze gebruikers wordt regelmatig een back-up gemaakt, met een geschiedenis van 3 maanden (langetermijnretentie) en een herstel naar een bepaald tijdstip (PITR) over 7 dagen.

## Regels voor gegevensarchivering

Als een account wordt verwijderd, worden de gegevens 1 maand bewaard voordat ze definitief worden verwijderd.

## Wachtwoordbeleid

* Minstens **10 tekens**, met **4 soorten tekens**: hoofdletters, kleine letters, cijfers en speciale tekens.
* Vertraging bij de toegang tot het account na meerdere mislukte aanmeldpogingen.
* Versleuteling van wachtwoorden in de database.

## Beleid voor wachtwoordvernieuwing

Organisatie-eigenaren kunnen een levensduur voor wachtwoorden instellen onder [Organisatie-instellingen > Beveiliging](https://app.dastra.eu/general-settings/security), in het blok **Beleid voor wachtwoordverlenging**. Dit geldt voor de interne gebruikers van de organisatie die geen SSO gebruiken. Wanneer de periode verstrijkt, maakt de gebruiker bij de volgende aanmelding een nieuw wachtwoord aan.

## Automatisch afmelden

Organisatie-eigenaren kunnen het blok **Automatisch verbinding verbreken** inschakelen: alle interne gebruikers die door de organisatie worden beheerd, worden dan na 1 uur inactiviteit afgemeld.

## Controle van API-tokens

Bekijk en beheer alle [API-sleutels](../features/settings/api-keys.md) die de ontwikkelaars van uw organisatie gebruiken. U kunt het bereik van een sleutel ook beperken tot één werkruimte en tot specifieke machtigingen.

## Toegangsbeheer

Dastra gebruikt het toegangsbeheermodel [RBAC](https://en.wikipedia.org/wiki/Role-based_access_control) (Role-Based Access Control). De organisatie-eigenaar kiest de [rollen en machtigingen](../features/settings/roles.md) van elke gebruiker met fijne granulariteit.

## Beveiligde authenticatie op basis van OpenID Connect voor al onze sites

De authenticatieautoriteit is [https://account.dastra.eu](https://account.dastra.eu). Zij gebruikt OpenID om al onze gebruikers te authenticeren.

**OpenID** is een gedecentraliseerd [authenticatiesysteem](https://en.wikipedia.org/wiki/Authentication) dat [eenmalige aanmelding](https://en.wikipedia.org/wiki/Single_sign-on) en het delen van attributen mogelijk maakt. Het stelt een gebruiker in staat om zich op verschillende sites die deze technologie ondersteunen te authenticeren met één OpenID-identificatiecode, zonder voor elke site een aparte identificatiecode te hoeven onthouden.

## IP-adres autorisatielijst

De toegang tot de organisatie kan worden beperkt tot toegestane IP-adresbereiken. De filtering geldt voor alle gebruikers (beheerders inbegrepen) en alle inlogmethoden (wachtwoord, SSO, passkey, magische link), bij het inloggen en bij elke vernieuwing van het token. Ze geldt niet voor API's, SCIM of SIEM-streaming.

Dastra controleert of uw eigen IP-adres tot de toegestane bereiken behoort. Controleer uw bereiken zorgvuldig voordat u ze opslaat: een regel kan niet via de interface worden verwijderd. Zie de pagina [IP-filtering](../features/settings/ip-filtering.md) voor details.

## Machtigingslijst e-maildomein

Organisatie-eigenaren kunnen de lijst van toegestane e-maildomeinen bepalen (bijvoorbeeld `example.com`): alleen gebruikers van wie het e-mailadres tot een van deze domeinen behoort, kunnen zich aanmelden. Ga naar **Organisatie-instellingen** > **Beveiliging**, blok **Filter de e-maildomeinen van je gebruikers**. Het kan enkele minuten duren voordat de configuratie van kracht wordt.

## Strikte isolatie tussen productie- en ontwikkelomgevingen

Afgezien van een paar geautoriseerde mensen, gebruiken of benaderen applicatieontwikkelaars nooit gegevens uit de productieomgeving. Deze isolatie is strikt en kan niet worden omzeild.

In test- en pre-productieomgevingen gebruiken we alleen testgegevenssets die we zelf hebben gemaakt.
