---
description: >-
  Lösungen für die wichtigsten bekannten Probleme: nicht erhaltene
  Einladungs-E-Mails, Browser-Cache sowie die Fehler 401, 403, 404 und 500.
---

# Bekannte Probleme

Diese Seite behandelt die Probleme, die jeden Nutzer betreffen können. Zu den Authentifizierungsproblemen von SSO siehe [Bekannte Probleme bei SSO](../features/settings/sso/known-problems.md).

## Der eingeladene Nutzer erhält die Einladungs-E-Mails nicht

Prüfen Sie zunächst Folgendes:

* Die E-Mail-Adresse des Nutzers (Domain, Name usw.) ist korrekt. Ist sie falsch, zeigt die Oberfläche keinen Fehler an.
* Das Postfach der Person ist nicht voll.
* Die E-Mail liegt nicht im Spam-Ordner. In seltenen Fällen blockiert der Spam-Filter des Mailservers des Empfängers die von Dastra gesendete E-Mail.

Wenn die E-Mail weiterhin nicht ankommt, erzeugen Sie einen Einladungslink:

1. Klicken Sie in der Liste der Nutzer auf **Einen Nutzer einladen** und folgen Sie den Schritten.
2. Wählen Sie im Schritt zur Art der Einladung **Einladungslink generieren** und klicken Sie dann auf die Schaltfläche **Einladungslink generieren**.

   <figure><img src="../.gitbook/assets/other-known-problems-1.png" alt="Einladungsfenster mit ausgewählter Option Einladungslink generieren"><figcaption><p>Den Einladungslink wählen</p></figcaption></figure>
3. Kopieren Sie den Link, der unter **Einladungslink, der direkt an den Nutzer gesendet werden kann** angezeigt wird.

   <figure><img src="../.gitbook/assets/other-known-problems-2.png" alt="Einladungsfenster mit dem erzeugten Einladungslink"><figcaption><p>Der erzeugte Einladungslink</p></figcaption></figure>

Senden Sie den Link dann dem Nutzer über den Chat Ihres Unternehmens oder aus Ihrem Postfach.

{% hint style="info" %}
Der Nutzer muss weiterhin seine E-Mail-Adresse bestätigen, um Zugriff auf Ihren Mandanten zu erhalten.
{% endhint %}

## Probleme mit dem Cache Ihres Browsers beheben

Der Browser nutzt einen Cache und Cookies, um Informationen von Websites zu speichern. Wenn Sie sie löschen, lassen sich manche Probleme beheben, etwa beim Laden von Anwendungen wie Dastra.

Probieren Sie die folgenden Lösungen der Reihe nach:

1. **Aktualisieren Sie die Seite ohne Cache** mit Strg + F5 (Windows) oder Cmd + Umschalt + R (Mac).
2. Wenn das Problem weiterhin besteht, **setzen Sie Ihre Präferenzdaten zurück**. Diese Aktion löscht die von Dastra gesetzten Cookies, leert die in Ihrem lokalen Speicher gespeicherten Elemente und setzt Ihre Anzeigeeinstellungen in Dastra zurück. Sie kann manche Anzeigeprobleme beheben.

Öffnen Sie dazu oben rechts Ihr Profilmenü, klicken Sie auf **Nutzerprofil** und dann auf **Präferenzdaten zurücksetzen**.

<figure><img src="../.gitbook/assets/other-known-problems-3.png" alt="Seite Nutzerprofil mit der Schaltfläche Präferenzdaten zurücksetzen"><figcaption><p>Die Präferenzdaten zurücksetzen</p></figcaption></figure>

{% hint style="info" %}
Diese Aktion löscht Ihre Spalteneinstellungen in allen Tabellen von Dastra und zeigt die Tutorials in allen Modulen erneut an.
{% endhint %}

Lösen diese beiden Maßnahmen Ihr Problem nicht, wenden Sie sich aus der Anwendung heraus an den Support: Öffnen Sie Ihr Profilmenü und wählen Sie dann **Hilfe** > **Bitte wenden Sie sich an den Support** oder **Bitte kontaktieren Sie uns über den Chat.**

## Fehler 401 bei der Anmeldung

**Szenario**: Sie melden sich über https://app.dastra.eu bei Dastra an, geben Ihre Zugangsdaten ein, und es erscheint eine Fehlerseite. Ihr Titel lautet „Zugriff verweigert (401)“.

<figure><img src="../.gitbook/assets/other-known-problems-4.png" alt="Fehlerseite 401 von Dastra mit den vorgeschlagenen Lösungen"><figcaption><p>Fehlerseite 401</p></figcaption></figure>

**Lösungen**:

1. **Prüfen Sie die Uhreinstellungen Ihres Computers.** Aktivieren Sie die Zeitsynchronisierung mit dem Internet. Die Ablaufzeiten Ihrer Identifikationstoken werden mit der Uhrzeit Ihres Rechners verglichen: Ist sie nicht mit der Serverzeit synchronisiert, erhalten Sie diesen Fehler. Wie Sie Ihre Uhr einstellen, lesen Sie unter den folgenden Links (auf Englisch):
   * [Mac](https://support.apple.com/en-ca/guide/mac-help/mchlp2996/mac)
   * [PC](https://support.microsoft.com/en-us/windows/how-to-set-your-time-and-time-zone-dfaa7122-479f-5b98-2a7b-fa0b6e01b261)
2. **Verwenden Sie https://app.dastra.eu, um auf Dastra zuzugreifen.** Sie können die Adresse als Favorit speichern. Das Problem kann auftreten, wenn Sie Dastra über Adressen der Domain account.dastra.eu aufrufen, die Browser oft automatisch in ihren Adressvorschlägen speichern.
3. **Löschen Sie die Websitedaten und Cookies Ihres Browsers.**

## Fehler 403: Zugriff verweigert

Die Meldung „Ressource nicht verfügbar (403)“ bedeutet, dass Sie ohne die nötige Berechtigung auf einen Teil von Dastra zugreifen wollen. Ein Administrator hat den Zugriff auf bestimmte Elemente oder Module Ihres Mandanten anhand Ihrer Rolle oder der Berechtigungen Ihres Teams eingeschränkt.

So beheben Sie das Problem:

* Prüfen Sie, ob Sie die nötigen Berechtigungen für das Modul oder das Element haben.
* Wenden Sie sich an einen der Administratoren Ihres Mandanten, damit er Ihre Zugriffsrechte prüft oder anpasst.

## Fehler 404: Element nicht gefunden

Die Meldung „404 not found“ bedeutet, dass das Element, auf das Sie zugreifen wollen, nicht gefunden wird. Es kann von einem anderen Nutzer oder von Ihnen geändert, verschoben oder gelöscht worden sein.

So beheben Sie das Problem:

* Prüfen Sie die Adresse (URL).
* Suchen Sie das Element in der Liste seines Moduls erneut.

## Fehler 500

Dieser Fehler kann gelegentlich auftreten. Häufig wird er verursacht durch:

* Verbindungsprobleme;
* Probleme in Ihrer Umgebung (Browser, Erweiterung usw.);
* mehrere Personen, die gleichzeitig am selben Element arbeiten;
* eine Aktion, die viele Serverressourcen benötigt.

In den meisten Fällen ist das Problem vorübergehend: Warten Sie einige Minuten, bevor Sie es erneut versuchen.

Besteht das Problem weiter, senden Sie über **Hilfe** > **Bitte wenden Sie sich an den Support** in Ihrem Profilmenü einen Fehlerbericht, damit unsere Teams der Ursache nachgehen können.
