---
description: >-
  Senden Sie die Benachrichtigungs-E-Mails von Dastra über Ihren eigenen
  E-Mail-Versandserver.
---

# SMTP-Konfiguration

Diese Seite erklärt, wie Sie die E-Mails von Dastra über Ihren eigenen SMTP-Server leiten. Sie richtet sich an die Inhaber der Organisation.

## Funktionsweise

Standardmäßig versendet Dastra seine E-Mails mit seinem eigenen SMTP-Dienst. Das betrifft:

* [Benachrichtigungen](../notifications.md) in Echtzeit (neue Kommentare, Aufgaben usw.);
* den E-Mail-Austausch im Rahmen einer [Betroffenenanfrage](../../requests/README.md);
* Einladungen an die Teilnehmer von [Fragebögen](../../questionnaires/README.md);
* [Einladungen](../../../getting-started/setup/users.md) neuer Nutzer.

Sobald Ihr Server konfiguriert ist, laufen alle diese E-Mails über ihn, für alle Mandanten der Organisation.

{% hint style="warning" %}
Das Anpassen von SMTP kann die Plattform instabil machen. Tun Sie dies nur, wenn Sie sicher sind, dass Ihr E-Mail-Versanddienst einwandfrei funktioniert und zuverlässig zustellt.
{% endhint %}

## Warum SMTP anpassen

Dastra stellt die Verfügbarkeit und Sicherheit transaktionaler E-Mails sicher. Je nach Ihrer internen Sicherheitsrichtlinie kann es dennoch nötig sein, das Routing dieser E-Mails selbst zu steuern, um Ihre Mailflüsse zu verwalten.

## Zugang und Voraussetzungen

Die Seite befindet sich unter **Organisationseinstellungen** > **Personalisiertes SMTP**. Sie ist den Inhabern der Organisation und dem Enterprise-Tarif vorbehalten (Funktion für erweiterte Sicherheit).

Sie haben zwei Möglichkeiten:

* einen Anbieter verbinden (**Outlook (MS Office 365)** oder **Gmail (Google workspace)**): siehe [Integration externer Anbieter](office-365-gmail.md);
* die Einstellungen Ihres eigenen SMTP-Servers eingeben, wie unten beschrieben.

Halten Sie für einen SMTP-Server Folgendes bereit:

* den Namen des SMTP-Servers (zum Beispiel `smtp.yourservice.com`);
* den Port des SMTP-Servers (standardmäßig 25);
* den Benutzernamen und das Passwort des Servers;
* eine gültige Absenderadresse (zum Beispiel `noreply@yourservice.com`): Ihr SMTP-Anbieter muss sie validiert haben;
* einen Absender-Alias, also den Namen, der als Absender angezeigt wird (zum Beispiel `Compliance-Team`).

{% hint style="warning" %}
Dastra verlangt eine gesicherte Verbindung mit TLS, mindestens in Version 1.2. Ihr SMTP-Server muss dies unterstützen.
{% endhint %}

## Konfiguration

1. Öffnen Sie die [SMTP-Konfigurationsseite](https://app.dastra.eu/general-settings/smtp).
2. Füllen Sie im Bereich **Personalisiertes SMTP** die Felder **Name des SMTP-Servers (TLS erforderlich)**, **SMTP-Server-Port**, **Benutzername des SMTP-Servers**, **SMTP-Server-Passwort**, **E-Mail des Absenders** und **Absender-Alias** aus.
3. Klicken Sie auf **Speichern**.

<figure><img src="../../../.gitbook/assets/settings-smtp-config-form.png" alt="Konfigurationsformular des SMTP-Servers mit den Feldern Server, Port, Benutzername, Passwort, Absender-E-Mail und Absender-Alias"><figcaption><p>Das Konfigurationsformular des SMTP-Servers</p></figcaption></figure>

Beim Speichern verbindet sich Dastra mit Ihrem Server und sendet eine Testnachricht an die E-Mail-Adresse Ihres Kontos. Schlägt die Verbindung fehl, wird die Konfiguration nicht gespeichert und die vom Server zurückgegebene Fehlermeldung angezeigt.

Solange ein Anbieter verbunden ist, ist das Formular für das personalisierte SMTP deaktiviert. Klicken Sie zuerst auf **Integration entfernen**, um Ihren eigenen Server zu verwenden.

## Testen

Sobald die Konfiguration gespeichert ist, erscheint die Schaltfläche **Testen**. Klicken Sie darauf und bestätigen Sie: Dastra sendet eine Testnachricht an die E-Mail-Adresse Ihres persönlichen Kontos.

Sie können auch prüfen, ob Benachrichtigungs-E-Mails von Ihrem Server kommen. Fügen Sie zum Beispiel einen Kommentar zu einer Verarbeitungstätigkeit hinzu und sehen Sie nach, ob die Benachrichtigung in Ihrem Postfach ankommt.

* **Sie erhalten keine E-Mail**: Entweder wurde die Benachrichtigung nicht ausgelöst, oder Ihre SMTP-Konfiguration hat ein Problem.
* **Sie erhalten eine E-Mail**: Prüfen Sie, ob Ihr SMTP-Server und Ihr Absender in den Details der Nachricht erscheinen.

{% hint style="info" %}
[So sehen Sie die E-Mail-Details in Gmail](https://support.google.com/mail/answer/29436).

[So sehen Sie die E-Mail-Details in Outlook](https://support.microsoft.com/en-us/office/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c)
{% endhint %}
