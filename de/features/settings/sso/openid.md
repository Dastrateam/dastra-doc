---
description: >-
  Konfiguration einer SSO-Verbindung mit dem Protokoll OpenId, mit einem
  geheimen Schlüssel oder einem privaten JWT-Schlüssel.
---

# OpenId

## Funktionsprinzip

Die Spezifikationen von OpenId finden Sie [hier](https://openid.net/connect/).

<figure><img src="../../../.gitbook/assets/openid1.png" alt="Ablauf des OpenID-Connect-Autorisierungscodes zwischen der Relying Party, dem OpenID-Anbieter, dem Token-Endpunkt und dem UserInfo-Endpunkt"><figcaption></figcaption></figure>

Die Einrichtung des SSO mit OpenId umfasst drei Schritte:

* den Authentifizierungsanbieter konfigurieren: Active Directory, Google Workspace usw.;
* den Dienstanbieter konfigurieren: Dastra;
* die Authentifizierung testen.

## 1. Den Authentifizierungsanbieter konfigurieren

Richten Sie bei Ihrem Authentifizierungsanbieter eine OpenId-Konfiguration ein.

Für Active Directory: [https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc)

Um die lokalen Konten (die in Dastra gehosteten) mit den Konten Ihres Anbieters zu verknüpfen, benötigt Dastra eine Eigenschaft, die die E-Mail-Adresse des Nutzers enthält. Das Feld **Der Name des Anspruchs, der die E-Mail-Adresse enthält** in Schritt 2 ist mit `email` vorausgefüllt. Fehlt dieser Claim, sucht Dastra auch nach der Eigenschaft mit dem Namen [http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress).

Diese Informationen benötigen Sie, um den Dienstanbieter auszufüllen:

* **Behörde/Domäne**, zum Beispiel `https://account.oauth.sso.com`;
* **Kunden-ID (ClientId)**;
* **Geheimer Schlüssel** oder die Elemente des privaten JWT-Schlüssels (siehe die Methode zur Client-Authentifizierung in Schritt 2);
* **Art der Antwort**, standardmäßig `id_token`;
* **Geltungsbereich**, standardmäßig `openid profile email`.

Um Ihren Authentifizierungsanbieter zu konfigurieren, benötigen Sie die im Dastra-Formular angezeigte **Weiterleitungs-URL** im Format `https://account.dastra.eu/signin-{connection identifier}`. Diese URL ist für jede Verbindung spezifisch.

## 2. Den Dienstanbieter konfigurieren

Öffnen Sie in Dastra die [Administrationsseite des SSO](https://app.dastra.eu/general-settings/sso) (**Konfiguration der Organisation** > **Einmalige Anmeldung**, nur für Inhaber der Organisation verfügbar) und klicken Sie auf **SSO-Login hinzufügen**. Wählen Sie das Protokoll **OpenID**.

<figure><img src="../../../.gitbook/assets/settings-sso-liste-logins.png" alt="Die Seite Einmalige Anmeldung mit der Liste der SSO-Anmeldungen und der Schaltfläche SSO-Login hinzufügen"><figcaption></figcaption></figure>

Füllen Sie die Formularfelder mit den Informationen Ihres Authentifizierungsanbieters aus:

<figure><img src="../../../.gitbook/assets/settings-sso-openid-config-modal.png" alt="Das Formular der OpenID-SSO-Anmeldung in Dastra"><figcaption></figcaption></figure>

Das Formular zeigt außerdem die Werte an, die Sie bei Ihrem Authentifizierungsanbieter hinterlegen müssen:

* **Weiterleitungs-URL**;
* **URL zum Abmelden (Back-Channel-Logout-URL)**, optional;
* **JSON-URI für öffentlichen Schlüssel (JWK-Privatschlüssel)**, nur beim privaten JWT-Schlüssel. Speichern Sie das Formular einmal, damit dieser Endpunkt funktioniert.

Tragen Sie die **URL zum Abmelden (Back-Channel-Logout-URL)** bei Ihrem Anbieter ein, wenn eine Abmeldung beim Anbieter auch die Dastra-Sitzung beenden soll. Dastra unterstützt OpenID Connect Back-Channel Logout: Sendet Ihr Anbieter ein Logout-Token für einen Nutzer oder eine Sitzung, widerruft Dastra die entsprechenden Sitzungen, sodass sich der Nutzer erneut anmelden muss.

### Methode zur Client-Authentifizierung: geheimer Schlüssel oder privater JWT-Schlüssel

Wählen Sie, wie sich Dastra bei Ihrem Identitätsanbieter authentifiziert:

* **Geheimer Schlüssel**: Dastra und Ihr Anbieter speichern dasselbe Client-Secret. Geben Sie es im Feld **Geheimer Schlüssel** ein.
* **Privater JWT-Schlüssel (private JWT-Assertion)**: Dastra signiert seine Authentifizierung mit dem privaten Schlüssel, den Sie angeben, und Ihr Anbieter prüft die Signatur mit dem öffentlichen Schlüssel. Es ist kein gemeinsames Secret nötig, was das Risiko einer Offenlegung verringert. Prüfen Sie, ob Ihr Identitätsanbieter diese Methode unterstützt.

<figure><img src="../../../.gitbook/assets/settings-sso-openid-jwt-private-key.png" alt="Das OpenID-Formular mit ausgewählter Option Privater JWT-Schlüssel"><figcaption></figcaption></figure>

Beim **privaten JWT-Schlüssel** wechselt die **Art der Antwort** zu `code` und das Formular verlangt:

* **Privater Schlüssel im PEM-Text (RAW)**: Nach dem Speichern wird der Schlüssel nicht mehr angezeigt. Klicken Sie auf **Replace private key**, um ihn zu ersetzen;
* **Inhalt des Zertifikats (RAW-Format), erforderlich für Entra Id**;
* **Schlüssel-ID (kid)**, optional: Geben Sie die von Ihrem Anbieter beim Hochladen des öffentlichen Schlüssels zugewiesene Schlüssel-ID ein oder lassen Sie das Feld leer, damit Dastra den JWK-Fingerabdruck (RFC 7638) des privaten Schlüssels verwendet.

Hinterlegen Sie anschließend die **JSON-URI für öffentlichen Schlüssel (JWK-Privatschlüssel)** bei Ihrem Anbieter, damit er den öffentlichen Schlüssel der Verbindung abrufen kann.

Das Feld **Aussteller** ist optional. Ist es ausgefüllt, prüft Dastra, dass das empfangene Token von diesem Aussteller ausgestellt wurde, zum Beispiel `https://login.microsoftonline.com/{tenantid}/v2.0`.

{% hint style="danger" %}
Sie können alle Nutzer der Organisation zwingen, ein bestimmtes SSO zu verwenden (Option **Für alle Nutzer erzwingen**). Vorsicht: Wenn das SSO nicht funktioniert, können Sie als Administrator nicht mehr auf Ihr Konto zugreifen. Halten Sie ein lokales Ausweichkonto bereit oder nehmen Sie Nutzer über das Feld **Bestimmte Nutzer, die von der SSO ausgenommen sind (z. B. Sicherheitsadministratoren)** aus (siehe [Single Sign On (SSO)](README.md)). Die Verwaltung des SSO pro Nutzer ist vorzuziehen.
{% endhint %}

{% hint style="warning" %}
**Sonderfall externer Nutzer**\
Nur Konten, die zu einem Abonnement gehören, unterliegen dem SSO. Konten externer Nutzer (die ein zusätzliches Abonnement haben) unterliegen dem SSO nicht.
{% endhint %}

## 3. Das SSO mit OpenId testen

Wenn die Konfiguration abgeschlossen ist, testen Sie die Authentifizierung, indem Sie in der Liste rechts neben der Verbindung auf **Testen** klicken. Wenn Sie auf ein Problem stoßen, eröffnen Sie ein Ticket über die [Supportseite](https://app.dastra.eu/general-settings/support).

<figure><img src="../../../.gitbook/assets/settings-sso-openid-card-status.png" alt="Eine SSO-Verbindung in der Liste mit ihrem Status und der Schaltfläche Testen"><figcaption></figcaption></figure>
