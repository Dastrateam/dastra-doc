---
description: >-
  Senden Sie die E-Mails von Dastra aus Ihrem eigenen Office-365- oder
  Gmail-Postfach statt von der Standardadresse von Dastra.
---

# Integration externer Anbieter (Office 365 / Gmail)

Diese Seite erklärt, wie Sie die E-Mails von Dastra über Ihr eigenes Office-365- oder Gmail-Konto versenden. Sie richtet sich an die Inhaber der Organisation. Um einen anderen Versandserver zu verwenden, lesen Sie [SMTP-Konfiguration](README.md).

## Zweck

Standardmäßig stammen alle von Dastra gesendeten Benachrichtigungen von der Adresse `no-reply@dastra.eu`. Mit der Integration eines externen E-Mail-Anbieters (Office 365 oder Gmail) versenden Sie diese E-Mails von Ihren eigenen Adressen. So können Sie:

* Vertrauen bei Ihren Empfängern aufbauen, weil die E-Mails mit Ihrer Domain versendet werden;
* Ihre Versand- und Zustellprotokolle in Ihrer eigenen E-Mail-Infrastruktur bündeln;
* Ihre eigenen Sicherheits-, Compliance- und Archivierungsregeln anwenden.

## Betroffene E-Mails

Die Konfiguration gilt für alle E-Mails, die Dastra innerhalb Ihrer Organisation versendet, zum Beispiel:

* Benachrichtigungen über neue Aufgaben oder Anfragen;
* Einladungen und Erinnerungen;
* Compliance-Warnungen;
* die Nachverfolgung von Betroffenenanfragen, Datenschutzvorfällen, Workflows usw.

Sobald die Integration aktiviert ist, verwenden alle diese E-Mails die konfigurierte Adresse statt `no-reply@dastra.eu`.

{% hint style="warning" %}
Alle E-Mails der Organisation sind betroffen, also alle Mandanten.
{% endhint %}

## Die Integration einrichten

Die Einrichtung ist den Inhabern der Organisation und dem Enterprise-Tarif vorbehalten (Funktion für erweiterte Sicherheit).

### Schritt 1: die Verbindung zum Anbieter autorisieren

