---
description: >-
  Erstellen Sie einen spezialisierten Chat-Assistenten mit eigener
  Persönlichkeit, eigenen Regeln und eigenen Tools
---

# Einen Chat-Agenten erstellen

Ein Chat-Agent ist ein Chat-Assistent, den Sie auf ein Thema spezialisieren: ein DSB-Assistent, der nur aus dem Verarbeitungsverzeichnis antwortet, ein Einkaufsassistent, der Verträge von Dienstleistern prüft, oder ein Sicherheitsassistent, der bei der Einstufung eines Vorfalls hilft.

Öffnen Sie **Mandanteneinstellungen** > **KI-Agenten**, klicken Sie auf **Einen Agenten anlegen** und dann auf **Chat**.

***

## Allgemeines

Name und Beschreibung identifizieren den Agenten in der Liste und in der Agentenauswahl. Sie können ihm außerdem ein **Logo** geben, das in der Unterhaltung als sein Avatar erscheint.

Der Name ist auf 120 Zeichen begrenzt, die Beschreibung auf 1000.

## Einrichtung des Chats

<figure><img src="../../../../.gitbook/assets/ai-agents-editeur-conversationnel.png" alt="Editor eines Chat-Agenten mit der Chat-Vorschau"><figcaption><p>Der Editor eines Chat-Agenten, rechts die Chat-Vorschau</p></figcaption></figure>

### Begrüßungsnachricht

Die erste Nachricht, die dem Nutzer beim Öffnen der Unterhaltung angezeigt wird (höchstens 1000 Zeichen). Teilen Sie hier mit, was der Agent kann und was er nicht kann.

### Assistentenanweisung

Sie ist das Herzstück des Agenten: seine Persönlichkeit und seine Verhaltensregeln, auf **10.000 Zeichen** begrenzt.

{% hint style="info" %}
Ihre Anweisung ersetzt nicht den gesamten Prompt. Sie legt die Persona des Agenten fest. Dastra ergänzt automatisch eigene Regeln: das Produktvokabular, die Beschreibung der verfügbaren Tools und die Regeln des Modus **Frage** oder **Ausgabe**. Sie müssen also nicht erklären, was eine Verarbeitungstätigkeit ist oder wie ein Tool funktioniert.
{% endhint %}

Eine wirksame Anweisung nennt:

* **die Rolle**: „Sie sind der Datenschutzbeauftragte der Organisation.“
* **die maßgebliche Quelle**: „Antworten Sie immer anhand der im Mandanten gespeicherten Einträge: Suchen Sie vor der Antwort den passenden Eintrag und zitieren Sie ihn immer.“
* **was zu tun ist, wenn etwas fehlt**: „Wenn die Information im Mandanten nicht vorhanden ist, sagen Sie das ausdrücklich, statt sie zu erfinden.“
* **das erwartete Format**: Sprache, Länge, verpflichtende Angaben.

### Beispielanfragen

Die vorgeschlagenen Fragen unter der Begrüßungsnachricht. Sie wirken wie eine implizite Anleitung: Wählen Sie diejenigen, mit denen Sie die gewünschten Einsatzzwecke zeigen. Mit **Beispielanfrage hinzufügen** ergänzen Sie beliebig viele.

***

## Tools

Standardmäßig hat ein Agent Zugriff auf **alle** Tools. Antworten Sie auf die Frage **Möchten Sie die Liste der von diesem Agenten nutzbaren Tools anpassen?** mit **Ja**, um diese Liste einzuschränken.

<figure><img src="../../../../.gitbook/assets/ai-agents-outils.png" alt="Tool-Auswahl, aufgeteilt in Lesetools und Bearbeitungstools"><figcaption><p>Die Tools sind in Lesetools und Bearbeitungstools gruppiert</p></figcaption></figure>

Es gibt zwei Gruppen von Tools:

* **Lesetools**: den Mandanten durchsuchen, einen Eintrag lesen, Kommentare und Dateien lesen, die Dastra-Dokumentation und das Regelwerk durchsuchen, im Web suchen.
* **Bearbeitungstools**: Einträge erstellen und ändern, Kommentare hinzufügen, den Workflow-Status ändern, Aufgaben und Tags erstellen, Fragebögen planen und ausfüllen.

{% hint style="warning" %}
Die Einschränkung der Tools ist der sicherste Weg, einen Agenten in seinen Grenzen zu halten. Ein Assistent, der nur Fragen beantworten soll, braucht kein Bearbeitungstool: Geben Sie ihm keines.
{% endhint %}

## Nutzer wurden benachrichtigt

Die Personen, die eine Dastra-Benachrichtigung erhalten, wenn eine Ausführung des Agenten endet.

***

## Die Modi Frage und Ausgabe

In der Unterhaltung wechselt eine Auswahl zwischen zwei Modi:

* **Frage**: Der Agent hat nur Lesezugriff. Er kann suchen, lesen und analysieren, aber nichts wird geändert.
* **Ausgabe**: Der Agent kann Einträge erstellen und ändern. Bearbeitungstools sind nur in diesem Modus verfügbar.

Der Bearbeitungsmodus hängt von Ihrem Tarif und von der entsprechenden Berechtigung ab. Steht er Ihnen nicht zur Verfügung, erscheint die Auswahl nicht, und die Bearbeitungstools bleiben inaktiv, selbst wenn sie in der Agentendefinition angehakt sind.

***

## Vor der Veröffentlichung testen

Die **Chat-Übersicht** rechts im Editor ist eine echte Unterhaltung mit dem Agenten, genau so, wie er gerade konfiguriert ist. Prüfen Sie damit Tonfall, Länge der Antworten und die Einhaltung Ihrer Regeln, bevor Sie den Agenten aktivieren. Mit **Zurücksetzen** beginnen Sie eine neue Unterhaltung.

## Den Agenten im Alltag nutzen

Sobald der Agent aktiviert ist, erreichen ihn die Nutzer des Mandanten:

* über den Bereich **Dastra AI** unten rechts auf dem Bildschirm,
* mit der Tastenkombination **Strg+J** (auf dem Mac **Cmd+J**),
* über die Dastra-AI-Seite im Vollbildmodus.

Die Auswahl **Einen Mitarbeiter auswählen** oben in der Unterhaltung wechselt zwischen den Agenten.

<figure><img src="../../../../.gitbook/assets/ai-agents-chat.png" alt="Unterhaltung mit einem benutzerdefinierten Agenten mit Begrüßungsnachricht und Beispielanfragen"><figcaption><p>Der Agent zeigt seine Begrüßungsnachricht und seine Beispielanfragen</p></figcaption></figure>

Jede Antwort können Sie mit „Daumen hoch“ oder „Daumen runter“ und einem Kommentar bewerten. Dieses Feedback hilft Ihnen, die Anweisung des Agenten abzustimmen.

***

{% content-ref url="autonomous.md" %}
[Einen autonomen Agenten erstellen](autonomous.md)
{% endcontent-ref %}
