---
description: Deze pagina legt uit hoe je API-sleutels aanmaakt in Dastr
---

# API-sleutelbeheer

### Waar worden API-sleutels voor gebruikt?

* Maak een Dastra API** client om data op te halen of te wijzigen buiten de applicatie. Deze client kan server-to-server (Client credential) of javascript (Autorisatie code) zijn. Voor meer informatie kunt u [de Dastra API authenticatie documentatie lezen](../../api-references/authentification.md).
* Een widget voor het uitoefenen van rechten** configureren (alleen openbare sleutel). [Lees de documentatie over het instellen van de widget voor het uitoefenen van rechten](broken-reference).
* Een cookie toestemmingswidget** configureren (alleen openbare sleutel). [Lees de documentatie over het instellen van de cookie toestemmingswidget](../gerer-le-consentement-aux-cookies/)

### Hoe maak ik een API-sleutel aan?

1. [Krijg toegang tot de Dastra sleutelbeheerder](https://app.dastra.eu/general-settings/api) (Alleen accounteigenaren hebben toegang tot dit gedeelte)
2. Klik op "**maak een API-sleutel**".
3. Voer de naam van de sleutel en de redirection en cors urls in (als u de API in javascript wilt gebruiken in OAuth2)
4. Klik op "**registreer**".
5. Zodra uw API-sleutel is aangemaakt, kunt u deze rechtstreeks uit de manager kopiëren en plakken (private of public key)

{% hint style="warning" %}
**Veilig uw API-sleutels! Onder geen enkele omstandigheid mag de privésleutel openbaar worden gemaakt!

**Als de veiligheid van je API sleutel in gevaar komt**, kun je deze verwijderen uit de manager en een nieuwe genereren.
{% endhint %}