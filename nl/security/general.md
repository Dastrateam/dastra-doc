---
description: >-
   Beveiliging is een integraal onderdeel van de structuur van onze Cloud-producten, -infrastructuur en -processen. infrastructuur en processen. U kunt er dus zeker van zijn dat uw gegevens beschermd zijn.
---
   
# Beveiliging bij Dastra

## Veilige cloud hosting

We besteden de hosting van de gegevens van het platform uit aan Microsoft Azure.&#x20;

Gegevens worden opgeslagen in Parijs en Marseille in Frankrijk. De gegevens worden redundant opgeslagen tussen de twee locaties.&#x20;

**Twee-factor authenticatie**

Het is voor alle organisatie-eigenaren mogelijk om het gebruik van twee-factor authenticatie af te dwingen. Authenticatie met twee factoren werkt met TOTP.
Elke gebruiker kan de functionaliteit voor authenticatie met twee factoren individueel activeren.

[Meer informatie over sterke authenticatie](mfa.md)

## Versleuteling van gegevens onderweg

Alle gegevens die tussen onze klanten en applicaties worden uitgewisseld, worden tijdens het transport versleuteld met behulp van het TLS-protocol (Transport Layer Security) met PFS (Perfect Forward Secrecy). De certificeringsautoriteit voor encryptie is CloudFlare inc.

## Encryptie van gegevens in rust

De gegevensschijven op de servers die klantgegevens hosten in de Azure-cloud zijn in rust allemaal versleuteld met behulp van "Transparante gegevensversleuteling"-technologie.

Fysieke bestanden worden ook statisch versleuteld in de Azure Storage-service met behulp van transparante 256-bits [AES-encryptie](https://en.wikipedia.org/wiki/Advanced), een van de sterkste algoritmen die voldoet aan FIPS 140-2.

## Penetratietests&#x20;

We laten onze applicatie regelmatig controleren door een onafhankelijke derde partij;

De laatste test is uitgevoerd op 25 januari 2022 en heeft geen kritieke kwetsbaarheden aan het licht gebracht.

## Organisatie Audit Logs

Organisatiebeheerders kunnen alle wijzigingen in gebruikersbeheer en toegangsrechten bijhouden.

## Unieke ID's

Elke gebruiker heeft een unieke identificatie en het gebruik van accounts die door meerdere gebruikers worden gedeeld, is niet toegestaan.

## Back-up van gegevens

Van alle gegevens (Azure SQL) en bestanden (Azure Blob Storage) van onze gebruikers wordt regelmatig een back-up gemaakt met een geschiedenis van één maand.

## Regels voor gegevensarchivering

Als een account wordt verwijderd. Gegevens worden 1 maand bewaard voordat ze definitief worden verwijderd.

## **Wachtwoordregels**

Minstens 8 tekens waaronder 3 van de 4 soorten tekens (hoofdletters, kleine letters, cijfers, speciale tekens)&#x20;

Time-out accounttoegang na meerdere mislukte pogingen.

Database wachtwoordcodering.



## Wachtwoord vernieuwingsbeleid

Met Dastra kan de accountbeheerder een wachtwoordvernieuwingsbeleid instellen voor al uw gebruikers via [de beveiligingsbeheerpagina](https://app.dastra.eu/general-settings/security).

## API token controle

Bekijk en beheer alle API tokens die gebruikt worden door ontwikkelaars in uw organisatie.

## Totale toegangscontrole

Gebruik het toegangsbeheermodel [RBAC](https://en.wikipedia.org/wiki/Role-based_access_control) (Role-base-access-control). Het hoofd van de organisatie kan de rollen en rechten van elke gebruiker kiezen.

## Beveiligde authenticatie op basis van OpenIdConnect voor al onze sites

![](<../.gitbook/assets/image (22).png>)

De authenticatie autoriteit is [https://account.dastra.eu](https://account.dastra.eu) gebruikt [IdentityServer4 ](https://identityserver.io/)technologie om al onze gebruikers te authenticeren.&#x20;

**OpenID** is een gedecentraliseerd [authenticatie systeem](https://fr.wikipedia.org/wiki/Authentification) dat [unieke authenticatie](https://fr.wikipedia.org/wiki/Authentification) en het delen van attributen mogelijk maakt. Het stelt een gebruiker in staat om zich op verschillende sites te authenticeren (die deze technologie moeten ondersteunen) zonder dat hij voor elke site een identificatiecode hoeft te onthouden, maar door telkens één OpenID-identificatiecode te gebruiken.

## IP-adres autorisatielijst

Gebruikers kunnen bij het inloggen worden gefilterd op basis van hun IP-adres.

## Machtigingslijst e-maildomein

Beheerders kunnen een witte lijst van geautoriseerde e-maildomeinen definiëren (bijv. gmail.com). Ga naar **Configuratie** => **Beveiliging** => **Domeinfilters** om deze instellingen te maken.

## Strikte isolatie tussen productie- en ontwikkelomgevingen

Afgezien van een paar geautoriseerde mensen, gebruiken of benaderen applicatieontwikkelaars nooit gegevens uit de productieomgeving. Deze isolatie is strikt en kan niet worden omzeild &#x20;

In test- of pre-productieomgevingen gebruiken we alleen testsets die we zelf hebben gemaakt.

## Regelmatige pentests

Elk jaar voeren we een penetratietest uit op de volledige perimeter van de applicatie (API Rest, Authenticatieservice, Widgets, enz.).

Onze methodologie voor beveiligingstests volgt de **OWASP** aanbevelingen en bestaat uit verschillende fasen, van het zoeken naar open source informatie (Reconnaissance) tot de exploitatie van de ontdekte kwetsbaarheden.

