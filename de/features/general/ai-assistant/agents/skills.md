---
description: >-
  Speichern Sie Ihre wiederkehrenden Anweisungen als wiederverwendbare Befehle
  im Dastra-AI-Chat
---

# Kompetenzen

Eine **Kompetenz** (Skill) ist eine Anweisung, die Sie einmal speichern und dann per Befehl abrufen, indem Sie in der Unterhaltung `/` eingeben. Stellen Sie sie sich als Prompt-Vorlage vor, die in der gesamten Organisation geteilt wird.

Kompetenzen verwalten Sie unter **Mandanteneinstellungen** > **KI-Agenten** > **Skills**.

<figure><img src="../../../../.gitbook/assets/ai-agents-competences.png" alt="Liste der Dastra-AI-Kompetenzen"><figcaption><p>Der Tab Skills mit den integrierten Kompetenzen von Dastra</p></figcaption></figure>

***

## Integrierte Kompetenzen

Dastra liefert zwei Kompetenzen mit, die in jedem Mandanten verfügbar und nicht bearbeitbar sind:

| Befehl | Was er bewirkt |
| --- | --- |
| `/scaffold_agent` | Führt Sie durch den Entwurf eines benutzerdefinierten Agenten (Persona, Tools, Regeln) und speichert ihn, sobald Sie bestätigen. Diese Kompetenz startet die Option **Generate with Dastra AI** im Dialog zum Erstellen eines Agenten. |
| `/dpo_opinion` | Verwandelt die laufende Diskussion oder den Eintrag, den Sie gerade ansehen, in eine förmliche, archivierbare Stellungnahme des Datenschutzbeauftragten. |

## Eine eigene Kompetenz erstellen

Klicken Sie auf **Funktion erstellen** und füllen Sie dann aus:

* **Name**: die Bezeichnung, die in der Befehlsliste angezeigt wird.
* **Befehl**: der Text, der nach dem `/` eingegeben wird. Kleinbuchstaben mit Unterstrichen, **eindeutig innerhalb der Organisation**, zum Beispiel `steering_committee_summary`.
* **Beschreibung**: ein Satz, der erklärt, wann die Kompetenz zu verwenden ist. Er erscheint im Chat neben dem Befehl.
* **Prompt**: die Anweisung, die an den Assistenten gesendet wird, bis zu 10.000 Zeichen.
* **Mit dem Unternehmen teilen**: Lassen Sie die Kompetenz nur für sich selbst oder teilen Sie sie mit den anderen Mitgliedern des Mandanten.

## Eine Kompetenz verwenden

Geben Sie in einer Dastra-AI-Unterhaltung `/` ein: Die Liste der verfügbaren Kompetenzen erscheint. Wählen Sie eine aus, ergänzen Sie bei Bedarf Ihre Nachricht und senden Sie sie ab.

{% hint style="info" %}
Eine Kompetenz gilt für die aktuelle Unterhaltung, mit dem Agenten und dem Modus (**Frage** oder **Ausgabe**), die gerade ausgewählt sind. Eine Kompetenz, die Einträge ändern muss, erfordert daher den Modus **Ausgabe**.
{% endhint %}

***

## Kompetenz und Agent im Vergleich

Beide lassen Sie eine Anweisung wiederverwenden, aber nicht zum selben Zeitpunkt:

* Eine **Kompetenz** ist ein Einzelaufruf. Sie lösen sie mitten in einer Unterhaltung aus, mit dem Kontext, der gerade vorliegt.
* Ein **Agent** ist dauerhaft. Er hat eine eigene Identität, eigene Tools und gegebenenfalls einen eigenen Zeitplan.

Wenn Sie dieselbe Anfrage immer wieder eintippen, erstellen Sie eine Kompetenz. Wenn Sie ein spezialisiertes Gegenüber oder eine automatisierte Aufgabe wünschen, erstellen Sie einen [Agenten](README.md).
