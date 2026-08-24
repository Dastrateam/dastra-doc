# Integration externer Anbieter (Office 365 / Gmail)

### 📌 Ziel

Standardmäßig werden alle von Dastra gesendeten Benachrichtigungen von der Adresse **`no-reply@dastra.eu`** versendet.\
Dank der Integration mit Ihren externen E-Mail-Anbietern (Office 365 oder Gmail) können Sie den Versand über **Ihre eigenen E-Mail-Adressen** konfigurieren, was Ihnen Folgendes ermöglicht:

* Das Vertrauen bei Ihren Empfängern stärken (E-Mails werden mit Ihrer Domain versendet).
* Ihre Versand- und Zustellprotokolle direkt in Ihrer E-Mail-Infrastruktur zentralisieren.
* Ihre eigenen Regeln für Sicherheit, Compliance und Archivierung verwalten.

***

### 📩 Betroffene E-Mails

Diese Konfiguration betrifft **alle von Dastra in Ihrer Organisation versendeten Benachrichtigungs-E-Mails**, zum Beispiel:

* Benachrichtigungen über neue Aufgaben oder Anfragen.
* Einladungen und Erinnerungen.
* Compliance-Warnungen.
* Verfolgung von Rechteausübungsanfragen, Vorfällen, Workflows usw.

👉 Mit anderen Worten, **alle ausgehenden E-Mails ersetzen `no-reply@dastra.eu` durch die konfigurierte Adresse**.

> ⚠️ **Achtung**: Dies betrifft alle E-Mails, die von der Organisation gesendet werden. **Alle Mandanten sind betroffen.**

***

### ⚙️ Konfiguration der Integration

#### Schritt 1: Auf die Anbieter-Integration zugreifen und die Verbindung autorisieren

* Gehen Sie zu **Mandant-Einstellungen > Integrationen**.
* Klicken Sie auf **Konfiguration hinzufügen** für Office 365 oder Gmail.

