---
description: >-
  Dastra ermöglicht es Ihnen, Ihre Benachrichtigungs-E-Mails über Ihren eigenen
  E-Mail-Versandserver zu routen
---

# SMTP-Konfiguration

## Funktionsprinzip

Standardmäßig routet Dastra eine große Anzahl von Benachrichtigungs-E-Mails für die folgenden Dienste:

* [Benachrichtigungen](../notifications.md) in Echtzeit (Neue Kommentare, Aufgaben, ...)
* Austausch-E-Mails im Rahmen [einer Rechteausübungsanfrage](../../gerer-les-exercices-des-droits/)
* Einladungen zu [Audits](../../audit/) für die Befragten
* [Einladungen](../../../getting-started/setup/inviter-utilisateurs.md) neuer Nutzer

Standardmäßig verwendet Dastra seinen eigenen SMTP-Dienst.

## Wie konfiguriere ich meinen SMTP-Versandserver?

{% hint style="warning" %}
Achtung! Die Anpassung des SMTP kann zu Instabilitäten der Plattform führen. Führen Sie diese Manipulation nur durch, wenn Sie sich des ordnungsgemäßen Funktionierens und der Zustellbarkeit Ihres E-Mail-Versanddienstes sicher sind.
{% endhint %}

### Interesse an der SMTP-Anpassung

Dastra ist bestrebt, eine maximale Verfügbarkeit und Sicherheit für den Versand transaktionaler E-Mails zu gewährleisten.

Abhängig von Ihrer internen Sicherheitsrichtlinie kann es jedoch erforderlich sein, das Routing der transaktionalen E-Mails zu internalisieren, um die E-Mail-Flüsse zu kontrollieren.

### Voraussetzungen

Sie benötigen die Konfigurationsdaten Ihres SMTP-Servers:

* SMTP-Host (z. B.: smtp.yourservice.com)
* SMTP-Port (standardmäßig Port 25)
* Benutzername
* Passwort
* Eine **gültige Absender-E-Mail-Adresse** (z. B.: noreply@yourservice.com): Diese Adresse muss von Ihrem SMTP-Anbieter korrekt validiert sein.

{% hint style="warning" %}
Achtung, Ihr SMTP-Server muss zwingend eine sichere Verbindung mit SSL unterstützen
{% endhint %}

### Konfiguration

Gehen Sie auf die [SMTP-Server-Konfigurationsseite](https://app.dastra.eu/general-settings/smtp)

Füllen Sie die Formularfelder mit den unter [Voraussetzungen](./#prerequis) angegebenen Daten aus

![](<../../../.gitbook/assets/Erweiterte Konfiguration28.png>)

Beachten Sie, dass die Konnektivität zum Server automatisch getestet wird, um sicherzustellen, dass die Server-Anmeldedaten korrekt sind. Eine Test-E-Mail wird automatisch von unseren Servern gesendet.

### Tests

Sobald Sie das Formular validiert haben, sollte Ihr SMTP-Server funktionieren.

Sie können überprüfen, ob die Benachrichtigungs-E-Mails tatsächlich von Ihrem SMTP-Server stammen. Erstellen Sie dazu beispielsweise einen Kommentar in einer Verarbeitung und prüfen Sie, ob Sie die Benachrichtigungs-E-Mail in Ihrem Postfach erhalten.

* **Wenn Sie keine E-Mail erhalten**: Entweder haben Sie es nicht geschafft, die Benachrichtigung auszulösen, oder es liegt ein Problem in Ihrer SMTP-Konfiguration vor
* **Wenn Sie eine E-Mail erhalten**: Überprüfen Sie, ob Ihr SMTP und Ihr Absender tatsächlich in den E-Mail-Details erscheinen.

{% hint style="info" %}
[Wie man die E-Mail-Details in GMAIL anzeigt](https://support.google.com/mail/answer/29436?hl=fr).

[Wie man die E-Mail-Details in Outlook anzeigt](https://support.microsoft.com/fr-fr/office/afficher-les-en-t%C3%AAtes-de-message-internet-dans-outlook-cd039382-dc6e-4264-ac74-c048563d212c)
{% endhint %}
