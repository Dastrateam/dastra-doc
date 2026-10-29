# Häufig gestellte Fragen

## Erhalten Antragsteller eine E-Mail-Benachrichtigung, wenn eine Anfrage abgeschlossen wird?

Standardmäßig wird keine E-Mail gesendet. Die Abschlussbenachrichtigung geht nur dann an den Antragsteller, wenn Sie im Abschlussdialog das Kontrollkästchen **Bitte senden Sie eine Benachrichtigung über den Abschluss des Antrags an** (gefolgt von der E-Mail-Adresse des Antragstellers) auswählen. Das Kontrollkästchen erscheint nur, wenn die Anfrage eine E-Mail-Adresse enthält, und es ist ausgegraut, wenn der Antragsteller bereits benachrichtigt wurde.

<figure><img src="../../.gitbook/assets/requests-faq-1.png" alt="Der Abschlussdialog einer Anfrage mit aktiviertem Kontrollkästchen für die Benachrichtigung"><figcaption><p>Das Kontrollkästchen für die Benachrichtigung im Abschlussdialog</p></figcaption></figure>

{% hint style="info" %}
Wählen Sie diese Option, wenn Sie die betroffene Person darüber informieren möchten, dass ihre Anfrage bearbeitet wurde. Das ist gute Praxis und hilft Ihnen nachzuweisen, dass Sie die Antwortfrist der DSGVO eingehalten haben.
{% endhint %}

***

## Wie lange hat der Antragsteller nach dem Abschluss Zugang zum gesicherten Bereich?

Nach dem Abschluss der Anfrage behält der Antragsteller **60 Tage** lang Zugang zu seinem gesicherten Bereich (Austauschverlauf, übermittelte Dokumente). In diesem Zeitraum kann er über die Konversationsoberfläche weiterhin eine Nachricht an die Person senden, die die Anfrage bearbeitet.

Nach Ablauf der 60 Tage wird der Zugang automatisch widerrufen.

## Wie funktioniert die Überprüfung der E-Mail-Adresse des Antragstellers?

Wird eine Anfrage über das öffentliche Formular eingereicht, erhält der Antragsteller eine Bestätigungs-E-Mail mit einem **Bestätigungslink** und einem **6-stelligen Code**. Die Anfrage wird erst berücksichtigt, wenn die Adresse bestätigt wurde.

* Link und Code sind **24 Stunden** gültig. Diese Dauer ist nicht konfigurierbar.
* Nach mehreren falschen Code-Eingaben (4) werden weitere Versuche **30 Minuten lang gesperrt**.
* Wird die Frist überschritten, muss der Antragsteller eine neue Anfrage einreichen.

## Warum kann ein Antragsteller keine neue Anfrage einreichen?

Derselbe Antragsteller (dieselbe E-Mail-Adresse) kann im selben Mandanten keine zweite Anfrage **desselben Typs** einreichen, solange die vorherige, vor weniger als 24 Stunden eingereichte Anfrage nicht abgeschlossen ist.

## Wie lang darf eine Nachricht in einer Anfrage höchstens sein?

Nachrichten an den Antragsteller, die Nachricht im öffentlichen Formular und Abschlussgründe sind auf **3.000 Zeichen** begrenzt. Eine Nachricht kann bis zu **20 Anhänge** enthalten.

***

## Setzt die Seite zur Erfassung von Anfragen Cookies? Ist ein Einwilligungsbanner erforderlich?

Nein. Die Dastra-Widget-Seite (URL der Form `https://api.dastra.eu/v1/client/data-subject-request/page?id=…`) setzt **nur einen einzigen Cookie**: `acaAffinity`.

Dabei handelt es sich um einen **Load-Balancing**-Cookie (Azure Application Gateway). Seine einzige Funktion ist es, die Serversitzung stabil zu halten, indem Anfragen an denselben Backend-Knoten weitergeleitet werden. Er gilt für die **Sitzung**, ist gesichert (`Secure`, `HttpOnly`) und fällt unter die **Einwilligungsbefreiung** nach Artikel 5 Absatz 3 der ePrivacy-Richtlinie, bestätigt durch die Leitlinien der CNIL (Cookies, die für den Betrieb des Dienstes unbedingt erforderlich sind).

Auf dieser Seite ist kein Einwilligungsbanner erforderlich.

{% hint style="success" %}
Audit vom 27. April 2026: 0 Analyse-Cookies, 0 Werbe-Cookies, 0 Drittanbieter-Tracker erkannt. Die geladenen Drittanbieter-Ressourcen (Bootstrap von cdnjs.cloudflare.com, die Schriftart Poppins von fonts.bunny.net, das SDK von cdn.dastra.eu) setzen keine Cookies.
{% endhint %}

***

## Muss der Cookie `acaAffinity` in unserem Cookie-Verzeichnis aufgeführt werden?

Ja, der vollständigen Dokumentation halber, auch wenn er von der Einwilligung befreit ist. Hier ist der empfohlene Eintrag:

| Feld                      | Wert                                           |
| ------------------------- | ---------------------------------------------- |
| Name                      | `acaAffinity`                                  |
| Domain                    | `api.dastra.eu`                                |
| Kategorie                 | Technisch / Unbedingt erforderlich             |
| Zweck                     | Load Balancing: Stabilität der Serversitzung   |
| Dauer                     | Sitzung (beim Schließen des Browsers gelöscht) |
| Herausgeber               | Dastra (Auftragsverarbeiter)                   |
| Rechtsgrundlage           | ePrivacy-Befreiung: unbedingt erforderlich     |
| Einwilligung erforderlich | Nein                                           |