Sie können auch über diese URL auf die Konfiguration zugreifen: [https://app.dastra.eu/general-settings/smtp](https://app.dastra.eu/general-settings/smtp)

<figure><img src="../../../.gitbook/assets/Erweiterte Konfiguration29.png" alt=""><figcaption></figcaption></figure>

* Wählen Sie den gewünschten Anbieter:
  * **Microsoft 365 (Office 365)**
  * **Google (Gmail / Google Workspace)**
* Beim ersten Hinzufügen fordert Dastra Sie auf, **die Verbindung zu autorisieren**:
  * Es öffnet sich ein Fenster zur Authentifizierung über **OAuth** bei Microsoft oder Google.
  * Sie müssen ein Konto verwenden, das über ausreichende Berechtigungen verfügt (z. B. Konto mit Administratorrolle oder Berechtigung zum Senden im Namen der Domain).
* Nach erfolgreicher Authentifizierung bestätigt Dastra die Verbindung und zeigt den Konfigurationsbildschirm für den Absender an.

⚠️ **Achtung**: Dieser Schritt ist unerlässlich, damit Dastra die Berechtigung hat, E-Mails über Ihren Anbieter zu senden. Ohne dies ist die Absender-Konfiguration nicht wirksam.

#### Schritt 2: Geforderte Informationen eingeben

<figure><img src="../../../.gitbook/assets/Erweiterte Konfiguration30.png" alt=""><figcaption></figcaption></figure>

Zwei Pflichtfelder müssen ausgefüllt werden:

1. **E-Mail des Absenders**
   * Die E-Mail-Adresse, die als Absender der Benachrichtigungen verwendet wird (Beispiel: `notifications@ihredomain.com`).
2. **Absender-Alias**
   * Der als Absender angezeigte Name (Beispiel: `Compliance-Team - Ihr Unternehmen`).

Klicken Sie nach dem Ausfüllen auf **Speichern und testen**, um die Konfiguration zu validieren.

#### Schritt 3: Verifizierung und Tests

* Dastra führt einen Versandtest durch, um die Gültigkeit der konfigurierten Adresse zu bestätigen.
* Überprüfen Sie in Ihrem Posteingang und Ihren Office 365 / Gmail-Protokollen, ob die Testnachricht erfolgreich zugestellt wurde.

Die Nachricht sieht folgendermaßen aus:

<figure><img src="../../../.gitbook/assets/image-1-1-7-1.png" alt=""><figcaption></figcaption></figure>

***

### ✅ Wichtige Punkte zum Merken

1. **Verantwortung für die Protokolle**
   * Durch die Verwendung Ihres eigenen Anbieters (Office 365 oder Gmail) **sind Sie Herr über Ihre Versandprotokolle**.
   * Informationen zu Zustellungen, Ablehnungen oder E-Mail-Blockierungen sind für die Dastra-Teams nicht mehr sichtbar.
2. **Verwaltung der IP-/Domain-Reputation**
   * Ihre Infrastruktur (Office 365 oder Gmail) trägt die Verantwortung für die gute Zustellbarkeit.
   * Stellen Sie sicher, dass:
     * Ihre SPF-/DKIM-/DMARC-Einträge korrekt konfiguriert sind.
     * Ihre Absender-Reputation gut ist.
     * Ihre Domain und Ihre IP nicht auf Spam-Listen stehen.
3. **Auswirkung auf Ihre Empfänger**
   * Die Benachrichtigungen erscheinen als direkt von Ihrer Organisation gesendet.
   * Dies erleichtert die Erkennung und reduziert das Risiko von Verwechslungen mit generischen Adressen.

***

### 🔒 Best Practices für Sicherheit

* Begrenzen Sie die für den Versand verwendeten Adressen (z. B. `no-reply@ihredomain.com` oder `notifications@ihredomain.com`).
* Aktivieren Sie die Multi-Faktor-Authentifizierung für die für die Integration verwendeten Konten.
* Überwachen Sie regelmäßig Ihre Versandprotokolle in Office 365 / Gmail, um Anomalien zu erkennen.

***

👉 Sobald die Integration aktiviert ist, **verwendet Dastra nicht mehr `no-reply@dastra.eu`**: Alle Ihre Benachrichtigungs-E-Mails werden über Ihren konfigurierten Anbieter geleitet.

***

### 🔧 Technische Fragen für IT-Administratoren

Dieser Abschnitt beantwortet häufig gestellte Fragen von IT- und Sicherheitsteams bei der Einrichtung der Office 365-Integration.

#### Welches Authentifizierungsmodell wird verwendet?

Die Office 365-Integration verwendet eine **Anwendungs**-Zustimmung (globale Administrator-Zustimmung) und keine delegierte Zustimmung im Namen eines Nutzers. Für den Betrieb der Integration ist keine aktive Exchange-Lizenz pro Nutzer erforderlich.

#### Welche Microsoft Graph-Scopes werden angefordert?

Dastra fordert bei der OAuth-Zustimmung die folgenden Berechtigungen an:

| Berechtigung       | Verwendung                                            |
| ------------------ | ----------------------------------------------------- |
| `Mail.Send`        | Versand von E-Mails aus dem konfigurierten Postfach   |
| `Mail.Send.Shared` | Versand aus einem geteilten Postfach (Shared Mailbox) |

#### Werden geteilte Postfächer unterstützt?

Ja. Um ein geteiltes Postfach zu verwenden (z. B. `privacy@ihrunternehmen.com`):

1. Melden Sie sich mit Ihrem **persönlichen Konto** an, das über Versandrechte für das geteilte Postfach verfügt.
2. Geben Sie im Feld **E-Mail des Absenders** die Adresse des geteilten Postfachs ein.

Für diesen Betriebsmodus ist keine Änderung der Exchange-Richtlinie (ApplicationAccessPolicy) erforderlich.

{% hint style="info" %}
Stellen Sie sicher, dass Ihr persönliches Konto über das Recht **„Senden als"** oder **„Senden im Auftrag von"** für das geteilte Postfach in Active Directory / Exchange verfügt.
{% endhint %}

#### Müssen die Quell-IPs von Dastra gefiltert werden?

Dastra verwendet die **Microsoft Graph API** für den E-Mail-Versand und keinen klassischen SMTP-Server. Die Aufrufe laufen über die Azure-Infrastruktur von Microsoft, deren IP-Bereiche zahlreich (\~100 Bereiche) sind und sich im Laufe der Zeit ändern können.

**Die IP-Einschränkung wird für diese Integration nicht empfohlen**: Sie wäre schwer zu pflegen und könnte bei Aktualisierungen der Azure-Bereiche zu Dienstunterbrechungen führen. Die Sicherheit wird durch das OAuth 2.0-Protokoll und die Administrator-Zustimmung gewährleistet.

{% hint style="info" %}
Wenn Ihre Sicherheitsrichtlinie eine IP-Einschränkung erfordert, können Sie die von Microsoft für Azure-Dienste veröffentlichten IP-Bereiche einsehen: [https://www.microsoft.com/en-us/download/details.aspx?id=56519](https://www.microsoft.com/en-us/download/details.aspx?id=56519). Beachten Sie, dass diese Liste regelmäßig aktualisiert wird.
{% endhint %}
