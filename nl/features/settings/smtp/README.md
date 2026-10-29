---
description: >-
  Verstuur de notificatiemails van Dastra via uw eigen e-mailserver.
---

# SMTP-configuratie

Deze pagina legt uit hoe u de e-mails van Dastra via uw eigen SMTP-server laat lopen. Ze is bedoeld voor eigenaren van de organisatie.

## Werking

Standaard verstuurt Dastra zijn e-mails met zijn eigen SMTP-service. Dat geldt voor:

* [meldingen](../notifications.md) in realtime (nieuwe opmerkingen, taken enzovoort);
* e-mailwisselingen binnen een [verzoek van een betrokkene](../../requests/README.md);
* uitnodigingen aan respondenten van [vragenlijsten](../../questionnaires/README.md);
* [uitnodigingen](../../../getting-started/setup/users.md) van nieuwe gebruikers.

Zodra uw server is geconfigureerd, lopen al deze e-mails erlangs, voor elke werkruimte van de organisatie.

{% hint style="warning" %}
Het aanpassen van SMTP kan het platform onstabiel maken. Doe dit alleen als u zeker weet dat uw e-mailverzendservice goed werkt en betrouwbaar aflevert.
{% endhint %}

## Waarom SMTP aanpassen

Dastra zorgt voor de beschikbaarheid en de beveiliging van transactionele e-mails. Afhankelijk van uw intern beveiligingsbeleid kan het toch nodig zijn dat u de routering van deze e-mails zelf beheert om uw mailstromen te sturen.

## Toegang en vereisten

De pagina staat onder **Organisatie-instellingen** > **Aangepaste SMTP**. Ze is voorbehouden aan eigenaren van de organisatie en aan het Enterprise-abonnement (geavanceerde beveiligingsfunctie).

U hebt twee mogelijkheden:

* een leverancier koppelen (**Outlook (MS Office 365)** of **Gmail (Google workspace)**): zie [Integratie van externe providers](office-365-gmail.md);
* de instellingen van uw eigen SMTP-server invoeren, zoals hieronder beschreven.

Houd voor een SMTP-server het volgende bij de hand:

* de naam van de SMTP-server (bijvoorbeeld `smtp.uwdienst.com`);
* de poort van de SMTP-server (standaard 25);
* de gebruikersnaam en het wachtwoord van de server;
* een geldig e-mailadres van de afzender (bijvoorbeeld `noreply@uwdienst.com`): uw SMTP-provider moet het hebben gevalideerd;
* een alias van de afzender, dat wil zeggen de naam die als afzender wordt weergegeven (bijvoorbeeld `Compliance-team`).

{% hint style="warning" %}
Dastra vereist een beveiligde verbinding via TLS, minimaal versie 1.2. Uw SMTP-server moet dit ondersteunen.
{% endhint %}

## Configuratie

1. Open de [SMTP-configuratiepagina](https://app.dastra.eu/general-settings/smtp).
2. Vul in de sectie **SMTP Persoonlijk** de velden **SMTP-servernaam (TLS vereist)**, **SMTP-serverpoort**, **Gebruikersnaam van SMTP-server**, **Wachtwoord SMTP-server**, **e-mail van de afzender** en **Naam van afzender** in.
3. Klik op **Opslaan**.

<figure><img src="../../../.gitbook/assets/settings-smtp-config-form.png" alt="Configuratieformulier van de SMTP-server met de velden server, poort, gebruikersnaam, wachtwoord, e-mail van de afzender en alias van de afzender"><figcaption><p>Het configuratieformulier van de SMTP-server</p></figcaption></figure>

Bij het opslaan maakt Dastra verbinding met uw server en stuurt een testbericht naar het e-mailadres van uw account. Mislukt de verbinding, dan wordt de configuratie niet opgeslagen en verschijnt de foutmelding van de server.

Zolang een leverancier is gekoppeld, is het formulier voor aangepaste SMTP uitgeschakeld. Klik eerst op **Verwijder de integratie** om uw eigen server te gebruiken.

## Testen

Zodra de configuratie is opgeslagen, verschijnt de knop **Testen**. Klik erop en bevestig: Dastra stuurt een testbericht naar het e-mailadres van uw persoonlijke account.

U kunt ook controleren of de notificatiemails van uw server komen. Voeg bijvoorbeeld een opmerking toe aan een verwerkingsactiviteit en kijk of de melding in uw mailbox aankomt.

* U ontvangt geen e-mail: ofwel is de melding niet geactiveerd, ofwel is er een probleem met uw SMTP-configuratie.
* U ontvangt wel een e-mail: controleer of uw SMTP-server en uw afzender in de details van het bericht staan.

{% hint style="info" %}
[E-maildetails bekijken in Gmail](https://support.google.com/mail/answer/29436).

[E-maildetails bekijken in Outlook](https://support.microsoft.com/en-us/office/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c)
{% endhint %}