1. Öffnen Sie [https://app.dastra.eu/general-settings/smtp](https://app.dastra.eu/general-settings/smtp), also **Organisationseinstellungen** > **Personalisiertes SMTP**.
2. Klicken Sie im Bereich **Anbieter** auf **Outlook (MS Office 365)** oder **Gmail (Google workspace)**.
3. Es öffnet sich ein Fenster, in dem Sie sich per OAuth bei Microsoft oder Google anmelden. Verwenden Sie ein Konto, das E-Mails mit der gewünschten Adresse senden darf.
4. Nach der Authentifizierung zeigt Dastra den Bildschirm zur Konfiguration des Absenders an.

<figure><img src="../../../.gitbook/assets/screenshot-2025-09-19-110910.png" alt="Seite Personalisiertes SMTP mit den Schaltflächen der Anbieter Outlook und Gmail"><figcaption><p>Die auf der Seite Personalisiertes SMTP angebotenen Anbieter</p></figcaption></figure>

{% hint style="info" %}
In den Mandanteneinstellungen führt die Karte der Office-365- oder Gmail-Integration zu derselben Seite.
{% endhint %}

Dieser Schritt ist zwingend: Ohne die Autorisierung des Anbieters kann Dastra keine E-Mails mit Ihrem Konto senden.

### Schritt 2: den Absender eingeben

Zwei Felder sind erforderlich:

1. **E-Mail des Absenders**: die Adresse, die als Absender der Benachrichtigungen verwendet wird (zum Beispiel `notifications@yourdomain.com`).
2. **Absender-Alias**: der Name, der als Absender angezeigt wird (zum Beispiel `Compliance-Team - Ihr Unternehmen`).

Klicken Sie anschließend auf **Speichern und testen**.

### Schritt 3: den Versand prüfen

Dastra sendet mit dem konfigurierten Absender eine Testnachricht an die E-Mail-Adresse Ihres Kontos. Prüfen Sie Ihren Posteingang und Ihre Office-365- oder Gmail-Protokolle, um sicherzustellen, dass die Nachricht angekommen ist.

<figure><img src="../../../.gitbook/assets/settings-smtp-test-email-received.png" alt="Empfangene Testnachricht mit dem Anhang test-attachment.txt"><figcaption><p>Die empfangene Testnachricht</p></figcaption></figure>

Sobald die Verbindung hergestellt ist, zeigt die Seite **Personalisiertes SMTP** die Absender-E-Mail und den Alias an. Klicken Sie auf **Integration entfernen**, um zum Standardversand von Dastra zurückzukehren oder einen anderen Server zu verwenden.

## Wichtige Hinweise

### Versandprotokolle

Mit Ihrem eigenen Anbieter kontrollieren Sie Ihre Versandprotokolle. Die Dastra-Teams sehen für diese E-Mails keine Informationen mehr über Zustellung, Ablehnung oder Sperrung.

### Reputation von IP-Adresse und Domain

Ihre Infrastruktur ist für eine gute Zustellbarkeit verantwortlich. Stellen Sie sicher, dass:

* Ihre SPF-, DKIM- und DMARC-Einträge korrekt konfiguriert sind;
* Ihre Absenderreputation gut ist;
* Ihre Domain und Ihre IP-Adresse nicht als Spam gelistet sind.

### Auswirkungen auf Ihre Empfänger

Die Benachrichtigungen erscheinen, als wären sie direkt von Ihrer Organisation gesendet worden. Die Empfänger erkennen sie, und das Risiko einer Verwechslung mit einer allgemeinen Adresse ist geringer.

## Bewährte Sicherheitspraktiken

* Beschränken Sie die für den Versand verwendeten Adressen (zum Beispiel `no-reply@yourdomain.com` oder `notifications@yourdomain.com`).
* Aktivieren Sie die Multi-Faktor-Authentifizierung für die Konten, die für die Integration verwendet werden.
* Prüfen Sie Ihre Versandprotokolle in Office 365 oder Gmail regelmäßig, um Auffälligkeiten zu erkennen.

## Technische Fragen für IT-Administratoren

Dieser Abschnitt beantwortet häufige Fragen von IT- und Sicherheitsteams bei der Einrichtung der Office-365-Integration.

### Authentifizierungsmodell

Die Office-365-Integration verwendet den OAuth-2.0-Autorisierungscode-Fluss mit **delegierten** Berechtigungen: Dastra sendet E-Mails im Namen des Kontos, das die Verbindung autorisiert hat, mit den Rechten dieses Kontos. Es handelt sich nicht um eine Anwendungsverbindung mit globaler Administratorzustimmung. Je nach Richtlinie Ihrer Microsoft-365-Organisation muss ein Administrator die angeforderten Berechtigungen gegebenenfalls genehmigen.

### Angeforderte Microsoft-Graph-Berechtigungen

Dastra fordert bei der Autorisierung die folgenden delegierten Berechtigungen an:

| Berechtigung | Verwendung |
| --- | --- |
| `Mail.Send` | E-Mails aus dem Postfach des verbundenen Kontos senden |
| `Mail.Send.Shared` | Senden aus einem freigegebenen Postfach |
| `offline_access` | Zugriff erneuern, ohne sich erneut anzumelden |

Für Gmail fordert Dastra den Zugriff `https://mail.google.com/` an.

### Unterstützung freigegebener Postfächer

Ja. Um ein freigegebenes Postfach zu verwenden (zum Beispiel `privacy@yourcompany.com`):

1. Melden Sie sich mit Ihrem **persönlichen Konto** an, das berechtigt ist, aus dem freigegebenen Postfach zu senden.
2. Geben Sie im Feld **E-Mail des Absenders** die Adresse des freigegebenen Postfachs ein.

Für diese Einrichtung ist keine Änderung der Exchange-Richtlinien (ApplicationAccessPolicy) erforderlich.

{% hint style="info" %}
Stellen Sie sicher, dass Ihr persönliches Konto im Active Directory oder in Exchange die Berechtigung „Senden als“ oder „Im Auftrag von senden“ für das freigegebene Postfach besitzt.
{% endhint %}

### Freigabe der ausgehenden IP-Adressen von Dastra

Dastra versendet E-Mails über die Microsoft-Graph-API und nicht über einen klassischen SMTP-Server. Die Aufrufe laufen über die Azure-Infrastruktur von Microsoft, die viele IP-Bereiche besitzt (etwa 100), die sich im Lauf der Zeit ändern.

Eine IP-Filterung wird für diese Integration nicht empfohlen: Sie wäre schwer zu pflegen und könnte den Dienst unterbrechen, wenn die Azure-Bereiche aktualisiert werden. Die Sicherheit beruht auf OAuth 2.0 und auf der Autorisierung durch das verbundene Konto.

{% hint style="info" %}
Wenn Ihre Sicherheitsrichtlinie eine IP-Beschränkung verlangt, finden Sie die von Microsoft veröffentlichten Bereiche für Azure-Dienste hier: [https://www.microsoft.com/en-us/download/details.aspx?id=56519](https://www.microsoft.com/en-us/download/details.aspx?id=56519). Diese Liste wird regelmäßig aktualisiert.
{% endhint %}
