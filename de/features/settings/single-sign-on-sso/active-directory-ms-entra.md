---
description: >-
  Diese Seite erklärt, wie Sie das Dastra-SSO mit dem Active Directory von
  Microsoft unter Verwendung des Saml2P-Protokolls einrichten
---

# Active Directory (MS Entra)

## **Konfiguration der Anwendung im Azure-Portal**

* Gehen Sie zum Microsoft Azure-Portal: [https://portal.azure.com](https://portal.azure.com)
* Klicken Sie auf **Active Directory**
* In der linken Navigation klicken Sie auf Entreprise Applications
* Klicken Sie auf die Schaltfläche **New application**
* Klicken Sie dann auf **Create your own application**
* Geben Sie den Namen der Anwendung ein, Sie können einfach „Dastra" eingeben
* Wählen Sie das Kontrollkästchen „**Integrate any other application you don't find in the gallery (Non-gallery)**"
* Ihre Anwendung ist erstellt!
* Klicken Sie auf **Single-Sign-On** und wählen Sie **SAML**
* **Sie gelangen auf diese Seite**

![](<../../../.gitbook/assets/image-8-1.png>)

## **Konfiguration des SSO-Clients in Dastra**

**Schritt 1: Erstellen Sie einen SSO-OpenId-Login in Dastra.**

* Gehen Sie auf die [SSO-Konfigurationsseite von Dastra](https://app.dastra.eu/general-settings/sso)
* Klicken Sie auf „SSO-Login hinzufügen"
* Wählen Sie **SAML** als „**SSO-Protokoll**"-Typ
* Geben Sie ein Verbindungslabel ein. Zum Beispiel „Active Directory"

**Schritt 2: Konfigurieren Sie den SSO-Login im Active Directory**

* Gehen Sie zurück zur SAML-Konfigurationsseite des Active Directory
* **Klicken Sie auf die Schaltfläche „Edit"** im ersten Bereich.
* Geben Sie die Verbindungsinformationen (**Entity ID und ACS-URL**) wie folgt ein:

![](<../../../.gitbook/assets/image-3-1-1-1-1-1-1.png>)

* Klicken Sie auf **Speichern**
* Gehen Sie direkt zu Bereich 3, um **das Zertifikat im Base64-Format herunterzuladen**
* ![](<../../../.gitbook/assets/image-5-1-1-1.png>)
* **Öffnen Sie die CER-Datei mit Ihrem bevorzugten Texteditor** (zum Beispiel Notepad) und kopieren Sie den Inhalt (STRG + C)
* ![](<../../../.gitbook/assets/image-4-1-2-1.png>)

**Schritt 3: Zertifikat zum Dastra-Client hinzufügen**

* Gehen Sie zurück zum SAML-Verbindungserstellungsbildschirm in Dastra
* **Fügen Sie den Zertifikatstext** in das Feld „Identity Provider Certificate (RAW)" ein (STRG + V)

**Schritt 4: IdP-URLs in Dastra konfigurieren**

* Kopieren Sie die 3 Links Entity Id, SSO URL und Logout URL aus Schritt 4 des Active Directory
* ![](<../../../.gitbook/assets/image-7-1-1-1.png>)
* Kopieren Sie die URLs nach folgendem Schema:\
  **Login URL => Single sign on url** \
  **Azure AD Identifier => Identity provider's Entity Id** \
  **Logout Url => Identity provider Signout url**
* Ihr SSO-Konfigurationsformular in Dastra sollte so aussehen:
* ![](<../../../.gitbook/assets/image-2-1-1-1-1-1-1-1-1.png>)
* Sie können das Kontrollkästchen „Nutzer erstellen, wenn der Nutzer noch nie in Dastra eingeladen wurde" aktivieren. Wenn Sie diese Option aktivieren, werden die Konten Ihrer AD-Organisation, die nicht in Dastra vorhanden sind, bei der Anmeldung automatisch bereitgestellt, sofern sie nicht lokal in Dastra existieren.

![](<../../../.gitbook/assets/image-6-1.png>)

* **Speichern Sie Ihre Änderungen** in Dastra

{% hint style="info" %}
Bevor Sie den Verbindungstest starten, stellen Sie sicher, dass ein Nutzer der neuen Anwendung zugewiesen ist.
{% endhint %}

### Testen Sie Ihre SSO-Verbindung

Klicken Sie dann auf die Schaltfläche „Test" am unteren Rand des Formulars im Active Directory. Wenn alles korrekt funktioniert, sollten Sie zur Dastra-Anwendung weitergeleitet werden.&#x20;

{% hint style="info" %}
Wenn Sie **die automatische Kontobereitstellung** nicht aktiviert haben, wird der Zugriff auf der Dastra-Seite verweigert, wenn das lokale Konto nicht über eine Einladung erstellt wurde
{% endhint %}

### Weiterführende Informationen

{% content-ref url="problemes-connus.md" %}
[problemes-connus.md](problemes-connus.md)
{% endcontent-ref %}

{% content-ref url="saml-2.md" %}
[saml-2.md](saml-2.md)
{% endcontent-ref %}
