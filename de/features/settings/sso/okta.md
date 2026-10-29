---
description: >-
  Richten Sie Okta als Identitätsanbieter in Dastra mit dem Protokoll OpenID
  Connect ein.
---

# Okta

Diese Seite erklärt, wie Sie die SSO-Anmeldung mit Okta in Dastra mit dem Protokoll **OpenID Connect** einrichten. Das ist auch mit SAML möglich: siehe [SAML 2](saml.md).

1. Melden Sie sich in der Okta-Administrationskonsole an.
2. Öffnen Sie das Menü **Applications** > **Applications** und klicken Sie auf **Create App Integration**.
3. Wählen Sie **OIDC - OpenID Connect**.
4. Wählen Sie den Anwendungstyp **Web application**.
5. Konfigurieren Sie die Anwendung und aktivieren Sie unter **Grant type** die Option **Implicit (hybrid)**. Als Logo der Anwendung können Sie [dieses hier verwenden](https://www.dastra.eu/img/press/logodastra.png).
6. Rufen Sie in Dastra die Weiterleitungs-URL ab: Öffnen Sie die [Seite zur Verwaltung des SSO](https://app.dastra.eu/general-settings/sso), klicken Sie auf **SSO-Login hinzufügen** und wählen Sie **OpenID**. Kopieren Sie im Abschnitt **Konfiguration** unten im Formular die Weiterleitungs-URL.

   <figure><img src="../../../.gitbook/assets/settings-okta-1.png" alt="Das Ende des Abschnitts Konfiguration des OpenID-Formulars mit der zu kopierenden Weiterleitungs-URL"><figcaption><p>Die von Dastra angezeigte Weiterleitungs-URL</p></figcaption></figure>
7. Gehen Sie zurück zu Okta und fügen Sie die Weiterleitungs-URL in **Sign-in redirect URIs** ein. Wählen Sie die Okta-Nutzer aus, denen Sie Zugriff auf Dastra geben möchten (standardmäßig können Sie **Allow everyone** ankreuzen), und klicken Sie dann auf **Save**.
8. Okta zeigt die Einstellungsseite der neuen Anwendung an: die Client-ID (Client ID), den geheimen Schlüssel (Client secret) und die Okta-Domain, die als Authority dient.
9. Gehen Sie zurück zu Dastra und füllen Sie die Formularfelder aus:

   * **Kunden-ID (ClientId)**: Kopieren Sie die Client ID aus Okta.
   * **Behörde/Domäne**: Geben Sie die Okta-Domain mit dem Protokoll an (`https://<your domain>.okta.com`).
   * **Aussteller**: Lassen Sie das Feld leer.
   * **Geheimer Schlüssel**: Kopieren Sie das Client secret aus Okta.
   * **Geltungsbereich**: `openid profile email`.
   * **Art der Antwort (Standard: id_token)**: `id_token`.

   <figure><img src="../../../.gitbook/assets/settings-okta-2.png" alt="Das OpenID-Formular von Dastra, ausgefüllt mit den Okta-Werten, wobei die geheimen Werte verdeckt sind"><figcaption><p>Das OpenID-Formular von Dastra</p></figcaption></figure>
10. Klicken Sie auf **Speichern** und dann auf der Karte der Verbindung auf **Testen**. Wenn Okta Sie zu Dastra weiterleitet, ist die Einrichtung abgeschlossen.
