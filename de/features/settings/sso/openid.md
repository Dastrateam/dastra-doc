---
description: Konfiguration einer SSO-Verbindung mit dem OpenId-Protokoll
---

# OpenId

## Funktionsprinzip

Die Spezifikationen von OpenId finden Sie [hier](https://openid.net/connect/)

![](<../../../.gitbook/assets/image-119.png>)

Die Konfiguration des SSO mit OpenID erfolgt in drei Schritten&#x20;

* Konfiguration des Authentifizierungsanbieters: Active Directory, Google Workspace...
* Konfiguration des Dienstanbieters: Dastra
* Tests der Authentifizierung

## 1. Konfiguration des Authentifizierungsanbieters

Sie müssen eine OpenId-Konfiguration in Ihrem Authentifizierungsanbieter einrichten.

Für Active Directory: [https://docs.microsoft.com/fr-fr/azure/active-directory/develop/v2-protocols-oidc](https://docs.microsoft.com/fr-fr/azure/active-directory/develop/v2-protocols-oidc)

Um den Abgleich zwischen den lokalen Konten (die in Dastra gehostet werden) herzustellen, müssen Sie eine Eigenschaft angeben, die die E-Mail des Nutzers enthält (standardmäßig sucht Dastra die Eigenschaft mit dem Namen [http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress)).

Hier sind die Informationen, die Sie zur Konfiguration des Service Providers benötigen:&#x20;

* **Authority/domain (z. B.: https://account.oauth.sso.com)**
* **Client-ID: ClientId**&#x20;
* **Secret key (optional)**
* **Response Type, standardmäßig id\_token**
* **Scope: standardmäßig „openid profile email"**

Zur Konfiguration Ihres Authentifizierungsanbieters benötigen Sie die folgenden Informationen:

* **Die bereitgestellte Redirect URI in diesem Format: https://account.dastra.eu/signin-{schemeId}**

## 2. Konfiguration des Dienstanbieters

Gehen Sie in dastra.eu auf [die SSO-Administrationsseite](https://app.dastra.eu/general-settings/sso) und klicken Sie auf „SSO-Login hinzufügen"

![](<../../../.gitbook/assets/image-116.png>)

Füllen Sie die Formularfelder mithilfe der Konfigurationsinformationen der Entität aus&#x20;

<figure><img src="../../../.gitbook/assets/image-2.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Ab dem **30.03.2026** wird Dastra die Authentifizierung über das JWT-Private-Key-System autorisieren. Sie müssen dann keinen geheimen Schlüssel mehr in Ihrer SSO-Konfiguration angeben. Dastra wird automatisch die öffentlichen Schlüssel abrufen, um die JWT mit privatem Schlüssel zu generieren.\
Wählen Sie dazu die zweite Option „JWT private key" im Formular.
{% endhint %}

{% hint style="danger" %}
Es ist möglich, alle Nutzer des Abonnementkontos zur Verwendung eines bestimmten SSO zu zwingen (durch Aktivieren des Kontrollkästchens „Nutzer zur Verwendung dieses SSO zwingen"). Vor der Aktivierung dieser Option ist Vorsicht geboten. Denn wenn das SSO nicht funktioniert, können Sie nicht mehr als Administrator auf Ihr Konto zugreifen. Es ist vorzuziehen, das SSO pro Nutzer zu verwalten.
{% endhint %}

{% hint style="warning" %}
**Sonderfälle externer Nutzer**\
Nur interne Konten eines Abonnements unterliegen dem SSO. Konten externer Nutzer (die ein anderes zusätzliches Abonnement haben) unterliegen nicht dem SSO.
{% endhint %}

## 3. SSO mit OpenId testen

Sobald die Konfiguration abgeschlossen ist, können Sie die Authentifizierung testen, indem Sie unten rechts auf die Schaltfläche „Testen" klicken. Wenn Sie bei der SSO-Konfiguration auf ein Problem stoßen, wenden Sie sich bitte an den Support, indem Sie die Seite zur [Verwaltung von Support-Tickets](https://app.dastra.eu/general-settings/support) aufrufen.

![](<../../../.gitbook/assets/image-122.png>)
