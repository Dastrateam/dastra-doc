# Häufig gestellte Fragen

### Erhalten Antragsteller eine E-Mail-Benachrichtigung beim Abschluss einer Anfrage? <a href="#comment-afficher-lhistorique-des-modifications-sur-un-traitement" id="comment-afficher-lhistorique-des-modifications-sur-un-traitement"></a>

Standardmäßig wird keine E-Mail automatisch gesendet. Die Abschlussbenachrichtigung wird dem Antragsteller **nur gesendet, wenn das Kontrollkästchen "Abschlussbenachrichtigung der Anfrage senden an"** zum Zeitpunkt des Abschlusses ausdrücklich aktiviert ist.

{% hint style="info" %}
Denken Sie daran, diese Option systematisch zu aktivieren, wenn Sie die betroffene Person über die Erledigung ihrer Anfrage informieren möchten -- dies ist eine bewährte Praxis, um die Einhaltung der von der DSGVO vorgeschriebenen Antwortfrist nachzuweisen.
{% endhint %}

***

### Wie lange hat der Antragsteller nach dem Abschluss Zugang zum gesicherten Bereich?

Nach Abschluss der Anfrage behält der Antragsteller **60 Tage** lang Zugang zu seinem gesicherten Bereich (Austauschverlauf, übermittelte Dokumente).

Dieser Zugang ermöglicht es ihm auch, über die Konversationsoberfläche eine Nachricht an den Anfragebearbeiter zu übermitteln.&#x20;

Nach Ablauf dieses Zeitraums wird der Zugang automatisch widerrufen.<br>

***

### Wie funktioniert die Überprüfung der E-Mail-Adresse des Antragstellers?

Wird eine Anfrage über das öffentliche Formular eingereicht, erhält der Antragsteller eine Bestätigungs-E-Mail mit einem **Bestätigungslink** und einem **6-stelligen Code**. Die Anfrage wird erst berücksichtigt, wenn die Adresse bestätigt wurde.

* Link und Code sind **24 Stunden** gültig. Diese Dauer ist nicht konfigurierbar.
* Nach mehreren falschen Code-Eingaben (4) werden weitere Versuche **30 Minuten lang gesperrt**.
* Wird die Frist überschritten, muss der Antragsteller eine neue Anfrage einreichen.

### Warum kann ein Antragsteller keine neue Anfrage einreichen?

Derselbe Antragsteller (dieselbe E-Mail-Adresse) kann im selben Arbeitsbereich keine zweite Anfrage **desselben Typs** einreichen, solange die vorherige, vor weniger als 24 Stunden eingereichte Anfrage nicht abgeschlossen ist.

### Wie lang darf eine Nachricht in einer Anfrage höchstens sein?

Nachrichten an den Antragsteller, die Nachricht im öffentlichen Formular und Abschlussgründe sind auf **3.000 Zeichen** begrenzt. Eine Nachricht kann bis zu **20 Anhänge** enthalten.

### Setzt die Seite zur Erfassung von Anfragen Cookies? Ist ein Einwilligungsbanner erforderlich?

Nein. Die Dastra-Widget-Seite (URL vom Typ `https://api.dastra.eu/v1/client/data-subject-request/page?id=…`) setzt **nur einen einzigen Cookie**: `acaAffinity`.

Dabei handelt es sich um einen **Load-Balancing**-Cookie (Azure Application Gateway), dessen einzige Funktion darin besteht, die Stabilität der Serversitzung aufrechtzuerhalten, indem Anfragen an denselben Backend-Knoten weitergeleitet werden. Er ist ein **Session**-Cookie, gesichert (`Secure`, `HttpOnly`) und fällt unter die **Einwilligungsbefreiung** gemäß Artikel 5§3 der ePrivacy-Richtlinie, bestätigt durch die Leitlinien der CNIL (für den Betrieb des Dienstes unbedingt erforderliche Cookies).

**Auf dieser Seite ist kein Einwilligungsbanner erforderlich.**

{% hint style="success" %}
Audit durchgeführt am 27. April 2026: 0 Analyse-Cookies, 0 Werbe-Cookies, 0 Drittanbieter-Tracker erkannt. Die geladenen Drittanbieter-Ressourcen (Bootstrap über cdnjs.cloudflare.com, Schriftart Poppins über fonts.bunny.net, SDK über cdn.dastra.eu) setzen keine Cookies.
{% endhint %}

***

### Muss der Cookie `acaAffinity` in unserem Cookie-Verzeichnis aufgeführt werden?

Ja, der Vollständigkeit der Dokumentation halber, auch wenn er von der Einwilligung befreit ist. Hier ist der empfohlene Eintrag:

| Feld                     | Wert                                            |
| ------------------------ | ----------------------------------------------- |
| Name                     | `acaAffinity`                                   |
| Domain                   | `api.dastra.eu`                                 |
| Kategorie                | Technisch / Unbedingt erforderlich              |
| Zweck                    | Load Balancing -- Stabilität der Serversitzung   |
| Dauer                    | Session (beim Schließen des Browsers gelöscht)  |
| Herausgeber              | Dastra (Auftragsverarbeiter)                    |
| Rechtsgrundlage          | ePrivacy-Befreiung -- unbedingt erforderlich    |
| Einwilligung erforderlich | Nein                                            |
