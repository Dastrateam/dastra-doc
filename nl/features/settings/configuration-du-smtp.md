---
description: >-
  Met Dastra kunt u uw notificatiemails routeren via uw eigen
  e-mailserver
---

# SMTP-configuratie

## Hoe het werkt

Standaard routeert Dastra een groot aantal e-mailmeldingen voor de volgende diensten:&#x20;

* [Meldingen](notifications.md) in realtime (nieuwe opmerkingen, taken, enz.)
* E-mails voor uitwisselingen als onderdeel van [een verzoek om rechten uit te oefenen](../gerer-les-exercices-des-droits/)
* Uitnodigingen voor [audits](../audit/) voor respondenten
* [Uitnodigingen](../../commencer/commencer/inviter-utilisateurs.md) voor nieuwe gebruikers

Standaard gebruikt Dastra zijn eigen SMTP-service.

## Hoe configureer je je SMTP verzendserver?

{% hint style="warning" %}
Waarschuwing! Het aanpassen van SMTP kan leiden tot instabiliteit van het platform. Voer deze handeling alleen uit als u zeker weet dat uw e-mailverzendservice goed werkt en afgeleverd kan worden.
{% endhint %}

### Waarom SMTP aanpassen?

Dastra stelt alles in het werk om maximale beschikbaarheid en veiligheid voor transactie-e-mails te garanderen &#x20;

Afhankelijk van uw interne beveiligingsbeleid kan het echter nodig zijn om de routering van transactie-e-mails te internaliseren om de berichtenstromen te controleren.

### Vereisten

U hebt de volgende SMTP-serverconfiguratie-elementen nodig:&#x20;

* SMTP host (bijv. smtp.yourservice.com)
* SMTP-poort (gebruik standaard poort 25)
* Gebruikersnaam
* Wachtwoord
* Een **geldig e-mailadres van de afzender** (bijv. noreply@yourservice.com): dit adres moet correct worden gevalideerd door uw SMTP-provider.

{% hint style="warning" %}
Uw SMTP-server moet een beveiligde verbinding met SSL ondersteunen.
{% endhint %}

### Configuratie

Ga naar de [SMTP server configuratiepagina](https://app.dastra.eu/general-settings/smtp)

Vul de formuliervelden in met de gegevens die worden gevraagd in [prerequisites](configuration-du-smtp.md#prerequisites)

![](<../../.gitbook/assets/image (249) (1).png>)

Merk op dat de server connectiviteit automatisch getest wordt om er zeker van te zijn dat de server login gegevens correct zijn. Een test e-mail wordt automatisch verzonden vanaf onze servers.

### Tests

Zodra je het formulier hebt gevalideerd, zou je SMTP-server moeten werken.

U kunt controleren of de notificatiemails van uw SMTP-server komen. Om dit te doen, maakt u bijvoorbeeld een opmerking in een behandeling en controleert u of u de notificatie-e-mail in uw mailbox ontvangt.

* Als je geen e-mail ontvangt**: ofwel is het je niet gelukt om de melding te triggeren, ofwel is er een probleem met je SMTP-configuratie.
* Als u wel een e-mail ontvangt**: controleer of uw SMTP en afzender worden weergegeven in de e-maildetails &#x20;

{% hint style="info" %}
[Hoe de e-maildetails in GMAIL te bekijken](https://support.google.com/mail/answer/29436?hl=fr).&#x20;

[Hoe de e-maildetails in Outlook te bekijken](https://support.microsoft.com/fr-fr/office/afficher-les-en-t%C3%AAtes-de-message-internet-dans-outlook-cd039382-dc6e-4264-ac74-c048563d212c)
{% endhint %}