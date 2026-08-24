---
description: Details zur Konfiguration von SAML 2
---

# SAML 2

Die Konfiguration des SSO mit SAML 2 erfolgt in drei Schritten

* Konfiguration des Authentifizierungsanbieters (**Identity Provider - IdP**): Active Directory, Google Workspace...
* Konfiguration des Dienstanbieters (**Service Provider - SP**): Dastra
* Tests der Authentifizierung

Im spezifischen Fall **von ADFS-Servern** konsultieren Sie unsere spezielle Dokumentation:

{% content-ref url="adfs.md" %}
[adfs.md](adfs.md)
{% endcontent-ref %}

## 1. Konfiguration des Authentifizierungsanbieters

Sie müssen eine SAML-Konfiguration in Ihrem Authentifizierungsanbieter einrichten.

Für AD FS: [https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings](https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings)

Für Azure AD: [https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings-azure-ad](https://docs.microsoft.com/fr-fr/powerapps/maker/portals/configure/configure-saml2-settings-azure-ad)

Für Google: [https://support.google.com/a/answer/6087519?hl=fr](https://support.google.com/a/answer/6087519?hl=fr)

Um den Abgleich zwischen den lokalen Konten (die in Dastra gehostet werden) herzustellen, müssen Sie eine Eigenschaft angeben, die die E-Mail des Nutzers enthält (standardmäßig sucht Dastra die Eigenschaft mit dem Namen [http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress)).

Hier sind die Informationen, die Sie zur Konfiguration des Service Providers benötigen:

* **Identity Provider's Entity id** (issuer)
* **Single sign on url**
* **Das Zertifikat im RAW-Format** (Base64-codiert)

Zur Konfiguration Ihres Authentifizierungsanbieters benötigen Sie die folgenden Informationen:

* **Issuer**: standardmäßig „https://www.dastra.eu"
* **SP Redirect URI**: standardmäßig [https://account.dastra.eu/Saml2/Acs](https://localhost:44375/Saml2/Acs)

## 2. Konfiguration des Dienstanbieters

Gehen Sie in dastra.eu auf [die SSO-Administrationsseite](https://app.dastra.eu/general-settings/sso) und klicken Sie auf „SSO-Login hinzufügen"

![](<../../../.gitbook/assets/image-116.png>)

Füllen Sie die Formularfelder mithilfe der Konfigurationsinformationen der Entität aus:

![](<../../../.gitbook/assets/image-117.png>)

{% hint style="danger" %}
Es ist möglich, alle Nutzer des Abonnementkontos zur Verwendung eines bestimmten SSO zu zwingen (durch Aktivieren des Kontrollkästchens „Nutzer zur Verwendung dieses SSO zwingen"). Vor der Aktivierung dieser Option ist Vorsicht geboten. Denn wenn das SSO nicht funktioniert, können Sie nicht mehr als Administrator auf Ihr Konto zugreifen. Es ist vorzuziehen, das SSO pro Nutzer zu verwalten.
{% endhint %}

{% hint style="warning" %}
**Sonderfälle externer Nutzer**\
Nur interne Konten eines Abonnements unterliegen dem SSO. Konten externer Nutzer (die ein anderes zusätzliches Abonnement haben) unterliegen nicht dem SSO.
{% endhint %}

## 3. SSO testen

Sobald die Konfiguration abgeschlossen ist, können Sie die Authentifizierung testen, indem Sie unten rechts auf die Schaltfläche „Testen" klicken. Wenn Sie bei der SSO-Konfiguration auf ein Problem stoßen, wenden Sie sich bitte an den Support, indem Sie die Seite zur [Verwaltung von Support-Tickets](https://app.dastra.eu/general-settings/support) aufrufen.

![](<../../../.gitbook/assets/image-120.png>)
