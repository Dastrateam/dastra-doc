---
description: >-
  Erfahren Sie, wie Sie Nachrichtenvorlagen mit dynamischen Feldern,
  Bedingungen und Schleifen schreiben, um mit Ihren Kunden oder Kollegen zu
  kommunizieren.
---

# E-Mail-Vorlagen

## Allgemeines

Nachrichtenvorlagen sind in Betroffenenanfragen, Aufgaben, Einladungen zu Fragebögen, Einladungen zum Ausfüllen einer Verarbeitungstätigkeit oder eines Datenschutzvorfalls und in Workflow-Regeln verfügbar, die eine Nachricht senden. Einmal gespeichert, sind sie eine schnelle Möglichkeit, mit den Beteiligten zu kommunizieren. Die Daten des betreffenden Objekts können in den Text eingefügt werden, mit Bedingungen und Schleifen, um weitere Informationen abzurufen.

Diese Seite erklärt, wie Sie eine Vorlage schreiben. Zu den Vorlagentypen, zum Teilen, Importieren und Exportieren siehe die Seite [Nachrichtenvorlagen](../settings/message-templates.md).

## Verwendung

Um eine Vorlage zu verwenden, klicken Sie neben dem Bereich zum Verfassen der Nachricht auf **Wählen Sie eine Vorlage aus**.

<figure><img src="../../.gitbook/assets/general-email-templates-1.png" alt="Bereich zum Verfassen einer Nachricht einer Betroffenenanfrage mit der Schaltfläche Wählen Sie eine Vorlage aus"><figcaption><p>Die Schaltfläche Wählen Sie eine Vorlage aus in einer Betroffenenanfrage</p></figcaption></figure>

Der Bereich zur Auswahl einer Vorlage öffnet sich. Durchsuchen Sie die Liste nach einer Vorlage, öffnen Sie die Vorlagen mit dem Status **Geteilt** oder **Privat** je Typ, oder wählen Sie einen anderen Mandanten, auf den Sie Zugriff haben. Klicken Sie neben der gewünschten Vorlage auf **Bitte auswählen**.

<figure><img src="../../.gitbook/assets/general-email-templates-2.png" alt="Bereich zur Auswahl einer Vorlage mit der Suche, den Tabs nach Typ und der Schaltfläche Vorlage erstellen"><figcaption><p>Der Bereich zur Auswahl einer Vorlage</p></figcaption></figure>

Passt keine Vorlage, klicken Sie auf **Vorlage erstellen**. Das Fenster zum Erstellen enthält:

* den **Namen** der Vorlage, damit Sie sie später wiederfinden;
* den **Modelltext**, den Eingabebereich;
* die Option, die Vorlage mit allen Nutzern des Mandanten zu teilen;
* den Tab **Übersicht**, der die Darstellung der Nachricht in Echtzeit anzeigt;
* den Tab **Input Data**, der die Daten des von der Vorlage betroffenen Objekts anzeigt.

Die Tabs **Übersicht** und **Input Data** erscheinen nur, wenn Sie die Vorlage an der Stelle erstellen, an der Sie die Nachricht verfassen, und nicht in den Einstellungen.

<figure><img src="../../.gitbook/assets/general-email-templates-3.png" alt="Fenster zum Erstellen einer Vorlage mit dem Namen, dem Modelltext, der Übersicht und dem Tab Input Data"><figcaption><p>Das Fenster zum Erstellen einer Vorlage</p></figcaption></figure>

## Die Vorlage anpassen

Im Modelltext können Sie Formatierungen anwenden und Bilder oder Tabellen einfügen. Das Ergebnis erscheint im Tab **Übersicht**.

Um eine Angabe des Objekts einzufügen, klicken Sie in der Symbolleiste auf das Symbol mit den geschweiften Klammern (**Dynamische Felder einfügen**) und wählen Sie ein Feld in der Liste aus. Der Wert des Feldes wird an der Cursorposition eingefügt.

<figure><img src="../../.gitbook/assets/general-email-templates-4.png" alt="Liste der dynamischen Felder, geöffnet über die Symbolleiste des Vorlageneditors"><figcaption><p>Ein dynamisches Feld einfügen</p></figcaption></figure>

## Dynamische Felder

Felder in doppelten geschweiften Klammern sind Variablen: Sie werden durch die Werte des entsprechenden Objekts ersetzt (hier eine Betroffenenanfrage).

### Ein Feld aus den Input Data verwenden

Der Tab **Input Data** listet die Eigenschaften des verknüpften Objekts auf. Um zum Beispiel die Nachricht der Anfrage anzuzeigen:

1. Suchen Sie das Feld im Tab **Input Data**.
2. Geben Sie seinen Namen im Modelltext mit der Syntax `{{message}}` ein.
3. Prüfen Sie das Ergebnis im Tab **Übersicht**.

Sie können mit Schleifen, Bedingungen und Datumsformaten weitergehen.

### Bedingungen

Ein bedingter Block wird nur unter bestimmten Bedingungen angezeigt. Er beginnt mit einem `if`-Tag und endet mit einem `endif`-Tag. Zum Beispiel:

```liquid
{% if attachments != blank %}
  You have an attachment
{% endif %}
```

Der Block wird nur angezeigt, wenn die Anfrage einen Anhang enthält.

### Schleifen

Schleifen funktionieren auf dieselbe Weise, mit einer schleifeninternen Variablen:

```liquid
{% for purpose in purposes %}
  {{ purpose }}
{% endfor %}
```

In diesem Beispiel durchläuft die Schleife die Liste `purposes` und zeigt jedes Element in der Variablen `purpose` an.

### Datumsformat

Die Datumsangaben der Input Data sind so, wie sie sind, nicht darstellbar. Wenden Sie ein Format auf sie an:

```liquid
{{ dateCreation | date: "%d-%m-%Y at %H:%M" }}
```

Diese Vorlage ergibt zum Beispiel 15-03-2023 at 15:40.

### Ein vollständigeres Beispiel

Der folgende Text verwendet alle oben genannten Elemente:

```liquid
Hello,

We have received your data subject request on {{ dateCreation | date: "%d-%m-%Y at %H:%M" }} concerning {{ givenName }} {{ familyName }}.

The request relates to the following purposes:
{% for purpose in purposes %}
* {{ purpose }}
{% endfor %}

{% if attachments != blank %}
We have received the following attachments:
{% for attachment in attachments %}
* {{ attachment.fileName }}
{% endfor %}
{% endif %}

We will keep you informed of the progress of your request.

Kind regards,
{{ operator.displayName }}
```

Für die gerade bearbeitete Anfrage wird die Nachricht wie folgt umgewandelt:

<figure><img src="../../.gitbook/assets/general-email-templates-5.png" alt="Vorschau der aus der vollständigen Vorlage erzeugten Nachricht für eine Betroffenenanfrage"><figcaption><p>Die Darstellung einer vollständigen Vorlage</p></figcaption></figure>

## Weiterführende Informationen

Die Vorlagen verwenden die Liquid-Syntax. Die Liste der Tags und Filter finden Sie in der [Liquid-Dokumentation](https://shopify.github.io/liquid/).
