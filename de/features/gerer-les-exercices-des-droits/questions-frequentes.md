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
