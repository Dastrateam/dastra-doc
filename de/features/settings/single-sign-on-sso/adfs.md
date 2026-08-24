---
description: >-
  Dastra integriert sich mit ADFS. Diese Seite erklärt die Besonderheiten der
  SSO-Konfiguration mit AD FS
---

# ADFS

## Was ist ADFS?

Die Active Directory Federation Services (allgemein unter dem Akronym ADFS bekannt) sind eine von Microsoft entwickelte Single-Sign-On-Lösung (SSO). Diese Dienste, die ein Bestandteil der Windows-Server-Betriebssysteme sind, ermöglichen Nutzern die Authentifizierung über Active Directory (AD), wenn sie auf eine Anwendung zugreifen möchten, die die integrierte Windows-Authentifizierung (IWA) nicht nutzen kann.

## **Konfiguration von ADFS in Dastra**

**Schritt 1: Erstellen Sie einen SAML-Login in Dastra.**

* Gehen Sie auf die [SSO-Konfigurationsseite von Dastra](https://app.dastra.eu/general-settings/sso)
* Klicken Sie auf „SSO-Login hinzufügen"
* Wählen Sie **SAML** als „**SSO-Protokoll**"-Typ
* Im Feld „Identity Provider's Entity id (issuer)" geben Sie die folgende URL ein: [**http**://\<adfs server url>/adfs/services/trust](http://fs.saur.fr/adfs/services/trust)&#x20;
* Im Feld „**Identity Provider single sign on url**": [**https**://\<adfs server url>](http://fs.saur.fr/adfs/services/trust)/adfs/ls

**Schritt 2: Abrufen des ADFS-Zertifikats**&#x20;

* Gehen Sie zum Verzeichnis „**Certificates**" des ADFS-Servers
* Rufen Sie das .CER-Zertifikat Ihres ADFS-Servers ab, indem Sie das Zertifikat „**Token-Signing**" verwenden.&#x20;

![](<../../../.gitbook/assets/image-259.png>)

* Klicken Sie auf „**View Certificates**"

![](<../../../.gitbook/assets/image-250.png>)

Kopieren Sie den Code des X509-Zertifikats, indem Sie die CER-Datei mit einem Texteditor öffnen.&#x20;

Fügen Sie den Zertifikatscode in das Zertifikatsfeld ein, das mit „----BEGIN CERTIFICATE-----" beginnt und mit „--------END CERTIFICATE-----" endet.

Die Konfiguration Ihres Logins sollte folgendermaßen aussehen:&#x20;

![](<../../../.gitbook/assets/image-257.png>)

**Schritt 3**: Bewahren Sie die folgenden Werte auf:&#x20;

* **SP redirect URI (Format: https://account.dastra.eu/xxxxx-xxxx-xxxx-xxxx/Acs):** Die SP redirect URI ist die Application Callback URL (das SAML Token wird hierhin gepostet). Die unterstützte Kodierung ist SHA-256 und höher.&#x20;
* **Identity Provider's Entity id (issuer)**

Diese beiden Werte benötigen Sie zur Konfiguration des ADFS-Servers, damit dieser die SSO-Anfragen von Dastra akzeptiert

## Konfiguration des Dastra-Clients in ADFS

So konfigurieren Sie das Dastra SSO mit ADFS SSO SAML2P

**Schritt 1**: Öffnen Sie auf Ihrem ADFS-Server „AD FS Management"

**Schritt 2:** Klicken Sie rechts auf **„Relying Party Trusts**" und wählen Sie „**Add Relying Party Trust**". Dies startet den Assistenten zum Hinzufügen eines **Relying Party Trust**.

&#x20;![](<../../../.gitbook/assets/image-248.png>)

**Schritt 3:**  Im Bildschirm _**Select Data Source**_ wählen Sie _**Enter data about the relying party manually**_.&#x20;

&#x20;![](<../../../.gitbook/assets/image-254.png>)

**Schritt 4:**  Geben Sie einen _**Display name** ein, zum Beispiel **„Dastra"**_ _und klicken Sie auf **„Next"**_

**Schritt 5:** Wählen Sie _**AD FS profile**_ mit SAML 2.0 und klicken Sie auf „**Next**"

**Schritt 6**:  Klicken Sie auf _**Next**_ im Bildschirm _**Configure Certificate** ohne ein Zertifikat auszuwählen_

**Schritt 7:** Wählen Sie „_**Enable support for the SAML 2.0 SSO Web SSO protocol**_."

![](<../../../.gitbook/assets/image-252.png>)&#x20;

Im Feld „Relying party SAML 2.0 SSO service URL" tragen Sie die URL der „**SP redirect URI**" aus Dastra ein. Diese URL hat das Format: https://account.dastra.eu/xxxx-xxxx-xxxx-xxxx/Acs

**Schritt 8**: Im Bereich „**Add a Relying party trust identifier**" **fügen Sie zwei Werte hinzu**: _account.dastra.eu_ und _https://account.dastra.eu_

**Schritt 9**: Klicken Sie auf Weiter bis zum Ende des Prozesses.&#x20;

**Schritt 10**: Aktivieren Sie das Kontrollkästchen _**Open the Edit Claim Rules dialog**_ bevor Sie auf „Fertig stellen" klicken. Ein Fenster „_**Edit Claim Rules"**_ wird dann angezeigt.&#x20;

![](<../../../.gitbook/assets/image-251.png>)

\
**Schritt 11**: Klicken Sie auf _**Add Rule**_ und wählen Sie die „Claim Rule": „_**Send LDAP Attributes as Claims"**_.

![](<../../../.gitbook/assets/image-256.png>)

**Schritt 12**: Ordnen Sie die Claims wie folgt zu. Die Claim-Namen können je nach Konfiguration Ihres Servers variieren. Dastra benötigt drei Attribute zum Funktionieren: E-Mail (Pflicht), Vorname und Nachname des Nutzers:

&#x20;![](<../../../.gitbook/assets/image-258.png>)

**Schritt 13**: Klicken Sie auf „**Finish**" und klicken Sie erneut auf „**Add Rule**". Wählen Sie dieses Mal den Typ „_**Transform an Incoming Claim"** und klicken Sie auf Weiter._

**Schritt 14:**  Konfigurieren Sie die folgende Regel: **Email Address => Name ID => Email**

![](<../../../.gitbook/assets/image-249.png>)

Wenden Sie anschließend die Änderungen an, indem Sie auf „Apply" klicken

**Schritt 15**: Zurück im Fenster „**AD FS Management**" klicken Sie rechts auf „**Relying Party for Dastra**" und wählen Sie „**properties**". Im Tab _**Advanced**_ wählen Sie **SHA­-256** als sicheren Algorithmus.\
&#x20;

**Schritt 16**:  Geschafft!

## **Abschluss und Tests!**

Sobald alles auf beiden Seiten konfiguriert ist, können Sie zu Dastra zurückkehren und einen SSO-Login-Test direkt im Manager starten.
